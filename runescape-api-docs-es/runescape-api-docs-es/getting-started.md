# Empezando con la API de RuneScape

## Tutorial

Si eres nuevo aquí y deseas una guía guiada paso a paso para crear tu primer plugin, consulta la [página del tutorial](tutorial/index.md), o utiliza esta navegación rápida:

1. [Acceso a la API (Hola Mundo)](tutorial/1helloworld.md)
2. [Añadir una interfaz de usuario](tutorial/2simpleui.md)
3. [Recuperar información del juego](tutorial/3info.md)
4. [Sistema de Eventos](tutorial/4events.md)
5. [Base de datos persistente](tutorial/5database.md)
6. [Comandos cheat de desarrollador](tutorial/6cheats.md)

## Programación en Lua

> **Información**
> Esta documentación está redactada asumiendo cierta familiaridad con el lenguaje de programación [Lua](https://www.lua.org/).

Recursos útiles para aprender o consultar Lua en general:

* [Sitio oficial de Lua](https://www.lua.org/start.html)
* [Guía de Lua en la wiki de RuneScape](https://runescape.wiki/w/Help:Editing/Lua_guide)

La API utiliza la versión **Lua 5.4.8**. Al consultar guías externas, asegúrate de que sus recomendaciones sean compatibles con esta versión.

## Publicación de Plugins

Antes de comenzar a programar tus plugins, te recomendamos leer las [directrices oficiales](submission/guidelines.md) sobre qué comportamientos están permitidos. También puedes consultar en el [Discord de RuneScape Plugin Portal](https://dsc.gg/rspp) para resolver dudas sobre tu idea específica.

Una vez creado (y probado) tu plugin, sigue los pasos del [proceso de envío](submission/process.md) para subirlo a [Mod.io](https://mod.io/g/runescape). Allí se explica todo lo necesario para la entrega y cómo se gestiona el proceso de moderación.

## Cómo Leer Esta Documentación

Lua es un lenguaje de tipado dinámico; sin embargo, para ofrecerte una referencia clara y precisa, en estos documentos se anotan los tipos de las propiedades y parámetros de las funciones.

> **Ejemplo de firmas de funciones:**
>
> **`function Cat:Meow(volume: Float)`**
> Representa un método que debe llamarse sobre un objeto/instancia de tipo `Cat` (usando dos puntos `:`) y recibe un valor de coma flotante (ej. `0.8`):
> ```lua
> local c = Cat.new() -- Requiere una instancia válida sobre la que ejecutarse
> c:Meow(0.8)
> ```
>
> **`function Cat.find(name: String?) -> Cat?`**
> Representa una función estática (asociada a la tabla, no a una instancia específica), que recibe un string opcional y puede retornar un objeto `Cat` o `nil`:
> ```lua
> local found = Cat.find()
> -- o bien
> local found = Cat.find("George")
> ```
>
> Además:
> * **`{ String -> Int }`** representa una tabla diccionario que asocia cadenas con enteros, por ejemplo `{ A = 3, B = 100 }`.
> * **`[String]`** representa un array tradicional de cadenas, como `{ "Hola", "Mundo" }`.

> **Información sobre tipos numéricos**
> En ocasiones verás tipos como `Uint8` o `Int32`. Solo indican el rango de valores válidos aceptados o devueltos por el motor, pero en Lua se manejan como valores numéricos estándar (`number`).

> **Información sobre tipos unión**
> Tipos en formato `A | B` indican que el parámetro o retorno puede ser de tipo `A` o de tipo `B`.

### Jerarquía y Herencia en la UI
Ciertos tipos heredan métodos y propiedades de clases base. Por ejemplo:
> [ui.Component](./ui/component.md) -> ui.Button

Esto indica que `ui.Button` incluye toda la funcionalidad del tipo base `ui.Component` y puede pasarse como argumento en cualquier función que espere dicho componente base.
