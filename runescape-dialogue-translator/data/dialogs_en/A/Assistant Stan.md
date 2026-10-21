# Assistant Stan

- **Original Wiki Page**: [Transcript:Assistant Stan](https://runescape.wiki/w/Transcript%3AAssistant%20Stan)
- **Letter**: `A`

---

## Dialogue Transcript

{{dialogue|npc}}

### Talk-to option

- **Assistant Stan:** Do you want to use the balloon? Just so you know, some locations require special logs and high Firemaking skills.
- {{tselect|Select an Option}}
  - {{topt|Yes.}}
    - {{tact|opens=Balloon transport system{{!}}Choose Destination}}
  - {{topt|No.}}
    - **Player:** No.
  - {{topt|Who are you?}}
    - **Player:** Who are you?
    - **Assistant Stan:** I am Stan. Auguste hired me to look after this balloon. I make sure people are prepared to fly.
    - **Assistant Stan:** Do you want to use the balloon?
    - {{tselect|Select an Option}}
      - {{topt|Yes.}}
        - {{tact|opens=Balloon transport system{{!}}Choose Destination}}
      - {{topt|No.}}
        - **Player:** No.

### Store logs option

- {{tselect|Give Assistant Stan all your logs?}}
  - {{topt|Hand over your logs}}
  - {{tcond|If the player has logs to hand over:}}
    - **Assistant Stan:** Thanks! You now have [number] charges.
  - {{tcond|If the player has no logs to hand over:}}
    - **Assistant Stan:** You don't have any logs I can store. You have [number] charges.
  - {{topt|Cancel}}
    - {{tact|end}}
