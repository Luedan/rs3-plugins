with open(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\PluginData.db', 'rb') as f:
    data = f.read()

idx = 0
while True:
    pos = data.find(b'Quest HelperactiveEntry', idx)
    if pos == -1:
        break
    snippet = data[pos:pos+60]
    print(f"Offset {pos}: {snippet}")
    idx = pos + 1
