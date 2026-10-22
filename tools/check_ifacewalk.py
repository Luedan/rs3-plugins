import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    if 'src/render/ifacewalk.lua' in z.namelist():
        print(z.read('src/render/ifacewalk.lua').decode('utf-8', errors='ignore'))
