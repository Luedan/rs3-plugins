# Documentación Oficial de RuneScape Client API (en Español)

Bienvenido a la versión completa y en español de la **RuneScape Client API**. Esta documentación técnica te permitirá programar plugins, extensiones de interfaz y utilidades para el cliente oficial de RuneScape utilizando **Lua 5.4.8**.

---

## 🗺️ Mapa de Contenidos

### 🚀 Primeros Pasos y Conceptos Base
* **[Empezando con la API](getting-started.md)**: Visión global de la API, tipos de datos y primeros conceptos.
* **[Gestión de Plugins](managing.md)**: Uso de la consola (`plist`, `pon`, `poff`, `prl`).
* **[Estructura del Plugin](structure.md)**: Carpetas, manifiesto `plugin.json` y permisos.
* **[Comandos Cheat de Desarrollador](cheats.md)**: Comandos especiales de teletransporte y generación de objetos en el entorno beta.

---

### 📚 Tutorial Paso a Paso
Una serie guiada pensada para desarrolladores que arrancan desde cero:
1. **[1. Acceso a la API (Hola Mundo)](tutorial/1helloworld.md)**: Configura la beta, tu primer plugin y la consola.
2. **[2. Añadir una Interfaz de Usuario](tutorial/2simpleui.md)**: Ventanas (`Interface`), paneles y botones (`Button`).
3. **[3. Recuperar Información del Juego](tutorial/3info.md)**: Datos estáticos de objetos/NPCs y datos dinámicos del jugador.
4. **[4. Sistema de Eventos](tutorial/4events.md)**: Suscripción a ticks y actualizaciones del juego.
5. **[5. Base de Datos Persistente](tutorial/5database.md)**: Guardar configuraciones y progreso en el disco con `PersistentDB`.
6. **[6. Cheats de Desarrollo](tutorial/6cheats.md)**: Acelerar pruebas y validaciones.
* **[Índice Completo de Tutoriales](tutorial/index.md)**.

---

### 🛡️ Publicación y Normativa
* **[Directrices de Plugins](submission/guidelines.md)**: Lo que está permitido y prohibido por Jagex.
* **[Proceso de Publicación](submission/process.md)**: Cómo subir tu plugin a Mod.io y flujo de moderación.
* **[Adecuación Legal](submission/adequacy.md)**: Tratamiento de datos y normativa de privacidad.
* **[Ejemplo de Envío](submission/example.md)**: Caso práctico de entrega de un plugin.

---

### ⚙️ Núcleo del Motor (`core`)
Funcionalidades base del entorno de ejecución:
* **[Descripción del Core](core/index.md)**
* **[Opciones del Cliente (`ClientOptions`)](core/clientoptions.md)**: Configuración gráfica y opciones del juego.
* **[Eventos (`Events`)](core/events.md)**: Lista exhaustiva de todos los eventos del cliente a los que suscribirse.
* **[HTTP (`Http`)](core/http.md)**: Peticiones web externas (GET, POST).
* **[Teclado (`Keyboard`)](core/keyboard.md)**: Detección y atajos de teclado.
* **[Ratón (`Mouse`)](core/mouse.md)**: Posición del cursor y pulsaciones.
* **[Base de Datos (`PersistentDB`)](core/persistentdb.md)**: Persistencia local SQLite clave-valor.
* **[Plugin (`Plugin`)](core/plugin.md)**: Metadatos y control del plugin actual.
* **[Utilidades de Cadenas (`String`)](core/string.md)**: Manipulación y formateo de texto.

---

### 🎮 Módulo del Juego (`game`)
Interacción directa con el mundo de RuneScape:
* **[Descripción de Game](game/index.md)**
* **[Cámara (`Camera`)](game/camera.md)**: Posición, orientación y enfoque de la cámara activa.
* **[Chat (`Chat`)](game/chat.md)**: Lectura y envío de mensajes en los canales de chat.
* **[Coordenadas Finas (`CoordFine`)](game/coordfine.md)**: Posiciones en unidades de sub-casilla (precisión milimétrica).
* **[Coordenadas de Cuadrícula (`CoordGrid`)](game/coordgrid.md)**: Posiciones en casillas estándar del mapa (`x, y, plano`).
* **[Grand Exchange (`GrandExchange`)](game/grandexchange.md)**: Ofertas de compra/venta y precios de mercado.
* **[Inventario (`Inventory`)](game/inventory.md)**: Mochila, equipo, banco y cofres.
* **[Minimenú (`MiniMenu`)](game/minimenu.md)**: Menú contextual que aparece al hacer clic secundario.
* **[Jugador (`Player`)](game/player.md)**: Salud, nivel de combate, nombres y estado del personaje.
* **[Conversión de Pantalla (`ScreenConvert`)](game/screenconvert.md)**: Traducir coordenadas del mundo 3D a píxeles 2D de pantalla.
* **[Formas (`Shapes`)](game/shapes.md)**: Primitivas geométricas y áreas en el espacio.
* **[Mundo (`World`)](game/world.md)**: Estado del servidor, tiempo de juego y entorno.

