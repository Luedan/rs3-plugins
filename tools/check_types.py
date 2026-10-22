import zipfile, re

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    content = z.read('src/types.lua').decode('utf-8', errors='ignore')

for line in content.splitlines():
    if any(k in line for k in ['CHAT', 'CHOICE', 'MESBOX', 'DIALOG', 'MODAL', 'NPC', 'PLAYER']):
        print(line)
