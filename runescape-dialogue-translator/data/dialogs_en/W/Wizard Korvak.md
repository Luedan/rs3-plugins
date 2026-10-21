# Wizard Korvak

- **Original Wiki Page**: [Transcript:Wizard Korvak](https://runescape.wiki/w/Transcript%3AWizard%20Korvak)
- **Letter**: `W`

---

## Dialogue Transcript

{{Incomplete|missing dialogue from having omni-talisman + runecrafting staff/tiara in the backpack}}

### Standard dialogue

- **Wizard Korvak:** AAAAAAAAAAH! Don't sneak up on me like that.
- **Player:** Uh, sorry.
- [Menu]: Choose an option:
  - [Choice]: Can you help me with my essence pouches?
    - **Player:** Can you help me with my essence pouches?
    - (Condition: If the player doesn't have any pouches that need repair:)
      - **Wizard Korvak:** You don't have any pouches that need repair...I could sell you a pouch, but only if you don't tell!
      - [Menu]: Select an option
        - [Choice]: I'd like to buy a pouch.
          - (continue|Trade option)
        - [Choice]: Never mind.
          - **Player:** Never mind.
    - (Condition: If the player has pouches that need repair:)
      - **Wizard Korvak:** I can restore them for a price - for a price, indeed. Muahahahahaahaha!
      - **Player:** Uh, what kind of a price?
      - **Wizard Korvak:** Whatever the voices tell me to ask for. Currently, they require 9.000 gp for a large pouch and 12,000 gp for a giant pouch. Shhhh, don't tell any one else: I have a connection on the inside and I can sell you pouches too. For a mere 25,000 gp, you can have a large pouch. A reasonable 50,000 gp will get you a giant pouch.
        - [Choice]: I'd like to have a pouch repaired.
          - **Player:** I'd like to have a pouch repaired.
          - **Wizard Korvak:** Very well. Let's have a look at it.
          - (continue|Repair-all option)
        - [Choice]: I'd like to buy a pouch.
          - (continue|Trade option)
  - [Choice]: cond=If the medium pouch has been lost:|I've lost my medium-sized pouch. Could you replace it?
    - **Player:** I've lost my medium-sized pouch. Could you replace it?
    - (receives=medium pouch)
    - **Wizard Korvak:** Lost it, did you? Or did they take it back? CLAIM IT BACK! Quick, better have another before the spoons come.
  - [Choice]: Why are you so jumpy?
    - **Player:** Why are you so jumpy?
    - **Wizard Korvak:** I am not jumpy! I am insane. There is a difference.
    - **Player:** If you are insane, wouldn't you think you were sane and so be insensible to the insanity that is you?
    - **Wizard Korvak:** Yebno.
    - **Player:** Beg your pardon?
    - **Wizard Korvak:** Yebno. It's a fast way of saying Yes Maybe No. Since I didn't know the answer to your question I gave you all of the answers.
    - **Player:** How did you end up in your rather peculiar mindset?
    - **Wizard Korvak:** They sent me to the place. They knew the dark wizards were there and someone had betrayed them. Us. So they sent me to spy. To the place. They sent me and would not let me come back.
    - **Player:** Who sent you? What betrayal?
    - **Wizard Korvak:** He sits there with the spinning light, always thinking. One of us led them to the place where the pickaxe hammers and so the betrayal happened. Please don't make me talk about it.
    - **Player:** Okay, we don't have to talk about it.
  - [Choice]: Who is that wizard outside the guild portal?
    - **Wizard Korvak:** Ah, the young Finix: brilliant young wizard!
    - **Vief:** Young troublemaker, more like!
    - **Wizard Korvak:** Just because his theories clash with yours, it doesn't make them incorrect.
    - **Vief:** The sheer notion of the altars running out is preposterous! You cannot run out of space in an infinitely folded dimension.
    - **Wizard Korvak:** Just because the space is infinite, it doesn't mean the energy inside fills all the space.
    - **Vief:** Of course it does! We all know that the energy inside a dimension must be evenly spread to stop it collapsing in on itself.
    - **Wizard Korvak:** That may be true, but why are the altars in Gielinor cracked, then?
    - **Player:** Er...I'm going to leave you guys to it.
  - [Choice]: Never mind.
    - **Player:** Never mind.

### Trade option

- **Player:** I'd like to buy a pouch.
- **Wizard Korvak:** Ah, coins to fund my rock collection.
- [Menu]: Which pouch would you like to buy?
  - [Choice]: Buy a large pouch for 25,000 gp.
    - (Condition: If the player doesn't already have a large pouch:)
      - (removes=25,000 coins) (receives=large pouch)
    - (Condition: If the player already has a large pouch:)
      - **Wizard Korvak:** You already own a large pouch! Don't you know you'll unbalance the world by having two? Dogs will hate cats, mice will dance, and they will all come for me. No, no pouch for you.
  - [Choice]: Buy a giant pouch for 50,000 gp.
    - (Condition: If the player doesn't already have a giant pouch:)
      - (removes=50,000 coins) (receives=giant pouch)
    - (Condition: If the player already has a large pouch:)
      - **Wizard Korvak:** No, no, no. They told me when I was there. Only one precious pouch, per size, per person. No more. I cannot sell you this pouch, or they might make me return there for punishments.
  - [Choice]: Never mind.
    - **Player:** Never mind.

### Repair-all option

- [Menu]: Which pouch would you like to repair?
  - [Choice]: Repair large pouch for 9,000 gp.
    - (Condition: If the pouch needs repair:)
      - **Wizard Korvak:** Magic makes me happy, magic makes me glad, magic makes the voices quiet, and nothing rhymes with purple.
    - (Condition: If the pouch does not need repair:)
      - **Wizard Korvak:** The voices are angry at you! You have nothing to repair. Leave us be.
    - (Condition: If the player does not have enough money:)
      - {{Transcript missing}}
  - [Choice]: Repair giant pouch for 12,000 gp.
    - (Condition: If the pouch needs repair:)
      - **Wizard Korvak:** Ahhh, the simple act of a transformation spell. So soothing. It makes the voices quiet. Your pouch is repaired.
    - (Condition: If the pouch does not need repair:)
      - **Wizard Korvak:** The voices are angry at you! You have nothing to repair. Leave us be.
    - (Condition: If the player does not have enough money:)
      - {{Transcript missing}}
  - [Choice]: Never mind.
    - (end)
