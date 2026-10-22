import os

walk_dir = r'D:\programacion\REPOS\rs-plugins\plugins\rs-translator\src\data'
br_count = 0
for f in os.listdir(walk_dir):
    if f.startswith('dialogues_') and f.endswith('.lua'):
        with open(os.path.join(walk_dir, f), 'r', encoding='utf-8') as fp:
            c = fp.read()
            br_count += c.count('<br')

print(f"Total <br in generated Lua files: {br_count}")
