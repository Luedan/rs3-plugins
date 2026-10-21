# Egil

- **Original Wiki Page**: [Transcript:Egil](https://runescape.wiki/w/Transcript%3AEgil)
- **Letter**: `E`

---

## Dialogue Transcript

{{Incomplete|Dialogue for exchanging cannons and for unknown brackets of sword rating percentages}}

### Talk to

- **Egil:** Welcome to the Artisans' Workshop. We've got normal smithing in the front, and burial smithing in the back!
- **Egil:** Also, I... my cousin will occasionally stop by and hand you some ceremonial sword plans to complete for extra experience.
- [Menu]: What would you like to say?
  - [Choice]: What's a ceremonial sword?
    - **Egil:** A ceremonial sword distinguishes the wielder from his peers. They are items of beauty and craftsmanship that are favoured by officers and the very rich.
    - **Player:** I'm guessing they're expensive?
    - **Egil:** Quite so. We use only the purest metal to get the most malleable and perfect swords. Each blade requires a lot of ore, which we smelt into a pure, dense metal. But if we give you some plans, we'll supply all the materials so you'll be able to freely smith your ceremonial sword!
    - (previous)
  - [Choice]: Can you show me how to make a ceremonial sword?
    - {{Qact|The player enters an instance of the workshop, wherein the ceremonial sword interface opens and a tutorial begins.}}
    - [You need to hammer the sword into the design above.]
    - [Choose points along the sword, hammering away as it cools. Once the sword is cool, you will no longer be able to work the sword.]
    - {{Qact|A soft hit is performed on the upper-right corner of the sword.}}
    - [There are different strengths of 'hit'.]
    - [pic=Hammer detail.png]
    - {{Qact|A hard hit is performed on the upper-right corner of the sword.}}
    - [pic=Hammer detail.png]
    - {{Qact|A medium hit is performed on the lower-right corner of the sword.}}
    - [pic=Hammer detail.png]
    - {{Qact|A soft hit is performed on the lower-right corner of the sword.}}
    - [pic=Hammer detail.png]
    - {{Qact|A careful hit is performed on the lower-right corner of the sword.}}
    - [pic=Hammer detail.png]
    - **Egil:** Once your sword is as close to the plans as possible, or it has cooled down, speak to me.
    - {{Qact|Sten walks over to face Egil.}}
    - **Egil:** I'll reward you with extra experience based on how closely you kept to the design.
    - {{Qact|The screen fades out to black then back in; the player is back in the non-instanced workshop.}}
  - [Choice]: Can you rate my sword?|cond=If the player has ceremonial sword plans in their backpack
    - (removes=the ceremonial sword plans)
    - ((If the sword was between [unknown] to 99%:) <!-- lower bound is ≤ 88 -->
      - Your sword is awarded [number]% of its potential experience. Reasonable work.
    - ((For other ranges:))
      - {{Transcript missing}}
      - Your sword is awarded [number]% of its potential experience.
  - [Choice]: Who are you?
    - **Egil:** I am Egil, ceremonial sword specialist and, apparently, one of the workshop's more senior artisans.
    - **Player:** Apparently?
    - **Egil:** I don't hold much stock in titles. They garnish the ego, but are rather impractical.
    - (previous)
  - [Choice]: Can I change my cannon?
    - (Condition: If the player doesn't have a cannon:)
      - **Egil:** I'm afraid you don't have any cannon upgrades unlocked. You can unlock golden and royale cannon upgrades here at my store, or different upgrades through other methods you may uncover on your travels.
      - (previous)
    - (Condition: Otherwise:)
      - [Menu]: Choose an option:
        - [Choice]: Dwarf multicannon.
          - ((If the player did not bring their existing multicannon in their backpack:))
            - You need to bring a golden, royale, or siege engine multicannon to exchange for a normal dwarf multicannon.
            - **Egil:** Don't waste my time, we're not giving you multicannons for free! You'll need to bring in a multicannon and I'll convert it.
            - (initial)
          - ((Otherwise:))
            - {{Transcript missing}}
        - [Choice]: Gold multicannon.
          - ((If the player did not bring their existing multicannon in their backpack:))
            - You need to bring a normal, royale, or siege engine multicannon to exchange for a golden dwarf multicannon.
            - **Egil:** Don't waste my time, we're not giving you multicannons for free! You'll need to bring in a multicannon and I'll convert it.
            - (initial)
          - ((Otherwise:))
            - {{Transcript missing}}
        - [Choice]: Royale multicannon.|cond=If the player has unlocked the royale cannon:
          - ((If the player did not bring their existing multicannon in their backpack:))
            - You need to bring a normal, golden, or siege engine multicannon to exchange for a royale dwarf multicannon.
            - **Egil:** Don't waste my time, we're not giving you multicannons for free! You'll need to bring in a multicannon and I'll convert it.
            - (initial)
          - ((Otherwise:))
            - {{Transcript missing}}
  - [Choice]: [More...]
    - [Menu]: What would you like to say:
      - [Choice]: Luminite Injector?
        - **Player:** What is a luminite injector?
        - **Egil:** If you activate it anywhere in the workshop, it'll overload the pipes within the workshop, causing you and everyone else to generate more progress while smithing!
        - **Player:** That sounds dangerous. How long does it last?
        - **Egil:** Ah, the workshop can take it! She might burst a pipe every now and then, though. They each last for 5 minutes, but you can queue several up to work at once.
        - (Condition: If luminite injectors are active:)
          - **Egil:** In fact, there is one active right now! It'll expire in [time given in minutes and seconds].
        - (initial)
      - [Choice]: Are there any rewards?
        - (opens=Artisans' Workshop Reward Shop)
      - [Choice]: Goodbye.
        - (end)
      - [Choice]: [More...]
        - (initial)

### Rewards

- (opens=Artisans' Workshop Reward Shop)

### Change cannon

- (above2|cannon)
