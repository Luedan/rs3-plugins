#!/usr/bin/env python3
"""
RuneScape NPC Dialogue Translator
Traductor portátil de transcripciones de diálogos de RuneScape al español.
Preserva intactos en inglés: ítems, armas, armaduras, ubicaciones, habilidades, misiones, NPCs,
comandos de wiki (Contrast, Colour, Audio button, #var) y mecánicas de juego.
Soporta procesamiento concurrente por hilos (--workers) y selección de múltiples letras (--letters).
"""

import os
import sys
import argparse
import time
import urllib.parse
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from core.engine import translate_file_content

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
EN_DIR = os.path.join(DATA_DIR, 'dialogs_en')
ES_DIR = os.path.join(DATA_DIR, 'dialogs_es')

ALL_LETTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '#'
]

progress_lock = threading.Lock()

def get_letter_stats():
    stats = {}
    for letter in ALL_LETTERS:
        src_l = os.path.join(EN_DIR, letter)
        dst_l = os.path.join(ES_DIR, letter)
        total_en = 0
        total_es = 0
        if os.path.exists(src_l):
            total_en = len([f for f in os.listdir(src_l) if f.endswith('.md') and f != 'README.md'])
        if os.path.exists(dst_l):
            total_es = len([f for f in os.listdir(dst_l) if f.endswith('.md') and f != 'README.md'])
        stats[letter] = (total_en, total_es)
    return stats

def get_next_pending_letter():
    stats = get_letter_stats()
    for letter in ALL_LETTERS:
        tot_en, tot_es = stats[letter]
        if tot_es < tot_en and tot_en > 0:
            return letter
    return None

def parse_letters(input_str):
    """Parsea una cadena de letras como 'C', 'C,D,E', 'C-F', 'ALL'."""
    if not input_str:
        return []
    result = []
    parts = [p.strip().upper() for p in input_str.split(',') if p.strip()]
    for part in parts:
        if '-' in part:
            sub = part.split('-')
            if len(sub) == 2 and len(sub[0]) == 1 and len(sub[1]) == 1:
                start_ch, end_ch = sub[0], sub[1]
                if start_ch in ALL_LETTERS and end_ch in ALL_LETTERS:
                    s_idx = ALL_LETTERS.index(start_ch)
                    e_idx = ALL_LETTERS.index(end_ch)
                    if s_idx <= e_idx:
                        for idx in range(s_idx, e_idx + 1):
                            l = ALL_LETTERS[idx]
                            if l not in result:
                                result.append(l)
                        continue
        if part in ALL_LETTERS and part not in result:
            result.append(part)
        elif part == 'ALL':
            return list(ALL_LETTERS)
    return result

