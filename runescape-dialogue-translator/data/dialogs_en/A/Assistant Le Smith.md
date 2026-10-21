# Assistant Le Smith

- **Original Wiki Page**: [Transcript:Assistant Le Smith](https://runescape.wiki/w/Transcript%3AAssistant%20Le%20Smith)
- **Letter**: `A`

---

## Dialogue Transcript


### Talk-to option

- **Assistant Le Smith:** Do you want to use the balloon? Just so you know, some locations require special logs and high Firemaking skills.
- {{tselect|Select an Option}}
  - {{topt|Yes.}}
    - {{tact|opens=Balloon transport system{{!}}Choose Destination}}
  - {{topt|No.}}
    - **Player:** No.
  - {{topt|Who are you?}}
    - **Player:** Who are you?
    - **Assistant Le Smith:** I am Assistant Le Smith. I used to work as a glider pilot, but they kicked me off.
    - **Player:** Why?
    - **Assistant Le Smith:** They said I was too full of hot air.
    - **Assistant Le Smith:** Do you want to use the balloon?
    - {{tselect|Select an Option}}
      - {{topt|Yes.}}
        - {{tact|opens=Balloon transport system{{!}}Choose Destination}}
      - {{topt|No.}}
        - **Player:** No.

### Store logs option

- {{tselect|Give Assistant Le Smith all your logs?}}
  - {{topt|Hand over your logs}}
  - {{tcond|If the player has logs to hand over:}}
    - **Assistant Le Smith:** Thanks! You now have [number] charges.
  - {{tcond|If the player has no logs to hand over:}}
    - **Assistant Le Smith:** You don't have any logs I can store. You have [number] charges.
  - {{topt|Cancel}}
    - {{tact|end}}
