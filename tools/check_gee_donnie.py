import os

for letter, name in [('G', 'Gee'), ('D', 'Donnie')]:
    en_path = os.path.join('runescape-dialogue-translator', 'data', 'dialogs_en', letter, f'{name}.md')
    es_path = os.path.join('runescape-dialogue-translator', 'data', 'dialogs_es', letter, f'{name}.md')
    print(f"{name}: EN={os.path.exists(en_path)}, ES={os.path.exists(es_path)}")
    if os.path.exists(en_path):
        with open(en_path, 'r', encoding='utf-8') as f:
            print(f"EN lines: {len(f.readlines())}")
    if os.path.exists(es_path):
        with open(es_path, 'r', encoding='utf-8') as f:
            print(f"ES lines: {len(f.readlines())}")
