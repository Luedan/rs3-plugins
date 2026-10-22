import os, sys, re
sys.path.insert(0, os.path.abspath('.'))
from tools.generate_dialogues import clean_file_lines, clean_dialogue_line

en_dir = os.path.join('runescape-dialogue-translator', 'data', 'dialogs_en', 'C')
es_dir = os.path.join('runescape-dialogue-translator', 'data', 'dialogs_es', 'C')

npc_map = {}
for fname in sorted(os.listdir(en_dir)):
    if not fname.endswith('.md') or fname == 'README.md': continue
    raw_npc_name = fname[:-3]
    en_path = os.path.join(en_dir, fname)
    es_path = os.path.join(es_dir, fname)
    if not os.path.exists(es_path): continue
    with open(en_path, 'r', encoding='utf-8') as fen: ec = fen.read()
    with open(es_path, 'r', encoding='utf-8') as fes: sc = fes.read()
    ep = ec.split('---', 1)
    sp = sc.split('---', 1)
    if len(ep) < 2 or len(sp) < 2: continue
    el = clean_file_lines(ep[1].splitlines())
    sl = clean_file_lines(sp[1].splitlines())
    current_npc_pairs = {}
    for e, s in zip(el, sl):
        _, te = clean_dialogue_line(e)
        _, ts = clean_dialogue_line(s)
        if te and ts and te != ts and len(te) > 1 and len(ts) > 1:
            current_npc_pairs[te] = ts
    if current_npc_pairs:
        if raw_npc_name not in npc_map:
            npc_map[raw_npc_name] = {}
        npc_map[raw_npc_name].update(current_npc_pairs)

        base_name = re.sub(r'\s*\([^)]*\)', '', raw_npc_name).strip()
        if base_name:
            if base_name not in npc_map:
                npc_map[base_name] = {}
            npc_map[base_name].update(current_npc_pairs)

print(f"Total lines in 'Cook' before was 21. Total lines in merged 'Cook' now: {len(npc_map['Cook'])}")
for k in list(npc_map['Cook'].keys())[:10]:
    print(" -", k[:60], "->", npc_map['Cook'][k][:60])
