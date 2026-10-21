# Faruq

- **Original Wiki Page**: [Transcript:Faruq](https://runescape.wiki/w/Transcript%3AFaruq)
- **Letter**: `F`

---

## Dialogue Transcript


### In Al Kharid

- **Faruq:** Hello! Have you come to sample my marvellous wares?
- [Menu]: Choose an option:
  - [Choice]: Yes, I'd like to see what you have.
    - (opens=Faruq's Tools for Games)
  - [Choice]: Perhaps. Your stall has some odd-looking stuff; what are they for?
    - **Player:** Perhaps. Your stall has some odd-looking stuff; what are they for?
    - **Faruq:** I have the finest of items for those who would find their own things to do. Would you like to see them?
    - [Menu]: Select an Option
      - [Choice]: Yes, please.
        - (opens=Faruq's Tools for Games)
      - [Choice]: But what are they for?
        - **Player:** But what are they for?
        - **Faruq:** Although the world has many things to do, some people like to play games of their own.
        - **Faruq:** I sell them the tools to keep track of time, mark out places and routes, decide things randomly, even to hold great ballots of their group.
        - [Menu]: Select an Option
          - [Choice]: Let me see, then.
            - (opens=Faruq's Tools for Games)
          - [Choice]: These tools, are they complicated?
            - **Player:** These tools, are they complicated?
            - **Faruq:** No, mister/madam, they are not complicated.
            - **Faruq:** I have a book that explains them, should you need.
            - (opens=Faruq's Tools for Games)
          - [Choice]: I don't think this is for me.
            - **Player:** I don't think this is for me.
            - **Faruq:** That is a shame. I shall be here if you change your mind.
  - [Choice]: cond=After Carnillean Rising|Can I have a treasure chest?
    - (Condition: If the player already has a treasure chest:)
      - **Player:** Can I have a treasure chest?
      - **Faruq:** No, you may only have one chest at a time. Can I interest you in my other wares?
      - (previous)
    - (Condition: Otherwise:)
      - (receives=Treasure chest (Carnillean Rising))
      - [Faruq gives you a treasure chest.]
      - **Faruq:** Now, can I interest you in my other wares?
      - (previous)
  - [Choice]: No, thanks.
    - **Player:** No thanks.
