import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    content = z.read('src/core/manager.lua').decode('utf-8', errors='ignore')
    for line in content.splitlines()[:150]:
        print(line)
