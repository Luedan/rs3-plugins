with open('C:/ProgramData/Jagex/RuneScape-BETA/plugins/PluginData.db', 'rb') as f:
    data = f.read()

import re
print("Searching for activeEntry in PluginData.db:")
for m in re.finditer(rb'([^\x00]{1,40}activeEntry[^\x00]{0,40})\x00([^\x00]{1,50})', data):
    print("  Key:", repr(m.group(1).decode('latin1', errors='ignore')), "=> Value:", repr(m.group(2).decode('latin1', errors='ignore')))

print("\nSearching for all keys in PluginData.db:")
for m in re.finditer(rb'([a-zA-Z0-9_\-\.\:\ ]{3,40})\x00([^\x00]{1,60})', data):
    k = m.group(1).decode('latin1', errors='ignore')
    v = m.group(2).decode('latin1', errors='ignore')
    if any(x in k.lower() for x in ['helper', 'entry', 'quest', 'trans', 'traductor']):
        print(f"  {k} => {v}")
