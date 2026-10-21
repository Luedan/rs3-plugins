# Doronbol

- **Original Wiki Page**: [Transcript:Doronbol](https://runescape.wiki/w/Transcript%3ADoronbol)
- **Letter**: `D`

---

## Dialogue Transcript


### Talk-to


#### Without a catspeak amulet

- **Doronbol:** Meow?

#### With a catspeak amulet


##### Before All Fired Up

- **Player:** Hello, cat. What on earth are you doing here?
- **Doronbol:** Oh, I'm looking after this beacon for King Roald.
- **Player:** How's that going for you?
- **Doronbol:** All's well, life is peaceful, the flowers are blooming, the birds are singing, and it's the most lovely of days today.
- **Player:** Wow, you seem very pleased about things!
- **Doronbol:** I am! I'm so happy, I can't help but wag my tail and bound about recklessly!
- **Doronbol:** It's nice to have such a high purpose in life and to have earned the trust and affection of such a noble human as King Roald.
- **Player:** Wait - you're a cat right? Not a dog in disguise?
- **Doronbol:** Uh, by 'wag my tail' I meant...um...'purr really loudly'. And, just for the record, I'm, uh, thoroughly indifferent to humans. And aloof. I'm very, very aloof.
- **Player:** That sounds more like it.
- **Doronbol:** Say, you won't repeat what I said before, will you? I wouldn't want any more marks on my cat license.
- **Player:** Don't worry, moggy; your secrets are safe with me.
- **Doronbol:** Purrrrrrr!

##### After All Fired Up but before A Tail of Two Cats

- **Player:** Hi, there. I was wondering if you could help me.
- **Doronbol:** That depends. Can you tell me any interesting stories? It's rather boring around here, you see.
- **Player:** Of course, I can tell you great stories! I'm an amazingly interesting adventurer, don't you know.
- **Doronbol:** Pshaw! I'm not interested in your boring human stories - I'm interested in some good feline gossip.
- **Player:** Oh, uhh...
- **Doronbol:** Oh, never mind; it was asking a lot. If you  come across any juicy tidbits, do stop by for a chinwag.
- [A Tail of Two Cats].}}

##### After All Fired Up and after A Tail of Two Cats

- **Doronbol:** Purrr! Hello there. Is there anything I can do for you?
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Doronbol:** Of course. Once the beacon is lit, just leave 5 logs with me and I'll take care of the fire for as long as I can.
    - (Condition: If the beacon is dying:)
      - **Doronbol:** Well, I could, but since you're here, you might as well do it yourself.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Doronbol does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Doronbol:** I'm afraid you don't have enough of the right type of logs for me to use.
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Doronbol:** I'll need five logs to be able to tend the fire. Is that alright? Purr.
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Doronbol:** Thanks! I'll use these five logs to keep the beacon burning while you're away.
              - [Choice]: No.
                - **Player:** I think I'll keep hold of my logs for now.
                - **Doronbol:** >Well, you know where I am if you change your mind.
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Doronbol has five logs:)
        - **Doronbol:** Of course I will - don't worry. I'll use the logs you've already left with me.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Doronbol:** Purrrr. Sure! Just have a peep at this map of mine.
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given Doronbol a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Doronbol:** Well, I might be short, but I can see very far indeed. I can tell you how many beacons are lit in either direction.
    - **Doronbol:** However, if you want to know about beacons beyond that, I’ll need the help of a creature whose eyes are even keener than mine.
    - **Player:** What sort of creature is that?
    - **Doronbol:** A creature that can view the world from above and which is smart enough to report back about what it has discovered.
    - **Player:** Yes, but what sort of creature, exactly?
    - **Doronbol:** Purr…a macaw.
    - **Player:** A macaw?
    - **Doronbol:** Yes, a yummy, delicious macaw. Purr.
    - **Player:** You’re just trying to trick me into bringing you a snack, aren’t you?
    - **Doronbol:** No, no. Sadly, if you brought me a macaw for the purpose of obtaining information about the beacons, my integrity as a fire tender would demand that I not make brunch of it.
    - ((If the player has a macaw pouch in their backpack:))
      - **Player:** I see. How very noble.
      - (continue|macaw)
  - [Choice]: How's it going?
    - **Player:** How's it going?
    - **Doronbol:** All's well, life is peaceful, the flowers are blooming, the birds are singing and it's the most lovely of days today.
    - **Player:** Wow, you seem very pleased about things!
    - **Doronbol:** I am! I'm so happy, I can't help but wag my tail and bound about recklessly!
    - **Doronbol:** It's nice to have such a high purpose in life and to have earned the trust and affection of such a noble human as King Roald.
    - **Player:** Wait - you're a cat, right? Not a dog in disguise?
    - **Doronbol:** Uh, by 'wag my tail' I meant...um...'purr really loudly'. And, just for the record, I'm, uh, thoroughly indifferent to humans. And aloof. I'm very, very aloof.
    - **Player:** That sounds more like it.
    - **Doronbol:** Say, you won't repeat what I said before, will you? I wouldn't want any more marks on my cat license.
    - **Player:** Don't worry, moggy; your secrets are safe with me.
    - **Doronbol:** Purrrrrrr!
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Doronbol:** Happy trails! Purrr.

### Using a macaw pouch on Doronbol


#### Before giving Doronbol a macaw pouch


##### Without a catspeak amulet

- (removes=macaw pouch)
- **Doronbol:** Mioaw. Miaow miaow miaow meeeeooow!

##### With a catspeak amulet

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=macaw pouch)
    - **Doronbol:** Thank you very much; what a delightful snack! You're so very considerate.
    - **Player:** Hey, wait! That's not why I brought you a macaw.
    - **Doronbol:** Oh, fine, whatever. Lucky for you, I've just had a big breakfast. I suppose I can use the macaw to give you more detailed information about the fire network, at least until I'm hungry again.
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Doronbol:** Shame. I could have used a snack.
    - **Player:** What was that?
    - **Doronbol:** Oh, nothing.

#### After giving Doronbol a macaw pouch

- **Player:** I've already given her a macaw; she doesn't need another.

### Using logs on Doronbol

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Doronbol does not have five logs:)
    - (Condition: If the confirmation prompt is enabled:)
      - [Menu]: Do you want to give five logs to the fire tender?
        - [Choice]: Yes.
          - (Condition: If the player does not have at least five logs of the same type:)
            - The fire tender needs five of the same type of log to maintain this fire.
          - (Condition: If the player has at least five logs of the same type:)
            - (removes=five logs)
            - You give the fire tender 5 [type] logs.
        - [Choice]: No.
          - **Player:** I think I'll hang on to my logs after all.
        - [Choice]: Yes. Please don't ask me for confirmation again.
          - (above|use-give-logs)
    - (Condition: If the confirmation prompt is disabled:)
      - (above|use-give-logs)
  - (Condition: If Doronbol has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed


#### Whether a catspeak amulet is equipped or not

- **Doronbol:** Oi! Get away from that! Until you've proven yourself a true ally of Varrock, you can't use that!
- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
