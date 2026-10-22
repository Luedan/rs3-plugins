with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_en\H\Hans.md', 'r', encoding='utf-8') as f:
    en_lines = f.readlines()

with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_es\H\Hans.md', 'r', encoding='utf-8') as f:
    es_lines = f.readlines()

print("EN length:", len(en_lines), "ES length:", len(es_lines))

for i in range(min(len(en_lines), 60)):
    if 'cond=' in en_lines[i] or 'cond=' in es_lines[i] or 'Condition' in en_lines[i] or 'Condition' in es_lines[i]:
        print(f"L{i+1} EN: {en_lines[i].strip()}")
        print(f"L{i+1} ES: {es_lines[i].strip()}")
