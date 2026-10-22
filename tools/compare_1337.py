with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_en\#\1337mage43.md', 'r', encoding='utf-8') as f:
    en_lines = f.readlines()
with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_es\#\1337mage43.md', 'r', encoding='utf-8') as f:
    es_lines = f.readlines()

print("EN lines:")
for i, l in enumerate(en_lines):
    print(f"{i+1}: {repr(l)}")

print("\nES lines:")
for i, l in enumerate(es_lines):
    print(f"{i+1}: {repr(l)}")
