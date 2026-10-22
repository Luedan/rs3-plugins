import os, re

base_dir = r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data'
en_dir = os.path.join(base_dir, 'dialogs_en')
es_dir = os.path.join(base_dir, 'dialogs_es')

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

total = 0
matches = 0
mismatches = []

for root, dirs, files in os.walk(en_dir):
    for f in files:
        if f.endswith('.md') and f != 'README.md':
            rel = os.path.relpath(os.path.join(root, f), en_dir)
            es_file = os.path.join(es_dir, rel)
            if os.path.exists(es_file):
                total += 1
                with open(os.path.join(root, f), 'r', encoding='utf-8') as fen:
                    en_parts = fen.read().split('---', 1)
                with open(es_file, 'r', encoding='utf-8') as fes:
                    es_parts = fes.read().split('---', 1)
                if len(en_parts) >= 2 and len(es_parts) >= 2:
                    en_lines = clean_file_lines(en_parts[1].splitlines())
                    es_lines = clean_file_lines(es_parts[1].splitlines())
                    if len(en_lines) == len(es_lines):
                        matches += 1
                    else:
                        mismatches.append((rel, len(en_lines), len(es_lines)))

print(f"Total checked: {total}, Matches: {matches}, Mismatches: {len(mismatches)}")
if mismatches:
    print("Mismatches:", mismatches[:10])
