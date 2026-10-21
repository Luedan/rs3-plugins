# Waldo

- **Original Wiki Page**: [Transcript:Waldo](https://runescape.wiki/w/Transcript%3AWaldo)
- **Letter**: `W`

---

## Dialogue Transcript


### Talk-to


#### On free-to-play worlds

- **Player:** Hello there. Could I ask you about the-
- **Waldo:** Not at the moment, I'm afraid! It's not nearly safe enough to talk right now.
- **Player:** But you don't even know what I was going to ask!
- **Waldo:** Oh, I have enough of an idea to know that it's not safe enough to talk about it on a free world.

#### Before All Fired Up

- **Player:** So, what are you up to, this fine day?
- **Waldo:** Oh, just tending this fire.
- **Player:** What fire? I don't see any fire.
- **Waldo:** Oh, it is not lit yet.
- **Player:** So, you're just standing here, watching an empty fire pit?
- **Waldo:** Of course not. When tending a beacon, it's much more important to watch your surroundings than to watch the fire itself.
- **Player:** It is?
- **Waldo:** Of course. One must be constantly vigilant for any sign of danger. In fact, talking to you is distracting me a bit from duties to the kingdom. I'm afraid I'll have to say goodbye now.
- **Player:** Oh, right. Sorry.

#### After All Fired Up


##### Before completing the Grand Exchange tutorial

- **Player:** Hello there. I was wondering if you could help me out...
- **Waldo:** I suppose I could, but I must admit, I feel a bit intimidated talking to someone who looks so brave and adventurous.
- **Player:** Are you being serious?
- **Waldo:** Oh, quite serious. I don't feel we have enough in common for me to even begin to be able to have a conversation with you.
- **Player:** So, ignoring the fact that we are, in fact, having a conversation at this very moment, are you saying that you'd help me out if... we shared some interests?
- **Waldo:** That's exactly it.
- **Player:**So, what are you interested in, then?
- **Waldo:** Well, perhaps if you learned more about the exciting world of trade and commerce, I'd feel more able to talk to you.
- **Player:** You are a very strange individual.
- **Waldo:** That sort of comment doesn't help, you know.
- [Grand Exchange].}}

##### After completing the Grand Exchange tutorial

- **Waldo:** Hello. Is there anything with which I can help you?
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Waldo:** Of course. Once the beacon is lit, just leave 5 logs with me and I'll take care of the fire for as long as I can.
    - (Condition: If the beacon is dying:)
      - **Waldo:**  Well, I could, but since you're here, you might as well do it yourself.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Waldo does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Waldo:** I'm afraid you don't have enough of the right type of logs for me to use.
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Waldo:** I'll need five logs to be able to tend the fire. Is that alright? Purr.
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Waldo:** Thanks! I'll use these five logs to keep the beacon burning while you're away.
              - [Choice]: No.
                - **Player:** I think I'll keep hold of my logs for now.
                - **Waldo:** Well, you know where I am if you change your mind.
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Waldo has five logs:)
        - **Waldo:** Of course I will; don't worry. I'll use the logs you've already left with me.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Waldo:** Oh, yes. Perhaps it would be easiest for me to show you on my map...
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given Waldo a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Waldo:** I can tell you about the state of the beacons in either direction, up to the last fires that are lit.
    - **Waldo:** I could probably tell you about the other beacons as well, but I'd need the help of a macaw.
    - **Player:** A macaw?
    - **Waldo:** Yes. Macaws have the ability to fly high into the air and see things that are much further away.
    - **Waldo:** They are also highly intelligent and can be trained to provide the exact information I'd need for a complete overview of the beacon network.
    - ((If the player has a macaw pouch in their backpack:))
      - **Waldo:**  Come to think of it, the macaw you've got there in your pack would be perfect, for instance.
      - (continue|macaw)
  - [Choice]: How's it going?
    - **Player:** How's it going?
    - **Waldo:** Not bad, not bad.
    - **Player:** So, what are you up to, this fine day?
    - **Waldo:** Oh, the usual.
    - **Player:** What's 'the usual'?
    - **Waldo:** Well, I'm keeping close watch for signs of danger and I'm constantly scanning the horizon for the glow of other beacons.
    - **Player:** Is that all you think about?
    - **Waldo:** Oh, no. It's quite important to keep the mind active in a job like this. If you get lazy in your thinking, you might get lazy in your observation.
    - **Player:** Intriguing... So, what do you think about to keep your mind active?
    - **Waldo:** Oh, I suppose I mostly think about my stamp collection.
    - **Player:** Mostly?
    - **Waldo:** I also think about the birds I've seen lately.
    - **Player:** Birds? You think about birds?
    - **Waldo:** Yes. I am an avid ornithologist.
    - **Player:** You like birdwatching, eh? You must see a lot of birds on the job!
    - **Waldo:** Oh, quite. It's very convenient to have a hobby that integrates so well with one's career.
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Waldo:** Then keep your voice down. You'll scare away the birds.

### Using a macaw pouch on Waldo


#### Before giving Waldo a macaw pouch{{Anchor|macaw}}

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=a macaw pouch)
    - **Waldo:** Thank you very much. This macaw will help me give you more detailed information about the beacon network.
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Waldo:** Suit yourself.

#### After giving Waldo a macaw pouch

- **Player:** I've already given him a macaw; he doesn't need another.

### Using logs on Waldo

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Waldo does not have five logs:)
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
  - (Condition: If Waldo has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Waldo:**  Oi! Get away from that! Until you've proven yourself a true ally of Varrock, you can't use that!
- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
