# Romily Weaklax

- **Original Wiki Page**: [Transcript:Romily Weaklax](https://runescape.wiki/w/Transcript%3ARomily%20Weaklax)
- **Letter**: `R`

---

## Dialogue Transcript


### Standard dialogue

- **Romily Weaklax:** Hello and welcome to my pie shop, how can I help you?
- {{anchor|standard}} [Menu]: Select an Option
  - [Choice]: I'd like to buy some pies.
    - (opens=Pie Shop)
  - [Choice]: cond=If the player does not have an active pie request|Do you need any help?
    - **Player:** Do you need any help?
    - **Romily Weaklax:** Actually I could, you see I'm running out of stock and I don't have time to bake any more pies. Would you be willing to bake me some pies? I'll pay you well for them.
    - [Menu]: Select an Option
      - [Choice]: Sure, what do you need?
        - **Player:** Sure, what do you need?
        - **Romily Weaklax:** Great, can you bake me [number] [type of pie] please.
      - [Choice]: Sorry, I can't help you.
        - **Player:** Sorry, I can't help you.
  - [Choice]: cond=If the player has an active pie request|I've got those pies you wanted.
    - **Player:** I've got those pies you wanted.
    - (Condition: If the player does not have the pies:)
      - **Romily Weaklax:** Doesn't look like you have any of the [number] [type of pie]  I requested.
    - (Condition: If the player has only some of the requested pies:)
      - (removes=pies) (receives=coins)
      - **Romily Weaklax:** Thank you, if you could bring me the other [remaining number] that'd be great!
    - (Condition: If the player has all of the requested pies with them:)
      - (removes=pies) (receives=coins)
      - **Romily Weaklax:** Thank you very much!
  - [Choice]: I'm good thanks.
    - **Player:** I'm good thanks.

### With a wild pie in inventory

- **Romily Weaklax:** Hello and welcome to my pie shop. My word! That's a nice smelling pie you have. Is it for me?
- [Menu]: Select an Option
  - [Choice]: Yes, it is.
    - **Player:** Yes, it is.
    - **Romily Weaklax:** Oh, how splendid! Let me take that from you then.
    - (removes=wild pie)
    - {{RSFontAchievement|Who Ate All the Pie?|Talk to Romily Weaklax and give him a wild pie.}}
    - **Romily Weaklax:** Now, was there anything else you needed?
    - (continuea|standard)
  - [Choice]: No, it's for...someone else.
    - **Player:** No, it's for...someone else.
    - **Romily Weaklax:** Oh, I see. Was there something else you needed?
    - (continuea|standard)
