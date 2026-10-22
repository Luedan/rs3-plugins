with open(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\PluginData.db', 'rb') as f:
    data = f.read()

import re
matches = re.findall(b'(Quest Helper[^\x00\x01\x02\x03\x04\x05]{1,30})[\x00-\x05]([^\x00\x01\x02\x03\x04\x05]{1,50})', data)
for k, v in matches:
    print(f"{k.decode('latin1', 'replace')} -> {v.decode('latin1', 'replace')}")
