# Head chef

- **Original Wiki Page**: [Transcript:Head chef](https://runescape.wiki/w/Transcript%3AHead%20chef)
- **Letter**: `H`

---

## Dialogue Transcript


### Outside the Cooks' Guild


#### Attempting to enter without 32 Cooking

- You need a Cooking level of 32 to enter the Chef's Guild.
- ((Repeated in a pop-up:))
  - You need a Cooking level of 32 to enter the Chef's Guild.
- **Head chef:** Sorry. Only the finest chefs are allowed in here. Get your Cooking level up to 32 and come back wearing a chef's hat.

#### Attempting to enter with level 32 Cooking but without a chef's hat

- **Head chef:** You can't come in here unless you're wearing a chef's hat, or something like that.

#### Entering with the hard Varrock achievements complete

- **Head chef:** A master explorer of Varrock! You are more than welcome in here, my friend!

### Inside the Cooks' Guild


#### Talking to the head chef


##### Without level 99 Cooking

- **Head chef:** Hello, welcome to the Cooking Guild. Only accomplished chefs and cooks are allowed in here. Feel free to use any of our facilities.
- [Menu]: Select an Option
  - [Choice]: Talk about 'Chef's Assistant'. {{anchor|cheesecake}}
    - (Condition: Before Chef's Assistant:)
      - (see|Chef's Assistant#Starting the quest)
    - (Condition: After Chef's Assistant:)
      - (see|Chef's Assistant#Post-Quest Dialogue)
  - [Choice]: cond=If the player is below 99 Cooking|Nice cape you're wearing!
    - **Player:** Nice cape, you're wearing!
    - **Head Chef:** Thank you! It's my most prized possession, it's a Skillcape of Cooking; it shows that I've achieved level 99 Cooking and am one of the best chefs in the world!
  - [Choice]: Thanks, bye.
    - **Player:** Thanks, bye.

##### With level 99 Cooking

- **Head chef:** Hello, welcome to the Cooking Guild. It's always great to have such an accomplished chef visit us. Say, would you be interested in a Skillcape of Cooking? They're only available to master chefs.
- [Menu]: Select an Option
  - [Choice]: Talk about 'Chef's Assistant'.
    - (above|cheesecake)
  - [Choice]: No thanks.
    - **Player:** No thanks.
    - **Head chef:** Okay, come back to me if you change your mind.
  - [Choice]: Yes please.
    - (Condition: If the player is on a free-to-play world:)
      - **Head Chef:** I'm sorry, I can't sell you one here. Try talking to me on a members' world.
    - (Condition: If the player is on a members' world:)
      - (Condition: If the player has a ring of charos (a) equipped:)
        - **Head chef:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
        - [Menu]: Choose an option:
          - [Choice]: 92,000 coins? That's much too expensive.
            - **Player:** I know where to find you if I change my mind.
          - [Choice]: I think I have the money right here, actually.
            - (Condition: If the player has no backpack space:)
              - **Head chef:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some backpack space before I can sell you one.
            - (Condition: If the player does not have enough money:)
              - **Player:** But unfortunately, I was mistaken.
              - **Head chef:** Well, come back and see me when you do.
            - (Condition: If the player has enough money:)
              - (receives=cooking cape and cooking hood) (removes=92,000 coins)
              - **Head chef:** Excellent! Wear that cape with pride my friend.
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
              - (receives=cooking cape and cooking hood) (removes=99,000 coins)
              - **Head chef:** Excellent! Wear that cape with pride my friend.
  - [Choice]: I've noticed there are a couple of versions of each skillcape.
    - **Head chef:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
    - (Condition: If you use the old model:)
      - **Head chef:** It looks like you're currently using the old model for your Prayer skillcape. Would you like to change to the newer one?
      - (continue)
    - (Condition: If you use the new model:)
      - **Head chef:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
      - (continue)
    - [Menu]: Select an option
      - [Choice]: Yes, I would like to wear the [new/old] version of the skillcape.
        - **Head chef:** Would you like to wear the [old/newer] model for just this cape, or for the Quest Cape and all of the skillcapes you own?
        - [Menu]: Select an option
          - [Choice]: I would just like to change the Prayer skillcape.
            - **Head chef:** No problem, you will now use the [older/newer] model for your Prayer skillcape.
          - [Choice]: I would like to change all my skillcapes.
            - **Head chef:** No problem, you will now use the [older/newer] model for all of your skillcapes!
          - [Choice]: I've changed my mind!
            - (end)
      - [Choice]: No, thank you.
        - **Head chef:** Great! I'm glad you're still enjoying the [old/new] version!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Head chef:** If you want, I can make it so you use the old model for all of the skillcapes you own.
          - [Menu]: Select an option
            - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
              - **Head chef:** Great, you will now use the old model for all of your skillcapes!
            - [Choice]: No, thanks.
              - (end)

#### Attempting to enter the bank room without the hard Varrock achievements

- **Head chef:** Hey, you can't go in there.
- **Player:** Oh, why not?
- **Head chef:** That's for Varrock's best explorers only, I'm afraid.
- **Player:** Oh, I see. How do I become such an explorer?
- **Head chef:** Hmm, well, from what I hear, it is given to people who have proven themselves a benefit to the city by completing all of the easy, medium and hard set Tasks in Varrock.
- (Condition: If the player has acquired the Varrock armour:)
  - **Player:** I have the Varrock armour, though.
  - **Head chef:** Yes, but it looks like you have some more tasks to perform before we can trust you in this bank. Come back when you have completed all of the hard tasks and can prove it.
- (Condition: If the player is wearing the Varrock armour:)
  - **Player:** I'm wearing the Varrock armour, though.
  - **Head chef:** Yes, but it looks like you have some more tasks to perform before we can trust you in this bank. Come back when you have completed all of the hard tasks and can prove it.
