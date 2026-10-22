import os

base_dir = r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\data'
en_dir = os.path.join(base_dir, 'dialogs_en')
es_dir = os.path.join(base_dir, 'dialogs_es')

diff_count = 0
same_count = 0
for root, dirs, files in os.walk(en_dir):
    for f in files:
        if f.endswith('.md'):
            rel = os.path.relpath(os.path.join(root, f), en_dir)
            es_file = os.path.join(es_dir, rel)
            if os.path.exists(es_file):
                with open(os.path.join(root, f), 'r', encoding='utf-8') as fen:
                    len_en = len(fen.readlines())
                with open(es_file, 'r', encoding='utf-8') as fes:
                    len_es = len(fes.readlines())
                if len_en != len_es:
                    diff_count += 1
                    if diff_count <= 20:
                        print(f"Diff lines: {rel} (EN: {len_en}, ES: {len_es})")
                else:
                    same_count += 1

print(f"Total same: {same_count}, Total diff: {diff_count}")
