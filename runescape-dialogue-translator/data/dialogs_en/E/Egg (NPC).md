# Egg (NPC)

- **Original Wiki Page**: [Transcript:Egg (NPC)](https://runescape.wiki/w/Transcript%3AEgg%20%28NPC%29)
- **Letter**: `E`

---

## Dialogue Transcript


### Talk-to


#### Before All Fired Up

- **Player:** So, what exactly are you doing up here, all by yourself.
- **Egg:** Oh, me keeping very close watch on horizon - it very important job, keeping watch for king.
- **Player:** Don't you ever get lonely?
- **Egg:** Oh, not at all. There lots of rocks and sticks to talk to - dey make very good company.
- **Player:** You talk to rocks and sticks?
- **Egg:** Yeah, dey very good listeners.
- **Player:** Well, I can't argue with that.

#### After All Fired Up


##### Without having completed Troll Romance and My Arm's Big Adventure

- **Player:** So, what exactly are you doing up here, all by yourself?
- **Egg:** Der usual. Watch fire. Watch horizon. Watch fire some more.
- **Player:** Sounds absolutely thrilling. Look, not to change the subject, but is there any way you could help me out? I've got a couple of questions.
- **Egg:** Hmm, not so sure. Maybe if you help trolls, me help you.
- **Player:** Oh but I'm a great friend of the trolls. Just ask anybo- I mean any troll.
- **Egg:** Don't know. I think about it. Meanwhile, leave me alone and let me get back to watching fire.
- [My Arm's Big Adventure] in order to earn Egg's trust.}}

##### Having also completed Troll Romance and My Arm's Big Adventure

- **Egg:** Oh, hello. What you want?
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Egg:** Yes. Once beacon lit, leave 5 logs with me and I take care of fire for while.
    - (Condition: If the beacon is dying:)
      - **Egg:** I could, but fire dying out now. You make it blaze again, then I look after it for you.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Egg does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Egg:** How can I tend fire for you? You not have enough good logs for me!
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Egg:** Need five logs to tend fire. That okay with you?
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Egg:** Thanks. I use these five logs to keep beacon burning while you away.
              - [Choice]: No.
                - **Player:** I think I'll keep hold of my logs for now.
                - **Egg:** Okay. You know where I am if you change mind.
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Egg has five logs:)
        - **Egg:** Of course. I use logs you already left with me.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Egg:** Here you go. Have look at my map.
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Egg:** Hmm, me have sharp eyes, can see very far. Can tell you about all lit beacons in both directions from here. But, little flappy macaw can see much further still.
    - **Player:** Flappy macaw?
    - **Egg:** If you brings Egg a little flappy macaw, I tell you anything you want to know about ALL de beacons!
    - **Egg:** Macaw can fly high into air and see long distance. They smart enough to report about things very much far away.
    - ((If the player has a macaw pouch in their backpack:))
      - **Egg:** You have macaw there in your pack. You give macaw, I tell you about other beacons.
      - (continue|macaw)
  - [Choice]: How's it going?
    - **Player:** How's it going?
    - **Egg:** Oh, it going great! Nice, rocky mountain. Nice, scenic dirt. Best of all, it a nice, quiet day - so far, no danger in sight, though me not stop looking.
    - **Player:** So, what exactly are you doing up here, all by yourself.
    - **Egg:** Oh, me keeping very close watch on horizon - it very important job, keeping watch for king.
    - **Player:** Don't you ever get lonely?
    - **Egg:** Oh, not at all. There lots of rocks and sticks to talk to - dey make very good company.
    - **Player:** You talk to rocks and sticks?
    - **Egg:** Yeah, dey very good listeners.
    - **Player:** Well, I can't argue with that.
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Egg:** Goodbye den, little human.

### Using a macaw pouch on Egg


#### Before giving Egg a macaw pouch{{Anchor|macaw}}

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=a macaw pouch)
    - **Egg:** Thank you. Macaw help me tell you more about de other beacons.
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Egg:** Fine.

#### After giving Egg a macaw pouch

- **Player:** I've already given her a macaw; she doesn't need another.

### Using logs on Egg

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Egg does not have five logs:)
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
  - (Condition: If Egg has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Egg:** Oi! Get away from that! Until you've proven yourself a true ally of Varrock, you can't use that!
- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
