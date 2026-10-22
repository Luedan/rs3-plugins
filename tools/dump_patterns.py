with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as f:
    c = f.read()

import re
pats = re.findall(r'\{\s*pat\s*=\s*"([^"]+)",\s*rep\s*=\s*"([^"]+)"', c)
print(f"Total patterns: {len(pats)}")
for p, r in pats[:30]:
    print(f"PAT: {p}")
    print(f"REP: {r}")
    print('-'*40)
