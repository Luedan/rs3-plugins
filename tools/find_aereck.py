import os

for root, dirs, files in os.walk(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator'):
    for f in files:
        if 'aereck' in f.lower() or 'restless' in f.lower():
            print(os.path.join(root, f))
