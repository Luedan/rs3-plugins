# Morgan

- **Original Wiki Page**: [Transcript:Morgan](https://runescape.wiki/w/Transcript%3AMorgan)
- **Letter**: `M`

---

## Dialogue Transcript


### In Draynor Village


#### Before Vampyre Slayer

- **Morgan:** Praise Saradomin! He has brought you here to save us all!
- **Player:** Wha–
- **Morgan:** He has guided your steps to my door, so that I may beseech you to save my village from a terrible threat!
- [Menu]: Choose an option:
  - [Choice]: Why don't you save your own village?
    - (see|Vampyre Slayer)
  - [Choice]: What terrible threat?
    - (see|Vampyre Slayer)
  - [Choice]: cond=Historical, only during the Battle of Lumbridge|Isn't there a battle raging nearby?
    - **Player:** Isn't there a battle raging nearby?
    - **Morgan:** Well, Saradomin himself is on the battlefield, so I can't see why I should be worried for my safety. He will protect us!
  - [Choice]: cond=With clay rings in backpack|I've brought clay rings for you.
    - **Player:** I've brought clay rings for you.
    - (continue|clayrings)
  - [Choice]: Anything else I can do for you?
    - **Player:** Anything else I can do for you?
    - **Morgan:** Actually you can, if you have some skill as a crafter. I hear one can have clay rings blessed to defend against foes; I could do with some of those. I'll buy as many as you can provide!
    - [Menu]: Select an Option
      - [Choice]: I've brought clay rings for you.
        - **Player:** I've brought clay rings for you.
          - (Condition: If the player has no clay rings:)
            - **Morgan:** No, you haven't. Feel free to return with one, though.
          - (Condition: If the player has one clay ring:)
            - **Morgan:** Ah, excellent. You can never be too careful, you know.
            - (removes=clay ring) (receives=10 coins)
            - [Morgan trades your ring for a small pile of coins, and stashes it safely away for later.]
          - (Condition: If the player has multiple clay rings:)
            - **Morgan:** Ah, excellent. You can never be too careful, you know.
            - **Morgan:** May I buy all the rings you have with you?
            - [Menu]: Select an Option
              - [Choice]: Just one.
                - (above|one-ring)
              - [Choice]: All.
                - (removes=clay rings) (receives=10 coins for each ring)
                - [Morgan trades your rings for a small pile of coins, and stashes it safely away for later.]
      - [Choice]: Right. Well, see you.
        - **Player:** Right. Well, see you.

#### After Vampyre Slayer

- **Morgan:** I cannot thank you enough, Player. My wife and I can truly start a new life here in Draynor, now that the threat of the vampyre is gone.
- [Menu]: Choose an option:
  - [Choice]: I'm glad I could help.
    - **Player:** I'm glad I could help.
  - [Choice]: Next time, you're on your own!
    - **Player:** Next time, you're on your own! I don't want to deal with any more vampyres.
    - **Morgan:** I know it was an arduous task, and we can never truly repay you.
  - [Choice]: cond=Historical, only during the Battle of Lumbridge|Isn't there a battle raging nearby?
    - (above)
  - [Choice]: cond=With clay rings in backpack|I've brought clay rings for you.
    - **Player:** I've brought clay rings for you.
    - (continuea|clayrings)
  - [Choice]: Anything else I can do for you?
    - **Player:** Anything else I can do for you?
    - **Morgan:** Actually you can, if you have some skill as a crafter. I hear one can have clay rings blessed to defend against foes; I could do with some of those. I'll buy as many as you can provide!
    - **Player:** But I killed the vampyre... what's there to defend against?
    - **Morgan:** Always be prepared for the worst, I say.
    - (continuea|prepared)

#### Sell-rings option

- **Player:** I've brought clay rings for you.
- (continuea|clayrings)
