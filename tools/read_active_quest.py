with open(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\PluginData.db', 'rb') as f:
    data = f.read()

idx = 0
while True:
    pos = data.find(b'Quest HelperactiveEntry', idx)
    if pos == -1:
        break
    print("Found at pos", pos, ":", repr(data[pos:pos+60]))
    idx = pos + 1
