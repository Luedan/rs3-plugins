import re, glob

total_all = 0
for f in sorted(glob.glob('plugins/rs-translator/src/data/dialogues_*.lua')):
    if 'quest' in f: continue
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    idx = c.find('dialogues.all = {')
    if idx != -1:
        count = len(re.findall(r'\["[^"]+"\]\s*=', c[idx:]))
        total_all += count
        # print(f"{f}: {count}")

print(f"Total entries across all dialogues.all: {total_all}")
