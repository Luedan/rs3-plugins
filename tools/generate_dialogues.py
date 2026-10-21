import os
import sys
import re

def clean_dialogue_line(line):
    if not line:
        return None, None
    line = line.strip()
    if not line:
        return None, None
        
    # Skip markdown headers, conditions, actions, stage directions
    if line.startswith('#') or line.startswith('(') or line.startswith("''") or line == '(continue)' or line == '(end)' or line == '(below)':
        return None, None
    
    # Strip list bullet: '- ' or '+ ' or '* '
    line = re.sub(r'^(?:[-+]\s+|\*(?!\*)\s+)+', '', line).strip()
    
    # Wiki scene descriptions/notes in italics
    if line.startswith("''"):
        return None, None
    
    # Check speaker: **Speaker:** or **Speaker**:
    m_spk = re.match(r'^\*\*([^*:]+?)(?::\*\*|\*\*:)\s*(.*)', line)
    if m_spk:
        speaker = m_spk.group(1).strip()
        text = m_spk.group(2).strip()
        text = re.sub(r'\{\{RSChat\|(.*?)\}\}', r'\1', text)
        text = re.sub(r'\{\{Qact\|(.*?)\}\}', r'\1', text)
        text = text.strip().strip("'\"")
        return speaker, text
        
    # Check [Choice]: ...
    m_choice = re.match(r'^\[Choice\]:\s*(.*)', line)
    if m_choice:
        rest = m_choice.group(1)
        if '|' in rest:
            rest = rest.split('|')[-1]
        rest = re.sub(r'\{\{RSChat\|(.*?)\}\}', r'\1', rest)
        return '[Choice]', rest.strip().strip("'\"")
        
    # Check [Menu]: ...
    m_menu = re.match(r'^\[Menu\]:\s*(.*)', line)
    if m_menu:
        rest = m_menu.group(1)
        if '|' in rest:
            rest = rest.split('|')[0]
        return '[Menu]', rest.strip().strip("'\"")
        
    # Other normal dialogue line or choice
    line = re.sub(r'\{\{RSChat\|(.*?)\}\}', r'\1', line)
    line = line.strip().strip("'\"")
    if line.startswith('{{') or line.startswith('(') or line.startswith("''") or line.endswith(':'):
        return None, None
        
    return None, line

def escape_lua_str(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = s.replace('\r\n', '\\n').replace('\n', '\\n').replace('\r', '\\n')
    return s

def process_letter(letter):
    letter_upper = letter.upper()
    folder_name = "#" if letter == "#" else letter_upper
    file_suffix = "NUM" if letter == "#" else letter_upper
    
    # Relative or absolute paths based on working directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    en_dir = os.path.join(base_dir, "runescape-dialogue-translator", "data", "dialogs_en", folder_name)
    es_dir = os.path.join(base_dir, "runescape-dialogue-translator", "data", "dialogs_es", folder_name)
    out_lua = os.path.join(base_dir, "plugins", "rs-translator", "src", "data", f"dialogues_{file_suffix}.lua")
    
    if not os.path.isdir(en_dir) or not os.path.isdir(es_dir):
        print(f"Directory not found for letter {letter} ({en_dir})")
        return 0, 0, 0

    os.makedirs(os.path.dirname(out_lua), exist_ok=True)
    all_global = {}
    npc_map = {}
    total_pairs = 0

    for fname in sorted(os.listdir(en_dir)):
        if not fname.endswith('.md') or fname == 'README.md':
            continue
        raw_npc_name = fname[:-3]
        en_path = os.path.join(en_dir, fname)
        es_path = os.path.join(es_dir, fname)
        if not os.path.exists(es_path):
            continue
            
        with open(en_path, 'r', encoding='utf-8') as fen:
            en_content = fen.read()
        with open(es_path, 'r', encoding='utf-8') as fes:
            es_content = fes.read()
            
        en_parts = en_content.split('---', 1)
        es_parts = es_content.split('---', 1)
        if len(en_parts) < 2 or len(es_parts) < 2:
            continue
            
        en_lines = [l.strip() for l in en_parts[1].splitlines()]
        es_lines = [l.strip() for l in es_parts[1].splitlines()]
        
        current_npc_pairs = {}
        for el, sl in zip(en_lines, es_lines):
            spk_e, txt_e = clean_dialogue_line(el)
            spk_s, txt_s = clean_dialogue_line(sl)
            if txt_e and txt_s and txt_e != txt_s:
                if len(txt_e) <= 1 or len(txt_s) <= 1:
                    continue
                current_npc_pairs[txt_e] = txt_s
                all_global[txt_e] = txt_s
                total_pairs += 1
                
        if current_npc_pairs:
            npc_map[raw_npc_name] = current_npc_pairs
            base_name = re.sub(r'\s*\([^)]*\)', '', raw_npc_name).strip()
            if base_name != raw_npc_name and base_name not in npc_map:
                npc_map[base_name] = current_npc_pairs

    lines = []
    lines.append("--- ============================================================================")
    lines.append(f"--- Diccionario de Diálogos: Letra {letter_upper}")
    lines.append("--- Autogenerado a partir de runescape-dialogue-translator")
    lines.append("--- Entidades, ítems, armas y nombres propios preservados en inglés.")
    lines.append("--- ============================================================================\n")
    lines.append("local dialogues = {}")
    lines.append("dialogues.npcs = {")

    for npc_name, d_map in npc_map.items():
        esc_npc = escape_lua_str(npc_name)
        lines.append(f'    ["{esc_npc}"] = {{')
        for en_text, es_text in d_map.items():
            lines.append(f'        ["{escape_lua_str(en_text)}"] = "{escape_lua_str(es_text)}",')
        lines.append("    },")

    lines.append("}\n")
    lines.append("dialogues.all = {")
    for en_text, es_text in all_global.items():
        lines.append(f'    ["{escape_lua_str(en_text)}"] = "{escape_lua_str(es_text)}",')
    lines.append("}\n")
    lines.append("return dialogues\n")

    with open(out_lua, 'w', encoding='utf-8') as f_out:
        f_out.write('\n'.join(lines))

    print(f"[{letter_upper}] NPCs: {len(npc_map)}, Pares: {total_pairs}, Únicos: {len(all_global)}")
    return len(npc_map), total_pairs, len(all_global)

if __name__ == '__main__':
    all_letters = [chr(c) for c in range(ord('A'), ord('Z') + 1)] + ["#"]
    
    target = sys.argv[1] if len(sys.argv) > 1 else "--all"
    if target == "--all":
        tot_npcs = 0
        tot_pairs = 0
        for ltr in all_letters:
            n, p, u = process_letter(ltr)
            tot_npcs += n
            tot_pairs += p
        print(f"\n>>> ¡PROCESO COMPLETO! Total NPCs generados: {tot_npcs}, Total pares traducidos: {tot_pairs}")
    else:
        process_letter(target)
