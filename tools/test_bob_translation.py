# -*- coding: utf-8 -*-
import re

# Simulate the exact Lua DialogueLoader logic
def norm_quotes(s):
    if not s: return ""
    return s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('…', '...')

def norm_tokens(s):
    if not s: return ""
    q = norm_quotes(s).lower()
    q = re.sub(r'<[^>]*>', ' ', q)
    q = re.sub(r'[\.,!\?;:\'\"…\-\–\—\(\)\[\]/\\|]', ' ', q)
    words = []
    for w in q.split():
        if len(w) > 4 and w.endswith('es'):
            w = w[:-2]
        elif len(w) > 4 and w.endswith('s'):
            w = w[:-1]
        words.append(w)
    return ' '.join(words)

def get_word_set(s):
    if not s: return set(), 0
    q = norm_quotes(s).lower()
    q = re.sub(r'<[^>]*>', ' ', q)
    q = re.sub(r'[\.,!\?;:\'\"…\-\–\—\(\)\[\]/\\|]', ' ', q)
    words = set([w for w in q.split() if len(w) >= 3])
    return words, len(words)

def compute_similarity(s1, c1, s2, c2):
    if c1 == 0 or c2 == 0: return 0.0
    inter = len(s1 & s2)
    union = c1 + c2 - inter
    if union <= 0: return 0.0
    return inter / union

def lookup_npc_fuzzy(npc_table, text):
    if not npc_table or not text or len(text) < 4: return None
    n_text = norm_tokens(text)
    if not n_text: return None

    # Nivel 1: Tokens / Plurales
    for orig, trans in npc_table.items():
        if norm_tokens(orig) == n_text:
            return trans

    # Nivel 2: Similitud
    if len(text) >= 15:
        target_set, target_cnt = get_word_set(text)
        if target_cnt >= 3:
            best_match = None
            best_score = 0.82
            for orig, trans in npc_table.items():
                len_diff = abs(len(orig) - len(text))
                if len_diff < len(text) * 0.40:
                    cand_set, cand_cnt = get_word_set(orig)
                    sim = compute_similarity(target_set, target_cnt, cand_set, cand_cnt)
                    if sim > best_score:
                        best_score = sim
                        best_match = trans
            if best_match:
                return best_match
    return None

# Load Bob's table from dialogues_B.lua
with open('plugins/rs-translator/src/data/dialogues_B.lua', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('["Bob"] = {')
end_idx = c.find('\n    },', idx)
bob_block = c[idx:end_idx]

bob_table = {}
for m in re.finditer(r'\["([^"]+)"\]\s*=\s*"([^"]+)"', bob_block):
    bob_table[m.group(1)] = m.group(2)

print(f"Loaded {len(bob_table)} entries for Bob.")

# Test exact screenshot text
screenshot_text = "Great! I buy and sell pickaxes and hatchets. There are plenty to choose from, and I've some free samples too. Take your pick...or hatchet."

# 1. Test direct match
direct = bob_table.get(screenshot_text)
print("Direct match:", direct)

# 2. Test fuzzy match if direct fails
fuzzy = lookup_npc_fuzzy(bob_table, screenshot_text)
print("Fuzzy match: ", fuzzy)

assert direct is not None or fuzzy is not None
print("\nTEST PASSED: Bob's dialogue in screenshot translates successfully!")
