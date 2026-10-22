import zipfile, re

with zipfile.ZipFile(r'runescape-api-docs-es.zip', 'r') as z:
    for name in z.namelist():
        if 'draw' in name.lower() or 'event' in name.lower():
            c = z.read(name).decode('utf-8', errors='ignore')
            for l in c.splitlines():
                if any(x in l.lower() for x in ['event.draw', 'draw event', 'pipeline', 'render']):
                    print(l[:100])
