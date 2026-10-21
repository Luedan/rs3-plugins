# Odovacar

- **Original Wiki Page**: [Transcript:Odovacar](https://runescape.wiki/w/Transcript%3AOdovacar)
- **Letter**: `O`

---

## Dialogue Transcript

- *If the player is on the tile directly north, east, south, or west of Odovacar:*
  - **Odovacar:** Well met, fellow adventurer! How can I help you?
- *If the player is not on the tile directly north, east, south, or west of Odovacar:*
  - **Odovacar:** Good day. How may I help you?
- *If the player has items they can collect from the Grand Exchange:*
  - **Odovacar:** Before we go any further, I should inform you that you have items ready for collection from the Grand Exchange.
- **What would you like to say?**
  - *If the player is on the tile directly north, east, south, or west of Odovacar:*
    - Who are you?
      - **Odovacar:** How frightfully rude of me, my dear [chap/lady]. My name is Odovacar and I work for that excellent enterprise, the Bank of Gielinor.
      - **What would you like to say?**
        - If you work for the bank, what are you doing here?
          - **Odovacar:** As part of our ongoing service to provide you, the customer, with an absolutely world-class banking experience, we are investigating the option of opening a chain of travelling banks. These will provide you, our esteemed customer, with the convenience of having banking facilities where they will be of optimum use to you. Such as here!
          - **Player:** Huh?
          - **Odovacar:** I am the first of a new generation of travelling bankers that will wander the perilous areas of the world to provide you, the valued customer, with a bank when you need it most!
          - **Player:** So I can access my bank account simply by talking to you?
          - **Odovacar:** Absolutely correct, dear [sir/lady]. I must warn you, however, that due to the significantly increased overheads of an enterprise such as this, there is a small bank charge of 100gp every time you want to access your account.
          - **What would you like to say?**
            - Sounds fair; here's the money. Can I access my account now?
              - (below|access-bank)
            - Let me open my account and then I'll pay you.
              - **Odovacar:** It's not that I don't trust you, old [chap/girl], but as the old adage goes, 'money comes before friends'.
            - That's preposterous! I'm not paying to withdraw my own money!
              - **Odovacar:** I'm sorry to hear that, [sir/madam]. If you should reconsider, because I believe this service offers excellent value for money, do not hesitate to contact me.
        - I'd like to access my bank account, please.
          - (below|access-bank)
        - I'd like to check my PIN settings.
          - (opens=Bank PIN)
  - I'd like to access my bank account, please.
    - *If the player has at least 100 coins:*
      - *If the player is on the tile directly north, east, south, or west of Odovacar:*
        - {{qact|You pay 100 coins to use the travelling bank.}}
      - (opens=Bank)
    - *If the player does not have at least 100 coins:*
      - **Odovacar:** I'm afraid you don't have the necessary funds with you at this time so I can't allow you to access your account. Please come again, when you have 100 gold to cover the fee.
  - I'd like to check my PIN settings.
    - (opens=Bank PIN)
  - I'd like to see my collection box.
    - (opens=Collection box)
  - *If the player is not on the tile directly north, east, south, or west of Odovacar:*
    - What is this place?
      - **Odovacar:** This is a branch of the Bank of Gielinor. We have branches in many towns.
      - **What would you like to say?**
        - And what do you do?
          - **Odovacar:** We will look after your items and money for you. Leave your valuables with us if you want to keep them safe.
        - Didn't you used to be called the Bank of Varrock?
          - **Odovacar:** Yes we did, but people kept on coming into our branches outside of Varrock and telling us that our signs were wrong. They acted as if we didn't know what town we were in or something.
