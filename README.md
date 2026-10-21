# Entorno de Desarrollo de Plugins para RuneScape (Client API)

Espacio de trabajo modular y organizado para desarrollar, probar y empaquetar múltiples plugins para el cliente oficial de **RuneScape (RS3)** utilizando **Lua 5.4.8**.

---

## 📁 Estructura del Repositorio

```text
rs-plugins/
├── plugins/                        # Carpeta raíz de todos los plugins
│   └── test-plugin/                # Plugin de prueba inicial listo para usar
│       ├── plugin.json             # Manifiesto oficial del plugin
│       ├── main.lua                # Punto de entrada y ciclo de vida (PluginShutdown)
│       ├── README.md               # Instrucciones específicas de este plugin
│       └── src/
│           ├── config.lua          # Configuración y almacenamiento persistente
│           ├── monitor.lua         # Escucha de ticks y lectura de datos del jugador
│           └── ui.lua              # Interfaz gráfica (Ribbon y Plugin Hub Settings)
├── shared/                         # Módulos y librerías Lua compartidas entre plugins
│   ├── logger.lua                  # Utilidad de logging con etiquetas y niveles
│   ├── event_manager.lua           # Gestor seguro de eventos y limpieza automática
│   └── storage.lua                 # Envoltorio seguro sobre PersistentDB
├── tools/                          # Herramientas de automatización en PowerShell
│   ├── sync-plugins.ps1            # Enlaza los plugins a dev_plugins mediante Junctions en tiempo real
│   ├── create-plugin.ps1           # Genera la estructura de un nuevo plugin con un comando
│   └── package-plugin.ps1          # Valida y empaqueta el plugin en ZIP para Mod.io
├── types/                          # Definiciones de tipos Lua (EmmyLua / LuaLS)
│   └── runescape-api.d.lua         # Autocompletado del API oficial para VS Code
├── dist/                           # Salida de paquetes .zip listos para publicar
├── runescape-api-docs-es/          # Documentación técnica completa de la API en Español
└── .luarc.json                     # Configuración del Lua Language Server
```

---

## 🚀 Inicio Rápido en Git Bash (`./rs.sh`)

Puedes hacer todo desde **Git Bash** con el script principal `./rs.sh`:

```bash
# 1. Enlazar plugins a RuneScape Beta (tiempo real con NTFS Junctions)
./rs.sh sync

# 2. Crear un nuevo plugin listo para desarrollar
./rs.sh new mi-plugin "Nombre Del Plugin"

# 3. Empaquetar un plugin en .zip para Mod.io
./rs.sh pack mi-plugin

# 4. Listar tus plugins
./rs.sh list

# 5. Limpiar enlaces
./rs.sh clean
```

> **Nota:** Al usar Junctions, **cualquier cambio que guardes en tus archivos `.lua` se refleja de inmediato en el juego**, sin tener que volver a sincronizar.

---

## 🎮 Comandos de Consola del Cliente RuneScape

Dentro del juego en el mundo Beta, abre la consola con **`ALT` + `` ` ``**:
* **`prf`**: Refresca la lista de plugins del disco.
* **`plist`**: Muestra los plugins detectados.
* **`pon <nombre>`**: Enciende el plugin (ej: `pon test-plugin`).
* **`poff <nombre>`**: Apaga el plugin.
* **`prl <nombre>`**: **Recarga el plugin** (usa esto tras guardar cambios en el código).

---

## 🛠️ Herramientas de Desarrollo

### 1. Crear un nuevo plugin (`create-plugin.ps1`)
Para comenzar un nuevo plugin con toda su estructura base y manifiesto:
```powershell
.\tools\create-plugin.ps1 -PluginId "mi-nuevo-plugin" -DisplayName "Mi Nuevo Plugin" -Email "tu@email.com" -AutoSync
```
* Parámetro `-PrettyUI`: Añade dependencia a la librería de interfaz `prettyui`.
* Parámetro `-AutoSync`: Crea de inmediato el enlace directo con la beta.

### 2. Sincronizar todos los plugins (`sync-plugins.ps1`)
```powershell
# Enlazar todos los plugins en dev_plugins
.\tools\sync-plugins.ps1

# Enlazar un plugin en concreto
.\tools\sync-plugins.ps1 -PluginName mi-nuevo-plugin

# Limpiar enlaces
.\tools\sync-plugins.ps1 -Clean
```

### 3. Empaquetar para Mod.io (`package-plugin.ps1`)
Cuando tu plugin esté listo para ser subido a [Mod.io RuneScape](https://mod.io/g/runescape):
```powershell
.\tools\package-plugin.ps1 -PluginName mi-nuevo-plugin
```
Este comando valida que `plugin.json` tenga todos los campos exigidos por Jagex (`name`, `version`, `contactEmailAddress`) y comprime los archivos en `dist/mi-nuevo-plugin-v1.0.0.zip` respetando la raíz.

---

## 🎮 Comandos de Consola del Cliente RuneScape

| Comando | Descripción |
| :--- | :--- |
| **`plist`** | Muestra la lista de plugins detectados en `dev_plugins`. |
| **`prf`** | Refresca el directorio `dev_plugins` desde el disco. |
| **`pon <nombre>`** | Activa y ejecuta el plugin indicado. |
| **`poff <nombre>`** | Desactiva el plugin indicado. |
| **`prl <nombre>`** | Recarga el plugin (equivale a `poff` seguido de `pon`). |

### Comandos Cheat de Prueba (Solo en Mundo Beta)
* `tpto <lugar>`: Teletransporte rápido (ej. `tpto varrock`, `tpto lumbridge`, `tpto grandexchange`).
* `give <id> [cantidad]`: Añade objetos a la mochila (ej. `give 4151 1` para un látigo abisal).
* `empty`: Vacía completamente tu inventario.
* `sethp <cantidad>`: Establece tus puntos de vida actuales.
* `setstats <nivel>`: Establece todos tus niveles (ej. `setstats 99`).

---

## 🛡️ Directrices Oficiales de Jagex

Al diseñar tus plugins, ten siempre presentes las directrices oficiales:
1. **Regla de 1:1**: 1 acción del jugador = 1 acción en el juego. **Está prohibida la automatización, macros o simulación de clics**.
2. **Privacidad**: No recopilar ni transmitir información confidencial o credenciales del usuario.
3. **Cierre Limpio**: Todo plugin debe implementar `PluginShutdown()` para cancelar eventos (`Unsubscribe`) y evitar fugas de memoria en el cliente.
4. **Respeto a la Interfaz**: Los plugins deben integrarse armoniosamente en el estilo visual del juego.
