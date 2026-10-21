# Zookeeper

- **Original Wiki Page**: [Transcript:Zookeeper](https://runescape.wiki/w/Transcript%3AZookeeper)
- **Letter**: `Z`

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Hi!
- **Zoo keeper:** Welcome to the Ardougne Zoo! How can I help you?
- [Menu]: Select an Option
  - [Choice]: Do you have any quests for me?
    - **Zookeeper:** Not at the moment. The explorers that come back from far away lands tell such amazing tales. Make sure you keep eyes and ears open as you may find new places to explore!
    - **Player:** Ooh, I will!
    - (initial)
  - [Choice]: Where did you get the animals from?
    - **Zookeeper:** We get them from all over the place! The most exotic creatures have been brought back by explorers and sold to us.
  - [Choice]: Keep up the good work.
    - (end)

### Treasure Trails

- (Condition: Only the first time:)
  - **Zookeeper:** Before I help you, can you do something for me?
  - **Player:** Sure.
  - **Zookeeper:** I need to know how many camels we have.
- (receives=challenge scroll (medium))
- [The zookeeper has given you a challenge scroll!]

##### When talked to again

- **Zookeeper:** Please tell me how many camels there are.
- Enter amount:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Zookeeper:** Sorry, but that doesn't sound right!
- (Condition: When given the correct answer:)
  - (removes=the old clue scroll (medium) and challenge scroll (medium))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [The zookeeper has given you another clue scroll!]
    - (continue)
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [You've found a casket!]
    - (continue)
  - **Zookeeper:** Thanks!
