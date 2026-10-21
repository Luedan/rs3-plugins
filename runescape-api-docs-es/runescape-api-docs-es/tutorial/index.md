# Tutorial de Creación de Plugins

Bienvenido a la serie de tutoriales paso a paso para desarrollar plugins en la RuneScape Client API.

Esta guía está diseñada para llevarte desde cero (tu primer "Hola Mundo") hasta crear una interfaz gráfica interactiva, leer datos dinámicos del juego, responder a eventos en tiempo real y almacenar datos persistentes en el disco.

---

## Índice de la Serie

### 1. [Acceso a la API (Hola Mundo)](1helloworld.md)
* Configuración del entorno beta de desarrollo.
* Rutas de carpetas y estructura inicial.
* Creación de `plugin.json` y `main.lua`.
* Uso de la consola del cliente (`plist`, `prf`, `pon`, `poff`, `prl`).
* Depuración básica y solución de errores.

### 2. [Añadir una Interfaz de Usuario](2simpleui.md)
* Creación de ventanas flotantes con `ui.Interface`.
* Contenedores y paneles (`ui.Panel`).
* Componentes interactivos: creación de botones (`ui.Button`).
* Aplicación de estilos mediante hojas de estilo (`stylesheets`).

### 3. [Recuperar Información del Juego](3info.md)
* Diferencia entre información estática e información dinámica.
* Consultas a la base de configuraciones: objetos, NPCs, animaciones.
* Consulta de estado del jugador local (`Player.GetLocal()`) e inventarios.
* Mostrar datos dinámicos en la interfaz del plugin.

### 4. [Sistema de Eventos](4events.md)
* ¿Qué es un evento y por qué es fundamental?
* Suscripción a eventos del cliente (ej. `Events.PlayerTick`, `Events.ItemAdded`).
* Actualización automática de la interfaz en respuesta a eventos del juego.
* Limpieza y gestión del ciclo de vida del plugin.

### 5. [Base de Datos Persistente](5database.md)
* Almacenamiento local con `PersistentDB`.
* Guardar y recuperar pares clave-valor entre sesiones de juego.
* Persistencia del estado y opciones del plugin.

### 6. [Comandos Cheat de Desarrollador](6cheats.md)
* Uso de herramientas de prueba exclusivas del entorno beta.
* Teletransportes rápidos, modificación de inventario y estado.
* Buenas prácticas para no acoplar la lógica del plugin a comandos de prueba.
* Próximos pasos hacia la publicación en Mod.io.
