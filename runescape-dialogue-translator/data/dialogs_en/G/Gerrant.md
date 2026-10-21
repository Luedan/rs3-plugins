# Gerrant

- **Original Wiki Page**: [Transcript:Gerrant](https://runescape.wiki/w/Transcript%3AGerrant)
- **Letter**: `G`

---

## Dialogue Transcript


### In Port Sarim

- **Gerrant:** Welcome! You can buy fishing equipment at my store. We'll also buy anything you catch off you.
- [Menu]: Choose an option:
  - [Choice]: cond=After partial completion of Heroes' Quest|I want to find out how to catch a lava eel.
    - **Gerrant:** Lava eels, eh? That's a tricky one, that is. You'll need a lava-proof fishing rod. The method for making this would be to take an ordinary fishing rod, and then cover it with fire-proof blamish oil.
    - (Condition: After completion of Heroes' Quest:)
      - **Gerrant:** Of course, you knew that already.
      - (continue)
    - **Player:** So where can I fish lava eels?
    - **Gerrant:** Taverley dungeon or the lava maze in the Wilderness.
  - [Choice]: cond=If the player has lost their oily fishing rod|I've lost my oily fishing rod.
    - [Gerrant replaces your oily fishing rod.]
    - (receives=oily fishing rod)
  - [Choice]: Let's see what you've got then.
    - **Player:** Let's see what you've got then.
    - (opens=Gerrant's Fishy Business)
  - [Choice]: Sorry, I'm not interested.
    - **Player:** Sorry, I'm not interested.

### Treasure Trails

- **Gerrant:** You've done it!
- (removes=the old clue scroll (hard))
- ((If the trail continues:))
  - (receives=a new clue scroll (hard))
  - [Gerrant has given you another clue scroll!]
- ((If the trail ends:))
  - (receives=reward casket (hard))
  - [You've found a casket!]
