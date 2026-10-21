# Redbeard Frank

- **Original Wiki Page**: [Transcript:Redbeard Frank](https://runescape.wiki/w/Transcript%3ARedbeard%20Frank)
- **Letter**: `R`

---

## Dialogue Transcript


### Standard dialogue

- **Redbeard Frank:** Arr, Matey!
- **Select an Option**
  - [Choice]: cond=Before Pirate's Treasure|I'm in search of treasure.
    - (see|Pirate's Treasure)
  - [Choice]: Arr!
    - **Player:** Arr!
    - **Redbeard Frank:** Arr!
    - (initial)
  - [Choice]: Do you have anything for trade?
    - **Player:** Do you have anything for trade?
    - **Redbeard Frank:** Nothin' at the moment, but then again the Customs Agents are on the warpath right now.
  - [Choice]: cond=After Pieces of Hate|Speak about Pieces of Hate
    - **Redbeard Frank:** Arrr ye really left me out of all that?
    - **Redbeard Frank:** Did ye not be thinking I would have liked to take me knife to Rabid Jack's throat?
    - **Choose an option:**
      - [Choice]: Sorry, I forgot.
        - **Redbeard Frank:** Aye I be forgotten about a lot these days.
        - (continue|grudge)
      - [Choice]: We already had enough people.
        - **Redbeard Frank:** Bah, first rule of be'in a pirate, always bring more than ye need.
        - (continue|grudge)
      - [Choice]: It wasn't my fault!
        - **Redbeard Frank:** Aye, but ye didn't say anything about it did ye?
        - **Player:** I mean I literally had no choice.
        - **Redbeard Frank:** Bah!
        - (continue|grudge)
      - [Choice]: Blame Raven
        - **Redbeard Frank:** What do ye think I am? An idiot? If I blame him he'll put me on his list!
        - **Player:** Oh gods!
        - **Redbeard Frank:** I'm too ginger to die!
        - {{anchor|grudge}}**Redbeard Frank:** Arrr but there be no point in holding a grudge o'er this.
        - **Redbeard Frank:** Was it at least a glorious battle?
        - **Player:**  It was very strange, there was 'rum' involved and kittens all over the place.
        - **Redbeard Frank:** Kittens?
        - **Player:**  Yeah I'm not sure I get it either.
        - **Redbeard Frank:** Strange tales indeed.
        - **Redbeard Frank:** Go on, be off with ya. I've got pirating to be doing.
        - **Player:**  See you around cap'n.
  - [Choice]: About the Task System...
    - (below|Task System)

### Task System

- (Condition: If the Easy Falador achievements have been completed and the rewards not claimed:)
  - **Player:** I've come for my reward.
  - **Redbeard Frank:** So, you've finished, well done! I believe congratulations are in order.
  - **Player:** I believe rewards are in order.
  - **Redbeard Frank:** Right you are.
  - (receives=Falador shield 1 and Antique lamp (Easy Falador Tasks))
  - **Redbeard Frank:** This is the first stage of the Falador shield: a buckler. It grants you access to a Prayer restore ability and an emote.
  - **Redbeard Frank:**Each of these features can be triggered while wielding the shield. The Prayer restore can also be activated from your inventory.
  - **Redbeard Frank:** The Prayer restore ability can only be used once per day, and gives you back a quarter of your Prayer points.
  - **Redbeard Frank:** As well as all of these features, the shield is pretty handy in combat, and gives you a small Prayer boost.
  - **Redbeard Frank:** I've even thrown in a bit of booty I found on my travels.
  - **Player:** Wow, thanks!
  - **Redbeard Frank:** If you should lose your shield, come back and see me for another one.
  - (continue)
- (Condition: If the player has lost their Falador shield 1:)
  - **Player:** I've lost my shield.
  - **Redbeard Frank:** What? That was valuable equipment!
  - **Redbeard Frank:** Luckily, I have a spare. Take better care of it this time.
  - (continue)
- [Menu]: Choose an option:
  - [Choice]: Tell me about the Achievement System.
    - **Redbeard Frank:** Arr! The Achievement System be a load o 'challenges ta do while adventuring 'round the world.
    - **Redbeard Frank:** Ye can earn plunder for completin' certain achievements - either booty or pieces o' eight - which ye can get from Explorer Jack in Lumbridge.
    - **Redbeard Frank:** Most o' them, if ye do enough in an area, gets ye a powerful item which can be claimed from someone in the area, such as meself.
    - [Menu]: Choose an option:
      - [Choice]: Tell me about the set reward for this locality.
        - **Player:** Tell me about the set reward for this area.
        - **Redbeard Frank:** Yer reward here in Falador be a shield, matey, and a better one each time ye finishes a difficulty level.
        - **Redbeard Frank:** We'll let ye know what it does when we gives it to ye.
        - You may also see what rewards a set item provides by hovering over the Rewards icon for its Exploration Achievement set in the Achievements interface.
        - (previous)
      - [Choice]: How do I claim these rewards?
        - **Player:** How do I claim the rewards?
        - **Redbeard Frank:** You need to complete all of the tasks in a set of a particular difficulty, then you can claim your reward.
        - **Redbeard Frank:** Some of the Falador set's tasks are simple, some will require certain skill levels, and some might require quests to be started or completed.
        - **Redbeard Frank:** Ta claim yer Falador set rewards, have a chinwag with the chemist in Rimmington, Sir Vyvin's squire in the White Knights' Castle, or meself.
        - (previous)
      - [Choice]: Sorry, I was just leaving.
        - (end)
  - [Choice]: Could I buy a spare of the reward?
    - [Menu]: Choose an option:
      - [Choice]: Falador shield 1
        - **Redbeard Frank:** Falador shield 1? Yes, but I'm afraid it would cost you 1,500 coins.
        - [Menu]: Purchase another for 1,500 coins?
          - [Choice]: Yes
            - (receives=Falador shield 1) (removes=1,500 coins)
            - [You're handed another Falador shield 1.]
          - [Choice]: No
            - **Player:** No thanks.
      - [Choice]: Falador shield 2
        - **Redbeard Frank:** Falador shield 2? Yes, but I'm afraid it would cost you 2,500 coins.
        - [Menu]: Purchase another for 2,500 coins?
          - [Choice]: Yes
            - (receives=Falador shield 2) (removes=2,500 coins)
            - [You're handed another Falador shield 2.]
          - [Choice]: No
            - **Player:** No thanks.
      - [Choice]: Falador shield 3
        - **Redbeard Frank:** Falador shield 3? Yes, but I'm afraid it would cost you 7,500 coins.
        - [Menu]: Purchase another for 7,500 coins?
          - [Choice]: Yes
            - (receives=Falador shield 3) (removes=7,500 coins)
            - [You're handed another Falador shield 3.]
          - [Choice]: No
            - **Player:** No thanks.
      - [Choice]: Falador shield 4
        - **Redbeard Frank:** Falador shield 4? Yes, but I'm afraid it would cost you 15,000 coins.
        - [Menu]: Purchase another for 15,000 coins?
          - [Choice]: Yes
            - (receives=Falador shield 4) (removes=15,000 coins)
            - [You're handed another Falador shield 4.]
          - [Choice]: No
            - **Player:** No thanks.
  - [Choice]: Sorry, I was just leaving.
    - (end)

### During the first Frank's Free Chest event


#### Using keys on the chest

- (see|Frank's Free Chest (scenery)#With keys)

#### Talk to

- **Redbeard Frank:** Arr, Matey!
- ((Only on first time during the event:))
  - **Player:** Arr yourself! Say Frank, what's the deal with that chest over there?
  - **Redbeard Frank:** That be a treasure chest of One-Eyed Hector, me ol' captain.
  - **Redbeard Frank:** It recently washed up and considerin' all them celebrations and gift-givings lately, I thought I'd hand out its riches to the people of Gielinor.
  - **Redbeard Frank:** Ye know, to right some past wrongs and such.
  - **Player:** That's great! Can I have some?
  - **Redbeard Frank:** Arr, well, ye know...
  - **Redbeard Frank:** ...I may not have the key for it.
  - **Redbeard Frank:** But that be where ye come in! For every 4 pirate's keys ye bring me, I'll give ye one piece of treasure once the chest's open.
  - **Redbeard Frank:** Until January 31st, ye'll be able to find keys every day when you arrive in Gielinor, and hourly while ye're out and about.
  - **Redbeard Frank:** However, ye won't be findin' more than 12 keys a week I reckon.
  - **Redbeard Frank:** A pirate's week always begins on Wednesday, so that's when more pirate's keys will surely appear.
  - **Player:** Sounds like a deal! But what if the fitting key is rusting away at the bottom of the sea?
  - **Redbeard Frank:** Arr, that be quite likely. I was hopin' to avoid keelhauling Hector's memory like this, but...
  - **Redbeard Frank:** ...if it's still shut on February 1st, I'll just blast it open.
  - **Player:** Fair enough.
  - **Redbeard Frank:** Either way, if ye come to me once the chest is open, I'll wait for another four weeks for ye to claim yer share, until February 28th.
  - (continue)
- **Select an Option**
  - I'm in search of treasure.
    - (above)
  - Arr!
    - (above)
  - Do you have anything for trade?
    - (above)
  - Speak about Pieces of Hate
    - (above)
  - Speak about Frank's Free Chest
    - **Redbeard Frank:** That be a treasure chest of One-Eyed Hector, me ol' captain.
    - ((With the chest closed:))
      - **Redbeard Frank:** For every 4 pirate's keys ye bring me, I'll give ye one piece of treasure once the chest's open.
      - **Redbeard Frank:** Ye'll be able to find keys every day when you arrive in Gielinor, and hourly while ye're out and about.
      - **Redbeard Frank:** However, ye won't be findin' more than 12 keys a week I reckon.
      - **Redbeard Frank:** A pirate's week always begins on Wednesday, so that's when ye'll be able to find more keys.
      - **Redbeard Frank:** Ye can bring me keys until January 31st.
      - **Redbeard Frank:** After that, I'll wait until February 28th for ye to claim yer share.
    - ((With the chest open:))
      - **Redbeard Frank:** I'm currently handing out its riches to the people of Gielinor.
      - **Redbeard Frank:** Go on and take yer share!
  - About the Task System...
    - (above|Task System)

### During the second Frank's Free Chest event


#### Talk to

- **Redbeard Frank:** Arr, Matey!
- ((Only on first time during the event:))
  - **Player:** Arr there! I see you've dredged up another chest from the depths of the sea?
  - **Redbeard Frank:** Aye! Hector's humid hoard be provin' quite lucrative.
  - ((Only until the chest is opened:))
    - **Player:** That's great to hear! Any chance I can get some loot in exchange for keys again?
    - **Player:** I hope there's no toads in there this time...
    - **Redbeard Frank:** I actually found the key fer this one meself!
    - **Redbeard Frank:** Took a peek in it earlier. Lots o' piratey attire an' pets, powerful items, an' not one toad!
    - **Player:** But how can I earn some loot if you don't need me to bring you keys?
    - **Redbeard Frank:** Ye can pay me for it, in bits of eight!
    - **Redbeard Frank:** Until the end of May 2nd, ye'll be able to find those every day when ye arrive in Gielinor, an' hourly while ye're out an' about.
    - **Redbeard Frank:** There be a cap of 16 a week, which resets every Wednesday.
    - **Redbeard Frank:** For every 4 bits of eight ye bring me, I'll reserve a piece o' treasure for ye.
    - **Redbeard Frank:** Every 8 bits of eight, that piece will be from a special pool.
    - **Redbeard Frank:** That means roughly half yer loot will be piratey spoils and powerful items!
    - **Redbeard Frank:** On top o' that, I've instructed me crew to deliver ye some extra pirate plunder for every 16 bits of eight ye find.
    - **Redbeard Frank:** Each pirate plunder has a piece of loot from this here chest as well as a title and some clothing worthy of a pirate.
    - **Redbeard Frank:** Ye can come claim yer earned loot from May 3rd until the end of May 31st.
  - ((Only after the chest is opened:))
    - **Redbeard Frank:** {{Transcript missing|}} pieces of eight.
  - (continue)
- **Select an Option**
  - I'm in search of treasure.
    - (above)
  - Arr!
    - (above)
  - Do you have anything for trade?
    - (above)
  - Speak about Pieces of Hate
    - (above)
  - About Frank's Free Chest
    - ((With the chest closed:))
      - **SELECT AN OPTION**
        - About Bits of Eight
          - **Redbeard Frank:** Since me rum reserves be runnin' out fast, I be handing out loot in exchange for bits of eight this time.
          - **Redbeard Frank:** Until the end of May 2nd, ye'll be able to find those every day when ye arrive in Gielinor, an' hourly while ye're out an' about.
          - **Redbeard Frank:** There be a cap of 16 a week, which resets every Wednesday.
          - (previous)
        - About Chest Loot
          - **Redbeard Frank:** For every 4 bits of eight ye bring me, I'll reserve a piece o' treasure for ye.
          - **Redbeard Frank:** Every 8 bits of eight, that piece will be from a special pool.
          - **Redbeard Frank:** That means roughly half yer loot will be piratey spoils and powerful items!
          - **Redbeard Frank:** Ye can come claim yer earned loot from May 3rd until the end of May 31st.
          - (previous)
        - About Pirate Plunder
          - **Redbeard Frank:** I've instructed me crew to deliver ye some extra pirate plunder for every 16 bits of eight ye find.
          - **Redbeard Frank:** Each pirate plunder has a piece of loot from this here chest as well as a title and some clothing worthy of a pirate.
          - (previous)
    - ((With the chest open:))
      - **Redbeard Frank:** If ye've got enough bits of eight, ye can now claim a share of the loot.
      - **Redbeard Frank:** It be one piece of treasure for every 4 bits of eight. Roughly half of the treasure be piratey attire an' pets, or powerful items!
  - About the Task System...
    - (above|Task System)
