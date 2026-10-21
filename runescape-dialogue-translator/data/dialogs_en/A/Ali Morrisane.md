# Ali Morrisane

- **Original Wiki Page**: [Transcript:Ali Morrisane](https://runescape.wiki/w/Transcript%3AAli%20Morrisane)
- **Letter**: `A`

---

## Dialogue Transcript

{{dialogue|npc}}
{{transcript npc|Ali Morrisane}}

### In Al Kharid


#### Before The Feud, without meeting the quest requirements

- **Ali Morrisane:** Hello, my friend. Have a look at my wares.
- [Menu]: Select an Option
  - [Choice]: No, I'm really too busy.
    - **Player:** No, I'm really too busy.
  - [Choice]: Okay.
    - {{tact|opens=Ali's Discount Wares}}

#### Before The Feud, meeting the quest requirements

- **Ali Morrisane:** Good day and welcome back to Al Kharid.
- **Player:** Hello to you too.
- **Ali Morrisane:** My name is Ali Morrisane - the greatest salesman in the world.
- [Menu]: Select an Option
  - [Choice]: If you are, then why are you still selling goods from a stall?
    - **Player:** If you are then why are you still selling goods from a stall?
    - **Ali Morrisane:** Well one can only do and sell so much. If I had more staff I'd be able to sell more, rather than wasting my time on menial things I could get on with selling sand to the Bedabin and useless tourist trinkets to everyone.
    - [Menu]: Select an Option
      - [Choice]: I'm far too busy - adventuring is a full time job you know.
        - **Player:** I'm far too busy - adventuring is a full time job you know.
        - **Ali Morrisane:** No problem my friend, perhaps another time.
        - **Ali Morrisane:** Anyway, have a look at my wares.
        - (removes=10 coins) (receives=a random junk item)
        - Despite your best efforts Ali M still manages to sell you some junk.
        - {{tact|above|wares}}
      - [Choice]: I'd like to help you but.....
        - (see|The Feud#Talking to Ali Morrisane)
  - [Choice]: So, what are you selling?
    - {{tact|opens=Ali's Discount Wares}}

#### After The Feud

- (see|Ali the Trader)

#### After Ali the Trader

{{cleanup}}
- **Ali Morrisane:** Hello Player. How's the adventuring going?
- (Condition: If the player has not completed Missing My Mummy)
  - **Player:** Hi Ali. Not bad. How are you?
  - **Ali Morrisane:** Still selling.
  - [Menu]: Select an Option
    - (Condition: Requires completion of The Feud and the blackjack section of Rogue Trader)
      - [Choice]: I would like to have a look at your selection of blackjacks.
        - (opens=Ali's Discount Wares)
    - (Condition: Requires completion of the clothing section of Rogue Trader)
      - [Choice]: I would like to have a look at your selection of clothes.
        - (opens=Ali's Discount Wares)
      - [Choice]: I would like to have a look at your selection of runes.
      - [Menu]: Select an Option
        - [Choice]: Try to open a small casket of runes
          - **Player:** I think I'll have to go at opening a small casket of runes.
          - (Condition: If the player hasn't opened a small casket that day)
            - [Menu]: Select an Option
              - [Choice]: Force box.
                - (Condition: If the player fails to force the lock)
                  - Your arms tire from the exertions of trying to open the casket...
                  - **Player:** Hmmm... This lock looks like it may be impossible to prise open.
                - (Condition: If the player successfully forces the lock)
                  - You force the lock open with a combination of your strength and agility
                  - [Menu]: Select an Option
                    - [Choice]: Buy all the runes for [amount] coins.
                      - (Condition: If the player has enough coins and free inventory space to buy all the runes)
                        - (removes=[amount] coins)
                        - **Ali Morrisane:** As always it's a pleasure doing business with you.
                        - **Player:** Likewise.
                      - (Condition: If the player does not have enough coins to buy all the runes:)
                        - **Player:** Dang, I don't have enough coins in my inventory to buy them.
                        - **Ali Morrisane:** Don't worry, I'll tell you what I won't put the runes up for sale just yet. I'll let you have first dibs on them.
                        - (opens=Ali's Rune Shop)
                      - (Condition: If the player does not have enough free inventory space to buy all the runes)
                        - **Player:** Blast I don't have enough space for all the runes in my inventory.
                        - **Ali Morrisane:** Don't worry, I'll tell you what I won't put the runes up for sale just yet. I'll let you have first dibs on them.
                        - (opens=Ali's Rune Shop)
                    - [Choice]: Find out what the runes are.
                      - (opens=Ali's Rune Shop)
              - [Choice]: Pick lock.
                - (Player crouches slightly and attempts to pick the lock)
                - (Condition: If the player fails to pick the lock:)
                  - (Condition: If the lockpick breaks:)
                    - (removes=lockpick)
                    - [Your lockpick snaps.]
                    - (continue)
                  - [You fail to pick the lock - your fingers get numb from fumbling with the lock.]
                - (Condition: If the player successfully picks the lock)
                  - You unlock the casket...
                  - (above|runes)
              - [Choice]: Examine lock.
                - (RuneSudoku puzzle interface for a small casket opens.)
                - (above|runes)
          - (Condition: If the player has already opened a small casket that day)
            - **Ali Morrisane:** Sorry friend, I don't have any more small caskets today. Come back tomorrow and another shipment will have arrived.
        - [Choice]: Try to open a large casket of runes
          - **Player:** I'm feeling lucky, let's have a look at opening one of those large caskets.
          - (Condition: If the player hasn't opened a large casket that day)
            - [Menu]: Select an Option
              - [Choice]: Force box.
                - (Condition: If the player fails to force the lock)
                  - Your arms tire from the exertions of trying to open the casket...
                  - **Player:** Hmmm... This lock looks like it may be impossible to prise open.
              - [Choice]: Pick lock.
                - (Player crouches slightly and attempts to pick the lock)
                - (Condition: If the player fails to pick the lock:)
                  - You fail to pick the lock - your fingers get numb from fumbling with the lock.
                  - (Condition: If the lockpick breaks:)
                    - (removes=lockpick)
                    - [Your lockpick snaps.]
                    - (continue)
                  - **Player:** Hmmm... This lock looks like it may be impossible to pick open.
                - (Condition: If the player successfully picks the lock)
                  - You unlock the casket...
                  - (above|runes)
              - [Choice]: Examine lock.
                - (RuneSudoku puzzle interface for a large casket opens.)
                - (above|runes)
          - (Condition: If the player has already opened a large casket that day)
            - **Ali Morrisane:** Sorry friend, I don't have any more large caskets today. Come back tomorrow and another shipment will have arrived.
        - [Choice]: Buy elemental runes.
          - (opens=Ali's Rune Shop)
        - [Choice]: Buy other runes.
          - (opens=Ali's Rune Shop)
        - [Choice]: On second thoughts I don't really need any runes.
          - **Player:** On second thoughts I don't really need any runes.
      - [Choice]: I would like to have a look at your general stock.
        - (opens=Ali's Discount Wares)
    - (Condition: If the player has asked any of the Al Kharid merchants about Ali Morrisane)
      - [Choice]: I hear you're planning to expand your business here...
        - **Player:** I hear you're planning to expand your business here...
        - **Ali Morrisane:** Of course, my friend. Any good salesman ought to take the opportunities that present themselves.
        - **Player:** But your men are threatening the other shopkeepers!
        - **Ali Morrisane:** That is regrettable, I'm afraid.
        - (Condition: If the player has asked Captain Dalbur what he thinks of Ali Morrisane)
          - **Player:** And the gnomes don't sound very happy about your magic carpet business.
          - **Ali Morrisane:** A good businessman looks for all the opportunities he can.
        - [Menu]: Select an Option
          - [Choice]: Aren't you going to do anything about your men?
            - **Player:** Aren't you going to do anything about your men?
            - **Ali Morrisane:** Well, these associates of my nephew can be somewhat... overenthusiastic.
            - **Ali Morrisane:** I'm sure they'll settle down soon.
            - [Menu]: Select an Option
              - [Choice]: But they're threatening to hurt the shopkeepers if they don't cooperate!
                - **Player:** But they're threatening to hurt the shopkeepers if they don't cooperate!
                - **Ali Morrisane:** Well, there's a simple solution there, don't you agree?
                - **Player:** Are you planning to take over all of Al Kharid's shops?
                - **Ali Morrisane:** It's a step in the right direction.
                - **Ali Morrisane:** Now, would you like to have a look at my wares?
                - {{Qact|Player has 10 coins taken from them and receives a random junk item: "Despite your best efforts Ali M still manages to sell you some junk."}}
                - (above|wares)
              - [Choice]: Well, good luck with your business.
                - **Player:** Well, good luck with your business.
                - **Ali Morrisane:** Before you go, have a look at my wares.
                - {{Qact|Player has 10 coins taken from them and receives a random junk item: "Despite your best efforts Ali M still manages to sell you some junk."}}
                - (above|wares)
          - (Condition: If the player has asked Captain Dalbur what he thinks of Ali Morrisane:)
            - [Choice]: What will you do about the gnomes?
              - **Player:** What will you do about the gnomes?
              - **Ali Morrisane:** They can continue running their gliders into trees, and I'll keep my business going. Sooner or later, it'll all work out in my favour.
              - **Player:** I suppose so...
              - **Ali Morrisane:** Anyway, before you go, take a look at my wares.
              - {{Qact|Player has 10 coins taken from them and receives a random junk item: "Despite your best efforts Ali M still manages to sell you some junk."}}
              - (above|wares)
          - [Choice]: Well, good luck with your business.
            - (above|goodluck)
- (Condition: If the player has completed Missing My Mummy)
  - [Menu]: Select an Option
    - [Choice]: Hi, Ali. Not bad. How are you?
      - (above|standard)
    - [Choice]: I have some questions about a tomb.
      - **Player:** I have some questions about a tomb.
      - **Ali Morrisane:** What exactly is it you need to know, then?
      - **Player:** I've just come to say that I solved the problem of the mummy, so all has ended well.
      - **Ali Morrisane:** Bah, where's the profit for me in all this! Get out of my sight, you gloater.

#### Trade option

- {{tact|above2|trade}} <!--Some options appear here but will not appear when talking to Ali Morrisane with standard dialogue.-->

#### Using an Al Kharid flyer on him

- **Player:** Hi! I have this money off voucher!
- **Ali Morrisane:** Oh! Err .. unfortunately it seems to have expired yesterday!
- **Player:** But I only just got it from Waseem the Leaflet !
- **Ali Morrisane:** I'm sorry, there's nothing I can do.
- **Player:** But you're the one that had them printed!
- **Ali Morrisane:** Look, I had those printed to win over the local traders. They weren't too pleased with the money off voucher, but I promised them I would repay their losses.
- **Player:** So that would be why they're all out of date then?
- **Ali Morrisane:** I don't know what you mean!
- **Ali Morrisane:** Anyway, before you go, take a look at my wares.
- {{tact|continuea|trade2}}

#### Using any other item on him

- **Ali Morrisane:** Stop trying to unload your merchandise on me. Can't you see I have enough assets to dispose of already?
