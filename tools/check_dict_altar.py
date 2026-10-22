with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'altar' in l.lower() or 'bones' in l.lower():
        print(f"Line {i+1}: {l.strip()[:100]}")
