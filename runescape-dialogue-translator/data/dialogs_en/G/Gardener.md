# Gardener

- **Original Wiki Page**: [Transcript:Gardener](https://runescape.wiki/w/Transcript%3AGardener)
- **Letter**: `G`

---

## Dialogue Transcript


### In Falador Park


#### Talking to him

- **Player:** Hello.
- **Gardener:** I'm busy. Unless you've got some lily seeds, you can go find Wyson if you need anything.
- [Menu]: Select an Option
  - [Choice]: Ask about exchanging Lily seeds
    - **Gardener:** I need fifty white lily seeds a day. In exchange, I'm willing to teach you some of the farming tricks I've picked up over the years.
    - [Menu]: Select an Option
      - [Choice]: Exchange seeds
        - (Condition: If the player has no white lily seeds:)
          - **Gardener:** You don't appear to have any seeds with you.
        - (Condition: If the player has traded in fifty white lily seeds for the day:)
          - **Gardener:** I'm afraid I've got nothing more I can teach you today. Could you come back tomorrow?
          - You can only exchange 50 seeds a day.
        - (Condition: If the player has white lily seeds in backpack:)
          - **Gardener:** How many seeds are you willing to offer?
          - {{tinput|Enter amount:}}
            - ((After entering a positive amount:))
              - You will gain [amount] Farming xp in exchange for [number] seeds.
              - (removes=white lily seeds) (receives=100 Farming XP for each white lily seed)
            - (Condition: If zero is entered:)
              - **Gardener:** Come back if you change your mind.
      - [Choice]: Leave
        - (end)
  - [Choice]: Ask about strange plant
    - **Player:** Haven't you noticed that there's a massive fissure in the park?
    - **Gardener:** Oh, yeah. I guess there's some sort of mole problem. Wyson said he had it under control, so I haven't paid it much mind.
  - [Choice]: Leave
    - (end)

#### Exchange seeds option

- How many lily seeds would you like to exchange?
- {{tinput|Enter amount:}}
  - ((After entering a positive amount:))
    - (Condition: If the player has no white lily seeds:)
      - You don't have that many lily seeds.
    - (Condition: If the player has traded in fifty white lily seeds for the day:)
      - **Gardener:** I'm afraid I've got nothing more I can teach you today. Could you come back tomorrow?
      - You can only exchange 50 seeds a day.
    - (Condition: If the player has white lily seeds:)
      - You will gain [amount] Farming xp in exchange for [number] seeds.
      - (removes=white lily seeds) (receives=100 Farming XP for each white lily seed)
  - (Condition: If zero is entered:)
    - **Gardener:** Come back if you change your mind.
