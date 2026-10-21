# Erskine

- **Original Wiki Page**: [Transcript:Erskine](https://runescape.wiki/w/Transcript%3AErskine)
- **Letter**: `E`

---

## Dialogue Transcript


### Standard dialogue

- {{anchor|standard}}**Erskine:** Can I interest you in a job?<br>I'll pay you for your work.
- [Menu]: What would you like to say?
  - [Choice]: Tell me about yourself.
    - **Erskine:** My name's Erskine. I'm a powerful warrior from Edgeville destined to eradicate the horrors of the Wilderness.
    - **Erskine:** Although, I've found that going in there isn't really my thing at the moment, so I'm hiring people to do all that stuff for me under my banner.
    - **Erskine:** If you're interested in doing some combat yourself, I'd be happy to give you a job. I can pay you.
    - [Menu]: What would you like to say?
      - [Choice]: What sort of job are you offering?
        - (below|what-job)
      - [Choice]: Are you scared to go do it yourself?{{anchor|scared}}
        - **Erskine:** Of course not, there are... dust storms sometimes and I have an allergy. . Ahem... cough, cough.
        - [Menu]: What would you like to say?
          - [Choice]: Okay, I'd like a job.
            - (below|accept-job)
          - [Choice]: What sort of job are you offering?
            - (below|what-job)
          - [Choice]: Tell me about yourself.
            - (above|about-erskine)
          - [Choice]: So you're incapable of doing your own work?
            - (below|incapable)
          - [Choice]: No thanks.
            - (below|decline-job)
      - [Choice]: Are you incapable of doing your own work?{{anchor|incapable}}
        - **Erskine:** What are you trying to say? That I'm too scared to go into the Wilderness myself in case I die and lose my stuff?
    - **Erskine:** I just want to eradicate the monsters, so I need stay here and hire enough people to speed up the process.
    - **Erskine:** So, would you like a job now?
        - [Choice]: What would you like to say?
          - Okay, I'd like a job.
            - (below|accept-job)
          - [Choice]: What sort of job are you offering?
            - (below|what-job)
          - [Choice]: Tell me about yourself.
            - (above|about-erskine)
          - [Choice]: No thanks.
            - (below|decline-job)
      - [Choice]: Okay, I'd like a job.
        - (below|accept-job)
      - [Choice]: No thanks.
        - (below|decline-job)
  - [Choice]: What sort of job are you offering?{{anchor|what-job}}
    - **Erskine:** I'm hiring people to kill the monsters out in the north.
    - **Erskine:** I'd do it myself, but I've found that the ash and dust isn't good for me. Ahem, cough cough.
    - **Erskine:** Instead, I'm paying people like you to kill the monsters for me.
    - **Erskine:** Effectively, I'm removing dangerous stuff from the Wilderness by telling everyone to get rid of it over and over!
    - **Erskine:** I can offer cash payments. Alternatively, I bought myself some books about combat but didn't feel like actually venturing past the intro after reading the warnings about the dangers, so you could have one as payment.
    - **Erskine:** Incidentally, if you already have an assignment from elsewhere to kill creatures that you can find in the wilds, do come and see me. Complete your task out there, and I'll give you a special contract that'll work in tandem with it, and give you an additional reward on top.
    - **Erskine:** So would you like a job now?
    - [Menu]: What would you like to say?
      - [Choice]: Are you scared to go do it yourself?
        - (above|scared)
      - [Choice]: Why don't you do it yourself?
        - (above|incapable)
      - [Choice]: Okay, I'd like a job.
        - (below|accept-job)
      - [Choice]: Tell me about yourself.
        - (above|about-erskine)
      - [Choice]: No thanks.
        - (below|decline-job)
  - [Choice]: Okay, I'd like a job.{{anchor|accept-job}}
    - **Erskine:** Excellent. Take a look at my contracts and see which one you'd like to do.
    - (opens=Slayer Contracts){{anchor|slayer-contracts}}
      - (Condition: Upon selecting a task:)
        - (receives=Slayer contract (Wilderness))
        - [The scroll can only track you progress if you carry it while slaying. Bring it back when you've finished.]
  - [Choice]: No thanks.{{anchor|decline-job}}
    - **Erskine:** Alright, but come back if you change your mind. I can pay you for your work.

### Talk to him when assigned relevant Slayer assignment

- **Erskine:** I see you've got a Slayer assignment. I'll pay you extra if you take a contract to do your assignment in the Wilderness.
- [Menu]: What would you like to say?
  - [Choice]: What are you offering?
    - **Erskine:** You'll also get a 20% bonus on Slayer XP earned from killing the monsters, an extra 20% Slayer XP when the Demonic skull is worn or in your inventory inside the Wilderness
    - **Erskine:** Plus a choice of [number] combat XP or [number] coins.
    - [Menu]: What would you like to say?
      - [Choice]: Okay, I'll take it.
        - (below|special-slayer-contracts)
      - [Choice]: Can I have a different contract instead?
        - (above|slayer-contracts)
      - [Choice]: No thanks.
        - (above|decline-job)
  - [Choice]: Okay, I'll take it.
    - {{anchor|special-slayer-contracts}}(receives=Special slayer contract (Wilderness))
    - [The scroll can only track you progress if you carry it while slaying. Bring it back when you've finished.]
  - [Choice]: Can I have a different contract instead?
    - (above|slayer-contracts)
  - [Choice]: Could I ask about something else?
    - (above|standard)
  - [Choice]: No thanks.
    - (above|decline-job)

### Talk to him when having a contract in the backpack

- (Condition: If the contract is not completed:)
  - (Condition: If the contract is a special slayer contract:)
    - {{anchor|show-special-contract}} **Erskine:** Show me your special contract when you've finished it.
  - (Condition: If the contract is a regular slayer contract:)
    - {{anchor|show-regular-contract}} **Erskine:** Show me your contract when you've finished it.
- (Condition: If the contract is completed:)
  - **Erskine:** I see you've completed that contract. Good work. Would you like combat XP or cash?
  - {{anchor|choose}} [Menu]: Choose your reward:
    - [Choice]: Combat XP: [number] XP
      - (removes=Slayer contract (Wilderness)) (receives=combat training book)
      - [You receive a book about combat.]
    - [Choice]: Cash: [number] coins
      - (removes=Slayer contract (Wilderness)) (receives=coins)
      - [You receive [number] coins.]

### Talk to him when having a contract in the bank

- **Erskine:** You have a contract in your bank.<br>Shall I fetch it for you?
- [Menu]: What would you like to say?
  - [Choice]: Yes. Please fetch it.
    - (Condition: If the contract is a special slayer contract:)
      - [Your contract has been retrieved from your bank.]
      - (Condition: If the contract is not completed:)
        - (above|show-special-contract)
      - (Condition: If the contract is completed:)
        - (above|choose)
    - (Condition: If the contract is a regular slayer contract:)
      - [Your contract has been retrieved from your bank.]
      - (above|show-regular-contract)
  - [Choice]: No thanks. Leave it alone.
    - **Erskine:** Very well, but you'll need to have it in your inventory if you want to make any progress on it.
    - (Condition: If the contract is a special slayer contract:)
      - (above|show-special-contract)
    - (Condition: If the contract is a regular slayer contract:)
      - (above|show-regular-contract)
