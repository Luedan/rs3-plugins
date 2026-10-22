import zipfile, re, glob

zip_path = r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip'

# 1. Gather all dialogue translations from dialogues_*.lua
dialogue_translations = {}
for f in glob.glob('plugins/rs-translator/src/data/dialogues_*.lua'):
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
        # Find ["EN"] = "ES"
        for m in re.finditer(r'\["([^"]+)"\]\s*=\s*"([^"]+)"', text):
            en = m.group(1).strip()
            es = m.group(2).strip()
            if en not in dialogue_translations:
                dialogue_translations[en] = es

# Also load dictionary.lua
with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as fh:
    text = fh.read()
    for m in re.finditer(r'\["([^"]+)"\]\s*=\s*"([^"]+)"', text):
        en = m.group(1).strip()
        es = m.group(2).strip()
        if en not in dialogue_translations:
            dialogue_translations[en] = es

print(f"Loaded {len(dialogue_translations)} translations.")

# 2. Extract quests and steps from Quest Helper zip
quests = {}
with zipfile.ZipFile(zip_path, 'r') as z:
    for name in z.namelist():
        if name.startswith('quests/') and name.endswith('.lua'):
            content = z.read(name).decode('utf-8', errors='ignore')
            m = re.search(r'QuestHelper:new\("([^"]+)"', content)
            if not m:
                continue
            qname = m.group(1).strip()
            steps = []
            for sm in re.finditer(r'addDialogStep(?:WithExclusion[s]?)?\(\s*"([^"]+)"', content):
                s = sm.group(1).strip()
                if s and s not in steps:
                    steps.append(s)
            if steps:
                quests[qname] = steps

print(f"Found {len(quests)} quests with dialog steps.")
sample = list(quests.keys())[:5]
for q in sample:
    print(f"  Quest: {q} ({len(quests[q])} steps)")
