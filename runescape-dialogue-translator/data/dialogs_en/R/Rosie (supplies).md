# Rosie (supplies)

- **Original Wiki Page**: [Transcript:Rosie (supplies)](https://runescape.wiki/w/Transcript%3ARosie%20%28supplies%29)
- **Letter**: `R`

---

## Dialogue Transcript


### Talk to

- **Rosie (supplies):** Want to buy some supplies for your ship?<br/>You'll need supplies to travel on your ship. The greater the distance, the more supplies you'll need.
  - (Condition: If the player has purchased the maximum amount of supplies:)
    - You have purchased the maximum of [X]/[X] supplies.
    - ((Repeated in a pop-up:))
    - You have purchased the maximum of [X]/[X] supplies.
  - (Condition: If the player has not purchased the maximum amount of supplies:)
    - ((Purchase supplies interface opens.))
    - Supplies: [X]/[X].<br/>How many supplies do you want to purchase?<br/>([X] chimes each)
      - (Condition: If the player enters 0:)
        - Enter a number larger than zero.
        - ((Repeated in a pop-up:))
        - Enter a number larger than zero.
        - (continuea|buy-supplies)
      - (Condition: If the player enters a number greater than 0:)
        - You purchased [X] [supply/supplies] for [X] chimes.
        - You now have [X]/[X] supplies.
        - ((Repeated in a pop-up:))
        - You now have [X]/[X] supplies.
        - (continuea|buy-supplies)

### Buy 1

- You purchased [X] [supply/supplies] for [X] chimes.
- You now have [X]/[X] supplies.
- ((Repeated in a pop-up:))
- You now have [X]/[X] supplies.

### Buy X

- ((Purchase supplies interface opens.))
  - Supplies: [X]/[X].<br/>How many supplies do you want to purchase?<br/>([X] chimes each)
    - (Condition: If the player enters 0:)
      - Enter a number larger than zero.
      - ((Repeated in a pop-up:))
      - Enter a number larger than zero.
    - (Condition: If the player enters a number greater than 0:)
      - You purchased [X] [supply/supplies] for [X] chimes.
      - You now have [X]/[X] supplies.
      - ((Repeated in a pop-up:))
      - You now have [X]/[X] supplies.

### Buy All

- (Condition: If the player has purchased the maximum amount of supplies:)
  - You have purchased the maximum of [X]/[X] supplies.
  - ((Repeated in a pop-up:))
  - You have purchased the maximum of [X]/[X] supplies.
- (Condition: If the player has not purchased the maximum amount of supplies:)
  - [Menu]: Confirm purchase: Are you sure you want to purchase [X] [supply/supplies] with [X] chimes?
    - [Choice]: Ok
      - You purchased [X] [supply/supplies] for [X] chimes.
      - You now have [X]/[X] supplies.
      - ((Repeated in a pop-up:))
      - You now have [X]/[X] supplies.
    - [Choice]: Cancel
      - (end)
