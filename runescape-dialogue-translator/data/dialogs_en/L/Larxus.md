# Larxus

- **Original Wiki Page**: [Transcript:Larxus](https://runescape.wiki/w/Transcript%3ALarxus)
- **Letter**: `L`

---

## Dialogue Transcript


### Talk-to


#### Before defeating the Leprechaun Champion

- (Condition: If the player has unclaimed reward lamps from a previous fight:)
  - (Condition: If the player does not have at least two free backpack spaces:)
    - **Larxus:** I've got some lamps for you but you've got a full inventory at the moment.
    - (continue)
  - (Condition: If the player has at least two free backpack spaces:)
    - **Larxus:** Ah ha! I've got some lamps for you!
    - (receives=constitution and slayer XP lamps)
    - (continue)
- (Condition: If the player has not defeated any champions:)
  - **Larxus:** Welcome to the Champions' Arena! If you ever find a champion's scroll during your adventures, here's where the duel will take place.
  - **Larxus:** If you want to experience what it is like to fight a champion, I have an informal challenge issued to you by the Leprechaun Champion.
  - **Larxus:** The rules of this fight are: No items allowed. Do you want to accept the challenge?
  - [Menu]: Select an Option
    - [Choice]: Yes, let me at him!
      - (Condition: If the player has any items equipped or in their backpack:)
        - **Larxus:** I believe I mentioned that you can't have any items with you for this fight.
      - (Condition: If the player does not have any items equipped or in their backpack:)
        - (Condition: If the player has a follower:)
          - **Larxus:** Sorry, but I'm not going to let you face the Leprechaun Champion with that follower.
          - **Larxus:** This is a challenge between you and the champion, not some multi-way brawl with everyone allowed!
        - (Condition: If the player does not have a follower:)
          - **Larxus:** Due to the informal nature of this challenge, it will take place in the training room. Your challenger is waiting for you there. Please go down through the trapdoor when you're ready.
    - [Choice]: No thanks, I'll pass.
      - **Player:** No thanks, I'll pass.
      - (continue|main-dialogue)
- (Condition: If the player has defeated at least one champion:)
  - **Larxus:** The Leprechaun Champion has issued an informal challenge. He has stated that there will be no items allowed for this fight. Do you want to accept the challenge?
  - (continuea|Leprechaun-Champion-challenge)

#### After defeating the Leprechaun Champion

- (Condition: If the player has unclaimed reward lamps from a previous fight:)
  - (Condition: If the player does not have at least two free backpack spaces:)
    - **Larxus:** I've got some lamps for you but you've got a full inventory at the moment.
    - (continue)
  - (Condition: If the player has at least two free backpack spaces:)
    - **Larxus:** Ah ha! I've got some lamps for you!
    - (receives=constitution and slayer XP lamps)
    - (continue)
- (Condition: If the player has been challenged by Leon d'Cour and has not defeated him:)
  - **Larxus:** Leon D'Cour{{Sic}} has issued you a challenge. He has stated that there will be no items allowed except those you're wearing. Do you want to accept the challenge?
  - [Menu]: Select an Option
    - [Choice]: Yes, let me at him!
      - **Larxus:** Your challenger is ready. Please go down through the trapdoor when you're ready.
    - [Choice]: No thanks, I'll pass.
      - **Player:** No thanks, I'll pass.
      - (continue|main-dialogue)
- (Condition: If the player has been challenged by Glophren and has not defeated him:)
  - **Larxus:** Glophren has issued a challenge to you. He has stated that only Magic is allowed, and you can't use any shields. Do you want to accept the challenge?
  - (continuea|champion-of-champions-challenge)
- (Condition: If the player has not claimed the calling beads after defeating any champion with a champion's scroll:)
  - **Larxus:** The champions would like to congratulate you for your accomplishments in this arena.
  - (Condition: If the player does not have at least one free backpack space:)
    - **Larxus:** Sadly, though, you seem to have no inventory space to receive the reward they have for you. I'll keep it here until you have space for it.
    - (continue)
  - (Condition: If the player has at least one free backpack space:)
    - **Larxus:** They would like you to have these calling beads. When used, they will call a banner carrier to you, and it will display your accomplishments in this arena.
    - **Larxus:** The banner will display the total number of champions' scrolls and Champion of Champions you have defeated, or will proudly bear a picture of their individual race.
    - **Larxus:** The banner carrier will be more than happy to change the banner on demand.
    - (receives=calling beads)
    - [pic=Calling beads detail.png]
    - (continue)
- (Condition: If the player has unclaimed rewards from defeating Glophren for the first time:)
  - (Condition: If the player has not claimed all four scrolls of knowledge:)
    - (receives=zero to four scrolls of knowledge)
    - (Condition: If the player does not have enough free backpack spaces for all unclaimed scrolls of knowledge:)
      - **Larxus:** Here are some of the rewards you earned for defeating the Gnome Champions{{Sic}} of Champions, Glophren. I'll give you the rest when you have some free space in your inventory for it.
      - (continue)
    - (Condition: If the player has enough free backpack spaces for all unclaimed scrolls of knowledge:)
      - **Larxus:** Greetings. Here are the rewards you earned for defeating the Gnome Champions{{Sic}} of Champions, Glophren.
      - (continue)
  - (Condition: If the player has not claimed the 50,000 coins:)
    - (receives=50,000 coins)
    - **Larxus:** Here is also a cash reward of 50,000 coins for defeating the Gnome Champions{{Sic}} of Champions, Glophren.
    - (continue)
  - (Condition: If the player has already claimed all four scrolls of knowledge, does not have at least one free backpack space, and has all unused scrolls of knowledge in their backpack:)
    - **Larxus:** Greetings. I have some rewards for you for defeating the Gnome Champions{{Sic}} of Champions, Glophren. However, you'll need some space in your inventory.
    - (continue)
  - (continue|Is there something I can help you with?)
- **Larxus:** Is there something I can help you with?
- [Menu]: Choose an option:
  - [Choice]: I wish to fight the champions!
    - (Condition: If the player has unclaimed reward lamps from a previous fight:)
      - (Condition: If the player does not have at least two free backpack spaces:)
        - **Larxus:** Sorry, but you've got a full inventory and you must accept these reward lamps before I can issue another fight.
      - (Condition: If the player has at least two free backpack spaces:)
        - **Larxus:** Sorry, you must accept these reward lamps before I can issue another fight.
        - (receives=constitution and slayer XP lamps)
    - (Condition: If the player does not have unclaimed reward lamps from a previous fight:)
      - ((Pick a champion interface opens.))
        - (Condition: If the player has already chosen a champion to fight:)
          - **Larxus:** You've already got a champion waiting for you.
        - (Condition: If the player chose the Leprechaun Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're not allowed items. Do you still want to proceed?
        - (Condition: If the player chose the Imp Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're not allowed to use any special attacks. Do you still want to proceed?
        - (Condition: If the player chose the Goblin Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're only allowed to use Magic attacks, no Melee or Ranged. Do you still want to proceed?
        - (Condition: If the player chose the Skeleton Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're only allowed to use Ranged attacks, no Melee or Magic. Do you still want to proceed?
        - (Condition: If the player chose the Zombie Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're not allowed to use any Magic attacks. Do you still want to proceed?
        - (Condition: If the player chose the Hobgoblin Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're not allowed to use any Melee attacks. Do you still want to proceed?
        - (Condition: If the player chose the Giant Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're only allowed to use Melee attacks, no Ranged or Magic. Do you still want to proceed?
        - (Condition: If the player chose the Banshee Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're not allowed to use any prayers or Melee attacks. Do you still want to proceed?
        - (Condition: If the player chose the Ghoul Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're only allowed to take weapons and runes, no other items are allowed. Do you still want to proceed?
        - (Condition: If the player chose the Earth Warrior Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're not allowed to use any prayers. Do you still want to proceed?
        - (Condition: If the player chose the Aberrant Spectre Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you must use a 2-handed weapon. Do you still want to proceed?
        - (Condition: If the player chose the Human Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're not alowed{{Sic}} items except those you're wearing. Do you still want to proceed?
        - (Condition: If the player chose the Jogre Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're not allowed to use any Ranged attacks. Do you still want to proceed?
        - (Condition: If the player chose the Mummy Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're not allowed to use anything that's worn in your off-hand slot. Do you still want to proceed?
        - (Condition: If the player chose the Lesser Demon Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're not allowed to bring any weapons or armour. Do you still want to proceed?
        - (Condition: If the player chose the Gnome Champion:)
          - **Larxus:** So, you want to accept the challenge, huh? Well, there are some specific rules for these champion fights. For this fight you're only allowed to use Magic attacks, and you can't use any shields. Do you still want to proceed?
      - [Menu]: Select an Option
        - [Choice]: Yes, let me at him!
          - **Player:** Yes, let me at him!
          - (Condition: If the player has a follower:)
            - **Larxus:** Sorry, but I'm not going to let you down there with that follower.
            - **Larxus:** This is a challenge between you and the champion, not some multi-way brawl with everyone allowed!
            - (Condition: If the player has calling beads:)
              - **Larxus:** That also includes this item: Calling beads.
          - (Condition: If the player does not have a follower:)
            - **Larxus:** Your challenger is ready. Please go down through the trapdoor when you're ready.
        - [Choice]: No thanks, I'll pass.
          - **Player:** No thanks, I'll pass.
  - [Choice]: cond=If the player has a champion's scroll from a champion not yet defeated:|I was given a challenge. What now?
    - **Player:** I was given a challenge. What now?
    - **Larxus:** Well, pass it here and we'll get you started.
  - [Choice]: cond=If the player has defeated all the champions:|I've defeated all the champions. What now?
    - **Player:** I've defeated all the champions. What now?
    - **Larxus:** You can come back next week and fight the champions again, give them time to nurse their wounds and their pride.
    - **Larxus:** Also, keep a watch out. More champions may rise to test your mettle in the future.
  - [Choice]: cond=If the player lost the calling beads:|I have lost my calling beads.
    - **Player:** I have lost my calling beads.
    - (Condition: If the player does not have at least one free backpack space:)
      - **Larxus:** That's alright. I'll give you some more when you have some space in your inventory for them.
    - (Condition: If the player has at least one free backpack space:)
      - **Larxus:** That's alright. Please take these as replacements.
      - (receives=calling beads)
      - [pic=Calling beads detail.png]
      - **Player:** Thank you.
  - [Choice]: What is this place?
    - **Player:** What is this place?
    - **Larxus:** This is the Champions' Arena. The champions of various races use it to duel those they deem worthy of the honour. Anything else?
    - [Menu]: Choose an option:
      - [Choice]: cond=If the player has a champion's scroll from a champion not yet defeated:|I was given a challenge. What now?
        - (above|I was given a challenge. What now?)
      - [Choice]: cond=If the player has defeated all the champions:|I've defeated all the champions. What now?
        - (above|I've defeated all the champions. What now?)
      - [Choice]: Nothing, thanks.
        - (below|Nothing, thanks.)
  - [Choice]: Nothing, thanks.
    - **Player:** Nothing, thanks.

### Fight


#### Before defeating the Leprechaun Champion

- (Condition: If the player has not defeated any champions:)
  - **Larxus:** Welcome to the Champions' Arena! If you ever find a champion's scroll during your adventures, here's where the duel will take place.
  - **Larxus:** If you want to experience what it is like to fight a champion, I have an informal challenge issued to you by the Leprechaun Champion.
  - **Larxus:** The rules of this fight are: No items allowed. Do you want to accept the challenge?
  - [Menu]: Select an Option
    - [Choice]: Yes, let me at him!
      - (Condition: If the player has any items equipped or in their backpack:)
        - **Larxus:** I believe I mentioned that you can't have any items with you for this fight.
      - (Condition: If the player does not have any items equipped or in their backpack:)
        - (Condition: If the player has a follower:)
          - **Larxus:** Sorry, but I'm not going to let you face the Leprechaun Champion with that follower.
          - **Larxus:** This is a challenge between you and the champion, not some multi-way brawl with everyone allowed!
        - (Condition: If the player does not have a follower:)
          - **Larxus:** Due to the informal nature of this challenge, it will take place in the training room. Your challenger is waiting for you there. Please go down through the trapdoor when you're ready.
    - [Choice]: No thanks, I'll pass.
      - **Player:** No thanks, I'll pass.
      - (continuea|I wish to fight the champions!)
- (Condition: If the player has defeated at least one champion:)
  - **Larxus:** The Leprechaun Champion has issued an informal challenge. He has stated that there will be no items allowed for this fight. Do you want to accept the challenge?
  - (continuea|Leprechaun-Champion-challenge-2)

#### After defeating the Leprechaun Champion

- (above|I wish to fight the champions!)

### Using a champion's scroll on Larxus

- (removes=the champion's scroll)
- (Condition: If the champion is not unlocked:)
  - **Larxus:** You can now challenge this champion.
- (Condition: If the champion is already unlocked:)
  - **Larxus:** You've already unlocked this champion. The challenge is void.

### After defeating any champion

- (Condition: If the player does not have at least two free backpack spaces:)
  - You have unclaimed lamps from Larxus the butler.
- (Condition: If the player has at least two free backpack spaces:)
  - (receives=constitution and slayer XP lamps)
  - You sense lamps have entered your bag.

### After defeating any champion with 10+ unique champions defeated before defeating Leon d'Cour

- **Leon d'Cour:** You have done well, brave adventurer, but I would test your mettle now. You may arrange the fight with Larxus at your leisure.

### After defeating any champion with 13+ unique champions defeated (including Leon d'Cour) before defeating Glophren

- **Glophren:** Your skills are admirable, human. I would like to test your mettle now. You may arrange the fight with Larxus at your leisure.

### After defeating any champion with a champion's scroll before claiming the calling beads

- **Larxus:** Congratulations! The champions and I have a reward for you. Come and talk to me to collect it.

### After defeating Glophren before collecting the rewards

- **Larxus:** I also have some extra rewards for your victory over the Gnome Champion. Come and talk to me to collect them.

### Attempting to open the trapdoor


#### Before defeating all champions

- The trapdoor is locked from the inside. You can hear the muffled sounds of things being hit.
- **Larxus:** That's the champions' training room. I can't let you down there while they are training.

#### After defeating all champions

- The trapdoor is locked. All is quiet on the other side.
- **Larxus:** That was the champions' training room - until you defeated all of them.

### Attempting to open the champion statue

- **Larxus:** You need to arrange a challenge with me before you enter the arena.

### Attempting to climb-down the champion statue with a follower

- **Larxus:** Sorry, but I'm not going to let you down there with that follower.
- **Larxus:** This is a challenge between you and the champion, not some multi-way brawl with everyone allowed!
- (Condition: If the player has calling beads:)
  - **Larxus:** That also includes this item: Calling beads.

### Attempting to climb-down the champion statue with prohibited items


#### Leprechaun Champion

- **Larxus:** I believe I mentioned that you're not allowed to take any weapons or armour into this duel.{{Sic}}

#### Lesser Demon Champion

- **Larxus:** I believe I mentioned that you're not allowed to take any weapons or armour into this duel.

#### Ghoul Champion

- **Larxus:** I believe I mentioned that you're only allowed to take weapons or runes into this duel.

#### Mummy Champion

- **Larxus:** I believe I mentioned that you cannot have any item that's worn in your off-hand slot in this duel.

#### Aberrant Spectre Champion

- **Larxus:** I believe I mentioned that you have to use a 2-handed weapon in this duel.

#### Leon d'Cour

- **Larxus:** I believe I mentioned that you're not allowed to take any items, except those you're wearing, into this duel.

#### Glophren

- **Larxus:** I believe I mentioned that you can't take in any shields.

### Attempting to use special attacks (including Ancient Magicks) during the fight with the Imp Champion

- **Larxus:** I believe I mentioned that you're not allowed to use special attacks or abilities in this duel.
- You're not allowed to use special attacks or abilities in this duel.
- ((Repeated in a pop-up:))
  - You're not allowed to use special attacks or abilities in this duel.

### Attempting to use melee or magic attacks during the fight with the Skeleton Champion

- **Larxus:** I believe I mentioned that you're only allowed to use Ranged in this duel.
- You're only allowed to use Ranged in this duel.
- ((Repeated in a pop-up:))
  - You're only allowed to use Ranged in this duel.

### Attempting to use melee or ranged attacks during the fight with the Goblin Champion and Glophren

- **Larxus:** I believe I mentioned that you're only allowed to use Magic in this duel.
- You're only allowed to use Magic in this duel.
- ((Repeated in a pop-up:))
  - You're only allowed to use Magic in this duel.

### Attempting to use melee attacks during the fight with the Hobgoblin and Banshee Champions

- **Larxus:** I believe I mentioned that you're not allowed to use melee combat in this duel.
- You're not allowed to use melee combat in this duel.
- ((Repeated in a pop-up:))
  - You're not allowed to use melee combat in this duel.

### Attempting to use magic or ranged attacks during the fight with the Giant Champion

- **Larxus:** I believe I mentioned that you're only allowed to use melee combat in this duel.
- You're only allowed to use melee combat in this duel!
- ((Repeated in a pop-up:))
  - You're only allowed to use melee combat in this duel!

### Attempting to use magic attacks during the fight with the Zombie Champion

- **Larxus:** I believe I mentioned that you're not allowed to use Magic in this duel.
- You're not allowed to use Magic in this duel.
- ((Repeated in a pop-up:))
  - You're not allowed to use Magic in this duel.

### Attempting to use ranged attacks during the fight with the Jogre Champion

- **Larxus:** I believe I mentioned that you're not allowed to use Ranged in this duel.
- You're not allowed to use Ranged in this duel.
- ((Repeated in a pop-up:))
  - You're not allowed to use Ranged in this duel.

### Attempting to activate prayers or curses during the fight with the Earth Warrior and Banshee Champions

- **Larxus:** I believe I mentioned you're not allowed to use Prayer in this duel. That goes for curses too!
- You're not allowed to use [prayers/curses] in this duel!

### Attempting to equip an item in the off-hand slot during the fight with the Mummy Champion

- You're not supposed to have anything that can be worn in your shield slot.
- ((Repeated in a pop-up:))
  - You're not supposed to have anything that can be worn in your shield slot.

### Attempting to equip a 1-handed weapon during the fight with the Aberrant Spectre Champion

- You can only use a 2-handed weapon.
- ((Repeated in a pop-up:))
  - You can only use a 2-handed weapon.

### Fighting Glophren

- (Condition: If the player is praying:)
  - Glophren throws something at your feet! You lose concentration and stop praying.

### Attempting to teleport out of the Champions' Arena

- **Larxus:** There's a ladder for a reason.
