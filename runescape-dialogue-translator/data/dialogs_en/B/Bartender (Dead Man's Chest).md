# Bartender (Dead Man's Chest)

- **Original Wiki Page**: [Transcript:Bartender (Dead Man's Chest)](https://runescape.wiki/w/Transcript%3ABartender%20%28Dead%20Man%27s%20Chest%29)
- **Letter**: `B`

---

## Dialogue Transcript


### Standard dialogue

- **Bartender:** Yohoho me hearty what would you like to drink?
- [Menu]: Select an Option
  - [Choice]: Nothing, thank you.
    - **Player:** Nothing, thank you.
  - [Choice]: A pint of Grog please.
    - **Player:** A pint of Grog please.
    - **Bartender:** One grog coming right up, that'll be three coins.
    - (Condition: If the player has enough money:)
      - (removes=3 coins) (receives=grog)
      - **Player:** Thanks, Bartender.
      - **Player:** Oh dear. I don't seem to have enough money.
    - (Condition: If the player does not have enough money:)
      - You can not afford that.
      - **Bartender:** I said 3 coins! You haven't got 3 coins!
      - **Player:** Sorry, I'll come back another day.
      - **Player:** Oh dear. I don't seem to have enough money.
  - [Choice]: A bottle of rum please.
    - **Player:** A bottle of rum please.
    - **Bartender:** That'll be 27 coins.
    - (Condition: If the player has enough money:)
      - (removes=27 coins) (receives=karamjan rum)
      - **Player:** Thanks, Bartender.
    - (Condition: If the player does not have enough money:)
      - You can not afford that.
      - **Bartender:** I said 27 coins! You haven't got 27 coins!
      - **Player:** Sorry, I'll come back another day.
