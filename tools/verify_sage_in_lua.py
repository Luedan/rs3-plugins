with open('plugins/rs-translator/src/data/dialogues_L.lua', 'r', encoding='utf-8') as f:
    cL = f.read()

print('Jacquelyn in dialogues_L.lua:', 'Jacquelyn' in cL)
idx = cL.find('Jacquelyn')
if idx != -1:
    print(cL[idx-30:idx+250])
