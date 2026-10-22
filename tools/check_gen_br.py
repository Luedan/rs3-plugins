with open('tools/generate_dialogues.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.group(0) for m in re.finditer(r'.*<br.*', text)]
print(f"Matches for <br> in generate_dialogues.py: {len(matches)}")
for m in matches[:10]:
    print("  ", m.strip())
