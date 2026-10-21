# Saniboch

- **Original Wiki Page**: [Transcript:Saniboch](https://runescape.wiki/w/Transcript%3ASaniboch)
- **Letter**: `S`

---

## Dialogue Transcript


### At Brimhaven Dungeon entrance


#### Trying to enter without paying

- **Saniboch:** You can't go in there without paying!

#### Talking to Saniboch

- **Saniboch:** Good day to you bwana.
- [Menu]: Select an option
  - [Choice]: Can I go through that door please?
    - **Player:** Can I go through that door please?
    - (Condition: With the hard set of Karamja tasks completed:)
      - **Saniboch:** You may enter free as you have proven you are a friend of Karamja.
    - (Condition: Otherwise:)
      - **Saniboch:** Most certainly, but I must charge you the sum of 875 coins first.
      - (Condition: If you do not have sufficient money with you:)
        - **Player:** I don't have the money on me at the moment.
        - **Saniboch:** Well this is a dungeon for the more wealthy discerning adventurer, be gone with you riff raff.
        - **Player:** But you don't even have clothes, how can you seriously call anyone riff raff.
        - **Saniboch:** Hummph.
      - (Condition: If you have enough money with you:)
        - [Menu]: Select an option
          - [Choice]: Ok, here's 875 coins.
            - **Player:** Ok, here's 875 coins.
            - [You give Saniboch 875 coins.]
            - You pay Saniboch 875 coins.
            - (removes=875 coins)
            - **Saniboch:** Many thanks. You may now pass the door. May your death be a glorious one!
          - [Choice]: Never mind.
            - **Player:** Never mind.
          - [Choice]: Why is it worth the entry cost?
            - **Player:** Why is it worth the entry cost?
            - **Saniboch:** It leads to a huge fearsome dungeon, populated by giants and strange dogs. Adventurers come from all around to explore its depths.
            - **Saniboch:** I know not what lies deeper in myself, for my skills in agility and woodcutting are inadequate, but I hear tell of even greater dangers deeper in.
  - [Choice]: Where does this strange entrance lead?
    - **Player:** Where does this strange entrance lead?
    - **Saniboch:** To a huge fearsome dungeon, populated by giants and strange dogs. Adventurers come from all around to explore its depths.
    - **Saniboch:** I know not what lies deeper in myself, for my skills in agility and woodcutting are inadequate.
  - [Choice]: Good day to you too.
    - **Player:** Good day to you too.
  - [Choice]: I'm impressed, that tree is growing on that shed.
    - **Player:** I'm impressed, that tree is growing on that shed.
    - **Saniboch:** My employer tells me it is an uncommon sort of tree called the Fyburglars tree.

#### Pay

- (Condition: Without having completed the hard set of Karamja tasks:)
  - [You give Saniboch 875 coins.]
  - You pay Saniboch 875 coins.
  - (removes=875 coins)
  - **Saniboch:** Many thanks. You may now pass the door. May your death be a glorious one!
- (Condition: With the hard set of Karamja tasks completed:)
  - **Saniboch:** You may enter free as you have proven you are a friend of Karamja.
