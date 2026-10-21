# Helwyr's Chosen

- **Original Wiki Page**: [Transcript:Helwyr's Chosen](https://runescape.wiki/w/Transcript%3AHelwyr%27s%20Chosen)
- **Letter**: `H`

---

## Dialogue Transcript


### Talk to

- **Helwyr's Chosen:** Adventurer.
- ((With an anima crystal in backpack:))
  - **Helwyr's Chosen:** That's an interesting Anima crystal you have there. Would you be willing to donate it?
  - [Menu]: Hand in your Anima crystal?
    - [Choice]: Yes. (Gain 500 reputation with Seren)
      - (removes=anima crystal)
      - **Helwyr's Chosen:** Thank you for your help.
      - (continue)
    - [Choice]: No.
      - (continue)
- (Condition: With seals of opposing factions in backpack and under 2,000 Seren reputation:)
  - **Helwyr's Chosen:** I notice you have a stock of seals from around the Heart. Would you be interested in donating them?
  - **EXCHANGE SEALS FOR REPUTATION WITH THE SERENISTS?**
    - ((With Seals of the Faceless in backpack:))
      - Hand in Sliske seals.
        - (The seals are exchanged for reputation.)
        - Your Seals of the faceless were worth [number] reputation with the Serenist forces!
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
        - Your Seals of the Furies were worth [number] reputation with the Serenist forces!
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
        - Your Seals of the Dragon riders were worth [number] reputation with the Serenist forces!
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
        - ((If Seals of the Faceless were handed in:))
          - Your Seals of the faceless were worth [number] reputation with the Serenist forces!
          - (continue)
        - ((If Seals of the Furies were handed in:))
          - Your Seals of the Furies were worth [number] reputation with the Serenist forces!
          - (continue)
        - ((If Seals of the Dragon riders were handed in:))
          - Your Seals of the Dragon riders were worth [number] reputation with the Serenist forces!
          - (continue)
        - (Condition: If new rewards were unlocked:)
          - (see|Reputation (Heart of Gielinor))
          - (continue)
        - (continue)
    - No thank you.
      - (continue)
- **SELECT AN OPTION**
  - What's going on here?
    - **Helwyr's Chosen:** You find yourself in the Heart of Gielinor, adventurer. This place is a brutal battlefield, but we elves must face it if we are to fight back the hordes of Zamorak, Zaros and Sliske in the name of Seren! Our leader is the ancient Cywir hunter Helwyr. With his unrivalled shapeshifting power at the helm we cannot fail.
    - **Player:** Why are you all just stood here? Shouldn't you be fighting?
    - **Helwyr's Chosen:** We are not all savages. Upon this platform a truce has been established, allowing us - the envoys of each faction - to use words rather than violence to sway fresh recruits. For below the battle rages on, so we must do what we can to persuade the mercenaries that join the fray to fight for our cause. Take a look at what I have to offer. I assure you, I'll make it worth your while to fight for Seren.
    - (previous)
  - What is your opinion of me?
    - ((Seren Reputation Rewards interface opens.))
  - How can I improve my reputation?
    - **Helwyr's Chosen:** There are a few ways you can improve your standing. The easiest thing you can do is defeat our enemies, and use Ingression fragments to call in reinforcements for us. The bounty master over there, Feng, can also help you improve your standing by offering you bounties. Speak to him if you'd like to know more. Oh, and I'm sure if you could somehow find a way to defeat the other factions' generals that would certainly earn you a lot of favour.
    - (previous)
  - Where can I get armour like that?
    - **Helwyr's Chosen:** You can collect armour shards and crests around the Heart which can then be combined to make armour similar to my own. If you prove your worth to me, I can show you how to improve it further and unlock its true potential.
    - (previous)
  - I'd like to reclaim my rewards.
    - ((If you currently have no rewards to claim:))
      - **Helwyr's Chosen:** There's nothing I can give you.
      - (previous)
    - ((With rewards to claim:))
      - (Condition: Without free backpack space:)
        - **Helwyr's Chosen:** You don't have enough space in your inventory.
        - (previous2)
      - (Condition: With free backpack space:)
        - [Menu]: Choose an option:
          - [Choice]: I'd like to reclaim my insignia.
            - (receives=Seren insignia)
            - [Helwyr's Chosen hands you a Seren insignia.]
            - (previous2)
          - [Choice]: cond=With the faction specific toy unlocked:|I'd like to reclaim my toy.
            - (receives=daystone)
            - [Helwyr's Chosen hands you a Daystone.]
            - (previous2)
          - [Choice]: Never mind.
            - (previous2)

### Reputation

- ((Seren Reputation Rewards interface opens.))

### Reclaim

- (above|reclaim)

### Using a seal of the Cywir

- [You don't think the chosen would be pleased to hear about that particular accomplishment.]
