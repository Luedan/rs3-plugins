# Assistant Brock

- **Original Wiki Page**: [Transcript:Assistant Brock](https://runescape.wiki/w/Transcript%3AAssistant%20Brock)
- **Letter**: `A`

---

## Dialogue Transcript

{{TranscriptNPC|Assistant Brock}}

### Talk-to option

- **Assistant Brock:** Do you want to use the balloon? Just so you know, some locations require special logs and high Firemaking skills.
- {{tselect|Select an Option}}
  - {{topt|Yes.}}
    - {{tact|opens=Balloon transport system{{!}}Choose Destination}}
  - {{topt|No.}}
    - **Player:** No.
  - {{topt|Who are you?}}
    - **Player:** Who are you?
    - **Assistant Brock:** I am Assistant Brock. I serve under Auguste as his number two assistant.
    - **Assistant Brock:** Do you want to use the balloon?
    - {{tselect|Select an Option}}
      - {{topt|Yes.}}
        - {{tact|opens=Balloon transport system{{!}}Choose Destination}}
      - {{topt|No.}}
        - **Player:** No.

### Store logs option

- {{tselect|Give Assistant Brock all your logs?}}
  - {{topt|Hand over your logs}}
  - {{tcond|If the player has logs to hand over:}}
    - **Assistant Brock:** Thanks! You now have [number] charges.
  - {{tcond|If the player has no logs to hand over:}}
    - **Assistant Brock:** You don't have any logs I can store. You have [number] charges.
  - {{topt|Cancel}}
    - {{tact|end}}
