import os

base_dir = r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data'
en_dir = os.path.join(base_dir, 'dialogs_en')
es_dir = os.path.join(base_dir, 'dialogs_es')

diff_count = 0
same_count = 0

for root, dirs, files in os.walk(en_dir):
    for f in files:
        if f.endswith('.md') and f != 'README.md':
            rel = os.path.relpath(os.path.join(root, f), en_dir)
            es_file = os.path.join(es_dir, rel)
            if os.path.exists(es_file):
                with open(os.path.join(root, f), 'r', encoding='utf-8') as fen:
                    en_parts = fen.read().split('---', 1)
                with open(es_file, 'r', encoding='utf-8') as fes:
                    es_parts = fes.read().split('---', 1)
                if len(en_parts) >= 2 and len(es_parts) >= 2:
                    l_en = len([l.strip() for l in en_parts[1].splitlines() if l.strip()])
                    l_es = len([l.strip() for l in es_parts[1].splitlines() if l.strip()])
                    if l_en != l_es:
                        diff_count += 1
                    else:
                        same_count += 1

print(f"Non-empty lines after '---': same={same_count}, diff={diff_count}")
