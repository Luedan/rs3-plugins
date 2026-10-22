import re

with open('plugins/rs-translator/src/data/dialogues_L.lua', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('["Lumbridge Sage"] = {')
end_idx = c.find('\n    },', idx)
block = c[idx:end_idx]

entries = re.findall(r'\["([^"]+)"\]\s*=', block)
print(f"Lumbridge Sage in dialogues_L.lua: {len(entries)} entries")
