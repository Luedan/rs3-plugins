# -*- coding: utf-8 -*-
import re

# Load dictionary.lua
with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as f:
    dict_code = f.read()

# Parse exact entries
dict_exact = {}
idx = dict_code.find('Dictionary.exact = {')
end_idx = dict_code.find('\nDictionary.patterns = {', idx)
exact_block = dict_code[idx:end_idx]

for m in re.finditer(r'\["([^"]+)"\]\s*=\s*"([^"]+)"', exact_block):
    dict_exact[m.group(1)] = m.group(2)

print(f"Total exact dictionary entries: {len(dict_exact)}")

# Test exact screenshot text
test_text = "Offering bones or ashes at an altar will give an extra 50% XP compared to burying them."
trans = dict_exact.get(test_text)
print("Translating screenshot text:")
print("EN:", test_text)
print("ES:", trans)

assert trans is not None
print("\nSUCCESS: Exact match found in dictionary!")
