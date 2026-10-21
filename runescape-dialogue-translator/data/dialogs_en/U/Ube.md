# Ube

- **Original Wiki Page**: [Transcript:Ube](https://runescape.wiki/w/Transcript%3AUbe)
- **Letter**: `U`

---

## Dialogue Transcript


### Talk-to


#### On free-to-play worlds

- **Player:** Hello there. Could I ask you about the-
- **Ube:** Not at the moment, I'm afraid! It's not nearly safe enough to talk right now.
- **Player:** But you don't even know what I was going to ask!
- **Ube:** Oh, I have enough of an idea to know that it's not safe enough to talk about it on a free world.

#### Before All Fired Up

- **Player:** Hi there. What are you doing here?
- **Ube:** I'm afraid that I don't have much time to chat right now.
- **Player:** Really? You don't seem to be doing anything but standing around.
- **Ube:** Well, that's where your eyes deceive you! I'm not only standing around, I'm also scanning the horizon. It takes a lot of energy and concentration to remain prepared for emergencies.
- **Player:** I see.

#### After All Fired Up


##### Before giving her a white fruit

- **Ube:** Hello, traveller! Could I impose on you for a moment?
- **Player:** What is it?
- **Ube:** Well, I'm supposed to be looking after these beacons, but I'm utterly exhausted. Constantly scanning the horizon is hard work.
- **Ube:** I've heard that the fruit from the White Tree can pep one up a bit. Is there any way you could bring me one? I'd be eternally grateful.
- [Menu]: Select an Option
  - [Choice]: I'd be happy to help.
    - **Player:** I'd be happy to help. The safety of the kingdom is paramount, after all.
    - **Ube:** Thank you very much. I'm worried that if I carry on on this state, I might miss something important.
  - [Choice]: Sorry, I'm busy at the moment.
    - **Player:** Sorry, I'm busy at the moment.
    - **Ube:** Ah, well. It costs nothing to ask.

##### Giving her a white fruit

- **Ube:** Hello, traveller! Look, I hate to be rude, but is that the aroma of White Tree fruit I smell?
- **Player:** It might be.
- **Ube:** You wouldn't happen to have one on you going spare, would you? I'm utterly exhausted and could really use a pick-me-up.
- [Menu]: Select an Option
  - [Choice]: Of course; I brought one just for you.
    - **Player:** Of course; I brought one just for you.
    - (removes=white tree fruit)
    - **Ube:** Thank you ever so much. I can't tell you how much I was craving White Tree fruit.
    - **Player:** Glad to help.
    - **Ube:** Should I ever be able to repay the favour, just let me know.
  - [Choice]: Sorry, I can't help you right now.
    - **Player:** Sorry, I can't help you right now.
    - **Ube:** Ah, well. It costs nothing to ask.

##### After giving her a white fruit

- **Ube:** Hello. Can I help you at all?
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Ube:** Of course. Once the beacon is lit, just leave 5 logs with me and I'll take care of the fire for as long as I can.
    - (Condition: If the beacon is dying:)
      - **Ube:**  Well, I could, but since you're here, you might as well do it yourself.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Ube does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Ube:** I'm afraid you don't have enough of the right type of log for me to use.
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
          - **Ube:** I'll need five logs to be able to tend the fire. Is that okay?
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Ube:** Thank you! I'll use these five logs to keep the beacon burning while you're away.
              - [Choice]: No.
                - **Player:** I think I'll keep hold of my logs for now.
                - **Ube:** Well, you know where I am if you change your mind.
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Ube has five logs:)
        - **Ube:** Of course I will, don't worry, I'll use the logs you've already left with me.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Ube:** But of course. Just have a look at my map.
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Ube:** I can tell you about the state of the beacons in either direction, up to the last fires that are lit.
    - **Ube:** I could probably tell you about the other beacons as well, but I'd need the help of a macaw.
    - **Player:** A macaw?
    - **Ube:** Yes. Macaws have the ability to fly high into the air and see things that are much further away.
    - **Ube:** They are also highly intelligent and can be trained to provide the exact information I'd need for a complete overview of the beacon network.
    - ((If the player has a macaw pouch in their backpack:))
      - **Ube:** Come to think of it, the macaw you've got there in your pack would be perfect.
      - (continue|macaw)
  - [Choice]: How's it going?
    - **Player:** How's it going?
    - **Ube:** Pretty good, for the most part. I've done quite a lot of looking at the horizon today - it's quite hard work.
    - **Player:** Have you seen anything worrying?
    - **Ube:** Not so far, thankfully, but one has to stay constantly vigilant for threats coming from the north.
    - **Player:** Isn't it exhausting, constantly keeping your eyes peeled like that?
    - **Ube:** Well, actually, staring intently at anything for too long can be a strain on one's eyes.
    - **Ube:** I take a little break every hour or so and look away from the horizon for a few minutes, just to rest my eyes.
    - **Player:** Oh? What do you look at, then?
    - **Ube:** Well, actually, I'm also using this opportunity to increase my knowledge about local moulds and fungi.
    - **Player:** Are you being serious?
    - **Ube:** Not only can I spot danger from miles away, but I'm the quickest identifier of bread moulds this side of the River Lum!
    - **Player:** That's a...unique claim to fame.
    - **Ube:** I'm quite proud of it, really. I'm hoping to branch out to yeasts next, then mushrooms.
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Ube:** Fine! I'm done talking to you, too, then.

### Using a macaw pouch on Ube


#### Before giving Ube a macaw pouch{{Anchor|macaw}}

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=a macaw pouch)
    - **Ube:** Thank you very much. This macaw will help me give you more detailed information about the beacon network.
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Ube:** Suit yourself.

#### After giving Ube a macaw pouch

- **Player:** I've already given her a macaw; she doesn't need another.

### Using logs on Ube

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Ube does not have five logs:)
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
  - (Condition: If Ube has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
