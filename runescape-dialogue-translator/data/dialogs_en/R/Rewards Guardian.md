# Rewards Guardian

- **Original Wiki Page**: [Transcript:Rewards Guardian](https://runescape.wiki/w/Transcript%3ARewards%20Guardian)
- **Letter**: `R`

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Hi.
- **Rewards Guardian:** Greetings. What wisdom do you seek?
- [Menu]: Select an Option
  - [Choice]: Who are you?
    - **Player:** Who are you?
    - **Rewards Guardian:** Me? I'm here to grant you rewards for any of the Pizazz Points you may have earned in this training arena. Like my fellow guardians I am part of the arena and live to ensure its safe running.
    - **Player:** I see.
    - (initial)
  - [Choice]: Can I trade my Pizazz Points, please?
    - **Player:** Can I trade my Pizazz Points, please?
      - (Condition: If the player has a Progress hat with them:)
        - **Rewards Guardian:** Why, of course.
        - (opens=Magic Training Arena Shop)
      - (Condition: If the player does not have a Progress hat with them:)
        - **Rewards Guardian:** Sorry, you must be carrying a Pizazz Progress Hat so I can check what points you have. If you haven't got one, talk to my fellow guardian downstairs.
  - [Choice]: Got anything else I can buy?
    - **Player:** Got anything else I can buy?
    - **Rewards Guardian:** Well, we do stock a special book that you may be interested in, which provides a comprehensive guide to this training arena. It costs 200gp; would you like one?
    - (Condition: If the player already has the book:)
      - **Player:** No thanks, I already have one.
      - **Rewards Guardian:** Let me know if you lose it.
    - (Condition: If the player does not have the book:)
      - [Menu]: Select an Option
        - [Choice]: That sounds useful. Yes please.
          - **Player:** That sounds useful. Yes please.
          - **Rewards Guardian:** Very good, that'll be 200gp please.
          - (Condition: If the player does not have enough money:)
            - You can not afford that.
            - **Player:** Sorry, I don't have enough money.
          - (Condition: If the player has enough money:)
            - (removes=200 coins) (receives=Arena book)
            - **Rewards Guardian:**Thank you.
        - [Choice]: I don't want some dusty old book.
          - **Player:** I don't want some dusty old book.
          - **Rewards Guardian:** It's not old and it certainly isn't dusty, but suit yourself.
  - [Choice]: Thanks, bye!
    - **Player:** Thanks, bye!
    - **Rewards Guardian:** Use what you've learned, young one.
