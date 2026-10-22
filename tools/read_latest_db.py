import os, glob

path = 'C:/ProgramData/Jagex/RuneScape-BETA/plugins/PluginData.db'
with open(path, 'rb') as f:
    data = f.read()

# Search for any strings containing "rs_diag_" or "test_" or "Father" or "That's lucky"
import re
print("Length of DB:", len(data))
found = []
for m in re.finditer(b'([a-zA-Z0-9_]{3,35})\x00([^\x00]{1,150})', data):
    k = m.group(1).decode('latin1', errors='ignore')
    v = m.group(2).decode('latin1', errors='ignore')
    if any(x in k.lower() or x in v.lower() for x in ['lucky', 'quest', 'father', 'aereck', '1184', '1188', 'diag_']):
        found.append((k, v))

print(f"Total found matches: {len(found)}")
for k, v in found[-20:]:
    # clean printable
    v_clean = ''.join(c if 32 <= ord(c) < 127 else ' ' for c in v)
    print(f"  {k} => {v_clean}")
