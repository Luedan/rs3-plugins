with open('plugins/rs-translator/src/data/quest_dialogue_steps.lua', 'r', encoding='utf-8') as f:
    c = f.read()
    idx = c.find('["the restless ghost"] = {')
    if idx != -1:
        print(c[idx:idx+800])
