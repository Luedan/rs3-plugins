import os

lumbridge_npcs = [
    ("L", "Lumbridge Sage"),
    ("J", "Jacquelyn"),
    ("B", "Bob"),
    ("H", "Hans"),
    ("C", "Cook"),
    ("D", "Duke Horacio"),
    ("F", "Father Aereck"),
    ("R", "Restless ghost"),
    ("F", "Father Urhney"),
    ("E", "Explorer Jack"),
    ("D", "Donnie"),
    ("A", "Apprentice Smith"),
    ("F", "Fred the Farmer"),
    ("G", "Gillie Groats"),
    ("G", "Gee"),
    ("R", "Roddeck"),
    ("M", "Mikasi"),
    ("N", "Nemarti"),
    ("H", "Head Chef"),
    ("V", "Victoria"),
    ("C", "Count Check"),
    ("D", "Doomsayer"),
    ("B", "Barman"),
    ("G", "Guard"),
    ("M", "Man"),
    ("W", "Woman"),
    ("F", "Foreman George"),
    ("X", "Xenia"),
]

for letter, npc in lumbridge_npcs:
    en_path = os.path.join('runescape-dialogue-translator', 'data', 'dialogs_en', letter, f'{npc}.md')
    es_path = os.path.join('runescape-dialogue-translator', 'data', 'dialogs_es', letter, f'{npc}.md')
    en_exists = os.path.exists(en_path)
    es_exists = os.path.exists(es_path)
    print(f"{npc:20} -> EN: {en_exists:1}, ES: {es_exists:1}")
