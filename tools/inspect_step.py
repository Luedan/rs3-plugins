import zipfile

with zipfile.ZipFile(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip', 'r') as z:
    content = z.read('src/steps/step.lua').decode('utf-8', errors='ignore')
    for i, line in enumerate(content.splitlines()):
        if 'openDialogSteps' in line:
            print("\n".join(content.splitlines()[max(0, i-10):min(len(content.splitlines()), i+30)]))
