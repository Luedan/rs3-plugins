# Fairy Nuff

- **Original Wiki Page**: [Transcript:Fairy Nuff](https://runescape.wiki/w/Transcript%3AFairy%20Nuff)
- **Letter**: `F`

---

## Dialogue Transcript


### Before A Fairy Tale I - Growing Pains


#### First time

- **Fairy Nuff:** Hello, can I help you at all?
- [Menu]: Select an Option
  - [Choice]: What do you do around here?
    - **Player:** What do you do around here?
    - **Fairy Nuff:** Oh, I'm the resident healer. My name is Nuff, Fairy Nuff. Who are you?
    - **Player:** My name is Player.
    - **Fairy Nuff:** Pleased to meet you, Player. As I was saying, I'm the healer in Zanaris. I graduated over 200 human years ago. Look, there's my Advanced Healing Certificate on the wall. I never go anywhere without it. It's my job to look after the sick, wounded or dying fairies around here. Of course, fairies being magical by nature, not many of them get hurt, so I don't normally have much to do.
    - **Player:** What about healing humans? Lots of adventurers must get hurt fighting the Otherworldly beings.
    - **Fairy Nuff:** Yes, they do. Silly isn't it? I do use my healing magic on humans sometimes, but I don't like them attacking our other guests, so I charge them for the service.
    - **Player:** How much do you charge to heal someone, then?
    - **Fairy Nuff:** Well, the gold that you humans are so fond of has no real value in Zanaris, so I ask my patients to pay me in gems. I will heal 40 life points for an opal, 50 life points for either a sapphire or a piece of jade, 70 life points for an emerald or red topaz, 90 for a ruby and 110 for a diamond.
    - **Player:** Only 110 life points for a diamond? Doesn't that seem a bit steep?
    - **Fairy Nuff:** Maybe to you, but you'd be surprised how many adventurers are willing to pay those prices.
  - [Choice]: No thanks. Just looking around.
    - **Player:** No thanks. Just looking around.
    - **Fairy Nuff:** Okay. If you want to know anything, just ask.

#### Subsequent times

- **Fairy Nuff:** Hello Player, do you need any assistance?
- [Menu]: Select an Option
  - [Choice]: Yes, please. I need healing.
    - **Player:** Yes, please. I need healing.
    - **Fairy Nuff:** Sure, how many life points would you like me to heal?
    - [Menu]: Select an Option
      - [Choice]: 40 Life points.
        - **Player:** 40 Life points.
        - **Fairy Nuff:** That will cost you 1 opal.
        - [Menu]: Select an Option
          - [Choice]: All right.
            - **Player:** All right.
            - (Condition: If the player has an opal in the backpack:)
              - (removes=opal)
              - {{Qact|The player is healed a maximum of 40 life points.}}
            - (Condition: If the player doesn't have an opal in the backpack:)
              - **Fairy Nuff:** You don't have  to pay me!
              - **Player:** Whoops, sorry.
          - [Choice]: On second thoughts, no thanks.
            - **Player:** On second thoughts, no thanks.
            - **Fairy Nuff:** Okay, suit yourself.
      - [Choice]: 50 Life points.
        - **Player:** 50 Life points.
        - **Fairy Nuff:** That will cost you 1 sapphire or 1 piece of jade.
        - [Menu]: Select an Option
          - [Choice]: All right.
            - **Player:** All right.
            - (Condition: If the player has a sapphire or jade in the backpack:)
              - (removes=sapphire or jade)
              - {{Qact|The player is healed a maximum of 50 life points.}}
            - (Condition: If the player doesn't have a sapphire or jade in the backpack:)
              - **Fairy Nuff:** You don't have a sapphire or a piece of jade with you!
              - **Player:** Whoops, sorry.
          - [Choice]: On second thoughts, no thanks.
            - **Player:** On second thoughts, no thanks.
            - **Fairy Nuff:** Okay, suit yourself.
      - [Choice]: 70 Life points.
        - **Player:** 70 Life points.
        - **Fairy Nuff:** That will cost you 1 emerald or 1 red topaz.
        - [Menu]: Select an Option
          - [Choice]: All right.
            - **Player:** All right.
            - (Condition: If the player has an emerald or a red topaz in the backpack:)
              - (removes=emerald or red topaz)
              - {{Qact|The player is healed a maximum of 70 life points.}}
            - (Condition: If the player doesn't have an emerald or a red topaz in the backpack:)
              - **Fairy Nuff:** You don't have an emerald or a red topaz to pay me with!
              - **Player:** Whoops, sorry.
          - [Choice]: On second thoughts, no thanks.
            - **Player:** On second thoughts, no thanks.
            - **Fairy Nuff:** Okay, suit yourself.
      - [Choice]: 90 Life points.
        - **Player:** 90 Life points.
        - **Fairy Nuff:** That will cost you 1 ruby.
        - [Menu]: Select an Option
          - [Choice]: All right.
            - **Player:** All right.
            - (Condition: If the player has a ruby in the backpack:)
              - (removes=ruby)
              - {{Qact|The player is healed a maximum of 90 life points.}}
            - (Condition: If the player doesn't have a ruby in the backpack:)
              - **Fairy Nuff:** You don't have a ruby to pay me!
              - **Player:** Whoops, sorry.
          - [Choice]: On second thoughts, no thanks.
            - **Player:** On second thoughts, no thanks.
            - **Fairy Nuff:** Okay, suit yourself.
      - [Choice]: 110 Life points.
        - **Player:** 110 Life points.
        - **Fairy Nuff:** That will cost you 1 diamond.
        - [Menu]: Select an Option
          - [Choice]: All right.
            - **Player:** All right.
            - (Condition: If the player has a diamond in the backpack:)
              - (removes=diamond)
              - {{Qact|The player is healed a maximum of 110 life points.}}
            - (Condition: If the player doesn't have a diamond in the backpack:)
              - **Fairy Nuff:** You don't have a diamond to pay me!
              - **Player:** Whoops, sorry.
          - [Choice]: On second thoughts, no thanks.
            - **Player:** On second thoughts, no thanks.
            - **Fairy Nuff:** Okay, suit yourself.
  - [Choice]: No thanks. Just looking around.
    - **Player:** No thanks. Just looking around.
    - **Fairy Nuff:** Okay. If you want to know anything, just ask.

### After Fairy Tale II

- **Fairy Nuff:** Thank you so much for all you've done for us, Player.

### After Fairy Tale III

- **Fairy Nuff:** Oh, Player, thanks so much for your help! You're a true friend to us fairies!

### Treasure Trails


#### Receiving the puzzle box

- **Fairy Nuff:** I have a puzzle for you!
- (receives=puzzle box)
- [Fairy Nuff has given you a puzzle box!]

#### When talked to again without solving the puzzle

- **Fairy Nuff:** Is that your best attempt? You'll have to try harder.

#### When talked to with the puzzle solved

- (Condition: If the trail continues:)
  - (removes=the old clue scroll (hard) and puzzle box) (receives= the new clue scroll (hard))
  - [Fairy Nuff has given you another clue scroll!]
  - (continue)
- (Condition: If the trail ends:)
  - (removes=the old clue scroll (hard) and puzzle box) (receives=reward casket (hard))
  - [You've found a casket!]
  - (continue)
- **Fairy Nuff:** There you go!
