with open('plugins/rs-translator/src/data/dialogues_L.lua', 'r', encoding='utf-8') as f:
    cL = f.read()

for alias in ["Lumbridge Guide", "Sage"]:
    print(f'["{alias}"] in L:', f'["{alias}"] = {{' in cL)
