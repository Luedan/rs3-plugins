# Assistant Marrow

- **Original Wiki Page**: [Transcript:Assistant Marrow](https://runescape.wiki/w/Transcript%3AAssistant%20Marrow)
- **Letter**: `A`

---

## Dialogue Transcript


### Talk-to option

- **Assistant Marrow:** Do you want to use the balloon? Just so you know, some locations require special logs and high Firemaking skills.
- {{tselect|Select an Option}}
  - {{topt|Yes.}}
    - {{tact|opens=Balloon transport system{{!}}Choose Destination}}
  - {{topt|No.}}
    - **Player:** No.
  - {{topt|Who are you?}}
    - **Player:** Who are you?
    - **Assistant Marrow:** I am Assistant Marrow. I'm working here part time while I study to be a doctor.
    - **Assistant Marrow:** Do you want to use the balloon?
    - {{tselect|Select an Option}}
      - {{topt|Yes.}}
        - {{tact|opens=Balloon transport system{{!}}Choose Destination}}
      - {{topt|No.}}
        - **Player:** No.

### Store logs option

- {{tselect|Give Assistant Marrow all your logs?}}
  - {{topt|Hand over your logs}}
  - {{tcond|If the player has logs to hand over:}}
    - **Assistant Marrow:** Thanks! You now have [number] charges.
  - {{tcond|If the player has no logs to hand over:}}
    - **Assistant Marrow:** You don't have any logs I can store. You have [number] charges.
  - {{topt|Cancel}}
    - {{tact|end}}
