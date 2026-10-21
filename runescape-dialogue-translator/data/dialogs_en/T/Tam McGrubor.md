# Tam McGrubor

- **Original Wiki Page**: [Transcript:Tam McGrubor](https://runescape.wiki/w/Transcript%3ATam%20McGrubor)
- **Letter**: `T`

---

## Dialogue Transcript


### In Burthorpe


#### In free-to-play worlds

- **Tam McGrubor:** Hello there. Thanks for stopping!
- **Tam McGrubor:** Let me tell you about what I have here.
- **Player:** Are those hoods?
- **Tam McGrubor:** Not just hoods. These are wicked hoods! I call them that because they're so cool, and they look kind of evil too.
- **Tam McGrubor:** Not only will you look like a serious wizard in one of these, you can use its magical powers to help your spellcasting too.
- **Player:** What magical powers?
- **Tam McGrubor:** It can create free runes and rune essence for casting spells with, and it can occasionally teleport you to the mysterious ruins where runes are crafted.
- [Log in to a members' world to claim your free wicked hood.]

#### In members' worlds, without a wicked hood in backpack

- **Tam McGrubor:** Hello there. Thanks for stopping!
- {{anchor|fix-up}}**Tam McGrubor:** So, can I fix you up with one of these wicked hoods?
- [Menu]: Select an Option
  - [Choice]: Yes, please.
    - (Condition: Without space in backpack:)
      - [You need one space in your inventory for the hood.]
    - (Condition: With space in backpack:)
      - (receives=wicked hood)
      - [Tam hands you a wicked hood.]
    - (continue|second-set-options)
  - [Choice]: What does it do?
    - (below|what-does-it-do)
  - [Choice]: No thanks.
    - (end)

#### In members' worlds, with a wicked hood in backpack

- **Tam McGrubor:** Hello there. Thanks for stopping!
- {{anchor|second-set-options}}[Menu]: Select an Option
  - [Choice]: Can I get another hood?
    - **Tam McGrubor:** You already have one! If you ever lose yours, though, come by and I'll replace it.
    - **Player:** Okay.
  - [Choice]: How does this hood work, anyway?
    - {{anchor|what-does-it-do}}**Tam McGrubor:** It's a fancy hood for Runecrafting. It can conjure runes and rune essence, teleport you to runecrafting altars, and unlock access to them.
    - **Tam McGrubor:** Most important thing to remember is, that if you want to use an ability associated to a particular rune, you first need to unlock that rune type for your hood.
    - [Menu]: Select an Option
      - [Choice]: What runes can I get from the hood?|cond=If previously not selected:
        - **Tam McGrubor:** Once per day, the hood can create a stack of runes of any type that the hood has unlocked. Just reach in and pull them out!
        - **Player:** Once per day?
        - **Tam McGrubor:** It's got to recharge.
        - (previous)
      - [Choice]: How much rune essence can I get?|cond=If previously not selected:
        - **Tam McGrubor:** One hundred fine pieces of rune essence every day!
        - **Player:** I don't have room for that much essence at once.
        - **Tam McGrubor:** Don't worry. It'll make as much as you have room for and then you can make more once you have the space.
        - (previous)
      - [Choice]: What's this about teleporting?|cond=If previously not selected:
        - **Tam McGrubor:** The hood can teleport you to any of the runecrafting altars, as long as you've unlocked the corresponding rune.
        - **Tam McGrubor:** You only get two teleports per day, though. Two total, not two per altar.
        - (previous)
      - [Choice]: How do I unlock a rune?|cond=If previously not selected:
        - **Tam McGrubor:** You need to find the right sort of talisman, and feed it into the hood. Once you do that, that rune type will be permanently unlocked for the hood.
        - **Tam McGrubor:** The hood starts out with air and mind runes already unlocked. Other talismans come from all over the place.
        - **Tam McGrubor:** Sometimes monsters will have them, or you might be able to buy them from other adventurers.
        - (previous)
      - [Choice]: That's all I want to ask.
        - (Condition: If players don't currently have a wicked hood:)
          - (above|fix-up)
        - (Condition: If players have a wicked hood:)
          - (previous)
  - [Choice]: Goodbye.
    - (end)
