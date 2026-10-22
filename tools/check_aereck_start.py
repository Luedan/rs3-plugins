with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_en\F\Father Aereck.md', 'r', encoding='utf-8') as f:
    en_lines = f.readlines()
with open(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_es\F\Father Aereck.md', 'r', encoding='utf-8') as f:
    es_lines = f.readlines()

print("EN lines 1-25:")
for i in range(25):
    print(f"{i+1}: {repr(en_lines[i])}")

print("\nES lines 1-25:")
for i in range(25):
    print(f"{i+1}: {repr(es_lines[i])}")
