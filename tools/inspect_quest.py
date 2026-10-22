import zipfile, re

zip_path = r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip'
with zipfile.ZipFile(zip_path, 'r') as z:
    content = z.read('quests/the-restless-ghost/the-restless-ghost.lua').decode('utf-8')
    steps = re.findall(r'addDialogStep(?:WithExclusion[s]?)?\(\s*"([^"]+)"', content)
    print("Steps in The Restless Ghost:")
    for s in steps:
        print(f"  - {s}")
