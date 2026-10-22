with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_en\H\Hans.md', 'r', encoding='utf-8') as f:
    en_body = f.read().split('---', 1)[1]
with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_es\H\Hans.md', 'r', encoding='utf-8') as f:
    es_body = f.read().split('---', 1)[1]

en_lines = en_body.splitlines()
es_lines = es_body.splitlines()
print(f"EN lines: {len(en_lines)}, ES lines: {len(es_lines)}")

import difflib
matcher = difflib.SequenceMatcher(None, [l.strip() for l in en_lines], [l.strip() for l in es_lines])
for tag, i1, i2, j1, j2 in matcher.get_opcodes():
    if tag != 'equal':
        print(f"\nOp: {tag} EN[{i1}:{i2}] vs ES[{j1}:{j2}]")
        print("EN:", en_lines[i1:i2])
        print("ES:", es_lines[j1:j2])
