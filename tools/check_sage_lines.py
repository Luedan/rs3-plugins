import re

with open('runescape-dialogue-translator/data/dialogs_en/L/Lumbridge Sage.md', 'r', encoding='utf-8') as f:
    text_en = f.read()

with open('runescape-dialogue-translator/data/dialogs_es/L/Lumbridge Sage.md', 'r', encoding='utf-8') as f:
    text_es = f.read()

# Extract all lines spoken by Lumbridge Sage or choices
lines_en = re.findall(r'\*\*Lumbridge Sage:\*\*\s*(.*)', text_en)
choices_en = re.findall(r'\[Choice\]:\s*(.*)', text_en)

print(f"Lumbridge Sage in MD: {len(lines_en)} spoken lines, {len(choices_en)} choices")
for l in lines_en[:15]:
    print(" -", l[:80])
