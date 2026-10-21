# Turgok

- **Original Wiki Page**: [Transcript:Turgok](https://runescape.wiki/w/Transcript%3ATurgok)
- **Letter**: `T`

---

## Dialogue Transcript


### Standard dialogue

- **Turgok:** Cave slime soup! Do you want to buy some soup? Only 10 coins a bowl.
- [Menu]: Select an Option
  - [Choice]: Yes, please.
    - **Player:** Yes please
  - (Condition: Without at least 10 coins:)
    - **Player:** But I don't have enough money on me.
  - (Condition: Without at least one free backpack space:)
    - **Turgok:** Looks like your hands are full. You'll have to free up some inventory space before I sell you anything.
  - (Condition: With at least one free backpack space:)
    - (removes=10 coins)
    - (receives=green gloop soup)
    - **Turgok:** There you go.
  - [Choice]: No, thanks.
    - **Player:** No, thanks.

### Overhead dialogue

- {{trandom}}
  - (Condition: Dialogue 1:)
    - **Turgok:** {{RSChat|Tasty soup!}}
  - (Condition: Dialogue 2:)
    - **Turgok:** {{RSChat|Green cave-slime soup!}}
  - (Condition: Dialogue 3:)
    - **Turgok:** {{RSChat|Soup!}}
  - (Condition: Dialogue 4:)
    - **Turgok:** {{RSChat|Hot, tasty soup!}}
  - (Condition: Dialogue 5:)
    - **Turgok:** {{RSChat|Cave slime soup!}}
