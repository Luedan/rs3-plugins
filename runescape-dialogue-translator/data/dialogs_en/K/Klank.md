# Klank

- **Original Wiki Page**: [Transcript:Klank](https://runescape.wiki/w/Transcript%3AKlank)
- **Letter**: `K`

---

## Dialogue Transcript


### After Underground Pass

- **Player:** Hello Klank.
- **Klank:** Hello again adventurer, so you're still around?
- **Player:** Still here!
- [Menu]: Select an Option
  - [Choice]: Have you anymore
    - **Player:** Have you any more gauntlets?
    - **Klank:** Well..yes, but they're not cheap to make. I'll have to sell you a pair...
    - **Player:** How much?
    - **Klank:** 5000 coins.
    - [Menu]: Select an Option
      - [Choice]: 5000, you must be joking!
        - **Player:** 5,000, you must be joking!
        - **Klank:** We don't joke down here friend...
      - [Choice]: Okay then, I'll take a pair.
        - **Player:** Okay then, I'll take a pair.
        - (Condition: If the player has enough money:)
          - (removes=5,000 coins) (receives= Klank's gauntlets)
          - You give Klank 5000 coins...
          - **Klank:**There you go... I hope they help.
          - **Player:** I'll see you around Klank.
        - (Condition: If the player does not have enough money:)
          - **Player:** Oh dear, I haven't enough money...
          - You can not afford that.
          - **Klank:** Sorry, I can't sell them any cheaper than that.
  - [Choice]: Take care Klank.
    - **Player:** Take care Klank.
    - **Klank:** You too adventurer...
