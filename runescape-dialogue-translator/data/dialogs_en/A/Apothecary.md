# Apothecary

- **Original Wiki Page**: [Transcript:Apothecary](https://runescape.wiki/w/Transcript%3AApothecary)
- **Letter**: `A`

---

## Dialogue Transcript

{{External|os|rsc}}

### In Varrock


#### Standard dialogue

- **Apothecary:{{anchor|brew}}** I am the Apothecary. I brew potions. Do you need anything specific?
- {{tselect|Select an option}}
  - {{topt|Can you make a strength potion?}}
    - **Player:** Can you make a strength potion?
    - {{tcond|Without the ingredients:}}
      - **Apothecary:** Yes, but the ingredients are a little to hard to find. If you ever get them I will make it for you, for a fee.
      - **Player:** So what are the ingredients?
      - **Apothecary:** You'll need to find the eggs of the deadly red spider and a limpwurt root.
      - **Apothecary:** Oh and you'll have to pay me 5 coins.
      - **Player:** Ok, I'll look out for them.
    - {{tcond|With the ingredients:}}
      - **Apothecary:** Certainly. I see you have the spider eggs and limpwurt root. Hand them over, and pay me 5 coins per potion, and I'll get started.
      - {{tselect|Select an option}}
        - {{topt|Okay, that sounds fine.}}
          - **Player:** Okay, that sounds fine.
          - {{tact|removes=red spiders' eggs, limpwurt root and 5 coins}} {{tact|receives=strength potion (4)}}
          - {{tcond|If this is the first time having a strength potion made at the apothecary:}}
            - {{RSFontAchievement|Double-strength Weaksauce}}
            - {{tact|continue}}
          - {{tbox|pic=Strength potion (4) detail.png|The Apothecary gives you a strength potion.}}
        - {{topt|No, forget it.}}
          - **Player:** No, forget it.
  - {{topt|Do you know a potion to make hair fall out?}}
    - **Player:** Do you know a potion to make hair fall out?
    - **Apothecary:** I do indeed. I gave it to my mother. That's why I now live alone.
  - {{topt|Have you got any good potions to give away?}}
    - **Player:** Have you got any good potions to give away?
    - {{tcond|With an acne potion in the backpack:}}
      - **Apothecary:** Only that spot cream. Hope you enjoy it.
    - {{tcond|Without an acne potion in the backpack:}}
      - {{tcond|If the Apothecary accepts the player's request:}}
        - **Apothecary:** Ok then. Try this potion.
        - {{tact|receives=acne potion}}
      - {{tcond|If the Apothecary declines the player's request:}}
        - **Apothecary:** Sorry, charity is not my strong point.
  - {{topt|Can you make a potion that makes it seem like I'm dead?}}
    - **Player:** Can you make a potion that makes it seem like I'm dead?
    - **Apothecary:** What a strange and morbid request! I can as it happens. The berry of the cadava bush, prepared properly, will induce a coma so deep that you will seem to be dead. It's very dangerous.
    - **Apothecary:** I have the other ingredients, but I'll need you to bring me one bunch of cadava berries.
    - {{tcond|Without cadava berries in the backpack:}}
      - **Player:** I'll bear that in mind.
    - {{tcond|With cadava berries in the backpack:}}
      - {{tselect|Select an option}}
        - {{topt|Take these cadava berries.}}
          - **Player:** Take these cadava berries.
          - {{tbox|You hand over the berries, which the Apothecary shakes up in a vial of strange liquid.}}
          - {{Qact|The apothecary mixes the potion}}
          - **Apothecary:** Phew! Here is what you need.
          - {{tact|removes=cadava berries}} {{tact|receives=cadava potion}}
          - {{tbox|pic=cadava potion detail.png|The apothecary gives you a Cadava potion.}}
        - {{topt|No thanks.}}
          - **Player:** No thanks.
  - {{topt|cond=After Rat Catchers:|You wouldn't be able to make any other cat potions, would you?}}
    - **Player:** You wouldn't be able to make any other cat potions, would you?
    - **Apothecary:** I have no plans to branch out into cat potions at the moment, but if there was sufficient demand for them I might change my mind.

#### Using Herbi Flax's diary on him

- {{tbox|pic=Diary (Shades of Mort'ton) detail.png|You show the Serum book to the Apothecary.}}
  - (Condition: If not already given:)
    - **Apothecary:** Do you want to trade the diary yet? I'd like to pass the information on to the scientific community in Varrock.
    - {{tselect|Select an option}}
      - {{topt|Yes, I'll trade it for herblore training.}}
        - **Player:** Yes, I'll trade it for herblore training.
        - **Apothecary:** Great...
        - {{tbox|The apothecary trains you in herblore.}}
        - {{tact|The player has Diary (Shades of Mort'ton) removed from them, and gains 335 Herblore experience.}}
        - Congratulations! You have completed: 'Herbi Flax' - Give Herbi Flax's diary to the Varrock apothecary.
        - **Apothecary:** Ok, that's all I can teach you. Many thanks for the diary.
      - {{topt|No thanks, I want to keep hold of it a bit longer.}}
        - **Player:** No thanks, I want to keep hold of it a bit longer.
        - **Apothecary:** Oh, that's a shame... Come back if you change your mind.
  - (Condition: If already given:)
    - **Apothecary:** Hmm, this is an interesting tome... But you've already sold me one, thanks!

#### If the player has lost their Nurse's or Doctor's hat

- {{tselect|Choose an option:}}
  - {{topt|Ask for another Nurse's or Doctor's hat.}}
    - **Player:** Hello Apothecary, I've lost that hat you gave me.
    - **Apothecary:** No problem, I get plenty of these from Gielinorian Hospital Supplies.
    - {{tselect|Choose a hat}}
      - {{topt|Nurse's Hat}}
        - {{tbox|pic=Nurse hat detail.png|The Apothecary has given you a Nurse's Hat.}}
        - {{tact|receives=nurse hat}}
        - **Apothecary:** Then all you need to do is give him a vial of water and he'll take it thinking it's a cure potion.
        - **Player:** Haha! I always wanted to be a Nurse!
      - {{topt|Doctor's Hat}}
        - {{tbox|pic=Doctors hat detail.png|The Apothecary has given you a Doctor's Hat.}}
        - {{tact|receives=doctors hat}}
        - **Apothecary:** Then all you need to do is give him a vial of water and he'll take it thinking it's a cure potion.
        - **Player:** Haha! I always wanted to be a Doctor!
  - {{topt|Talk about something else.}}
    - {{tact|above|brew}}

### In New Varrock

- **Apothecary:{{anchor|brew}}** I am the Apothecary. I brew potions. <br>Do you need anything specific?
- {{tselect|Choose an option:}}
  - {{topt|Can you make a strength potion?}}
    - (Condition: Before Dimension of Disaster: Demon Slayer:)
      - **Apothecary:** Normally, I'd be happy to oblige, but some of my more dangerous ingredients have been impounded in Delrith's demon camp.
      - **Apothecary:** If you ever manage to get in there, and can find my stash of red spider eggs and limpwurt roots, bring them to me.
      - **Apothecary:** As thanks, I'll give you the 'special friend' rate of five zemomarks per strength potion!
      - **Player:** I'll keep that in mind.
      - {{tact|initial}}
    - (Condition: After Dimension of Disaster: Demon Slayer:)
      - **Apothecary:** I'd be happy to oblige, but some of my more 'dangerous' ingredients have been impounded in Delrith's demon camp.
      - **Apothecary:** I've heard you can get in there - if you find my stash of red spider eggs and limpwurt roots, bring them to me. I'll only charge five zemomarks per strength potion.
      - **Apothecary:** Though, I only had a handful of ingredients - those things are hard to come by in New Varrock. Once they're gone, they're gone.
      - {{tact|initial}}
    - (Condition: With red spiders' eggs and limpwurt roots in backpack:)
      - **Apothecary:** Want me to use those to mix up some strength potions? Only five zemomarks per potion.
      - [Menu]: Select an Option
        - [Choice]: Yes.
          - (removes=three red spiders' eggs, three limpwurt roots and 15 zemomarks)
          - (receives=three strength potions)
          - (initial)
        - [Choice]: No.
          - (end)
  - {{topt|Can you make a potion that makes it seem like I'm dead?}}
    - **Apothecary:** What a strange and morbid request! I can, as it happens. The berry of the cadava bush, prepared properly, will induce a coma so deep that you will seem to be dead. It's very dangerous.
    - **Apothecary:** I have the other ingredients, but I'll need you to bring me one bunch of cadava berries.
    - (Condition: Without cadava berries in backpack:)
      - **Player:** I'll bear that in mind.
      - {{tact|initial}}
    - (Condition: With cadava berries in backpack:)
      - [Menu]: Select an Option
        - [Choice]: Take these cadava berries.
          - [You hand over the berries, which the apothecary shakes up in a vial of strange liquid.]
          - **Apothecary:** Phew!<br>Here is what you need.
          - (removes=cadava berries)
          - (receives=cadava potion)
          - [The apothecary gives you a cadava potion.]
        - [Choice]: No, thanks.
          - (initial)
  - {{topt|Nothing, thanks.}}
    - {{tact|end}}
