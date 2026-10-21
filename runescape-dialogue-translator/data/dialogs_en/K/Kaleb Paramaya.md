# Kaleb Paramaya

- **Original Wiki Page**: [Transcript:Kaleb Paramaya](https://runescape.wiki/w/Transcript%3AKaleb%20Paramaya)
- **Letter**: `K`

---

## Dialogue Transcript


### In Shilo Village


#### Before completing the Shilo Village quest

- **Kaleb Paramaya:** I'm getting out of here Bwana, the place is infested with zombies.

#### After completing the Shilo Village quest

- **Player:** Hello.
- **Kaleb Paramaya:** Hello Bwana, What{{Sic}} can I do for you today?
- [Menu]: Select an Option
  - [Choice]: Can you tell me a bit about this this place?
    - **Player:** Can you tell me a bit about this this place?
    - **Kaleb Paramaya:** Of course Bwana, you look like a traveller!
    - **Player:** Yes I am actually!
    - **Kaleb Paramaya:** Well, I am a traveller myself, and I have set up this hostel for adventurers and travellers who are weary from their journey.
    - **Kaleb Paramaya:** There is a dormitory upstairs if you are tired, it costs 35 gold pieces which covers the cost of laundry and cleaning.
  - [Choice]: Buy something.
    - [Menu]: Select an Option
      - [Choice]: Buy some wine: 1 Gold.{{Sic}}
        - **Kaleb Paramaya:** Very good [sir/madam]!
        - (Condition: If the player does not have enough money:)
          - **Kaleb Paramaya:** Sorry Bwana, you don't have enough money.
          - You can not afford that.
        - (Condition: If the player has enough money:)
          - (receives=jug of wine) (removes=one coin)
          - You purchase a jug of wine.
      - [Choice]: Buy some Beer: 2 Gold.{{Sic}}
        - **Kaleb Paramaya:** Very good [sir/madam]!
        - (Condition: If the player does not have enough money:)
          - **Kaleb Paramaya:** Sorry Bwana, you don't have enough money.
          - You can not afford that.
        - (Condition: If the player has enough money:)
          - (receives=beer) (removes=two coins)
          - You purchase a frothy glass of beer.
      - [Choice]: Buy a nights rest: 35 Gold{{Sic}}
        - **Kaleb Paramaya:** Very good [sir/madam]!
        - (Condition: If the player does not have enough money:)
          - **Kaleb Paramaya:** Sorry Bwana, you don't have enough money.
          - You can not afford that.
        - (Condition: If the player has enough money:)
          - (receives=Paramaya ticket) (removes=35 coins)
          - You purchase a ticket to access the dormitory.
      - [Choice]: Buy a pack of 5 Dorm tickets: 175 Gold{{Sic}}
        - **Kaleb Paramaya:** Very good [sir/madam]!
        - (Condition: If the player does not have enough money:)
          - **Kaleb Paramaya:** Sorry Bwana, you don't have enough money.
          - You can not afford that.
        - (Condition: If the player has enough money:)
          - (receives=five Paramaya tickets) (removes=175 coins)
          - You purchase 5 tickets to access the dormitory.
  - [Choice]: About the Task System...
    - (Condition: If the player has completed the medium Karamja achievements, but not yet claimed the rewards:)
      - **Player:** I've done all the Medium Tasks in the Karamja set.
      - **Kaleb Paramaya:** Ahh, yes, you have! Congratulations!
      - (Condition: If the player does not have Karamja gloves 1 in backpack:)
        - **Kaleb Paramaya:** How can I enchant your Karamja gloves if you don't have them with you? Bring me the Karamja gloves you earned from completing the Easy Tasks.
        - (continue|task-system)
      - (Condition: If the player has Karamja gloves 1 in backpack:)
        - Kaleb takes the Karamja gloves and mutters something over them. They seem to shimmer. He hands them back.
        - (receives=Karamja gloves 2 and an antique lamp)
        - **Kaleb Paramaya:** The enchantment I've placed on these gloves is a symbol of your further exploration of the island. As well as the benefits of the previous ones, you can also earn more rewards in the Agility Arena. Oh, there's a little added extra for all your hard work too.
        - **Player:** Wow, thanks!
        - **Kaleb Paramaya:** If you lose them, come back to me to reclaim them.
        - (continue|task-system)
    - (Condition: If the player has lost their Karamja gloves 2:)
      - **Kaleb Paramaya:** Oh...wait a minute, I remember you from last time - didn’t I bless your Karamja gloves?
      - **Player:** Yes, but I lost them.
      - **Kaleb Paramaya:** Thought as much. Here, have another pair.
      - (receives=Karamja gloves 2)
      - (continue|task-system)
    - [Menu]: Choose an option:
      - [Choice]: Tell me about the Achievement System.{{anchor|achievements}}
        - **Kaleb Paramaya:** Very well: the Achievement System is a collection of deeds you may wish to complete while adventuring around the world.
        - **Kaleb Paramaya:** You can earn special rewards for completing certain achievements; at the very least, each is worth a cash bounty from Explorer Jack in Lumbridge.
        - **Kaleb Paramaya:** Some also give items that will help complete other achievements, and many count as progress towards the set for the area they're in.
        - [Menu]: Choose an option:
          - [Choice]: Tell me about the set reward for this locality.
            - **Player:** Tell me about the set reward for this area.
            - **Kaleb Paramaya:** For completing the Tasks in the Karamja set, you are presented with a pair of gloves.
            - **Kaleb Paramaya:** Completing each difficulty level of the set will allow your gloves to be improved.
            - **Kaleb Paramaya:** When you are presented with your rewards, you will be told of their uses.
            - You may also see what rewards a set item provides by hovering over the Rewards icon for its Exploration Achievement set in the Achievements interface.
            - (previous)
          - [Choice]: How do I claim these rewards?
            - **Player:** How do I claim the rewards?
            - **Kaleb Paramaya:** You need to complete all of the Tasks in the set of a particular difficulty, then you can claim your reward.
            - **Kaleb Paramaya:** Some of the Karamja set's Tasks are simple, some will require certain skill levels, and some might require quests to be started or completed.
            - **Kaleb Paramaya:** You can claim your Karamja set reward from Jackie the Fruit at the Brimhaven Agility Arena, me, or one of the jungle foresters to the south.
            - (previous)
          - [Choice]: Sorry, I was just leaving.
            - (end)
      - [Choice]: Could I buy a spare of the reward?
        - [Menu]: Choose an option:
          - [Choice]: Karamja gloves 1
            - **Kaleb Paramaya:** Karamja gloves 1? Yes, but I'm afraid it would cost you 1,500 coins.
            - [Menu]: Purchase another for 1,500 coins?
              - [Choice]: Yes
                - (receives=Karamja gloves 1) (removes=1,500 coins)
                - [You're handed another Karamja gloves 1.]
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Karamja gloves 2
            - **Kaleb Paramaya:** Karamja gloves 2? Yes, but I'm afraid it would cost you 2,500 coins.
            - [Menu]: Purchase another for 2,500 coins?
              - [Choice]: Yes
                - (receives=Karamja gloves 2) (removes=2,500 coins)
                - [You're handed another Karamja gloves 2.]
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Karamja gloves 3
            - **Kaleb Paramaya:** Karamja gloves 3? Yes, but I'm afraid it would cost you 7,500 coins.
            - [Menu]: Purchase another for 7,500 coins?
              - [Choice]: Yes
                - (receives=Karamja gloves 3) (removes=7,500 coins)
                - [You're handed another Karamja gloves 3.]
              - [Choice]: No
                - **Player:** No thanks.
          - [Choice]: Karamja gloves 4
            - **Kaleb Paramaya:** Karamja gloves 4? Yes, but I'm afraid it would cost you 15,000 coins.
            - [Menu]: Purchase another for 15,000 coins?
              - [Choice]: Yes
                - (receives=Karamja gloves 4) (removes=15,000 coins)
                - [You're handed another Karamja gloves 4.]
              - [Choice]: No
                - **Player:** No thanks.
      - [Choice]: Sorry, I was just leaving.
        - (end)

##### Attempting to enter the dormitory


##### With a ticket

- (removes=Paramaya ticket)
- The barman takes your ticket and allows you up to the dormitory.

##### Without a ticket

- **Kaleb Paramaya:** You can buy a ticket to the dormitory from me. And have a lovely nights rest.
