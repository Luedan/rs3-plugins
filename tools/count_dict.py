import re
c = open('plugins/rs-translator/src/dictionary.lua', encoding='utf-8').read()
entries = re.findall(r'\["([^"]+)"\]\s*=', c)
print('Total exact entries in dictionary.lua:', len(entries))
