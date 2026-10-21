# Jim

- **Original Wiki Page**: [Transcript:Jim](https://runescape.wiki/w/Transcript%3AJim)
- **Letter**: `J`

---

## Dialogue Transcript


### Talk to

- (Condition: If the player is inside a clockwork suit:)
  - **Player:** Hi Jim!
  - **Jim:** What do you think you're doing? You'll blow your cover. Let me get you out of that suit.
  - [Menu]: Do you want to get out of the penguin suit?
    - [Choice]: Yes
      - (Condition: Without at least one free backpack space:)
        - **Player:** I don't have enough room to store my penguin suit in my pack. I'll have to make room first.
      - {{Qact|The player exits the clockwork suit and grows back to normal size.}}
      - (receives=a clockwork suit)
      - The spell wears off as you climb out of the suit, growing back to normal size.
    - [Choice]: No
      - **Player:** No, thanks.
- [Menu]: Select an Option
  - [Choice]: Tuxedo-time.
    - (Condition: With something equipped in the main- or off-hand slots:)
      - **Jim:** You will need your hands free to operate the suit.
    - (Condition: With a cape equipped:)
      - **Jim:** You can't wear a cape inside the suit, it might get caught.
    - {{Qact|The player shrinks and walks into a clockwork suit.}}
    - (removes=a clockwork suit (if one was present in the backpack))
    - You shrink and walk in to the penguin suit.
  - [Choice]: Ask about hunting ground.
    - (Condition: First time talking after completing Hunt for Red Raktuber:)
      - **Jim:** Pssst.
      - **Player:** Oh, so you can talk now?
      - **Jim:** I could always talk. But I didn't want to reveal myself to the enemy.
      - **Player:** Well, what do you want?
      - **Jim:** I have heard of Larry's capture. I am sorry for your loss. Larry is very brave.
      - **Player:** Yeah. I hope he's okay. Where ever he is.
      - **Jim:** That is why I wish to speak to you. I have been instructed to assist you in infiltrating the penguins and training for future assignments.
      - **Player:** What? What future assignments?
      - **Jim:** When you go to rescue Larry, of course. It is not a task to be approached unprepared.
      - **Player:** So what exactly am I supposed to do?
      - **Jim:** Should you wish to infiltrate the penguins, I have been granted access to the spell that puts you in your penguin suit.
      - **Jim:** There is more than that, though. A new iceberg has floated down from the north, bringing with it reinforcements for the Penguin Outpost.
      - **Jim:** To prepare you for the times ahead, we have provided some equipment for you to practise hunting and tracking penguins.
      - **Jim:** In exchange for the experience you gain, we only ask that you hand over the captured KGP agents to us.
      - **Jim:** Simply jump across the ice floes here.
      - **Player:** Why KGP agents? What will you do with them?
      - **Jim:** That is classified. You do not need to know.
      - [Menu]: What do you want to do?
        - [Choice]: Press him further.
          - **Player:** That's not good enough? I'm tired of just taking orders. What will you do with the captured penguins?
          - **Jim:** Very well, if you insist on knowing. We will interrogate them and keep them imprisoned. They may reveal valuable information about Larry's location. That is why we only want KGP agents, the other penguins know nothing of
          - **Jim:** interest.
        - [Choice]: Ignorance is bliss.
          - **Player:** Fine, I don't want to know.
          - **Jim:** It is for the best.
    - (Condition: Thereafter:)
      - **Jim:** Do you have any captured KGP agents you would like to hand over?
      - [Menu]: Select an Option
        - [Choice]: Yes.
          - **Player:** Yes, I do have some.
          - **Jim:** Very good. Let me take a look.
          - (Condition: If the player doesn't have any KGP penguins with them:)
            - **Jim:** You don't appear to have any with you.
          - (Condition: If the player does have KGP penguins with them:)
            - **Jim:** The PBJ thanks you for your help.
        - [Choice]: No.
          - **Player:** No, I don't have any for you right now.

### Tickle

- **Jim:** {{RSChat|Hee hee hee}}
- You tickle the polar bear.

### Tuxedo-Time

- (Condition: While not inside a clockwork suit:)
  - (above|tuxedo-time)
- (Condition: While inside a clockwork suit:)
  - (Condition: Without at least one free space in the backpack:)
    - You do not have enough space in your inventory to get out of the suit.
  - (above|exit-suit)
