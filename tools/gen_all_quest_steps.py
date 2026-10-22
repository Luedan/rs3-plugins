import zipfile, re

zip_path = r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip'
all_quests = {}
all_steps_set = set()

with zipfile.ZipFile(zip_path, 'r') as z:
    for name in z.namelist():
        if name.startswith('quests/') and name.endswith('.lua'):
            content = z.read(name).decode('utf-8', errors='ignore')
            m = re.search(r'QuestHelper:new\("([^"]+)"', content)
            if not m:
                continue
            qname = m.group(1)
            steps = []
            for sm in re.finditer(r'addDialogStep(?:WithExclusion[s]?)?\(\s*"([^"]+)"', content):
                s = sm.group(1)
                if s not in steps:
                    steps.append(s)
                all_steps_set.add(s)
            if steps:
                all_quests[qname] = steps

# Load all dialogues to find translations for these steps
dialogue_translations = {}
import glob
for f in glob.glob('plugins/rs-translator/src/data/dialogues_*.lua'):
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
        for step in all_steps_set:
            if step not in dialogue_translations:
                key = f'["{step}"] = "'
                idx = text.find(key)
                if idx != -1:
                    end_idx = text.find('"', idx + len(key))
                    if end_idx != -1:
                        dialogue_translations[step] = text[idx + len(key):end_idx]

print(f"Total steps: {len(all_steps_set)}, Translated steps: {len(dialogue_translations)}")

lua_lines = [
    '--- Autogenerado a partir de Quest Helper (compatibilidad total de resaltado cian)',
    'local QuestSteps = {}',
    '',
    'QuestSteps.universal = {',
    '    ["i\'m looking for a quest!"] = true,',
    '    ["¡estoy buscando una misión!"] = true,',
    '    ["estoy buscando una mision"] = true,',
    '    ["i am looking for a quest!"] = true,',
    '    ["have you got any quests for me?"] = true,',
    '    ["¿tienes alguna misión para mí?"] = true,',
    '    ["tienes alguna mision para mi"] = true,',
    '    ["do you have a quest for me?"] = true,',
    '    ["accept quest"] = true,',
    '    ["aceptar misión"] = true,',
    '    ["aceptar mision"] = true,',
    '    ["yes."] = true,',
    '    ["sí."] = true,',
    '    ["si."] = true,',
    '    ["yes"] = true,',
    '    ["sí"] = true,',
    '    ["si"] = true,',
    '}',
    '',
    'QuestSteps.allSteps = {'
]

for s in sorted(all_steps_set):
    escaped = s.lower().replace('\\', '\\\\').replace('"', '\\"')
    lua_lines.append(f'    ["{escaped}"] = true,')
    if s in dialogue_translations:
        es_s = dialogue_translations[s].lower().replace('\\', '\\\\').replace('"', '\\"')
        lua_lines.append(f'    ["{es_s}"] = true,')

lua_lines.append('}')
lua_lines.append('')
lua_lines.append('return QuestSteps')

out_path = 'plugins/rs-translator/src/data/quest_dialogue_steps.lua'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lua_lines))

print(f"Generated {out_path} with {len(all_steps_set)} English steps and translations.")
