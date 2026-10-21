# Bartender (Flying Horse Inn)

- **Original Wiki Page**: [Transcript:Bartender (Flying Horse Inn)](https://runescape.wiki/w/Transcript%3ABartender%20%28Flying%20Horse%20Inn%29)
- **Letter**: `B`

---

## Dialogue Transcript


### Standard dialogue

- **Bartender:** Would you like to buy a drink?
- **Player:** What do you serve?
- **Bartender:** Beer!
- [Menu]: Select an Option
  - [Choice]: I'll have a beer then.
    - **Player:** I'll have a beer then.
    - **Bartender:**Ok, that'll be two coins.
    - (Condition: If the player has enough money:)
      - (removes=2 coins) (receives=beer)
      - **Player:** Thanks, Bartender.
    - (Condition: If the player does not have enough money:)
      - You can not afford that.
      - **Bartender:** I said 2 coins! You haven't got 2 coins!
      - **Player:** Sorry, I'll come back another day.
  - [Choice]: I'll not have anything then.
    - **Player:** I'll not have anything then.
