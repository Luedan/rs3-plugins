# Royal Guard (servant)

- **Original Wiki Page**: [Transcript:Royal Guard (servant)](https://runescape.wiki/w/Transcript%3ARoyal%20Guard%20%28servant%29)
- **Letter**: `R`

---

## Dialogue Transcript


### In Servants' Guild

- **Royal Guard:** Nice to meet you!
- **Player:** What are you doing here?
- **Royal Guard:** Ah, I visited with her Royal Highness for the Diamond Jubilee, and I liked it so much I never left! However, I find myself without an income. Care to hire me, for only [number] coins?
- [Menu]: Select an Option
  - [Choice]: cond=Only if not asked last|What can you do?
    - **Player:** What can you do?
    - **Royal Guard:** I have some experience cooking, and I'm happy to take items to and from the bank.
    - (previous)
  - [Choice]: cond=Only if not asked last|Tell me about your previous jobs
    - **Player:** Tell me about your previous jobs.
    - **Royal Guard:** I've worked in the Queen's service, almost since I was a lad. A high quality of service expected there, let me tell you!
    - (previous)
  - [Choice]: You're hired!
    - **Royal Guard:** My dear sir, we've been discouraged from taking on more work for now.

#### Historical dialogue

- **Royal Guard:** Nice to meet you!
- **Player:** What are you doing here?
- **Royal Guard:** Ah, I visited with her Royal Highness for the Diamond Jubilee, and I liked it so much I never left! However, I find myself without an income. Care to hire me, for only [number] coins?
- [Menu]: Select an Option
  - [Choice]: cond=Only if not asked last|What can you do?
    - (above)
  - [Choice]: cond=Only if not asked last|Tell me about your previous jobs
    - (above)
  - [Choice]: You're hired!
    - (Condition: If the player doesn't have a servant:)
      - {{Transcript missing}}
    - (Condition: If the player already has a servant:)
      - You already have a servant.

### In a player-owned house

- {{Transcript missing}}
- **Royal Guard:** What can I do for you?
- [Menu]: Select an option
  - [Choice]: Go the bank/sawmill...
    - [Choice]: Take something to the bank
    - **Player:** Can you take something to the bank for me?
    - **Royal Guard:** Such tasks seem rather below a guard of the Queen's service, but I will do it. Give the item to me.
    - [Choice]: Bring something from the bank
    - (Condition: If the item is in your bank:)
    - **Royal Guard:** Here you go. Service worthy of a monarch, I must say.
    - (Condition: If the item is not in your bank:)
    - **Royal Guard:** You don't have any of those in your bank.
    - [Choice]: Take something to the sawmill
    - **Royal Guard:** I'm afraid I can't go to the sawmill; I'd need extra insurance you see.
  - [Choice]: Misc...
    - [Choice]: Make Tea
    - **Royal Guard:** A most excellent choice! One cuppa, coming up.
    - **Royal Guard:** Do you take milk with your tea?
      - [Menu]: Select an option
        - [Choice]: Yes please
        - **Player:** Yes please.
        - [Choice]: No thanks
        - **Player:** No thanks.
        - [Choice]: Actually I don't want any
        - **Player:** Actually I don't want any.
    - [Choice]: Serve dinner
    - **Royal Guard:** Certainly.
    - [Choice]: Serve drinks
    - **Player:** Serve drinks please.
    - **Royal Guard:** As long as everything is kept in order.
    - **Royal Guard:** Can I offer you a drink?
      - [Menu]: Select an option
        - [Choice]: Yes please
        - **Player:** Yes please.
        - **Royal Guard:** Do enjoy it.
        - [Choice]: No thanks
        - **Player:** No thanks.
        - [Choice]: Something else.
    - (Condition: Returns to previous.)
    - [Choice]: Greet guests
    - **Player:** Stay at the entrance and greet guests.
    - **Royal Guard:** If you like. I am highly trained in greeting etiquette, after all.
  - [Choice]: Stop following me
    - (Condition: Conversation ends.)
  - [Choice]: You're fired
    - [Menu]: Do you really want to fire your servant?
      - [Choice]: Yes.
        - **Player:** You're fired!
        - **Royal Guard:** I shall return to my monarch. It has been a pleasure.
      - [Choice]: No.
- (Condition: If you use bones/ashes on them)
- **Royal Guard:** As a member of the Queen's Guard, I cannot be seen handling such... objects.
- **Royal Guard:** Excuse me mate, I don't work for free! If you want me to keep working for you, you'll need to pay me 500 coins.
  - [Menu]: Select an option
    - [Choice]: Pay servant 500 coins.
    - **Royal Guard:** Thank you.
    - [Choice]: Pay servant 500 coins and don't ask again.
    - **Royal Guard:** Thank you.
    - [Choice]: Don't Pay.
      - (Condition: Conversation ends.)
    - [Choice]: Fire servant.
- (Condition: After Love Story)
  - **Royal Guard:** Excuse me mate, I don't work for free! If you want me to keep working for you, you'll need to pay me 375 coins.
