with open('plugins/rs-translator/src/data/dialogues_H.lua', 'r', encoding='utf-8') as f:
    c = f.read()
    idx = c.find('["Hans"] = {')
    if idx != -1:
        print(c[idx:idx+2500])
    else:
        print("Hans not found in dialogues_H.lua")
