# Professor Henry

- **Original Wiki Page**: [Transcript:Professor Henry](https://runescape.wiki/w/Transcript%3AProfessor%20Henry)
- **Letter**: `P`

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Hello!
- **Professor Henry:** Good day!
- {{anchor|old-jail-block}}**Professor Henry:** Did you want to know about the old jail block? We always need adventurers to keep the cockroaches in check.
- **Player:** Do I need to do your exam?
- **Professor Henry:** No, the exam isn't really for adventurers like you. Are you looking for the jail block?
- **Player:** Sure, tell me about the jail.
- **Professor Henry:** In the cells downstairs there's a secret passage into the old prison. I hear that fame and fortune awaits a suitably skilled adventurer.
- **Player:** Thanks, I'll look into that.

#### If you have previously completed the historical Player Safety test

- **Player:** Hello, Professor.
- **Professor Henry:** Ah, hello, Player. How goes the adventuring? I trust you are enjoying your adventures?
- **Player:** I am, thanks. I was wondering where the jail block might be.
- **Professor Henry:** Ah, yes. Search the cells downstairs and I'm sure you'll find it easily enough.
- **Player:** Okay, thanks.

#### If you have previously talked about the Player Safety test

- **Player:** Hello, Professor
- **Professor Henry:** Good to see you again.
- (continuea|old-jail-block)

### Historical dialogue


#### First time speaking to the professor

- **Player:** Hello.
- **Professor Henry:** Hello what?
- **Player:** Uh...hello there?
- **Professor Henry:** Hello, 'Professor'. Manners cost nothing, you know. When you're in my classroom, I ask that you use the proper address for my station.
- **Player:** Your station?
- **Professor Henry:** Yes. It means 'position', so to speak.
- **Player:** Oh, okay.
- **Professor Henry:** Now, what can I do for you, exactly?
- {{anchor|what-is-this-place}}**Player:** What is this place?
- **Professor Henry:** This is the Misthalin Training Centre of Excellence. It is where bold adventurers, such as yourself, can come to learn of the dangers of the wide world and gain some valuable experience at the same time.
- **Player:** What can I do here?
- **Professor Henry:** Here you can take part in the Player Safety test: a set of valuable lessons to learn about staying safe.
- **Professor Henry:** I can give you a test paper to take and, once completed, you can bring it back to me for marking. Would you like to take the test? It will not cost you anything.
- [Menu]: Select an option
  - [Choice]: Yes, please.
    - **Player:** Yes, please.
    - (Condition: With the test paper already in backpack:)
      - **Professor Henry:** Right then, I...oh! You already have a test paper? Excellent! Well, good luck then.
      - **Player:** Uh, thanks.
    - (Condition: Without the test paper in backpack:)
      - **Professor Henry:** Right then. Here is the test paper. When you have completed all the questions, bring it back to me for marking.
      - **Player:** Okay, thanks.
  - [Choice]: Not right now, thanks.
    - **Player:** Not right now, thanks.
    - **Professor Henry:** Very well. Come back and see me again if you change your mind.

#### Before completing the test

- **Player:** Hello, Professor.
- **Professor Henry:** Ah, hello again. How may I help you?
- (continuea|what-is-this-place)

#### After completing the test

- **Player:** Hello, Professor.
- **Professor Henry:** Ah, Player. How's the test going?
- **Player:** I think I've finished.
- **Professor Henry:** Excellent! Let me mark the paper for you, then.
- **Professor Henry:** Hmm. Uh-huh, yes, I see. Good! Yes, that's right.
- **Professor Henry:** Excellent! Allow me to reward you for your work. I have these two old lamps that you may find useful.
- **Professor Henry:** Also, there is an old jail block connected to the cells below the training centre, which have been overrun with vicious creatures. If you search around the jail cells downstairs, you should find it easily enough.
- **Professor Henry:** Now, your rewards.
- (removes=test paper) (receives=two Antique lamp (Misthalin Training Centre of Excellence))
- {{Qact|You have completed the Player Safety test!}}

### With the CS Week clue

- **Professor Henry:** Aha! Top marks! Well done on solving this clue!
- (removes=clue scroll (CS Week))
- (Condition: If the trail continues:)
  - (receives= a new clue scroll (CS Week))
- (Condition: If the trail ends:)
  - (receives=casket (CS Week) and security casket (CS Week))
