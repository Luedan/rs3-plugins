# Nails Newton

- **Original Wiki Page**: [Transcript:Nails Newton](https://runescape.wiki/w/Transcript%3ANails%20Newton)
- **Letter**: `N`

---

## Dialogue Transcript


### Before Let Them Eat Pie

- (see|Let Them Eat Pie#Hired to steal)

### After Let Them Eat Pie

- (see|Let Them Eat Pie#Post-quest dialogue)

### Treasure Trails


#### Receiving the challenge scroll

- (Condition: Only the first time:)
  - **Nails Newton:** You here for something?
  - **Player:** I'm trying to complete a treasure trail.
  - **Nails Newton:** Well you need to do this favour for me first.
- (receives=challenge scroll (medium))
- [Nails Newton has given you a challenge scroll!]

#### When talked to again

- **Nails Newton:** Please enter the answer to the question.
- Enter amount:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Nails Newton:** Wrong. Have you tried counting?
- (Condition: When given the correct answer:)
  - (removes=the clue scroll (medium) and challenge scroll (medium))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [Nails Newton has given you another clue scroll!]
    - (continue)
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [You've found a casket!]
    - (continue)
  - **Nails Newton:** Correct!
