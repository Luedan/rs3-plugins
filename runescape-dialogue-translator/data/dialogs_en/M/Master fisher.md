# Master fisher

- **Original Wiki Page**: [Transcript:Master fisher](https://runescape.wiki/w/Transcript%3AMaster%20fisher)
- **Letter**: `M`

---

## Dialogue Transcript


### In the Fishing Guild


#### Talking to him

- **Master fisher:** Hello, welcome to the Fishing Guild. Please feel free to make use of any of our facilities.
- [Menu]: What would you like to ask about?
  - [Choice]: Can you tell me about the Fishing skillcape.
    - (Condition: If the player is below level 99 Fishing:)
      - **Master fisher:** I'm happy to, my friend. This beautiful cape was presented to me in recognition of my skills and experience as a fisherman and I was asked to be the head of this guild at the same time. As the best fisherman in the guild it is my duty to control who has access to the guild and to say who can buy similar skillcapes.
    - (Condition: If the player is at least level 99 Fishing)
      - (Condition: If the player has a ring of charos (a) equipped:)
        - **Master fisher:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
        - [Menu]: Choose an option:
          - [Choice]: 92,000 coins? That's much too expensive.
            - **Player:** I know where to find you if I change my mind.
          - [Choice]: I think I have the money right here, actually.
            - (Condition: If the player has no backpack space:)
              - **Master fisher:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some backpack space before I can sell you one.
            - (Condition: If the player does not have enough money:)
              - **Player:** But unfortunately, I was mistaken.
              - **Master fisher:** Well, come back and see me when you do.
            - (Condition: If the player has enough money:)
              - (receives=fishing cape and fishing hood) (removes=92,000 coins)
              - **Master fisher:** Excellent! Wear that cape with pride my friend.
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
              - (receives=fishing cape and fishing hood) (removes=99,000 coins)
              - **Master fisher:** Excellent! Wear that cape with pride my friend.
          - [Choice]: cond=With 120 virtual Fishing:|I've mastered this skill. Is there anything else?
            - **Master fisher:** There is something...though I have kept it a secret for a very long time. It is something that can only be worn by a true master.
            - **Master fisher:** Not even I can wear it - that's how hard it is to achieve.
            - **Master fisher:** You say you're a master. Stand straight, let me take a look at you...
            - **Master fisher:** You...really have mastered it. What an honour! It would be my pleasure to sell you a Fishing master cape.
            - [Menu]: Buy Fishing master cape for 120,000 coins?
              - [Choice]: Yes.
                - (Condition: Without free backpack space:)
                  - **Master fisher:** You do not have enough room in your backpack. Please come back when you have some more.
                - (Condition: With free backpack space:)
                  - (Condition: Without 120,000 coins:)
                    - You do not have enough money to purchase this cape.
                    - (pop-up)
                      - {{Pop-up|You do not have enough money to purchase this cape.|warning=yes}}
                  - (Condition: With 120,000 coins:)
                    - (removes=120,000 coins) (receives=Fishing master cape)
                    - {{Qact|Master cape music plays.}}
              - [Choice]: No.
                - (end)
  - [Choice]: Can you help me with the shark outfits?
    - **Player:** Can you help me with the shark outfits?
    - ((If the player can't receive shark fragments and hasn't unlocked the blueprint required to make the outfit pieces:))
      - **Master fisher:** At level 70 you can start to collect fragments to make elite skilling outfits. When you get to that level you will automatically start collecting fragments. Then you can use them with a blueprint to make yourself any remaining elite outfit pieces for this skill.
    - ((If the player can receive shark fragments but hasn't unlocked the blueprint required to make the outfit pieces:))
      - **Master fisher:** You are set up to receive fragments. When you get to level 80 you will be able to create outfit pieces.
    - ((If the player can receive shark fragments and has unlocked the blueprint required to make the outfit pieces:))
      - **Master fisher:** You are set up to receive fragments. When you have 3600 fragments you can use them to create an elite outfit piece. Simply go to an Invention workbench to create the pieces.
    - ((If the player owns the full fury shark outfit, or all of the outfit pieces required to craft it:))
      - **Master fisher:** You have already created all of the possible outfit pieces. I will make sure you do not receive any further fragments. Remember you can combine the base outfit pieces to make the high tier versions, to get the additional benefits.
  - [Choice]: I've noticed there are a couple of versions of each skillcape.
    - **Master fisher:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
    - (Condition: If you use the old model:)
      - **Master fisher:** It looks like you're currently using the old model for your Fishing skillcape. Would you like to change to the newer one?
      - (continue)
    - (Condition: If you use the new model:)
      - **Master fisher:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
      - (continue)
    - [Menu]: Select an option
      - [Choice]: Yes, I would like to wear the [new/old] version of the skillcape.
        - **Master fisher:** Would you like to wear the [old/newer] model for just this cape, or for the Quest Cape and all of the skillcapes you own?
        - [Menu]: Select an option
          - [Choice]: I would just like to change the fishing skillcape.
            - **Master fisher:** No problem, you will now use the [older/newer] model for your fishing skillcape.
          - [Choice]: I would like to change all my skillcapes.
            - **Master fisher:** No problem, you will now use the [older/newer] model for all of your skillcapes!
          - [Choice]: I've changed my mind!
            - (end)
      - [Choice]: No, thank you.
        - **Master fisher:** Great! I'm glad you're still enjoying the [old/new] version!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Master fisher:** If you want, I can make it so you use the old model for all of the skillcapes you own.
          - [Menu]: Select an option
            - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
              - **Master fisher:** Great, you will now use the old model for all of your skillcapes!
            - [Choice]: No, thanks.
              - (end)
  - [Choice]: Nothing.
    - (end)

#### Pickpocket option

- (Before and after Deadliest Catch:)
- You've no reason to pickpocket him.
