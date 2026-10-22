import zipfile, re

zip_path = r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip'
all_steps = set()

with zipfile.ZipFile(zip_path, 'r') as z:
    for name in z.namelist():
        if name.startswith('quests/') and name.endswith('.lua'):
            content = z.read(name).decode('utf-8', errors='ignore')
            for sm in re.finditer(r'addDialogStep(?:WithExclusion[s]?)?\(\s*"([^"]+)"', content):
                s = sm.group(1).strip()
                if s:
                    all_steps.add(s)

with open('tools/all_quest_steps_list.txt', 'w', encoding='utf-8') as f:
    for s in sorted(all_steps):
        f.write(s + '\n')

print(f"Wrote {len(all_steps)} steps to tools/all_quest_steps_list.txt")
