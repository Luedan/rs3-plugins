# Solomon

- **Original Wiki Page**: [Transcript:Solomon](https://runescape.wiki/w/Transcript%3ASolomon)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Solomon:** ¡Bienvenido a General Store de Solomon!<br/>¿En qué puedo servirle de ayuda?
- [Menu]: Selecciona una opción
  - [Choice]: cond=If the player is not on mobile:|¿Qué es este lugar?
    - **Solomon:** Este es General store de Solomon, el mejor minorista en el reino corpóreo.
    - **Solomon:** Aquí puedes comprar mascotas, ropa y una selección de excelentes artículos cosméticos.
    - (initial|initial-options)
  - [Choice]: cond=If the player is not on mobile:|¿Cómo compro cosas aquí?
    - **Solomon:** Simplemente ingresa a la tienda, selecciona los artículos que deseas y completa tu transacción usando Loyalty Points o RuneCoins.
    - **Solomon:** No podría ser más sencillo.
    - (initial|initial-options)
  - [Choice]: cond=If the player is not on mobile:|Me gustaría comprar algo.
    - [Menu]: ¿Quieres entrar a la tienda de Solomon?
      - [Choice]: Sí.
        - (Action: el player se envía al lobby y General Store de Solomon se abre en una pestaña del navegador.)
      - [Choice]: No.
        - (initial|initial-options)
  - [Choice]: cond=If the player is on mobile:|¿Qué hay en tu tienda?
    - **Solomon:** ¡Navega a tu gusto!
    - (opens=Customisations)
  - [Choice]: Adiós.
    - **Solomon:** Hasta la próxima.
