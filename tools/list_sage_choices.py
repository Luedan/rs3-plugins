import re

with open('runescape-dialogue-translator/data/dialogs_en/L/Lumbridge Sage.md', 'r', encoding='utf-8') as f:
    text_en = f.read()

choices = re.findall(r'\[Choice\]:\s*(.*)', text_en)
print(f"Total choices in Lumbridge Sage: {len(choices)}")
for c in choices:
    print(" -", c)
