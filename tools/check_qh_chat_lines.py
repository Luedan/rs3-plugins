import zipfile, os, re

p = r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip'
with zipfile.ZipFile(p, 'r') as z:
    for name in z.namelist():
        if name.endswith('.lua'):
            c = z.read(name).decode('utf-8', errors='ignore')
            if 'CHAT_V2_LEFT' in c:
                for line in c.split('\n'):
                    if 'CHAT_V2_LEFT' in line or 'CHAT_V2_RIGHT' in line:
                        print(f"{name}: {line.strip()}")
