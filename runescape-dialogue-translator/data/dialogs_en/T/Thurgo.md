# Thurgo

- **Original Wiki Page**: [Transcript:Thurgo](https://runescape.wiki/w/Transcript%3AThurgo)
- **Letter**: `T`

---

## Dialogue Transcript


### At Mudskipper Point


#### During The Knight's Sword

- (see|The Knight's Sword#Talking to Thurgo)

#### After the Knight's Sword

- [Menu]: What would you like to ask about? {{anchor|standard}}
  - [Choice]: Skillcape of Smithing
    - (Condition: If the player is below 99 Smithing:)
      - **Player:** That's an unusual cape you're wearing, what is it?
      - **Thurgo:** It's a Skillcape of Smithing. Shows that I am a master blacksmith, but of course that's only to be expected. I am an Imcando dwarf after all and everybody knows we're the best blacksmiths.
    - (Condition: If the player has 99 Smithing and has a ring of charos (a) equipped:)
      - **Thurgo:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
      - [Menu]: Choose an option:
        - [Choice]: 92,000 coins? That's much too expensive.
          - **Player:** I know where to find you if I change my mind.
        - [Choice]: I think I have the money right here, actually.
          - (Condition: If the player has no backpack space:)
            - **Thurgo:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some backpack space before I can sell you one.
          - (Condition: If the player does not have enough money:)
            - **Player:** But unfortunately, I was mistaken.
            - **Thurgo:** Well, come back and see me when you do.
          - (Condition: If the player has enough money:)
            - (receives=Smithing cape and Smithing hood) (removes=92,000 coins)
            - **Thurgo:** Excellent! Wear that cape with pride my friend.
        - [Choice]: cond=If the player has 120 Smithing|I've mastered this skill. Is there anything else?
          - **Thurgo:** There is something...though I have kept it a secret for a very long time. It is something that can only be worn by a true master.
          - **Thurgo:** Not even I can wear it - that's how hard it is to achieve.
          - **Thurgo:** You say you're a master. Stand straight, let me take a look at you.
          - **Thurgo:** You...really have mastered it. What an honour! It would be my pleasure to sell you a Smithing master cape.
          - [Menu]: Buy Smithing master cape for 120,000 coins?
            - [Choice]: Yes.
              - (Condition: If the player has no backpack space:)
                - **Thurgo:** You do not have enough room in your backpack. Please come back when you have some more.
              - (Condition: If the player does not have enough money:)
                - You do not have enough money to purchase this cape.
              - (Condition: If the player has enough money:)
                - (receives=Smithing master cape) (removes=120,000 coins)
                - {{qact|Master cape music plays.}}
            - [Choice]: No.
              - (end)
    - (Condition: If the player has 99 Smithing but does not have a ring of charos (a) equipped:)
      - [Menu]: Choose an option:
        - [Choice]: 99,000 coins? That's much too expensive.
          - **Player:** I know where to find you if I change my mind.
        - [Choice]: I think I have the money right here, actually.
          - (Condition: If the player has no backpack space:)
            - (above)
          - (Condition: If the player does not have enough money:)
            - (above)
          - (Condition: If the player has enough money:)
            - (receives=Smithing cape and Smithing hood) (removes=99,000 coins)
            - **Thurgo:** Excellent! Wear that cape with pride my friend.
        - [Choice]: cond=If the player has 120 Smithing|I've mastered this skill. Is there anything else?
          - (above)
  - [Choice]: cond=If the player has 99 Smithing|I've noticed there are a couple of versions of each skillcape.
    - **Thurgo:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
    - (Condition: If the player is using the old model:)
      - **Thurgo:** It looks like you're currently using the old model for your Smithing skillcape. Would you like to change to the newer one?
      - (continue)
    - (Condition: If the player is using the new model:)
      - **Thurgo:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
      - (continue)
    - [Menu]: Select an Option
      - [Choice]: Yes, I would like to wear the [new/old] version of the skillcape.
        - **Thurgo:** Would you like to wear the [old/newer] model for just this cape, or for the Quest Cape and all of the skillcapes you own?
        - [Menu]: Select an Option
          - [Choice]: I would just like to change the Smithing skillcape.
            - **Thurgo:** No problem, you will now use the [older/newer] model for your Smithing skillcape.
          - [Choice]: I would like to change all my skillcapes.
            - **Thurgo:** No problem, you will now use the [older/newer] model for all of your skillcapes!
          - [Choice]: I've changed my mind!
            - (end)
      - [Choice]: No, thank you.
        - **Thurgo:** Great! I'm glad you're still enjoying the [old/new] version!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Thurgo:** If you want, I can make it so you use the old model for all of the skillcapes you own.
          - [Menu]: Select an Option
            - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
              - **Thurgo:** Great, you will now use the old model for all of your skillcapes!
            - [Choice]: No, thanks.
              - (end)
  - [Choice]: Something else.
    - **Player:** About that sword...
    - **Player:** Thanks for all your help in getting it for me!
    - **Thurgo:** No worries mate.

#### After Birthright of the Dwarves while having Imcando pickaxe pieces in inventory

- **Thurgo:** A tingling in my Imcando bones! Can it really be...
- **Thurgo:** Yes! You've found part of an ancient Imcando pickaxe! May I take a look at it?
- [Menu]: Select an Option
  - [Choice]: Please do.
    - *(If you have one to three Imcando pickaxe fragment in your inventory:)*
      - **Thurgo:** Yes! You have a piece of the ancient Imcando pickaxe! If you bring me all four pieces, I can recreate the pickaxe for you.
      - (continue|MakePickaxe)
    - *(If you have all four Imcando pickaxe fragments in your inventory:)*
      - **Thurgo:** You have all four pieces! With these, I can recreate an ancient Imcando pickaxe for you!
      - (continue|MakePickaxe)
    - **Thurgo:** It won't be easy, though. As well as the pieces, I'll need a gilded dragon pickaxe, and one million coins to buy other materials.
    - **Thurgo:** And a redberry pie, of course. Smithing makes me hungry!
    - [Menu]: Select an Option
      - [Choice]: If the player has all necessary items in backpack|I have those things with me now.
        - **Player:** I have those things with me now.
        - **Thurgo:** Excellent! Let me get to work.
        - {{qact|Screen fades out and then fades in.}}
        - (removes=1,000,000 coins, the four Imcando pickaxe fragments and the redberry pie)
        - (receives=the Imcando pickaxe)
        - [Thurgo creates a magical pickaxe for you.]
      - [Choice]: An Imcando pickaxe?
        - **Player:** An Imcando pickaxe?
        - [The Imcando pickaxe is equivalent to a bane pickaxe +4, and similarly requires 80 Mining to use. Unlike a bane pickaxe, the Imcando pickaxe can be augmented with the Invention skill.]
      - [Choice]: Thanks, bye.
        - (end)
  - [Choice]: Ask about something else.
    - (above|standard)

#### While having Imcando mattock pieces in inventory

- **Thurgo:** A tingling in my Imcando toes! Is that really what I think it is?
- **Thurgo:** Yes! You've come across a very rare thing. Some unforged Imcando metal. Do you mind if I take a look at it?
- [Menu]: Select an Option
  - [Choice]: Please do.
    - ((If the player doesn't have all four Imcando pieces:))
      - **Thurgo:** Yes! You have a piece of the ancient Imcando metal! With Archaeology being the big craze right now, if you bring me all four pieces, I can teach you how to make your very own Imcando mattock.
      - (continue|MakeMattock)
    - ((If the player has all four Imcando pieces:))
      - [Menu]: Select an Option
        - [Choice]: Can you help me make a mattock?
          - **Thurgo:** You have enough pieces! With these, rather than do it myself, I can actually teach you how to work Imcando metals and make the mattock for yourself.
          - (continue|MakeMattock)
        - [Choice]: Can you help me make a pickaxe?
          - **Thurgo:** Sadly not, for a tool as large as an Imcando pickaxe I'd require some much larger pieces, with Archaeology being the big craze right now this is enough for a mattock.
          - (previous)
    - **Thurgo:** It won't be easy, though. As well as the pieces, I'll need a dragon mattock, and one million coins for the time.
    - **Thurgo:** And a redberry pie, of course.
    - [Menu]: Select an Option
      - [Choice]: cond=If the player has all of the required items|I have those things with me now.
        - **Thurgo:** Lets get to work.
        - {{Qact|Screen fades out to black then back in.}}
        - (removes=redberry pie and 1,000,000 coins)
        - You've learnt how to create an Imcando mattock, take the Imcando metal to an anvil in the warforge.
        - **Thurgo:** ...and then once you bind these two pieces together with some flux to prevent the metal from oxidising. You've made yourself a tool the dwarves would be proud to weild{{Sic}}.
        - **Player:** Thank you, Thurgo.
      - [Choice]: cond=If the player does not have all four Imcando pieces|An Imcando mattock
        - (below|AskAboutMattock)
      - [Choice]: cond=If the player has all four Imcando pieces|An Imcando mattock?
        - **Thurgo:** With all the ancient sites that have been uncovered lately, it only feels right to equip the best archaeologists with the tools and means to uncover the secrets of our ancestory.
        - **Thurgo:** If you can find enough of these rare Imcando metals, I can teach you how to create a such a tool for yourself.
      - [Choice]: Thanks, bye.
        - (end)
  - [Choice]: Ask about something else.
    - (above|standard)

#### After Song from the Depths while having a coral crossbow in inventory

- **Thurgo:** You! May I take a look at that coral crossbow?
- [Menu]: Select an Option
  - [Choice]: Please do.
    - **Thurgo:** This is amazing engineering! Your crossbow could become extremely powerful if we added the right components onto it.
    - **Thurgo:** Unfortunately, judging by the materials, the flames you'll need to forge these components together will need to be extremely hot; far beyond anything any conventional forge could produce. You'd probably need an ancient
    - **Thurgo:** dragon from the legends to produce a flame hot enough!
    - **Thurgo:** In the meantime, I can perform a basic assembly of these components if you'd like; it won't be usable as a weapon until you expose it to extreme heat, though.
    - [Menu]: Assemble the unforged royal crossbow?
      - [Choice]: Yes.
        - *(If royal crossbow parts are missing:)*
          - You are missing the following components: <br>a bolt stabiliser <br>a frame <br>a sight <br>a spring
        - *(If all royal crossbow parts are present:)*
          - (removes=royal torsion spring, royal stabiliser, royal sight and royal frame) (receives=Royal crossbow (unforged))
          - Thurgo starts assembling the crossbow. Thurgo hands you the unforged crossbow.
          - **Thurgo:** You need to expose it to extreme heat to finish the process. I'll probably be able to perform any maintenance needed once that's done, if you'll let me.
      - [Choice]: Not right now.
        - (above|standard)
  - [Choice]: Ask about something else.
    - (above|standard)

#### While having Imcando hatchet pieces in inventory

- **Thurgo:** A tingling in my Imcando fingers! Is that...
- **Thurgo:** Yes! You've found part of an ancient Imcando hatchet! May I take a look at it?
- [Menu]: Select an Option
  - [Choice]: Please do.
    - (Condition: If the player doesn't have all four Imcando hatchet fragments:)
      - **Thurgo:** Yes! You have a piece of the ancient Imcando hatchet! If you bring me all four pieces, I can recreate the hatchet for you.
    - (Condition: If the player has all four Imcando hatchet fragments:)
      - **Thurgo:** You have all four pieces! With these, I can recreate an ancient Imcando hatchet for you!
    - **Thurgo:** It won't be easy, though. As well as the pieces, I'll need a dragon hatchet, and one million coins to buy other materials.
    - (Condition: If the player doesn't have all four Imcando hatchet fragments:)
      - **Thurgo:** And a redberry pie, of course. Smithing makes me hungry!
    - (Condition: If the player has all four Imcando hatchet fragments:)
      - **Thurgo:** And as I'm sure you know by now, my redberry pie is of utmost importance!
    - [Menu]: Select an Option
      - [Choice]: cond=Only with all the required items:|I have those things with me now.
        - **Thurgo:** Excellent! Let me get to work.
        - {{Qact|The screen fades out and back in.}}
        - (removes=the Imcando hatchet fragments, dragon hatchet, redberry pie, and a million coins) (receives=an Imcando hatchet)
        - (Condition: If receiving an Imcando hatchet for the first time:)
          - Congratulations! You have completed: 'Imcando at a tree' - Obtain an Imcando hatchet.
          - (continue)
        - [Thurgo creates a magical hatchet for you.]
      - [Choice]: An Imcando hatchet?
        - **Thurgo:** It's an ancient dwarven artefact, isn't that exciting enough?
        - **Thurgo:** An  hatchet will be far better at cutting trees than a dragon hatchet, that's for sure.
        - (Condition: If the player has a crystal hatchet on their toolbelt:)
          - **Player:** Oh, I already have a crystal hatchet on my toolbelt. It's an enhanced dragon hatchet!
          - **Thurgo:** This flimsy thing? Bah! An Imcando hatchet will cut right through it!
      - [Choice]: Thanks, bye.
        - (end)
  - [Choice]: Ask about something else.
    - (above|standard)

### At Thalmund's forge

- ((One of the following sequences is seen.))

#### Giving him a redberry pie

- **Thurgo:** {{RSChat|Thanks, pal!}}

#### Sequence 1

- (Thurgo appears at the northern doors.)
- (Thurgo walks to the debris in the south.)
- **Thurgo:** {{RSChat|Needs a clean.}}
- (Thurgo walks to the lever.)
- **Thurgo:** {{RSChat|Smells like pie and slag.}}
- (Thurgo walks to the room with the imcando anvil and investigates it.)
- (Thurgo walks to the furnace.)
- **Thurgo:** {{RSChat|Impressive.}}
- (Thurgo walks to the goblin weapon rack, investigates it and teleports out.)

#### Sequence 2

- (Thurgo appears at the northern doors.)
- (Thurgo walks to the debris in the south.)
- **Thurgo:** {{RSChat|What a mess!}}
- (Thurgo walks to the lever.)
- **Thurgo:** {{RSChat|Hmmm...}}
- (Thurgo walks to the room with the imcando anvil and investigates it.)
- (Thurgo walks to the furnace.)
- **Thurgo:** {{RSChat|Not bad.}}
- (Thurgo walks to the goblin weapon rack, investigates it and teleports out.)
