import zipfile, re, json

zip_path = r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip'
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

with open('tools/quests_and_steps.json', 'w', encoding='utf-8') as f:
    json.dump(quests, f, indent=2, ensure_ascii=False)

print(f"Saved {len(quests)} quests to tools/quests_and_steps.json")
