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
                        if 'PersistentDB' in data:
                            print(f"{f} -> {name}")
                            for line in data.splitlines():
                                if 'PersistentDB' in line:
                                    print("  ", line.strip()[:100])
