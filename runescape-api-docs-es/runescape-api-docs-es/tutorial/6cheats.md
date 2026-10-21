# 6. Comandos Cheat de Desarrollador

Durante la creación de un plugin necesitas probar situaciones difíciles de reproducir en el juego normal (ej. tener 1 punto de vida, poseer un objeto rarísimo o estar en una mazmorra lejana). Para esto, el entorno beta incluye **comandos cheat de desarrollo**.

> **Información Crucial**  
> Estos comandos **SOLO** existen en el mundo beta de desarrollo. Están totalmente deshabilitados en el juego en vivo y la moderación rechazará cualquier plugin cuya lógica dependa de ellos.

---

## Objetivos
* Usar comandos cheat desde la consola para agilizar pruebas.
* Teletransportes instantáneos a zonas clave.
* Generación de objetos en el inventario para validar interfaces.
* Concluir el tutorial y preparar el plugin para su uso real.

---

## Comandos Cheat Más Útiles

Los comandos se escriben directamente en la consola (`ALT` + `` ` ``):

### Teletransporte
* **`tp <x> <y> <plano>`**: Teletransporta a coordenadas exactas de cuadrícula.
* **`tpto <nombre>`**: Teletransporta a ubicaciones conocidas con nombre:
  * `tpto lumbridge`
  * `tpto varrock`
  * `tpto prifddinas`
  * `tpto grandexchange`

### Manipulación de Objetos
* **`give <id_objeto> [cantidad]`**: Añade el objeto especificado a tu inventario.
  * `give 4151 1` (Añade un látigo abisal).
  * `give 995 1000000` (Añade 1,000,000 monedas).
* **`empty`**: Vacía por completo tu inventario actual para pruebas limpias.

### Estado del Personaje
* **`sethp <cantidad>`**: Fija tus puntos de vida actuales (ideal para probar alertas de baja salud).
* **`setstats <nivel>`**: Ajusta todos tus niveles de habilidad al valor deseado (ej. `setstats 99`).

Consulta la referencia completa de todos los comandos en [Comandos Cheat (Referencia Completa)](../cheats.md).

---

## ¡Felicidades! Has Completado la Serie de Tutoriales

Ahora dominas los 5 pilares del desarrollo de plugins para RuneScape:
1. **Configuración y Ciclo de Vida**: Manifiesto, carga y consola.
2. **Interfaces Gráficas**: Ventanas, paneles, botones y estilos.
3. **Lectura de Datos**: Objetos, inventario, coordenadas y estado del jugador.
4. **Eventos**: Reacción en tiempo real a los ticks y cambios del juego.
5. **Persistencia**: Almacenamiento local SQLite con `PersistentDB`.

### Próximos Pasos Recomendados:
* Explora la documentación de la **[API de Interfaz (UI)](../ui/index.md)** para componentes avanzados como deslizadores (sliders), campos de texto y listas desplegables.
* Revisa las **[Directrices Oficiales de Publicación](../submission/guidelines.md)** para asegurar que tu plugin cumpla las normas de Jagex.
* Consulta el **[Índice General de la API](../README.md)** para ver todas las funciones disponibles.
