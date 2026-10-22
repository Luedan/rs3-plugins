import os

for root, dirs, files in os.walk(r'D:\programacion\REPOS\rs-plugins'):
    for f in files:
        if 'Hans.md' in f or 'Father_Aereck.md' in f:
            print(os.path.join(root, f))
