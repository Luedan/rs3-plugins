import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    for name in z.namelist():
        if 'restless' in name.lower() or 'ghost' in name.lower():
            print("Found:", name)
            content = z.read(name).decode('utf-8', errors='ignore')
            print(content[:1500])
