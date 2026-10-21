# Armoursmith

- **Original Wiki Page**: [Transcript:Armoursmith](https://runescape.wiki/w/Transcript%3AArmoursmith)
- **Letter**: `A`

---

## Dialogue Transcript


### First conversation

- **Armoursmith:** Not good. Not good at all.
- **Player:** What isn't?
- **Armoursmith:** Your shell, it won't do.
- The armoursmith wiggles a hammer in the direction of your stomach.
- **Armoursmith:** The Airut will crush it, their hounds will shred it and the desert will cook it.
- Select an option
  - How do you suggest I improve my shell?
    - **Armoursmith:** Mazcab is old, hides many secrets, I have fragments of these secrets. Bring me Teci, I make them into a better shell for you. Maybe you find your own Mazcab secrets. Maybe they form better shell than I make. Until then, come to me.
    - {{tact|continue|init}}
  - I think my shell will do fine, thank you.
    - **Player:** I think my shell will do fine, thank you.

### Subsequent conversations

- *(Without any Achto parts equipped:)*
  - **Armoursmith:** Still not good enough, human.
  - *(Continues below.)*
- *(With Achto parts equipped:)*
  - **Armoursmith:** Looking much better human.
  - *(Continues below.)*
- Select an option{{anchor|init}}
  - Could you make some armour for me?
    - {{tact|opens=Raid Rewards}}
  - Where can I find Teci?
    - **Armoursmith:** Teci can be found from defeating worthy opponents in the area north of this barrier.
    - {{tact|initial|init}}
  - Can you imbue a ring for me?
    - *(As in imbuing rings.)*
  - Good bye.
    - {{tact|end}}

### Imbuing rings

- **Armoursmith:** Which do you want me to imbue?
- [Menu]: Select an option
  - [Choice]: Can you remove the enchantment from my item?|cond=Only with an imbued ring in backpack
    - **Player:** Can you remove the effect from my item?
    - **Armoursmith:** No problem. Just use the ring on me and I'll see what I can do.
  - {{topt|Ring of Fortune (2,500 Teci)}}
    - {{tact|continue}}
  - {{topt|Luck of the Dwarves (7,500 Teci)}}
    - {{tact|continue}}
  - {{topt|Hazelmere's Signet Ring (10,000 Teci)}}
    - {{tact|continue}}
  - {{topt|More...}}
    - [Menu]: Select an option
      - {{topt|Ring of Death (15,000 Teci)}}
        - {{tact|continue}}
      - {{topt|Asylum Surgeon's ring (10,000 Teci)}}
        - {{tact|continue}}
      - {{topt|Back...}}
        - {{tact|previous}}
- **Player:** [Chosen ring], please.
- (Condition: If the player doesn't have the chosen ring in the inventory:)
  - **Player:** Actually, I don't have any of those rings with me.
- (Condition: If the player doesn't have the chosen ring in the inventory but not enough Teci:)
  - **Player:** Actually, I don't have that much {{Sic|Teci}}
- (Condition: If the player has the chosen ring in the inventory and enough Teci:)
  - (removes=unimbued ring) (receives=imbued ring)
  - **Armoursmith:** Here you go human, I have imbued your finger-shell. Come back if you want me to remove the effect.

### Using an imbued ring

- [Menu]: Remove the enchantment?
  - {{topt|Yes}}
    - (The enchantment is removed.)
    - **Armoursmith:** There you go.
  - {{topt|No}}
    - (end)
