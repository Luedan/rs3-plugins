# Kolodion

- **Original Wiki Page**: [Transcript:Kolodion](https://runescape.wiki/w/Transcript%3AKolodion)
- **Letter**: `K`

---

## Dialogue Transcript


### Standard dialogue

- [Menu]: Select an Option
  - [Choice]: Task System
    - [Menu]: Choose an option:
      - [Choice]: Tell me about the Task System.
        - **Kolodion:** Very well: the Achievement System is a collection of deeds you may wish to complete while adventuring around the world.
        - **Kolodion:** You can earn special rewards for completing certain achievements; at the very least, each is worth a cash bounty from Explorer Jack in Lumbridge.
        - **Kolodion:** Some also give items that will help complete other achievements, and many count as progress towards the set for the area they're in.
        - [Menu]: Choose an option:
          - [Choice]: Tell me about the set reward for this locality.
            - **Kolodion:** For completing the Wilderness set, you are presented with Wilderness sword.
            - **Kolodion:** This sword will become increasingly useful with each difficulty level of the set that you complete.
            - **Kolodion:** When you are presented with your rewards, you will be told of their uses.
            - You may also select a set Task (denoted in the main Task System interface by a small shield icon) and choose 'Rewards' to see what rewards a set item provides.
            - (previous2)
          - [Choice]: How do I claim these rewards?
            - **Kolodion:** You need to complete all the Tasks in the set of a particular difficulty, then you can claim your reward. Most of the Wilderness set's Tasks are straightforward, although you might find some require quests to be
            - **Kolodion:** started, if not finished.
            - **Kolodion:** To claim the Wilderness set reward, speak to Mr Ex, Mandrith, Quercus or myself.
            - (previous2)
          - [Choice]: Sorry, I was just leaving.
            - (end)
      - [Choice]: Can I claim any rewards from you?
        - (Condition: If the player doesn't have any rewards to claim:)
          - **Kolodion:** You don't have any more rewards to claim!
        - (Condition: If the player has not claimed the rewards from the elite Wilderness task set:)
          - (Condition: Without three free backpack spaces:)
            - **Kolodion:** I'm afraid you don't have enough inventory space to claim all your rewards. Speak to me again when you have 3 spaces.
          - (Condition: Without three free backpack spaces:)
            - **Player:** I've completed all the tasks in the elite Wilderness task set.
            - **Kolodion:** Well done Player, I've kept some rewards aside for you.
            - (receives=two Antique lamp (Elite Wilderness Tasks) and Wilderness sword 1)
            - [You are given some rewards for completing the elite Wilderness task set!]
            - **Kolodion:** There you go, looks like that's everything.
        - (Condition: If the player has lost their Wilderness sword 4:)
          - **Player:** I lost the Wilderness sword 4 you gave me...
          - **Kolodion:** Lucky for you I have a spare... I'm afraid it's going to cost you 100,000 coins though.
          - [Menu]: Reclaim for 100,000 coins?
            - [Choice]: Yes.
              - (Condition: If the player does not have enough money:)
                - You can not afford that.
                - **Kolodion:** But it doesn't look like you have enough money for that. Come back to me when you do.
              - (Condition: If the player has enough money:)
                - (removes=100,000 coins) (receives=Wilderness sword 4)
                - [You're handed another Wilderness sword 4.]
            - [Choice]: No.
              - **Player:** No thanks.
      - [Choice]: cond=If the player has claimed at least one of the Wilderness task set rewards:|Could I buy a spare of the reward?
        - [Menu]: Choose an option:
          - [Choice]: Wilderness sword 1
            - **Kolodion:** Wilderness sword 1? Yes, but I'm afraid it would cost you 50,000 coins.
            - [Menu]: Purchase another for 50,000 coins?
              - [Choice]: Yes
                - (removes=50,000 coins) (receives=Wilderness sword 1)
                - [You're handed another Wilderness sword 1.]
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Wilderness sword 2
            - **Kolodion:** Wilderness sword 2? Yes, but I'm afraid it would cost you 65,000 coins.
            - [Menu]: Purchase another for 65,000 coins?
              - [Choice]: Yes
                - (removes=65,000 coins) (receives=Wilderness sword 2)
                - [You're handed another Wilderness sword 2.]
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Wilderness sword 3
            - **Kolodion:** Wilderness sword 3? Yes, but I'm afraid it would cost you 80,000 coins.
            - [Menu]: Purchase another for 80,000 coins?
              - [Choice]: Yes
                - (removes=80,000 coins) (receives=Wilderness sword 3)
                - [You're handed another Wilderness sword 3.]
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Wilderness sword 4
            - **Kolodion:** Wilderness sword 4? Yes, but I'm afraid it would cost you 100,000 coins.
            - [Menu]: Purchase another for 100,000 coins?
              - [Choice]: Yes
                - (removes=100,000 coins) (receives=Wilderness sword 4)
                - [You're handed another Wilderness sword 4.]
              - [Choice]: No
                - **Player:** No thanks.
      - [Choice]: Sorry, I was just leaving.
        - (end)
  - [Choice]: Something else
    - (below)

#### Players under level 60 magic

- [Menu]: Select an Option
  - [Choice]: Task System
    - (above|tasks)
  - [Choice]: Something else
    - **Player:** Hello there. What is this place?
    - **Kolodion:** Do not waste my time with trivial questions. I am the Great Kolodion, master of battle magic. I have an arena to run.
    - **Player:** Can I enter?
    - **Kolodion:** Hah! A wizard of your level? Don't be absurd.

#### Players over level 60 magic

- [Menu]: Select an Option
  - [Choice]: Task System
    - (above|tasks)
  - [Choice]: Something else
    - **Player:** Hello there. What is this place?
    - **Kolodion:** I am the great Kolodion, master of battle magic, and this is my battle arena. Top wizards travel from all over Gielinor to fight here.
    - [Menu]: Select an Option
      - [Choice]: Can I fight here?
        - **Player:** Can I fight here?
        - **Kolodion:** My arena is open to any high level wizard, but this is no game. Many wizards fall in this arena, never to rise again. The strongest mages have been destroyed.
        - **Kolodion:** If you're sure you want in?
        - (continue|join)
      - [Choice]: What's the point of that?
        - **Player:** What's the point of that?
        - **Player:** We learn how to use our magic to its fullest and how to channel the forces of the cosmos into our world...
        - **Player:** But mainly, I just like blasting people into dust.
        - (other)
      - [Choice]: That's barbaric!
        - **Player:** That's barbaric!
        - **Kolodion:** Nope, it's magic. But I know what you mean. So do you want to join us?
        - (continue|join)
    - {{anchor|join}}[Menu]: Select an Option
      - [Choice]: Yes indeedy.
        - **Player:** Yes indeedy.
        - **Kolodion:** Good, good. You have a healthy sense of competition.
        - **Kolodion:** Remember, traveller - in my arena, hand-to-hand combat is useless. Your strength will diminish as you enter the arena, but the spells you can learn are amongst the most powerful in all of Gielinor.
        - **Kolodion:** Before I can accept you in, we must duel.
        - [Menu]: Select an Option
          - [Choice]: Okay, let's fight.
            - **Player:{{anchor|lets-fight}}** Okay, let's fight.
            - **Kolodion:** I must first check that you are up to scratch.
            - **Player:** You don't need to worry about that.
            - **Kolodion:** Not just any magician can enter - only the most powerful and most feared. Before you can use the power of this arena, you must prove yourself against me.
            - {{Qact|Kolodion teleports himself and the player to the Mage Arena.}}
            - (continue|Battling him at the Mage Arena)
          - [Choice]: No thanks.
            - **Player:** No thanks.
      - [Choice]: No I don't.
        - **Player:** No I don't.
        - **Kolodion:** Your loss.

### If the player fled a fight

- [Menu]: Select an Option
  - [Choice]: Task System
    - (above|tasks)
  - [Choice]: Something else
    - (continuea|lets-fight)

### Battling him at the Mage Arena


#### First form

- **Kolodion:** {{RSChat|You must prove yourself... now!}}

#### Second form

- {{Qact|Kolodion transforms into an ogre.}}
- **Kolodion:** {{RSChat|This is only the beginning; you can't beat me!}}

#### Third form

- {{Qact|Kolodion transforms into a troll.}}
- **Kolodion:** {{RSChat|Foolish mortal; I am unstoppable.}}

#### Fourth form

- {{Qact|Kolodion transforms into a dark beast.}}
- **Kolodion:** {{RSChat|Now you feel it... The dark energy}}

#### Final form

- {{Qact|Kolodion transforms into a black demon.}}
- **Kolodion:** {{RSChat|Aaaaaaaarrgghhhh! The power!}}

#### Defeating him

- {{Qact|Kolodion transforms back into a human and teleports himself and the player to the Mage Arena bank.}}
- **Kolodion:** Well done, young adventurer; you truly are a worthy battle mage.
- **Player:** What now?
- **Kolodion:{{anchor|step-into-pool}}** Step into the magic pool. It will take you to a chamber. There, you must decide which god you will represent in the arena.
- **Player:** Thanks, Kolodion.
- **Kolodion:** That's what I'm here for.

### Talking to him after defeating him and without having chosen a god to represent

- [Menu]: Select an Option
  - [Choice]: Task System
    - (above|tasks)
  - [Choice]: Something else
    - **Player:** Hello, Kolodion.
    - **Kolodion:** Hello, young mage. You're a tough one.
    - **Player:** What now?
    - (continuea|step-into-pool)

### Talking to him after having chosen a god to represent

- [Menu]: Select an Option
  - [Choice]: Task System
    - (above|tasks)
  - [Choice]: Something else
    - **Player:** Hello, Kolodion.
    - **Kolodion:** Hey there, how are you? Are you enjoying the bloodshed?
    - **Player:** I think I've had enough for now.
    - **Kolodion:**A shame. You're a good battle mage. I hope to see you soon.
