# Bartender (Golden Scarab Inn)

- **Original Wiki Page**: [Transcript:Bartender (Golden Scarab Inn)](https://runescape.wiki/w/Transcript%3ABartender%20%28Golden%20Scarab%20Inn%29)
- **Letter**: `B`

---

## Dialogue Transcript


### Standard dialogue

- **Bartender:** Welcome to the Golden Scarab Inn! Come take a load off before you go on your next adventure.
- [Menu]: Select an Option
  - [Choice]: Could I buy a beer, please?
    - **Player:** Could I buy a beer, please?
    - **Bartender:** Sure, that will be two gold coins, please.
    - (Condition: If the player has enough money:)
      - (removes=2 coins) (receives=beer)
      - **Player:** Thanks, Bartender.
    - (Condition: If the player does not have enough money:)
      - You can not afford that.
      - **Bartender:** I said 2 coins! You haven't got 2 coins!
      - **Player:** Sorry, I'll come back another day.
  - [Choice]: Do you sell anything special?
    - **Bartender:** Well, there is this one drink we sell that's a little 'out there'. It's called Squeck Juice.
    - **Player:** Oh, will it help with my thieving?
    - **Bartender:** Not in the least. Want to try it? It's 10 gold.
    - [Menu]: Buy some Squeck Juice?
      - [Choice]: Yes.
        - (Condition: If the player has no space in backpack:)
          - **Player:** You don't have room to take it.
        - (Condition: If the player has enough money:)
          - (removes=10 coins) (receives=squeck juice)
          - You buy some Squeck Juice.
        - (Condition: If the player does not have enough money:)
          - You can not afford that.
      - [Choice]: No.
        - **Player:** No, thanks.
  - [Choice]: What is there to do in the Ports district?
    - **Bartender:** This is the waypoint to the rest of the world - we have ships that can sail you anywhere you need to be, whether that is to take you on a new adventure or to help you escape trouble.
    - **Bartender:** Of course, you're happy to hide out here anytime you want. The Golden Scarab has a renowned reputation for keeping our mouths shut if the Imperial guard come asking questions.
    - **Bartender:** So don't be shy, tell me your secrets.
    - (previous)
  - [Choice]: Goodbye!
    - **Bartender:** Take care, sailor.

#### Buy ale option

- (above|squeck)
