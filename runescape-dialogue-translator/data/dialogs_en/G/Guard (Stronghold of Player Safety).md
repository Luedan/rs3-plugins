# Guard (Stronghold of Player Safety)

- **Original Wiki Page**: [Transcript:Guard (Stronghold of Player Safety)](https://runescape.wiki/w/Transcript%3AGuard%20%28Stronghold%20of%20Player%20Safety%29)
- **Letter**: `G`

---

## Dialogue Transcript


### Standard dialogue


#### First time speaking to the guard

- **Guard:** Can I help you?
- **Player:** I hope so. What is this place?
- **Guard:** Above us is the Misthalin Training Centre of Excellence, where young adventurers are taught things that will help keep themselves safe.
- **Guard:** They say that hidden away somewhere here is the entrance to the old jail, which no doubt has fabulous treasures for those willing to search for them.
- **Guard:** Together they’re called the Stronghold of Player Safety, for historical reasons.
- **Player:** So what do you do?
- **Guard:** I guard this stairway to make sure that prospective students are ready, and to explain the Report function.
- **SELECT AN OPTION**
  - [Choice]: What is this report thing?
    - **Player:** What is this report thing?
    - **Guard:** Should you find a player who acts in a way that breaks one of our rules, you should report them.
    - **Guard:** You can also right-click a player to examine them, and use the ‘report’ button on the top left of the examine interface.
    - **Guard:** Or you can simply click the ‘Report an issue’ button in your chat window and then click the ‘Report Player’ button. You will be shown the following screens:
    - {{qact|Report Player interface opens, then closes after a few seconds}}
    - **Guard:** If you used the 'Report' button you’ll see the first page, simply click a line of chat the player has said. Then click ‘Next’. For offences other than botting or bug abuse you can only report players who have spoken recently.
    - **Guard:** On the following page, click on the offence that the player has committed.
    - **Guard:** Finally, you’ll be given the option to temporarily ignore the player you’ve reported. That will last until you next log out.
    - **Player:** Thank you. I’ll bear that in mind.
  - [Choice]: That’s interesting. Goodbye.
    - **Player:** That’s interesting. Goodbye.

#### Talking to the guard again

- **Guard:** Hello again. Did you want me to tell you about the Report button?
- **SELECT AN OPTION**
  - [Choice]: Yes, please.
    - **Player:** Yes, please.
    - (continuea|report-help)
  - [Choice]: No thanks.
    - **Player:** No thanks. Goodbye.

#### Talking to the guard if you have previously completed the historical Player Safety test

- **Guard:** Ah, hello again citizen. Would you like to hear about the Report button once more?
- **SELECT AN OPTION**
  - [Choice]: Yes please.
    - **Player:** Yes please.
    - (continuea|report-help)
  - [Choice]: No thanks.
    - **Player:** No thanks. Just let me through.
    - **Guard:** Right you are then.
    - {{qact|The player is teleported to the classroom upstairs}}

#### Other dialogue

- **Guard:** Can I help you?
- **Player:** Can I go upstairs?
- **Guard:** Yes, citizen. Before you do, I am instructed to give you one final piece of information.
- **Guard:** Should you find a player who acts in a way that breaks one of our rules, you should report them.
- **Guard:** You can also right-click a player to examine them, and use the 'report' button on the top left of the examine interface.
- **Guard:** Or you can simply click the 'Report an issue' button in your chat window and then the 'Report Player' button. You will then be shown the following screens:
- {{qact|Report Player interface opens, then closes after a few seconds}}
- **Guard:** If you used the 'Report' button you’ll see the first page, simply click a line of chat the player has said. Then click 'Next'. For offences other than botting or bug abuse you can only report players who have spoken recently.
- **Guard:** On the following page, click on the offence that the player has committed.
- **Guard:** Finally, you’ll be given the option to temporarily ignore the player you’ve reported. That will last until you next log out.
- **Player:** Okay. Then what?
- **Guard:** That's it! It really is that simple and it only takes a moment to do. Now, you may enter the training centre. Good luck, citizen.
- **Player:** Thanks!

### Historical dialogue


#### First time speaking to the guard

- You need to read the plaques before the guard will allow you upstairs.
- **Guard:** Ahem! Can I help you?
- **Player:** I'd like to go up to the training centre, please.
- **Guard:** Sorry, citizen, but you can't go up there.
- **Player:** Why not?
- **Guard:** You must learn about player safety before entering the training centre.
- **Player:** Oh. How do I do that?
- **Guard:** Each of these gublinches have been caught breaking the Rules of RuneScape. You should read the plaques on each of their cells to learn what they did wrong.
- **Player:** Oh, right. I can enter the training centre once I have done that?
- **Guard:** Yes. Once you have examined each of the plaques, come and speak to me and I will tell you about the Report Abuse function.
- **Guard:** After that, I can let you into the training centre, upstairs.
- **Player:** Okay, thanks for the help.

#### Talking to the guard again after reading the plaques

- It doesn't look like I should be going up here. I should speak to the guard first.
- **Guard:** Can I help you?
- **Player:** Can I go upstairs?
- **Guard:** Yes, citizen. Before you do, I am instructed to give you one final piece of information.
- **Player:** Oh, okay then.
- **Guard:** In your travels around RuneScape, should you find a player who acts in a way that breaks one of our rules, you should report them.
- **Guard:** Reporting is very simple and easy to do. Simply click the Report Abuse button at the bottom of the screen and you will be shown the following screen:
- {{qact|Report Player interface opens, then closes after a few seconds}}
- **Guard:** Simply enter the player's name in the box and click the rule that the offender was breaking.
- **Player:** Okay. Then what?
- **Guard:** That's it! It really is that simple and it only takes a moment to do. Now, you may enter the training centre. Good luck, citizen.
- **Player:** Thanks!

### With the CS Week clue

- **Guard:** Well done, you've solved a clue. Speak to me again to find out more about the report feature!
- (removes=clue scroll (CS Week))
- (Condition: If the trail continues:)
  - (receives= a new clue scroll (CS Week))
- (Condition: If the trail ends:)
  - (receives=casket (CS Week) and security casket (CS Week))
