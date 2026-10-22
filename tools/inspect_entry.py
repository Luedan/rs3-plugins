import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    for name in ['main.lua', 'src/core/entry.lua', 'src/core/helper.lua']:
        if name in z.namelist():
            print("="*40, name, "="*40)
            content = z.read(name).decode('utf-8', errors='ignore')
            print(content[:2500])
