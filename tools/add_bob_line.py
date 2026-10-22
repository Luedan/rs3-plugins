# -*- coding: utf-8 -*-

# 1. Update dialogues_B.lua
with open('plugins/rs-translator/src/data/dialogues_B.lua', 'r', encoding='utf-8') as f:
    content = f.read()

old_key = '["Great! I buy and sell pickaxes and hatchet. There are plenty to choose from, and I\'ve some free samples too. Take your pick...or hatchet."]'
new_line = '        ["Great! I buy and sell pickaxes and hatchets. There are plenty to choose from, and I\'ve some free samples too. Take your pick...or hatchet."] = "¡Genial! Compro y vendo picos y hachas. Hay mucho para elegir y también tengo algunas muestras gratis. Elija... o hacha.",\n'

if old_key in content:
    idx = content.find(old_key)
    # Insert new_line right before old_key
    content = content[:idx] + new_line + content[idx:]

    # Also add to dialogues.all
    all_idx = content.find('dialogues.all = {')
    if all_idx != -1:
        insert_all = all_idx + len('dialogues.all = {\n')
        content = content[:insert_all] + '    ["Great! I buy and sell pickaxes and hatchets. There are plenty to choose from, and I\'ve some free samples too. Take your pick...or hatchet."] = "¡Genial! Compro y vendo picos y hachas. Hay mucho para elegir y también tengo algunas muestras gratis. Elija... o hacha.",\n' + content[insert_all:]

    with open('plugins/rs-translator/src/data/dialogues_B.lua', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated dialogues_B.lua successfully.")
else:
    print("Warning: old_key not found in dialogues_B.lua")

# 2. Update dictionary.lua
with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as f:
    dict_content = f.read()

dict_entry = '    ["Great! I buy and sell pickaxes and hatchets. There are plenty to choose from, and I\'ve some free samples too. Take your pick...or hatchet."] = "¡Genial! Compro y vendo picos y hachas. Hay mucho para elegir y también tengo algunas muestras gratis. Elija... o hacha.",\n'
dict_idx = dict_content.find('Dictionary.exact = {')
if dict_idx != -1:
    insert_pos = dict_idx + len('Dictionary.exact = {\n')
    dict_content = dict_content[:insert_pos] + dict_entry + dict_content[insert_pos:]
    with open('plugins/rs-translator/src/dictionary.lua', 'w', encoding='utf-8') as f:
        f.write(dict_content)
    print("Updated dictionary.lua successfully.")
