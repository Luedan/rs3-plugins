with open(r'D:\programacion\REPOS\rs-plugins\plugins\rs-translator\src\data\dialogues_H.lua', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'veteran' in line.lower() or 'cape' in line.lower() or 'eligible' in line.lower():
            print(f"{i+1}: {line.strip()[:120]}")
