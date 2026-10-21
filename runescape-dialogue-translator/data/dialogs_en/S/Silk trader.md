# Silk trader

- **Original Wiki Page**: [Transcript:Silk trader](https://runescape.wiki/w/Transcript%3ASilk%20trader)
- **Letter**: `S`

---

## Dialogue Transcript


### In Al Kharid

- **Silk trader:** Do you want to buy any fine silks?
- [Menu]: Select an Option
  - [Choice]: How much are they?
    - **Player:** How much are they?
    - **Silk trader:** 3gp.
    - [Menu]: Select an Option
      - [Choice]: No, that's too much for me.
        - **Player:** No, that's too much for me.
        - **Silk trader:** 2gp and that's as low as I'll go. I'm not selling it for any less. You'll only go and sell it in Varrock for a profit.
        - [Menu]: Select an Option
          - [Choice]: 2gp sounds good.
            - **Player:** 2gp sounds good.
            - (Condition: If the player has enough money:)
              - You buy some silk for 2gp.
              - (receives=silk) (removes=2 coins)
            - (Condition: If the player does not have enough money:)
              - **Player:** Oh dear. I don't have enough money.
              - **Silk trader:** Well, come back when you do have some money.
              - You can not afford that.
          - [Choice]: No, really, I don't want it.
            - **Player:** No, really, I don't want it.
            - **Silk trader:** Okay, but that's the best price you're going to get.
      - [Choice]: Okay, that sounds good.
        - **Player:** Okay, that sounds good.
        - (Condition: If the player has enough money:)
          - You buy some silk for 3gp.
          - (receives=silk) (removes=3 coins)
        - (Condition: If the player does not have enough money:)
          - **Player:** Oh dear. I don't have enough money.
          - **Silk trader:** Well, come back when you do have some money.
          - You can not afford that.
  - [Choice]: No, silk doesn't suit me.
    - **Player:** No, silk doesn't suit me.
