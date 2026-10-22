import os

walk_dir = r'D:\programacion\REPOS\rs-plugins\plugins\rs-translator\data\dialogs_en'
for root, dirs, files in os.walk(walk_dir):
    for f in files:
        if f.endswith('.md'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
                if "looking for a quest" in content.lower():
                    print("Found in EN:", f)

walk_dir_es = r'D:\programacion\REPOS\rs-plugins\plugins\rs-translator\data\dialogs_es'
for root, dirs, files in os.walk(walk_dir_es):
    for f in files:
        if f.endswith('.md'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
                if "looking for a quest" in content.lower() or "buscando una" in content.lower():
                    print("Found in ES:", f)
