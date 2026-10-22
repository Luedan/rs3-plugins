with open(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\PluginData.db', 'rb') as f:
    f.seek(0, 2)
    size = f.tell()
    read_size = min(size, 65536)
    f.seek(max(0, size - read_size))
    data = f.read()

import re
matches = re.findall(b'Quest HelperactiveEntry[^\x00]*[\x01-\x05]([^\x00\r\n]+)\x00', data)
print(f"File size: {size}, read: {len(data)}")
print(f"Matches found: {matches}")
if matches:
    print(f"Active quest: {matches[-1].decode('latin1')}")
