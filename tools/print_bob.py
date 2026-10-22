with open('plugins/rs-translator/src/data/dialogues_B.lua', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('["Bob"] = {')
end_idx = c.find('\n    },', idx)
print(c[idx:end_idx])
