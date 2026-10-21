# Karim

- **Original Wiki Page**: [Transcript:Karim](https://runescape.wiki/w/Transcript%3AKarim)
- **Letter**: `K`

---

## Dialogue Transcript


### In Al Kharid


#### Talking to him

- **Karim:** Would you like to buy a nice kebab? Only one gold.
- [Menu]: Select an Option
  - [Choice]: I think I'll give it a miss.
    - **Player:** I think I'll give it a miss.
  - [Choice]: Yes please.
    - **Player:** Yes please.
    - (Condition: If the player does not have at least one free backpack space:)
      - **Player:** I don't have enough room, sorry.
    - (Condition: If the player has at least one free backpack space:)
      - (Condition: If the player has at least one coin:)
        - (removes=1 coin) (receives=kebab)
        - You buy a kebab.
      - (Condition: If the player has no coins:)
        - **Player:** Oops, I forgot to bring any money with me.
        - **Karim:** Come back when you have some.
        - You can not afford that.
  - [Choice]: What do you think of Ali Morrisane?
    - **Player:** What do you think of Ali Morrisane?
    - **Karim:** I don't like him. He makes all these claims about being the best salesman in the world, and he even has some thugs that he's hired to threaten us.
    - **Karim:** One of them came round here and threatened to cut my head off if I didn't cooperate with them!
    - **Karim:** I've also heard some rumours about them from my friend Isma'il in Pollnivneach...
    - **Player:** What sort of rumours?
    - **Karim:** Apparently he has men there as well, who have also been threatening people.
    - **Karim:** And it's said that they even intend to steal from the ruler of Al Kharid himself!
    - **Player:** Really?
    - **Karim:** That's what I've heard. Anyway, are you sure you wouldn't like a kebab?
    - [Menu]: Select an Option
      - [Choice]: I think I'll give it a miss.
        - (above|give-it-a-miss)
      - [Choice]: Yes please.
        - (above|yes-please)

#### Treasure Trails

- (Condition: Only the first time:)
  - **Karim:** I've got a little problem for you to solve.
- (receives=challenge scroll (medium))
- [The salesman has given you a challenge scroll!]

##### When talked to again

- **Karim:** Please enter the answer to the riddle.
- Enter amount:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Karim:** No that's not right, think again.
- (Condition: When given the correct answer:)
  - (removes=the clue scroll (medium) and challenge scroll (medium))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [The salesman has given you another clue scroll!]
    - (continue)
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [You've found a casket!]
    - (continue)
  - **Karim:** Correct!
