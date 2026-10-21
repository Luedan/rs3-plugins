# RS Test Plugin

Plugin de prueba diseñado para validar la integración con la RuneScape Client API en el entorno Beta de desarrolladores.

## ¿Qué demuestra este plugin?
1. **Ciclo de vida completo**: Carga limpia y descarga ordenada con `PluginShutdown()` sin fugas de memoria.
2. **Sistema de Eventos**: Suscripción segura a `Event.PlayerTick` (cada 600 ms).
3. **Lectura de Estado en Tiempo Real**: Consulta de nombre de jugador, nivel de combate, energía de correr y coordenadas en `CoordGrid`.
4. **Almacenamiento Persistente (`PersistentDB`)**: Guarda en disco un contador de clics y las preferencias del usuario entre sesiones.
5. **Interfaz de Usuario dual**:
   * **Capa de Contenido (Ribbon)**: Muestra información en vivo del jugador y un botón interactivo.
   * **Capa de Ajustes (Plugin Hub > Settings)**: Casillas de verificación para activar/desactivar registros de ticks y alertas.

## Cómo Probarlo en RuneScape Beta
1. Sincroniza el plugin ejecutando desde la raíz del proyecto:
   ```powershell
   .\tools\sync-plugins.ps1 -PluginName test-plugin
   ```
2. Inicia sesión en el mundo Beta de RuneScape.
3. Abre la consola del cliente con la combinación de teclas **`ALT` + `` ` ``** (o `ALT` + `~`).
4. Ejecuta:
   ```text
   prf
   pon test-plugin
   ```
5. Abre la ventana flotante de **Plugins** en el cliente y haz clic en el icono del listón de **RS Test Plugin**.
6. Cada vez que edites el código, solo escribe en la consola:
   ```text
   prl test-plugin
   ```
