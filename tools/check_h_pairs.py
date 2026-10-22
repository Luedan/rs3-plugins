with open(r'D:\programacion\REPOS\rs-plugins\plugins\rs-translator\src\data\dialogues_H.lua', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(1, 100):
        if i < len(lines):
            print(lines[i][:120].strip())
