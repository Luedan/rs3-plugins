import os

for letter in ['C', 'A', 'D', 'G', 'M', 'N']:
    d = os.path.join('runescape-dialogue-translator', 'data', 'dialogs_en', letter)
    if os.path.exists(d):
        for f in os.listdir(d):
            low = f.lower()
            if any(k in low for k in ['cook', 'apprentice', 'donnie', 'gee', 'guard', 'mikasi', 'nemarti']):
                print(f"{letter}: {f}")
