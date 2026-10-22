import glob, re

npcs_to_check = [
    "Bob", "Hans", "Father Aereck", "Duke Horacio", "Cook", "Gee", 
    "Explorer Jack", "Donnie", "Fred the Farmer", "Gillie Groats", 
    "Guard", "Man", "Woman", "Doomsayer", "Father Urhney", "Restless ghost"
]

found_npcs = {}
for f in glob.glob('plugins/rs-translator/src/data/dialogues_*.lua'):
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
        for npc in npcs_to_check:
            key = f'["{npc}"] = {{'
            if key in c:
                # count lines
                idx = c.find(key)
                end_idx = c.find('\n    },', idx)
                snippet = c[idx:end_idx]
                lines_count = len(re.findall(r'\["[^"]+"\]\s*=', snippet))
                found_npcs[npc] = (f, lines_count)

for npc in npcs_to_check:
    if npc in found_npcs:
        print(f"FOUND: {npc} in {found_npcs[npc][0]} with {found_npcs[npc][1]} lines")
    else:
        print(f"MISSING: {npc}")
