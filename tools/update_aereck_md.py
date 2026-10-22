en_path = r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_en\F\Father Aereck.md'
es_path = r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data\dialogs_es\F\Father Aereck.md'

with open(en_path, 'r', encoding='utf-8') as f:
    en_content = f.read()

target_en = "- (Condition: After The Restless Ghost:)\n  - **Father Aereck:** Welcome back to the church of holy Saradomin, my friend! What can I do for you today?\n  - (continue)"
repl_en = "- (Condition: After The Restless Ghost:)\n  - **Father Aereck:** Welcome back to the church of holy Saradomin, my friend! What can I do for you today?\n  - (continue)\n- **Father Aereck:** If you find any bones or ashes on your adventures, please feel free to offer them at this altar. You will be rewarded by Saradomin's light with greater knowledge for each one offered.\n- (continue)"

en_content = en_content.replace(target_en.replace('\n', '\r\n'), repl_en.replace('\n', '\r\n'))
if target_en in en_content:
    en_content = en_content.replace(target_en, repl_en)

with open(en_path, 'w', encoding='utf-8') as f:
    f.write(en_content)

with open(es_path, 'r', encoding='utf-8') as f:
    es_content = f.read()

target_es = "- (Condition: After The Restless Ghost:)\n  - **Father Aereck:** ¡Bienvenido de nuevo a la iglesia del santo Saradomin, amigo mío! ¿Qué puedo hacer por ti hoy?\n  - (continue)"
repl_es = "- (Condition: After The Restless Ghost:)\n  - **Father Aereck:** ¡Bienvenido de nuevo a la iglesia del santo Saradomin, amigo mío! ¿Qué puedo hacer por ti hoy?\n  - (continue)\n- **Father Aereck:** Si encuentras huesos o cenizas en tus aventuras, no dudes en ofrecerlos en este altar. La luz de Saradomin te recompensará con mayor conocimiento por cada uno ofrecido.\n- (continue)"

es_content = es_content.replace(target_es.replace('\n', '\r\n'), repl_es.replace('\n', '\r\n'))
if target_es in es_content:
    es_content = es_content.replace(target_es, repl_es)

with open(es_path, 'w', encoding='utf-8') as f:
    f.write(es_content)

print("Updated both Father Aereck.md files successfully.")
