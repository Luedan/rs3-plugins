# Furies' Chosen

- **Original Wiki Page**: [Transcript:Furies' Chosen](https://runescape.wiki/w/Transcript%3AFuries%27%20Chosen)
- **Letter**: `F`

---

## Dialogue Transcript


### Talk to

- **Furies' Chosen:** Welcome, mortal.
- ((With an anima crystal in backpack:))
  - **Furies' Chosen:** That's an interesting Anima crystal you have there. Would you be willing to donate it?
  - [Menu]: Hand in your Anima crystal?
    - [Choice]: Yes. (Gain 500 reputation with Zamorak)
      - (removes=anima crystal)
      - (Condition: Without 5,000 Zamorak reputation:)
        - You have gained 500 reputation with the Zamorakian forces!
        - (Condition: If new rewards were unlocked:)
          - (see|Reputation (Heart of Gielinor))
          - (continue)
        - (continue)
      - **Furies' Chosen:** Thank you for your help.
      - (continue)
    - [Choice]: No.
      - (continue)
- (Condition: With seals of opposing factions in backpack and under 2,000 Zamorak reputation:)
  - **Furies' Chosen:** I notice you have a stock of seals from around the Heart. Would you be interested in donating them?
  - **EXCHANGE SEALS FOR REPUTATION WITH THE ZAMORAKIANS?**
    - ((With Seals of the Cywir in backpack:))
      - Hand in Seren seals.
        - (The seals are exchanged for reputation.)
        - Your Seals of the Cywir were worth [number] reputation with the Zamorakian forces!
        - (Condition: If new rewards were unlocked:)
          - (see|Reputation (Heart of Gielinor))
          - (continue)
        - ((With other seals of the opposing factions left:))
          - (above|seals)
        - ((Without other seals of the opposing factions left:))
          - (continue)
    - ((With Seals of the Faceless in backpack:))
      - Hand in Sliske seals.
        - (The seals are exchanged for reputation.)
        - Your Seals of the faceless were worth [number] reputation with the Zamorakian forces!
        - (Condition: If new rewards were unlocked:)
          - (see|Reputation (Heart of Gielinor))
          - (continue)
        - ((With other seals of the opposing factions left:))
          - (above|seals)
        - ((Without other seals of the opposing factions left:))
          - (continue)
    - ((With Seals of the Dragon riders in backpack:))
      - Hand in Zaros seals
        - (The seals are exchanged for reputation.)
        - Your Seals of the Dragon riders were worth [number] reputation with the Zamorakian forces!
        - (Condition: If new rewards were unlocked:)
          - (see|Reputation (Heart of Gielinor))
          - (continue)
        - ((With other seals of the opposing factions left:))
          - (above|seals)
        - ((Without other seals of the opposing factions left:))
          - (continue)
    - ((With multiple types of opposing factions' seals in backpack:))
      - Hand in all seals.
        - (The seals are exchanged for reputation.)
        - ((If Seals of the Cywir were handed in:))
          - Your Seals of the Cywir were worth [number] reputation with the Zamorakian forces!
          - (continue)
        - ((If Seals of the Faceless were handed in:))
          - Your Seals of the faceless were worth [number] reputation with the Zamorakian forces!
          - (continue)
        - ((If Seals of the Dragon riders were handed in:))
          - Your Seals of the Dragon riders were worth [number] reputation with the Zamorakian forces!
          - (continue)
        - (Condition: If new rewards were unlocked:)
          - (see|Reputation (Heart of Gielinor))
          - (continue)
        - (continue)
    - No thank you.
      - (continue)
- **SELECT AN OPTION**
  - What's going on here?
    - **Furies' Chosen:** You find yourself in the Heart of Gielinor, adventurer. Hear the cries and relish the chaos of the battlefield as the forces of Zamorak do battle with the vile minions of Zaros, Sliske and Seren! Leading us into battle are the ferocious Twin Furies: Avaryss the unceasing and Nymora the vengeful.
    - **Player:** Why are you all just stood here? Shouldn't you be fighting?
    - **Furies' Chosen:** We are not all savages. Upon this platform a truce has been established, allowing us - the envoys of each faction - to use words rather than violence to sway fresh recruits. For below the battle rages on, so we must do what we can to persuade the mercenaries that join the fray to fight for our cause. Take a look at what I have to offer. I assure you, I'll make it worth your while to fight for Zamorak.
    - (previous)
  - What is your opinion of me?
    - ((Zamorak Reputation Rewards interface opens.))
  - How can I improve my reputation?
    - **Furies' Chosen:** There are a few ways you can improve your standing. The easiest thing you can do is defeat our enemies, and use Ingression fragments to call in reinforcements for us. The bounty master over there, Feng, can also help you improve your standing by offering you bounties. Speak to him if you'd like to know more. Oh, and I'm sure if you could somehow find a way to defeat the other factions' generals that would certainly earn you a lot of favour.
    - (previous)
  - Where can I get armour like that?
    - **Furies' Chosen:** You can collect armour shards and crests around the Heart which can then be combined to make armour similar to my own. If you prove your worth to me, I can show you how to improve it further and unlock its true potential.
    - (previous)
  - I'd like to reclaim my rewards.
    - ((If you currently have no rewards to claim:))
      - **Furies' Chosen:** There's nothing I can give you.
      - (previous)
    - ((With rewards to claim:))
      - **CHOOSE AN OPTION:**
        - I'd like to reclaim my insignia.
          - Furies' Chosen hands you a Zamorak insignia.
          - (previous2)
        - Never mind.
          - (previous2)

### Reputation

- ((Zamorak Reputation Rewards interface opens.))

### Reclaim

- (above|reclaim)

### Using anima crystal

- **Furies' Chosen:** That's an interesting Anima crystal you have there. Would you be willing to donate it?
- [Menu]: Hand in your Anima crystal?
  - [Choice]: Yes. (Gain 500 reputation with Zamorak)
  - (removes=anima crystal)
  - You have gained 500 reputation with the Zamorakian forces!
  - ((If Avernic components were unlocked:))
    - You can now discover the blueprint for Avernic components if you have at least 89 Invention.
    - (continue)
  - ((If Fury Wings were unlocked:))
    - You have unlocked the Fury Wings cosmetic override.
    - (continue)
  - **Furies' Chosen:** Thank you for your help.
  - [Choice]: No.
    - (end)

### Attempting to use a seal of opposing faction with 2,000 Zamorak reputation

- [You can't gain any more reputation with that faction.]
