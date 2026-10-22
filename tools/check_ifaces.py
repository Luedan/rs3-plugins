import zipfile, re

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    for name in z.namelist():
        if name.endswith('.lua'):
            c = z.read(name).decode('utf-8', errors='ignore')
            for m in re.finditer(r'id\.Interface\.([A-Z0-9_]+)', c):
                s = m.group(1)
                if any(x in s for x in ['CHAT', 'CHOICE', 'MES', 'DIALOG', 'MODAL', 'BOX']):
                    print(s)
