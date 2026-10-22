import json, re

with open('tools/quests_and_steps.json', 'r', encoding='utf-8') as f:
    quests = json.load(f)

# Load existing translations
trans_map = {}
import glob
for f in glob.glob('plugins/rs-translator/src/data/dialogues_*.lua'):
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
        for m in re.finditer(r'\["([^"]+)"\]\s*=\s*"([^"]+)"', text):
            en = m.group(1).strip()
            es = m.group(2).strip()
            if en not in trans_map:
                trans_map[en] = es

with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as fh:
    text = fh.read()
    for m in re.finditer(r'\["([^"]+)"\]\s*=\s*"([^"]+)"', text):
        en = m.group(1).strip()
        es = m.group(2).strip()
        if en not in trans_map:
            trans_map[en] = es

# Find all steps
all_steps = set()
for q, steps in quests.items():
    for s in steps:
        all_steps.add(s)

missing = []
for s in sorted(all_steps):
    if s not in trans_map:
        missing.append(s)

print(f"Total steps: {len(all_steps)}")
print(f"Existing translated: {len(all_steps) - len(missing)}")
print(f"Missing: {len(missing)}")

with open('tools/missing_step_translations.txt', 'w', encoding='utf-8') as f:
    for s in missing:
        f.write(s + '\n')
