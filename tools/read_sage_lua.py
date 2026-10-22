with open('plugins/rs-translator/src/data/dialogues_L.lua', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('["Lumbridge Sage"] = {')
if idx != -1:
    end_idx = c.find('\n    },', idx)
    print(c[idx:end_idx][:2500])
else:
    print("Lumbridge Sage not found in dialogues_L.lua")
