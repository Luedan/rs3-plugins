# Makeover Mage

- **Original Wiki Page**: [Transcript:Makeover Mage](https://runescape.wiki/w/Transcript%3AMakeover%20Mage)
- **Letter**: `M`

---

## Dialogue Transcript


### Standard dialogue

- **Makeover Mage:** Hello there! I am known as the Makeover Mage! I have spent many years researching magicks that can change your physical appearance.
- **Makeover Mage:** I call it a 'makeover'.<br>Would you like me to perform my magicks on you?
- [Menu]: Choose an option:
  - [Choice]: Tell me more about this 'makeover'.{{anchor|about-makeover}}
    - **Player:** Tell me more about this 'makeover'.
    - **Makeover Mage:** Why, of course! Basically, and I will explain this so that you understand it correctly.
    - **Makeover Mage:** I use my secret magical technique to melt your body down into a puddle of its elements.
    - **Makeover Mage:** When I have broken down all components of your body, I then rebuild it into the form I am thinking of.
    - **Makeover Mage:** Or, you know, something vaguely close enough, anyway.
    - **Player:** Uh...that doesn't sound particularly safe to me.
    - **Makeover Mage:** It's as safe as houses! Why, I have only had thirty-six major accidents this month!
    - **Makeover Mage:** So, what do you say? Feel like a change?
    - [Menu]: Select an Option
      - [Choice]: Sure, do it.
        - (below|sure)
      - [Choice]: No, thanks.
        - (below|no-thanks)
  - [Choice]: Sure, do it.{{anchor|sure}}
    - **Player:** Sure, do it.
    - **Makeover Mage:** You, of course, agree that if by some accident you are turned into a frog you have no rights for compensation or refund.
    - (opens=Makeover Mage)
    - (After changing appearance:)
    - (Condition: A random set of the following dialogues:)
      - (Condition: Set 1:)
        - **Makeover Mage:** Two arm, two legs, one head; it seems that spell finally worked okay.
        - (continue|thanks)
      - (Condition: Set 2:)
        - **Makeover Mage:** Hmm, you didn't feel any unexpected growths on your head just then, did you?
        - **Player:** Er, no?
        - **Makeover Mage:** Good, good! I was worried for a second there.
        - (continue|thanks)
      - (Condition: Set 3:)
        - **Makeover Mage:** Whew! That was lucky.
        - **Player:** What was?
        - **Makeover Mage:** Nothing! It's all fine! You seem alive anyway.
        - (continue|thanks)
      - (Condition: Set 4:)
        - **Makeover Mage:** Woah!
        - **Player:** What?
        - **Makeover Mage:** You still look human!
        - (continue|thanks)
    - {{anchor|thanks}}**Player:** Uh, thanks, I guess.
    - (Condition: If the player chooses the same appearance that they currently have:)
      - **Makeover Mage:** That is no different from what you already have. But  happy you've found your look.
  - [Choice]: No, thanks.{{anchor|no-thanks}}
    - **Player:** No, thanks. I'm happy as I am.
    - **Makeover Mage:** Well, I'm always happy to help if you change your mind. Is there anything else I can help you with
    - (initial|initial-options)
  - [Choice]: Can you give me some more pharmakos berries?|cond=During and after Land of the Goblins:
    - **Player:** Can you give me some more pharmakos berries?
    - (Condition: If the player doesn't already have any in their backpack or bank:)
      - **Makeover Mage:** Of course. You just need to combine them with toadflax in a vial and you'll have a potion to transform you into a goblin.
      - **Makeover Mage:** But they are hard for me to get, so please don't waste the potion.
      - **Makeover Mage:** Remember, it will reverse itself if you are in direct sunlight or if you perform a strenuous activity like fighting. Now, here are the berries.
      - (receives=pharmakos berries)
      - [bunch] of strange red berries.}}
    - (Condition: If the player has no space in backpack:)
      - **Makeover Mage:** Not until you free up some inventory space.
    - (Condition: If the player already has the berries in their backpack or bank:)
      - **Makeover Mage:** I think you already have some, so you just need to get some toadflax and make the potion.
  - [Choice]: [More...]
    - [Menu]: Choose an option:
      - [Choice]: Cool amulet! Can I have one?
        - **Player:** Cool amulet! Can I have one?
        - **Makeover Mage:** No problem, but please remember that the amulet I will sell you is only a copy of my own. It contains no magical powers and, as such, will only cost you 100 coins.
        - (Condition: If the player does not have enough money:)
          - **Player:** Oh, I don't have enough money for that.
        - (Condition: If the player has enough money:)
          - [Menu]: Select an Option
            - [Choice]: Sure, here you go.
              - **Player:** Sure, here you go.
              - (Condition: If the player has no space in backpack:)
                - **Makeover Mage:** Um...you don't seem to have room to take the amulet. Maybe you should buy it some other time.
                - **Player:**  Oh yeah, that's true.
              - (Condition: If the player has space in backpack:)
                - (removes=100 coins) (receives=yin yang amulet)
                - [You receive an amulet in exchange for 100 coins.]
            - [Choice]: No way! That's too expensive.
              - **Player:** No way! That's far too expensive.
              - **Makeover Mage:** That's fair enough, my jewellery is not to everyone's taste.
      - [Choice]: Could you do anything about my voice?
        - **Player:** Could you do anything about my voice?
        - **Makeover Mage:** It's not something I have a huge amount of experience in, but I've picked up a thing or two from my peers over the years. Would you like me to alter your voice?
        - [Menu]: Select an Option
          - [Choice]: Yes please!
            - **Player:** Yes please!
            - **Makeover Mage:** Well then, if you hold still this shouldn't hurt too much.
            - **Player:** You didn't mention it was going to hu-
            - **Player:** Ow!
            - **Player:** Wow! I sound so different, thanks!
            - **Makeover Mage:** Glad I could help. Was there anything else I could help with?
            - (initial|initial-options)
          - [Choice]: On second thoughts, I'll pass.
            - **Player:** On second thoughts, I'll pass.
            - **Makeover Mage:** Is there anything else I could help you with?
            - (initial|initial-options)
      - [Choice]: Can you make me a different colour?
        - **Makeover Mage:** Why, of course! I have a wide array of colours for you to choose from.
        - **Makeover Mage:** I also have some speciality colours for you should you wish to take advantage of them.
        - **Makeover Mage:** Furthermore I have some speciality potions avaiable for you to purchase should you want to take on a more vibrant colour. I call them 'Chameleon extract', they are quite handy if that is what you are after but they are one use potions.
        - **Makeover Mage:** So, what do you say? Feel like a change?
        - [Menu]: Select an Option
          - [Choice]: Sure, do it.
            - (above|sure)
          - [Choice]: I would like to buy some 'Chameleon extract'.
            - **Player:** I would like to buy some 'Chameleon extract'.
            - **Makeover Mage:** Excellent. I sell them in pack of 1, 3 or 6. How many would you like to purchase?
            - [Menu]: How many would you like to buy?
              - [Choice]: One.
                - (Purchase interface opens up for Chameleon Extract (x1) for 126 RuneCoins)
                - (Condition: If the 'confirm' button is pressed:)
                  - (receives=a chameleon extract)
                  - Your chameleon extract has been added to your bank.
                - (Condition: If the 'cancel' button is pressed:)
                  - (end)
              - [Choice]: Three.
                - (Purchase interface opens up for Chameleon Extract (x3) for 270 RuneCoins)
                - (Condition: If the 'confirm' button is pressed:)
                  - (receives=three chameleon extract)
                  - Your chameleon extract has been added to your bank.
                - (Condition: If the 'cancel' button is pressed:)
                  - (end)
              - [Choice]: Six.
                - (Purchase interface opens up for Chameleon Extract (x6) for 396 RuneCoins)
                - (Condition: If the 'confirm' button is pressed:)
                  - (receives=six chameleon extract)
                  - Your chameleon extract has been added to your bank.
                - (Condition: If the 'cancel' button is pressed:)
                  - (end)
              - [Choice]: None, I changed my mind.
                - **Player:** None, I have changed my mind.
                - **Makeover Mage:** Oh well, if you change your mind you know where to find them. Anything else you wanted to ask?
                - (initial|initial-options)
          - [Choice]: No, thanks.
            - (above|no-thanks)
      - [Choice]: [More...]
        - (initial|initial-options)

#### Using a Makeover voucher on the Makeover Mage

- [Menu]: Use your makeover voucher?
  - [Choice]: Yes
    - **Player:** Sure, do it. I am going to be using this voucher for a free makeover.
    - **Makeover Mage:** Ah, but of course! I didn't know those were still around. The service is free anyway.
    - (opens=Makeover Mage)
  - [Choice]: No
    - (end)

### After Evil Dave's Big Day Out

- **Makeover Mage:** Nice to see you again in your actual body. I assume everything went well on the whole getting-your-body-back front.
- **Player:** It did indeed!
- **Makeover Mage:** Great to hear – now what can I do for you?
- (above|initial-options)

### Overhead dialogue

- {{Qact|The mage casts a spell on themselves.}}
- {{Qact|The mage changes their own appearance.}}
- (Condition: If they went from male to female:)
  - **Makeover Mage:** {{RSChat|Ooh!}}
- (Condition: If they went from female to male:)
  - **Makeover Mage:** {{RSChat|Aha!}}
