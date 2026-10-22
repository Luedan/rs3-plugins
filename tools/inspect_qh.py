import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    for name in z.namelist():
        if any(w in name.lower() for w in ['dialog', 'choice', 'highlight', 'main', 'core']):
            print(name)
