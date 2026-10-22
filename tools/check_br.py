import glob, re

total_br = 0
for f in glob.glob('plugins/rs-translator/src/data/dialogues_*.lua'):
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
        total_br += len(re.findall(r'<br\s*/?>', c))

print("Total <br> tags in dialogues_*.lua:", total_br)
