with open('plugins/rs-translator/src/data/quest_dialogue_steps.lua', 'r', encoding='utf-8') as f:
    c = f.read()
    u_idx = c.find('QuestSteps.universal = {')
    u_end = c.find('}', u_idx)
    u_text = c[u_idx:u_end+1]
    print(u_text)
    for bad in ['["yes"]', '["si"]', '["sí"]', '["no"]', '["chat"]', '["goodbye"]']:
        if bad in u_text:
            print("ALERT: Found", bad)
        else:
            print("OK: Clean of", bad)
