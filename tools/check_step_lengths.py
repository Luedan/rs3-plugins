import zipfile, re

zip_path = r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip'
steps_by_len = []

with zipfile.ZipFile(zip_path, 'r') as z:
    for name in z.namelist():
        if name.startswith('quests/') and name.endswith('.lua'):
            content = z.read(name).decode('utf-8', errors='ignore')
            for m in re.finditer(r'addDialogStep(?:WithExclusion[s]?)?\(\s*"([^"]+)"', content):
                s = m.group(1)
                steps_by_len.append((len(s), s, name))

steps_by_len.sort(key=lambda x: x[0])
print(f"Total dialog steps found: {len(steps_by_len)}")
print("\nShortest 30 steps:")
for l, s, q in steps_by_len[:30]:
    print(f"  [{l}] '{s}' in {q}")
