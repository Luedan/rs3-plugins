# Orry

- **Original Wiki Page**: [Transcript:Orry](https://runescape.wiki/w/Transcript%3AOrry)
- **Letter**: `O`

---

## Dialogue Transcript


### Talk-to


#### On free-to-play worlds

- **Player:** Hello there. Could I ask you about the-
- **Orry:** Not at the moment, [dude/dudette]! It's not nearly safe enough to talk right now.
- **Player:** But you don't even know what I was going to ask!
- **Orry:** Oh, I have enough of an idea to know that it's not safe enough to talk about it on a free world.

#### Before All Fired Up

- **Player:** Hi there! What are you up to today?
- **Orry:** Man, I'd just be chillin', takin' it easy, like, but there's so much to do.
- **Player:** Oh? Like what?
- **Orry:** Sorry, [dude/dudette], I know it's a total bummer, but I've got to focus right now. Catch ya later, yeah?
- **Player:** Oh, sure. Good luck with everything.

#### After All Fired Up


##### Before Family Crest

- **Player:** Hi, there. I was wondering if you could help me ou-
- **Orry:** Like, I can't possibly tune in to your wavelength right now, man! I'm way too angstin'.
- **Player:** What's wrong?
- **Orry:** It's my friend, , in the Jolly Boar, like. He's really ailin', and I'm stuck watchin' this beacon so I can't help out.
- **Player:** I'm sorry to hear that. If it hel-
- **Orry:** Look, just don't even talk to me, okay? I need some head space, like. 's my best friend, man.
- [Family Crest] quest.}}

##### After Family Crest

- **Orry:** Hey, [dude/dudette]. What's up?
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Orry:** Of course. Once the beacon is lit, just leave 5 logs with me and I'll take care of the fire for as long as I can.
    - (Condition: If the beacon is dying:)
      - **Orry:**  Well, I could, but since you're here, you might as well do it yourself.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Orry does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Orry:** 'Fraid you don't have enough of the right type of log for me to use.
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Orry:** [Dude/dudette], I'll need, like, five logs to tend the fire for you. Is that cool?
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Orry:** Ace! I'll use these five logs to keep the beacon burning while you're away.
              - [Choice]: No.
                - **Player:** I think I'll keep hold of my logs for now.
                - **Orry:** Well, you know where I am if you change your mind, yeah?
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Orry has five logs:)
        - **Orry:** Of course [dude/dudette]; no worries. I'll use the logs you've already left with me.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Orry:** Sure thing, [dude/dudette]! Just point your peepers at this awesome map of mine.
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Orry:** My eyes are pretty awesome - I can tell you all about the beacons in either direction, like, as long as the fires are lit.
    - **Orry:** To tell you about the other ones, I'd need the help of a macaw, like.
    - **Player:** A macaw?
    - **Orry:** Yeah. Macaws can fly high into the air and see things that are much further away, like.
    - **Orry:** They are also highly intelligent and can be trained up to, like, to return with the exact information I'd need to tell you everything about the beacon network.
    - ((If the player has a macaw pouch in their backpack:))
      - **Orry:** Come to think of it, the macaw you've got there in your pack would be perfect, like.
      - (continue|macaw)
  - [Choice]: How's it going?
    - **Player:** How's it going?
    - **Orry:** Man, I'd just be chillin', takin' it easy, like, but there's so much to do!
    - **Player:** Oh? Like what?
    - **Orry:** Well, there's these beacons, man. They need lookin' after.
    - **Player:** Isn't it exhausting, constantly keeping your eyes peeled like that?
    - **Orry:** Well, actually, staring intently at anything for too long can be a strain on one's eyes.
    - **Orry:** And when I'm not doin' that, I need to keep the peepers glued to the horizon, constantly watching for signs of trouble.
    - **Player:** That does sound like a lot of work!
    - **Orry:** Totally, like. Can't wait to meet up with Jonathan later at the Jolly Boar - I'm *parched*!
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Orry:** Harsh, [dude/dudette]!

### Using a macaw pouch on Orry


#### Before giving Orry a macaw pouch{{Anchor|macaw}}

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=a macaw pouch)
    - **Orry:** Thank you very much. This macaw will help me give you more detailed information about the beacon network.
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Orry:** Suit yourself.

#### After giving Orry a macaw pouch

- **Player:** I've already given him a macaw; he doesn't need another.

### Using logs on Orry

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Orry does not have five logs:)
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
  - (Condition: If Orry has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Orry:**  Oi! Get away from that! Until you've proven yourself a true ally of Varrock, you can't use that!
- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
