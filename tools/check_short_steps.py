import zipfile, re

zip_path = r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip'
short_steps = set()

with zipfile.ZipFile(zip_path, 'r') as z:
    for name in z.namelist():
        if name.startswith('quests/') and name.endswith('.lua'):
            content = z.read(name).decode('utf-8', errors='ignore')
            for m in re.finditer(r'addDialogStep(?:WithExclusion[s]?)?\(\s*"([^"]+)"', content):
                s = m.group(1)
                if len(s) < 15:
                    short_steps.add(s)

print(f"Total short steps (< 15 chars): {len(short_steps)}")
for s in sorted(short_steps):
    print(f"  '{s}'")
