# Barman

- **Original Wiki Page**: [Transcript:Barman](https://runescape.wiki/w/Transcript%3ABarman)
- **Letter**: `B`

---

## Dialogue Transcript


### Standard dialogue

- (Condition: If the player has more than 2,000 coins in their backpack or money pouch:)
  - **Barman:** And what will it be for you, fine [sir/madam]?
  - (continue)
- (Condition: If the player has 2,000 coins or fewer in their backpack or money pouch:)
  - **Barman:** Yes? Can I help you with something?
  - (continue)
- [Menu]: Choose an option:
  - [Choice]: A beer please.
    - **Player:** A beer please.
    - **Barman:** That'll be 1 gold coin please.
    - [Menu]: Select an Option
      - [Choice]: Pay.
        - (Condition: Without at least one free backpack space:)
          - **Barman:** You don't have room to take a beer.
        - (Condition: With at least one free backpack space:)
          - (Condition: If the player does not have at least 1 coin:)
            - **Player:** I'm sorry, I seem to have run out of money.
          - (Condition: If the player does have at least 1 coin:)
            - (removes=1 coin)
            - (receives=a beer)
            - **Barman:** Here you go. One delicious pint of beer.
      - [Choice]: Don't pay.
        - **Player:** Sorry, I changed my mind.
  - [Choice]: A dwarven stout please.
    - **Player:** A dwarven stout please.
    - **Barman:** It'll be yours for just 2 gold coins!
    - [Menu]: Select an Option
      - [Choice]: Pay.
        - (Condition: Without at least one free backpack space:)
          - **Barman:** You don't have room to take a beer.
        - (Condition: With at least one free backpack space:)
          - (Condition: If the player does not have at least 2 coins:)
            - **Player:** I'm sorry, I seem to have run out of money.
          - (Condition: If the player does have at least 2 coins:)
            - (removes=2 coins)
            - (receives=a dwarven stout)
            - **Barman:** One dwarven stout, best in all of Keldagrim!
      - [Choice]: Don't pay.
        - **Player:** Sorry, I changed my mind.
  - [Choice]: A fine wine please.
    - **Player:** A fine wine please.
    - **Barman:** Ah, [sir/madam] has taste! A jug of wine will cost you 10 gold coins.
    - [Menu]: Select an Option
      - [Choice]: Pay.
        - (Condition: Without at least one free backpack space:)
          - **Barman:** You don't have room to take a jug of wine.
        - (Condition: With at least one free backpack space:)
          - (Condition: If the player does not have at least 10 coins:)
            - **Player:** I'm sorry, I seem to have run out of money.
          - (Condition: If the player does have at least 10 coins:)
            - (receives=a jug of wine for 10 coins)
            - **Barman:** I hope [sir/madam] will enjoy it!
      - [Choice]: Don't pay.
        - **Player:** Sorry, I changed my mind.
  - [Choice]: Nothing, thanks.
    - **Player:** Nothing, thanks.
