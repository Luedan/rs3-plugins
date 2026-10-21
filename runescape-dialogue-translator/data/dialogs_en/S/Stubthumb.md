# Stubthumb

- **Original Wiki Page**: [Transcript:Stubthumb](https://runescape.wiki/w/Transcript%3AStubthumb)
- **Letter**: `S`

---

## Dialogue Transcript


### Talk-to


#### On free-to-play worlds

- **Player:**Hello there. Could I ask you about th-
- **Stubthumb:**Hmph! Don't you know anything? It not safe to talk right now.
- **Player:**But you don't even know what I was going to ask.
- **Stubthumb:**I know enough to know it not safe to talk unless we on members' world.

#### Before All Fired Up

- **Player:** Hi there!
- **Stubthumb:** Hmmph. Hi yourself.
- **Player:** That doesn't sound very friendly!
- **Stubthumb:** It hard to feel friendly when feet hurt.
- **Player:** I take your point. Have you tried, you know, just sitting down?
- **Stubthumb:** Sitting makes back hurt.
- **Player:** Ah. That is a dilemma.

#### After All Fired Up


##### Before giving him a davy kebbit hat

- **Player:** Hi there. I was wondering if you could help me out.
- **Stubthumb:** Sorry. Can't hear you. My ears too cold and my feet hurt.
- **Player:** How does your feet hurting stop you from hearing?
- **Stubthumb:** Am glad I can't hear - you sound very annoying.
- **Player:** Right. So, say I were to bring you - oh, I don't know - a nice, warm hat to cover your ears. Then would you be able to hear me?
- **Stubthumb:** If it were nice, warm, furry kebbit hat made by Frawd the ogress. Those very good to look at AND very warm.
- **Player:** You're not very subtle, you know.
- **Stubthumb:** What? Sorry. Ears too cold to hear you and all.

##### Giving him a davy kebbit hat

- **Stubthumb:** Oh, kebbit hat! That exactly what I always wanted. It would be perfect thing to keep wind out of hair.
- **Player:** What hair? You don't have any hair!
- **Stubthumb:** Are you going to give it or are you here to taunt me?
- [Menu]: Select an Option
  - [Choice]: Go ahead and take it.
    - (removes=davy kebbit hat)
    - **Stubthumb:** Thank you very much. It fit like dream! My ears so warm now.
    - **Player:** Glad you like it. It suits you to a 'T'.
    - **Stubthumb:** Very grateful. I in your debt, human.
  - [Choice]: Sorry, I just brought it here to taunt you.
    - **Player:** Sorry, I just brought it here to taunt you.
    - **Stubthumb:** Harrumph. It good thing my ears too cold to hear you or I'd get real angry.

##### After giving him a davy kebbit hat

- **Stubthumb:** Hmph, it's you. Thanks much for great hat. Anything you want in return?
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Stubthumb:** Of course. Once you light beacon, give me 5 logs and I make fire burn long time.
    - (Condition: If the beacon is dying:)
      - **Stubthumb:**  I only look after blazing fire. You deal with dying fire yourself!
    - (Condition: If the beacon is not dying:)
      - (Condition: If Stubthumb does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Stubthumb:** How can I tend fire for you? You don't have enough good logs for me to use!
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Stubthumb:** Need five logs to tend fire. Okay?
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Stubthumb:** Thanks. I use these five logs to keep beacon burning while you away.
              - [Choice]: No.
                - **Player:**  I think I'll keep hold of my logs for now.
                - **Stubthumb:** Well. You know where I am if you change your mind.
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Stubthumb has five logs:)
        - **Stubthumb:** Of course. I use logs you already left here.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Stubthumb:** Yes, well, if you must, have look at map.
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Stubthumb:** Hmm, what you saying? Dat my eyes aren't good? They much better than yours! I can tell you about all beacons in either direction, as long as they lit.
    - **Player:** Yes, but what about beacons that aren't lit?
    - **Stubthumb:** I could tell about the other beacons as well, if I have help from macaw.
    - **Player:** A macaw?
    - **Stubthumb:** Yes. Macaws can fly high into air and see long distance. They also very smart creature.
    - **Stubthumb:** Can fly into air and then report back about whole beacon network.
    - ((If the player has a macaw pouch in their backpack:))
      - **Stubthumb:** Hey, you holding a macaw. You give macaw, I tell you about other beacons, too.
      - (continue|macaw)
  - [Choice]: How's it going?
    - **Player:** How's it going?
    - **Stubthumb:** Awful! Why you ask such stupid questions?
    - **Player:** That doesn't sound very friendly!
    - **Stubthumb:** It hard to be friendly when feet hurt.
    - **Player:** I take your point. Have you tried, you know, just sitting down?
    - **Stubthumb:** Sitting makes back hurt.
    - **Player:** Ah. That is a dilemma.
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Stubthumb:** Hmmph.

### Using a macaw pouch on Stubthumb


#### Before giving Stubthumb a macaw pouch{{Anchor|macaw}}

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=a macaw pouch)
    - **Stubthumb:** Thanks. Macaw help me tell you more about other beacons.
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Stubthumb:** Suit yourself.

#### After giving Stubthumb a macaw pouch

- **Player:** I've already given him a macaw; he doesn't need another.

### Using logs on Stubthumb

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Stubthumb does not have five logs:)
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
  - (Condition: If Stubthumb has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
