# Wellington

- **Original Wiki Page**: [Transcript:Wellington](https://runescape.wiki/w/Transcript%3AWellington)
- **Letter**: `W`

---

## Dialogue Transcript


### Hand in fish with raw tropical trout

- (removes=raw tropical trout)
- You hand [number] fish to Wellington.
- (pop-up)
  - {{Pop-up|You hand [number] fish to Wellington.}}

### Hand in fish without raw tropical trout or talk to

- [Menu]: Select an Option
  - [Choice]: cond=Only if not asked last:|What's going on here?
    - **Wellington:** There's great fishing to be had here. The tropical trout are frisky, but just the thing for cooking up a tasty summer treat.
    - [Using the fishing spots gives you fishing experience. You can gain extra experience for handing the fish to Wellington or delivering them to the barbecue area.]
    - (previous)
  - [Choice]: cond=Only if not asked last:|Why are there pirate ships?
    - **Wellington:** Those ships are feisty ones! They're looking for something to fight.
    - **Wellington:** If you have any battleships you can pit them against one of the pirate ships but beware, {{Colour|#FF0000|the pirates never lose}}!
    - (previous)
  - [Choice]: cond=Only if not asked last:|How are things going?
    - **Wellington:** I can't complain. {{Sic|Sunshine and fish what more could a man want?}}
    - **Wellington:** Although, saying that, I wouldn't mind getting my hands on that beastie in the pool. She'd make a meal fit for a kingdom.
    - **Wellington:** I might need a bigger rod though!
    - (previous)

### Any option with the Sandy Clue Scroll (historical)

- **Wellington:** Here take it, I don't want to be involved in this {{Sic|fishyness}}!
- (Condition: Receiving a scroll box:)
  - (removes=Sandy Clue Scroll) (receives=Sandy Scroll box)
  - [scrollbox].}}
- (Condition: Receiving caskets:)
  - (Condition: Without free backpack space:)
    - [You need 1 free space in our backpack to receive your clue caskets.]
  - (Condition: With free backpack space:)
    - (removes=Sandy Clue Scroll) (receives=Sandy Casket and its red version)
    - [You are handed a casket!]
