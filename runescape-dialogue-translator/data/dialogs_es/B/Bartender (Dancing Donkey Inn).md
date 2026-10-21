# Bartender (Dancing Donkey Inn)

- **Original Wiki Page**: [Transcript:Bartender (Dancing Donkey Inn)](https://runescape.wiki/w/Transcript%3ABartender%20%28Dancing%20Donkey%20Inn%29)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Hola.
- **Bartender:** Buenos días, valiente aventurero. ¿Puedo traerte una cerveza refrescante?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Sí, por favor!
    - **Player:** ¡Sí, por favor!
    - **Bartender:** Ok, entonces son dos gold coins, por favor.
    - (Condition: Si el player tiene suficiente dinero:)
      - (removes=2 coins) (receives=beer)
      - **Player:** Gracias, camarero.
    - (Condition: Si el player no tiene suficiente dinero:)
      - No puedes permitirte eso.
      - **Bartender:** ¡Dije 2 coins! ¡No tienes 2 coins!
      - **Player:** Lo siento, volveré otro día.
  - [Choice]: No gracias.
    - **Player:** No, gracias.
    - **Bartender:** Avísame si cambias de opinión.
  - [Choice]: ¿Cuanto?
    - **Player:** ¿Cuánto?
    - **Bartender:** Dos piezas de oro la pinta. Entonces, ¿qué dices?
    - [Menu]: Selecciona una opción
      - [Choice]: ¡Sí, por favor!
        - (arriba)
      - [Choice]: No gracias.
        - (arriba)
