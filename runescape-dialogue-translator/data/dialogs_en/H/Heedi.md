# Heedi

- **Original Wiki Page**: [Transcript:Heedi](https://runescape.wiki/w/Transcript%3AHeedi)
- **Letter**: `H`

---

## Dialogue Transcript


### Talk to

- [Menu]: Choose an option:|anchor=Heedi-options
  - [Choice]: Who are you?
    - **Heedi:** I am Heedi the botanist. I have laboured my life, searching for a way to overcome the dying nature of my world.
    - **Heedi:** There was a tree, sacred to my people, but over the ages, it grew less and less abundant.
    - **Heedi:** But now, look - it lives again.<br>In essence, at least.<br>Merged with another; a child to two parents.
    - **Heedi:** What a wonderful thing, no?
    - (previous|Heedi-options)
  - [Choice]: About these trees.
    - [Menu]: Select an Option|anchor=TheseTees
      - [Choice]: Tell me about these trees.
        - **Heedi:** You are familiar, I assume, with the magic tree?
        - [Without pausing for a response, Heedi enthusiastically continues.]
        - **Heedi:** A magic tree siphons energy from sites of magical power to sustain itself...a fascinating relationship with the soil.<br>Almost parasitic.
        - **Heedi:** Adaptable. Mutable. Imbued with stolen power!<br>Not unlike your warring gods.
        - [Heedi sniggers in amusement.]
        - **Heedi:** But I digress.
        - **Heedi:** Let us call this magical youth the second child.<br>Full of life and magic, energetic and wild, but unfocused and distractible.
        - **Heedi:** By contrast, I present, in its splendour, my clear-cut favourite child, the Iaian baobab.
        - **Heedi:** Adansonia mysticata, to its friends.<br>Friends like me.
        - **Heedi:** It took much patience, some coercion, even a little cruelty, to cross-breed the trees of my marshy homeland with your magic trees.
        - **Heedi:** But behold the result!<br>They flourish, do they not?<br>And oh so very pretty.
        - (previous|TheseTees)
      - [Choice]: Can I cut these trees?
        - **Heedi:** You may harvest their wood, if you so desire. The assault of your hatchets will only strengthen my eternal magic trees, and thusly swell my heart with pride.
        - **Heedi:** Their bark is tough, however. You'll need a formidable tool.
        - **Heedi:** Wilfred the Woodcutting skillcape vendor near Falador lodestone sells a means to combine a crystal hatchet and imcando hatchet, but only to a veteran adventurer that has earned the respect of the elves and the dwarves.
        - **Heedi:** I also hear tales of a differently sighted dwarf who lives within Ice Mountain. He may guide you in upgrading that hatchet, for a price.
        - (previous|TheseTees)
      - [Choice]: Back.
        - [Choice]: previous|Heedi-options
  - [Choice]: Is there anything else I can do for you?|cond=With no branches:
    - **Heedi:** If you manage to cut a perfect branch from an eternal magic tree, I'll share some horticultural knowledge in exchange.
    - **Heedi:** Alternatively, in sufficiently skilled hands, a pair of branches (and a bucket of eternal magic tree sap) would make excellent limbs for a powerful bow.
    - (Condition: Without 110 Woodcutting:)
      - [pic=Perfect eternal magic branch detail.png]
      - (continue)
    - (Condition: With 110 Woodcutting:)
      - [pic=Perfect eternal magic branch detail.png]
      - (continue)
    - [pic=Perfect eternal magic branch detail.png]
    - (previous|Heedi-options)
  - [Choice]: Can I offer you a branch in this trying time?|cond=With at least one branch:
    - **Heedi:** Oh, what an excellent specimen. I'll share some horticultural knowledge in exchange.
    - (Condition: Shown in an interface titled "OFFER BRANCHES":)
      - File:Woodcutting.png You have [number] eternal magic tree [branch/branches].<br><br>Would you like to give [it/them] to Heedi?<br><br>You will receive [number] Woodcutting XP.
        - [Choice]: Cancel
          - ((The interface closes.))
          - (previous|Heedi-options)
        - [Choice]: OK
          - ((The interface closes.))
          - (removes=all perfect eternal magic branches)
          - {{Qact|The player gains the corresponding amount of Woodcutting experience.}}
          - (previous|Heedi-options)
  - [Choice]: Can I plant these trees elsewhere?|cond=Having completed The Lute of Love achievement:
    - **Player:** I think I found a spot where these eternal magic trees would flourish. Any chance you could help me plant some there?
    - **Heedi:** I would gladly send my children out into the world.
    - **Heedi:** Have these saplings. I prepared them with the utmost care.
    - **Heedi:** If the soil you speak of is truly worthy, they shall grow swiftly, even in the hands of an amateur farmer.
    - (Condition: If the player has any saplings in the bank or inventory already:)
      - **Heedi:** Ah but you still have some of my saplings. Come back if you run out.
  - [Choice]: Farewell.
    - (end)

### Give branches to


#### Without branches


##### Without 110 Woodcutting

- [pic=Perfect eternal magic branch detail.png]

##### With 110 Woodcutting

- [pic=Perfect eternal magic branch detail.png]
- [pic=Perfect eternal magic branch detail.png]

#### With branches

- ((Shown in an interface titled "OFFER BRANCHES":))
  - File:Woodcutting.png You have [number] eternal magic tree [branch/branches].<br><br>Would you like to give [it/them] to Heedi?<br><br>You will receive [number] Woodcutting XP.
    - [Choice]: CANCEL
      - ((The interface closes.))
    - [Choice]: OK
        - ((The interface closes.))
        - (removes=all perfect eternal magic branches)
        - {{Qact|The player gains the corresponding amount of Woodcutting experience.}}
