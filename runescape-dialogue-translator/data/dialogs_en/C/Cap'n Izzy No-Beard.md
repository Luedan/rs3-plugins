# Cap'n Izzy No-Beard

- **Original Wiki Page**: [Transcript:Cap'n Izzy No-Beard](https://runescape.wiki/w/Transcript%3ACap%27n%20Izzy%20No-Beard)
- **Letter**: `C`

---

## Dialogue Transcript


### Before Pieces of Hate

- **Player:** Ahoy, Cap'n!
- **Cap'n Izzy No-Beard:** Ahoy there!
- **Parrot:** Avast ye scurvy swabs!
- **Player:** Huh?
- **Cap'n Izzy No-Beard:** Don't mind me parrot, he's Cracked Jenny's Tea Cup!
- [Menu]: Select an Option
  - [Choice]: What is this place?
    - **Player:** What is this place?
    - **Cap'n Izzy No-Beard:** This, me hearty, is the entrance to the Brimhaven Agility Arena!
    - **Cap'n Izzy No-Beard:** I were diggin' for buried treasure when I found it! Amazed I was! It was a sight to behold!
    - **Parrot:** Buried treasure!
    - **Cap'n Izzy No-Beard:** It were the biggest thing I'd ever seen! It must've been at least a league from side to side!
    - **Cap'n Izzy No-Beard:** It made me list, I were that excited!
    - **Parrot:** Get on with it!
    - **Cap'n Izzy No-Beard:** I'd found a huge cave with all these platforms. I reckon it be an ancient civilisation that made it. I had to be mighty careful, as there was these traps everywhere! Dangerous it was!
    - **Parrot:** Danger! Danger!
    - **Cap'n Izzy No-Beard:** Entrance is only 200 coins!
    - (initial|options)
  - [Choice]: What do I do in the arena?
    - **Player:** What do I do in the arena?
    - **Cap'n Izzy No-Beard:** Well, me hearty, it's simple. Ye can cross between two platforms by using the traps or obstacles strung across 'em. Try to make your way to the pillar that is indicated by the flashing arrow.
    - **Cap'n Izzy No-Beard:** Ye receive tickets for tagging more than one pillar in a row. So, ye won't get a ticket from the first pillar, but ye will for every platform ye tag in a row after that.
    - **Cap'n Izzy No-Beard:** If ye miss a platform, ye will miss out on the next ticket, so try to get every platform you can! When ye be done, take the tickets to Jackie over there and she'll exchange them for more stuff!
    - **Parrot:** Tag when green light means tickets! Tag when red light means green light!
    - **Cap'n Izzy No-Beard:** Thanks me hearty!
    - **Parrot:** Danger! Danger!
    - **Player:** This sounds dangerous. Can I die down there?
    - **Cap'n Izzy No-Beard:** Aye ye can, me hearty, but I look after me customers, see. If ye die, I'll bring yer gravestone and items back up to this hut.
    - **Player:** Thanks!
    - (initial|options)
  - [Choice]: I'd like to use the Agility Arena, please.
    - **Player:** I'd like to use the Agility Arena, please.
    - (Condition: If the player has not completed Rocking Out:)
      - **Cap'n Izzy No-Beard:** Aye, entrance be 200 coins.
      - **Parrot:** Pieces of eight!
      - **Cap'n Izzy No-Beard:** A word of warning, me hearty! There are dangerous traps down there!
      - [Menu]: Select an Option
        - [Choice]: Okay, here's 200 coins.
          - (Condition: If the player does not have enough money:)
            - You can not afford that.
            - **Player:**  I don't have the money on me at the moment.
            - **Parrot:** *squawk*
            - **Cap'n Izzy No-Beard:** No coins, no entrance!
          - (Condition: If the player has enough money:)
            - **Player:** Okay, here's 200 coins.
            - (removes=200 coins)
            - [You give Cap'n Izzy 200 coins.]
            - **Cap'n Izzy No-Beard:** May the wind be in ye sails!
        - [Choice]: Never mind.
          - **Player:** Never mind.
    - (Condition: If the player has already paid:)
      - **Cap'n Izzy No-Beard:** Ye've already paid, so down ye goes...
    - (Condition: If the player has completed Rocking Out:)
      - **Cap'n Izzy No-Beard:** Yer always welcome here, Player. No need to pay!
  - [Choice]: Is it true you sell Skillcapes of Agility?
    - (Condition: If the player has a ring of charos (a) equipped:)
      - **Cap'n Izzy No-Beard:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
      - [Menu]: Choose an option:
        - [Choice]: 92,000 coins? That's much too expensive.
          - **Player:** I know where to find you if I change my mind.
        - [Choice]: I think I have the money right here, actually.
          - (Condition: If the player has no backpack space:)
            - **Cap'n Izzy No-Beard:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some backpack space before I can sell you one.
          - (Condition: If the player does not have enough money:)
            - **Player:** But unfortunately, I was mistaken.
            - **Cap'n Izzy No-Beard:** Well, come back and see me when you do.
          - (Condition: If the player has enough money:)
            - (receives=agility cape and agility hood) (removes=92,000 coins)
            - **Cap'n Izzy No-Beard:** Excellent! Wear that cape with pride my friend.
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
            - (receives=agility cape and agility hood) (removes=99,000 coins)
            - **Cap'n Izzy No-Beard:** Excellent! Wear that cape with pride my friend.
  - [Choice]: I've noticed there are a couple of versions of each skillcape.
    - **Cap'n Izzy No-Beard:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
    - (Condition: If the player is using the old model:)
      - **Cap'n Izzy No-Beard:** It looks like you're currently using the old model for your Agility skillcape. Would you like to change to the newer one?
      - (continue)
    - (Condition: If the player is using the new model:)
      - **Cap'n Izzy No-Beard:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
      - (continue)
    - [Menu]: Select an Option
      - [Choice]: Yes, I would like to wear the [new/old] version of the skillcape.
        - **Cap'n Izzy No-Beard:** Would you like to wear the [old/newer] model for just this cape, or for the Quest Cape and all of the skillcapes you own?
        - [Menu]: Select an Option
          - [Choice]: I would just like to change the agility skillcape.
            - **Cap'n Izzy No-Beard:** No problem, you will now use the [older/newer] model for your agility skillcape.
          - [Choice]: I would like to change all my skillcapes.
            - **Cap'n Izzy No-Beard:** No problem, you will now use the [older/newer] model for all of your skillcapes!
          - [Choice]: I've changed my mind!
            - (end)
      - [Choice]: No, thank you.
        - **Cap'n Izzy No-Beard:** Great! I'm glad you're still enjoying the [old/new] version!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Cap'n Izzy No-Beard:** If you want, I can make it so you use the old model for all of the skillcapes you own.
          - [Menu]: Select an Option
            - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
              - **Cap'n Izzy No-Beard:** Great, you will now use the old model for all of your skillcapes!
            - [Choice]: No, thanks.
              - (end)

#### Attempting to enter the Agility Arena without paying

- **Parrot:** Clap [him/her] in irons!
- **Cap'n Izzy No-Beard:** Ahoy there! Pay up first!

#### Attempting to enter the Agility Arena with a follower out

- **Parrot:** Squawk!
- **Cap'n Izzy No-Beard:** Oi, matey! No followers allowed in the arena!

### After Pieces of Hate

- [Menu]: Select an Option
  - [Choice]: Talk about Pieces of Hate.
    - **Cap'n Izzy No-Beard:** It's done! It's over with! Rabid Jack will threaten us no more!
    - **Cap'n Izzy No-Beard:** Thanks, Player. We couldn't have done it without you.
  - [Choice]: Talk about the Agility Arena.
    - (continuea|greeting)

### Pay option


#### Before Rocking Out

- (removes=200 coins)
- [You give Cap'n Izzy the 200 coin entrance fee.]
- You give Cap'n Izzy the 200 coin entrance fee.

#### After paying

- **Cap'n Izzy No-Beard:** Avast there, ye've already paid!
- **Parrot:** Shiver me timbers, what a ninny!

#### After Rocking Out

- **Cap'n Izzy No-Beard:** Yer always welcome here, Player. No need to pay!

### Treasure Trails

- **Cap'n Izzy No-Beard:** Can I help you with something?
- **Player:** Well, I'm here about a Treasure Trail.
- **Cap'n Izzy No-Beard:** Ah, you'll be wanting to talk to him then.
- **Player:** Him?
- **Parrot:** Avast!
- **Parrot:** Answer this and I'll give you treasure!
- (receives=challenge scroll)
- [The parrot has given you a challenge scroll!]

##### When talked to again

- **Parrot:** Please enter the answer to the question.
- ''(When given the wrong answer:)
  - **Parrot:** Try again! Try again!
- ''(When given the correct answer:)
  - (removes=the challenge scroll and the old clue scroll (hard))
  - (If the trail continues:)
    - (receives=a new clue scroll (hard))
    - [The parrot has given you another clue scroll!]
    - (continue)
  - (If the trail ends:)
    - (receives=reward casket (hard))
    - [You've found a casket!]
    - (continue)
  - **Parrot:** Squawk! Pieces of eight!
