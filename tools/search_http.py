import zipfile, os

plugins_dir = r'C:\ProgramData\Jagex\RuneScape-BETA\plugins'
for root, dirs, files in os.walk(plugins_dir):
    for f in files:
        if f.endswith('.zip'):
            zpath = os.path.join(root, f)
            with zipfile.ZipFile(zpath, 'r') as z:
                for name in z.namelist():
                    if name.endswith('.lua'):
                        data = z.read(name).decode('utf-8', errors='ignore')
                        for w in ['http', 'Http', 'HTTP', 'request', 'socket', 'network']:
                            if w in data:
                                print(f"{f} -> {name}: found {w}")
