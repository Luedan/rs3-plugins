# Flo (The Beach)

- **Original Wiki Page**: [Transcript:Flo (The Beach)](https://runescape.wiki/w/Transcript%3AFlo%20%28The%20Beach%29)
- **Letter**: `F`

---

## Dialogue Transcript


### Talk to

- **Flo:** Ready to head back?
- [Menu]: Select an Option
  - [Choice]: Yeah, I'm ready to go.
    - {{Qact|The player is moved to the Grand Exchange, in front of the Sunlight Sands Beach portal.}}
  - [Choice]: No, I'll stay a little longer.
    - **Flo:** I can't complain. {{Sic|Sunshine and fish what more could a man want?}}
    - **Flo:** Although, saying that, I wouldn't mind getting my hands on that beastie in the pool. She'd make a meal fit for a kingdom.
    - **Flo:** I might need a bigger rod though!
    - [Menu]: Select an Option
      - [Choice]: cond=Only if not asked last:|What's going on here?
        - **Flo:** There's great fishing to be had here. The tropical trout are frisky, but just the thing for cooking up a tasty summer treat.
        - [Using the fishing spots gives you fishing experience. You can gain extra experience for handing the fish to Wellington or delivering them to the barbecue area.]
        - (previous)
      - [Choice]: cond=Only if not asked last:|Why are there pirate ships?
        - **Flo:** Those ships are feisty ones! They're looking for something to fight.
        - **Flo:** If you have any battleships you can pit them against one of the pirate ships but beware, {{Colour|#FF0000|the pirates never lose}}!
        - (previous)
      - [Choice]: cond=Only after asking something else:|How are things going?
        - (above|I can't complain)

### Head Home

- {{Qact|The player is moved to the Grand Exchange, in front of the Sunlight Sands Beach portal.}}

### Trying to open the store with the relevant Sandy Clue Scroll (historical)

- Oo, a stranger left this for you!
- (Condition: Receiving a scroll box:)
  - (removes=Sandy Clue Scroll) (receives=Sandy Scroll box)
  - [scrollbox].}}
- (Condition: Receiving caskets:)
  - (Condition: Without free space in backpack:)
    - You need 1 free space in your backpack to receive your clue caskets.
  - (Condition: With free space in backpack:)
    - (removes=Sandy Clue Scroll) (receives=Sandy Casket and its red version)
    - [You are handed a casket!]
