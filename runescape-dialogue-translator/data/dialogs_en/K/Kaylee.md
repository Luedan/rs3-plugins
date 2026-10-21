# Kaylee

- **Original Wiki Page**: [Transcript:Kaylee](https://runescape.wiki/w/Transcript%3AKaylee)
- **Letter**: `K`

---

## Dialogue Transcript


### Talk-to


#### Normally

- **Kaylee:** Hi! What can I get you?
- [Menu]: What would you like to say?
  - [Choice]: What ales are you serving?
    - **Player:** What ales are you serving?
    - **Kaylee:** Well, we've got Asgarnian Ale, Wizard's Mind Bomb and Dwarven Stout, all for only 3 coins.
    - [Menu]: Select an Option
      - [Choice]: One Asgarnian Ale, please.
        - **Player:** One Asgarnian Ale, please.
        - (Condition: If the player does not have enough money:)
          - **Kaylee:** I said 3 coins! You haven't got 3 coins! {{anchor|isaid3coins}}
          - **Player:** Sorry, I'll come back another day.
        - (Condition: If the player has enough money:)
          - (removes=3 coins) (receives=Asgarnian ale)
          - **Player:** Thanks, Kaylee.
      - [Choice]: I'll try the Mind Bomb.
        - **Player:** I'll try the Mind Bomb.
        - (Condition: If the player does not have enough money:)
          - (above|isaid3coins)
        - (Condition: If the player has enough money:)
          - (removes=3 coins) (receives=Wizard's mind bomb)
          - **Player:** Thanks, Kaylee.
      - [Choice]: Can I have a Dwarven Stout?
        - **Player:** Can I have a Dwarven Stout?
        - (Condition: If the player does not have enough money:)
          - (above|isaid3coins)
        - (Condition: If the player has enough money:)
          - (removes=3 coins) (receives=Dwarven stout)
          - **Player:** Thanks, Kaylee.
      - [Choice]: I don't feel like any of those.
        - **Player:** I don't feel like any of those.
  - [Choice]: cond=After a certain point in Recipe for Disaster: Freeing the Mountain Dwarf|What can you tell me about dwarves and ale?
    - **Player:** What can you tell me about dwarves and ale?
    - **Kaylee:** Oh it's you again. Forgotten the secret already?
    - **Player:** No... I just... misplaced it.
    - **Kaylee:** Mmmmm... the secret is in the gold. Drop a gold coin into asgarnian ale and you'll get this weird golden ale that the dwarves seem to love, I think they're genetically attracted to gold.
    - **Player:** Thanks, I won't forg...err.. misplace it, this time.

#### With a keg of mead before making a delivery to Rising Sun during The Need for Mead event

- **Player:** I was wondering if you could give some feedback on this mead?
- **Kaylee:** I'd recognise those old kegs anywhere.
- **Kaylee:** I'd love to try the next batch of Leslie's mead.
- (removes=keg of mead) (receives=50 nectar)
- (see|nectar)
- ((Shown in a pop-up:))
  - {{Pop-up|You find 50 x Nectar as you hand over the keg of mead.|colour=#00FF00}}
  - (continue)
- **Kaylee:** Mead isn't my favourite choice of drink but that's very nice.
- **Kaylee:** That may be the best mead I've ever drunk actually.
- **Kaylee:** The flavours are very subtle. Delicious.
- **Player:** Fantastic, I'll pass that on. Thank you!

### Using coins on Kaylee

- **Kaylee:** Thanks!
- (removes=one coin)
