# Captain Harlan

- **Original Wiki Page**: [Transcript:Captain Harlan](https://runescape.wiki/w/Transcript%3ACaptain%20Harlan)
- **Letter**: `C`

---

## Dialogue Transcript


### In Lumbridge Market

- [Menu]: What would you like to talk about?
  - [Choice]: Who are you?
    - **Harlan:** My name is Harlan, a master of defence!
    - (other)
  - [Choice]: cond=If the player has 99 Defence|What is that cape you're wearing?
    - **Harlan:** Ah, this is a Skillcape of Defence. I have mastered the art of defence and wear it proudly to show others.
    - **Player:** Hmm, interesting.
    - **Harlan:** Ah, but I can see you are already a master in the fine art of defence. Perhaps you have come to me to purchase a Skillcape of Defence, and thus join the elite few who have mastered this exacting skill?
    - [Menu]: Choose an option:
      - [Choice]: Yes, please sell me a Skillcape of Defence.
        - (Condition: If the player has a ring of charos (a) equipped:)
          - **Harlan:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
          - [Menu]: Choose an option:
            - [Choice]: 92,000 coins? That's much too expensive.
              - **Player:** I know where to find you if I change my mind.
            - [Choice]: I think I have the money right here, actually.
              - (Condition: If the player has no backpack space:)
                - **Harlan:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some backpack space before I can sell you one.
              - (Condition: If the player does not have enough money:)
                - **Player:** But unfortunately, I was mistaken.
                - **Harlan:** Well, come back and see me when you do.
              - (Condition: If the player has enough money:)
                - (receives=Defence cape and Defence hood) (removes=92,000 coins)
                - **Harlan:** Excellent! Wear that cape with pride my friend.
        - (Condition: If the player does not have a ring of charos (a) equipped:)
          - [Menu]: Choose an option:
            - [Choice]: 99,000 coins? That's much too expensive.
              - **Player:** I know where to find you if I change my mind.
            - [Choice]: I think I have the money right here, actually.
              - (Condition: If the player has no backpack space:)
                - (above)
              - (Condition: If the player does not have enough money:)
                - (above)
              - (Condition: If the player has enough money:)
                - (receives=Defence cape and Defence hood) (removes=99,000 coins)
                - **Harlan:** Excellent! Wear that cape with pride my friend.
      - [Choice]: No, thanks.
        - (end)
      - [Choice]: I've noticed there are a couple of versions of each skillcape.
        - **Harlan:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
        - (Condition: If you use the old model:)
          - **Harlan:** It looks like you're currently using the old model for your Defence skillcape. Would you like to change to the newer one?
          - (continue)
        - (Condition: If you use the new model:)
          - **Harlan:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
          - (continue)
        - [Menu]: Select an Option
          - [Choice]: Yes, I would like to wear the [new/old] version of the skillcape.
            - **Harlan:** Would you like to wear the [old/newer] model for just this cape, or for the Quest Cape and all of the skillcapes you own?
            - [Menu]: Select an Option
              - [Choice]: I would just like to change the Defence skillcape.
                - **Harlan:** No problem, you will now use the [older/newer] model for your Defence skillcape.
              - [Choice]: I would like to change all my skillcapes.
                - **Harlan:** No problem, you will now use the [older/newer] model for all of your skillcapes!
              - [Choice]: I've changed my mind!
                - (end)
          - [Choice]: No, thank you.
            - **Harlan:** Great! I'm glad you're still enjoying the [old/new] version!
            - (Condition: If the player uses the new model for any other skillcape:)
              - **Harlan:** If you want, I can make it so you use the old model for all of the skillcapes you own.
              - [Menu]: Select an Option
                - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
                  - **Harlan:** Great, you will now use the old model for all of your skillcapes!
                - [Choice]: No, thanks.
                  - (end)
  - [Choice]: Talk about boss assistance.
    - (Condition: If on a free-to-play world:)
      - You need to be on a member's world to use this feature.
    - (Condition: If on a members' world:)
      - **Harlan:** Boss assistance is an incentive to help out your fellow adventurers take on the larger foes of the world.
      - **Player:** So how does it work?
      - **Harlan:** Simple enough really. When a boss dies, if you've fought with adventurers that managed to hurt the boss but still have less than ten kills, you'll receive a point for each person.
      - **Player:** So I get a point for everyone who has less than ten kills and managed to get involved in the fight?
      - **Harlan:** That's correct, yes. The points you earn can help towards unlocking some rewards - would you like to see them?
      - [Menu]: What would you like to say?
        - [Choice]: Sure, show me my progress towards rewards.
          - (Boss Assistance interface opens.)
        - [Choice]: That's all for now.
          - **Harlan:** No problems. Don't forget I taught you everything you know, Player.

#### Historical dialogue

- [Menu]: What would you like to talk about?
  - [Choice]: Who are you?
    - (above)
  - [Choice]: cond=If the player has 99 Defence|What is that cape you're wearing?
    - (above)
  - [Choice]: What's happening in Lumbridge?
    - (Condition: After the Lumbridge Rebuildathon:)
      - **Harlan:** Not long ago, there was a great battle near here, between Saradomin and Zamorak. It lasted for months!
      - **Harlan:** You can see the devastation around still. Even with the rebuilding effort, it will take years for Lumbridge to fully recover.
    - (Condition: After the Battle of Lumbridge but before the Lumbridge Rebuildathon:)
      - **Harlan:** You can see the devastation around still - it will take years for Lumbridge to recover.
      - **Harlan:** Not long ago, there was a great battle here, between Saradomin and Zamorak. It lasted for months!
      - **Harlan:** It is over now. I hope such fights never return to Lumbridge!
    - (Condition: During the Battle of Lumbridge:)
      - **Harlan:** Look around - you can see the devastation, all due to the fighting on the battlefield to the west.
      - **Harlan:** Not long after the death of Guthix, Saradomin and Zamorak returned to Gielinor, and started to fight right here in Lumbridge.
      - **Harlan:** Still, Lady Deathknell and myself try to train people so they can learn to defend themselves during these troubled times.
  - [Choice]: Talk about boss assistance.
    - (above)
