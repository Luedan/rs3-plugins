#!/usr/bin/env python3
"""
RuneScape Dialogue Translator - Condition Restorer
Restaura de forma instantánea todas las líneas de condición ((...)), (Condition: ...) y tokens
de control en los archivos traducidos en español (dialogs_es) copiándolos directamente
desde sus archivos originales en inglés (dialogs_en).
No realiza peticiones web ni consume API, ejecutándose en pocos segundos sobre todos los NPCs.
"""

import os
import sys
import re
import time
import argparse

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
EN_DIR = os.path.join(DATA_DIR, 'dialogs_en')
ES_DIR = os.path.join(DATA_DIR, 'dialogs_es')

def standardize_and_clean_line(line):
    line = re.sub(r'\{\{tselect\|([^}]+)\}\}', r'[Menu]: \1', line)
    line = re.sub(r'\{\{topt\|cond=([^|]+)\|([^}]+)\}\}', r'[Choice]: cond=\1|\2', line)
    line = re.sub(r'\{\{topt\|([^}]+)\}\}', r'[Choice]: \1', line)
    line = re.sub(r'\{\{tcond\|([^}]+)\}\}', r'(Condition: \1)', line)
    def clean_tact(m):
        arg = m.group(1).strip()
        if arg in {'continue', 'initial', 'end', 'previous'}:
            return f"({arg})"
        if arg.startswith('removes=') or arg.startswith('receives='):
            return f"({arg})"
        return f"(Action: {arg})"
    line = re.sub(r'\{\{tact\|([^}]+)\}\}', clean_tact, line)
    line = re.sub(r'\{\{Qact\|([^}]+)\}\}', r'(Action: \1)', line)
    line = re.sub(r'\{\{qact\|([^}]+)\}\}', r'(Action: \1)', line)
    line = re.sub(r'\{\{Pop-up\|([^}]+)\}\}', r'(Pop-up: \1)', line)
    line = re.sub(r'\{\{(?:incomplete|cleanup|wip|ToC|DEFAULTSORT:[^}]+)\}\}', '', line)
    return line

def is_preserved_condition_or_token(content_after):
    c = content_after.strip()
    if re.match(r'^\(Condition:\s*.*\)$', c, re.IGNORECASE):
        return True
    if re.match(r'^\(\(.*?\)\)$', c):
        return True
    if re.match(r'^\((?:continue|initial|end|previous|opens=|removes=|receives=|below\||above\||pop-up)[^)]*\)$', c, re.IGNORECASE):
        return True
    return False

def restore_file(en_path, es_path):
    if not os.path.exists(en_path) or not os.path.exists(es_path):
        return 0, False

    with open(en_path, 'r', encoding='utf-8') as f:
        c_en = f.read()
    with open(es_path, 'r', encoding='utf-8') as f:
        c_es = f.read()

    p_en = c_en.split('---', 1)
    p_es = c_es.split('---', 1)
    if len(p_en) < 2 or len(p_es) < 2:
        return 0, False

    header_es = p_es[0]
    en_lines = p_en[1].splitlines()
    es_lines = p_es[1].splitlines()

    if len(en_lines) != len(es_lines):
        return 0, False

    replaced_in_file = 0
    new_es_lines = list(es_lines)

    for i, (el, sl) in enumerate(zip(en_lines, es_lines)):
        cleaned_el = standardize_and_clean_line(el)
        indent_m = re.match(r'^(\s*(?:-\s*)?)', cleaned_el)
        indent = indent_m.group(1) if indent_m else ''
        content_after = cleaned_el[len(indent):].strip()

        if is_preserved_condition_or_token(content_after):
            if sl != cleaned_el:
                new_es_lines[i] = cleaned_el
                replaced_in_file += 1

    if replaced_in_file > 0:
        new_content = header_es + '---' + '\n'.join(new_es_lines)
        # Ensure trailing newline if original had it
        if c_es.endswith('\n') and not new_content.endswith('\n'):
            new_content += '\n'
        with open(es_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return replaced_in_file, True

    return 0, False

def process_all():
    total_files = 0
    modified_files = 0
    total_lines = 0

    t0 = time.time()
    for letter in sorted(os.listdir(EN_DIR)):
        en_l = os.path.join(EN_DIR, letter)
        es_l = os.path.join(ES_DIR, letter)
        if not os.path.isdir(en_l) or not os.path.isdir(es_l):
            continue

        letter_mod = 0
        letter_lines = 0
        for fname in sorted(os.listdir(en_l)):
            if not fname.endswith('.md') or fname == 'README.md':
                continue
            en_path = os.path.join(en_l, fname)
            es_path = os.path.join(es_l, fname)
            
            total_files += 1
            lines_rep, modified = restore_file(en_path, es_path)
            if modified:
                modified_files += 1
                total_lines += lines_rep
                letter_mod += 1
                letter_lines += lines_rep

        if letter_mod > 0:
            print(f"[{letter}] {letter_mod} archivos actualizados ({letter_lines} condiciones restauradas en inglés)")

    t1 = time.time()
    print("=" * 65)
    print(f"Restauración completada en {t1 - t0:.2f}s")
    print(f"Total de archivos revisados: {total_files}")
    print(f"Archivos corregidos: {modified_files}")
    print(f"Total de líneas de condición restauradas a inglés: {total_lines}")
    print("=" * 65)

def main():
    parser = argparse.ArgumentParser(description="Restaurador instantáneo de condiciones a inglés original.")
    parser.add_argument('--file', '-f', type=str, help="Ruta a un archivo .md individual para restaurar")
    parser.add_argument('--letter', '-l', type=str, help="Letra específica a procesar")
    args = parser.parse_args()

    if args.file:
        src = os.path.abspath(args.file)
        if 'dialogs_es' in src:
            es_path = src
            en_path = src.replace('dialogs_es', 'dialogs_en')
        else:
            en_path = src
            es_path = src.replace('dialogs_en', 'dialogs_es')
        rep, mod = restore_file(en_path, es_path)
        print(f"Archivo procesado: {rep} líneas restauradas. Modificado: {mod}")
        return

    if args.letter:
        ltr = args.letter.upper()
        en_l = os.path.join(EN_DIR, ltr)
        es_l = os.path.join(ES_DIR, ltr)
        mod_count = 0
        line_count = 0
        for fname in sorted(os.listdir(en_l)):
            if fname.endswith('.md') and fname != 'README.md':
                rep, mod = restore_file(os.path.join(en_l, fname), os.path.join(es_l, fname))
                if mod:
                    mod_count += 1
                    line_count += rep
        print(f"Letra {ltr}: {mod_count} archivos actualizados ({line_count} condiciones restauradas).")
        return

    process_all()

if __name__ == '__main__':
    main()
