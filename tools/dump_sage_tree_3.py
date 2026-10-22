import re

with open('runescape-dialogue-translator/data/dialogs_en/L/Lumbridge Sage.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = re.findall(r'(\*\*Lumbridge Sage:\*\*.*|\[Choice\]:.*|\[Menu\]:.*)', text)
for l in lines[100:]:
    print(l)
