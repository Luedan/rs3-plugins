# Nanuq

- **Original Wiki Page**: [Transcript:Nanuq](https://runescape.wiki/w/Transcript%3ANanuq)
- **Letter**: `N`

---

## Dialogue Transcript

{{Incomplete|Missing dialogue for having 81 Summoning but before All Fired Up}}

### Talk-to


#### Before All Fired Up


##### Without 81 Summoning

- **Nanuq:** Grrrrrrrrrrr. Groooowliowlioooo!

##### With 81 Summoning

- {{transcript missing}}

#### After All Fired Up


##### Without 81 Summoning

- **Nanuq:** Grrrrrrrrrrr. Groooowliowlioooo!

##### With 81 Summoning

- **Nanuq:** Grrroooorgh. <br>(Hello, Player. What can I do for you today?)
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Nanuq:** Grrrrrrrrrrr. Groooowliowlioooo! <br>(Of course. Once the beacon is lit, just have 5 logs with me and I'll take care of the fire for as long as I can.)
    - (Condition: If the beacon is dying:)
      - **Nanuq:** Groooowliowlioooo! ( Well, I could, but since you're here, you might as well do it yourself.)
    - (Condition: If the beacon is not dying:)
      - (Condition: If Nanuq does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Nanuq:** Grrrrrrrrrrr. Groooowliowlioooo! <br> (I'm afraid that you don't have enough of the right type of log for me to use.)
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Nanuq:** Grrr-arrrrg?<br>(I'll need five logs to be able to tend the fire. Is that okay?)
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Nanuq:** Groooowliowlioooo!  <br>(Thank you! I'll use these five logs to keep the beacon burning while you're away.)
              - [Choice]: No.
                - **Player:** I think I'll keep hold of my logs for now.
                - **Nanuq:** Raaaargh-groooool. <br> (Well, you know where I am if you change your mind.)
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Nanuq has five logs:)
        - **Nanuq:** Groooowliowlioooo! <br>(Of course I will, don't worry. I'll use the logs you've already left with me.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Nanuq:** Grrrroooorrg-gah. <br>(Most certainly.)
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Nanuq:** Grrroooorrgh.<br> (I can tell you about the beacons in either direction, up to and including the first one that's out.)
    - **Nanuq:** Grrrummmbberggrah. <br>(Of course, a macaw has much sharper eyes than I do. If I could work with that macaw you've got there, we could tell you about the entire beacon network.)
    - **Player:** A macaw?
    - **Nanuq:** Grrrummmbble. <br>(Yes. Macaws have the ability to fly high into the air and see things that are much further away.}
    - **Nanuq:** Grrr-bah.<br> {They are also highly intelligent and can be trained to provide the exact information needed for a complete overview of the beacon network.)
    - ((If the player has a macaw pouch in their backpack:))
      - **Nanuq:** Grrroooorrgh.<br> (Come to think of it, the macaw you've got there in  pack would be perfect.)
      - (continue|macaw)
  - [Choice]: How's it going?
    - **Player:** How's it going?
    - **Nanuq:** Grrrrrrrrrrr. Groooowliowlioooo!<br> (Oo, are you the snack that I ordered? I must say, I'm impressed at the speed of deliveries these days.)
    - **Player:** I'm no snack! You can get that thought right out of your head.
    - **Nanuq:** Raaaargh, grrrrrrowl groooo.<br> (Sincerest apologies, my mistake.)
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Nanuq:** Grrroooorrgh. <br>(Goodbye, then.)

##### Attempting to add logs to the beacon before repairing the windbreak

- **Nanuq:** Grrrrrrrrrrr. Groooowliowlioooo! <br> (I wouldn't bother. That beacon won't stay alight until that windbreak gets repaired.)
- **Nanuq:** Rawwrrr grrrrowl. <br> (I've been trying to chew the fibres together with my teeth, but for some reason, that just seems to make it worse.)
- **Player:** Hmm. Could you use a little help with that?
- **Nanuq:** Grrrrrrrrrrumph...grr. <br> (Perhaps a more pedestrian approach would suffice. I suspect someone with opposable thumbs could fix it with a needle and several pieces of jute fibre.)
- **Nanuq:** Grrrah? <br> (You wouldn't have time for a little DIY, would you?)
- **Player:** I'll see what I can do.
- **Nanuq:** Grrroooorrgh. <br>(Much obliged.)

### Using a macaw pouch on Nanuq


#### Before giving Nanuq a macaw pouch{{Anchor|macaw}}

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=a macaw pouch)
    - **Nanuq:** Raaaargh, grooool grrrrrrrowl. <br> (Thank you very much. This will help me give you more detailed information about the fire network.)
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Nanuq:** Raaaargh-groooool. <br> (Suit yourself.)

#### After giving Nanuq a macaw pouch

- **Player:** I've already given him a macaw; he doesn't need another.

### Using logs on Nanuq

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Nanuq does not have five logs:)
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
  - (Condition: If Nanuq has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed


#### Regardless of Summoning level

- **Nanuq:** Oi! Get away from that! Until you've proven yourself a true ally of Varrock, you can't use that!
- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
