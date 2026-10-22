import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    for name in z.namelist():
        if name.endswith('.lua'):
            data = z.read(name).decode('utf-8', errors='ignore')
            if 'openDialogSteps' in data:
                print("Found openDialogSteps in:", name)
