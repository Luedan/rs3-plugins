with open(r'D:\programacion\REPOS\rs-plugins\plugins\rs-translator\src\data\dialogues_F.lua', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'father aereck' in line.lower() or 'lucky' in line.lower() or 'church of holy' in line.lower():
            print(f"{i+1}: {line[:120]}")
