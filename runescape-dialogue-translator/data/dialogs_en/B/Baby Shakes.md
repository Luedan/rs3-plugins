# Baby Shakes

- **Original Wiki Page**: [Transcript:Baby Shakes](https://runescape.wiki/w/Transcript%3ABaby%20Shakes)
- **Letter**: `B`

---

## Dialogue Transcript


### Before completing the player-owned farm tutorial

- **Baby Shakes:** I can has animals?
- Baby Shakes will take any and all checked animals off your hands in exchange for 10% of their base bean value.
- **Granny Potterington:** Now now dear, let's not get ahead of ourselves. You can deal with that little blighter once we're all finished up here.

### After completing the player-owned farm tutorial

- **Baby Shakes:** I can has animals?
- Baby Shakes will take any and all checked animals off your hands in exchange for 10% of their base bean value.
  - [Menu]: Pick an option.
    - [Choice]: Offer animals to Baby Shakes one at a time.
      - Would you like to sell [animal name] for [X] beans?
      - [Menu]: Sell [animal name] for [X] beans?
        - [Choice]: Yes.
          - [Amount] beans added to your currency pouch.
          - (Condition: If the player has another animal to sell:)
            - (above|sell-one-animal)
          - (Condition: If the player does not have another animal to sell:)
            - (end)
        - [Choice]: No.
          - (Condition: If the player has another animal to sell:)
            - (above|sell-one-animal)
          - (Condition: If the player does not have another animal to sell:)
            - (end)
    - [Choice]: Give ALL held animals to Baby Shakes.
      - **Baby Shakes:** Are you sure you want me to take all the animals you're holding? I won't take any of your favourites.
      - [Menu]: Sell all the animals for a low bean price?
        - [Choice]: Yes
          - (Condition: If no animals were sold:)
            - You don't have any animals to sell. Zero animals, Zero beans!
            - ((Repeated in a pop-up:))
              - You don't have any animals to sell. Zero animals, Zero beans!
          - (Condition: If one animal was sold:)
            - (end)
          - (Condition: If multiple animals were sold:)
            - You've sold [X] animals for [X] total beans.
            - ((Repeated in a pop-up:))
              - You've sold [X] animals for [X] total beans.
        - [Choice]: No
          - (end)
    - [Choice]: [Back away slowly.]
      - (end)

### Using an animal on Baby Shakes

- **Baby Shakes:** {{RSChat|YUM! Me like [animal name].}}

### Using any other item on Baby Shakes

- **Baby Shakes:** Er, no thanks.
