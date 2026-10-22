# Bartender (Dead Man's Chest)

- **Original Wiki Page**: [Transcript:Bartender (Dead Man's Chest)](https://runescape.wiki/w/Transcript%3ABartender%20%28Dead%20Man%27s%20Chest%29)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Bartender:** Yohoho, cariño, ¿qué te gustaría beber?
- [Menu]: Selecciona una opción
  - [Choice]: Nada, gracias.
    - **Player:** Nada, gracias.
  - [Choice]: Una pinta de grog, por favor.
    - **Player:** Una pinta de Grog, por favor.
    - **Bartender:** Un grog en breve, serán tres coins.
    - (Condition: If the player has enough money:)
      - (removes=3 coins) (receives=grog)
      - **Player:** Gracias, camarero.
      - **Player:** Dios mío. Parece que no tengo suficiente dinero.
    - (Condition: If the player does not have enough money:)
      - No puedes permitirte eso.
      - **Bartender:** ¡Dije 3 coins! ¡No tienes 3 coins!
      - **Player:** Lo siento, volveré otro día.
      - **Player:** Dios mío. Parece que no tengo suficiente dinero.
  - [Choice]: Una botella de ron por favor.
    - **Player:** Una botella de ron, por favor.
    - **Bartender:** Serán 27 coins.
    - (Condition: If the player has enough money:)
      - (removes=27 coins) (receives=karamjan rum)
      - **Player:** Gracias, camarero.
    - (Condition: If the player does not have enough money:)
      - No puedes permitirte eso.
      - **Bartender:** ¡Dije 27 coins! ¡No tienes 27 coins!
      - **Player:** Lo siento, volveré otro día.
