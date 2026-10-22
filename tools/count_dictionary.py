with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as f:
    c = f.read()

import re
exact_count = len(re.findall(r'\["[^"]+"\]\s*=', c[:c.find('Dictionary.patterns')]))
pat_count = len(re.findall(r'\{\s*pat\s*=', c[c.find('Dictionary.patterns'):]))

print(f"Dictionary.exact entries: {exact_count}")
print(f"Dictionary.patterns entries: {pat_count}")
