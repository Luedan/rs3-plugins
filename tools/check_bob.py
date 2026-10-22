with open('plugins/rs-translator/src/data/dialogues_B.lua', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('["Bob"] = {')
if idx != -1:
    print(c[idx:idx+1500])
else:
    print("Bob not found in dialogues_B.lua!")
