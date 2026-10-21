# Barlak

- **Original Wiki Page**: [Transcript:Barlak](https://runescape.wiki/w/Transcript%3ABarlak)
- **Letter**: `B`

---

## Dialogue Transcript

{{Incomplete|Missing dialogue regarding trading (perfect) snail shells to Barlak, and dialogue regarding trading long and curved bones without the level 30 Construction requirement.}}

### In Dorgesh-Kaan

- **Barlak:** Bones!
- **Player:** What?
- **Barlak:** I don't have any bones!
- [Menu]: Select an Option
  - [Choice]: Then how do you stand up?
    - **Player:** Then how do you stand up?
    - **Barlak:** What?
    - **Player:** How do you stand up if you have no bones? Shouldn't you collapse into a gelatinous blob?
    - **Barlak:** Ha, ha, ha, ha, ha!
    - [Menu]: Select an Option
      - [Choice]: What do you need bones for?
        - (below|need)
      - [Choice]: What kind of bones do you need?
        - (below|kind)
      - [Choice]: Will you buy anything besides bones?
        - (below|anything)
      - [Choice]: Goodbye.
        - **Player:** Goodbye.
        - **Barlak:** Goodbye.
  - [Choice]: What do you need bones for?
    - **Player:** What do you need bones for?
    - **Barlak:** To stand up properly. Otherwise I'd collapse into a gelatinous blob!
    - **Barlak:** Ha, ha, ha, ha, ha!
    - **Barlak:** No, seriously, I need bones to use as a Construction material. We always need big bones to prop up the mine shafts and to make other temporary structures.
    - [Menu]: Select an Option
      - [Choice]: What kind of bones do you need?
        - (below|kind)
      - [Choice]: Will you buy anything besides bones?
        - (below|anything)
      - [Choice]: Goodbye.
        - (above|goodbye)
  - [Choice]: Will you buy anything besides bones?
    - **Player:** Will you buy anything besides bones?
    - **Barlak:** Well, I've had a few people bring me some interesting giant shells. They say they came from giant snails and giant tortoises.
    - **Barlak:** Of course, like the bones, some shells are better than others. I'll give you 250gp for ordinary shells, but what I really need are perfect shells. I'll pay double for them and give you a few tips about Crafting too.
    - [Menu]: Select an Option
      - [Choice]: What do you need bones for?
        - (above|need)
      - [Choice]: What kind of bones do you need?
        - (below|kind)
      - [Choice]: Goodbye.
        - (above|goodbye)
  - [Choice]: What kind of bones do you need?
    - **Player:** What kind of bones do you need?
    - **Barlak:** Enormous bones, as big as you can get. Not just any big bones will do.
    - **Barlak:** Sometimes you might find a particularly long, straight bone. That's the kind of thing I need; I'll give you 1,000gp for one of them.
    - **Barlak:** Occasionally, you might find a long curved bone - these are especially valuable - I'll give you 2,000gp for them.
    - **Barlak:** I'll also teach you a bit about how we use the bones in Construction, if you like.
    - [Menu]: Select an Option
      - [Choice]: What kind of bones do you need?
        - (above|kind)
      - [Choice]: Will you buy anything besides bones?
        - (above|anything)
      - [Choice]: Goodbye.
        - (above|goodbye)

#### With tortoise shells in backpack

- **Barlak:** That giant shell... what is it?
- **Player:** It's a giant battle tortoise shell!
- (Condition: If the player is carrying only regular tortoise shells:)
  - **Barlak:** Hmmm... I think I might be able to make something out of them.
  - **Barlak:** I'll give you [amount]gp for the tortoise shell you're carrying
  - (continue)
- (Condition: If the player is carrying one or more perfect shells:)
  - **Barlak:** Hmmm... I think I might be able to make something out of them, especially that perfect one.
  - **Barlak:** I'll give you [amount]gp for the tortoise shell you're carrying, and I'll try to give you some advice on Crafting while I'm at it.
  - (continue)
- [Menu]: Select an Option
  - [Choice]: Okay.
    - **Player:** Okay.
    - (removes=tortoise shell and/or perfect shell)
    - (receives=coins and experience)
    - **Barlak:** Thanks! Now, I don't think I could use that for Construction, but maybe I could make something...
    - Barlak gives you a short lecture and you learn more about Crafting.
  - [Choice]: No thanks.
    - **Player:** No thanks.

#### With long or curved bones in backpack

- **Barlak:** Those bones! Those are exactly the sort of thing I need! Will you sell them? I'll give you [amount]gp for the bones you're carrying.
- **Barlak:** I'll try to teach you something about Construction as well, but it's highly technical so you won't understand if you don't already have level 30 Construction.
- [Menu]: Select an Option
  - [Choice]: Okay.
    - **Player:** Okay.
    - (removes=long bone and/or curved bone)
    - (receives=coins and experience)
    - **Barlak:** Thanks! Now let me explain...
    - Barlak gives you a short lecture and you learn more about Construction.
  - [Choice]: No, I'll keep the bones.
    - **Player:** No thanks.
