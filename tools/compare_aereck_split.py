with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_en\F\Father Aereck.md', 'r', encoding='utf-8') as f:
    en_parts = f.read().split('---', 1)
with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_es\F\Father Aereck.md', 'r', encoding='utf-8') as f:
    es_parts = f.read().split('---', 1)

en_lines = [l.strip() for l in en_parts[1].splitlines()]
es_lines = [l.strip() for l in es_parts[1].splitlines()]

print(f"en_lines count: {len(en_lines)}, es_lines count: {len(es_lines)}")

for i in range(len(en_lines)):
    if i < len(es_lines):
        if en_lines[i] != es_lines[i]:
            print(f"{i:2d} EN: {en_lines[i]}")
            print(f"{i:2d} ES: {es_lines[i]}")
            print()
