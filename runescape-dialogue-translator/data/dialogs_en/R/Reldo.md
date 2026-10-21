# Reldo

- **Original Wiki Page**: [Transcript:Reldo](https://runescape.wiki/w/Transcript%3AReldo)
- **Letter**: `R`

---

## Dialogue Transcript


### Talking to Reldo

- **Reldo:** Hello there. <br>How can I help you today?
- [Menu]: Choose an option:
  - [Choice]: Tell me about yourself.
    - **Reldo:** Me? What do you want to know?
    - [Menu]: Select an Option
      - [Choice]: What do you do?
        - **Reldo:** I am the palace librarian.
        - **Player:** Ah. That's why you're in the library, then.
        - **Reldo:** Yes.
        - **Reldo:** Although I would probably be in here even if I didn't work here. I like reading.
        - **Reldo:** Some day, I hope to catalogue all of the information stored in these books, so all may read it.
        - (previous)
      - [Choice]: Do you have anything to trade?
        - **Reldo:** Only knowledge.
        - **Player:** How much do you want for that, then?
        - **Reldo:** No, sorry, that was just my little joke. <br>I'm not the trading type.
        - **Player:** Oh, well.
        - (previous)
      - [Choice]: Do you know any heroic stories?
        - **Player:** Do you know any heroic stories?
        - **Reldo:** Yes, I do.
        - **Reldo:** Years ago, a terrible creature slew King Roald's betrothed and terrorized the people. Varrock sent an embassy to Morytania to open a dialogue with Drakan about it.
        - **Player:** What happened?
        - **Reldo:** It didn't end happily. Poor Gar'rth, we didn't know he was... Well, it would be unfair for me to say. That's his secret, not mine.
        - **Player:** What about the terrible creature?
        - **Reldo:** It was brought to justice, but not before claiming many innocents.
        - **Player:** Go on, tell me about Gar'rth.
        - **Reldo:** Another time, perhaps? I have work to do.
        - **Player:** Hmpf!
        - (previous)
      - [Choice]: That's enough about you.
        - (initial)
  - [Choice]: About the Task System...
    - (Condition: If the player has completed medium task set, but not claimed it yet:)
      - **Player:** I've finished all the Medium Tasks in the Varrock set.
      - **Reldo:** Really? How extraordinary! Well, that certainly is a worthy achievement indeed.
      - **Player:** Thanks. Was there a reward?
      - **Reldo:** A reward? Well, yes, I suppose I can help you there.
      - (receives=Varrock armour 2 and Antique lamp (Medium Varrock Tasks))
      - Reldo takes the Varrock armour and attaches some more plate metal to it, filling it out to look like a proper suit of armour. He etches some words into the armour, which glows slightly before fading.
      - **Reldo:** I have enhanced your body armour with a spell. You now have a chance to double your bars when smelting, ores when mining and progress when smithing mithril and adamant. I can also change your Varrock Teleport spell so that it takes you to the Grand Exchange, if you'd find that more convenient. As an extra reward, I have also given you a magical lamp to help with your skills.
      - **Player:** Wow, thanks! What if I lose the armour?
      - **Reldo:** Oh, that's not a problem. You can come back to see me and I'll get you another set.
      - (continue)
    - (Condition: If the player has lost their Varrock armour 2:)
      - **Reldo:** Don't tell me you lost the armour I gave you?
      - **Player:** Yes, sorry about that. I don't know what happened to it.
      - **Reldo:** Oh, well, no harm done. Fortunately, I have another set here - we get quite a lot of Varrock explorers these days, you know.
      - (receives=Varrock armour 2)
      - (continue)
    - [Menu]: Choose an option:
      - [Choice]: Tell me about the Achievement System.
        - **Reldo:** Very well: the Achievement System is a collection of deeds you may wish to complete while adventuring around the world.
        - **Reldo:** You can earn special rewards for completing certain achievements; at the very least, each is worth a cash bounty from Explorer Jack in Lumbridge.
        - **Reldo:** Some also give items that will help complete other achievements, and many count as progress towards the set for the area they're in.
        - [Menu]: Choose an option:
          - [Choice]: Tell me about the set reward for this locality.
            - **Player:** Tell me about the set reward for this area.
            - **Reldo:** For completing the Varrock set, you are presented with some body armour.
            - **Reldo:** This armour will become increasingly useful with each difficulty level of the set that you complete.
            - **Reldo:** When you are presented with your rewards, you will be told of their uses.
            - You may also see what rewards a set item provides by hovering over the Rewards icon for its Exploration Achievement set in the Achievements interface.
            - (previous2)
          - [Choice]: How do I claim these rewards?
            - **Player:** How do I claim the rewards?
            - **Reldo:** You need to complete all Tasks within a particular difficulty set, then you can claim your reward. Most of the Varrock set's Tasks are straightforward, though you might find some require quests to be started, if not finished.
            - **Reldo:** To claim your Varrock set reward, speak to Rat Burgiss south of Varrock, Vannaka in Edgeville Dungeon, or me.
            - (previous2)
          - [Choice]: Sorry, I was just leaving.
            - (end)
      - [Choice]: Could I buy a spare of the reward?
        - [Menu]: Choose an option:
          - [Choice]: Varrock armour 1
            - **Reldo:** Varrock armour 1? Yes, but I'm afraid it would cost you 1,500 coins.
            - [Menu]: Purchase another for 1,500 coins?
              - [Choice]: Yes
                - [You're handed another Varrock armour 1.]
                - (receives=Varrock armour 1) (removes= 1,500 coins)
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Varrock armour 2
            - **Reldo:** Varrock armour 2? Yes, but I'm afraid it would cost you 2,500 coins.
            - [Menu]: Purchase another for 2,500 coins?
              - [Choice]: Yes
                - You're handed another Varrock armour 2.
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Varrock armour 3
            - **Reldo:** Varrock armour 3? Yes, but I'm afraid it would cost you 7,500 coins.
            - [Menu]: Purchase another for 7,500 coins?
              - [Choice]: Yes
                - [You're handed another Varrock armour 3.]
                - (receives=Varrock armour 3) (removes= 7,500 coins)
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Varrock armour 4
            - **Reldo:** Varrock armour 4? Yes, but I'm afraid it would cost you 15,00 coins.
            - [Menu]: Purchase another for 15,000 coins?
              - [Choice]: Yes
                - [You're handed another Varrock armour 4.]
                - (receives=Varrock armour 4) (removes= 15,000 coins)
              - [Choice]: No
                - **Player:** No thanks.
      - [Choice]: cond=If at least the easy Varrock tasks have been completed and the rewards claimed|I'd like to change my teleport point.
        - **Player:** I'd like to change my Varrock Teleport point.
        - **Player:** Can I change my Varrock teleport point?
        - **Reldo:** Certainly. It's currently set to [the altar in the north of Varrock/the fountain in the middle of Varrock/the Grand Exchange]. Where would you prefer?
        - [Menu]: Choose an option:
          - [Choice]: Fountain in the middle of Varrock.
            - **Reldo:** Okay, that's all done.
            - Your Varrock teleport will now teleport you to the middle of Varrock.
          - [Choice]: Grand Exchange.
            - **Reldo:** Okay, that's all done.
            - Your Varrock teleport will now teleport you to the Grand Exchange.
          - [Choice]: Altar in the north.
            - **Reldo:** Okay, that's all done.
            - Your Varrock teleport will now teleport you to the altar in the north of Varrock.
      - [Choice]: Sorry, I was just leaving.
        - (end)
  - [Choice]: cond=After completing TokTz-Ket-Dill|I have a question about the TzHaar language.
    - **Player:** Hello, Reldo. Could you remind me where I could find that book on the TzHaar language?
    - **Reldo:** Of course. It's the TzHaar Tourist Guide. It should be somewhere in the library. I'm not sure exactly where, but if you have a look around, I'm sure you will find it.
    - **Player:** Alright, thank you.
  - [Choice]: cond=After completing Missing My Mummy|I'd like to talk about a pyramid.
    - **Player:** I'd like to talk about a pyramid.
    - **Reldo:** How goes the matter of the mummy's personality?
    - **Player:** She is reunited with knowledge of her personality now - so overall a happy ending.
    - **Reldo:** Excellent, all too rare to see a good end to matters these days.

#### Archaeology relic

(Condition: After reaching level 42 Archaeology:)
- **Reldo:** Before we get to business, I hear you have access to the Everlight Dig Site. I wonder if you might retrieve a certain artefact from there for me...
- **Reldo:** If you would bring me a restored Dominarian device, I have a magical relic I would give you as payment. It might help you, er, 'fund' future endeavours.
- (Condition: Only after completing Desperate Times:)
  - **Player:** Why do you need a Dominarian device.
  - **Reldo:** Oh, come now, you know I like to tinker. The idea of some ahead-of-its-time technology from my old stomping grounds is too intriguing a mystery to pass up!
  - (continue)
- (Condition: If the player has the Dominarian device:)
  - **Player:** As it so happens, I have just that thing on me right now!
  - (continue)
- [Menu]: Give Dominarian device to Reldo?
  - [Choice]: Yes.
    - (removes=Dominarian device) (receives=Andvaranaut)
    - **Reldo:** And in return...this is Andvaranaut. This ring will help mask you from people you are picking the pockets of. That's not really my style.
    - (Condition: Only after completing Desperate Times:)
      - **Player:** One of your own creation, I take? You have a knack for creating rings that manipulate people into parting with their money.
      - **Reldo:** What can I say? My gift is my curse.
      - **Player:** And you say picking pockets isn't your style?
      - **Reldo:** Of course not! Why go through all the effort of stealing from individuals, when the payoff is so much greater if you just broaden your horizons a little.
      - [Menu]: Select an Option
        - [Choice]: [Talk to Charos.]
          - (above|Talking to Reldo)
        - [Choice]: [Talk to Reldo.]
          - (above|Talking to Reldo)
  - [Choice]: No.
    - **Reldo:** I hope you'll reconsider. I need it for my research.
    - (continuea|Talking to Reldo)
- (Condition: If the player does not have the Dominarian device:)
  - **Player:** I'll keep you in mind.
  - (continuea|Talking to Reldo)

### Shield of Arrav

- (see|Shield of Arrav)

### The Knight's Sword

- (see|The Knight's Sword)

### Dimension of Disaster: Defender of Varrock

- (see|Dimension of Disaster: Defender of Varrock)

### The Lost Tribe

- (see|The Lost Tribe#Reldo)

### A Tail of Two Cats

- (see|A Tail of Two Cats#Talking to Reldo)

### Missing My Mummy

- (see|Missing My Mummy#Reldo)

### TokTz-Ket-Dill

- (see|TokTz-Ket-Dill#Varrock Palace's library)

### Tomes of the Warlock

- (see|Tomes of the Warlock#Talking to Reldo)

### You Are It

- (see|You Are It#Reldo)

### While Guthix Sleeps

- (see|While Guthix Sleeps#In Search of Movario)
