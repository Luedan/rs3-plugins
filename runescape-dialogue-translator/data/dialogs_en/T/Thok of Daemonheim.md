# Thok of Daemonheim

- **Original Wiki Page**: [Transcript:Thok of Daemonheim](https://runescape.wiki/w/Transcript%3AThok%20of%20Daemonheim)
- **Letter**: `T`

---

## Dialogue Transcript

{{Incomplete|missing dialogue to claim Daemonheim aura 4 for first time, skillcape dialogue is also outdated}}

### On Daemonheim Peninsula


#### Standard dialogue

- **Thok of Daemonheim:** What you want with Thok?
- [Menu]: Select an Option
  - [Choice]: What is this place?
    - **Player:** What is this place?
    - **Thok of Daemonheim:** This is camp. This where warriors rest and prepare for onslaught.
    - **Thok of Daemonheim:** Thok wait here to reward those who survive Daemonheim, who show might as great as Thok's.
    - [Menu]: Select an Option
      - [Choice]: Daemonheim?
        - **Player:** Daemonheim?
        - **Thok of Daemonheim:** It mean Demon Halls. Name not quite right, as there worse things than demons in Daemonheim. It less a hall and more a pit, too. Some say it has no end, but Thok know better.
        - [Menu]: Select an Option
          - [Choice]: What is this place?
            - (above|what-is-this-place)
          - [Choice]: What can I do here?
            - (below|what-can-i-do-here)
          - [Choice]: cond=If the player does not have 99 Dungeoneering|What is that cape beside you?
            - (below|what-is-cape)
          - [Choice]: cond=If the player has 99 Dungeoneering|Can I buy a Skillcape of Dungeoneering?
            - (below|can-buy-cape)
      - [Choice]: What can I do here?
        - (below|what-can-i-do-here)
      - [Choice]: cond=If the player does not have 99 Dungeoneering|What is that cape beside you?
        - (below|what-is-cape)
      - [Choice]: cond=If the player has 99 Dungeoneering|Can I buy a Skillcape of Dungeoneering?
        - (below|can-buy-cape)
  - [Choice]: What can I do here?
    - **Player:** What can I do here?
    - **Thok of Daemonheim:** Up path is Daemonheim. It hold more treasure than Thok can put in his pockets, which is lucky for you, but it guarded by countless monsters, which is unlucky for you. First-timers should talk to tutor before going into castle.
    - [Menu]: Select an Option
      - [Choice]: What is this place?
        - (above|what-is-this-place)
      - [Choice]: cond=If the player does not have 99 Dungeoneering|What is that cape beside you?
        - (below|what-is-cape)
      - [Choice]: cond=If the player has 99 Dungeoneering|Can I buy a Skillcape of Dungeoneering?
        - (below|can-buy-cape)
  - [Choice]: cond=If the player does not have 99 Dungeoneering|What is that cape beside you?
    - **Player:** What is that cape beside you?
    - **Thok of Daemonheim:** Ah, this Dungeoneering skillcape. It mark bearer as true master of Demon Halls.
    - **Thok of Daemonheim:** Though Thok has been far into Daemonheim, no-one believe him. So, Thok must guard skillcape, and offer it to brave warriors who find bottom of this place.
    - [Menu]: Select an Option
      - [Choice]: What is this place?
        - (above|what-is-this-place)
      - [Choice]: What can I do here?
        - (above|what-can-i-do-here)
      - [Choice]: Daemonheim?
        - (above|daemonheim)
  - [Choice]: cond=If the player has 99 Dungeoneering|Can I buy a Skillcape of Dungeoneering?
    - **Player:** Can I buy a Skillcape of Dungeoneering?
    - (Condition: If the player has 99–119 Dungeoneering:)
      - **Thok of Daemonheim:** Thok say it okay. You are great warrior and Thok will raise a drink to you this eventide.
      - **Thok of Daemonheim:** Thok must ask for 99,000 coins for materials, though.
      - (Condition: If the player has an inverted skillcape token:)
        - **Thok of Daemonheim:** Thok see you have inversion coin! Thok will take that and offer you different colour cape.
        - (removes=any inverted skillcape tokens and inverted master skillcape tokens)
      - [Menu]: Choose an option:
        - [Choice]: 99,000 coins? That's much too expensive.
          - **Player:** 99,000 coins? That's much too expensive.
          - **Thok of Daemonheim:** Not at all; there are many other adventurers who would love the opportunity to purchase such a prestigious item! You can find me here if you change your mind.
        - [Choice]: I think I have the money right here, actually.
          - **Player:** I think I have the money right here, actually.
          - (99,000 coins are taken from the player in exchange for Dungeoneering cape.)
          - **Thok of Daemonheim:** Excellent! Wear that cape with pride my friend.
    - ((If the player has 120 Dungeoneering:))
      - **Thok of Daemonheim:** Thok say he impressed. For being true master of skill you have option for two skillcapes.
      - [Menu]: Choose an option:
        - [Choice]: Buy the level 99 skillcape.
          - **Thok of Daemonheim:** Thok must ask for 99,000 coins for materials, though.
          - [Menu]: Choose an option:
            - [Choice]: 99,000 coins? That's much too expensive.
              - (above)
            - [Choice]: I think I have the money right here, actually.
              - (above)
            - [Choice]: I'd like a skillcape with the colours inverted.|cond=If the player has given Thok an inverted skillcape token:
              - {{tmissing}}
            - [Choice]: I've mastered this skill. Is there anything else?
              - **Thok of Daemonheim:** There is something...though I have kept it a secret for a very long time. It is something that can only be worn by a true master.
              - **Thok of Daemonheim:** Not even I can wear it - that's how hard it is to achieve.
              - **Thok of Daemonheim:** You say you're a master. Stand straight, let me take a look at you...
              - **Thok of Daemonheim:** You...really have mastered it. What an honour! It would be my pleasure to sell you a Dungeoneering master cape.
              - [Menu]: Buy Dungeoneering master cape for 120,000 coins?
                - [Choice]: Yes.
                  - (120,000 coins are taken from the player in exchange for Dungeoneering master cape.)
                - [Choice]: No.
                  - (end)
            - [Choice]: I'd like a master cape with the colours inverted.|cond=If the player has given Thok an inverted master skillcape token:
              - {{tmissing}}
        - [Choice]: Buy the level 120 skillcape.
          - **Thok of Daemonheim:** Thok must ask for 120,000 coins for materials, though.
          - (Condition: If the player has an inverted skillcape token:)
            - **Thok of Daemonheim:** Thok see you have inversion coin! Thok will take that and offer you different colour cape.
            - (removes=any inverted skillcape tokens and inverted master skillcape tokens)
          - [Menu]: Choose an option:
            - [Choice]: No, that's too much.
              - **Player:** No, that's too much.
              - **Thok of Daemonheim:** Thok would offer loan, but has spent all money on beer.
            - [Choice]: Okay, that seems reasonable.
              - (Condition: If the player has given Thok an inverted master skillcape token:)
                - [Menu]: Select an Option
                  - [Choice]: I would like a normal master cape.
              - (above|buy-master-cape)
                  - [Choice]: I would like an inverted master cape.
                    - [Menu]: Buy Dungeoneering master cape for 120,000 coins?
                      - [Choice]: Yes.
                        - (120,000 coins are taken from the player in exchange for the inverted Dungeoneering master cape.)
                      - [Choice]: No.
                        - (end)
              - (above|buy-master-cape)
  - [Choice]: cond=If the player has found all ten Marmaros and Thok Dungeoneering journals|I managed to find all your letters.
    - **Player:** I managed to find all your letters.
    - **Thok of Daemonheim:** Marm! Marm, wake up. Thok was wrong: someone managed to find our letters!
    - **Marmaros, rewards trader:** W... What - all of them? You... You know we made it to bottom of that place?
    - **Player:** You must have done. The letters go all the way down to the lowest floors.
    - **Marmaros, rewards trader:** I can't believe it! Do, you know what ha... happened to me? Why I have trouble thinking? Why I can't even sl... sleep for fear?
    - **Player:** Neither of you remember? Your letters aren't clear, but it was like someone pulled a plug and drained Marmaros of all hope and optimism. You became suicidal, and Thok had to stop you hurting yourself by breaking your arms.
    - **Thok of Daemonheim:** Not remember that at all, but it feel true. Thok and Marm can't remember what happened at bottom of the halls at all, Player. Memory a mess, like when Thok fell asleep in keg of stout.
    - **Player:** You wrote that somebody saved you and brought you back here: a man with a...white beard, I think you said. I guess he must have-
    - **Marmaros, rewards trader:** A white beard? No, it couldn't be...
    - **Thok of Daemonheim:** Haha, look! Marm must be getting better: he using his head again!
    - **Player:** What is it?
    - **Marmaros, rewards trader:** I... I can't be sure, but I might have an idea of who this man with a white beard is. There's someone I need to talk to...someone who has a lot of explaining to do.
    - **Thok of Daemonheim:** But for now, Thok have work to do, and mustn't exhaust Marm from excitement. You have thanks, Player. Thok will sing your name at tonight's eveningtide.
  - [Choice]: cond=If the player has completed Thok It To 'Em|I've been you.
    - **Player:** I've been you.
    - **Thok of Daemonheim:** What? You confuse Thok.
    - **Player:** Skaldrun showed me the story of how you battled your way through the dungeons to save Marmaros.
    - **Thok of Daemonheim:** Yes, was a great adventure.
    - [Menu]: Select an Option
      - [Choice]: cond=After claiming the Hard Daemonheim Task rewards from Talsar|Thanks for teaching me how to headbutt like you.
        - **Player:** Thanks for teaching me how to headbutt like you.
        - **Thok of Daemonheim:** You welcome. No try headbutt Thok though. Thok head thicker than yours.
      - [Choice]: cond=Before claiming the Hard Daemonheim Task rewards from Talsar|Can you teach me that ability? You know, the one where you obliterate the enemy with your forehead?
        - **Player:** Can you teach me that ability? You know, the one where you obliterate the enemy with your forehead?
        - **Thok of Daemonheim:** Ha ha ha. No, tiny person, only Thok has head thick and powerful enough for that.
      - [Choice]: It all seemed a little
        - **Player:** It all seemed a little . Did you really fight so many boss monsters?
        - **Thok of Daemonheim:** Thok fought many powerful monsters and Thok beat them all. Do not mock Thok.
        - **Player:** Erm, sorry.
      - [Choice]: Whatever happened to Mini Marm?
        - **Player:** Whatever happened to Mini Marm?
        - **Thok of Daemonheim:** Mini Marm is great and mighty crab warrior. He went back into dungeon to slay many monsters.
        - **Player:**  Will he be alright?
        - **Thok of Daemonheim:** Do not fear for Mini Marm, fear for the monsters that dare stand in his way!
  - [Choice]: About the Task System...
    - (Condition: If the player has completed the elite Daemonheim achievements and the rewards have not been claimed:)
      - **Player:** I've completed all of the Elite tasks in the Daemonheim set.
      - **Thok of Daemonheim:** Good, good.
      - [Thok hands you a few lamps]
      - **Thok of Daemonheim:** In Daemonheim you make second gatestone and teleport to it. Also in Daemonehim then bury bones of dead enemies - you get prayer. Also, let you through magical barrier in Brimhaven Dungeon - Thok try head-butting
      - **Thok of Daemonheim:** but now he share the secret.
      - **Player:** Thanks! What else does it do?
      - **Thok of Daemonheim:** For doing all tasks your ring of kinship made better! Also Thok persuade smuggler to take less monies for stuff. If you really think you as good as Thok, you try hard mode...but me not think your head hard enough for that.
      - (continue)
    - [Menu]: Choose an option:
      - [Choice]: Tell me about the Achievement System.
        - **Thok of Daemonheim:** Very well: the Achievement System is a collection of deeds you may wish to complete while adventuring around the world.
        - **Thok of Daemonheim:** You can earn special rewards for completing certain achievements; at the very least, each is worth a cash bounty from Explorer Jack in Lumbridge.
        - **Thok of Daemonheim:** Some also give items that will help complete other achievements, and many count as progress towards the set for the area they're in.
        - [Menu]: Choose an option:
          - [Choice]: Tell me about the set reward for this locality.
            - **Player:** Tell me about the set reward for this area.
            - **Thok of Daemonheim:** If Thok think you strong enough, you get aura.
            - **Thok of Daemonheim:** Aura will become better if you do more harder task sets.
            - **Thok of Daemonheim:** When you get aura, you learn about its powers.
            - You may also see what rewards a set item provides by hovering over the Rewards icon for its Exploration Achievement set in the Achievements interface.
            - (previous2|about-task-system)
          - [Choice]: How do I claim these rewards?
            - **Player:** How do I claim the rewards?
            - **Thok of Daemonheim:** To get reward, you complete all tasks in set, then you come get reward.
            - **Thok of Daemonheim:** Some of the tasks are simple, some need good skills, and some need quests. Thok did all tasks easy!
            - **Thok of Daemonheim:** For shiny rewards, talk to Drangund the Dungeoneering Tutor, Marmaros the Rewards trader, Talsar or Thok.
            - (previous2|about-task-system)
          - [Choice]: Sorry, I was just leaving.
            - (end)
      - [Choice]: Sorry, I was just leaving.
        - (end)
  - [Choice]: cond=If the player has 99 Dungeoneering|I've noticed there are a couple versions of each skillcape.
    - **Thok of Daemonheim:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
    - (Condition: If the player is using the old model:)
      - **Thok of Daemonheim:** It looks like you're currently using the old model for your Dungeoneering skillcape. Would you like to change to the newer one?
      - (continue)
    - (Condition: If the player is using the new model:)
      - **Thok of Daemonheim:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
      - (continue)
    - [Menu]: Select an Option
      - [Choice]: Yes, I would like to wear the [new/old] version of the skillcape.
        - **Thok of Daemonheim:** Would you like to wear the [old/newer] model for just this cape, or for the Quest Cape and all of the skillcapes you own?
        - [Menu]: Select an Option
          - [Choice]: I would just like to change the Dungeoneering skillcape.
            - **Thok of Daemonheim:** No problem, you will now use the [older/newer] model for your Dungeoneering skillcape.
          - [Choice]: I would like to change all my skillcapes.
            - **Thok of Daemonheim:** No problem, you will now use the [older/newer] model for all of your skillcapes!
          - [Choice]: I've changed my mind!
            - (end)
      - [Choice]: No, thank you.
        - **Thok of Daemonheim:** Great! I'm glad you're still enjoying the [old/new] version!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Thok of Daemonheim:** If you want, I can make it so you use the old model for all of the skillcapes you own.
          - [Menu]: Select an Option
            - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
              - **Thok of Daemonheim:** Great, you will now use the old model for all of your skillcapes!
            - [Choice]: No, thanks.
              - (end)

#### Using Thok on Wood on him

- **Thok of Daemonheim:** What you want with Thok?
- **Player:** I found this book of yours by rummaging in Balthazar's Raffle, it was at the bottom of a barrel!
- **Thok of Daemonheim:** Book did not sell as well as Thok want. Showing book off to people, I punch everyone who say book was stupid.
- **Thok of Daemonheim:** Then weaklings who chop tree with axe start to hate Thok too. They say I take all trees so they have nothing to cut. So I punch them too.
- **Thok of Daemonheim:** After Thok punch weaklings, green people who hug trees say Thok not think about trees feelings. They say Thok no care if a tree not want to become place where beer goes, I punch them as well.
- **Thok of Daemonheim:** Thok not stupid, Thok king of make stuff with trees!
- **Player:** How do you make furniture? I don't see a workbench around here and I'd be very surprised if the Housing Agency allowed you to own a house.
- **Thok of Daemonheim:** Thok pick up tree and smash tree over knee until Thok is happy.
- **Player:** I'm not sure how that works.
- **Thok of Daemonheim:** Thok think of what to make and smash on knee until it is made. It not hard, just need to find tree. Here Thok show-
- **Player:** No no no Thok, that isn't necessary. Thank you for whatever that conversation was.
- **Thok of Daemonheim:** Thok happy to see book again, Thok no punch you this time.

#### After the 2010 Christmas event

- (see|O Little Town of Daemonheim#Talking to Thok, Master of Dungeoneering)

#### Player has Ferret of Doom as a follower pet

- **Thok of Daemonheim:** Thok not talk to you with that around.
- **Player:** With what around?
- **Thok of Daemonheim:** ...
- **Thok of Daemonheim:** DOOM!
- [Thok barely brings himself to look at your pet ferret.]
- **Player:** I understand. I'll come back once I have a different companion.

### In Burthorpe Castle during Song of Seren

- **Thok:** Player! Thok is pleased to see you! But Thok is busy, busy watching all these villains.
- **Thok:** One of them is bound to do something EVIL and when they do, Thok will teach them a lesson.
- **Thok:** With his FIST!

### At War's Retreat (Thok's Smashing Buffs)

- {{Main|Transcript:Thok's Smashing Buffs}}
