# Vindicta's Chosen

- **Original Wiki Page**: [Transcript:Vindicta's Chosen](https://runescape.wiki/w/Transcript%3AVindicta%27s%20Chosen)
- **Letter**: `V`

---

## Dialogue Transcript


### Talk to

- **Vindicta's Chosen:** Greetings.
- ((With an anima crystal in backpack:))
  - **Vindicta's Chosen:** That's an interesting Anima crystal you have there. Would you be willing to donate it?
    - Yes. (Gain 500 reputation with Zaros)
      - (removes=anima crystal)
      - You have gained 500 reputation with the Zarosian forces!
      - (Condition: If new rewards were unlocked:)
        - (see|Reputation (Heart of Gielinor))
        - (continue)
      - **Vindicta's Chosen:** Thank you for your help.
      - (continue)
    - No.
      - (continue)
- (Condition: With seals of opposing factions in backpack and under 2,000 Zaros reputation:)
  - **Vindicta's Chosen:** I notice you have a stock of seals from around the Heart. Would you be interested in donating them?
  - **EXCHANGE SEALS FOR REPUTATION WITH THE ZAROSIANS?**
    - ((With Seals of the Cywir in backpack:))
      - Hand in Seren seals.
        - (The seals are exchanged for reputation.)
        - Your Seals of the Cywir were worth [number] reputation with the Zarosian forces!
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
        - Your Seals of the faceless were worth [number] reputation with the Zarosian forces!
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
        - Your Seals of the Furies were worth [number] reputation with the Zarosian forces!
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
          - Your Seals of the Cywir were worth [number] reputation with the Zarosian forces!
          - (continue)
        - ((If Seals of the Faceless were handed in:))
          - Your Seals of the faceless were worth [number] reputation with the Zarosian forces!
          - (continue)
        - ((If Seals of the Furies were handed in:))
          - Your Seals of the Furies were worth [number] reputation with the Zarosian forces!
          - (continue)
        - (Condition: If new rewards were unlocked:)
          - (see|Reputation (Heart of Gielinor))
          - (continue)
        - (continue)
    - No thank you.
      - (continue)
- **SELECT AN OPTION**
  - What's going on here?
    - **Vindicta's Chosen:** You find yourself in the Heart of Gielinor, adventurer. The Empty Lord watches over this vast cavern. Under his gaze we will lay waste to the minions of Seren, Zamorak and Sliske that oppose us. Commanding our forces from above is the mighty ilujanka Vindicta, riding atop her dragon Gorvek and instilling fear in our enemies.
    - **Player:** Why are you all just stood here? Shouldn't you be fighting?
    - **Vindicta's Chosen:** We are not all savages. Upon this platform a truce has been established, allowing us - the envoys of each faction - to use words rather than violence to sway fresh recruits. For below the battle rages on, so we must do what we can to persuade the mercenaries that join the fray to fight for our cause. Take a look at what I have to offer. I assure you, I'll make it worth your while to fight for Zaros.
    - (previous)
  - What is your opinion of me?
    - ((Zaros Reputation Rewards interface opens.))
  - How can I improve my reputation?
    - **Vindicta's Chosen:** There are a few ways you can improve your standing. The easiest thing you can do is defeat our enemies, and use Ingression fragments to call in reinforcements for us. The bounty master over there, Feng, can also help you improve your standing by offering you bounties. Speak to him if you'd like to know more. Oh, and I'm sure if you could somehow find a way to defeat the other factions' generals that would certainly earn you a lot of favour.
    - (previous)
  - Where can I get armour like that?
    - **Vindicta's Chosen:** You can collect armour shards and crests around the Heart which can then be combined to make armour similar to my own. If you prove your worth to me, I can show you how to improve it further and unlock its true potential.
    - (previous)
  - I'd like to reclaim my rewards.
    - ((If you currently have no rewards to claim:))
      - **Vindicta's Chosen:** There's nothing I can give you.
      - (previous)
    - ((With rewards to claim:))
      - **CHOOSE AN OPTION:**
        - I'd like to reclaim my insignia.
          - Vindicta's Chosen hands you a Zaros insignia.
          - (previous2)
        - ((Only with nightstone unlocked:))
          - I'd like to reclaim my toy.
            - (receives=nightstone)
            - Vindicta's Chosen hands you a Nightstone.
            - (previous2)
        - Never mind.
          - (previous2)

### Reputation

- ((Zaros Reputation Rewards interface opens.))

### Reclaim

- (above|reclaim)

### Attempting to use a seal of opposing faction with 2,000 Zaros reputation

- [You can't gain any more reputation with that faction.]
