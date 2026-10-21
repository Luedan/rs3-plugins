# Examiner

- **Original Wiki Page**: [Transcript:Examiner](https://runescape.wiki/w/Transcript%3AExaminer)
- **Letter**: `E`

---

## Dialogue Transcript


### Talk to


#### Without the Treasure Trails clue or 25th Anniversary celebration task in progress


##### Before The Dig Site

- (see|The Dig Site#Starting Out)

##### After The Dig Site

- **Examiner:** Hello there! My colleague tells me you helped to uncover a hidden altar to the god Zaros.
- **Examiner:** A great scholar and archaeologist indeed! Good health and prosperity to you.
- [Menu]: Select an Option
  - [Choice]: Thanks.
    - **Player:** Thanks!
  - [Choice]: I have lost my trowel.
    - **Player:** I have lost my trowel.
    - (Condition: If the player doesn't have a trowel:)
      - **Examiner:** Deary me. That was a good one as well. It's a good job I have another. Here you go...
      - (receives=a trowel)
    - (Condition: If the player already has a trowel:)
      - **Examiner:** Really? Look in your backpack and make sure first.

#### Treasure Trails


##### Receiving the puzzle box

- **Examiner:** Hi! Please complete this.
- (receives=puzzle box)
- [The examiner has given you a puzzle box!]

##### Without solving the puzzle

- **Examiner:** I'm afraid that you have not finished the puzzle.

##### With the puzzle solved

- (If the trail continues:)
  - (removes=the old clue scroll (hard) and puzzle box) (receives= the new clue scroll (hard))
  - [The examiner has given you another clue scroll!]
  - (continue)
- (If the trail ends:)
  - (removes=the old clue scroll (hard) and puzzle box) (receives=reward casket (hard))
  - [You've found a casket!]
  - (continue)
- **Examiner:** Correct! Well done!

#### During the 25th Anniversary celebrations task

- **Examiner:** Right! Time for your exam.
- **Player:** But I haven't studied! I'm not prepared!
- **Examiner:** Aha! I am, of course, joking. Here, we learn by doing.
- {{RSFontAchievement|You Dig?|Talk to an examiner at the Varrock Dig Site's Exam Centre.}}
- ((Shown in a task completion pop-up:))
  - {{Colour|#F0BE79|&nbsp;25TH ANNIVERSARY TASK&nbsp;|#181513}}
  - You Dig?
  - Talk to an examiner at the Varrock Dig Site's Exam Centre.
  - (continue)
- **Examiner:** So grab a mattock and get stuck in!
- (Condition: If all the tasks have been completed:)
  - **Player:** Looks like I've completed everything. I'd better go and see Hans about that reward!
