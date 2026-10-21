# Emmett

- **Original Wiki Page**: [Transcript:Emmett](https://runescape.wiki/w/Transcript%3AEmmett)
- **Letter**: `E`

---

## Dialogue Transcript


### South of Eagles' Peak, without the skill requirements to start The Firemaker's Curse

- You need the following skills to start this quest: 74 Firemaking, 76 Constitution, 64 Agility.
- **Player:** What are you all doing here?
- **Emmett:** Top secret, my friend. But perhaps when you're more experienced you could help us.
- **Player:** I see.

### Balthazar Beauregard's Big Top Bonanza


#### First-time dialogue

- **Emmett:** Player!
- **Player:** How's it going?
- **Emmett:** It's wonderful!
- **Emmett:** The ringmaster seemed to want to push us away from the other acts; something about fiery carnage...
- **Emmett:** I'm just happy to be running the fire poi again! Let me show you how to do it!
- **Player:** Okay.
- (below|explain first)

#### Before and after the performance


##### If the player has not already performed this week

- **Emmett:** Do you want to start your flaming poi performance?
- [Menu]: Select an Option
  - [Choice]: Yes
    - {{Qact|Player starts the performance.}}
  - [Choice]: No
    - **Player:** No.
  - [Choice]: Could you explain it to me again? {{anchor|explain}}
    - **Player:** Could you explain it to me again?
    - **Emmett:** Of course!
    - {{anchor|explain first}}**Emmett:** You should stand on the nearby star to begin. When you're ready, start spinning!
    - **Emmett:** There's a range of tricks you can do with fire poi, some more difficult than others. You can try any you like, but your skill level will determine which ones you're most likely to be able to complete.
    - **Emmett:** You've got as much time as you like, but you can only perform 6 tricks. At the end, I'll let you know how you've done.
    - **Emmett:** If for some reason you want to finish early, just speak to me. You can only do one performance at a time.
    - **Emmett:** Do you want to start your flaming poi performance?
    - [Menu]: Select an Option
      - [Choice]: Yes
        - {{Qact|Player starts the performance.}}
      - [Choice]: No
        - **Player:** No.
  - [Choice]: *(If audience reaction is toggled off)* Can you tell me how I'm doing? {{anchor|tellme}}
    - **Emmett:** Yes.
  - [Choice]: *(If audience reaction is toggled on)* Could you stop telling me how I'm doing?
    - **Emmett:** Of course! They won't stop talking to you, but they'll stop telling you if they think you're being repetitive or not.
    - **Emmett:** Do you still want me to stop them?
    - [Menu]: Select an Option
      - [Choice]: Yes
        - (end)
      - [Choice]: No
        - **Player:** No.

##### If the player has already performed this week

- **Emmett:** You've already done your fire poi performance this week. Speak to the ringmaster to see if there's anything else you can do.

#### During the performance


##### Upon starting the performance

- **Emmett:** If you want to end your performance, just tell me or walk away from the performance area.

##### If spoken to during the performance

- **Emmett:** Do you want to end your performance early?
- [Menu]: Select an Option
  - [Choice]: Yes
    - {{anchor|ended}} {{Qact|The player ends their performance.}}
    - (Condition: If the player scored points in their performance:)
      - Congratulations! You scored [amount] in your Firemaking (fire poi) performance. You received [amount] experience points.
    - (Condition: If the player scored no points in their performance:)
      - **Ringmaster:** I'm sorry, but that performance just wasn't good enough for a reward. Try again next week.
      - Oh no! You didn't score anything in your Firemaking (fire poi) performance. You received 0 experience points.
  - [Choice]: No
    - **Player:** No.
  - Could you explain it to me again?
    - (above|explain)
  - Can you tell me how I'm doing?
    - (above|tellme)

##### If the player tries to step out of the performance area

- Do you want to end your performance early?
- [Menu]: Select an Option
  - [Choice]: Yes
    - (above|ended)
  - [Choice]: No
    - (end)

### Celebration of Fire

- **Emmet Logowski:** Hello there.
- **Player:** What are you doing here?
- **Emmet Logowski:** Sera and I heard about the celebration and we wanted to come join in!
- **Player:** What is it you're doing exactly?
- **Emmet Logowski:** Fire dancing, which by the way is awesome!
- **Player:** I can see that...
- **Emmet Logowski:** Fire dancing is cool, when you're part of a display team!
- **Player:** ...
- **Emmet Logowski:** I could fire dance all day...
- (Condition: If the fire poi hasn't been claimed:)
  - (receives=fire poi)
  - **Emmet Logowski:** Here, have this Poi. Perhaps you can learn and one day you'll become the special like me.
  - **Player:** Thanks, I'll give it a whirl!
- (Condition: If the fire poi has been claimed:)
  - **Player:** Have you got any more Pois?
  - **Emmet Logowski:** Sorry, I've not got any on me, but I did give some supplies to Alice.
  - **Player:** Ok, thanks.

### Wintumber Warmer


#### Before the event


##### Talk to

- **Emmet Logowski:** Hello there.
- **Player:** What are you doing here?
- **Emmet Logowski:** The time of celebration is upon us!
- **Emmet Logowski:** Come back soon and we can dance with fire!

##### Fire Dance

- The Wintumber Warmer event hasn't started yet.

#### During the event


##### Talk to

- **Emmet Logowski:** Hello there.
- [Menu]: Select an Option
  - [Choice]: What are you doing here?
    - **Player:** What are you doing here?
    - **Emmet Logowski:** Sera and I heard about the celebration and we wanted to come join in!
    - **Player:** What is it you're doing exactly?
    - **Emmet Logowski:** Fire dancing, which by the way is awesome!
    - **Player:** I can see that...
    - **Emmet Logowski:** Fire dancing is cool, when you're part of a display team!
    - **Player:** ...
    - **Emmet Logowski:** I could fire dance all day...
    - (initial)
  - [Choice]: Dance with fire.
    - {{Qact|Player starts the activity.}}

##### Fire Dance

- {{Qact|Player starts the activity.}}

#### After the event


##### Talk to

- **Emmet Logowski:** Hello there.
- **Player:** What are you doing here?
- **Emmet Logowski:** I was here for the new years celebration!
- **Emmet Logowski:** That's over now though... so I guess I'll go and fire dance elsewhere.

##### Fire Dance

- The Wintumber Warmer event has ended.
