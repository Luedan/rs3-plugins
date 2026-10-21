# Gregorovic's Chosen

- **Original Wiki Page**: [Transcript:Gregorovic's Chosen](https://runescape.wiki/w/Transcript%3AGregorovic%27s%20Chosen)
- **Letter**: `G`

---

## Dialogue Transcript


### Talk to

- **Gregorovic's Chosen:** Yeeeeeassss?
- ((With an anima crystal in backpack:))
  - **Gregorovic's Chosen:** That's an interesting Anima crystal you have there. Would you be willing to donate it?
  - [Menu]: Hand in your Anima crystal?
    - [Choice]: Yes. (Gain 500 reputation with Sliske)
      - (removes=anima crystal)
      - You have gained 500 reputation with the Sliskean forces!
      - (Condition: If new rewards were unlocked:)
        - (see|Reputation (Heart of Gielinor))
        - (continue)
      - **Gregorovic's Chosen:** Thank you for your help.
      - (continue)
    - [Choice]: No.
      - (continue)
- (Condition: With seals of opposing factions in backpack and under 2,000 Sliske reputation:)
  - **Gregorovic's Chosen:** I notice you have a stock of seals from around the Heart. Would you be interested in donating them?
  - **EXCHANGE SEALS FOR REPUTATION WITH THE SLISKEANS?**
    - ((With Seals of the Cywir in backpack:))
      - Hand in Seren seals.
        - (The seals are exchanged for reputation.)
        - Your Seals of the Cywir were worth [number] reputation with the Sliskean forces!
        - (Condition: If new rewards were unlocked:)
          - (see|Reputation (Heart of Gielinor))
          - (continue)
        - ((With other seals of the opposing factions left:))
          - (above|seals)
        - ((Without other seals of the opposing factions left:))
          - (continue)
    - ((With Seals of the Furies in backpack:))
      - Hand in Zamorak seals.
        - (The seals are exchanged for reputation.)
        - Your Seals of the Furies were worth [number] reputation with the Sliskean forces!
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
        - Your Seals of the Dragon riders were worth [number] reputation with the Sliskean forces!
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
          - Your Seals of the Cywir were worth [number] reputation with the Sliskean forces!
          - (continue)
        - ((If Seals of the Furies were handed in:))
          - Your Seals of the Furies were worth [number] reputation with the Sliskean forces!
          - (continue)
        - ((If Seals of the Dragon riders were handed in:))
          - Your Seals of the Dragon riders were worth [number] reputation with the Sliskean forces!
          - (continue)
        - (Condition: If new rewards were unlocked:)
          - (see|Reputation (Heart of Gielinor))
          - (continue)
        - (continue)
    - No thank you.
      - (continue)
- **SELECT AN OPTION**
  - What's going on here?
    - **Gregorovic's Chosen:** You find yourself in the Heart of Gielinor, adventurer. Here the helpless minions of Zamorak, Seren and Zaros face the relentless onslaught of Sliske's forces. We're even lead by Sliske's secret weapon, the most terrible of us all: Gregorovic, the faceless one.
    - **Player:** Why are you all just stood here? Shouldn't you be fighting?
    - **Gregorovic's Chosen:** We are not all savages. Upon this platform a truce has been established, allowing us - the envoys of each faction - to use words rather than violence to sway fresh recruits. For below the battle rages on, so we must do what we can to persuade the mercenaries that join the fray to fight for our cause. Take a look at what I have to offer. I assure you, I'll make it worth your while to fight for Sliske.
    - (previous)
  - What is your opinion of me?
    - ((Sliske Reputation Rewards interface opens.))
  - How can I improve my reputation?
    - **Gregorovic's Chosen:** There are a few ways you can improve your standing. The easiest thing you can do is defeat our enemies, and use Ingression fragments to call in reinforcements for us. The bounty master over there, Feng, can also help you improve your standing by offering you bounties. Speak to him if you'd like to know more. Oh, and I'm sure if you could somehow find a way to defeat the other factions' generals that would certainly earn you a lot of favour.
    - (previous)
  - Where can I get armour like that?
    - **Gregorovic's Chosen:** You can collect armour shards and crests around the Heart which can then be combined to make armour similar to my own. If you prove your worth to me, I can show you how to improve it further and unlock its true potential.
    - (previous)
  - I'd like to reclaim my rewards.
    - ((If you currently have no rewards to claim:))
      - **Gregorovic's Chosen:** There's nothing I can give you.
      - (previous)
    - ((With rewards to claim:))
      - (Condition: Without free backpack space:)
        - **Gregorovic's Chosen:** You don't have enough space in your inventory.
        - (previous2)
      - (Condition: With free backpack space:)
        - [Menu]: Choose an option:
          - [Choice]: I'd like to reclaim my insignia.
            - (receives=Sliske insignia)
            - [Gregorovic's Chosen hands you a Sliske insignia.]
            - (previous2)
          - [Choice]: cond=With the faction specific toy unlocked:|I'd like to reclaim my toy.
            - (receives=mysterious bottle)
            - [Gregorovic's Chosen hands you a Mysterious bottle.]
            - (previous2)
          - [Choice]: Never mind.
            - (previous2)

### Reputation

- ((Sliske Reputation Rewards interface opens.))

### Reclaim

- (above|reclaim)

### Attempting to use a seal of opposing faction with 2,000 Sliske reputation

- [You can't gain any more reputation with that faction.]
