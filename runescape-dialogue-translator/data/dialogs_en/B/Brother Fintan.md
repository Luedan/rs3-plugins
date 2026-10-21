# Brother Fintan

- **Original Wiki Page**: [Transcript:Brother Fintan](https://runescape.wiki/w/Transcript%3ABrother%20Fintan)
- **Letter**: `B`

---

## Dialogue Transcript


### Talk-to


#### On free-to-play worlds

- **Player:** Hello there. Could I ask you about the-
- **Brother Fintan:**  Not at the moment, I'm afraid! It's not nearly safe enough to talk right now.
- **Player:** But you don't even know what I was going to ask!
- **Brother Fintan:**  Oh, I have enough of an idea to know that it's not safe enough to talk about it on a free world.

#### Before All Fired Up

- **Player:** Hello there! What might you be up to?
- **Brother Fintan:** Oh, I'm looking after this beacon for King Roald.
- **Player:** How is that working out for you?
- **Brother Fintan:** Oh, very well, thank you. The time away from the Monastery has given me opportunity to meditate and reflect on my path in life.
- **Player:** That sounds very spiritually fulfilling.
- **Brother Fintan:** It is, indeed. It's very satisfying to be able to look after one's spiritual needs while serving one's kingdom as well.

#### After All Fired Up


##### Without 53 Prayer

- **Brother Fintan:** Hail, traveler!
- **Player:** Yeah, hello. So, I was wondering if you might be able to help out...
- **Brother Fintan:** But of course I could, pilgrim! You look as if you could, indeed, use some guidance.
- **Player:** Excellent! So, here's the prob-
- **Brother Fintan:** Oh, but the problem is obvious; you're in need of spiritual development!
- **Player:** But, the beac-
- **Brother Fintan:** I am looking after the beacon, [brother/sister]. Have no worries about that. Focus on your inner development - that is what is of most importance.
- [53] Prayer before Brother Fintan will be willing to talk to you about non-spiritual matters.}}

##### With 53 Prayer or greater

- **Brother Fintan:** Hail, traveler! How can I help you?
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Brother Fintan:** Of course. Once the beacon is lit, just leave 5 logs with me and I'll take care of the fire for as long as I can.
    - (Condition: If the beacon is dying:)
      - **Brother Fintan:**  Well, I could, but since you're here, you might as well do it yourself.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Brother Fintan does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Brother Fintan:** I'm afraid you don't have enough of the right type of log for me to use.
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Brother Fintan:**  I'll need five logs to be able to tend the fire. Is that okay?
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Brother Fintan:** Thank you! I'll use these five logs to keep the beacon burning while you're away.
              - [Choice]: No.
                - **Player:** I think I'll keep hold of my logs for now.
                - **Brother Fintan:** Well, you know where I am if you change your mind.
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Brother Fintan has five logs:)
        - **Brother Fintan:** Of course I will; don't worry. I'll use the logs you've already left with me.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Brother Fintan:** Oh, but of course! Allow me to assist you by showing you my map.
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Brother Fintan:** I can tell you about the state of the beacons in either direction, up to the last fires that are lit.
    - **Brother Fintan:** I could probably tell you about the other beacons as well, but I'd need the help of a macaw.
    - **Player:** A macaw?
    - **Brother Fintan:** Yes. Macaws have the ability to fly high into the air and see things that are much further away.
    - **Brother Fintan:** They are also highly intelligent and can be trained to provide the exact information I'd need for a complete overview of the beacon network.
    - ((If the player has a macaw pouch in their backpack:))
      - **Brother Fintan:**  Come to think of it, the macaw you've got there in your pack would be perfect, for instance.
      - (continue|macaw)
  - [Choice]: How's it going?
    - **Player:** How's it going?
    - **Brother Fintan:** Oh, very well, thank you. The time away from the Monastery has given me opportunity to mediate and reflect on my path in life.
    - **Player:** That sounds very spiritually fulfilling.
    - **Brother Fintan:** It certainly is. I must admit, it's been very nice to spend some time outdoors. The Monastery is pretty stuffy this time of year, not to mention a bit boring.
    - **Player:** Oh?
    - **Brother Fintan:** Sometimes, I really wish I'd followed by heart when picking a career, but mother did want a monk in the family. It would have broken her heart.
    - **Brother Fintan:** Oh, but you won't tell the abbot I said so, will you? He would be so disappointed.
    - [Menu]: Select an Option
      - [Choice]: Of course I won't.
        - **Player:** Of course I won't.
        - **Brother Fintan:** I thank you.
      - [Choice]: It's not too late to take up another profession, you know.
        - **Player:** It's not too late to take up another profession, you know.
        - **Brother Fintan:** Do you really think so?
        - **Player:** Of course!
        - **Brother Fintan:** But, my dear mother...
        - **Player:** Well, what's to say that you can't be a monk AND do something else?
        - **Brother Fintan:** A monk and something else? I'd never considered that!
        - **Player:** For example, you seem to be doing a pretty good job at being both a monk and a professional fire tender at present.
        - **Brother Fintan:** You know, you're right! Thank you, Player, you've given me much to think about. I'm very grateful for your advice.
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Brother Fintan:** My, such assertiveness!

### Using a macaw pouch on Brother Fintan


#### Before giving Brother Fintan a macaw pouch{{Anchor|macaw}}

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=a macaw pouch)
    - **Brother Fintan:** Thank you very much. This macaw will help me give you more detailed information about the beacon network.
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Brother Fintan:** Suit yourself.

#### After giving Brother Fintan a macaw pouch

- **Player:** I've already given him a macaw; he doesn't need another.

### Using logs on Brother Fintan

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Brother Fintan does not have five logs:)
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
  - (Condition: If Brother Fintan has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
