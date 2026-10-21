# Kelhar

- **Original Wiki Page**: [Transcript:Kelhar](https://runescape.wiki/w/Transcript%3AKelhar)
- **Letter**: `K`

---

## Dialogue Transcript

{{Incomplete|missing dialogue for the other gems}}

### First-time dialogue when interacting with Kelhar or attempting to enter the gemstone cavern

- **Kelhar:** Halt! There are dangerous monsters ahead!
- [Menu]: Select an Option
  - [Choice]: Tell me more about them.
    - (continue|what)
  - [Choice]: Let me at them!
    - (continue|face)

### Main dialogue

- [Menu]: Choose an option:
  - [Choice]: What is in that cave?
    - **Kelhar:** Within that cave there are dragons unlike any you may have encountered before.
    - **Kelhar:** Tipped with gems, they are stronger than the regular dragons you may have faced before.
    - **Kelhar:** I guard this cave to protect those who may otherwise enter unaware.
    - [Menu]: Select an Option
      - [Choice]: Let me face them.
        - **Kelhar:** I shall only let you through if a Slayer master has instructed you to do so... or if you are willing to make a payment.
        - **Player:** How much do you want?
        - **Kelhar:** Not in your coins. In gems.
        - **Player:** There are gems all around us. I'll mine some and be right back.
        - **Kelhar:** No. I require some a bit more precious. Bring me uncut dragonstone, onyx or an incomplete hydrix and I shall allow you in. With each gem I will allow you to kill a certain amount before you must leave.
      - [Choice]: Thanks for letting me know.
        - (end)
  - [Choice]: Can I enter the cave?
    - (above|face)
  - [Choice]: I'd like to make a payment to enter the cave.
    - (Condition: If the player has already made the maximum payment:)
      - You have already paid Kelhar the maximum number of gems. Kill some gemstone dragons before trying to pay again.
    - (Condition: If the player does not have acceptable payment and has not made the maximum payment:)
      - Kelhar will only accept uncut dragonstone, onyx and incomplete hydrix gems as payment to enter the cave.
    - (Condition: If the player does have acceptable payment and has not made the maximum payment:)
      - [Menu]: WHAT GEM WOULD YOU LIKE TO USE AS PAYMENT?
        - (Condition: If the player has at least one uncut onyx:)
          - {{Transcript missing}}
        - (Condition: If the player has at least one incomplete hydrix:)
          - {{Transcript missing}}
        - (Condition: If the player has at least one uncut dragonstone:)
          - Uncut dragonstone (2 kills per gem)
            - How many gems would you like to use?
            - (The player must enter a number:)
            - (Condition: If the player enters 0:)
              - (end)
            - (Condition: If the player enters any number other than 0:)
              - **Kelhar:** Thank you! You may now kill a total of [number] gemstone dragons.
        - [Choice]: I don't want to pay you right now.
          - (end)

### Paying gems

- (above|gems)

### Checking kills

- (Condition: If the player has zero kills remaining:)
  - **Kelhar:** You must pay me in uncut gems before I will allow you to enter the dungeon again.
- (Condition: If the player has one or more kills remaining:)
  - **Kelhar:** I will allow you to kill another [1-60,000] gemstone dragons before I will request further gem payments.
