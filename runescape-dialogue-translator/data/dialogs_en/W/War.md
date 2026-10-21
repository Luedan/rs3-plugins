# War

- **Original Wiki Page**: [Transcript:War](https://runescape.wiki/w/Transcript%3AWar)
- **Letter**: `W`

---

## Dialogue Transcript


### Outside of War's Retreat


#### With a combat level below 60

- **War:** Sorry, Player I can't let you join me in combat here until you are stronger, I wouldn't want you to get seriously hurt. Combat level 60 should be enough!
- **War:** Make sure you return when you are strong enough and I'll help you become a MIGHTY WARRIOR!

#### With a combat level below 60, but at least 1,000 skill total

- **War:** Sorry, Player I can't let you join me in combat here until you are stronger, I wouldn't want you to get seriously hurt. Combat level 60 should be enough!
- **War:** Hmm... On second thought, you do look very skilled. Maybe I could make an exception?
- **War:** Yes, I'll let you in. I will take no responsibility should you get hurt, however.
- [Menu]: Do you want to enter War's Retreat without at least combat level 60?
  - [Choice]: Yes. Let me in.
    - {{Qact|Screen fades out and in as the player enters War's Retreat.}}
  - [Choice]: No. I'll get stronger first.
    - (end)

### In War's Retreat


#### Initial Dialogue

- **War:** Welcome Player! I'm glad to see your thirst for battle has led you to me.
- **Player:** Who are you?
- **War:** I am War, retired horseman, battle-hardened warrior, blood sport enthusiast and owner of this delightful retreat.
- **Player:** Yes, I can feel the relaxation washing over me.
- **War:** I'm glad you feel it too, Player, I can see you will fit in here!
- **Player:** Other than this lovely atmosphere we both definitely agree you've created, what is this place for?
- **War:** WARRIORS!
- **War:** Nurturing the combat talent of the future is my new hobby.
- **War:** And you are my next project.
- **Player:** What do you mean? What do you want from me?
- **War:** I want you to fight and grow as a warrior. Earn my favour by defeating the strongest creatures in Gielinor.
- **War:** As my new project I shall need a name for you. How about Project?
- **Player:** Well, I suppose it's a functional name if nothing else.
- **Player:** What do I get out of this?
- **War:** My retreat has various facilities to help the eager warrior.
- **War:** If you defeat enough foes to earn it, I can offer you a teleport to return you to this retreat whenever you like.
- {{Qact|Camera pans to the portals.}}
- **War:** My portals can be directed to take you to any bosses you can battle, if you've defeated them once before and can pay the price.
- {{Qact|Camera pans to the reaper portal.}}
- **War:** If you are helping out Old Boney with his reaping, the reaper portal will take you to the target he has assigned you.
- **Player:** Do you mean Death?
- **War:** That's right, Old Boney!
- {{Qact|Camera pans to Fateful Portal.}}
- **War:** The final portal will activate if there is a new foe to battle or an event to participate in.
- {{Qact|Camera returns to the player.}}
- **War:** I can also grant you access to a campfire and altar to reinvigorate you after a battle and adrenaline crystals to rouse you for your next one!
- **War:** Finally, whenever you fight powerful creatures, I will give you marks to spend. They can be used to buy combat auras and aura and life refreshes.
- **Player:** That all sounds good, if a little dangerous. I'll think it over.
- **War:** Don't think Project.
- **War:** FIGHT!
- (continue|NormalDialogue)

#### Normal dialogue

- **War:** Welcome back to my retreat, Project!
- [Menu]: Choose an option:
  - [Choice]: Can you tell me about yourself?
    - **Player:** Can you tell me about yourself?
    - **War:** I am War. I was one of the four riders of the apocalypse, before I retired.
    - **Player:** Why did you retire?
    - **War:** I got old! There's only so long you can keep up the pace I rode at.
    - **Player:** So what do you do now?
    - **War:** Other than a battle Old Boney roped me into, I've been thirsting for combat.
    - **War:** But that's why I've started this retreat! Everyone needs a hobby.
    - (previous|NormalDialogue)
  - [Choice]: I would like to talk about Combat Mastery.
    - [Menu]: Choose an option:|anchor=Combat-Mastery
      - [Choice]: What can you tell me about Combat Mastery?
        - **War:** Welcome back to my Retreat, Project! I have new tasks for you.
        - **War:** I have watched your progress with much interest, Project. I want to take your glory to the next level!
        - **Player:** What did you have in mind?
        - **War:** I have devised a new set of tasks for you which will further test your mettle. For GLORIOUS BATTLE!
        - **War:** The more tasks you complete, the more rewards I will grant you.
        - (previous|Combat-Mastery)
      - [Choice]: Show me the Combat Mastery tasks I can do.
        - ((Combat achievements interface opens to the first available Combat Master achievement group))
      - [Choice]: cond=If the player has unlocked War's Blessing 4 and has not claimed the rewards:|Do you have any rewards for me?
        - **War:** Well done Player, I've kept some rewards aside for you.
        - (Condition: If the player does not have at least two free backpack spaces:)
          - **War:** But unfortunately you don't have space for them.
          - (previous|Combat-Mastery)
        - (Condition: If the player has at least two free backpack spaces:)
          - (receives=War's Ancient Weapon Gizmo Shell (Costless) and War's Ancient Armour Gizmo Shell (Costless))
          - (previous|Combat-Mastery)
      - [Choice]: Goodbye.
        - **Player:** Goodbye!
        - **War:** Fight on Project, fight on!
  - [Choice]: What do you want me to do?
    - **Player:** What do you want me to do?
    - **War:** BATTLE!
    - **Player:** Do battle?
    - **War:** GLORIOUS BATTLE!
    - **Player:** Could you be a bit more specific?
    - (Condition: If the player has no boss kills:)
      - **War:** I can see you are quite new to this, so I will point out a few good places to start, Project.
      - **War:** The Barrows Brothers of Morytania are long dead and buried, but that doesn't mean they can't put up a fight.
      - **War:** The gardeners in Falador Park have been having trouble with a Giant Mole, it would make a good first hunt for a fledging warrior.
      - **War:** If you venture north of Burthorpe into troll lands, you can find the site of an ancient battle of the gods. The generals of this so-called God Wars Dungeon should be fun to spar with.
      - (continue)
    - (Condition: If the player already has boss kills:)
      - **War:** Defeat powerful creatures! Earn my favour! Be rewarded!
      - (continue)
    - **War:** Fight bosses and I will give you marks, return them to me for rewards.
    - **War:** The more bosses you kill the more access I will grant you to my facilities.
    - (previous|NormalDialogue)
  - [Choice]: Can you explain the rewards to me?
    - **Player:** Can you explain the rewards to me?
    - **War:** Which rewards are you interested in knowing more about?
    - [Menu]: Select an Option
      - [Choice]: What are marks of war?
        - **Player:** What are marks of war?
        - **War:** When you defeat worthy foes, I will give you marks to spend. I want combat to become habitual to you, so I will award you up to 1,000 marks an hour. The more impressive the foe, the more marks I will award you.
        - **War:** These marks can be used to buy combat auras and aura and life refreshes.
        - **War:** You can also use them with logs to upgrade the campfire, so you can warm your heart and sing songs of your battle prowess!
        - (previous|RewardExplanations)
      - [Choice]: Can you tell me about the transport options here?
        - **Player:** Can you tell me about the transport options here?
        - **War:** If you defeat 10 foes, I can offer you a teleport to return you to this retreat whenever you like.
        - {{Qact|Camera pans to the portals.}}
        - **War:** My portals can be directed to take you to any bosses you can battle, if you've defeated them once before and can pay the price of 100,000 coins.
        - **War:** The first portal, and first redirection is free. I will let you use the second portal when you've defeated 100 impressive foes.
        - **War:** If you've killed a specific boss at least 100 times, you can redirect a portal to it for 50,000 coins.
        - {{Qact|Camera pans to the reaper portal.}}
        - **War:** If you are helping out Old Boney with his reaping, the reaper portal will take you to the target he has assigned you.
        - {{Qact|Camera pans to Fateful Portal.}}
        - **War:** The final portal will activate if there is a new foe to battle or an event to participate in.
        - {{Qact|Camera returns to the player.}}
      - (previous|RewardExplanations)
      - [Choice]: Can you tell me about the altar and adrenaline crystals?
        - **Player:** Can you tell me about the altar and adrenaline crystals?
        - {{Qact|Camera pans to the altar of War.}}
        - **War:** I can grant you access to my altar to reinvigorate your prayer and summoning after battle...
        - {{Qact|Camera pans to the adrenaline crystals.}}
        - **War:** ...and crystals to rouse you for your next one by refilling your adrenaline!
        - {{Qact|Camera returns to the player.}}
        - **War:** Both of these can be gained by killing 200 and 1,000 powerful creatures, respectively.
        - (previous|RewardExplanations)
      - [Choice]: Can you tell me about the campfire?
        - **Player:** Can you tell me about the campfire?
        - {{Qact|Camera pans to the campfire.}}
        - **War:** The campfire can be used to warm your heart and boost your lifepoints before an {{Sic|upcomping}} battle.
        - **War:** You can also use 1,000 marks of war with 1,000 logs to upgrade the campfire to improve its effects.
        - {{Qact|Camera returns to the player.}}
        - (previous|RewardExplanations)
      - [Choice]: Can we talk about something else?
        - **Player:** Can we talk about something else?
        - **War:** Of course, Project!
        - (previous2|NormalDialogue)
  - [Choice]: [More...]
    - [Menu]: Choose an option:
      - [Choice]: I would like to purchase some rewards.
        - **Player:** I would like to purchase some rewards.
        - **War:** Very well, Project.
        - (opens=War's Wares)
      - [Choice]: cond=If warnings have been turned off for reattuning a portal|Can you warn me when I'm trying to reattune a portal?
        - **Player:** Can you warn me when I'm trying to reattune a portal?
        - **War:** MY WARNING SHOUT WILL BE SO LOUD YOUR ANCESTORS WILL HEAR IT!
        - **Player:** A simple yes would have sufficed.
        - (initial|NormalDialogue)
      - [Choice]: Goodbye!
        - **Player:** Goodbye!
        - **War:** Fight on Project, fight on!
      - [Choice]: [More...]
        - (initial|NormalDialogue)

#### Attuning the eastern boss portal without having unlocked it


##### Before having killed enough bosses to unlock the feature

- You must have killed 100 boss monsters to use this.
- **War:** You can't use that yet Project, you haven't killed enough worthy foes yet!

##### Having killed enough bosses to unlock the feature

- **War:** Project, you have littered the world with the corpses of your fallen foes.
- **War:** IT IS BEAUTIFUL!
- **War:** Feel free to use this portal.
- You can now attune the eastern portal.

#### Praying at the Altar of War without having unlocked it


##### Before having killed enough bosses to unlock the feature

- You must have killed 200 boss monsters to use this.
- **War:** You can't use that yet Project, you haven't killed enough worthy foes!

##### Having killed enough bosses to unlock the feature

- **War:** Project, you have littered the world with the corpses of your fallen foes.
- **War:** IT IS BEAUTIFUL!
- **War:** Feel free to use my altar.
- You can now use the altar of War to restore prayer and summoning points.

#### Using War's Grimoire without having unlocked it


##### Before having killed enough bosses to unlock the feature

- You must have killed 750 boss monsters to use this.
- **War:** You can't use that yet Project, you haven't killed enough worthy foes!

##### Having killed enough bosses to unlock the feature

- **War:** Project, you have littered the world with the corpses of your fallen foes.
- **War:** IT IS BEAUTIFUL!
- **War:** Feel free to use my grimoire.
- Congratulations! You have completed: 'A Change of Pace' - Unlock the ability to change your spellbook using War's Grimoire at War's Retreat.
- You can now change your spellbook from War's Grimoire.

#### Channelling an adrenaline crystal without having unlocked it


##### Before having killed enough bosses to unlock the feature

- You must have killed 1,000 boss monsters to use this.
- **War:** You can't use that yet Project, you haven't killed enough worthy foes!

##### Having killed enough bosses to unlock the feature

- **War:** Project, you have littered the world with the corpses of your fallen foes.
- **War:** IT IS BEAUTIFUL!
- **War:** Feel free to channel adrenaline from the crystals.
- colour=lightgreen

#### Channelling an adrenaline crystal with 2,000 boss kills without adrenaline potion refresh unlocked

- **War:** Project, you have littered the world with the corpses of your fallen foes.
- **War:** IT IS BEAUTIFUL!
- **War:** Feel free to channel adrenaline from the crystals.
- Congratulations! You have completed: 'Second Wind' - Unlock the ability to refresh the cooldown of adrenaline potions using the adrenaline crystals at War's Retreat.
- You can now reset adrenaline potion cooldowns from the crystals in the garden.

#### Check cooldown


##### If no Marks of War have been earned recently

- **War:** Project, stop standing around here and go out and battle some bosses to start earning marks!

##### If less than 1,000 Marks of War have been earned in the last hour

- **War:** There is still more blood to be shed, Project. You've earned X out of 1000 marks during this call to battle.

##### If 1,000 Marks of War have been earned in the last hour

- **War:** Well fought, Project! You have earned the maximum amount of marks during this call to battle, you can earn more in X minutes.

#### Resurrecting the player after if they die within War's Retreat

- **War:** You're not dying on my watch! Remember to get more food if you need it.

### Historical dialogue


#### Normal dialogue before 17 February 2025

- **War:** Welcome back to my retreat, Project!
- [Menu]: Choose an option:
  - [Choice]: Can you tell me about yourself?
    - (above)
  - [Choice]: What do you want me to do?
    - (above)
  - [Choice]: Can you explain the rewards to me?
    - (above)
  - [Choice]: I would like to purchase some rewards.
    - (above)
  - [Choice]: [More...]
    - [Menu]: Choose an option:
      - [Choice]: cond=If warnings have been turned off for reattuning a portal|Can you warn me when I'm trying to reattune a portal?
        - (above)
      - [Choice]: Can you decant some potions or jellyfish for me?
        - (below|Decanting dialogue before 17 February 2025)
      - [Choice]: Can you sell me some Challenge Gems?
        - **Player:** Can you sell me some Challenge Gems?
        - **War:** Of course, Project! How many do you want?
        - [Menu]: How many would you like to buy?
          - [Choice]: One.
            - ((Purchase interface opens up for Challenge Gem (x1) for 10 RuneCoins))
          - [Choice]: Three.
            - ((Purchase interface opens up for Challenge Gem (x3) for 25 RuneCoins))
          - [Choice]: Six.
            - ((Purchase interface opens up for Challenge Gem (x6) for 40 RuneCoins))
          - [Choice]: None, I changed my mind.
            - **Player:** None, I have changed my mind.
            - **War:** Never fear, you know where to find them now Project. Anything else?
            - (initial|NormalDialogue)

#### Decanting dialogue before 17 February 2025

- [Menu]: Select an Option
  - [Choice]: Decant vials
    - [Menu]: How many doses do you want to decant into?
      - [Choice]: One dose
        - (Condition: If the player has no viable vials of potions to decant:)
          - **War:** You haven't got anything to decant!
        - (Condition: If the player has no backpack space:)
          - Searching...
          - **War:** Your inventory's a bit too full for me to do anything for you.
        - (Condition: If the player has viable vials of potions to decant:)
          - Searching...
          - (Condition: If additional vials were purchased from War:)
            - (receives=vials) (removes=two coins for each vial)
            - (continue)
          - **War:** There you go, chum.
      - [Choice]: Two doses
        - (above|decant-vials)
      - [Choice]: Three doses
        - (above|decant-vials)
      - [Choice]: Four doses
        - (above|decant-vials)
  - [Choice]: Decant flasks
    - (Condition: If the player has flasks to decant:)
      - **War:** Let's see what you have. I will decant your potion flasks back into 6 dosed flasks. I can make use of the flasks, so I'll take those as payment.
      - {{Qact|War decants as many as he can to full 6-dose flasks}}
      - **War:** Here you go. That's the best I can do! If the flasks don't look too different, I gave them a clean{{Sic}}
    - (Condition: If the player has no viable flasks of potions to decant:)
      - **War:** Sorry, you don't seem to have anything I can use. Make sure you have 2 flasks that aren't completely full!
  - [Choice]: Convert vials to flasks
    - (Condition: If the player has empty flasks in backpack:)
      - **War:** Lets see what you have. I will decant potion vials and all flasks with up to 4 doses into 6 dose flasks. You'll need to supply the empty flasks yourself; they're not cheap.
      - {{Qact|War decants as many potions as he can to full 6-dose flasks}}
      - **War:** Here you go. That's the best I can do!
    - (Condition: If the player has no empty flasks in backpack:)
      - **War:** You'll need to supply the empty flasks yourself; they're not cheap. You can bring them to me noted or unnoted.
  - [Choice]: Convert flasks to vials
    - (Condition: If the player has flasks of potions to decant to vials:)
      - **War:** Certainly. I think I can make use of the flasks, so I'll give you the vials for free.
      - {{Qact|War decants as many potions as he can to noted vials}}
      - **War:** There you go, that's the best I can do!
    - (Condition: If the player has no viable flasks of potions to decant:)
      - **War:** Sorry, you don't seem to have anything I can use. Make sure you have at least 1 flask!
  - [Choice]: Combine jellyfish
    - (Condition: If the player has viable jellyfish to combine:)
      - {{Qact|Jellyfish are combined where possible}}
      - **War:** There you go.
    - (Condition: If the player has no viable jellyfish to combine:)
      - **War:** Sorry, I don't know how to combine anything that you're carrying.
  - [Choice]: Cancel
    - (end)
