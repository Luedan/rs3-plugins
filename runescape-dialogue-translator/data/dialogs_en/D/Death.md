# Death

- **Original Wiki Page**: [Transcript:Death](https://runescape.wiki/w/Transcript%3ADeath)
- **Letter**: `D`

---

## Dialogue Transcript


### Upon death


#### At first death

- **Death:** Greetings.
- [Menu]: Select an Option
  - [Choice]: Pleased to meet you.
    - **Death:** I'm glad to see you taking this so well. Most of the recently deceased are more upset.
    - (continue|not-your-time1)
  - [Choice]: Am I... dead?
    - **Death:** Yes, I'm afraid that you are.
    - (continue|not-your-time1)
  - [Choice]: AHHHHHHHHHHHH!
    - **Death:** Calm down, calm down. You're just dead.
    - (continue|not-your-time1)
- **Death:{{anchor|not-your-time1}}** Fortunately for you, it is not yet your time.
- [Menu]: Select an Option
  - [Choice]: Great! How do I get back?
    - **Death:** It is not your time. Destiny awaits you. I will not claim you. Yet.
    - **Player:** Right... thanks.
    - (continue|use-the-portal)
  - [Choice]: Wait...I'm not dead?
    - (continue|use-the-portal)
- **Death:{{anchor|use-the-portal}}** You can go back now. When you leave here, you'll return to the town.
- **Death:** When you die you keep some of your items, but you lose others.
- **Player:** I lose my stuff?
- **Death:** Your valuable gear will be dropped wherever it is you died. However, you can choose three of those items to keep.
- You can see which items will drop and which will be kept in the deathkeep interface in your Worn Inventory.
- **Death:** When you return to the world of living, you have a short time limit to return to the site of your death and reclaim your dropped gear.
- Whenever you die with items that could drop, you'll see an interface allowing you to choose which ones to keep.
- You can selectively take your items one at a time, take them all with the 'take all' button, or re-equip your gear and take the rest of your items with the 'Equip all' button.
- **Death:** Take the portal behind you and return to the world of the living.
- [Menu]: Select an Option
  - [Choice]: Goodbye!
    - (end)
  - [Choice]: I just want to ask you about-
    - **Death:** Go!

#### At first death without losing any items

- **Death:** Greetings.
- Select an option
  - Pleased to meet you.
    - **Death:** I'm glad to see you taking this so well. Most of the recently deceased are more upset.
    - (continue|not-your-time)
  - Am I... dead?
    - **Death:** Yes, I'm afraid that you are.
    - (continue|not-your-time)
  - AHHHHHHHHHHHH!
    - **Death:** Calm down, calm down. You're just dead.
    - (continue|not-your-time)
- **Death:{{anchor|not-your-time}}** Fortunately for you, it is not yet your time.
- Select an option
  - Great! How do I get back?
    - **Death:** It is not your time. Destiny awaits you. Death will not claim you. Yet.
    - **Player:** Right... thanks.
    - (continue|use-the-hourglass)
  - Wait...I'm not dead?
    - **Death:** You can go back now. When you leave here, you'll return to the town.
    - (continue|use-the-hourglass)
- **Death:{{anchor|use-the-hourglass}}** Use the hourglass behind you and return to the world of the living.
- Select an option
  - Goodbye!
    - (end)
  - I just want to ask you about-
    - **Death:** Go!

##### Attempting to leave through the hourglass

- **Death:** Come over here.

##### Attempting to leave through the doorway to War's Retreat

- {{anchor|gracefully}} **Death:** I can't let you use that door whilst I'm teaching you how to die gracefully.

#### Second or more death, but losing items for the first time

- **Death:** Hello again..
- Select an option
  - Hello again.
    - **Death:** I have more to tell you.
    - (continue|not-your-time2)
  - Am I dead for real this time?
    - **Death:** No, but I have more to tell you.
    - (continue|not-your-time2)
  - AHHHHHHHHHHHH!
    - **Death:** It's alright, I just have more to tell you.
    - (continue|not-your-time2)
- **Death:{{anchor|not-your-time2}}** I'll now show you what you could reclaim from me. You may return at any time to reclaim these items.
- (Death Cost Overview interface opens.)
- (Condition: After the player has reclaimed their items, or closed the interface without reclaming:)
  - **Death:** Use the hourglass behind you and return to the world of the living.
  - Select an option
    - Goodbye!
      - (end)
    - I just want to ask you about-
      - **Death:** Go!

##### Attempting to leave through the doorway to War's Retreat

- (above|gracefully)

#### After subsequent deaths

  - **Death:** I thought you would return, Player. Do you wish to reclaim your items?
  - Reclaim your items?
    - Yes.
      - (Condition: With non-event free item reclaim:)
        - (receives=lost items)
        - Death has returned your items for free.<br>Death may not be so charitable next time, so enter dangerous situations at your own risk.
      - (Condition: With Item Protection Contract in backpack:)
        - **Death:** I notice you have {{Sic|a}} Item Protection Contract in your possession. I shall gladly return your items to you for free in exchange for that item, if you desire?
        - USE YOUR ITEM PROTECTION CONTRACT?
          - Yes please.
            - (removes=Item Protection Contract) (receives=lost items)
            - You use your Item Protection Contract and retrieve your items for free.
            - Death has returned your items for free.<br>Death may not be so charitable next time, so enter dangerous situations at your own risk.
          - Not this time thank you.
            - (continue)
      - ((Reclaim Items interface opens.))
    - Ask about something else.
      - ((Continues with Soul Reaper dialogue.))

### Soul Reaper tasks


#### If below 60 combat and group assignments are disabled

- **Death:** It is not your time yet, Player. What do you require from me?
- '''Select an option
  - Is there anything I can help out with?
    - **Death:** You may be of use to me, in time. Return to me when you are more experienced in dealing death.
  - I'd like to change my loot beam settings.
    - *(Opens Death's Store and the Slayer settings interface)*

#### First task

- **Death:** Welcome, Player.
- **Player:** Am I dead? What's going on here?
- **Death:** You are not dead... yet. I have allowed you to enter as I need your help with a task.
- **Death:** As you are no doubt aware, I am Death. The Reaper, the Collector of Souls, or any other name civilisations have given me. My task is to retrieve the soul from a dying creature, enabling its passage to the underworld.
- **Player:** So what do you need me for?
- **Death:** There is an imbalance in the harmony of life and death. <br>There is far too much... life.
- **Death:** My eyes have been on you in this age, Player, as have the eyes of many others. You appear to have the skills I require to bring balance.
- **Player:** So you want me to kill stuff?
- **Death:** If you wish to put it so indelicately, yes.
- **Player:** Great! When do I start?
- **Death:** Immediately. First, you must take this gem. It will allow you to contact me remotely, should you require aid or a new assignment.
- [You receive a grim gem.]
- **Death:** Before you receive your first assignment, are you happy to take on creatures as a group, or do you prefer to kill alone? You may change your mind later on, if you wish.
- '''Allow group bosses to be assigned?
  - Yes, I'm happy to receive group bosses.
    - (continue)
  - No, I don't want to have to team up with other adventurers.
    - (continue)
- **Death:** And one final thing. Are you happy to take on non-combat, skilling creatures, or do you prefer to use combat only? You may change your mind later on, if you wish.
- '''Allow skilling bosses to be assigned?
  - Yes, I'm happy to receive skilling bosses.
    - (continue)
  - No, I don't want to have to encounter skilling bosses.
    - (continue)
- If you wish to change your mind about being assigned group bosses, or skilling bosses, you can do so under the 'Options' tab in Death's store. You can only do this in between assignments.
- **Death:** Now for your first assignment. I hope you are ready.
- **Death:** I require you to collect <number> souls from the following battle: [Boss name]. Can I trust you with this task?
- You have a new reaper assignment: <number> x [Boss name].
- '''Select an option
  - You certainly can. Thanks!
    - (end)
  - I'd like a different assignment.{{anchor|different-assignment}}
    - *At first reroll attempt:*
      - **Death:** I will be patient with you once, with no penalty. Do you wish me to assign you a new creature?
        - Yes, remove my current assignment and give me a new one.
          - **Death:** I require you to collect X souls from the following battle: [Boss name]. Can I trust you with this task?
            - You certainly can. Thanks!
              - (end)
            - I'd like a different assignment.
              - (above|different-assignment)
            - I need some hints about my assignment.
              - *(Same as below)*
        - No, I've changed my mind. Leave my assignment.
    - *At second reroll attempt:*
      - **Death:** Do not think I will allow you to change your mind freely. If you request a different assignment today, you will only receive 75% of the reaper points for completion. You will gain the full experience, however.
        - *(Same as above)*
    - *At third reroll attempt:*
      - **Death:** Do not think I will allow you to change your mind freely. If you request a different assignment today, you will only receive 50% of the reaper points for completion. You will gain the full experience, however.
        - *(Same as above)*
    - *At fourth reroll attempt:*
      - **Death:** Do not think I will allow you to change your mind freely. If you request a different assignment today, you will only receive 25% of the reaper points for completion. You will gain the full experience, however.
        - *(Same as above)*
    - *At fifth reroll attempt:*
      - **Death:** I find your indecision tiresome. If you request a different assignment again today you will not receive any reaper points for completion. I cannot stop you from receiving the full experience...unfortunately.
        - *(Same as above)*
    - *At sixth reroll attempt:*
      - **Death:** My patience only stretches so far. You have wasted enough of my time, I must address this imbalance myself. Be gone, mortal.
  - I need some hints about my assignment.
    - [Task hint]

#### Subsequent task

- *If you have yet to complete the currently assigned task*
  - **Death:** You are taking a long time to complete my assignment, Player. Are you finding it too difficult?
  - If you choose to reset your assignment this will be treated as a brand new task, with fresh rerolls. There is no guarantee the new assignment will be different to your current one. If you wish to reroll your current task instead, use your grim gem.
    - I'd like a new assignment.
      - *(Same as above)*
    - I'd like another grim gem.
      - You receive a grim gem.
        - I'd like a different assignment.
          - *(Same as above)*
        - Are there any rewards for this?
          - *(Same as below)*
        - I need some hints about my assignment.
          - *(Same as above)*
        - Am I dead? What do you want from me?
          - *(Same as below)*
    - Are there any rewards for this?
      - *(Death's Store interface opens)*
    - I need some hints about my assignment.
      - *(Same as above)*
    - Am I dead? What do you want from me?
      - *(Same as above)*
- *If you have completed a task today*
  - **Death:** The imbalance has been corrected for today; your task is done. Visit me tomorrow for further instructions.

### Overcharging the ring of death

- **Death:** I can help you but it will come at a cost.
- **Death:** To overcharge your ring I will need 25 Black stone hearts and 5 cut onyxes.
*If the ring of death is not in the inventory*
- **Death:** You don't have a ring for me to overcharge.

### Activating the grim gem

- **Death:** What is it mortal? Time is ticking.
  - **Player:** How am I doing so far?
    - **Death:** I have requested that you collect souls from the following: [Boss name]. I require X more before your task is complete.
      - *(Shows other options)*
  - **Player:** Can you give me any hints?
    - [Task hint]
  - **Player:** What do you want from me?
    - **Death:** As you are no doubt aware, I am Death. The Reaper, the Collector of Souls, or any other name civilisations have given me. My task is to retrieve the soul from a dying creature, enabling its passage to the underworld.
    - **Player:** So what do you need me for?
    - **Death:** There is an imbalance in the harmony of life and death. There is far too much... life. My eyes have been on you in this age, Player, as have the eyes of many others. You appear to have the skills I require to bring balance.
    - **Player:** So you want me to kill stuff?
    - **Death:** If you wish to put it so indelicately, yes.
    - **Player:** Great! When do I start?
    - **Death:** Immediately. I have already tasked you to collect souls from the following battle: [Boss name]. You have yet to bring me X souls.
  - **Player:** Where are you?
    - **Death:** You may find me in my office, a portal to which may be accessed south of Draynor Manor.
      - *(Shows other options)*
  - **Player:** Nothing, thanks.

### 2015 Halloween event

*After Missing, Presumed Death*
- **Death:** Ah, my saviour graces me with his/her presence once more.
*Before Missing, Presumed Death*
- **Death:**  Greetings, mortal. A matter of great urgency requires your attention.
- **Player:**  What's going on?
- **Death:**  Beyond this rift Icthlarin and Amascut do battle over the River Noumenon, in front of the gates to the Underworld. The are vying for control of the only crossing between the lands of the living and the dead. If Amascut succeeeds, it may be the end of the afterlife as we know it. Her power will grow exponentially. Icthlarin is in need of your help Player. Step into the rift. Aid him in his fight against The Devourer.
- **Player:**
  - **Who are Icthlarin and Amascut?**
    - **Death:**  Icthlarin is the god of the Underworld, and not only that, he is my friend. For millennia he has carried the burden of protecting souls on their journey to the afterlife. Amascut is his sister. She once stood beside her brother, offering the greatest of souls a chance of reincarnation. But she has since descended into madness. Devouring those very souls is now what drives her. She who Icthlarin must protect these helpless souls from. He is the light that guards them from her devourer beasts.
    - **Player:** Will you be coming down to help as well?
    - **Death:** I must stay here to guard the rift, Player. I fear our old friend Nomad will try to enter and gain the power of the souls for himself. He is plotting something sinister. I am sure of it.
  - **What caused this battle to start?**
    - **Death:**  When the world-eater, Tuska, crashed into this planet she was not killed completely. Strangely, her anima remains locked in her lifeless body, gradually leaking out into Gielinor. Further investigation of the husk revealed that there are also  souls leaking out. Souls that are not of this world. As the beast consumed other worlds, she also consumed their Underworlds and the souls within them. These souls remained within her, until now. They are leaking out and overflowing Gielinor's underworld.
    - **Player:**  Why has that caused a battle between Icthlarin and Amascut?
    - **Death:**  Amascut has seized her opportunity to attack whilst the Underworld is in disarray. There is an abundance of souls for her to devour. Icthlarin is spread thin… he cannot protect them all. Amascut draws power from the souls she devours, Player. If she is not stopped, there is no telling how strong she will become.
  - **How can I help?**
    - **Death:** Pass through the rift, mortal. Be warned: you may experience some nausea, but this is perfectly normal for a human. It will soon pass. Once on the other side you will find yourself at the edge of the Realm of the Living, on the bank of the River Noumenon. Look for the various inhabitants of this area. They are an... odd bunch, but they will instruct you well. I believe Icthlarin has assigned Ka -  a talking cat - to the rift. She will be able to help you upon your arrival.
  - **What will I get in return?**
    - **Death:**  It is a shame you adventurers must always be so focused on self gain, but it will please you to know you will be well compensated. Whilst rounding up souls in the River Noumenon you will notice there are some that stand out from the rest. These are the souls which may once have stood a chance of reincarnation. Collecting them will reward you with experience in the skill they specialised in during their lives.. Today I have noticed these souls are *the five special souls of the day*. You will also gain Noumenon Favour for your contribution towards Icthlarin's efforts, which can be redeemed for rewards at Sinn Derkwill on the other side of the rift.
  - **Goodbye.**

### 2018 Halloween event

*Before completing the tutorial*
- **Death:** [Player], come over here and talk to me before you go any further.
*Leading up to the Tutorial.*
- **Death:** Do you feel that? That force coming from the rift... An energy that feels ancient. Even to me.
- **Player:** What is it?
- **Death:** I... I have no idea. But whatever it is, I feel compelled to stop it. Would you be willing to aid me?
  - *If yes is selected* **Player:** What would you have me do?
  - *If no is selected* **Death:** A pity. Gielinor may be at stake here; if you reconsider I would gladly accept your help.
- **Death:** This energy is tearing itself forth from deep beneath Gielinor's surface. We need to disrupt the rift to ensure that whatever is behind it cannot escape.
- **Player:** What does Moia have to do with the rift?
- **Death:** I do not know, but I fear she may be being used as a conduit - her unique nature of half mahjarrat and half human may make her malleable to this energy. It manipulates her power to draw itself closer.
- **Player:** So you are here to claim Moia? Would that not close the rift?
- **Death:** It may, but tell me, is that really the solution you believe we should proceed with?
  - *If yes is selected*
    - **Death:** Interesting. I expected a more heroic response from you, [player]. Do you feel the need to talk to someone about it?
    - **Player:** Actually, that would be quite nice. It turns out adventuring isn't just making cakes and saving missing cats. Recently I've been having this dream-
    - **Death:** I wasn't suggesting me.
    - **Player:** Oh.
  - *If no is selected*
    - **Player:** I didn't actually mean we kill her. I was just suggesting it as an idea. What's that saying? 'No idea is a bad idea'
    - **Death:** That was a bad idea.
  - **Death:** Anyway, it is not yet Moia's time. There is more to her story yet.
  - **Player:** What would you suggest we do instead?
  - **Death:** The rift is an opening that leads to the source of this power. I have created some pillars that can be used to disrupt the rift. If you could use your skills to ensure they remain powered, then it will allow us entry into the rift for a short period of time. Once you enter the rift, search within and find a way to break the source.
  - **Player:** That sounds an easy enough job for the World Guardian.
  - **Death:** It isn't that simple - there are monsters escaping. They will try to stop you stabilising the rift, so you will need to deal with them as well. However, I fear even this won't be enough. I never wanted to do this, but I fear I need to call for assistance from my... co-workers is probably the most human word for describing them.
  - **Player:** You mean the other Guardians of Guthix?
  - **Death:** Ah, if only it was that simple. No, but you will understand in time. I'll show you everything you need to know in order to help me stabilise the energy coming from the rift.
*During the tutorial*
- **Death:** I'm pleased you agreed to help, [player]. I'll bring you up to speed on my plan to stabilise this rift so we can get back to our day to day activities. I've built 5 pillars around the rift to help stabilise the energy coming from within. Each of the pillars will randomly be assigned a skill. You'll be able to train: Prayer, Runecrafting, Divination, Magic, Crafting, Summoning, Smithing, and Invention. Dealing with the hindrances will reward you with Slayer experience. Should you not wish to gain combat experience, you can talk to me to toggle experience gain off or on for all combat skills.
- **Death:** Stabilising at a pillar will increase XP multipliers at the other pillars, encouraging you to move between them for optimal experience gain. There are five multiplier stages, these are highlighted by different amounts of energy growing in intensity the higher it climbs. As you work on the pillar you'll slowly progress towards stabilising the rift. Your progress can be seen via the energy being directed from the pillars toward the centre. The more you stabilise, the more the beam will grow in intensity. Once it reaches the rift you've fully stabilised it.
- **Death:** Using a tainted shard will allow you to choose between doubling the experience gained OR halving the time it takes for you to stabilise a rift. And those are the basics. It's time we got to work [player].

### City of Um


#### Before having completed Rune Mythos or after having completed Vessel of the Harbinger

- **Player:** I've been meaning to ask, but where are we?
- **Death:** Um.
- **Player:** Do you not know? Because it sounded like you did.
- **Death:** I do know. This is Um.
- **Player:** Have you forgotten?
- **Death:** No. This is Um. The name of this city is Um.
- **Player:** ...
- **Player:** Because it's fine if you have forgotten.
- **Death:** I haven't forgotten!
- **Death:** Hear my words: Um is the name of this city. This is the City of Um!
- **Death:** Big 'U', little 'm': Um.
- **Player:** Um?
- **Death:** Um!
- **Player:** Um... Um, um, um...
- **Death:** If you were thinking of cracking some wry joke, don't. I am NOT in the mood.
- **Player:** Okay, different approach. WHAT is this place?
- **Death:** It is many things to many people. A city for the dead; a necropolis; a way-station; a waiting room...
- **Death:** All who die pass through it. Most know where they are going, and so quickly head downriver to the bridge, and on to their afterlives.
- **Death:** But some are not ready, do not know, or are simply waiting for loved ones to join them in death. For them, this is home.
- **Death:** And so here they wait, in a city built from the memories of the dead who inhabit it.
- **Player:** Wait, it's built from memories, but you can't even remember what it's called? How ironic.
- **Death:** *stares into your soul*
- **Player:** I'm joking! Sorry...

#### After having completed Rune Mythos and before having completed Vessel of the Harbinger

- (see|Vessel of the Harbinger)

### Death's office


#### Talk to

- (Condition: If the player has an active task from another day:)
  - **Death:** You are taking a long time to complete my assignment, Player. Are you finding it too difficult?
  - If you choose to reset your assignment this will be treated as a brand new task, with fresh rerolls. There is no guarantee the new assignment will be different to your current one. If you wish to reroll your current task, use your grim gem instead.
  - (continue)
- (Condition: Without an active task from another day:)
  - **Death:** What brings you to my realm?
  - (continue)
- [Menu]: Select an Option
  - {{anchor|needassign}} [Choice]: I need an assignment.|cond=Without an active assignment:
    - (Condition: If the player has not previously completed today's task:)
      - {{anchor|assign}} (Condition: By chance with Reaper's choice unlocked, or during certain events:)
        - ((An interface titled 'PICK TASK' opens, showing a list of all bosses.))  <!-- are group/skilling bosses greyed out if not enabled? -->
          - [Choice]: [Boss]
            - (continue)
    - (Condition: If the player has already completed today's task, but has not unlocked 'Additional tasks':)
      - {{transcript missing}}
    - (Condition: If the player has already completed today's task and has unlocked 'Additional tasks':)
      - **Death:** You have done what I asked of you today, but there is still an imbalance to be addressed.
      - (Condition: Without 250 slayer points:)
        - **Death:** I would give you another assignment, but I ask for 250 slayer points in exchange. You do no have what I seek.
      - (Condition: With 250 slayer points:)
        - **Death:** I will give you another assignment, but I will require 250 slayer points in exchange.
        - [Menu]: Select an Option
          - [Choice]: Yes, I would like to purchase another assignment for 250 slayer points.
            - You exchange 250 slayer points for an additional reaper assignment.
            - (continue)
          - [Choice]: No, thank you.
            - (end)
    - **Death:** I require you to collect [number] souls from the following battle: [Boss]. Can I trust you with this task?
    - You have a new reaper assignment: [number] x [Boss].
    - [Menu]: Select an Option
      - [Choice]: You certainly can. Thanks!
        - (end)
      - [Choice]: I'd like a different assignment.
        - (below|newassign)
      - [Choice]: I need some hints about my assignment.
        - (below)
  - {{anchor|newassign}} [Choice]: I'd like a new assignment.|cond=With an active assignment:
    - (Condition: First time rerolling an assignment today:)
      - **Death:** I will be patient with you once, with no penalty. Do you wish me to assign a new creature?
        - [Menu]: Select an Option
          - [Choice]: Yes, remove my current assignment and give me a new one.
            - (above|assign)
          - [Choice]: No, I've changed my mind. Leave my assignment.
            - (end)
    - (Condition: Second time rerolling an assignment today:)
      - **Death:** Do not think I will allow you to change your mind freely. If you request a different assignment today, you will only receive 75% of the reaper points for completion. You will gain the full experience, however.
      - {{anchor|reroll2}} [Menu]: Select an Option
        - [Choice]: I understand, remove my current assignment and give me a new one.
          - (above|assign)
        - [Choice]: No, I've changed my mind. Leave my assignment.
          - (end)
    - (Condition: Third time rerolling an assignment today:)
      - **Death:** Do not think I will allow you to change your mind freely. If you request a different assignment today, you will only receive 50% of the reaper points for completion. You will gain the full experience, however.
      - (continuea|reroll2)
    - (Condition: Fourth time rerolling an assigment today:)
      - **Death:** Do not think I will allow you to change your mind freely. If you request a different assignment today, you will only receive 25% of the reaper points for completion. You will gain the full experience, however.
      - (continuea|reroll2)
    - (Condition: Fifth time rerolling an assignment today:)
      - **Death:** I find your indecision tiresome. If you request a different assignment again today you will not receive and reaper points for completion. I cannot stop you from receiving the full experience...unfortunately.
      - (continuea|reroll2)
    - (Condition: After the fifth reroll today:)
      - **Death:** My patience only stretches so far. You have wasted enough of my time, I must address this imbalance myself. Be gone, mortal.
  - [Choice]: Are there any rewards for this?
    - (opens=Death's Store)
  - [Choice]: Am I dead? What do you want from me?
    - **Death:** You are not dead... yet. I have allowed you to enter as I need your help with a task.
    - **Death:** As you are no doubt aware, I am Death. The Reaper, the Collector of Souls, or any other name civilisations have given me. My task is to retrieve the soul from a dying creature, enabling its passage to the underworld.
    - **Player:** So what do you need me for?
    - **Death:** There is an imbalance in the harmony of life and death. There is far too much... life.
    - **Death:** My eyes have been on you in this age, Player, as have the eyes of many others. You appear to have the skills I require to bring balance.
    - **Player:** So you want me to kill stuff?
    - **Death:** If you wish to put it so indelicately, yes.
    - **Player:** Great! When do I start?
    - (Condition: With an active assignemt:)
      - **Death:** Immediately. I have already tasked you to collect souls from the following battle: [Boss]. You have yet to bring me [number] souls. <!-- still plural with 1 soul left? -->
    - (Condition: Without an active assignment:)
      - (above|needasssign)
  - [Choice]: I'd like another grim gem.
    - (receives=Grim gem)
    - [pic=Grim gem detail.png]
    - (other) <!-- not quite right, shows: 'different assigmment; any rewards?; hints; AmIdead?; That's all, thanks; -->
  - [Choice]: More options.
    - [Choice]: Can you help me overcharge this ring? <!-- does this only appear after unlocking the ability from Death's Store? -->
      - **Death:** I can help you but it will come at a cost.
      - **Death:** To overcharge your ring I will need 25 Black stone hearts and 5 cut onyxes.
      - [Menu]: Are you sure you want to do this?
      - [Choice]: Yes
        - (Condition: Without carrying a ring of death:)
          - **Death:** You don't have a ring for me to overcharge.
        - (Condition: With a ring of death, but without all ingredients:)
          - {{transcript missing}}
        - (Condition: With a ring of death and all ingredients:)
          - {{transcript missing}}
      - [Choice]: No
        - (end)
    - [Choice]: I'd like to discuss Nomad and the Underworld.
      - {{transcript missing}}
    - [Choice]: I need some hints about my assignment.|cond=With an active assignment:
    - [Choice]: More options.
      - (previous)
    - [Choice]: That's all, thanks.
      - (end)

#### Get task

- (Condition: If the player has an active task from another day:)
  - If you choose to reset your assignment this will be treated as a brand new task, with fresh rerolls. There is no guarantee the new assignment will be different to your current one. If you wish to reroll your current task, use your grim gem instead.
  - [Menu]: Select an Option
    - [Choice]: I'd like a new assignment.
      - (above)
    - [Choice]: I'd like another grim gem.
      - (above)
    - [Choice]: Are there any rewards for this?
      - (above)
    - [Choice]: I need some hints about my assignment.
      - (above)
    - [Choice]: Am I dead? What do you want from me?
      - (above)
- (Condition: Without an active task from another day:)
  - {{transcript missing}}

#### Rewards

- (opens=Death's Store)

#### Reclaim items


##### With items to reclaim

- (above|reclaim-items)

##### Without items to reclaim

- **Death:** You have nothing to reclaim, Player.

#### Death event

- (Condition: If you have no additional death events unlocked:)
  - You currently have no additional death events unlocked.
- (Condition: If you have at least one additional death event unlocked:)
  - {{Transcript missing}}
