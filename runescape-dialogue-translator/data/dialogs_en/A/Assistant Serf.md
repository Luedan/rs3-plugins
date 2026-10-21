# Assistant Serf

- **Original Wiki Page**: [Transcript:Assistant Serf](https://runescape.wiki/w/Transcript%3AAssistant%20Serf)
- **Letter**: `A`

---

## Dialogue Transcript

{{dialogue|npc}}

### Talk-to option

- **Assistant Serf:** Do you want to use the balloon? Just so you know, some locations require special logs and high Firemaking skills.
- {{tselect|Select an Option}}
  - {{topt|Yes.}}
    - {{tact|opens=Balloon transport system{{!}}Choose Destination}}
  - {{topt|No.}}
    - **Player:** No.
  - {{topt|Who are you?}}
    - **Player:** Who are you?
    - **Assistant Serf:** I am a serf. Assistant Serf to you! Auguste freed me and gave me this job.
    - **Assistant Serf:** Do you want to use the balloon?
    - {{tselect|Select an Option}}
      - {{topt|Yes.}}
        - {{tact|opens=Balloon transport system{{!}}Choose Destination}}
      - {{topt|No.}}
        - **Player:** No.

### Store logs option

- {{tselect|Give Assistant Serf all your logs?}}
  - {{topt|Hand over your logs}}
  - {{tcond|If the player has logs to hand over:}}
    - **Assistant Serf:** Thanks! You now have [number] charges.
  - {{tcond|If the player has no logs to hand over:}}
    - **Assistant Serf:** You don't have any logs I can store. You have [number] charges.
  - {{topt|Cancel}}
    - {{tact|end}}
