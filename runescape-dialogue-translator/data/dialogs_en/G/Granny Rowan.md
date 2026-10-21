# Granny Rowan

- **Original Wiki Page**: [Transcript:Granny Rowan](https://runescape.wiki/w/Transcript%3AGranny%20Rowan)
- **Letter**: `G`

---

## Dialogue Transcript


### Before the player has the ability to use the botanist's workbench


#### Attempting to use the botanist's workbench

- **Granny Rowan:** Over here, dearie! Indulge me with a spot of conversation before you get started over there, would you my sweet?

#### Any option before the completing the following dialogue

- **Player:** Who are you? Who let you in here?
- **Granny Rowan:** Rowan, dearest. Granny Rowan, if you'd prefer. Most do.
- **Granny Rowan:** A little birdie told me that you had built a new botanists{{Sic}} bench in this quaint little fort of yours, so I decided to hop on over and lend you a hand.
- **Granny Rowan:** I know a thing or two about making potions, you see. Isn't that right, Leaf?
- **Leaf:** Meow.
- **Player:** Why should I trust you?
- **Granny Rowan:** The wilderness is a dangerous place, dearie. Now more than ever. Zombies running rampant, and now a Mahjarrat with an undead dragon on the way...
- **Granny Rowan:** It never hurts to have allies in such times, my dear. Especially when they make a good brew.
- **Leaf:** Meow.
- **Player:** How do you know about that?
- **Granny Rowan:** I have my ways, love. That nasty, nasty man is no friend of Granny's, I assure you.
- **Player:** I feel like I need to have a word with the captain of the guard...
- **Granny Rowan:** As you must, sweetness. But don't keep an old dear waiting.

#### Any option after completing the dialogue above but before talking to guard captain Sofía

- **Granny Rowan:** Have you spoken to little Sofia, yet?
- **Player:** How did you- oh, never-mind. Not yet.
- **Granny Rowan:** Do hurry, sweetness. It's very rude to keep an old lady waiting.

#### Any option after talking to guard captain Sofía

- **Granny Rowan:** Have you spoken to little Sofia, yet?
- **Player:** How did you- oh, never-mind. A little birdie told you, did they?
- **Granny Rowan:** You're a fast learner dearie. Now, what's the verdict?
- **Player:** You can stay and help manage the workbench. But we'll be keeping an eye on you.
- **Granny Rowan:** How darling! You must join me for a spot of tea some time, I insist!
- **Leaf:** Meow.
- **Player:** Another time, perhaps.

### After the player has the ability to use the botanist's workbench


#### Talk to

- Choose an option:
  - Can you decant my potions for me?
    - (below|Decant)
  - ((With Tier 2 built:))
    - Do you have anything for trade?
      - (opens=Granny Rowan's Supplies)
  - ((With Tier 3 built:))
    - Can you prepare my potions for me?
      - (below|Prepare potions)
  - What do you do here?
    - **Player:** So what is it exactly that you do here?
    - **Granny Rowan:** Oh you know, this and that.
    - At tier 1, Granny Rowan can decant your potions and blubbers for you.
    - At tier 2, Granny Rowan will open a shop that has a limited stock of tradeable herblore supplies. You will additionally be able to receive unnoted vials of water from the botanist's bench.
    - At tier 3, Granny Rowan will prepare overloads and overload salves for you, allowing you to make them in larger quantities at the botanist's workbench.
  - Cancel
    - (end)

#### Decant

- ((The following is shown in an interface titled "SELECT AN OPTION":))
  - Decanting Options
    - Decant vials
      - (The interface closes.)
      - **HOW MANY DOSES DO YOU WANT TO DECANT INTO?**
        - One dose
          - ((Without items in backpack:))
            - **Granny Rowan:** You haven't got anything to decant!
          - ((With items in backpack:))
            - Searching...
            - ((Without compatible potions found:))
              - ((Without any potions found:))
                - **Granny Rowan:** Sorry, I don't know how to decant anything that you're carrying.
              - ((With one incompatible potion found:))
                - **Granny Rowan:** Sorry, I can't do anything with that potion.
              - ((With multiple incompatible potions found:))
                - **Granny Rowan:** Sorry, I can't do anything with those potions.
            - ((With compatible potions found:))
              - ((With coins for missing vials:))
                - ((Without backpack space for the new items:))
                  - **Granny Rowan:** Your inventory's a bit too full for me to do anything for you.
                - ((With backpack space for the new items:))
                  - (removes=two coins for each missing vial) (receives=as many one-dose potions as possible)
                  - ((Repeated for each type of potion if the coins were taken from the money pouch, then continues below:))
                    - [number] coins have been removed from your money pouch.
                  - **Granny Rowan:** There you go, chum.
              - ((Without coins for missing vials:))
                - **Granny Rowan:** Sorry, you don't have enough money to pay for enough empty vials.
        - Two doses
          - ((Without items in backpack:))
            - **Granny Rowan:** You haven't got anything to decant!
          - ((With items in backpack:))
            - Searching...
            - ((Without compatible potions found:))
              - ((Without any potions found:))
                - **Granny Rowan:** Sorry, I don't know how to decant anything that you're carrying.
              - ((With one incompatible potion found:))
                - **Granny Rowan:** Sorry, I can't do anything with that potion.
              - ((With multiple incompatible potions found:))
                - **Granny Rowan:** Sorry, I can't do anything with those potions.
            - ((With compatible potions found:))
              - ((With coins for missing vials:))
                - ((Without backpack space for the new items:))
                  - **Granny Rowan:** Your inventory's a bit too full for me to do anything for you.
                - ((With backpack space for the new items:))
                  - (removes=two coins for each missing vial) (receives=as many two-dose potions as possible)
                  - ((Repeated for each type of potion if the coins were taken from the money pouch, then continues below:))
                    - [number] coins have been removed from your money pouch.
                  - **Granny Rowan:** There you go, chum.
              - ((Without coins for missing vials:))
                - **Granny Rowan:** Sorry, you don't have enough money to pay for enough empty vials.
        - Three doses
          - ((Without items in backpack:))
            - **Granny Rowan:** You haven't got anything to decant!
          - ((With items in backpack:))
            - Searching...
            - ((Without compatible potions found:))
              - ((Without any potions found:))
                - **Granny Rowan:** Sorry, I don't know how to decant anything that you're carrying.
              - ((With one incompatible potion found:))
                - **Granny Rowan:** Sorry, I can't do anything with that potion.
              - ((With multiple incompatible potions found:))
                - **Granny Rowan:** Sorry, I can't do anything with those potions.
            - ((With compatible potions found:))
              - ((With coins for missing vials:))
                - ((Without backpack space for the new items:))
                  - **Granny Rowan:** Your inventory's a bit too full for me to do anything for you.
                - ((With backpack space for the new items:))
                  - (removes=two coins for each missing vial) (receives=as many three-dose potions as possible)
                  - ((Repeated for each type of potion if the coins were taken from the money pouch, then continues below:))
                    - [number] coins have been removed from your money pouch.
                  - **Granny Rowan:** There you go, chum.
              - ((Without coins for missing vials:))
                - **Granny Rowan:** Sorry, you don't have enough money to pay for enough empty vials.
        - Four doses
          - Searching...
          - ((Without items in backpack:))
            - **Granny Rowan:** You haven't got anything to decant!
          - ((With items in backpack:))
            - Searching...
            - ((Without compatible potions found:))
              - ((Without any potions found:))
                - **Granny Rowan:** Sorry, I don't know how to decant anything that you're carrying.
              - ((With one incompatible potion found:))
                - **Granny Rowan:** Sorry, I can't do anything with that potion.
              - ((With multiple incompatible potions found:))
                - **Granny Rowan:** Sorry, I can't do anything with those potions.
            - ((With compatible potions found:))
              - (receives=as many four-dose potions as possible)
              - **Granny Rowan:** There you go.
    - Decant flasks
      - (The interface closes.)
      - ((Without flasks in backpack:))
        - **Granny Rowan:** Sorry, you don't seem to have anything I can use. Make sure you have 2 flasks that aren't completely full!
      - ((With flasks in backpack:))
        - **Granny Rowan:** Let's see what you have. I will decant your potion flasks back into 6 dosed flasks. I can make use of the flasks, so I'll take those as payment.
        - ((Only with confirmation not toggled off:))
          - **DECANT THE FLASKS, AND I WILL KEEP ANY EMPTY FLASKS?**
            - Yes
              - (continue)
            - No
              - (end)
            - Yes, and don't ask again
              - (continue)
        - (receives=as many six-dose flasks as possible) (removes=all flasks that were emptied completely)
        - **Granny Rowan:** Here you go. That's the best I can do! {{Sic|If the flasks don't look too different, I gave them a clean}}
    - Convert vials to flasks
      - (The interface closes.)
      - ((Without empty flasks in backpack:))
        - **Granny Rowan:** You'll need to supply the empty flasks yourself; they're not cheap. You can bring them to me noted or unnoted.
      - ((With empty flasks in backpack:))
        - **Granny Rowan:** {{Sic|Lets}} see what you have. I will decant potion vials and all flasks with up to 4 doses into 6 dose flasks. &nbsp;You'll need to supply the empty flasks yourself; they're not cheap.
        - ((Without potions to decant or without backpack space for the new items:))
          - **Granny Rowan:** Sorry you don't seem to have anything I can help you with! Make sure you have the correct potions and some free space in your inventory and I can try again.
        - ((With potions to decant and backpack space for the new items:))
          - (removes=as many potion doses as possible) (receives=empty vials for completely emptied potion vials and full potion flasks for all removed doses)
          - **Granny Rowan:** Here you go. That's the best I can do!
    - Convert flasks to vials
      - (The interface closes.)
      - ((Without flasks to convert or without backpack space for the new items:))
        - **Granny Rowan:** Sorry, you don't seem to have anything I can use. Make sure you have at least 1 flask!
      - ((With flasks to convert and with backpack space for the new items:))
        - **Granny Rowan:** Certainly. I think I can make use of the flasks, so I'll give you the vials for free.
        - (removes=flasks) (receives=vials with corresponding number of doses)
        - **Granny Rowan:** There you go, that's the best I can do!
    - Combine jellyfish
      - (The interface closes.)
      - ((Without items in backpack:))
        - **Granny Rowan:** You don't have any jellyfish to combine!
      - ((With items in backpack:))
        - ((Without jellyfish to combine:))
          - **Granny Rowan:** Sorry, I don't know how to combine anything that you're carrying.
        - ((With jellyfish to combine:))
          - {{Qact|The jellyfish are combined.}}
          - **Granny Rowan:** There you go.
    - Cancel
      - (The interface closes.)

#### Trade

- (opens=Granny Rowan's Supplies)

#### Prepare potions


##### With the functionality enabled

- **Player:** Can you prepare my potions for me, please?
- **Granny Rowan:** Certainly! Just to warn you, I won't be able to take them back afterwards. I also won't benefit from any of your fancy buffs.
  - Would you like to continue?
    - Yes.
      - (Make-X interface for item production opens with item with the highest Herblore requirement selected, or overload (3) (unf) if the player doesn't have materials for any items.)
      - ((After making unfinished potions:))
        - **Granny Rowan:** Here you go!
    - No.
      - (end)

##### With the functionality disabled

- Granny Rowan is too tired to do this right now.
