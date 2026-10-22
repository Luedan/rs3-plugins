import os

for letter in ['S', 'A']:
    d = os.path.join('runescape-dialogue-translator', 'data', 'dialogs_en', letter)
    for f in os.listdir(d):
        if 'smith' in f.lower() or 'apprentice' in f.lower():
            print(f"{letter}: {f}")
