import re

with open('runescape-dialogue-translator/data/dialogs_en/L/Lumbridge Sage.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Print lines with Lumbridge Sage
lines = re.findall(r'(\*\*Lumbridge Sage:\*\*.*|\[Choice\]:.*|\[Menu\]:.*)', text)
print(f"Total lines in Sage: {len(lines)}")
for l in lines[:40]:
    print(l)
