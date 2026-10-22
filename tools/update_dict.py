# -*- coding: utf-8 -*-
with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as f:
    c = f.read()

entries = """    -- Lumbridge Sage y asesores de combate / Slayer
    ["Jacquelyn, the Slayer master in Lumbridge courtyard, can suggest monsters for you to fight."] = "Jacquelyn, la Slayer master en el patio de Lumbridge, puede sugerirte monstruos contra los que luchar.",
    ["Jacquelyn, the Slayer master in Lumbridge courtyard, can suggest monsters for you to fight. Remember, you will do better if you have better armour and weapons and it's always worth carrying a bit of food to heal yourself."] = "Jacquelyn, la Slayer master en el patio de Lumbridge, puede sugerirte monstruos contra los que luchar. Recuerda, te irá mejor si tienes mejores armaduras y armas y siempre vale la pena llevar un poco de comida para curarte.",
    ["Jacquelyn, the Slayer Master in Lumbridge courtyard, can suggest monsters for you to fight."] = "Jacquelyn, la Slayer Master en el patio de Lumbridge, puede sugerirte monstruos contra los que luchar.",
    ["Jacquelyn, the Slayer Master in Lumbridge courtyard, can suggest monsters for you to fight. Remember, you will do better if you have better armour and weapons and it's always worth carrying a bit of food to heal yourself."] = "Jacquelyn, la Slayer Master en el patio de Lumbridge, puede sugerirte monstruos contra los que luchar. Recuerda, te irá mejor si tienes mejores armaduras y armas y siempre vale la pena llevar un poco de comida para curarte.",
    ["Turael, the Slayer master in Burthorpe, can suggest monsters for you to fight."] = "Turael, el Slayer master en Burthorpe, puede sugerirte monstruos contra los que luchar.",
    ["Spria, the Slayer master in Burthorpe, can suggest monsters for you to fight."] = "Spria, la Slayer master en Burthorpe, puede sugerirte monstruos contra los que luchar.",
    ["Mazchna, the Slayer master in Canifis, can suggest monsters for you to fight."] = "Mazchna, el Slayer master en Canifis, puede sugerirte monstruos contra los que luchar.",
    ["Vannaka, the Slayer master in Edgeville Dungeon, can suggest monsters for you to fight."] = "Vannaka, el Slayer master en Edgeville Dungeon, puede sugerirte monstruos contra los que luchar.",
    ["Chaeldar, the Slayer master in Zanaris, can suggest monsters for you to fight."] = "Chaeldar, la Slayer master en Zanaris, puede sugerirte monstruos contra los que luchar.",
    ["Sumona, the Slayer master in Pollnivneach, can suggest monsters for you to fight."] = "Sumona, la Slayer master en Pollnivneach, puede sugerirte monstruos contra los que luchar.",
    ["Duradel, the Slayer master in Shilo Village, can suggest monsters for you to fight."] = "Duradel, el Slayer master en Shilo Village, puede sugerirte monstruos contra los que luchar.",
    ["Kuradal, the Slayer master in the Ancient Cavern, can suggest monsters for you to fight."] = "Kuradal, la Slayer master en la Ancient Cavern, puede sugerirte monstruos contra los que luchar.",
    ["Morvran, the Slayer master in Prifddinas, can suggest monsters for you to fight."] = "Morvran, el Slayer master en Prifddinas, puede sugerirte monstruos contra los que luchar.",
    ["Laniakea, the Slayer master on Anachronia, can suggest monsters for you to fight."] = "Laniakea, la Slayer master en Anachronia, puede sugerirte monstruos contra los que luchar.",
    ["Mandrith, the Slayer master in the Wilderness, can suggest monsters for you to fight."] = "Mandrith, el Slayer master en the Wilderness, puede sugerirte monstruos contra los que luchar.",
    ["Krystilia, the Slayer master in Edgeville, can suggest monsters for you to fight."] = "Krystilia, la Slayer master en Edgeville, puede sugerirte monstruos contra los que luchar.",

    -- Diálogos de Gee (Lumbridge)
    ["Hello there, can I help you?"] = "Hola, ¿puedo ayudarte?",
    ["What is this place?"] = "¿Qué lugar es este?",
    ["This is the town of Lumbridge, adventurer. The town is famous for its castle and river."] = "Este es el pueblo de Lumbridge, aventurero. El pueblo es famoso por su castillo y su río.",
    ["What is there to do around here?"] = "¿Qué se puede hacer por aquí?",
    ["There are goblins across the river to fight, sheep to shear, and trees to cut down."] = "Hay goblins al otro lado del río contra los que luchar, ovejas que esquilar y árboles que talar.",
    ["Do you know of any quests?"] = "¿Conoces alguna misión?",
    ["The Cook in Lumbridge Castle might need some help, or perhaps the Duke upstairs."] = "El Cook del castillo de Lumbridge podría necesitar ayuda, o tal vez el Duke en el piso superior.",
    ["Do you know what happened in the castle cellar?"] = "¿Sabes qué pasó en el sótano del castillo?",
    ["I heard some strange noises coming from down there, like digging or tapping on the walls."] = "Escuché ruidos extraños provenientes de allí abajo, como excavaciones o golpes en las paredes.",
    ["I'm fine, thanks."] = "Estoy bien, gracias.",
    ["Take care on your travels!"] = "¡Cuídate en tus viajes!",

    -- Opciones comunes de interacción y despedida
    ["Can I help you with anything?"] = "¿Puedo ayudarte en algo?",
    ["Is there anything else I can help you with?"] = "¿Hay algo más en lo que pueda ayudarte?",
    ["I don't need any help, thanks."] = "No necesito ayuda, gracias.",
    ["Good adventuring, traveller."] = "Buena aventura, viajero.",
    ["Good adventuring, adventurer."] = "Buena aventura, aventurero.",
    ["Take care out there."] = "Ten cuidado ahí fuera.",
    ["See you later."] = "Hasta luego.",
    ["Talk to you later."] = "Hablamos luego.",
    ["Have a good day."] = "Que tengas un buen día.",
    ["Farewell, adventurer."] = "Adiós, aventurero.",
    ["Where can I find more information?"] = "¿Dónde puedo encontrar más información?",
    ["I don't need any help."] = "No necesito ayuda.",
    ["I'm fine for now, thanks."] = "Estoy bien por ahora, gracias.",
    ["I need guidance."] = "Necesito orientación.",
    ["Tell me about the town of Lumbridge."] = "Háblame sobre el pueblo de Lumbridge.",
    ["Where can I get better armour and weapons?"] = "¿Dónde puedo conseguir mejores armaduras y armas?",
    ["Where can I make money?"] = "¿Dónde puedo ganar dinero?",
    ["Where can I smith?"] = "¿Dónde puedo hacer herrería?",
    ["How do I fish?"] = "¿Cómo pesco?",
    ["What monsters should I fight?"] = "¿Qué monstruos debería combatir?",
    ["Where can I find a bank?"] = "¿Dónde puedo encontrar un banco?",
    ["More options..."] = "Más opciones...",
    ["Navigation and lodestones."] = "Navegación y lodestones.",
    ["Tools and tool belt."] = "Herramientas y cinturón de herramientas.",
    ["Quest list."] = "Lista de misiones.",
    ["Skills list."] = "Lista de habilidades.",
    ["Even more options..."] = "Aún más opciones...",
    ["Previous options..."] = "Opciones anteriores...",
"""

