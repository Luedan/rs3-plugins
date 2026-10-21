# Jaraah

- **Original Wiki Page**: [Transcript:Jaraah](https://runescape.wiki/w/Transcript%3AJaraah)
- **Letter**: `J`

---

## Dialogue Transcript


### Talk to

- **Player:** Hi!
- **Jaraah:** What? Can't you see I'm busy?
- [Menu]: Select an Option
  - [Choice]: Can you heal me?
    - ((Before the destruction of Duel Arena:))
      - **Jaraah:** Okay. This will hurt you more than it will me.
      - (continue)
    - ((After the destruction of Duel Arena:))
      - **Player:** Can you heal me?
      - **Jaraah:** These facilities aren't ideal for a hospital, but I can make them work.
      - **Jaraah:** Okay. This will hurt you more than it will hurt me.
      - (continue)
    - *If at full health:*
      - **Jaraah:** You look healthy to me!
      - (previous)
    - *If not at full health:*
      - You feel a little better.
      - (previous)
  - [Choice]: cond=Historical, before the destruction of Duel Arena|You must see some gruesome things.
    - **Jaraah:** It's a gruesome business, and, with the tools they give me, it gets more gruesome before it gets better.
  - [Choice]: cond=After the destruction of Duel Arena|You must have seen some gruesome things.
    - **Player:** You must have seen some gruesome things.
    - **Jaraah:** In my time at the Duel Arena? Certainly, it was a gruesome business.
    - **Jaraah:** But now that the arena has sunk back into the desert, things are a little bit better.
  - [Choice]: Why do they call you 'The Butcher'?
    - ((Before the destruction of Duel Arena:))
      - **Jaraah:** 'The Butcher'?
      - **Jaraah:** Ha!
      - **Jaraah:** Would you like me to demonstrate?
      - **Player:** Er... I'll give it a miss, thanks.
    - ((After the destruction of Duel Arena:))
      - **Player:** Why do they call you 'The Butcher'?
      - **Jaraah:** 'The Butcher'?
      - **Jaraah:** Ha!
      - **Jaraah:** Would you like me to demonstrate?
      - **Player:** Er...I'll give it a miss, thanks.

### Heal

- (above|heal)

### Treasure Trails

- **Jaraah:** Here! Now, I have work to do!
- (removes=the old clue scroll (medium))
- ((If the trail continues:))
  - (receives=a new clue scroll (medium))
  - [Jaraah has given you another clue scroll!]
- ((If the trail ends:))
  - (receives=reward casket (medium))
  - [You've found a casket!]
