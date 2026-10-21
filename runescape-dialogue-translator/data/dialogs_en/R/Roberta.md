# Roberta

- **Original Wiki Page**: [Transcript:Roberta](https://runescape.wiki/w/Transcript%3ARoberta)
- **Letter**: `R`

---

## Dialogue Transcript


### Talk to

- (Condition: Before obtaining On the Origin of Centaurs:)
  - **Roberta:** Hey, can you help me out? I excavated the cave to the south while digging for artefacts. It contains a rare and precious type of clay, but I lack the expertise and equipment to mine the porcelain myself.
  - (continue)
- (Condition: After obtaining On the Origin of Centaurs:)
  - Thanks a ton for helping me out - you're the best! I hope you have a blast reading the book.
  - (continue)
- [Menu]: Choose an option:|anchor=Roberta-options
  - [Choice]: What will you give me in exchange?|cond=Before obtaining On the Origin of Centaurs:
    - **Roberta:** I found a book in the cave when I first discovered it. I'll trade it for 100 porcelain, soft or dry.
    - [pic=On the Origin of Centaurs detail.png]
    - (initial|Roberta-options)
  - [Choice]: Tell me about this cave.
    - **Roberta:** Two streams of water flow through the cave, which is rich in porcelain clay deposits. The clay closest to water is softer.
    - **Roberta:** Everlight's water has special mineral properties which over time have made the clay stronger - both to mine and to work.
    - **Roberta:** Porcelain could make strong and beautiful pottery, but it requires a skilled hand and strong pickaxe to extract.
    - (initial|Roberta-options)
  - [Choice]: Look at all this porcelain clay I've mined!|cond=With porcelain clay in backpack:
    - (Condition: With less than 100 porcelain clay in backpack before obtaining On the Origin of Centaurs:)
      - **Roberta:** Wow! [number] is impressive! Can you bring me 100 porcelain clay? I'll give you my book in exchange.
      - (initial|Roberta-options)
    - (Condition: With at least 100 porcelain clay in backpack before obtaining On the Origin of Centaurs:)
      - **Roberta:** Wow! [number] is impressive!
      - **Roberta:** You can have the book I found in exchange for 100 porcelain clay.
      - (Condition: Without one free backpack space:)
        - **Roberta:** However, you need a free space in your backpack, so I can give you the book.
      - (Condition: With one free backpack space:)
        - (removes=100 porcelain clay) (receives=On the Origin of Centaurs)
        - [pic=On the Origin of Centaurs detail.png]
        - (initial|Roberta-options)
    - (Condition: After obtaining On the Origin of Centaurs:)
      - **Roberta:** [number] porcelain clay is impressive! I don't have anything else to give you in exchange, though.
      - (initial|Roberta-options)
  - [Choice]: Goodbye.
    - (end)

### Attempting to enter the Everlight porcelain clay mine without level 102 Mining

- **Roberta:** You'll need to be a particularly proficient Miner to gather porcelain clay in that cave.