#### Configuraciones y Tipos del Juego (`game/config/`)
Consulta de definiciones estáticas de la caché de RuneScape:
* [`ItemType`](game/config/objtype.md) (Objetos), [`NpcType`](game/config/npctype.md) (NPCs), [`LocType`](game/config/loctype.md) (Objetos de mapa/escenarios), [`QuestType`](game/config/questtype.md) (Misiones), [`AchievementType`](game/config/achievementtype.md) (Logros), [`EnumType`](game/config/enumtype.md), [`StructType`](game/config/structtype.md), [`VarType`](game/config/vartype.md), [`ParamType`](game/config/paramtype.md), [`SeqType`](game/config/seqtype.md), [`SpotAnimType`](game/config/spotanimtype.md), [`InvType`](game/config/invtype.md), [`HitmarkType`](game/config/hitmarktype.md), [`HeadbarType`](game/config/headbartype.md), [`FontType`](game/config/fonttype.md), [`CursorType`](game/config/cursortype.md), [`DBTableType`](game/config/dbtabletype.md), [`DBRowType`](game/config/dbrowtype.md), [`BaseAnimSetType`](game/config/baseanimsettype.md), [`MapElementType`](game/config/mapelementtype.md).

#### Entidades y Listas (`game/entity/` y `game/list/`)
* **Entidades**: [`PlayerEntity`](game/entity/playerentity.md), [`NpcEntity`](game/entity/npcentity.md), [`LocEntity`](game/entity/locentity.md), [`ObjStackEntity`](game/entity/objstackentity.md).
* **Listas de Búsqueda**: [`PlayerList`](game/list/playerlist.md), [`NpcList`](game/list/npclist.md), [`LocList`](game/list/loclist.md), [`ObjStackList`](game/list/objstacklist.md), [`ShapeList`](game/list/shapelist.md).

---

### 🎨 Sistema de Interfaz de Usuario (`ui`)
Crea ventanas y widgets con estética idéntica al cliente oficial:
* **[Descripción General de UI](ui/index.md)**
* **[Tipos Comunes](ui/common_types.md)**, **[Componente Base (`Component`)](ui/component.md)**, **[Ventanas (`Interface`)](ui/interface.md)**, **[Hojas de Estilo (`Stylesheets`)](ui/stylesheets.md)**, **[Colección de Componentes](ui/component_collection.md)**, **[Configuraciones de Componentes](ui/component_configs.md)**.

#### Componentes Decorativos (`ui/decorative_components/`)
* [`Text`](ui/decorative_components/text.md) (Etiquetas de texto), [`Sprite`](ui/decorative_components/sprite.md) (Iconos e imágenes de juego), [`Rectangle`](ui/decorative_components/rectangle.md) (Rectángulos de color), [`Line`](ui/decorative_components/line.md) (Líneas), [`Canvas`](ui/decorative_components/canvas.md) (Lienzo personalizado), [`Model`](ui/decorative_components/model.md) (Modelos 3D interactivos), [`ModelGroup`](ui/decorative_components/modelgroup.md), [`RadialProgressOverlay`](ui/decorative_components/radial_progress_overlay.md) (Barras de progreso circulares).

#### Componentes Interactivos (`ui/interactive_components/`)
* [`Button`](ui/interactive_components/button.md) (Botones), [`InputField`](ui/interactive_components/input_field.md) (Campos de entrada de texto), [`Check`](ui/interactive_components/check.md) (Casillas de verificación), [`Slider`](ui/interactive_components/slider.md) (Barras de desplazamiento), [`List`](ui/interactive_components/list.md) (Listas seleccionables), [`ComboField`](ui/interactive_components/combo_field.md) (Listas desplegables), [`RadioGroup`](ui/interactive_components/radio_group.md) (Grupos de radio), [`Carousel`](ui/interactive_components/carousel.md) (Carruseles).

#### Componentes de Maquetación (`ui/layout_components/`)
* [`Panel`](ui/layout_components/panel.md) (Paneles contenedores), [`Grid`](ui/layout_components/grid.md) (Cuadrículas automáticas), [`GroupBox`](ui/layout_components/group_box.md) (Cajas de agrupación con título), [`Layer`](ui/layout_components/layer.md) (Capas), [`PagedLayer`](ui/layout_components/paged_layer.md) (Capas con paginación), [`PagedCarousel`](ui/layout_components/paged_carousel.md), [`CutsceneLayer`](ui/layout_components/cutscene_layer.md).

---

### 📐 Matemáticas y Utilidades (`math`, `audio`, `requests`)
* **Matemáticas**: [`Vector`](math/vector.md) (`Vector2`, `Vector3`), [`Matrix`](math/matrix.md), [`Quaternion`](math/quaternion.md), [`Rect`](math/rect.md), [`AABB`](math/aabb.md).
* **[Audio](audio/index.md)**: Control de reproducción de sonidos, pistas de música y efectos ambientales.
* **[Peticiones (Requests)](requests/index.md)**: Gestión de solicitudes asíncronas.

---

*Documentación adaptada y traducida al español para la comunidad de desarrolladores de RuneScape.*
