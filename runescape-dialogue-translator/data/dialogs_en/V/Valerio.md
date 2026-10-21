# Valerio

- **Original Wiki Page**: [Transcript:Valerio](https://runescape.wiki/w/Transcript%3AValerio)
- **Letter**: `V`

---

## Dialogue Transcript


### Before One Piercing Note

- **Valerio:** Greetings, traveller!
- [Menu]: Select an Option
  - [Choice]: What were you singing about?
    - **Player:** What were you singing about?
    - **Valerio:** Ah...it's a song about someone I knew, a long time ago.
    - (other)
  - [Choice]: What are you doing at the abbey?
    - **Player:** What are you doing at the abbey?
    - **Valerio:** One of the sisters here, Sister Anna, she passed away recently. I knew her before she joined the abbey, so I've come to pay my respects.
    - [Menu]: Select an Option
      - [Choice]: How did you hear about Sister Anna's death?
        - **Player:** How did you hear about Sister Anna's death?
        - **Valerio:** I have my ear to the ground. Even a religious order isn't completely cut off from the world.
        - [Menu]: Select an Option
          - [Choice]: What were you singing about?
            - (above)
          - [Choice]: Goodbye.
            - (below)
      - [Choice]: Goodbye.
        - (below)
  - [Choice]: Goodbye.
    - **Player:** Goodbye.

### After One Piercing Note

- **Valerio:** Hello again, adventurer.
- [Menu]: Select an option
  - [Choice]: How are you doing?
    - **Player:** How are you doing?
    - *(If the player lied about The Killer:)*
      - **Valerio:** I still can't believe that a demon killed Anna. I knew there were still demons in the Wilderness, but the idea of one striking in a place like this...
    - *(If the player told the truth:)*
      - **Valerio:** I still can't believe that Anna could do those things. You think you know someone... but I suppose people can change a lot in time.
    - (other)
  - [Choice]: Is there anything I can help you with?
    - **Player:** Is there anything I can help you with?
    - **Valerio:** Thank you, adventurer, but no. You have done enough.
    - (other)
  - [Choice]: Goodbye.
    - **Player:** Goodbye.

### Treasure Trails


#### Receiving the challenge scroll

- (Condition: Only the first time:)
  - **Valerio:** Are you here about the treasure trail?
  - **Player:** Yes, I am!
  - **Valerio:** Here is your challenge. Good luck!
- (receives=challenge gem (medium))
- [Valerio has given you a challenge scroll!]

#### When talked to again

- **Valerio:** Please enter the answer to the question.
- Enter amount:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Valerio:** Not quite! Go look again.
- (Condition: When given the correct answer:)
  - (removes=the clue scroll (medium) and challenge gem (medium))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [Valerio has given you another clue scroll!]
    - (continue)
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [You've found a casket!]
    - (continue)
  - **Valerio:** Correct!
