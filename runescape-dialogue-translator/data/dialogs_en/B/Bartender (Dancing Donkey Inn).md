# Bartender (Dancing Donkey Inn)

- **Original Wiki Page**: [Transcript:Bartender (Dancing Donkey Inn)](https://runescape.wiki/w/Transcript%3ABartender%20%28Dancing%20Donkey%20Inn%29)
- **Letter**: `B`

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Hello.
- **Bartender:** Good day to you, brave adventurer. Can I get you a refreshing beer?
- [Menu]: Select an Option
  - [Choice]: Yes please!
    - **Player:** Yes please!
    - **Bartender:** Ok then, that's two gold coins please.
    - (Condition: If the player has enough money:)
      - (removes=2 coins) (receives=beer)
      - **Player:** Thanks, Bartender.
    - (Condition: If the player does not have enough money:)
      - You can not afford that.
      - **Bartender:** I said 2 coins! You haven't got 2 coins!
      - **Player:** Sorry, I'll come back another day.
  - [Choice]: No thanks.
    - **Player:** No thanks.
    - **Bartender:** Let me know if you change your mind.
  - [Choice]: How much?
    - **Player:** How much?
    - **Bartender:** Two gold pieces a pint. So, what do you say?
    - [Menu]: Select an Option
      - [Choice]: Yes please!
        - (above)
      - [Choice]: No thanks.
        - (above)
