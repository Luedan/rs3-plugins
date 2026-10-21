# The Spirit of Accomplishment

- **Original Wiki Page**: [Transcript:The Spirit of Accomplishment](https://runescape.wiki/w/Transcript%3AThe%20Spirit%20of%20Accomplishment)
- **Letter**: `T`

---

## Dialogue Transcript


### Trade


#### With under 99 Necromancy

- **Player:** I'm not yet accomplished enough as a necromancer to buy a skillcape...

#### With 99 or higher Necromancy

- [Menu]: Buy Necromancy skillcape?
  - [Choice]: Yes.
    - (Condition: With an inverted skillcape token:)
      - [The spirit takes your cape inversion token.]
      - (removes=inverted skillcape token)
      - (continue)
    - [Menu]: Choose an option:
      - [Choice]: cond=While wearing an activated or imbued ring of charos:|92,000 coins? That's much too expensive.
        - **Player:** I know where to find you if I change my mind.
      - [Choice]: cond=Without an activated or imbued ring of charos:|99,000 coins? That's much too expensive.
        - **Player:** I know where to find you if I change my mind.
      - [Choice]: I think I have the money right here, actually.
        - (Condition: Without enough coins:)
          - **Player:** Oh, I don't have enough coins to buy this.
        - (Condition: Without two free spaces in backpack:)
          - **Player:** Ah, I need room for both the cape and the hood.
        - (Condition: With enough coins and two free spaces in backpack:)
          - (removes= 92,000 or 99,000 coins) (receives=a Necromancy cape (or trimmed variant) and hood)
          - **Player:** Excellent! I will wear this cape with pride.
      - [Choice]: cond=Having unlocked the inverted skillcape:|I'd like a skillcape with the colours inverted.
        - (Condition: Without enough coins:)
          - **Player:** Oh, I don't have enough coins to buy this.
        - (Condition: Without two free spaces in backpack:)
          - **Player:** Ah, I need room for both the cape and the hood.
        - (Condition: With enough coins and two free spaces in backpack:)
          - (removes= 92,000 or 99,000 coins) (receives=a Inverted hooded Necromancy cape)
          - **Player:** Excellent! I will wear this cape with pride.
  - [Choice]: No.
    - (end)
