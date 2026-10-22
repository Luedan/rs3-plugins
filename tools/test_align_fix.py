import os, re

base_dir = r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data'
diff_files = [
    r'A\Agnar.md',
    r'M\Member of the Godless.md',
    r'A\Ali Morrisane.md',
    r'L\Locks and traps trainer.md',
    r'S\Signature Heroes.md',
    r'V\Vannaka.md',
    r'W\Wahisietel.md'
]

def clean_file_lines(lines):
    out = []
    for l in lines:
        s = l.strip()
        if not s:
            continue
        if re.match(r'^\{\{(?:incomplete|cleanup|wip|ToC|DEFAULTSORT:[^}]+)\}\}$', s, re.I):
            continue
        out.append(s)
    return out

for rel in diff_files:
    en_path = os.path.join(base_dir, 'dialogs_en', rel)
    es_path = os.path.join(base_dir, 'dialogs_es', rel)
    with open(en_path, 'r', encoding='utf-8') as f:
        en_lines = clean_file_lines(f.read().split('---', 1)[1].splitlines())
    with open(es_path, 'r', encoding='utf-8') as f:
        es_lines = clean_file_lines(f.read().split('---', 1)[1].splitlines())
    print(f"{rel}: EN={len(en_lines)}, ES={len(es_lines)}, Match={len(en_lines) == len(es_lines)}")
