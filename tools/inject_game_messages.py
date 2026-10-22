# -*- coding: utf-8 -*-

exact_messages = {
    # Prayer & Altars
    "Offering bones or ashes at an altar will give an extra 50% XP compared to burying them.": "Ofrecer huesos o cenizas en un altar otorgará un 50% de XP adicional en comparación con enterrarlos.",
    "Offering bones at an altar will give an extra 50% XP compared to burying them.": "Ofrecer huesos en un altar otorgará un 50% de XP adicional en comparación con enterrarlos.",
    "Offering ashes at an altar will give an extra 50% XP compared to scattering them.": "Ofrecer cenizas en un altar otorgará un 50% de XP adicional en comparación con esparcirlas.",
    "The gods are pleased with your offering.": "Los dioses están complacidos con tu ofrenda.",
    "You offer the bones to the gods.": "Ofreces los huesos a los dioses.",
    "You scatter the ashes.": "Esparces las cenizas.",
    "You bury the bones.": "Entierras los huesos.",
    "You already have full Prayer points.": "Ya tienes todos tus Prayer points.",
    "You already have full prayer points.": "Ya tienes todos tus prayer points.",
    "You recharge your Prayer points.": "Recargas tus Prayer points.",
    "You have recharged your Prayer points.": "Has recargado tus Prayer points.",
    "You pray at the altar...": "Rezas en el altar...",
    "You pray at the altar.": "Rezas en el altar.",
    "Your Prayer points have been restored.": "Tus Prayer points han sido restaurados.",
    "Your prayer points have been restored.": "Tus prayer points han sido restaurados.",
    
    # Coffin / The Restless Ghost
    "You search the coffin...": "Registras el ataúd...",
    "You search the coffin.": "Registras el ataúd.",
    "You open the coffin.": "Abres el ataúd.",
    "You close the coffin.": "Cierras el ataúd.",
    "The coffin is empty.": "El ataúd está vacío.",
    "There is a skeleton inside the coffin.": "Hay un esqueleto dentro del ataúd.",
    "A skull is missing from the skeleton.": "Al esqueleto le falta el cráneo.",
    "You put the skull in the coffin.": "Pones el cráneo en el ataúd.",
    "You put the skull inside the coffin.": "Pones el cráneo dentro del ataúd.",
    "You place the skull in the coffin.": "Colocas el cráneo en el ataúd.",
    "You place the skull inside the coffin.": "Colocas el cráneo dentro del ataúd.",
    "The ghost appears to be released from its torment.": "El fantasma parece haber sido liberado de su tormento.",
    "The ghost seems to have disappeared.": "El fantasma parece haber desaparecido.",
    "The ghost rests in peace at last.": "El fantasma por fin descansa en paz.",
    "You search the rocks...": "Registras las rocas...",
    "You search the rocks.": "Registras las rocas.",
    "You find a muddy skull!": "¡Encuentras un cráneo lleno de barro!",
    "You find a muddy skull.": "Encuentras un cráneo lleno de barro.",
    "You find a skull.": "Encuentras un cráneo.",
    "A skeleton suddenly attacks you!": "¡Un esqueleto de repente te ataca!",
    "You put on the Ghostspeak amulet.": "Te pones el Ghostspeak amulet.",
    "You wear the Ghostspeak amulet.": "Llevas puesto el Ghostspeak amulet.",
    "You take off the Ghostspeak amulet.": "Te quitas el Ghostspeak amulet.",
    "You can now understand the speech of ghosts.": "Ahora puedes entender el habla de los fantasmas.",

    # Inventory & Skilling Warnings
    "You don't have enough space in your inventory.": "No tienes suficiente espacio en tu inventario.",
    "Your inventory is too full to hold any more.": "Tu inventario está demasiado lleno para guardar más.",
    "Your inventory is too full.": "Tu inventario está demasiado lleno.",
    "Your backpack is too full.": "Tu mochila está demasiado llena.",
    "You need a free inventory slot to do that.": "Necesitas un espacio libre en el inventario para hacer eso.",
    "You need a free backpack space to do that.": "Necesitas un espacio libre en la mochila para hacer eso.",
    "Nothing interesting happens.": "No ocurre nada interesante.",
    "You can't reach that.": "No puedes alcanzar eso.",
    "I can't reach that!": "¡No puedo alcanzar eso!",
    "You cannot reach that.": "No puedes alcanzar eso.",
    "You can't do that right now.": "No puedes hacer eso ahora mismo.",
    "You cannot do that right now.": "No puedes hacer eso ahora mismo.",
    "You can't do that while in combat.": "No puedes hacer eso mientras estás en combate.",
    "You cannot do that while in combat.": "No puedes hacer eso mientras estás en combate.",
    "You can't use that here.": "No puedes usar eso aquí.",
    "You cannot use that here.": "No puedes usar eso aquí.",
    "It's locked.": "Está cerrado con llave.",
    "The door is locked.": "La puerta está cerrada con llave.",
    "The chest is locked.": "El cofre está cerrado con llave.",
    "The gate is locked.": "La verja está cerrada con llave.",
    "It won't open.": "No se abre.",
    "It's stuck.": "Está atascado.",

    # UI & Selection
    "Choose an option:": "Elige una opción:",
    "Select an option:": "Selecciona una opción:",
    "Select an Option": "Selecciona una opción",
    "Choose an Option": "Elige una opción",
    "What would you like to do?": "¿Qué te gustaría hacer?",
    "What would you like to make?": "¿Qué te gustaría fabricar?",
    "How many would you like to make?": "¿Cuántos te gustaría fabricar?",
    "Please wait...": "Por favor espera...",
    "Click here to continue": "Haz clic aquí para continuar",
    "Click here to close": "Haz clic aquí para cerrar",
    "Press here to continue": "Presiona aquí para continuar",
    "Tap here to continue": "Toca aquí para continuar",
    "Are you sure you want to do that?": "¿Estás seguro de que quieres hacer eso?",
    "Are you sure?": "¿Estás seguro?",
    "Yes, I'm sure.": "Sí, estoy seguro.",
    "No, cancel.": "No, cancelar.",
}

