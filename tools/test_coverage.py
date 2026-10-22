import zipfile, re, glob

zip_path = r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\6399152\6399152.zip'

dialogue_translations = {}
for f in glob.glob('plugins/rs-translator/src/data/dialogues_*.lua'):
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
        for m in re.finditer(r'\["([^"]+)"\]\s*=\s*"([^"]+)"', text):
            en = m.group(1).strip()
            es = m.group(2).strip()
            if en not in dialogue_translations:
                dialogue_translations[en] = es

with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as fh:
    text = fh.read()
    for m in re.finditer(r'\["([^"]+)"\]\s*=\s*"([^"]+)"', text):
        en = m.group(1).strip()
        es = m.group(2).strip()
        if en not in dialogue_translations:
            dialogue_translations[en] = es

# Lowercase lookup table
dt_lower = {k.lower(): v for k, v in dialogue_translations.items()}

all_steps = set()
with zipfile.ZipFile(zip_path, 'r') as z:
    for name in z.namelist():
        if name.startswith('quests/') and name.endswith('.lua'):
            content = z.read(name).decode('utf-8', errors='ignore')
            for sm in re.finditer(r'addDialogStep(?:WithExclusion[s]?)?\(\s*"([^"]+)"', content):
                s = sm.group(1).strip()
                if s:
                    all_steps.add(s)

matched = 0
unmatched = []
for s in sorted(all_steps):
    trans = dialogue_translations.get(s) or dt_lower.get(s.lower())
    if not trans:
        # try without punctuation
        s_bare = s.rstrip('.!?')
        trans = dialogue_translations.get(s_bare) or dt_lower.get(s_bare.lower())
    if trans:
        matched += 1
    else:
        unmatched.append(s)

print(f"Total steps: {len(all_steps)}, Matched translations: {matched}, Unmatched: {len(unmatched)}")
print("\nFirst 20 unmatched steps:")
for s in unmatched[:20]:
    print(f"  '{s}'")
