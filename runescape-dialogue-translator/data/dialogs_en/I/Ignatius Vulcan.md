# Ignatius Vulcan

- **Original Wiki Page**: [Transcript:Ignatius Vulcan](https://runescape.wiki/w/Transcript%3AIgnatius%20Vulcan)
- **Letter**: `I`

---

## Dialogue Transcript


### Without level 99 Firemaking

- **Ignatius Vulcan:** Can I help you at all?
- [Menu]: Select an Option
  - [Choice]: Who are you?
    - **Player:** Who are you?
    - **Ignatius Vulcan:** My name is Ignatius Vulcan. Once I was - like you - an adventurer, but that was before I realised the beauty and power of flame! Just look at this...
    - {{qact|Ignatius lights a fire under the player.}}
    - **Player:** {{RSChat|Yeeouch!}}
    - **Ignatius Vulcan:** Stare into the flame and witness the purity and power of fire! As my attraction to flame grew, so did my skills at firelighting. I began to neglect my combat skills, my Mining skills and my questing. Who needs such mundane skills
    - **Ignatius Vulcan:** when one can harness the power of fire? After years of practice I am now the acknowledged Master of Flame! Everything must be purified by fire!
    - **Player:** Okaaaay! Err, I'll be going now. Umm, get better soon.
  - [Choice]: Do you have anything for trade?
    - **Player:** Do you have anything for trade?
    - (opens=Ignatius's Hot Deals)
  - [Choice]: What is that cape you're wearing?
    - **Player:** What is that cape you're wearing?
    - **Ignatius Vulcan:** This is a Skillcape of Firemaking. I was given it in recognition of my skill as the greatest firemaker in the lands! I AM the Master of Flame!
    - **Player:** Hmm, I'll be going now. Keep a sharp look out for those men with their white jackets!
  - [Choice]: No, thanks.
    - **Player:** No, thanks.
    - **Ignatius Vulcan:** Okay, keep the fire burning.

### With level 99 Firemaking

- **Ignatius Vulcan:** Can I help you at all?
- [Menu]: Select an Option
  - [Choice]: Who are you?
    - (above)
  - [Choice]: Do you have anything for trade?
    - (above)
  - [Choice]: Can I buy a Skillcape of Firemaking?
    - (Condition: If the player has a ring of charos (a) equipped:)
      - **Ignatius Vulcan:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
      - [Menu]: Choose an option:
        - [Choice]: 92,000 coins? That's much too expensive.
          - **Player:** I know where to find you if I change my mind.
        - [Choice]: I think I have the money right here, actually.
          - (Condition: If the player has no backpack space:)
            - **Ignatius Vulcan:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some backpack space before I can sell you one.
          - (Condition: If the player does not have enough money:)
            - **Player:** But unfortunately, I was mistaken.
            - **Ignatius Vulcan:** Well, come back and see me when you do.
          - (Condition: If the player has enough money:)
            - (receives=firemaking cape and firemaking hood) (removes=92,000 coins)
            - **Ignatius Vulcan:** Excellent! Wear that cape with pride my friend.
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
            - (receives=firemaking cape and firemaking hood) (removes=99,000 coins)
            - **Ignatius Vulcan:** Excellent! Wear that cape with pride my friend.
        - [Choice]: cond=With virtual level 120 Firemaking:|I've mastered this skill. Is there anything else?
          - **Ignatius Vulcan:** There is something...though I have kept it a secret for a very long time. It is something that can only be worn by a true master.
          - **Ignatius Vulcan:** Not even I can wear it - that's how hard it is to achieve.
          - **Ignatius Vulcan:** You say you're a master. Stand straight, let me take a look at you.
          - **Ignatius Vulcan:** You...really have mastered it. What an honour! It would be my pleasure to sell you a Firemaking master cape.
          - [Menu]: Buy Firemaking master cape for 120,000 coins?
            - [Choice]: Yes.
              - (Condition: Without free backpack space:)
                - **Ignatius Vulcan:** You do not have enough room in your backpack. Please come back when you have some more.
              - (Condition: With free backpack space:)
                - (Condition: Without 120,000 coins:)
                  - You do not have enough money to purchase this cape.
                  - (pop-up)
                    - {{Pop-up|You do not have enough money to purchase this cape.|warning=yes}}
                - (Condition: With 120,000 coins:)
                  - (removes=120,000 coins) (receives=Firemaking master cape)
                  - {{Qact|Master cape music plays.}}
            - [Choice]: No.
              - (end)
  - [Choice]: I've noticed there are a couple of versions of each skillcape.
    - **Ignatius Vulcan:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
    - (Condition: If you use the old model:)
      - **Ignatius Vulcan:** It looks like you're currently using the old model for your Firemaking skillcape. Would you like to change to the newer one?
      - (continue)
    - (Condition: If you use the new model:)
      - **Ignatius Vulcan:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
      - (continue)
    - [Menu]: Select an option
      - [Choice]: Yes, I would like to wear the [new/old] version of the skillcape.
        - **Ignatius Vulcan:** Would you like to wear the [old/newer] model for just this cape, or for the Quest Cape and all of the skillcapes you own?
        - [Menu]: Select an option
          - [Choice]: I would just like to change the Firemaking skillcape.
            - **Ignatius Vulcan:** No problem, you will now use the [older/newer] model for your Firemaking skillcape.
          - [Choice]: I would like to change all my skillcapes.
            - **Ignatius Vulcan:** No problem, you will now use the [older/newer] model for all of your skillcapes!
          - [Choice]: I've changed my mind!
            - (end)
      - [Choice]: No, thank you.
        - **Ignatius Vulcan:** Great! I'm glad you're still enjoying the [old/new] version!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Ignatius Vulcan:** If you want, I can make it so you use the old model for all of the skillcapes you own.
          - [Menu]: Select an option
            - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
              - **Ignatius Vulcan:** Great, you will now use the old model for all of your skillcapes!
            - [Choice]: No, thanks.
              - (end)
  - [Choice]: No, thanks.
    - **Player:** No, thanks.
    - **Ignatius Vulcan:** Okay, keep the fire burning.
