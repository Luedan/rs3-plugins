# Mrs. Winkin

- **Original Wiki Page**: [Transcript:Mrs. Winkin](https://runescape.wiki/w/Transcript%3AMrs.%20Winkin)
- **Letter**: `M`

---

## Dialogue Transcript


### Standard dialogue

- **Mrs. Winkin:** Oh, hello there, dear. How can I help you?
- [Menu]: Select an option
  - [Choice]: Where are we?
    - **Player:** Where are we?
    - **Mrs. Winkin:** This is Winkin's Farm, dear.
    - **Player:** Oh, I see. So where is Mr. Winkin?
    - **Mrs. Winkin:** Oh, he headed off to the market a while back. We look after the farm while he's gone.
    - **Mrs. Winkin:** Now, was there anything else you wanted?
    - (initial|initial-options)
  - [Choice]: Have you got any flags?
    - **Player:** Have you got any flags?
    - **Mrs. Winkin:** Let me check for you.
    - (Condition: If it is the first time:)
      - **Farmer Blinkin:** Oh, you must be new, dear! It's always good to see a new face. Now, usually we charge for flags, since so many go missing, but you can have your first set for free.
      - **Player:** Wow, thanks!
      - **Farmer Blinkin:** Now, remember: if you plant the flags in any place that doesn't have seeds in it, you'll lose yer flag - and they're not cheap to buy back from me. Here you go, then.
      - (receives=10 flags)
      - **Player:** Thanks very much! I'll be off, then.
      - **Farmer Blinkin:** Bye now.
    - (Condition: If player has less than 10 flags in the backpack:)
      - **Mrs. Winkin:** Ah! First things first. One of the farmers dropped off some flags for you. You can have them back. Here you go.
    - (Condition: If player still has less than ten flags in the backpack, substitute [price] with (10 - (# of flags in the backpack) * 500):)
      - **Mrs. Winkin:** Alright. You can have a total of 10 flags. To obtain a full set of flags will cost you [price] coins. Would you like to buy these flags?
      - [Menu]: Select an option
        - [Choice]: Yes, please.
          - **Player:** Yes, please.
          - (removes=[price] coins) (receives=[number] flags)
          - **Mrs. Winkin:** Here you are then, dear.
        - [Choice]: No, thanks.
          - **Player:** No, thanks.
          - **Mrs. Winkin:** Okay, dear. Goodbye.
    - (Condition: If player has 10 flags in the backpack:)
      - **Mrs. Winkin:** It looks like you have all the flags you need. You don't need to buy any more.
    - (Condition: If player ask him for flags for the first time:)
      - **Mrs. Winkin:** Oh, you must be new, dear! It's always good to see a new face. Now, usually we charge for flags, since so many go missing, but you can have your first set for free.
      - **Player:** Wow, thanks!
      - **Mrs. Winkin:** Now, remember: if you plant the flags in any place that doesn't have seeds in it, you'll lose the flag - and they're not cheap to buy back from me. Here you go, then.
      - **Player:** Thanks very much! I'll be off, then.
      - (receives=10 flags)
      - **Mrs. Winkin:** Bye now.
  - [Choice]: Do you have a spare spade?
    - **Player:** Do you have a spare spade?
    - **Mrs. Winkin:** Why, of course. I can sell you one for 5 gold pieces.
      - [Choice]: Okay, thanks.
        - **Player:** Okay, thanks.
        - (removes=5 coins) (receives=spade)
        - **Mrs. Winkin:** Here you are, then.
      - [Choice]: Actually, I've changed my mind.
        - **Player:** Actually, I've changed my mind.
        - **Mrs. Winkin:** Okay then.
  - [Choice]: Do you have anything for trade?
    - **Player:** Do you have anything for trade?
    - **Mrs. Winkin:** Of course.
    - (opens=Mrs Winkin's World of Seeds)
  - [Choice]: Nothing. I'm fine, thanks.
    - **Player:** Nothing. I'm fine, thanks.
    - **Mrs. Winkin:** Okay, dear.
