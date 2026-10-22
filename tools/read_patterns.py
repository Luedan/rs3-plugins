c = open('plugins/rs-translator/src/dictionary.lua', encoding='utf-8').read()
idx = c.find('Dictionary.patterns = {')
if idx != -1:
    print(c[idx:idx+2000])
