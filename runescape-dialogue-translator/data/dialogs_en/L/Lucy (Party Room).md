# Lucy (Party Room)

- **Original Wiki Page**: [Transcript:Lucy (Party Room)](https://runescape.wiki/w/Transcript%3ALucy%20%28Party%20Room%29)
- **Letter**: `L`

---

## Dialogue Transcript


### Talk-to

- **Lucy:** Hi! I'm Lucy. Welcome to the Party Room!
- **Player:** Hi.
- **Lucy:** Would you like to buy a beer?
- **Player:** How much do they cost?
- **Lucy:** Just 2 gold pieces.
- [Menu]: Select an Option
  - [Choice]: Yes please!
    - **Player:** Yes please!
    - **Lucy:** Coming right up [sir/ma'am]!
    - (Condition: If the player does not have at least two coins:)
      - You can not afford that.
      - ((Repeated in a popup:))
        - You can not afford that.
        - (continue)
      - **Lucy:** I said 2 coins! You haven't got 2 coins!
      - **Player:** Sorry, I'll come back another day.
    - (Condition: If the player has at least two coins:)
      - 2 coins have been removed from your money pouch.
      - (receives=a beer)
      - **Player:** Thanks, Lucy.
  - [Choice]: No thanks, I can't afford that.
    - **Player:** No thanks, I can't afford that.
    - **Lucy:** I see. Well, come and see me if you change your mind. You know where I am!