def update_progress_markdown():
    """Genera y actualiza automáticamente PROGRESS.md con el estado actual del proyecto de forma segura."""
    with progress_lock:
        stats = get_letter_stats()
        progress_file = os.path.join(BASE_DIR, 'PROGRESS.md')

        grand_total_en = sum(s[0] for s in stats.values())
        grand_total_es = sum(s[1] for s in stats.values())
        grand_pct = (grand_total_es / grand_total_en * 100) if grand_total_en > 0 else 0.0

        completed_letters = [l for l, (en, es) in stats.items() if es >= en and en > 0]
        in_progress_letters = [l for l, (en, es) in stats.items() if 0 < es < en and en > 0]
        pending_letters = [l for l, (en, es) in stats.items() if es == 0 and en > 0]

        next_letter = get_next_pending_letter()

        bar_len = 25
        filled_len = int(bar_len * grand_pct / 100)
        bar_str = "█" * filled_len + "░" * (bar_len - filled_len)

        lines = []
        lines.append("# Estado y Progreso de Traducción de NPCs de RuneScape\n\n")
        lines.append("> **Documento de seguimiento automático**: Se actualiza automáticamente cada vez que se traduce una letra o archivo.\n\n")
        lines.append("## Resumen General\n\n")
        lines.append(f"- **Total de NPCs en el juego**: `{grand_total_en:,}`\n")
        lines.append(f"- **Total de NPCs traducidos al español**: `{grand_total_es:,}` (**{grand_pct:.1f}%**)\n")
        lines.append(f"- **Total de NPCs pendientes**: `{grand_total_en - grand_total_es:,}`\n")
        lines.append(f"- **Progreso Global**: `[{bar_str}] {grand_pct:.1f}%`\n")
        lines.append(f"- **Letras Completadas ({len(completed_letters)}/27)**: `{'`, `'.join(completed_letters)}`\n")
        if in_progress_letters:
            lines.append(f"- **Letras en Progreso**: `{'`, `'.join(in_progress_letters)}`\n")
        if next_letter:
            next_remaining = stats[next_letter][0] - stats[next_letter][1]
            lines.append(f"- **Siguiente Letra Pendiente**: **`{next_letter}`** ({next_remaining} NPCs restantes)\n")
        lines.append(f"- **Última actualización**: `{time.strftime('%Y-%m-%d %H:%M:%S')}`\n\n")

        lines.append("## ¿Cómo continuar traduciendo en tu PC?\n\n")
        lines.append("Abre la terminal en la carpeta del proyecto y ejecuta:\n\n")
        lines.append("```bash\n")
        lines.append("# Opción A: Continuar automáticamente con la siguiente letra pendiente\n")
        lines.append("python translate.py --next\n\n")
        if next_letter:
            lines.append(f"# Opción B: Traducir una letra específica o varias (ej: C,D,E)\n")
            lines.append(f"python translate.py --letters {next_letter}\n\n")
        lines.append("# Opción C: Ver la tabla de progreso en consola\n")
        lines.append("python translate.py --status\n")
        lines.append("```\n\n")

        lines.append("## Tabla de Progreso por Letra (A-Z, #)\n\n")
        lines.append("| Letra | Estado | Total (EN) | Traducidos (ES) | Progreso | Carpeta de Diálogos |\n")
        lines.append("|:-----:|:------:|:----------:|:---------------:|:--------:|:-------------------:|\n")

        for letter, (tot_en, tot_es) in stats.items():
            pct = (tot_es / tot_en * 100) if tot_en > 0 else 0.0
            if tot_es >= tot_en and tot_en > 0:
                status_icon = "✅ COMPLETO"
            elif tot_es > 0:
                status_icon = "⏳ EN PROGRESO"
            else:
                status_icon = "⏸️ PENDIENTE"

            folder_link = f"[Ver diálogos (ES)](./data/dialogs_es/{urllib.parse.quote(letter)}/)"
            lines.append(f"| **{letter}** | {status_icon} | {tot_en} | {tot_es} | {pct:5.1f}% | {folder_link} |\n")

        content = "".join(lines)
        for _ in range(5):
            try:
                with open(progress_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                break
            except (IOError, PermissionError):
                time.sleep(0.2)

    return progress_file

def print_status():
    stats = get_letter_stats()
    print("=" * 65)
    print(f"{'LETRA':<8}{'TOTAL (EN)':<15}{'TRADUCIDOS (ES)':<18}{'ESTADO':<15}{'PROGRESO':<10}")
    print("=" * 65)
    grand_total_en = 0
    grand_total_es = 0
    for letter, (tot_en, tot_es) in stats.items():
        grand_total_en += tot_en
        grand_total_es += tot_es
        pct = (tot_es / tot_en * 100) if tot_en > 0 else 0.0
        status = "COMPLETO" if tot_es >= tot_en and tot_en > 0 else ("EN PROGRESO" if tot_es > 0 else "PENDIENTE")
        bar = f"{pct:5.1f}%"
        print(f"  {letter:<6}{tot_en:<15}{tot_es:<18}{status:<15}{bar:<10}")
    print("=" * 65)
    grand_pct = (grand_total_es / grand_total_en * 100) if grand_total_en > 0 else 0.0
    print(f"TOTAL:  {grand_total_en:<15}{grand_total_es:<18}{grand_pct:5.1f}%")
    print("=" * 65)

    next_letter = get_next_pending_letter()
    if next_letter:
        print(f"\n>> Siguiente letra pendiente: '{next_letter}' ({stats[next_letter][0] - stats[next_letter][1]} NPCs)")
        print(f">> Para continuar ejecuta: python translate.py --next  o  python translate.py --letters {next_letter}")
    else:
        print("\n>> ¡Todos los NPCs de todas las letras han sido traducidos exitosamente!")

    # Auto-update PROGRESS.md
    update_progress_markdown()

def update_letter_readme(letter):
    dst_letter_dir = os.path.join(ES_DIR, letter)
    if not os.path.exists(dst_letter_dir):
        return
    files = sorted([f for f in os.listdir(dst_letter_dir) if f.endswith('.md') and f != 'README.md'])
    readme_path = os.path.join(dst_letter_dir, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as rf:
        rf.write(f"# Transcripciones de Diálogos de NPCs - Letra {letter}\n\n")
        rf.write(f"- **Total NPCs**: {len(files)}\n")
        rf.write(f"- **Idioma**: Español\n")
        rf.write(f"- **Reglas de Traducción**: Diálogos traducidos al español natural, preservando estrictamente en inglés nombres de ítems, armas, armaduras, ubicaciones, habilidades, misiones, comandos de wiki (Contrast, Colour, Audio button, variables) y mecánicas de juego.\n\n")
        rf.write("## Índice de NPCs\n\n")
        for f in files:
            npc_clean = f[:-3]
            rf.write(f"- [{npc_clean}](./{urllib.parse.quote(f)})\n")

def process_file(src_path, dst_path, force=False):
    if not force and os.path.exists(dst_path) and os.path.getsize(dst_path) > 100:
        try:
            with open(dst_path, 'r', encoding='utf-8') as f:
                header = f.read(300)
                if '- **Language**:' in header:
                    return 'skipped'
        except:
            pass
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
    translated = translate_file_content(content)
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    return 'translated'

def process_letter(letter, force=False, workers=4):
    letter = letter.upper()
    src_letter_dir = os.path.join(EN_DIR, letter)
    dst_letter_dir = os.path.join(ES_DIR, letter)

    if not os.path.exists(src_letter_dir):
        print(f"Error: No existe el directorio de origen para la letra {letter}: {src_letter_dir}")
        return False

    os.makedirs(dst_letter_dir, exist_ok=True)
    files = sorted([f for f in os.listdir(src_letter_dir) if f.endswith('.md') and f != 'README.md'])
    total = len(files)

    print(f"\n{'='*70}", flush=True)
    print(f"Iniciando traducción para Letra {letter} ({total} NPCs) (force={force}, workers={workers})", flush=True)
    print(f"{'='*70}\n", flush=True)

    t0 = time.time()
    translated_count = 0
    skipped_count = 0
    error_count = 0
    print_lock = threading.Lock()
    done_counter = 0

    def task(fname):
        src_p = os.path.join(src_letter_dir, fname)
        dst_p = os.path.join(dst_letter_dir, fname)
        f_start = time.time()
        try:
            res = process_file(src_p, dst_p, force=force)
            elapsed = time.time() - f_start
            return (fname, res, elapsed, None)
        except Exception as e:
            return (fname, 'error', 0, str(e))

    if workers <= 1:
        for i, fname in enumerate(files, 1):
            fname, res, elapsed, err = task(fname)
            if res == 'skipped':
                skipped_count += 1
                print(f"[{i:03d}/{total:03d}] [OMITIDO] {fname} (ya traducido)", flush=True)
            elif res == 'error':
                error_count += 1
                print(f"[{i:03d}/{total:03d}] [ERROR] {fname}: {err}", flush=True)
            else:
                translated_count += 1
                print(f"[{i:03d}/{total:03d}] [OK {elapsed:4.1f}s] {fname}", flush=True)
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            future_to_fname = {executor.submit(task, fname): fname for fname in files}
            for future in as_completed(future_to_fname):
                fname, res, elapsed, err = future.result()
                with print_lock:
                    done_counter += 1
                    if res == 'skipped':
                        skipped_count += 1
                        print(f"[{done_counter:03d}/{total:03d}] [OMITIDO] {fname} (ya traducido)", flush=True)
                    elif res == 'error':
                        error_count += 1
                        print(f"[{done_counter:03d}/{total:03d}] [ERROR] {fname}: {err}", flush=True)
                    else:
                        translated_count += 1
                        print(f"[{done_counter:03d}/{total:03d}] [OK {elapsed:4.1f}s] {fname}", flush=True)

    total_time = time.time() - t0
    update_letter_readme(letter)
    update_progress_markdown()

    print(f"\n{'-'*70}", flush=True)
    print(f"Letra {letter} finalizada en {total_time:.1f}s", flush=True)
    print(f"Traducidos: {translated_count} | Omitidos: {skipped_count} | Errores: {error_count}", flush=True)
    print(f"README.md actualizado en {dst_letter_dir}", flush=True)
    print(f"PROGRESS.md actualizado en la raíz del proyecto", flush=True)
    print(f"{'-'*70}\n", flush=True)
    return error_count == 0

def main():
    parser = argparse.ArgumentParser(
        description="RuneScape NPC Dialogue Translator - CLI",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--letter', '-l',
        type=str,
        help="Letra o letras a traducir (ej: --letter C  o  --letter C,D,E  o  --letter C-F)"
    )
    parser.add_argument(
        '--letters', '-L',
        type=str,
        help="Alias para especificar múltiples letras (ej: --letters C,D,E o --letters C-G)"
    )
    parser.add_argument(
        '--workers', '-w',
        type=int,
        default=4,
        help="Número de hilos concurrentes para procesar en paralelo (por defecto: 4)"
    )
    parser.add_argument(
        '--next', '-n',
        action='store_true',
        help="Traduce automáticamente la siguiente letra pendiente en orden alfabético"
    )
    parser.add_argument(
        '--all', '-a',
        action='store_true',
        help="Traduce todas las letras pendientes secuencialmente"
    )
    parser.add_argument(
        '--status', '-s',
        action='store_true',
        help="Muestra una tabla con el progreso actual de todas las letras y actualiza PROGRESS.md"
    )
    parser.add_argument(
        '--file', '-f',
        type=str,
        help="Traduce un archivo específico. Ejemplo: --file data/dialogs_en/B/Bob.md"
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help="Fuerza la re-traducción incluso si el archivo ya existe en dialogs_es"
    )

    args = parser.parse_args()

    if args.status:
        print_status()
        return

    if args.file:
        src = os.path.abspath(args.file)
        if not os.path.exists(src):
            print(f"Error: Archivo no encontrado: {src}")
            return
        rel = os.path.relpath(src, EN_DIR)
        dst = os.path.join(ES_DIR, rel)
        t0 = time.time()
        print(f"Traduciendo archivo individual: {rel}...")
        res = process_file(src, dst, force=args.force)
        print(f"Resultado: {res} en {time.time() - t0:.2f}s -> {dst}")
        update_progress_markdown()
        return

    letters_input = args.letters or args.letter
    if letters_input:
        target_letters = parse_letters(letters_input)
        if not target_letters:
            print(f"Error: No se reconocieron letras válidas en: '{letters_input}'")
            return
        print(f"Letras seleccionadas para procesar ({len(target_letters)}): {', '.join(target_letters)}")
        for l in target_letters:
            process_letter(l, force=args.force, workers=args.workers)
        print_status()
        return

    if args.next:
        next_letter = get_next_pending_letter()
        if not next_letter:
            print("¡Todas las letras están completadas!")
            return
        print(f"Detectada siguiente letra pendiente: '{next_letter}'")
        process_letter(next_letter, force=args.force, workers=args.workers)
        return

    if args.all:
        for letter in ALL_LETTERS:
            process_letter(letter, force=args.force, workers=args.workers)
        print_status()
        return

    # Default action if no flags provided
    parser.print_help()
    print("\nEstado actual del proyecto:")
    print_status()

if __name__ == '__main__':
    main()
