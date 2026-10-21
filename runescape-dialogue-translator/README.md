# RuneScape Dialogue Translator (Proyecto Portable)

Herramienta independiente y portátil para traducir transcripciones de diálogos de NPCs de RuneScape (`.md`) al español, diseñada específicamente para el desarrollo de plugins de traducción de clientes de RuneScape.

---

## Características Principales

1. **Autocontenido y Portátil**:
   - Incluye **todas las 3,226 transcripciones en inglés** organizadas de la `A` a la `Z` y `#`.
   - Incluye **todas las transcripciones traducidas al español** hasta la fecha (Letra `A` completa con 194 NPCs).
   - No requiere instalar paquetes externos (`pip install` no necesario). Funciona con la librería estándar de Python 3.8+.
   - Compatible con **Windows**, **Linux** y **macOS**.

2. **Reglas Estrictas de Traducción**:
   - **Ítems, armas y armaduras intactos en inglés**: `oak tree`, `oak logs`, `bronze dagger`, `dragon scimitar`, `armadyl battlestaff`, `redberries`, `planks`, `steel nails`, `coins`, etc.
   - **Lugares y sitios en inglés**: `Draynor Village`, `Draynor Manor`, `Al Kharid`, `Varrock`, `Lumbridge`, `Senntisten`, etc.
   - **Habilidades y roles en inglés**: `Attack`, `Ranged`, `Magic`, `Slayer`, `Slayer Master`, `training officer`, `Combat Instructor`, etc.
   - **Nombres de NPCs en inglés**: `Aggie`, `Ajjat`, `Ali Morrisane`, `Aubury`, `Azzanadra`, `Count Draynor`, etc.
   - **Misiones en inglés**: `Vampyre Slayer`, `Monkey Madness`, `The Feud`, `Temple at Senntisten`, etc.
   - **Comandos técnicos y plantillas wiki protegidos**: `{{Contrast|...}}`, `{{Colour|...}}`, `{{#var:...}}`, `{{Audio button|...}}`, archivos de audio `.ogg` y enlaces de imágenes.
   - **Estructura estandarizada**: `[Menu]: Selecciona una opción`, `[Choice]: ...`, `(Condition: Si el player ...)`, `(Action: ...)`.

---

## Estructura del Proyecto

```
runescape-dialogue-translator/
├── README.md                      # Esta guía de uso
├── requirements.txt               # Información de requisitos (cero dependencias externas)
├── translate.py                   # CLI principal de traducción
├── core/
│   ├── dictionaries.py            # Listas de entidades, habilidades, lugares, misiones y NPCs
│   ├── protector.py               # Motor de enmascaramiento y protección de entidades y código
│   └── engine.py                  # Motor de traducción por lotes y formateador de Markdown
├── data/
│   ├── npc_dialogue_index.json    # Índice completo de los 3,226 NPCs de RuneScape
│   ├── dialogs_en/                # Transcripciones completas en inglés (A-Z, #) [3,226 archivos]
│   └── dialogs_es/                # Transcripciones traducidas al español (A-Z, #)
└── scripts/
    ├── package_zip.py             # Script para comprimir todo el proyecto en un .zip portable
    └── verify_progress.py         # Script para consultar la tabla de progreso
```

---

## Requisitos

- **Python 3.8 o superior** instalado en el sistema.
- Conexión a Internet para la traducción automática.
- No es necesario ejecutar ningún comando `pip install`.

---

## Instrucciones de Uso (CLI)

Abre una terminal o PowerShell en la carpeta del proyecto `runescape-dialogue-translator/`:

### 1. Ver el estado y progreso de traducción
```bash
python translate.py --status
```
Muestra una tabla con cada letra, el total de NPCs en inglés, cuántos se han traducido a español y el porcentaje completado.

### 2. Traducir una o varias letras específicas (por ejemplo, la Letra C, o C, D y E)
```bash
# Traducir una sola letra:
.\translate.bat --letter C

# Traducir varias letras en lote (por comas o rangos):
.\translate.bat --letters C,D,E
.\translate.bat --letters C-F

# Ajustar hilos concurrentes en paralelo (por defecto: 4 hilos):
.\translate.bat --letters C,D,E --workers 4
```
- Procesa todos los NPCs de las letras indicadas con multihilo concurrente (4x más rápido).
- Omite automáticamente los archivos que ya hayan sido traducidos.
- Actualiza los índices de cada letra y `PROGRESS.md` automáticamente.

### 3. Ejecutar varias letras simultáneamente en ventanas independientes
Si quieres tener múltiples ventanas de consola abiertas traduciendo diferentes letras en tiempo real:
```bash
.\launch_letters.bat C D E
```
Abre 3 ventanas de CMD dedicadas, una para cada letra, trabajando en simultáneo de forma 100% segura.

### 4. Forzar re-traducción de una letra
Si deseas volver a traducir archivos ya existentes aplicando las reglas más recientes:
```bash
.\translate.bat --letter B --force
```

### 5. Traducir un archivo individual
Para probar o traducir un único NPC específico:
```bash
.\translate.bat --file data/dialogs_en/B/Bob.md
```

### 6. Traducir todas las letras restantes en secuencia
Para dejar el proceso traduciendo automáticamente de la `C` a la `Z`:
```bash
.\translate.bat --all
```

---

## Cómo Llevar el Proyecto a tu Casa (Transferencia Portable)

Para copiar todo el proyecto a tu PC de casa en un solo archivo comprimido:

1. Ejecuta el script de empaquetado:
   ```bash
   python scripts/package_zip.py
   ```
2. Esto creará el archivo comprimido:
   `runescape-dialogue-translator.zip` (aproximadamente 3 a 4 MB).
3. Copia ese `.zip` a tu pendrive, Google Drive, OneDrive o cárgalo a un repositorio Git.
4. En tu PC de casa:
   - Descomprime el `.zip`.
   - Abre la terminal en esa carpeta.
   - Ejecuta `python translate.py --letter B` para continuar exactamente donde lo dejamos.
