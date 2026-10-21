# Wilfred

- **Original Wiki Page**: [Transcript:Wilfred](https://runescape.wiki/w/Transcript%3AWilfred)
- **Letter**: `W`

---

## Dialogue Transcript

{{incomplete|Dialogue for attempting to buy shard without having completed While Guthix Sleeps}}

### Standard dialogue


#### Before reaching Woodcutting level 99

- [Menu]: Select an Option
  - [Choice]: Who are you?
    - **Wilfred:** My name is Wilfred and I'm the best woodsman in Asgarnia! I've spent my life studying the best methods for woodcutting. That's why I have this cape, the Skillcape of Woodcutting.
  - [Choice]: What is that cape you're wearing?
    - **Wilfred:** This is a Skillcape of Woodcutting. Only a person who has achieved the highest possible level in a skill can wear one.
  - [Choice]: Can you help me with the sentinel outfits?
    - **Player:** Can you help me with the sentinel outfits?
    - (Condition: If the player can't receive sentinel fragments and hasn't unlocked the blueprint required to make the outfit pieces:)
      - **Wilfred:** At level 70 you can start to collect fragments to make elite skilling outfits. When you get to that level you will automatically start collecting fragments. Then you can use them with a blueprint to make yourself any remaining elite outfit pieces for this skill.
    - (Condition: If the player can receive sentinel fragments but hasn't unlocked the blueprint required to make the outfit pieces:)
      - **Wilfred:** You are set up to receive fragments. When you get to level 80 you will be able to create outfit pieces.
    - (Condition: If the player can receive sentinel fragments and has unlocked the blueprint required to make the outfit pieces:)
      - **Wilfred:** You are set up to receive fragments. When you have 3600 fragments you can use them to create an elite outfit piece.
      - **Wilfred:** Simply go to an Invention workbench to create the pieces.
    - (Condition: If the player owns the full nature's sentinel outfit or all of the outfit pieces required to craft it:)
      - **Wilfred:** You have already created all of the possible outfit pieces. I will make sure you do not receive any further fragments.
      - **Wilfred:** Remember you can combine the base outfit pieces to make the high tier versions, to get the additional benefits.
  - [Choice]: Ask about something else.
    - (continue|More information)

#### After reaching Woodcutting level 99

<!-- commented-out dialogue below is (temporarily?) missing in-game, likely due to bugs introduced with The Spirit of Accomplishment -->
- **Wilfred:** Wow! It's not often I meet somebody as accomplished as you in Woodcutting! Seeing as you're so skilled, maybe you are interested in buying a Skillcape of Woodcutting?
- [Menu]: Select an Option
  - [Choice]: No, thanks.
    - **Player:** No, thanks.
    - **Wilfred:** Okay. Come back to me if you change your mind.
  - [Choice]: Yes, please.
    - (Condition: If the player has a ring of charos (a) equipped:)
      - **Wilfred:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
    - ((Otherwise:))
<!--**** **Wilfred:** Anybody who has spent as much time cutting trees as you deserves the right to own one. That'll be 99,000 coins, please.-->
      - ((The price of the cape is 99,000 coins.))
    - [Menu]: Choose an option:
      - [Choice]: [99,000/92,000] coins? That's much too expensive.
<!--***** **Wilfred:** Not at all; there are many other adventurers who would love the opportunity to purchase such a prestigious item! You can find me here if you change your mind.-->
        - **Player:** I know where to find you if I change my mind.
      - [Choice]: I think I have the money right here, actually.
        - [99,000/92,000] coins have been removed from your money pouch.
        - (receives=a (trimmed or untrimmed) Woodcutting cape and a Woodcutting hood)
        - **Wilfred:** Excellent! Wear that cape with pride my friend.
      - [Choice]: cond=If the player has virtual level 120 Woodcutting:|I've mastered this skill. Is there anything else?
        - **Wilfred:** There is something...though I have kept it a secret for a very long time. It is something that can only be worn by a true master.
        - **Wilfred:** Not even I can wear it - that's how hard it is to achieve.
        - **Wilfred:** You say you're a master. Stand straight, let me take a look at you...
        - **Wilfred:** You...really have mastered it. What an honour! It would be my pleasure to sell you a Woodcutting master cape.
        - [Menu]: Buy Woodcutting master cape for 120,000 coins?
          - [Choice]: Yes.
            - (Condition: Without free backpack space:)
              - **Wilfred:** You do not have enough room in your backpack. Please come back when you have some more.
            - (Condition: With free backpack space:)
              - (Condition: Without 120,000 coins:)
                - You do not have enough money to purchase this cape.
                - (pop-up)
                  - {{Pop-up|You do not have enough money to purchase this cape.}}
              - (Condition: With 120,000 coins:)
                - 120,000 coins have been removed from your money pouch.
                - (removes=120,000 coins) (receives=Woodcutting master cape)
                - {{Qact|Master cape music plays.}}
          - [Choice]: No.
            - (end)
  - [Choice]: I've noticed there are a couple of versions of each skillcape.
    - **Wilfred** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
    - (Condition: If the player is currently using the newer version of the Woodcutting skillcape:)
      - **Wilfred:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
      - [Menu]: Select an Option
        - [Choice]: Yes, I would like to wear the old version of the skillcape.
          - **Wilfred:** Would you like to wear the old model for just this cape, or for the Quest Cape and all of the skillcapes you own?
          - [Menu]: Select an Option
            - [Choice]: I would just like to change the Woodcutting skillcape.
              - **Wilfred:** No problem, you will now use the older model for your Woodcutting skillcape.
            - [Choice]: I would like to change all my skillcapes.
              - **Wilfred:** No problem, you will now use the older model for all of your skillcapes!
            - [Choice]: I've changed my mind!
              - (end)
        - [Choice]: No, thank you.
          - **Wilfred:** Great! I'm glad you're enjoying our new version!
    - (Condition: If the player is currently using the old version of the Woodcutting skillcape:)
      - **Wilfred:** It looks like you're currently using the old model for your Woodcutting skillcape. Would you like to change to the newer one?
      - [Menu]: Select an Option
        - [Choice]: Yes, I would like to wear the new version of the skillcape.
          - **Wilfred:** Would you like to wear the newer model for just this cape, or all of the skillcapes you own?
          - [Menu]: Select an Option
            - [Choice]: I would just like to change the Woodcutting skillcape.
              - **Wilfred:** No problem, you will now use the newer model for your Woodcutting skillcape.
            - [Choice]: I would like to change all my skillcapes.
              - **Wilfred:** No problem, you will now use the newer model for all of your skillcapes!
            - [Choice]: I've changed my mind!
              - (end)
        - [Choice]: No, thank you.
          - **Wilfred:** Great! I'm glad you're still enjoying the old version!
          - (Condition: If the player does not have all their skillcapes set to the old version:)
            - **Wilfred:** If you want, I can make it so you use the old model for all of the skillcapes you own!
            - [Menu]: Select an Option
              - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
                - **Wilfred:** Great, you will now use the old model for all of your skillcapes!
              - [Choice]: No, thanks.
                - (end)
  - [Choice]: Can you help me with the sentinel outfits?
    - (above|outfits)
  - [Choice]: Ask about something else.
    - (continue|More information)

#### More information

- [Menu]: Can you tell me about...
  - [Choice]: Elder trees.
    - **Player:** Can you tell me about elder trees?
    - **Wilfred:** Certainly, I'd be happy to share what I've gathered during my years of studying tree with you.
    - **Wilfred:** There are a handful of Elder trees that I know of and they've been around a lot longer than even I can remember.
    - **Wilfred:** The outer bark of the main trunk is very tough but some of the higher branches are easier to cut through with enough skill.
    - **Wilfred:** They're very slow growing and take a bit longer than most other trees to regrow.
    - **Wilfred:** The nearest Elder tree I know of from here is just south east of Falador near the ivy.
    - **Wilfred:** In the past, I've cut that elder tree down and whilst waiting for it to grow back I've chopped away at other nearby trees and the ivy.
    - **Wilfred:** That said, if you found some other elder trees, you might find moving between them more effective giving the others you've already cut down a chance to regrow.
    - **Player** Thanks, that's been very helpful.
  - [Choice]: Crystal trees.
    - **Player** Can you tell me about Crystal trees?
    - **Wilfred:** Sure thing, though crystal trees are somewhat different to normal trees that's for sure.
    - **Wilfred:** The crystal tree that I know of just west of Falador near the Dark Wizard's tower, seems to grow shards of crystal around it at various times.
    - **Wilfred:** The main tree can't be cut with any axe I've tried, but the shards of crystal that occasionally grow around the  edges can be shattered with a decent axe.
    - **Wilfred:** After years of studying it, I've also noticed that when the shards are present the tree points directly upwards.
    - **Wilfred:** However, upon closer inspection when the shards aren't growing around it the tree leans very slightly in a handful of different directions.
    - **Wilfred:** Perhaps you can work out why the shards only appear occasionally and what the different directions mean.
    - **Wilfred:** On occasion I even managed to chip off some crystal geodes that were encased within the shards to find some hidden gems inside.
    - **Wilfred:** A few that I broke open had some other strange objects in them as well, perhaps you'll be able to shed some light on the matter if you find any.
    - **Player:** How interesting, thanks.
  - [Choice]: Hatchet of ember and glade.
    - (Condition: If the player doesn't meet the requirements:)
      - **Wilfred:** I have in my possession a powerful artefact that will fuse an imcando hatchet to a crystal hatchet, combining the best elements of dwarven and elven craftsmanship.
      - **Wilfred:** However, I will only bequeath it to one who is champion to both the dwarves and the elves.
      - **Wilfred:** Some day, I foresee you will be a kingmaker amidst chaos.
      - **Wilfred:** But your time has not yet come.
    - (Condition: If the player has purchased Shard of the Lumberjack before:)
      - **Player:** You got any more of those Shards of the Lumberjack?
      - **Wilfred:** Again? How many questionably magic sticks can one person need?
      - (continue|BuyShard)
    - **Player** Do you know of a way I can upgrade my imcando hatchet?
    - **Wilfred:** How fortuitous. I have in my possession the Shard of the Lumberjack. This powerful artefact will fuse an imcando hatchet to a crystal hatchet, combining the best elements of dwarven and elven craftsmanship.
    - **Player** And you're going to give me this artefact for free, yes? Given I've heroically saved the world on multiple occasions?
    - **Wilfred:** I will sell you the Shard of the Lumberjack for precisely one million coins.
    - [Menu]: Select an Option|anchor=BuyShard
      - [Choice]: Buy Shard of the Lumberjack : 1,000,000 (1M) coins.
        - (Condition: Without 1,000,000 coins:)
          - **Wilfred:** Sorry, friend. You don't seem to have sufficient coinage.
        - (Condition: With at least 1,000,000 coins:)
          - (Condition: Without backpack space:)
            - **Wilfred:** Sorry, friend. Your backpack is full.
          - (Condition: With backpack space:)
            - (removes=1,000,000 coins) (receives=Shard of the Lumberjack)
            - (Condition: Without having bought a Shard of Lumberjack before:)
              - [pic=Shard of the Lumberjack detail.png]
            - (Condition: Having bought a Shard of Lumberjack before:)
              - [pic=Shard of the Lumberjack detail.png]
      - [Choice]: I'll leave it for now, thanks.
        - You decide against making a purchase.
        - (previous2|More information)
  - [Choice]: Never mind.
    - (end)
