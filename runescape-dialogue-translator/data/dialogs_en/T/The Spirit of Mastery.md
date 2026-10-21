# The Spirit of Mastery

- **Original Wiki Page**: [Transcript:The Spirit of Mastery](https://runescape.wiki/w/Transcript%3AThe%20Spirit%20of%20Mastery)
- **Letter**: `T`

---

## Dialogue Transcript


### Trade


#### Without 120 Necromancy

- **Player:** I haven't mastered necromancy yet, so I can't buy a master cape...

#### With 120 Necromancy

- (Condition: With an inverted skillcape token:)
  - [The spirit takes your cape inversion token.]
  - (removes=inverted master skillcape token)
  - (continue)
- (Condition: Having unlocked the inverted skillcape:)
  - [Menu]: Select an Option
    - [Choice]: I would like a normal master cape.
      - (continue)
    - [Choice]: I would like an inverted master cape.
      - (continue)
- [Menu]: Buy Necromancy master cape for 120,000 coins?
  - [Choice]: Yes.
    - (Condition: Without free space in backpack:)
      - **Player:** I do not have enough room in my backpack. I should come back when I have some more.
    - (Condition: With free space in backpack:)
      - (Condition: Without 120,000 coins:)
        - You do not have enough money to purchase this cape.
        - (pop-up)
          - {{Popup|You do not have enough money to purchase this<br>cape.|warning=yes}}
      - (Condition: Without 120,000 coins:)
        - {{Qact|A jingle is heard.}}
        - (removes=120,000 coins) (receives=Necromancy master cape or Inverted Necromancy master cape)
  - [Choice]: No.
    - (end)
