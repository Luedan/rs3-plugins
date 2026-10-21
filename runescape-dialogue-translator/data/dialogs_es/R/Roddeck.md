# Roddeck

- **Original Wiki Page**: [Transcript:Roddeck](https://runescape.wiki/w/Transcript%3ARoddeck)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Lumbridge

- (Condition: Si el player no realizó el tutorial de Cimientos inestables:)
  - **Roddeck:** ¡Saludos! Soy Roddeck.<br>¿Qué puedo hacer por ti hoy?
  - (continue)
- (Condition: Si el player hizo el tutorial de Cimientos inestables:)
  - **Roddeck:** Ah, Player, que gusto verte de nuevo.<br> ¿Qué te trae a mi humilde hogar?
  - (continue)
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: cond=Without Unstable Foundations|¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Roddeck:** Mi nombre es Roddeck. Sólo soy un señor mayor de Lumbridge, y esta es mi casa.
    - **Roddeck:** Ahora, ¿necesitabas algo más?
    - (otro)
  - [Choice]: cond=With Unstable Foundations|Sobre el dragón en tu sótano...
    - **Player:** Sobre el dragón en tu sótano...
    - **Roddeck:** Oh, sí, mi dragón mascota. Pobrecito, era muy dulce cuando lo nací por primera vez, pero se salió completamente de control. Fue entonces cuando envié un mensaje a los Caballeros Blancos para pedirles ayuda.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Eso fue realmente cruel.
        - **Player:** Eso fue realmente cruel.
        - **Roddeck:** Lo siento, ¡no tuve otra opción! Me tenía completamente atrapado en mi propio armario.<br>Ahora, ¿había algo más que quisieras?
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: ¿Puedes ofrecerme algún consejo?
            - (abajo)
          - [Choice]: Nada, gracias.
            - (abajo)
      - [Choice]: ¡Esa fue una aventura divertida!
        - **Player:** ¡Fue una aventura divertida!
        - **Roddeck:** ¿Ah? Bueno, me alegro que hayas disfrutado. Personalmente, me resultó algo aterrador quedar atrapado en mi propio armario por un dragón que escupe fuego.
        - **Roddeck:** Ahora, ¿había algo más que quisieras?
        - (continuea|anything-else)
      - [Choice]: Me iré ahora.
        - **Player:** Me voy ahora.
  - [Choice]: ¿Puedes ofrecerme algún consejo?
    - **Player:** ¿Puedes ofrecerme algún consejo?
    - **Roddeck:** ¿Consejo? ¡Ciertamente, ciertamente! <br>Utiliza el sistema de tareas para ayudarte a encontrar tu lugar, ese es mi consejo.
  - [Choice]: Nada, gracias.
    - **Player:** Nada, gracias.
