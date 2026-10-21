# Solomon

- **Original Wiki Page**: [Transcript:Solomon](https://runescape.wiki/w/Transcript%3ASolomon)
- **Letter**: `S`

---

## Dialogue Transcript


### Talk to

- **Solomon:** Welcome to Solomon's General Store!<br/>How may I be of assistance?
- [Menu]: Select an Option
  - [Choice]: cond=If the player is not on mobile:|What is this place?
    - **Solomon:** This is Solomon's General store, the finest retailer in the corporeal realm.
    - **Solomon:** Here you can buy pets, clothing, and a selection of fine cosmetic items.
    - (initial|initial-options)
  - [Choice]: cond=If the player is not on mobile:|How do I buy things here?
    - **Solomon:** Simply enter the store, select the items you want, and complete your transaction using Loyalty Points or RuneCoins.
    - **Solomon:** It couldn't be simpler.
    - (initial|initial-options)
  - [Choice]: cond=If the player is not on mobile:|I'd like to buy something.
    - [Menu]: Do you want to enter Solomon's store?
      - [Choice]: Yes.
        - {{Qact|The player is sent to the lobby and Solomon's General Store opens in a browser tab.}}
      - [Choice]: No.
        - (initial|initial-options)
  - [Choice]: cond=If the player is on mobile:|What's in your store?
    - **Solomon:** Browse at your leisure!
    - (opens=Customisations)
  - [Choice]: Goodbye.
    - **Solomon:** Until next time.
