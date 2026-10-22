with open(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\PluginData.db', 'rb') as f:
    data = f.read()

import re
# Find all printable ASCII strings of length >= 4
strings = re.findall(b'[\x20-\x7e]{4,}', data)
for s in strings:
    s_str = s.decode('ascii', errors='ignore')
    if any(w in s_str.lower() for w in ['active', 'entry', 'quest', 'helper']):
        print(s_str)
