# -*- coding: utf-8 -*-
import re

# Load quest_dialogue_steps.lua directly and parse it
with open('plugins/rs-translator/src/data/quest_dialogue_steps.lua', 'r', encoding='utf-8') as f:
    lua_code = f.read()

# Extract universal
universal = {}
u_m = re.search(r'QuestSteps\.universal = \{([^}]+)\}', lua_code, re.DOTALL)
if u_m:
    for line in u_m.group(1).split('\n'):
        sm = re.search(r'\["([^"]+)"\]\s*=\s*true', line)
        if sm:
            universal[sm.group(1)] = True

# Extract byQuest
by_quest = {}
bq_m = re.search(r'QuestSteps\.byQuest = \{(.*)\nQuestSteps\.longSteps', lua_code, re.DOTALL)
if bq_m:
    cur_q = None
    for line in bq_m.group(1).split('\n'):
        qm = re.search(r'\["([^"]+)"\]\s*=\s*\{', line)
        if qm:
            cur_q = qm.group(1)
            by_quest[cur_q] = {}
        elif cur_q:
            sm = re.search(r'\["([^"]+)"\]\s*=\s*true', line)
            if sm:
                by_quest[cur_q][sm.group(1)] = True

# Extract longSteps
long_steps = {}
ls_m = re.search(r'QuestSteps\.longSteps = \{([^}]+)\}', lua_code, re.DOTALL)
if ls_m:
    for line in ls_m.group(1).split('\n'):
        sm = re.search(r'\["([^"]+)"\]\s*=\s*true', line)
        if sm:
            long_steps[sm.group(1)] = True

print(f"Universal count: {len(universal)}")
print(f"ByQuest quests count: {len(by_quest)}")
print(f"LongSteps count: {len(long_steps)}")

def norm(s):
    if not s: return ""
    s = re.sub(r'<[^>]*>', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s

def strip_punct(s):
    s = re.sub(r'^[¡¿]', '', s)
    s = re.sub(r'[!?:;.,]$', '', s).strip()
    return s

def strip_number_prefix(s):
    if not s: return ""
    clean = re.sub(r'<[^>]*>', '', s)
    m = re.match(r'^\d+[\.:\-]?\s*(.*)$', clean) or re.match(r'^\[\d+\]\s*(.*)$', clean)
    bare = m.group(1) if m else clean
    return bare.strip()

def matches_quest_step(text, active_quest=None):
    if not text: return False
    clean = strip_number_prefix(text)
    n_clean = norm(clean)
    if not n_clean: return False
    bare = strip_punct(n_clean)

    # 1. Universal
    if n_clean in universal or (bare and bare in universal):
        return True

    # 2. Active quest
    if active_quest:
        nq = norm(active_quest)
        q_steps = by_quest.get(nq)
        if q_steps:
            if n_clean in q_steps or (bare and bare in q_steps):
                return True

    # 3. Fallback: long steps only (>= 15 chars)
    if not active_quest and len(bare) >= 15:
        if n_clean in long_steps or (bare and bare in long_steps):
            return True

    return False

test_cases = [
    # (text, active_quest, expected, description)
    ("1. Sí, he visto Lachtopher.", "The Restless Ghost", False, "Victoria line about Lachtopher with active quest"),
    ("1. Sí, he visto Lachtopher.", None, False, "Victoria line without active quest"),
    ("1. No, no lo he visto.", "The Restless Ghost", False, "Victoria line 2"),
    ("1. I'm looking for a quest!", None, True, "Universal quest starter EN"),
    ("1. ¡Estoy buscando una misión!", None, True, "Universal quest starter ES"),
    ("1. Estoy buscando una mision", None, True, "Universal quest starter ES without accent"),
    ("1. Yes.", "The Restless Ghost", True, "Restless ghost step EN"),
    ("1. Sí.", "The Restless Ghost", True, "Restless ghost step ES"),
    ("1. Sí", "The Restless Ghost", True, "Restless ghost step ES no dot"),
    ("1. Father Aereck sent me to talk to you.", "The Restless Ghost", True, "Father Urhney step EN"),
    ("1. El padre Aereck me envió a hablar contigo.", "The Restless Ghost", True, "Father Urhney step ES"),
    ("1. Yes.", "A Shadow over Ashdale", True, "Ashdale also has Yes."),
    ("1. Yes.", "Cook's Assistant", False, "Cook's Assistant does not have Yes."),
    ("1. Sí, me gustaría comprar algo.", "The Restless Ghost", False, "Shopkeeper line"),
    ("1. Chat.", "The Restless Ghost", False, "Banker/Bartender chat line"),
    ("1. Goodbye.", "The Restless Ghost", False, "Goodbye line"),
    ("WHAT WOULD YOU LIKE TO SAY?", None, False, "Interface title - not a step"),
    ("A ghost is haunting his graveyard.", None, True, "Long step without active quest (>= 15 chars)"),
]

passed = 0
for text, aq, exp, desc in test_cases:
    res = matches_quest_step(text, aq)
    if res == exp:
        print(f"PASS: [{desc}] -> {res}")
        passed += 1
    else:
        print(f"FAIL: [{desc}] -> Got {res}, expected {exp}")

print(f"\n{passed}/{len(test_cases)} tests passed.")
assert passed == len(test_cases)
