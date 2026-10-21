# Skulgrimen

- **Original Wiki Page**: [Transcript:Skulgrimen](https://runescape.wiki/w/Transcript%3ASkulgrimen)
- **Letter**: `S`

---

## Dialogue Transcript


### Before The Fremennik Trials


#### Talking to him

- **Player:** Hello!
- **Skulgrimen:**Sorry. I can't sell weapons to outerlanders. Wouldn't be right. Against our beliefs.

#### Trading him

- Only Fremenniks may purchase weapons and armour here.

### After The Fremennik Trials

- ((Having at least one rock-shell chunk, shard, or splinter in the backpack:))
  - **What would you like to ask about?**
    - Rock Crab Armour
      - **Player:** Hello there. I have these shards of rock crab shell, and believe you might be able to make them into armour for me...?
      - **Skulgrimen:** No problem, [Fremennik name]. What armour you want?
      - **Select an Option**
        - A fine helm
          - **Skulgrimen:** It'll cost 5,000 coins. That ok?
          - **Select an Option**
            - YES
              - ((If one or more required component is missing:))
                - **Skulgrimen:** Sorry. Need 1 piece of dark daggermouth hide, 1 rock-shell chunk and 5,000 coins to make you helmet. Come back when you got it.
                - (end)
              - (removes=1 rock-shell chunk, 1 dagannoth hide, and 5,000 coins) (receives=rock-shell helm)
              - **Skulgrimen:** There you go. Fine helm. You want another?
              - **Select an Option**
                - YES
                  - (continuea|helm)
                - NO
                  - (continuea|armour)
        - Sturdy bodyarmour
          - **Skulgrimen:** It'll cost 10,000 coins. That ok?
          - **Select an Option**
            - YES
              - ((If one or more required component is missing:))
                - **Skulgrimen:** Apologies. Need 3 pieces of dark daggermouth hide, 1 rock-shell shard and 10,000 coins to make you strong armour. Come back when you got it.
                - (end)
              - (removes=1 rock-shell shard, 3 dagannoth hides, and 10,000 coins) (receives=rock-shell plate)
              - **Skulgrimen:** There you go. Sturdy armour. You need another piece?
              - **Select an Option**
                - YES
                  - (continuea|body)
                - NO
                  - (continuea|armour)
        - Powerful leg armour
          - **Skulgrimen:** It'll cost 7,500 coins. That ok?
          - **Select an Option**
            - YES
              - ((If one or more required component is missing:))
                - **Skulgrimen:** Apologies. Need 2 pieces of dark daggermouth hide, 1 rock-shell splinter and 7,500 coins to make you leg armour. Come back when you got it.
                - (end)
              - (removes=1 rock-shell splinter, 2 dagannoth hides, and 7,500 coins) (receives=rock-shell legs)
              - **Skulgrimen:** There you go. Sturdy armour. You need another piece?
              - **Select an Option**
                - YES
                  - (continuea|legs)
                - NO
                  - (continuea|armour)
            - NO
              - (continuea|armour)
        - Nothing
          - **Player:** Actually, I don't want anything.
          - **Skulgrimen:** AS you wish.
    - The Fremennik Trials
      - (continue)
- **Skulgrimen:** Hello again, [Fremennik name]. Come to see what's for sale?
- ((Unknown condition:))
  - **Choose an option:**
    - Show me what you've got.
      - (opens=Skulgrimen's Battle Gear)
    - Can I ask you about V?
      - **Skulgrimen:** We'll keep his stories alive, at least his legend will live forever.
      - (end)
- (opens=Skulgrimen's Battle Gear)
