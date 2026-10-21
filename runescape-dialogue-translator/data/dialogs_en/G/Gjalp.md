# Gjalp

- **Original Wiki Page**: [Transcript:Gjalp](https://runescape.wiki/w/Transcript%3AGjalp)
- **Letter**: `G`

---

## Dialogue Transcript


### Talk-to


#### On free-to-play worlds

- You need to be on a members' world to access this content.
- (pop-up)
  - {{Pop-up|You need to be on a members' world to access this content.|colour=#EBE0BC|shadow=no}}

#### Before All Fired Up

- **Gjalp:** I'm busy here. No time to chat.
- **Player:** You don't look busy to me.
- **Gjalp:** How little you understand.
- **Player:** Exactly what I don't understand, then?
- **Gjalp:** It take too long to explain.
- **Player:** Well, I've got nothing urgent I need to do - please explain.
- **Gjalp:** It not worth it. You annoy me, be off with you!
- **Player:** Right, I'll see you later then, shall I?
- **Gjalp:** Begone!
- **Player:** Bye!
- **Gjalp:** BEGONE!

#### After All Fired Up


##### Without having completed the Stronghold of Security

- **Gjalp:** You waste my time.
- **Player:** Pardon me?
- **Gjalp:** I need to keep sharp eyes peeled on horizon, not talk to likes of you.
- **Player:** But, I'm here to help test the beacon network for King Roald!
- **Gjalp:** You? You who know nothing of security?
- **Player:** Bu-
- **Gjalp:** No 'buts'! You go gain some experience of world around you, *then* come back to talk of helping.
- [Stronghold of Security].}}

##### Having completed the Stronghold of Security

- **Gjalp:** Hi. What you want?
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Gjalp:** Of course. Once you light the beacon, give me 5 logs and I make fire burn long time.
    - (Condition: If the beacon is dying:)
      - **Gjalp:** I only look after blazing fire. You deal with dying fire yourself!
    - (Condition: If the beacon is not dying:)
      - (Condition: If Gjalp does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Gjalp:** How you expect me to tend fire for you? You not have enough good logs for me to use!
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Gjalp:** I need five logs to tend fire for you. Okay?
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Gjalp:** Thanks. I use these five logs to keep beacon burning whilst you away.
              - [Choice]: No.
                - **Player:** I think I'll keep hold of my logs for now.
                - **Gjalp:** Hmph. You know where I am if you change your mind.
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Gjalp has five logs:)
        - **Gjalp:** Of course. I use logs you left with me before.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Gjalp:** Yes. Have a look at my map.
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Gjalp:** Hmm. My eyes good. Can tell you about all beacons in either direction, as long as they lit.
    - **Gjalp:** I could tell about the other beacons as well, if I have help of macaw.
    - **Player:** A macaw?
    - **Gjalp:** Yes. Macaw can fly high into air and see long distance. They also very smart creatures.
    - **Gjalp:** Macaw can fly into air and then report back about whole beacon network.
    - ((If the player does not have a macaw pouch in their backpack:))
      - **Gjalp:** If you give me a macaw, I can tell you about other beacons, too.
    - ((If the player has a macaw pouch in their backpack:))
      - **Gjalp:** Hey, you holding a macaw, right there. You give macaw, I tell you about other beacons, too.
      - (continue|macaw)
  - [Choice]: How's it going?
    - **Player:** How's it going?
    - **Gjalp:** Very, very quiet. No danger in sight.
    - **Player:** That's great!
    - **Gjalp:** On contrary. Then when danger is greatest! Nothing more dangerous than danger one can't see or hear.
    - **Gjalp:** Now, unless you have good questions, becone. I must watch and listen.
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Gjalp:** Then leave me be! I have more important things to do than listen to you continue speaking.

### Using a macaw pouch on Gjalp


#### Before giving Gjalp a macaw pouch{{Anchor|macaw}}

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=a macaw pouch)
    - **Gjalp:** Thank you very much. This macaw will help me give you more detailed information about the beacon network.
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Gjalp:** Suit yourself.

#### After giving Gjalp a macaw pouch

- **Player:** I've already given her a macaw; she doesn't need another.

### Using logs on Gjalp

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Gjalp does not have five logs:)
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
  - (Condition: If Gjalp has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Gjalp:** Oi! Get away from that! Until you've proven yourself a true ally of Varrock, you can't use that!
- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
