# Magic assistant

- **Original Wiki Page**: [Transcript:Magic assistant](https://runescape.wiki/w/Transcript%3AMagic%20assistant)
- **Letter**: `M`

---

## Dialogue Transcript


### First-time dialogue

- **Magic assistant:** Howdy! I'm your assistant for the Magic performance. As it's yar first time I'm gunna give ya a run down on what happens.
- **Player:** Okay.
  - (continue|first time)

### Before completing your Magic performance in the circus

- **Magic assistant:** Do ya want to start yar Magic performance?
- **Select an option**
  - Yes
    - (end)
  - No
    - **Player:** No.
  - Could you explain it to me again?
    - **Player:** Can you explain it to me again?
    - {{anchor|first time}}**Magic assistant:** Course I can. There are four kinds of spells ya can perform. Levitation, teleportation, alchemy and elemental. The ring is filled with animals and props for ya to perform them spells on. Certain spells will only work on certain props and animals though. Give 'em a try and see what happens. Oh, but I'd best tell ya, the props and animals all have different difficulty ratings, which suggest the skill level most likely to grant ya success, but ya welcome to try any ya like. Last thing: you can only perform 10 spells. At the end of 'em I'll tell ya how ya done. Oh, and ya can do emotes in between moves to keep things fresh. The audience love that. No need to speed through 'em though, the performance ain't timed. If ya wanna finish yar performance early, just come speak to me. Ya can only do one performance at a time.
      - (Starts conversation over directly afterward)
  - *Only one of the following options will appear, depending on which has been toggled previously:*
    - Could you tell me how I'm doing?
      - **Magic assistant:** Yes.
    - Could you stop telling me how I'm doing?
      - **Player:** Could you stop telling me what the audience thinks of my performance? It's distracting.
      - **Magic assistant:** I certainly can. I can't make them stop yakking to ya, though. I'll just stop tellin' ya if they think yar performance is repetitive or not. Do ya still want me to stop telling you?
        - Yes
          - (end)
        - No
          - **Player:** No.

### During your Magic performance in the circus

- **Magic assistant:** Do ya wanna end yar performance early?
- **Select an option**
  - Yes
    - *If the player scored points in their performance:*
      - Congratulations! You scored [amount] in your Magic performance. You received [amount] experience points.
    - *If the player scored no points in their performance:*
      - **Ringmaster:** I'm sorry, but that performance just wasn't good enough for a reward. Try again next week.
      - Oh no! You didn't score anything in your Magic performance. You received 0 experience points.
  - No
    - **Player:** No.
  - *Only one of the following options will appear, depending on which has been toggled previously:*
    - Could you tell me how I'm doing?
      - (above)
    - Could you stop telling me how I'm doing?
      - (above)

### After your Magic performance in the circus

- **Magic assistant:**  Ya've already done yar Magic performance this week. Ya should speak to the ringmaster and see if there's anything else ya can do.
