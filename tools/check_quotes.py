import os

walk_dir = r'D:\programacion\REPOS\rs-plugins\plugins\rs-translator\src\data'
curly_count = 0
ascii_count = 0
for f in os.listdir(walk_dir):
    if f.startswith('dialogues_') and f.endswith('.lua'):
        with open(os.path.join(walk_dir, f), 'r', encoding='utf-8') as fp:
            c = fp.read()
            curly_count += c.count('’') + c.count('‘') + c.count('“') + c.count('”')
            ascii_count += c.count("'") + c.count('"')

print(f"In generated Lua files: curly quotes={curly_count}, ascii quotes={ascii_count}")
