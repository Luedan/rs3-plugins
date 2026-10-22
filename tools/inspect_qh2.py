import zipfile

files_to_check = [
    'src/render/widgethighlight.lua',
    'src/requirements/dialog.lua',
    'src/core/helpers/quest.lua'
]

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    for fname in files_to_check:
        print("="*40, fname, "="*40)
        try:
            content = z.read(fname).decode('utf-8')
            print(content[:3000])
        except Exception as e:
            print(e)
