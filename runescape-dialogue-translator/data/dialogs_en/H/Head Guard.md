# Head Guard

- **Original Wiki Page**: [Transcript:Head Guard](https://runescape.wiki/w/Transcript%3AHead%20Guard)
- **Letter**: `H`

---

## Dialogue Transcript

{{Incomplete|missing dialogue for players with higher clan rank & citadels of other languages besides English}}

### Dialogue

- **Head Guard:** Need something, [sir/ma'am]?
- [Menu]: Select an option
  - [Choice]: I'd like a clan cloak.
    - (Condition: If the player already has a clan cloak:)
      - **Head Guard:** I've already given you one!
      - (previous)
    - (Condition: If the player does not have a clan cloak:)
      - **Head Guard:** Certainly. Here you are.
      - The captain gives you a cloak.
      - (receives=a clan cloak)
      - (previous)
  - [Choice]: I'd like a clan vexillum.
    - (Condition: If the player already has a clan vexillum:)
      - **Head Guard:** I've already given you one!
      - (previous)
    - (Condition: If the player does not have a clan vexillum:)
      - **Head Guard:** Certainly. Here you are.
      - The captain gives you a vexillum.
      - (receives=a clan vexillum)
      - (previous)
  - [Choice]: How do I change my clan permissions?
    - **Head Guard:** You can access your clan settings by clicking on the 'permissions' tab in the 'clan settings interface', accessible from the clan list. Pick a rank from the list on the left and a category from the top to see what permissions each rank has, and click an option to toggle it on and off. Remember, however, that you can't alter the permissions for any players of your own rank or higher, and that some options can only be accessed by those with administrator access or higher. Also, the chat category works slightly differently to the others, in that you set the minimum rank to talk or kick, rather than setting permissions for each rank individually. Would you like to know more about a specific category?
    - [Menu]: Select an option
      - [Choice]: Admin.
        - **Head Guard:** The admin category lets you change the permissions for all administrative actions within your clan.This includes recruiing, accessing the clan citadel and keep, and leading Rated Clan Wars.
        - (previous)
      - [Choice]: Events.
        - The events category lets you change the permissions related to clan events. This includes adding notices to the board, starting ameeting, holding a vote, or starting a game on the clan battlefield. Access to the controls for the party room and theatre is also controlled from the events page.
        - (previous)
      - [Choice]: Citadel.
        - The citadel category lets you change the permissions relating to citadel building operations. This includes marking buildings for upgrade or downgrade, and changing the layout of the clan battlefield. You have to be overseer rank or higher to move the build tick, though.
        - (previous)
      - [Choice]: Skills.
        - The skills category lets you change the permissions related to skilling within the clan citadel. This includes things like setting resource goals and changing the day of the build tick.
        - (previous)
      - [Choice]: Back.
        - (initial)
  - [Choice]: I'd like to change my citadel's language.
    - (Condition: If the clan citadel is affined to English servers:)
      - **Head Guard:** Your citadel is currently affined to English speaking servers.
    - (Condition: If the clan citadel is affined to other language servers:)
      - {{Transcript missing}}
    - (Condition: If the player has permissions to change the language:)
      - {{Transcript missing}}
    - (Condition: If the player does not have permissions to change the language:)
      - **Head Guard:** I'm afraid you don't have the necessary permissions for that, [sir/ma'am].
      - (previous)
  - [Choice]: I'd like to change my citadel's chat visibility settings.
    - (Condition: If the player is the clan owner:)
      - {{Transcript missing}}
    - (Condition: If the player is not the clan owner:)
      - Only the clan owner can change this setting.
      - (end)
