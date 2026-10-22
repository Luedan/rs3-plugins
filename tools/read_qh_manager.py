import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    c = z.read('src/core/manager.lua').decode('utf-8', errors='ignore')

for i, l in enumerate(c.split('\n')):
    if 'CHAT_V2' in l:
        print('\n'.join(c.split('\n')[max(0, i-5):min(len(c.split('\n')), i+15)]))
        print('='*50)
