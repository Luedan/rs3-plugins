with open(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\PluginData.db', 'rb') as f:
    data = f.read()

import re
m = re.findall(b'RS Traductor[^\x00]*[\x01-\x05]([^\x00\r\n]+)', data)
print("RS Traductor DB entries:")
for x in m[-10:]:
    print(" ", x[:80])
