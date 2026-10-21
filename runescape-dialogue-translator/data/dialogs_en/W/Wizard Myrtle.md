# Wizard Myrtle

- **Original Wiki Page**: [Transcript:Wizard Myrtle](https://runescape.wiki/w/Transcript%3AWizard%20Myrtle)
- **Letter**: `W`

---

## Dialogue Transcript


### At the Wizards' Tower


#### Talking to her


##### Before Beneath Cursed Tides

- **Wizard Myrtle:** Well met, traveller.
- **Player:** Hello, what's that you're doing?
- **Wizard Myrtle:** Oh this? I specialise in a type of magic based on the manipulation of water, I'm just practicing my technique.
- **Wizard Myrtle:** My name's Myrtle, I'm a hydromancer!
- **Player:** Nice to meet you. Are you a member of the Wizards' Tower?
- (Condition: Without the quest requirements:)
  - **Wizard Myrtle:** You might say I'm affiliated. I came here in search of help, but I'm afraid I need someone a little more experienced.
  - **Player:** I'll come back when I've trained some more then!
- (Condition: With the quest requirements:)
  - (see|Beneath Cursed Tides#Starting Out)

##### After Beneath Cursed Tides

- **Wizard Myrtle:** Player! Good to see you again, would you like to return to the sunken island?
- [Menu]: Choose an option:
  - [Choice]: I'd like to change my under water
    - [Menu]: What underwater breathing method would you like to use?
      - [Choice]: Underwater breathing spell.
        - **Wizard Myrtle:** Great, I'll cast my spell on you so you can breathe without any diving apparatus.
      - [Choice]: Aquarium diving suit.
        - **Wizard Myrtle:** Great, you can use the diving suit from your house!
      - [Choice]: Fishbowl helmet and diving apparatus.
        - (Condition: If both fishbowl helmet and diving apparatus are equipped or in backpack:)
          - **Wizard Myrtle:** Great, the fishbowl helmet and diving apparatus should work perfectly!
        - (Condition: Without both fishbowl helmet and diving apparatus equipped or in backpack:)
          - **Wizard Myrtle:** If you want to use the fishbowl helmet and diving apparatus you'll need to go and fetch them first.
  - [Choice]: I'd like to dive to the sunken island.
    - (below|Dive option)
  - [Choice]: I need to deposit some items.
    - (below|Deposit option)
  - [Choice]: cond=With unclaimed rewards|Could I get any rewards you're holding for me?
    - (Condition: Without enough space in backpack)
      - **Wizard Myrtle:** It appears you don't have enough room to take all the rewards I have for you. I'll hold on to them until you do.
    - (Condition: With enough space in backpack)
      - (receives=unclaimed quest rewards)
      - **Wizard Myrtle:** That's everything I have for you. Thanks again for your help!
  - [Choice]: No thanks.
    - **Wizard Myrtle:** Ok, just let me know if you do.

#### Deposit option

- **Wizard Myrtle:** I can deposit some items for you if you want.
- (opens=Bank deposit box)

#### Dive option

- (Condition: If the player has weapons equipped, or with both weapons equipped and a follower out:)
  - **Wizard Myrtle:** You should unequip your weapons before you go, the water could damage them.
- (Condition: If the player has a follower out:)
  - **Wizard Myrtle:** You should dismiss your follower before you go, we can't be sure they'll be safe.
- (Condition: Otherwise:)
  - {{Qact|Screen fades in and out. The player is now underwater in front of the Giant Oyster.}}

#### Overhead dialogue

(One of the following is randomly played alongside Myrtle's idle spellcasting animation:)
- **Wizard Myrtle:** {{RSChat|Be patient, like water. Water always finds its way.}}
- **Wizard Myrtle:** {{RSChat|Present water with an obstacle - a force - and it will find a way around.}}
- **Wizard Myrtle:** {{RSChat|Water seeks to be guided. It does not resist, it flows.}}
- **Wizard Myrtle:** {{RSChat|We are all made of water. All you must do, is let it flow through you.}}
