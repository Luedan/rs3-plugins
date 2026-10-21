# Richie (NPC)

- **Original Wiki Page**: [Transcript:Richie (NPC)](https://runescape.wiki/w/Transcript%3ARichie%20%28NPC%29)
- **Letter**: `R`

---

## Dialogue Transcript


### Before contributing coins


#### If the player has 0 coins with them

- You have no coins to give away.

#### If the player has less than 1,000,000 coins with them

- The magpie ignores you.

#### If the player has between 1,000,000 and 9,999,999 coins with them

- The magpie takes a small interest in your coins, but continues to ignore you.

#### If the player has over 10,000,000 coins with them

- **Richie:** Good day there! That's quite a shiny looking set of coins you have there.
- **Player:** Are you eyeing up my coins?
- [You hold your coins out in front of you.]
- **Player:** These are my hard earned coins. I've been on many adventures you see.
- **Richie:** Would you be so kind and share some with me?
- (continue|withgp)

### After contributing coins

- **Richie:** Good day Player. It's great to see you again.
- **Richie:** Are you here to share more of your wealth?
- (Condition: Without coins:)
  - You have no coins to give away.
- (Condition: With coins:) {{anchor|withgp}}
  - How many coins would you like to give away?<br>You have helped Richie accumulate a total wealth of [number].<br><br>(0-[100,000,000 minus the already donated amount])<br>[input field]
  - (Condition: Entering a positive amount:)
    - (Condition: If a number over 100,000 was entered, the following is shown in an interface titled 'CONFIRMATION':)
      - You are about to give away [number] coins.<br><br>Do you wish to continue?
        - [Choice]: CANCEL
          - (end)
        - [Choice]: OK
          - (continue)
    - (removes=coins)
    - **Richie:** Player, you have helped me accumulate a total wealth of [number]!
    - (Condition: If the total donated sum reached 100,000,000 coins:)
      - **Richie:** As you clearly know how to increase your wealth, I have decided to join you on your adventures!
      - {{qact|Richie disappears from the Grand Exchange.}}
      - You have unlocked the pet: 'Richie'.
      - (popup)
        - {{popup|You have unlocked the pet:<br>'Richie'.|colour=#0f0}}
      - You can activate this via the 'Pets' tab in the 'Customisations' interface.
      - Congratulations! You have completed: 'Richie' - Unlock the Richie pet from helping Richie accumulate wealth at the Grand Exchange. (100,000,000/100,000,000)
