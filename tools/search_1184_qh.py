import zipfile, re

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    for name in z.namelist():
        if name.endswith('.lua'):
            c = z.read(name).decode('utf-8', errors='ignore')
            if '1184' in c:
                for line in c.split('\n'):
                    if '1184' in line:
                        print(f"{name}: {line.strip()}")
