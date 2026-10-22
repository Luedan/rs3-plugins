import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    for name in ['src/ui/main.lua', 'src/render/overlay.lua', 'src/game/bankfilter.lua']:
        content = z.read(name).decode('utf-8', errors='ignore')
        for line in content.splitlines():
            if '_G' in line:
                print(name, ":", line)
