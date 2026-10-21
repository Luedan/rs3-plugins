# Eniola

- **Original Wiki Page**: [Transcript:Eniola](https://runescape.wiki/w/Transcript%3AEniola)
- **Letter**: `E`

---

## Dialogue Transcript


### Bank

- ((The rune payment interface opens.))
- (Condition: If the player has enough runes of the chosen type with them:)
  - (removes=20 of the selected rune)
  - (opens=Bank)
- (Condition: If the player does not have enough runes of the chosen type with them:)
  - **Eniola:** I'm afraid you don't have the necessary runes with you at this time, so I can't allow you to access your account. Please bring twenty runes of one type and you can open your account.

### Talk to

- **Eniola:** Well met, fellow adventurer! How can I help you?
- (Condition: If the player has items they can collect from the Grand Exchange:)
  - **Eniola:** Before we go any further, I should inform you that you have items ready for collection from the Grand Exchange.
  - (continue)
- [Menu]: What would you like to say?
  - [Choice]: Who are you?
    - **Player:** Who are you?
    - **Eniola:** How frightfully rude of me, my dear [chap/lady]. My name is Eniola and I work for that most excellent enterprise, the Bank of Gielinor.
    - [Menu]: Select an Option
      - [Choice]: If you work for the bank, what are you doing here?
        - **Player:** If you work for the bank, what are you doing here?
        - **Eniola:** My presence here is the start of a new enterprise of travelling banks.
        - **Eniola:** I, and others like me, will provide you with the convenience of having banking facilities where they will be of optimum use to you.
        - **Player:** So...what are you doing here?
        - **Eniola:** The Z.M.I., that is, the Zamorakian Magical Institute, requested my services upon discovery of this altar. We at the Bank of Gielinor are a neutral party and are willing to offer our services regardless of affiliation.
        - **Eniola:** So that is why I am here.
        - **Player:** Can I access my bank account by speaking to you?
        - **Eniola:** Of course, dear [sir/lady].
        - **Eniola:** However, I must inform you that because the Z.M.I. are paying for my services, they require anyone not part of the Institute to pay an access fee to open their bank account.
        - **Eniola:** But, as our goal as travelling bankers is to make our customers' lives more convenient, we have accomodated to your needs. We know you will be busy creating runes and do not wish to carry money with you. The charge to open your account is the small amount of twenty of one type of rune. The type of rune is up to you.
        - **Eniola:** Would you like to pay the price of twenty runes to open your bank account?
          - [Menu]: Select an Option
            - [Choice]: Yes please.
              - **Player:** Yes please.
              - (above|Bank)
            - [Choice]: Let me open my account and then I'll give you the runes.
              - **Player:** I don't have the runes on me. Let me open my account and then I'll give them to you.
              - **Eniola:** It's not that I don't trust you, old [chap/girl], but as the old adage goes: 'Payment comes before friends'.
            - [Choice]: No way! I'm not paying to withdraw my own money.
              - **Player:** That's preposterous! I'm not paying runes to withdraw my own stuff.
              - **Eniola:** I'm sorry to hear that, [sir/madam]. If you should reconsider, because I believe this service offers excellent value for money, do not hesitate to contact me.
      - [Choice]: I'd like to access my bank account, please.
        - (above|Bank)
      - [Choice]: I'd like to check my PIN settings.
        - (opens=Bank PIN)
  - [Choice]: I'd like to access my bank account, please.
    - [Menu]: It costs twenty runes of one type.<br>Do you wish to continue?
      - [Choice]: Yes
        - (above|Bank)
      - [Choice]: No
        - (end)
  - [Choice]: I'd like to check my PIN settings.
    - (opens=Bank PIN)
  - [Choice]: I'd like to see my Collection box.
    - (continue|Collect)

### Collect

- ((The rune payment interface opens.))
- (Condition: If the player has enough runes of the chosen type with them:)
  - (removes=20 of the selected rune)
  - (opens=Collection box)
- (Condition: If the player does not have enough runes of the chosen type with them:)
  - **Eniola:** I'm afraid you don't have the necessary runes with you at this time, so I can't allow you to access your account. Please bring twenty runes of one type and you can open your account.
