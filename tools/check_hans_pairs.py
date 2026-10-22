with open(r'D:\programacion\REPOS\rs-plugins\plugins\rs-translator\src\data\dialogues_H.lua', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    in_hans = False
    for i, line in enumerate(lines):
        if '["Hans"] = {' in line:
            in_hans = True
        elif in_hans and line.startswith('    },'):
            in_hans = False
            print(f"Hans ended at line {i+1}")
            break
        if in_hans:
            print(line[:120].strip())
