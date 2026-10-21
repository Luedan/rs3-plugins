# RuneScape NPC Dialogue Transcripts Archive

Este repositorio contiene las transcripciones completas de los diálogos de todos los NPCs de RuneScape extraídas directamente de la [RuneScape Wiki (Category:NPC_dialogue)](https://runescape.wiki/w/Category:NPC_dialogue) en su versión original en inglés.

El propósito de este archivo es servir como base de textos originales para proyectos de localización, análisis de diálogos y desarrollo de **plugins de traducción al español para el cliente de RuneScape**.

---

## 📊 Resumen General: **3,226 NPCs** en total

| Letra | Total de NPCs | Estado | Carpeta |
| :---: | :---: | :---: | :--- |
| **#** | 2 | ✅ Descargado | [#/](./#/README.md) |
| **A** | 194 | ✅ Descargado | [A/](./A/README.md) |
| **B** | 203 | ✅ Descargado | [B/](./B/README.md) |
| **C** | 196 | ✅ Descargado | [C/](./C/README.md) |
| **D** | 136 | ✅ Descargado | [D/](./D/README.md) |
| **E** | 106 | ✅ Descargado | [E/](./E/README.md) |
| **F** | 154 | ✅ Descargado | [F/](./F/README.md) |
| **G** | 240 | ✅ Descargado | [G/](./G/README.md) |
| **H** | 138 | ✅ Descargado | [H/](./H/README.md) |
| **I** | 59 | ✅ Descargado | [I/](./I/README.md) |
| **J** | 77 | ✅ Descargado | [J/](./J/README.md) |
| **K** | 92 | ✅ Descargado | [K/](./K/README.md) |
| **L** | 127 | ✅ Descargado | [L/](./L/README.md) |
| **M** | 286 | ✅ Descargado | [M/](./M/README.md) |
| **N** | 66 | ✅ Descargado | [N/](./N/README.md) |
| **O** | 63 | ✅ Descargado | [O/](./O/README.md) |
| **P** | 126 | ✅ Descargado | [P/](./P/README.md) |
| **Q** | 15 | ✅ Descargado | [Q/](./Q/README.md) |
| **R** | 133 | ✅ Descargado | [R/](./R/README.md) |
| **S** | 368 | ✅ Descargado | [S/](./S/README.md) |
| **T** | 212 | ✅ Descargado | [T/](./T/README.md) |
| **U** | 24 | ✅ Descargado | [U/](./U/README.md) |
| **V** | 53 | ✅ Descargado | [V/](./V/README.md) |
| **W** | 87 | ✅ Descargado | [W/](./W/README.md) |
| **X** | 5 | ✅ Descargado | [X/](./X/README.md) |
| **Y** | 24 | ✅ Descargado | [Y/](./Y/README.md) |
| **Z** | 40 | ✅ Descargado | [Z/](./Z/README.md) |

---

## 📁 Formato de los Archivos de Diálogo

Cada archivo `.md` de un NPC contiene el árbol de interacción completo con la siguiente estructura limpia:

```markdown
### Ubicación / Contexto

- **Nombre NPC:** Texto del diálogo en inglés...
- ((Condición o prerrequisito))
  - [Menu]: Título de la lista de opciones
    - [Choice]: Texto de la opción que el jugador puede seleccionar
      - **Player:** Respuesta del jugador...
      - **Nombre NPC:** Respuesta del NPC...
```

---

## 🛠️ Cómo descargar las siguientes letras

Para continuar descargando cualquier otra letra (ejemplo: `B`, `C`, etc.):
```bash
python download_npc_dialogues.py B
```
O podemos ir procesándolas letra por letra según lo solicites.
