# Rohak

- **Original Wiki Page**: [Transcript:Rohak](https://runescape.wiki/w/Transcript%3ARohak)
- **Letter**: `R`

---

## Dialogue Transcript


### Under White Wolf Mountain


#### Before Recipe for Disaster

- **Old Dwarf:** Hello there, youngster.
- **Player:** Who are you calling youngster??
- **Old Dwarf:** Why you. Unless you have seen the small village of Falador grow into a heaving city like I have of course!
- **Player:** Err… no…
- **Old Dwarf:** Well then! Enjoy your stay in our mountain home.

#### After Recipe for Disaster

- **Rohak:** Hello again, youngster.
- [Menu]: What would you like to say?
  - [Choice]: About your son...
    - **Player:** How's your son getting on, now that I've rescued him from the time bubble and the culinaromancer?
    - **Rohak:** My son's fine. I'm not so sure about you, though. Maybe you should lay down in a dark room until the babbling stops.
  - [Choice]: Can I have another rock cake?
    - **Rohak:** Aye, I've still got enough ingredients from before, but I'll want 100 coins.
    - [Menu]: What would you like to say?
      - [Choice]: Okay, 100 coins will be fine.
        - (Condition: Without enough money:)
          - You can not afford that.
          - (pop-up)
            - {{Pop-up|You can not afford that.|warning=yes}}
        - (Condition: With enough money:)
          - (removes=100 coins)
          - [You hand over 100 gold and Rohak bakes you a rock cake.]
          - {{Qact|A dwarven rock cake appears on the nearby table.}}
      - [Choice]: No thanks.
        - **Rohak:** I'm not doing it for less, even for a mate.
