# Teddy

- **Original Wiki Page**: [Transcript:Teddy](https://runescape.wiki/w/Transcript%3ATeddy)
- **Letter**: `T`

---

## Dialogue Transcript

{{toc}}

### First-time dialogue

- **Teddy:** Hello. My name is Theodore. I will be your assistant today.
- **Player:** Uh, Teddy, I know who you are.
- **Teddy:** Don't interrupt, you'll make me forget my lines. And it's Theodore!
- **Teddy:** Blast. I can't remember what I was saying. Ah, yes...I was explaining the act.
- (below|initial-explain)

### Before the performance

*If the player has not already performed this week:*
- **Teddy:** Do you want to start your Thieving performance?
- **Select an option**
  - Yes
    - {{Qact|Player starts the performance.}}
  - No
    - **Player:** No.
      - *(Dialogue ends.)*
  - Could you explain it to me again? {{anchor|explain}}
    - **Player:** Could you explain it to me again?
    - **Teddy:** If I must.
    - **Teddy:** To begin your Thieving performance, stand on the nearby star. Upon starting, you will be presented with a list of tricks you may perform.
    - **Teddy:** Each trick has a different difficulty rating. The rating suggests which skill level is most likely to succeed at performing said trick. You may, however, attempt tricks you do not have the level for.
    - **Teddy:** Finally: you may only perform 5 tricks. At the end you will be informed of your results. You may perform emotes between tricks to keep things lively.
    - **Teddy:** If you wish to end your performance early - and I would completely understand the feeling - simply speak to me.
    - (Condition: First time:)
      - **Teddy:** Would you like to begin your Thieving performance?
    - (Condition: Afterwards:)
      - **Teddy:** Would you like to start your Thieving performance?
    - **Select an option**
      - Yes
        - {{Qact|Player starts the performance.}}
      - No
        - **Player:** No.
          - *(Dialogue ends.)*
  - *One of:*
    - Can you tell me how I'm doing? {{anchor|tellme}}
      - **Teddy:** Yes.
        - *(Dialogue ends.)*
    - Could you stop telling me how I'm doing?
      - **Teddy:** Certainly. But it will only stop you being informed if you are repetitive, not their general obnoxious shouting. Would you still like me to quiet them?
      - **Teddy:** Do you still want me to stop them?
      - **Select an option**
        - Yes
          - *(Dialogue ends.)*
        - No
          - **Player:** No.
            - *(Dialogue ends.)*

### During the performance

*Upon starting the performance:*
- **Teddy:** If you want to end your performance, just tell me or walk away from the performance area.
*If spoken to during the performance:*
- **Teddy:** Tsk, giving up so quickly?
- **Select an option**
  - Yes
    - {{Qact|Player ends the performance.}}
    - *If the player scored points in their performance:*
      - Congratulations! You scored [amount] in your Thieving performance. You received [amount] experience points.
    - *If the player scored no points in their performance:*
      - **Ringmaster:** I'm sorry, but that performance just wasn't good enough for a reward. Try again next week.
      - Oh no! You didn't score anything in your Thieving performance. You received 0 experience points.
  - No
    - **Player:** No.
      - *(Dialogue ends.)*
  - Could you explain it to me again?
    - (above|explain)
  - Can you tell me how I'm doing?
    - (above|tellme)
*If the player tries to step out of the performance area:*
- Do you want to end your performance early?
- **Select an option**
  - Yes
    - {{Qact|Player ends the performance.}}
    - *If the player scored points in their performance:*
      - Congratulations! You scored [amount] in your Thieving performance. You received [amount] experience points.
    - *If the player scored no points in their performance:*
      - **Ringmaster:** I'm sorry, but that performance just wasn't good enough for a reward. Try again next week.
      - Oh no! You didn't score anything in your Thieving performance. You received 0 experience points.
  - No
    - *(Dialogue ends.)*

### After the performance

- **Teddy:** Thank you for completing your Thieving performance. Please speak to the Ringmaster if you require any further information. I hate this spy job.
