with open(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\PluginData.db', 'rb') as f:
    data = f.read()

import re
matches = re.findall(b'Quest HelperactiveEntry[^\x00]*[\x01-\x05]([^\x00\r\n]+)', data)
print("Matches:", matches)
if matches:
    print("Last match (active quest):", matches[-1].decode('latin1', 'replace'))
