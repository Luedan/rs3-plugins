# Battlemaster

- **Original Wiki Page**: [Transcript:Battlemaster](https://runescape.wiki/w/Transcript%3ABattlemaster)
- **Letter**: `B`

---

## Dialogue Transcript

- **Battlemaster:** Welcome to the clan battlefield. What can I do for you?
- [Menu]: What would you like to say?
  - [Choice]: What is a clan battlefield?
    - **Player:** What is a clan battlefield?
    - **Battlemaster:** In addition to these citadels, clans have a private battlefield where they can organise battles.
    - **Battlemaster:** Members with sufficient rank are allowed to change the layout of the battlefield, building walls, setting up spikes, adding aggressive monsters to fight, and much more besides. Other members may be able to initiate a battle, if there isn't one already in progress. Battles don't have to involve combat; if a clan wants to kick a ball or chase a flag around the battlefield instead, that's up to them.
    - **Battlemaster:** The battlefields are safe; you don't lose your items when you die in there.
    - (other)
  - [Choice]: I want to join a battle.
    - **Player:** I want to join a battle.
    - **Battlemaster:** I'm searching for it now...
    - ((Clan Battlefield Setup interface opens.))
      - [Choice]: Quit
        - [Attempting to leave battlefield...]
        - Entering citadel...
      - [Choice]: Confirm
        - You are not the person who initiated this battle. If you want to initiate a battle, speak to the battlemaster in your citadel.
  - [Choice]: I want to initiate a new battle.
    - **Player:** I want to initiate a new battle.
    - (Condition: If the player has permission to start a battle:)
      - {{tmissing}}
    - (Condition: If the player doesn't have permission to start a battle:)
      - {{tmissing}}
    - (Condition: If the player is in another clan's citadel:)
      - **Battlemaster:** Hang on, you're not in this clan! You'll have to let someone else start the battle.
  - [Choice]: I want to edit the battlefield.
    - **Player:** I want to edit the battlefield.
    - (Condition: If the player has permission to edit the battlefield:)
      - {{tmissing}}
    - (Condition: If the player doesn't have permission to edit the battlefield:)
      - {{tmissing}}
    - (Condition: If the player is in another clan's citadel:)
      - **Battlemaster:** Hang on, you're not in this clan! You can't edit their battlefield.
  - [Choice]: Never mind.
    - **Player:** Never mind.
