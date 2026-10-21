# Squire Fyre

- **Original Wiki Page**: [Transcript:Squire Fyre](https://runescape.wiki/w/Transcript%3ASquire%20Fyre)
- **Letter**: `S`

---

## Dialogue Transcript


### Talk-to


#### On free-to-play worlds

- **Player:** Hello there. Could I ask you about the-
- **Squire Fyre:** Not at the moment, I'm afraid! It's not nearly safe enough to talk right now.
- **Player:** But you don't even know what I was going to ask!
- **Squire Fyre:** Oh, I have enough of an idea to know that it's not safe enough to talk about it on a free world.

#### Before All Fired Up

- **Player:** So, I'm curious. What are you doing up here and what's that interesting contraption?
- **Squire Fyre:** Well, it's all part of King Roald's new security initiative.
- **Player:** Security initiative? That sounds intriguing. What's going on?
- **Squire Fyre:** I'm afraid that I can't discuss it in detail at present, but if you're that interested, have a chat with the king. Last I heard, we needed some extra hands on deck.
- **Player:** Thanks, I just might.

#### After All Fired Up

- **Squire Fyre:** Hello again! And what might I be able to do for you today?
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Squire Fyre:** Of course. Once the beacon is lit, just leave 5 logs with me and I'll take care of the fire for as long as I can.
    - (Condition: If the beacon is dying:)
      - **Squire Fyre:** Well, I could, but since you're here, you might as well do it yourself.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Squire Fyre does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Squire Fyre:** I'm afraid you don't have enough of the right type of log for me to use.
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Squire Fyre:**  I'll need five logs to be able to tend the fire. Is that okay?
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Squire Fyre:** Thank you! I'll use these five logs to keep the beacon burning while you're away.
              - [Choice]: No.
                - **Player:** I think I'll keep hold of my logs for now.
                - **Squire Fyre:** Well, you know where I am if you change your mind.
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Squire Fyre has five logs:)
        - **Squire Fyre:** Of course I will; don't worry. I'll use the logs you've already left with me.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Squire Fyre:** But, of course! Just have a look at my map.
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Squire Fyre:** I can tell you about the state of the beacons in either direction, up to the last fires that are lit.
    - **Squire Fyre:** I could probably tell you about the other beacons as well, but I'd need the help of a macaw.
    - **Player:** A macaw?
    - **Squire Fyre:** Yes. Macaws have the ability to fly high into the air and see things that are much further away.
    - **Squire Fyre:** They are also highly intelligent and can be trained to provide the exact information I'd need for a complete overview of the beacon network.
    - ((If the player has a macaw pouch in their backpack:))
      - **Squire Fyre:** Come to think of it, the macaw you've got there in your pack would be perfect.
      - (continue|macaw)
  - [Choice]: How's it going?
    - **Player:** How's it going?
    - **Squire Fyre:** Very well, thank you. We're ever so grateful for your help in testing the beacon network.
    - **Player:** Oh, it was no big deal. You're doing most of the hard work, standing watch like that.
    - **Squire Fyre:** To be honest, I'd intended to become an 'Arcanist', but due to an administrative error, I ended up being put forward as an 'Arsonist'.
    - **Player:** Go figure.
    - **Squire Fyre:** Still, things worked out for the best. It's a great honour to play such an important role in protecting the kingdom.
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Squire Fyre:** Goodbye, then. Stop by again if you're in the neighbourhood - it's nice to have the company.

### Using a macaw pouch on Squire Fyre


#### Before giving Squire Fyre a macaw pouch{{Anchor|macaw}}

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=a macaw pouch)
    - **Squire Fyre:** Thank you very much. This macaw will help me give you more detailed information about the beacon network.
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Squire Fyre:** Suit yourself.

#### After giving Squire Fyre a macaw pouch

- **Player:** I've already given her a macaw; she doesn't need another.

### Using logs on Squire Fyre

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Squire Fyre does not have five logs:)
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
  - (Condition: If Squire Fyre has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