# New patterns to add to Dictionary.patterns
new_patterns = [
    ('{ pat = "^Offering (.-) at an altar will give an extra (.-)%% XP compared to (.-)%.$", rep = "Ofrecer %1 en un altar otorgará un %2%% de XP adicional en comparación con %3." }'),
    ('{ pat = "^Offering (.-) at an altar will give (.-)%.$", rep = "Ofrecer %1 en un altar otorgará %2." }'),
    ('{ pat = "^Offering (.-) at an altar gives (.-)%.$", rep = "Ofrecer %1 en un altar otorga %2." }'),
    ('{ pat = "^You need an? (.-) level of (%d+) to (.-)%.$", rep = "Necesitas un nivel de %1 de %2 para %3." }'),
    ('{ pat = "^You need an? (.-) level of at least (%d+) to (.-)%.$", rep = "Necesitas un nivel de %1 de al menos %2 para %3." }'),
    ('{ pat = "^You must have an? (.-) level of (%d+) to (.-)%.$", rep = "Debes tener un nivel de %1 de %2 para %3." }'),
    ('{ pat = "^You need (%d+) (.-) to (.-)%.$", rep = "Necesitas %1 %2 para %3." }'),
    ('{ pat = "^Congratulations! You have completed (.-)!$", rep = "¡Felicitaciones! ¡Has completado %1!" }'),
    ('{ pat = "^Congratulations, you have completed (.-)!$", rep = "¡Felicitaciones, has completado %1!" }'),
    ('{ pat = "^You have completed (.-)!$", rep = "¡Has completado %1!" }'),
    ('{ pat = "^You are awarded: (.-)$", rep = "Se te otorga: %1" }'),
    ('{ pat = "^You search the (.-) and find (.-)%.$", rep = "Registras el %1 y encuentras %2." }'),
    ('{ pat = "^You search the (.-) but find nothing%.$", rep = "Registras el %1 pero no encuentras nada." }'),
    ('{ pat = "^You search the (.-) and find nothing of interest%.$", rep = "Registras el %1 y no encuentras nada de interés." }'),
    ('{ pat = "^You examine the (.-)%.$", rep = "Examinas el %1." }'),
    ('{ pat = "^You use the (.-) on the (.-)%.$", rep = "Usas %1 en %2." }'),
    ('{ pat = "^You give the (.-) to (.-)%.$", rep = "Le das %1 a %2." }'),
    ('{ pat = "^You hand the (.-) to (.-)%.$", rep = "Le entregas %1 a %2." }'),
]

with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject exact messages
idx = content.find('Dictionary.exact = {')
if idx != -1:
    insert_pos = idx + len('Dictionary.exact = {\n')
    lines_to_add = []
    for en, es in exact_messages.items():
        en_esc = en.replace('\\', '\\\\').replace('"', '\\"')
        es_esc = es.replace('\\', '\\\\').replace('"', '\\"')
        if f'["{en_esc}"]' not in content:
            lines_to_add.append(f'    ["{en_esc}"] = "{es_esc}",')
    content = content[:insert_pos] + '\n'.join(lines_to_add) + '\n' + content[insert_pos:]
    print(f"Added {len(lines_to_add)} exact messages.")

# 2. Inject patterns
p_idx = content.find('Dictionary.patterns = {')
if p_idx != -1:
    p_insert_pos = p_idx + len('Dictionary.patterns = {\n')
    p_lines_to_add = []
    for p in new_patterns:
        if p not in content:
            p_lines_to_add.append(f'    {p},')
    content = content[:p_insert_pos] + '\n'.join(p_lines_to_add) + '\n' + content[p_insert_pos:]
    print(f"Added {len(p_lines_to_add)} patterns.")

with open('plugins/rs-translator/src/dictionary.lua', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated dictionary.lua successfully!")
