# Crate (NPC)

- **Original Wiki Page**: [Transcript:Crate (NPC)](https://runescape.wiki/w/Transcript%3ACrate%20%28NPC%29)
- **Letter**: `C`

---

## Dialogue Transcript


### Talk-to


#### On free-to-play worlds

- **Player:** Hello there. Could I ask you about th-
- **Crate:** No. It too hush-hush for talking about right now.
- **Player:** But you don't even know what I was going to ask!
- **Crate:** I know enough to know it not safe to talk unless we on members' world.

#### Before All Fired Up

- **Crate:** What you doing here? No one told Crate to expect visitors!
- **Player:** Huh? Wait, what's going on here?
- **Crate:** Not authorised to tell. It too important.
- **Player:** Well, it looks like you're just standing around, daydreaming about rocks.
- **Crate:** It much more important - and top secret! Crate too important troll to talk to likes of you.
- **Player:** Okay, fine. Catch you later.

#### After All Fired Up


##### Before giving him a cave eel

- **Crate:** What you doing here? No one told Crate to expect visitors!
- **Player:** I'm helping King Roald test the fire beacon network.
- **Crate:** Hmph, no one tell me about it. But, while you here, maybe you could be of use.
- **Player:** How so?
- **Crate:** I very hungry. Want some lava eel. You bring some to me.
- **Player:** What? I'm not an errand [boy/girl]! I'm here to help test these beacons.
- **Crate:** We talk about that later. For now, me hungry. You bring some lava eel for me or not?
- [Menu]: Select an Option
  - [Choice]: Fine, I'll bring you some lava eel.
    - **Player:** Fine, I'll bring you some lava eel.
    - **Crate:** Good. And hurry. It matter of great importance.
    - **Player:** Sure.
  - [Choice]: Keep dreaming!
    - **Player:** Keep dreaming!
    - **Crate:** Then begone, before I lose temper.

##### Giving him a cave eel

- **Crate:** Halt! Who goes there?
- **Player:** Oh, don't worry, it's just me.
- **Crate:** Do I know you? Are you supposed to be here? Wait minute, I smell lave eel! Is dat for me?
- [Menu]: Select an Option
  - [Choice]: Yes, it's all yours, if you want it.
    - **Player:** Yes, it's all yours, if you want it.
    - (Condition: If the player has both raw and cooked lava eels in backpack:)
      - [Menu]: Which lava eel do you want to give to Crate?
        - [Choice]: Raw.
          - (below)
        - [Choice]: Cooked.
          - (below)
    - (Condition: If the player has either only raw or only cooked lava eels in backpack:)
      - (removes=raw lava eel or cooked lava eel)
      - **Crate:** Thank you very much. Lava eel my very favourite.
      - **Player:** Glad you like it.
      - **Crate:** Very grateful. If you need any help, let me know.
  - [Choice]: Nope, it's all for me.
    - **Player:** Nope, it's all for me.
    - **Crate:** Then begone, before I lose temper.

##### After giving him a cave eel

- **Crate:** Hi, what you doing here again? You want something?
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Crate:** Yes. Once beacon lit, leave 5 logs with me and I take care of fire for while.
    - (Condition: If the beacon is dying:)
      - **Crate:** I could, but fire dying out now. You make it blaze again, then I look after it for you.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Crate does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Crate:** How can I tend fire for you? You not have enough good logs for me to use!
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Crate:** Need five logs to tend fire. That okay?
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Crate:** Thanks. I use these five logs to keep beacon burning while you away.
              - [Choice]: No.
                - **Player:** I think I'll keep hold of my logs for now.
                - **Crate:** Fine. You know where I am if you change mind.
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Crate has five logs:)
        - **Crate:** Of course. I use the logs you already left here.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Crate:** Well, have look at my map, then. But hurry up.
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Crate:** Hmm, me have sharp eyes, can see very far. Can tell you all about lit beacons in both directions from here. But, little flappy macaw can see much further still.
    - **Player:** Flappy macaw?
    - **Crate:** If you brings Crate a little flappy macaw, I tell you anything you want to know about ALL de beacons!
    - **Crate:** Macaw can fly high into air and see long distance. They smart enough to report about things very much far away.
    - ((If the player has a macaw pouch in their backpack:))
      - **Crate:** You have macaw there in your pack. You give macaw, I tell you about other beacons, too.
      - (continue|macaw)
  - [Choice]: How's it going?
    - **Player:** How's it going?
    - **Crate:** Hmm, pressure of job very great, but I strong and eyes are sharp. They only pick very important trolls for this sort of job.
    - **Player:** You must feel very proud.
    - **Crate:** Of course. But, having so many trolls respect me and having so much work to do make me very, very hungry.
    - **Player:** Hmm, must be difficult.
    - **Crate:** Oh, it is. Someone like you could never understand.
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Crate:** Hmph.

### Using a macaw pouch on Crate


#### Before giving Crate a macaw pouch{{Anchor|macaw}}

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=a macaw pouch)
    - **Crate:** Thank you. Macaw help me tell you more about de other beacons.
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Crate:** Fine.

#### After giving Crate a macaw pouch

- **Player:** I've already given him a macaw; he doesn't need another.

### Using logs on Crate

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Crate does not have five logs:)
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
  - (Condition: If Crate has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Crate:** Oi! Get away from that! Until you've proven yourself a true ally of Varrock, you can't use that!
- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
