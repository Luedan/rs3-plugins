import os

for letter, name in [('D', 'Donie'), ('G', 'Gee'), ('L', 'Lumbridge Guide'), ('P', 'Phileas')]:
    p_en = os.path.join('runescape-dialogue-translator', 'data', 'dialogs_en', letter, f'{name}.md')
    p_es = os.path.join('runescape-dialogue-translator', 'data', 'dialogs_es', letter, f'{name}.md')
    print(f"{name}: EN={os.path.exists(p_en)}, ES={os.path.exists(p_es)}")
