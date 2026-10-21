# Recruiter

- **Original Wiki Page**: [Transcript:Recruiter](https://runescape.wiki/w/Transcript%3ARecruiter)
- **Letter**: `R`

---

## Dialogue Transcript


### Before Plague's End

- **Recruiter:** Citizens of West Ardougne! Who will join the Royal Army of Ardougne? It is a very noble cause. Fight alongside King Tyras, crusading in the darklands of the west!
- **Man (#1):** Plague bringer!
- **Man (#2):** King Tyras is scum!
- **Recruiter:** Tyras will be informed of these words of treason!
- (continue|tomatoes)

### After Plague's End

- **Recruiter:** Citizens of West Ardougne! Who will join the Royal Army of Ardougne? It is a very noble cause. Stand alongside King Thoros, ready to defend our land from new threats!
- **Man (#1):** Liar!
- **Man (#2):** Thoros is just as bad!
- **Recruiter:** King Thoros will be informed of these words of treason!
- {{anchor|tomatoes}}{{qact|Two nearby men throw tomatoes at the recruiter.}}
- shadow=yes
- *(If the Red Revolution achievement hasn't been completed:)*
  - shadow=yes

### Treasure Trails

- (Condition: Only the first time:)
  - **Recruiter:** Look lively! Let's see if you have what it takes to answer this question.
  - **Player:** What question?
  - **Recruiter:** The one on this scroll.
- (receives=challenge scroll (medium))
- [The recruiter has given you a challenge scroll!]

##### When talked to again

- **Recruiter:** Please enter the answer to the question.
- Enter amount:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Recruiter:** Not even close!
- (Condition: When given the correct answer:)
  - (removes=the clue scroll (medium) and challenge scroll (medium))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [The recruiter has given you another clue scroll!]
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [You've found a casket!]
  - **Recruiter:** Spot on!
