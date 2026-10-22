# -*- coding: utf-8 -*-
import json, re

with open('tools/step_translations.json', 'r', encoding='utf-8') as f:
    custom_trans = json.load(f)

# Extra common UI / Quest phrases
custom_trans["WHAT WOULD YOU LIKE TO SAY?"] = "¿QUÉ TE GUSTARÍA DECIR?"
custom_trans["WHAT WOULD YOU LIKE TO SAY"] = "¿QUÉ TE GUSTARÍA DECIR?"
custom_trans["What would you like to say?"] = "¿Qué te gustaría decir?"
custom_trans["What would you like to say"] = "¿Qué te gustaría decir?"
custom_trans["CLICK HERE TO CONTINUE"] = "HAZ CLIC AQUÍ PARA CONTINUAR"
custom_trans["Click here to continue..."] = "Haz clic aquí para continuar..."
custom_trans["Click here to continue"] = "Haz clic aquí para continuar"
custom_trans["SELECT AN OPTION"] = "SELECCIONA UNA OPCIÓN"
custom_trans["CHOOSE AN OPTION"] = "ELIGE UNA OPCIÓN"
custom_trans["Choose an option:"] = "Elige una opción:"
custom_trans["Choose an Option:"] = "Elige una opción:"
custom_trans["PLEASE WAIT..."] = "POR FAVOR ESPERA..."
custom_trans["Please wait..."] = "Por favor espera..."
custom_trans["Accept Quest"] = "Aceptar misión"
custom_trans["Accept quest"] = "Aceptar misión"
custom_trans["[Accept Quest]"] = "[Aceptar misión]"
custom_trans["[Accept quest]"] = "[Aceptar misión]"
custom_trans["Not Right Now"] = "Ahora no"
custom_trans["Not right now"] = "Ahora no"
custom_trans["Quest Overview"] = "Resumen de misión"

with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate Dictionary.exact = {
idx = content.find('Dictionary.exact = {')
if idx == -1:
    print("Error: Dictionary.exact not found")
    exit(1)

insert_pos = idx + len('Dictionary.exact = {\n')

new_entries = []
for en, es in sorted(custom_trans.items()):
    en_esc = en.replace('\\', '\\\\').replace('"', '\\"')
    es_esc = es.replace('\\', '\\\\').replace('"', '\\"')
    key_pattern = f'["{en_esc}"]'
    if key_pattern not in content:
        new_entries.append(f'    ["{en_esc}"] = "{es_esc}",')

print(f"Adding {len(new_entries)} new entries to Dictionary.exact...")
updated_content = content[:insert_pos] + '\n'.join(new_entries) + '\n' + content[insert_pos:]

with open('plugins/rs-translator/src/dictionary.lua', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("Updated plugins/rs-translator/src/dictionary.lua successfully.")
