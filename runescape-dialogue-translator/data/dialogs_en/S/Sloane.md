# Sloane

- **Original Wiki Page**: [Transcript:Sloane](https://runescape.wiki/w/Transcript%3ASloane)
- **Letter**: `S`

---

## Dialogue Transcript


### Standard dialogue

- **Sloane:** Ahhh, hello there, Player.
- (Condition: If the player has 99 Strength:)
  - **Sloane:** Ah, but I can see you are already strong as is possible! Perhaps you have come to me to purchase a Skillcape of Strength, and thus join the elite few who have mastered this exacting skill?
  - (continue)
- [Menu]: Select an Option
  - [Choice]: cond=If the player is below 99 Strength:|Can you tell me a bit about skillcapes?
    - **Player:** Can you tell me a bit about skillcapes?
    - **Sloane:** Sure. You can buy a skillcape when you reach level 99 in a skill. Apart from boosting your statistics in that skill, they can also be used to perform some pretty amazing emotes! Is there anything else you would like to know?
    - (initial)
  - [Choice]: |cond=If the player has 99 Strength:|May I buy a Skillcape of Strength, please?
    - (Condition: If the player has a ring of charos (a) equipped:)
      - **Sloane:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
      - [Menu]: Choose an option:
        - [Choice]: 92,000 coins? That's much too expensive.
          - **Player:** I know where to find you if I change my mind.
        - [Choice]: I think I have the money right here, actually.
          - (Condition: If the player has no backpack space:)
            - **Sloane:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some backpack space before I can sell you one.
          - (Condition: If the player does not have enough money:)
            - **Player:** But unfortunately, I was mistaken.
            - **Sloane:** Well, come back and see me when you do.
          - (Condition: If the player has enough money:)
            - (receives=Strength cape and Strength hood) (removes=92,000 coins)
            - **Sloane:** Excellent! Wear that cape with pride my friend.
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
            - (receives=Strength cape and Strength hood) (removes=99,000 coins)
            - **Sloane:** Excellent! Wear that cape with pride my friend.
  - [Choice]: I've noticed there are a couple of versions of each skillcape.
    - **Sloane:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
    - (Condition: If you use the old model:)
      - **Sloane:** It looks like you're currently using the old model for your Strength skillcape. Would you like to change to the newer one?
      - (continue)
    - (Condition: If you use the new model:)
      - **Sloane:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
      - (continue)
    - [Menu]: Select an Option
      - [Choice]: Yes, I would like to wear the [new/old] version of the skillcape.
        - **Sloane:** Would you like to wear the [old/newer] model for just this cape, or for the Quest Cape and all of the skillcapes you own?
        - [Menu]: Select an Option
          - [Choice]: I would just like to change the Strength skillcape.
            - **Sloane:** No problem, you will now use the [older/newer] model for your Strength skillcape.
          - [Choice]: I would like to change all my skillcapes.
            - **Sloane:** No problem, you will now use the [older/newer] model for all of your skillcapes!
          - [Choice]: I've changed my mind!
            - (end)
      - [Choice]: No, thank you.
        - **Sloane:** Great! I'm glad you're still enjoying the [old/new] version!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Sloane:** If you want, I can make it so you use the old model for all of the skillcapes you own.
          - [Menu]: Select an Option
            - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
              - **Sloane:** Great, you will now use the old model for all of your skillcapes!
            - [Choice]: No, thanks.
              - (end)
  - [Choice]: What can I do here?
    - **Player:** What can I do here?
    - **Sloane:** Ahh, the shot put is a great test of strength and can be quite rewarding. Mind you do it properly, though, you might want to dust your hands with some powdery substance first. It'll give better grip.
    - **Player:** I'll remember that. What should I use?
    - **Sloane:**I personally prefer ground ashes, it makes a nice fine powder and gives some really good grip.
    - **Player:** Okay, what else?
    - **Sloane:** Basically you'll need to go in there, make sure you've got nothing cluttering up your hands, pick up a shot and throw it. Depending upon your technique, you can get quite long throws.
    - **Player:** What was your best?
    - **Sloane:** Ahh, that would be telling.
    - (initial)
  - [Choice]: That's a big axe!
    - **Player:** That's a big axe!
    - **Sloane:** Yes, indeed, it is. Have to be mighty strong to wield it too.
    - **Player:** But you don't look that strong!
    - **Sloane:** Maybe, maybe not, but I still had to beat a Barbarian to get it. Mind you, usually they don't part with them. This was an unusual circumstance.
    - **Player:** Oh?
    - **Sloane:** I bet him he couldn't catch a squirrel whilst still holding his axe but that I could... and that if I won I'd get his axe.
    - **Player:** What happened?
    - **Sloane:** He went running after the squirrel... nearly caught it too... it shot up a tree and he tried to climb up it, only got a bit tangled up with his axe cause he couldn't hang on to it at the same time and... he fell out of the tree.
    - **Sloane:** Then it was my turn....
    - **Sloane:** I simply went and chopped the tree down with this big old axe, still holding it. The squirrel was so petrified it simply jumped straight out of the tree onto me. I won the axe and let the poor creature go!
    - **Player:** I sense a moral in there somewhere.
    - **Sloane:** Aye indeed. Brawn isn't all you need to wield a big axe, brains are required too!
    - (initial)
  - [Choice]: Bye!
    - **Player:** Bye!
    - {{qact|Sloane does the Bow emote.}}
    - **Sloane:** Be well, warrior Player.

### In City of Um


#### Saluting Sloane

- {{Qact|The player salutes to Sloane and he salutes back.}}
- **Player:** Yadech continues on your legacy.
