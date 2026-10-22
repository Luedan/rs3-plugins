with open('runescape-dialogue-translator/data/dialogs_en/L/Lumbridge Sage.md', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.split('\n'):
    if 'jacquelyn' in line.lower() or 'monsters' in line.lower() or 'courtyard' in line.lower() or 'slayer' in line.lower():
        print(line)
