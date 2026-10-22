# Klank

- **Original Wiki Page**: [Transcript:Klank](https://runescape.wiki/w/Transcript%3AKlank)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### After Underground Pass

- **Player:** Hola Klank.
- **Klank:** Hola de nuevo aventurero, ¿todavía estás por aquí?
- **Player:** ¡Aún aquí!
- [Menu]: Selecciona una opción
  - [Choice]: ¿Tienes más?
    - **Player:** ¿Tienes más guanteletes?
    - **Klank:** Bueno... sí, pero no son baratos de hacer. Tendré que venderte un par...
    - **Player:** ¿Cuánto?
    - **Klank:** 5000 coins.
    - [Menu]: Selecciona una opción
      - [Choice]: 5000, ¡debes estar bromeando!
        - **Player:** 5000, ¡debes estar bromeando!
        - **Klank:** Aquí no bromeamos amigo...
      - [Choice]: Está bien, entonces tomaré un par.
        - **Player:** Está bien, entonces tomaré un par.
        - (Condition: If the player has enough money:)
          - (removes=5,000 coins) (receives= Klank's gauntlets)
          - Le das Klank 5000 coins...
          - **Klank:**Ahí lo tienes... Espero que te ayuden.
          - **Player:** Nos vemos en Klank.
        - (Condition: If the player does not have enough money:)
          - **Player:** Dios mío, no tengo suficiente dinero...
          - No puedes permitirte eso.
          - **Klank:** Lo siento, no puedo venderlos más baratos que eso.
  - [Choice]: Cuídate Klank.
    - **Player:** Cuídate Klank.
    - **Klank:** Tú también aventurero...
