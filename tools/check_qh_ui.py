import zipfile, re

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    for name in z.namelist():
        if name.startswith('src/ui/'):
            c = z.read(name).decode('utf-8', errors='ignore')
            for l in c.splitlines():
                if 'addtitle' in l.lower() or 'content =' in l.lower() or 'activeentry' in l.lower():
                    print(name, ':', l.strip()[:100])
