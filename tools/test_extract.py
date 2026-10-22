with open(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\PluginData.db', 'rb') as f:
    data = f.read()

prefix = b'Quest HelperactiveEntry'
last_pos = None
init = 0
while True:
    p = data.find(prefix, init)
    if p == -1:
        break
    last_pos = p
    init = p + len(prefix)

print("last_pos:", last_pos)
if last_pos:
    after = data[last_pos + len(prefix):last_pos + len(prefix) + 80]
    import re
    m = re.match(b'^\x03([^\x00]+)\x00', after)
    if m:
        print("Extracted quest name:", m.group(1).decode('utf-8'))
    else:
        print("No match, after is:", repr(after[:30]))
