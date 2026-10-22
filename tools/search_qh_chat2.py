import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    for name in ['quests/dealing-with-scabaras/maths-step.lua', 'quests/tree-gnome-village/tree-gnome-village.lua', 'quests/violet-is-blue/match-face.lua']:
        print("="*40, name)
        content = z.read(name).decode('utf-8', errors='ignore')
        for line in content.splitlines():
            if any(k in line for k in ['CHAT', '1184', '1188', 'dialog', 'Dialog']):
                print(line)
