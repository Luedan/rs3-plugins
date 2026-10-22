# Bartender (Flying Horse Inn)

- **Original Wiki Page**: [Transcript:Bartender (Flying Horse Inn)](https://runescape.wiki/w/Transcript%3ABartender%20%28Flying%20Horse%20Inn%29)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Bartender:** ¿Te gustaría comprar una bebida?
- **Player:** ¿Qué sirves?
- **Barman:** ¡Cerveza!
- [Menu]: Selecciona una opción
  - [Choice]: Entonces tomaré una cerveza.
    - **Player:** Entonces tomaré una cerveza.
    - **Bartender:**Ok, serán dos coins.
    - (Condition: If the player has enough money:)
      - (removes=2 coins) (receives=beer)
      - **Player:** Gracias, camarero.
    - (Condition: If the player does not have enough money:)
      - No puedes permitirte eso.
      - **Bartender:** ¡Dije 2 coins! ¡No tienes 2 coins!
      - **Player:** Lo siento, volveré otro día.
  - [Choice]: Entonces no tendré nada.
    - **Player:** Entonces no tendré nada.
