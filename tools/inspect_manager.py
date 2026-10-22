import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    content = z.read('src/core/manager.lua').decode('utf-8', errors='ignore')
    print("Length:", len(content))
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if any(w in line.lower() for w in ['widgethighlight', 'dialogue', 'choice', 'step', 'render', 'highlight']):
            print(f"{i+1}: {line}")
