# Aminishi gem trader

- **Original Wiki Page**: [Transcript:Aminishi gem trader](https://runescape.wiki/w/Transcript%3AAminishi%20gem%20trader)
- **Letter**: `A`

---

## Dialogue Transcript

{{Transcript npc|Aminishi gem trader}}

### Before purchasing the Aminishi miststone


#### Without any Ports Spice

- **Aminishi gem trader:** Perhaps you would be willing to trade?
- **Aminishi gem trader:** I'm looking for Ports Spice, and I'm willing to give you something precious in exchange.
- **Aminishi gem trader:** I want 1 and you have 0. How about it?

#### With at least one Ports Spice

- **Aminishi gem trader:** Perhaps you would be willing to trade?
- **Aminishi gem trader:** I'm looking for Ports Spice, and I'm willing to give you something precious in exchange.
- **Aminishi gem trader:** I want 1 and you have [number]. How about it?
- [Menu]: Select an Option
  - [Choice]: Yes
    - (Condition: Without any space in backpack:)
      - **Aminishi gem trader:** Sorry, you don't have enough space!
    - (Condition: With space in backpack:)
      - **Aminishi gem trader:** Great, here take this Aminishi miststone.
      - (receives=Aminishi miststone)
      - **Aminishi gem trader:** Thank you, friend!
  - [Choice]: No
    - **Player:** No, thanks.

### After purchasing the Aminishi miststone

- **Aminishi gem trader:** Thank you, friend!
