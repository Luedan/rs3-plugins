import os, re
from collections import defaultdict

base_to_variants = defaultdict(list)
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ#':
    f_folder = '#' if letter == '#' else letter
    en_dir = os.path.join('runescape-dialogue-translator', 'data', 'dialogs_en', f_folder)
    if not os.path.exists(en_dir): continue
    for f in os.listdir(en_dir):
        if not f.endswith('.md') or f == 'README.md': continue
        raw_name = f[:-3]
        base_name = re.sub(r'\s*\([^)]*\)', '', raw_name).strip()
        if base_name != raw_name:
            base_to_variants[base_name].append(raw_name)

print(f"Total base names with multiple variants: {len(base_to_variants)}")
# Show top 25
sorted_bases = sorted(base_to_variants.items(), key=lambda x: len(x[1]), reverse=True)
for b, variants in sorted_bases[:25]:
    print(f"'{b}': {len(variants)} variants -> {variants[:4]}")
