with open(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\PluginData.db', 'rb') as f:
    data = f.read()

prefix = b'Quest HelperactiveEntry'
pos = data.rfind(prefix)
print("pos:", pos)
if pos != -1:
    chunk = data[pos:pos+150]
    print("chunk:", repr(chunk))
    # Let's inspect the exact bytes after prefix
    val_part = chunk[len(prefix):]
    print("val_part bytes:", [b for b in val_part[:30]])
