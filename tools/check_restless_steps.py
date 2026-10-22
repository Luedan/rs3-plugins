import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    content = z.read('quests/the-restless-ghost/the-restless-ghost.lua').decode('utf-8', errors='ignore')
    for line in content.splitlines()[30:120]:
        print(line)
