import re

def norm_tokens(s):
    if not s: return ""
    s = s.lower()
    # Normalize unicode quotes and ellipsis
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('…', '...')
    # Remove punctuation
    s = re.sub(r'[\.\,\!\?\;\:\'\"…\-\–\—\(\)\[\]]', ' ', s)
    tokens = s.split()
    stemmed = []
    for t in tokens:
        if len(t) > 4 and t.endswith('es'):
            stemmed.append(t[:-2])
        elif len(t) > 4 and t.endswith('s'):
            stemmed.append(t[:-1])
        else:
            stemmed.append(t)
    return ' '.join(stemmed)

def word_set(s):
    if not s: return set()
    s = s.lower()
    s = re.sub(r'[\.\,\!\?\;\:\'\"…\-\–\—\(\)\[\]]', ' ', s)
    tokens = [w for w in s.split() if len(w) >= 2]
    return set(tokens)

def word_similarity(w1, w2):
    if not w1 or not w2: return 0.0
    inter = len(w1 & w2)
    union = len(w1 | w2)
    return inter / union

# Test with Bob
bob_game = "Great! I buy and sell pickaxes and hatchets. There are plenty to choose from, and I've some free samples too. Take your pick...or hatchet."
bob_wiki = "Great! I buy and sell pickaxes and hatchet. There are plenty to choose from, and I've some free samples too. Take your pick...or hatchet."

print("Tier 2 Match (Tokens):", norm_tokens(bob_game) == norm_tokens(bob_wiki))
w_game = word_set(bob_game)
w_wiki = word_set(bob_wiki)
print("Tier 3 Match (Sim):   ", word_similarity(w_game, w_wiki))
