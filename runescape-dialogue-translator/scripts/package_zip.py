import os
import zipfile
import time

def make_zip():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_zip = os.path.abspath(os.path.join(base_dir, '..', 'runescape-dialogue-translator.zip'))
    
    print(f"Empaquetando proyecto en: {output_zip}")
    t0 = time.time()
    
    file_count = 0
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for root, dirs, files in os.walk(base_dir):
            # Ignore cache
            if '__pycache__' in root or '.git' in root:
                continue
            for f in files:
                if f.endswith('.pyc') or f.endswith('.tmp'):
                    continue
                abs_path = os.path.join(root, f)
                rel_path = os.path.relpath(abs_path, os.path.join(base_dir, '..'))
                zf.write(abs_path, rel_path)
                file_count += 1
                if file_count % 500 == 0:
                    print(f"  Empaquetados {file_count} archivos...", flush=True)

    size_mb = os.path.getsize(output_zip) / (1024 * 1024)
    print(f"\n¡Empaquetado exitoso!")
    print(f"- Archivo ZIP: {output_zip}")
    print(f"- Total de archivos: {file_count}")
    print(f"- Tamaño comprimido: {size_mb:.2f} MB")
    print(f"- Tiempo transcurrido: {time.time() - t0:.1f}s")

if __name__ == '__main__':
    make_zip()