target = "Dictionary.exact = {"
if target in c:
    idx = c.find(target) + len(target)
    c = c[:idx] + "\n" + entries + c[idx:]
    print("Added exact entries to Dictionary.exact.")
else:
    print("Error: target not found.")

# Add patterns
pat_target = "Dictionary.patterns = {"
patterns = """    { pat = "^(.-), the [sS]layer [mM]aster in (.-), can suggest monsters for you to fight%.$", rep = "%1, la Slayer Master en %2, puede sugerirte monstruos contra los que luchar." },
    { pat = "^(.-), the [sS]layer [mM]aster on (.-), can suggest monsters for you to fight%.$", rep = "%1, la Slayer Master en %2, puede sugerirte monstruos contra los que luchar." },
    { pat = "^(.-) can suggest monsters for you to fight%.$", rep = "%1 puede sugerirte monstruos contra los que luchar." },
    { pat = "^You can find (.-) in (.-)%.$", rep = "Puedes encontrar a %1 en %2." },
    { pat = "^You can find (.-) at (.-)%.$", rep = "Puedes encontrar a %1 en %2." },
"""
if pat_target in c:
    idx = c.find(pat_target) + len(pat_target)
    c = c[:idx] + "\n" + patterns + c[idx:]
    print("Added patterns to Dictionary.patterns.")
else:
    print("Error: pat_target not found.")

with open('plugins/rs-translator/src/dictionary.lua', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated dictionary.lua successfully.")
