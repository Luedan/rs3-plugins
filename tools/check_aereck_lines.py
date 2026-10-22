with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_en\F\Father Aereck.md', 'r', encoding='utf-8') as f:
    en_lines = f.readlines()
with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_es\F\Father Aereck.md', 'r', encoding='utf-8') as f:
    es_lines = f.readlines()

print("EN lines 25-45:")
for i in range(24, 45):
    print(f"{i+1}: {repr(en_lines[i])}")

print("\nES lines 25-45:")
for i in range(24, 45):
    print(f"{i+1}: {repr(es_lines[i])}")
