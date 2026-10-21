# Robin

- **Original Wiki Page**: [Transcript:Robin](https://runescape.wiki/w/Transcript%3ARobin)
- **Letter**: `R`

---

## Dialogue Transcript


### Before Ghosts Ahoy

- [Menu]: Choose an option:
  - [Choice]: About the Task System...
    - (below)
  - [Choice]: Talk about something else.
    - (Condition: If the player doesn't have a bedsheet:)
      - **Player:** It's nice to see another human face around here.
      - **Robin:** Leave me be, peasant - I am relaxing.
      - **Player:** Well, that's nice!
      - **Robin:** Do you know who I am?
      - **Player:** I'm sorry, I haven't had the privilege.
      - **Robin:** I, peasant, am Robin, Master Bowman. I am very famous you know.
      - **Player:** Oh, Robin, Master Bowman, I see.
      - **Robin:** So have you heard of me?
      - **Player:** No.
      - **Robin:** Would you do me a favour? I appear to have run out of bed linen. Can you run along to the innkeeper and get me a clean bedsheet?
      - [Menu]: Select an Option
        - [Choice]: Anything for a famous person such as yourself.
          - **Player:** Anything for a famous person such as yourself.
          - **Robin:** Now that sounds more like it. Run along now, get me my sheet.
        - [Choice]: Go and get it yourself.
          - **Player:** Go and get it yourself.
          - **Robin:** Oh charming. You just can't get the staff these days.
    - (Condition: If the player has a bedsheet:)
      - **Player:** I've brought you a clean bedsheet, Robin.
      - (removes=bedsheet)
      - **Robin:** Well it's about time. Run along now, I need some Robin time.

### After Ghosts Ahoy

- [Menu]: Choose an option:
  - [Choice]: About the Task System...
    - ((If the player has completed the medium Morytania achievements and the rewards have not been claimed:))
      - **Player:** I've completed all of the Medium Tasks in the Morytania set.
      - **Robin:** So you have. I have some special leggings kept aside for you.
      - [Robin hands you a pair of leggings and a lamp.]
      - **Robin:** There you go. They're a bit odd, though. I'm not sure I like the way they fit; they feel rather slimy, but at least you can have a ball at the forge in town. Oh, and someone gave me this lamp, but it's not really any use to me.
      - **Player:** Thanks!
      - **Robin:** By the way, Lyra says she'll pop down and look after your mushroom patch, and Razmire has been in touch about some planks and more doses to his olive oil. I've also...acquired some of that slime you adventurers
      - **Robin:** seem to like, and I'll swap you bones for bonemeal as I, uh, made a deal with someone and seem to have rather a lot.
      - **Robin:** On top of that there are some storage chests in Mort'ton, near the funeral pyres. You'll be allowed to stockpile any one type of pyre log type in them from now on.
      - (continue)
    - (Condition: If the player has lost their Morytania legs 2:)
      - **Robin:** Ah, the leggings wearer! How are you finding them?
      - **Player:** I lost them.
      - **Robin:** Oh, no!
      - **Robin:** Never mind, I have another pair. Here...
      - [Robin hands you a pair of leggings.]
      - (continue)
    - [Menu]: Choose an option:
      - [Choice]: Tell me about the Achievement System.
        - **Robin:** Very well: the Achievement System is a collection of deeds you may wish to complete while adventuring around the world.
        - **Robin:**You can earn special rewards for completing certain achievements; at the very least, each is worth a cash bounty from Explorer Jack in Lumbridge.
        - **Robin:** Some also give items that will help complete other achievements, and many count as progress towards the set for the area they're in.
        - [Menu]: Choose an option:
          - [Choice]: Tell me about the set reward for this locality.
            - **Player:** Tell me about the set reward for this area.
            - **Robin:** For completing the Morytania set, you are presented with some leggings.
            - **Robin:** These leggings will become increasingly useful as you complete greater difficulties of task sets.
            - **Robin:** When you are presented with your rewards, you will be told of their uses.
            - You may also see what rewards a set item provides by hovering over the Rewards icon for its Exploration Achievement set in the Achievements interface.
            - (previous2)
          - [Choice]: How do I claim these rewards?
            - **Player:** How do I claim the rewards?
            - **Robin:** You need to complete all Tasks within a particular difficulty set, then you can claim your reward.
            - **Robin:** Some of the Morytania set's Tasks are simple, some require certain skill levels, and others require quests to be started or completed.
            - **Robin:**  To claim your Morytania set rewards, speak to Hiylik Myna just east of Paterdomus, the Strange Old Man at the Barrows, Old Man Ral in Meiyerditch or myself.
            - (previous2)
          - [Choice]: Sorry, I was just leaving.
            - (end)
      - [Choice]: Could I buy a spare of the reward?
        - [Menu]: Choose an option:
          - [Choice]: Morytania legs 1
            - **Robin:** Morytania legs 1? Yes, but I'm afraid it would cost you 1,500 coins.
            - [Menu]: Purchase another for 1,500 coins?
              - [Choice]: Yes
                - [You're handed another Morytania legs 1.]
                - (receives=Morytania legs 1) (removes= 1,500 coins)
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Morytania legs 2
            - **Robin:** Morytania legs 2? Yes, but I'm afraid it would cost you 2,500 coins.
            - [Menu]: Purchase another for 2,500 coins?
              - [Choice]: Yes
                - [You're handed another Morytania legs 2.]
                - (receives=Morytania legs 2) (removes= 2,500 coins)
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Morytania legs 3
            - **Robin:** Morytania legs 3? Yes, but I'm afraid it would cost you 7,500 coins.
            - [Menu]: Purchase another for 7,500 coins?
              - [Choice]: Yes
                - [You're handed another Morytania legs 3.]
                - (receives=Morytania legs 3) (removes= 7,500 coins)
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Morytania legs 4
            - **Robin:** Morytania legs 4? Yes, but I'm afraid it would cost you 15,000 coins.
            - [Menu]: Purchase another for 15,000 coins?
              - [Choice]: Yes
                - [You're handed another Morytania legs 4.]
                - (receives=Morytania legs 4) (removes= 15,000 coins)
              - [Choice]: No
                - **Player:** No thanks.
      - [Choice]: Sorry, I was just leaving.
        - (end)
  - [Choice]: cond=If at least the medium Morytania tasks have been completed and the rewards claimed|Ask for bonemeal and slime.
    - **Player:** You said something about slime and bonemeal when you gave me the Morytania legs...
    - **Robin:** Oh, so I did. I have [13/26/39] buckets of slime left. Simply give me the bones you wish to exchange.
  - [Choice]: cond=If at least the medium Morytania tasks have been completed and the rewards claimed|Ask for information on bonemeal and slime.
    - **Player:** You said something about slime and bonemeal when you gave me the Morytania legs. Can you tell me more?
    - **Robin:** I suppose so. I will exchange bones you bring me for ground bonemeal, and an equivalent number of buckets of slime.
    - **Robin:** I've also begun to accept noted bones recently. The bonemeal and buckets of slime I give you in return will also be noted.
    - **Player:** So, if I bring you 2 wyvern bones and 3 noted dragon bones, you'll give me 2 lots of wyvern bonemeal and 3 lots of noted dragon bonemeal?
    - **Robin:** That's right, and don't forget the five free buckets of slime. You can exchange up to 13/26/39 bones daily. Don't forget you'll need free space for the buckets of slime though!
  - [Choice]: Talk about something else.
    - **Player:** So, still here then.
    - **Robin:** Do you want another game of Runedraw?
    - **Player:** You have a serious gambling problem, you know.

#### Using bones on Robin without sufficient bag space

- **Robin:** Go away peasant, you don't have enough free bag space for that!
