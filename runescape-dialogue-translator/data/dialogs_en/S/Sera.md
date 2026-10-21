# Sera

- **Original Wiki Page**: [Transcript:Sera](https://runescape.wiki/w/Transcript%3ASera)
- **Letter**: `S`

---

## Dialogue Transcript


### South of Eagles' Peak, without the skill requirements to start The Firemaker's Curse

- You need the following skills to start this quest: 74 Firemaking, 76 Constitution, 64 Agility.
- **Player:** What are you all doing here?
- **Sera:** Top secret, my friend. But perhaps when you're more experienced you could help us.
- **Player:** I see.

### Balthazar Beauregard's Big Top Bonanza


#### First-time dialogue

- **Sera:** Good to see you again, Player.
- **Player:** What happened to out-doing Vulcan?
- **Sera:** Oh, I decided to let him have his glory for now. I know I easily have the experience to out-do him after our excursion.
- **Sera:** In the mean time, I'm running the fire-breathing here. Let me give you a rundown of what to do.
- **Player:** Okay.
- (below|explain first)

#### Before and after the performance


##### If the player has not already performed this week

- **Sera:** Do you want to start your fire-breathing performance?
- [Menu]: Select an Option
  - [Choice]: Yes
    - {{Qact|Player starts the performance.}}
  - [Choice]: No
    - **Player:** No.
  - [Choice]: Could you explain it to me again?
    - **Player:** Could you explain it to me again? {{anchor|explain}}
    - **Sera:** If I must.
    - {{anchor|explain first}}**Sera:** I've made up some solutions that will enable you to breathe different colour flames.
    - **Sera:** You can breathe whichever you like, but some of the solutions are harder than others; I've written guidelines on the bottles.
    - **Sera:** You've got as much time as you like, but you can only perform 6 colours. At the end, I'll let you know how you've done.
    - **Sera:** If you can't take it, and want to finish early, just speak to me. You can only do one performance at a time.
    - **Sera:** Do you want to start your fire-breathing performance?
    - [Menu]: Select an Option
      - [Choice]: Yes
        - {{Qact|Player starts the performance.}}
      - [Choice]: No
        - **Player:** No.
  - [Choice]: *(If audience reaction is toggled off)* Can you tell me how I'm doing? {{anchor|tellme}}
    - **Sera:** Yes.
  - [Choice]: *(If audience reaction is toggled on)* Could you stop telling me how I'm doing?
    - **Sera:** Of course! They won't stop talking to you, but they'll stop telling you if they think you're being repetitive or not.
    - **Sera:** Do you still want me to stop them?
    - [Menu]: Select an Option
      - [Choice]: Yes
        - (end)
      - [Choice]: No
        - **Player:** No.

##### If the player has already performed this week

- **Sera:** You've already done your fire-breathing performance this week. Speak to the ringmaster to see if there's anything else you can do.

#### During the performance


##### Upon starting the performance

- **Sera:** If you want to end your performance, just tell me or walk away from the performance area.

##### If spoken to during the performance

- **Sera:** Do you want to end your performance early?
- [Menu]: Select an Option
  - [Choice]: Yes
    - {{anchor|ended}} {{Qact|The player ends their performance.}}
    - (Condition: If the player scored points in their performance:)
      - Congratulations! You scored [amount] in your Firemaking (fire-breathing) performance. You received [amount] experience points.
    - (Condition: If the player scored no points in their performance:)
      - **Ringmaster:** I'm sorry, but that performance just wasn't good enough for a reward. Try again next week.
      - Oh no! You didn't score anything in your Firemaking (fire-breathing) performance. You received 0 experience points.
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

- **Sera:** Hi!
- **Player:** What are you doing here?
- **Sera:** Emmet and I heard about the celebration and we simply couldn't resist a huge glowing fire!
- **Player:** What is it you're doing exactly?
- **Sera:** Fire breathing, which helps me vent my anger.
- (Condition: If the fire breathing solution hasn't been claimed:)
  - **Player:** Can I have a go?
  - (receives=Fire breathing solution)
  - **Sera:** Sure, take this fire breathing solution. Who knows you might even have an 'extraordinary talent' for it.
  - **Player:** Thanks; got any tips?
  - **Sera:** It's all about one thing and that's making sure you take a deep breath so you have enough air to breathe the correct pressure.
- (Condition: If the fire breathing solution has been claimed:)
  - **Player:** Have you got any more fire breathing solution?
  - **Sera:** Sorry, I've not got any on me, but I did give some supplies to Alice.
  - **Player:** Ok, thanks.

### Wintumber Warmer


#### Before the event


##### Talk to

- **Sera:** Hi!
- **Player:** What are you doing here?
- **Sera:** We're here for a celebration and we simply couldn't resist a huge glowing fire!
- **Sera:** We haven't quite started yet though, so come back soon!

##### Breathe fire

- The Wintumber Warmer event hasn't started yet.

#### During the event


##### Talk to

- **Sera:** Hi!
- [Menu]: Select an Option
  - [Choice]: What are you doing here?
    - **Player:** What are you doing here?
    - **Sera:** Emmet and I heard about the celebration and we simply couldn't resist a huge glowing fire!
    - **Player:** What is it you're doing exactly?
    - **Sera:** Fire breathing, which helps me vent my anger.
    - (initial)
  - [Choice]: Breathe fire.
    - {{Qact|Player starts the activity.}}

##### Breathe fire

- {{Qact|Player starts the activity.}}

#### After the event


##### Talk to

- **Sera:** Hi!
- **Player:** What are you doing here?
- **Sera:** We're just packing up after the new year's celebration{{Sic}}
- **Sera:** I'd love to come back next year! This has been so much fun!

##### Breathe fire

- The Wintumber Warmer event has ended.
