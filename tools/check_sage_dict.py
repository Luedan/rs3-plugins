with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as f:
    c = f.read()

print('Jacquelyn in dictionary.lua:', 'Jacquelyn' in c or 'jacquelyn' in c)

with open('plugins/rs-translator/src/data/dialogues_L.lua', 'r', encoding='utf-8') as f:
    cL = f.read()

print('Jacquelyn in dialogues_L.lua:', 'Jacquelyn' in cL or 'jacquelyn' in cL)
