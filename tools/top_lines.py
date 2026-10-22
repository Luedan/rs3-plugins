import re, glob
from collections import Counter

counter = Counter()
for f in glob.glob('plugins/rs-translator/src/data/dialogues_*.lua'):
    if 'quest' in f: continue
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    # Find all English keys in dialogues.all
    idx = c.find('dialogues.all = {')
    if idx != -1:
        keys = re.findall(r'\["([^"]+)"\]\s*=', c[idx:])
        for k in keys:
            counter[k] += 1

print("Top 30 most common dialogue lines across all NPCs:")
for text, cnt in counter.most_common(30):
    print(f"[{cnt}x] {text}")
