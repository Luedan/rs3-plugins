import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
sys.path.append(PROJ_DIR)

from translate import print_status

if __name__ == '__main__':
    print("\n=== REPORTE DE PROGRESO DE TRADUCCIÓN ===")
    print_status()
