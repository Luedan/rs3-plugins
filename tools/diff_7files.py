import os, difflib

base_dir = r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data'
diff_files = [
    r'A\Agnar.md',
    r'M\Member of the Godless.md',
    r'A\Ali Morrisane.md'
]

for rel in diff_files:
    en_path = os.path.join(base_dir, 'dialogs_en', rel)
    es_path = os.path.join(base_dir, 'dialogs_es', rel)
    with open(en_path, 'r', encoding='utf-8') as f:
        en_lines = [l.strip() for l in f.read().split('---', 1)[1].splitlines() if l.strip()]
    with open(es_path, 'r', encoding='utf-8') as f:
        es_lines = [l.strip() for l in f.read().split('---', 1)[1].splitlines() if l.strip()]
    print(f"=== {rel} ===")
    m = difflib.SequenceMatcher(None, en_lines, es_lines)
    for tag, i1, i2, j1, j2 in m.get_opcodes():
        if tag != 'equal':
            print(f"{tag}: EN[{i1}:{i2}]={en_lines[i1:i2]} vs ES[{j1}:{j2}]={es_lines[j1:j2]}")
