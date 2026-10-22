import zipfile, re, json

zip_path = r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip'
all_quests = {}

with zipfile.ZipFile(zip_path, 'r') as z:
    for name in z.namelist():
        if name.startswith('quests/') and name.endswith('.lua'):
            content = z.read(name).decode('utf-8', errors='ignore')
            # Extract quest name
            quest_name_m = re.search(r'QuestHelper:new\("([^"]+)"', content)
            if not quest_name_m:
                continue
            quest_name = quest_name_m.group(1)
            
            steps = []
            for m in re.finditer(r'addDialogStep(?:WithExclusion[s]?)?\(\s*"([^"]+)"', content):
                s = m.group(1)
                if s not in steps:
                    steps.append(s)
            if steps:
                all_quests[quest_name] = steps

print(f"Extracted {len(all_quests)} quests.")

# Generate Lua file
lua_lines = [
    '--- Autogenerado a partir de Quest Helper (compatibilidad total de resaltado cian)',
    'local QuestSteps = {}',
    '',
    'QuestSteps.byQuest = {'
]

for qname, steps in sorted(all_quests.items()):
    lua_lines.append(f'    ["{qname}"] = {{')
    for s in steps:
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        lua_lines.append(f'        "{escaped}",')
    lua_lines.append('    },')

lua_lines.append('}')
lua_lines.append('')
lua_lines.append('-- Pasos universales de inicio de misiones en RS3')
lua_lines.append('QuestSteps.universal = {')
lua_lines.append('    "i\'m looking for a quest!",')
lua_lines.append('    "i am looking for a quest!",')
lua_lines.append('    "have you got any quests for me?",')
lua_lines.append('    "do you have a quest for me?",')
lua_lines.append('    "accept quest",')
lua_lines.append('    "yes.",')
lua_lines.append('    "yes",')
lua_lines.append('}')
lua_lines.append('')
lua_lines.append('return QuestSteps')

out_path = 'plugins/rs-translator/src/data/quest_dialogue_steps.lua'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lua_lines))

print(f"Generated {out_path} successfully.")
