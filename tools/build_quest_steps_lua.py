# -*- coding: utf-8 -*-
import json, re, glob

# 1. Load quests and steps
with open('tools/quests_and_steps.json', 'r', encoding='utf-8') as f:
    quests = json.load(f)

# 2. Load translations from all sources
all_translations = {}

# From dialogues_*.lua
for f in glob.glob('plugins/rs-translator/src/data/dialogues_*.lua'):
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
        for m in re.finditer(r'\["([^"]+)"\]\s*=\s*"([^"]+)"', text):
            en = m.group(1).strip()
            es = m.group(2).strip()
            if en not in all_translations:
                all_translations[en] = es

# From dictionary.lua
with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as fh:
    text = fh.read()
    for m in re.finditer(r'\["([^"]+)"\]\s*=\s*"([^"]+)"', text):
        en = m.group(1).strip()
        es = m.group(2).strip()
        if en not in all_translations:
            all_translations[en] = es

# From step_translations.json
with open('tools/step_translations.json', 'r', encoding='utf-8') as f:
    custom_trans = json.load(f)
    for en, es in custom_trans.items():
        all_translations[en] = es

def norm(s):
    if not s:
        return ""
    s = re.sub(r'<[^>]*>', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s

def strip_punct(s):
    s = re.sub(r'^[¡¿]', '', s)
    s = re.sub(r'[!?:;.,]$', '', s).strip()
    return s

def norm_qname(qname):
    return norm(qname)

def generate_variations(s):
    vars_set = set()
    ns = norm(s)
    if not ns: return vars_set
    bare = strip_punct(ns)
    vars_set.add(ns)
    vars_set.add(bare)

    # If has Father/Padre
    if "father " in ns:
        vars_set.add(ns.replace("father ", "el padre "))
        vars_set.add(ns.replace("father ", "padre "))
        vars_set.add(bare.replace("father ", "el padre "))
        vars_set.add(bare.replace("father ", "padre "))
    if "brother " in ns:
        vars_set.add(ns.replace("brother ", "el hermano "))
        vars_set.add(ns.replace("brother ", "hermano "))
        vars_set.add(bare.replace("brother ", "el hermano "))
        vars_set.add(bare.replace("brother ", "hermano "))

    # Accents variations for Spanish (á/a, é/e, í/i, ó/o, ú/u, ñ/n)
    unaccented = ns.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    if unaccented != ns:
        vars_set.add(unaccented)
        vars_set.add(strip_punct(unaccented))

    return vars_set

# 3. Universal quest steps (ONLY clear quest-starting prompts, NEVER 'yes', 'no', 'si')
universal_en = [
    "i'm looking for a quest!",
    "i am looking for a quest!",
    "i'm looking for a quest",
    "i'm in search of a quest",
    "i am in search of a quest",
    "have you got any quests for me?",
    "have you got any quests for me",
    "do you have a quest for me?",
    "do you have any quests for me?",
    "do you have any jobs for me?",
    "accept quest",
    "[accept quest]",
    "accept Quest",
    "can i help at all?",
    "is there any way i could help?",
    "is there anything else i can help with?",
    "tell me of this quest.",
    "tell me of this quest",
    "go on an adventure",
    "to go on an adventure."
]

universal_es = [
    "¡estoy buscando una misión!",
    "estoy buscando una misión!",
    "estoy buscando una misión",
    "estoy buscando una mision",
    "estoy en busca de una misión",
    "estoy en busca de una mision",
    "¿tienes alguna misión para mí?",
    "tienes alguna misión para mí?",
    "¿tienes alguna mision para mi?",
    "tienes alguna mision para mi",
    "¿tienes una misión para mí?",
    "¿tienes algún trabajo para mí?",
    "aceptar misión",
    "aceptar mision",
    "[aceptar misión]",
    "[aceptar mision]",
    "¿puedo ayudar en algo?",
    "¿hay alguna manera en que pueda ayudar?",
    "¿hay algo más en lo que pueda ayudar?",
    "cuéntame sobre esta misión.",
    "cuéntame sobre esta misión",
    "ir a una aventura",
    "ir a una aventura."
]

universal_set = set()
for s in universal_en + universal_es:
    for v in generate_variations(s):
        universal_set.add(v)

# 4. By-quest steps
by_quest = {}
long_steps_set = set()

for qname, steps in quests.items():
    nq = norm_qname(qname)
    step_dict = set()
    for s in steps:
        for v in generate_variations(s):
            step_dict.add(v)
            if len(strip_punct(v)) >= 15:
                long_steps_set.add(v)

        # Translation
        trans = all_translations.get(s)
        if not trans:
            for k, v in all_translations.items():
                if k.lower() == s.lower():
                    trans = v
                    break
        if trans:
            for v in generate_variations(trans):
                step_dict.add(v)
                if len(strip_punct(v)) >= 15:
                    long_steps_set.add(v)

    by_quest[nq] = sorted(list(step_dict))

print(f"Total quests: {len(by_quest)}")
print(f"Total long steps: {len(long_steps_set)}")

# Generate Lua file
lua_lines = [
    '--- ============================================================================',
    '--- Autogenerado a partir de Quest Helper y Diccionarios de Traducción',
    '--- Organizado por misión activa para CERO falsos positivos en otros NPCs.',
    '--- ============================================================================',
    '',
    'local QuestSteps = {}',
    '',
    '--- Pasos universales de inicio de misiones (exact match solamente)',
    'QuestSteps.universal = {'
]

for s in sorted(universal_set):
    escaped = s.replace('\\', '\\\\').replace('"', '\\"')
    lua_lines.append(f'    ["{escaped}"] = true,')

lua_lines.append('}')
lua_lines.append('')
lua_lines.append('--- Pasos específicos indexados por nombre normalizado de misión')
lua_lines.append('QuestSteps.byQuest = {')

for qname in sorted(by_quest.keys()):
    q_esc = qname.replace('\\', '\\\\').replace('"', '\\"')
    lua_lines.append(f'    ["{q_esc}"] = {{')
    for s in by_quest[qname]:
        s_esc = s.replace('\\', '\\\\').replace('"', '\\"')
        lua_lines.append(f'        ["{s_esc}"] = true,')
    lua_lines.append('    },')

lua_lines.append('}')
lua_lines.append('')
lua_lines.append('--- Pasos largos inequívocos (>= 15 caracteres) para respaldo general')
lua_lines.append('QuestSteps.longSteps = {')

for s in sorted(long_steps_set):
    s_esc = s.replace('\\', '\\\\').replace('"', '\\"')
    lua_lines.append(f'    ["{s_esc}"] = true,')

lua_lines.append('}')
lua_lines.append('')
lua_lines.append('return QuestSteps')

out_path = 'plugins/rs-translator/src/data/quest_dialogue_steps.lua'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lua_lines))

print(f"Successfully generated {out_path} with {len(by_quest)} quests and {len(long_steps_set)} long steps.")
