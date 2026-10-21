# Dark mage (Underground Pass)

- **Original Wiki Page**: [Transcript:Dark mage (Underground Pass)](https://runescape.wiki/w/Transcript%3ADark%20mage%20%28Underground%20Pass%29)
- **Letter**: `D`

---

## Dialogue Transcript


### In West Ardougne

- **Player:** Hello there.
- (Condition: Before Underground Pass:)
  - **Dark mage:** Why do you interrupt me, traveller?
  - (continue)
- (Condition: After Underground Pass - this is an oversight by Jagex)
  - **Dark mage:** Oh, it's the liberator of Ardougne. Why do you interrupt me?
  - (continue)
- **Player:** I just wondered what you're doing?
- **Dark mage:** I experiment with dark magic. It's a dangerous craft.
- (Condition: With a broken Iban's staff in backpack:)
  - **Player:** Could you fix this staff?
  - **Dark mage:** Almighty Zamorak! The Staff of Iban!
  - **Player:** Can you fix it?
  - **Dark mage:** This truly is dangerous magic, traveller. I can fix it, but it will cost you. The process could kill me.
  - **Player:** How much?
  - **Dark mage:** 200,000 gold pieces. Not a penny less.
  - [Menu]: Select an Option
    - [Choice]: Okay then.
      - (Condition: With 200,000 coins:)
        - You give the mage 200,000 coins and the staff.
        - (removes=200,000 coins and Iban's staff (broken)) (receives=Iban's staff)
        - [The mage fixes the staff and returns it to you.]
        - **Player:** Thanks. I appreciate that.
        - **Dark mage:** You be careful with that thing!
      - (Condition: Without 200,000 coins:)
        - **Player:** Oops! I'm a bit short.
        - You can not afford that.
        - (popup)
          - {{popup|You can not afford that.|warning=yes}}
    - [Choice]: No chance. that's
      - **Dark mage:** ...Fine by me.
