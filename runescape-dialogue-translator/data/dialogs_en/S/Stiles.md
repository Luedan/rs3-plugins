# Stiles

- **Original Wiki Page**: [Transcript:Stiles](https://runescape.wiki/w/Transcript%3AStiles)
- **Letter**: `S`

---

## Dialogue Transcript


### At Musa Point


#### Talking to him


##### Normally

- **Stiles:** Ay-uh, 'tis a grand day for the fishin'. Will ye be wantin' to exchange yer fish for banknotes?
- [Menu]: What would you like to say?
  - [Choice]: cond=If the player has used the Exchange option or asked "Which fish can you exchange?" before|Okay, exchange all my fish for banknotes.
    - **Player:** Okay, exchange all my fish for banknotes.
    - (Condition: With unnoted tuna, lobsters or swordfish in backpack:)
      - (removes=all unnoted tuna, lobster or swordfish in backpack) (receives=noted tuna, lobster and/or swordfish)
      - **Stiles:** There ye goes.
    - (Condition: Without unnoted tuna, lobsters or swordfish in backpack:)
      - **Stiles:** Ahhh, ye've nothing that ol' Stiles can exchange. I'll do yer lobbies, yer swordies an' yer tuna, that's all.
  - [Choice]: Who are you and why are you here?
    - **Player:** Who are you and why are you here?
    - **Stiles:** Ahhh, when I were a young'un my name were Nigel but, these days, folks mostly call me Stiles.
    - **Stiles:** Long time ago, in Draynor Village, there were three brothers who'd exchange yer stuff for bitty bits o' paper, like these new-fangled banknotes we've got today. Niles, Miles an' Giles they called themselves.
    - **Stiles:** They be long gone, like the golden days, but they were an inspiration to me, so I took this trade myself, an' I changed my name to Stiles.
    - **Player:** But why are you here, in this place?
    - **Stiles:** The smell of yon bananas were drivin' me scatty, so I can't go too near the fishing spots.
    - **Stiles:** A tough-lookin' geezer callin' himself a slayer master tried to give me a nosepeg once, but I bain't wearin' one o' them things. Ol' Stiles has a tender nose.
    - **Stiles:** So, would ye like me to exchange yer fish now?
    - (other)
  - [Choice]: Which fish can you exchange?
    - **Player:** Which fish can you exchange?
    - **Stiles:** Ahhh, ol' Stiles has banknotes for yer lobbies, yer swordies and yer tuna. 'Tis a grand service I be offerin' here, and nary a penny do I ask in return.
    - [Menu]: What would you like to say?
      - [Choice]: Why don't you exchange other fish?
        - **Player:** Why don't you exchange other fish?
        - **Stiles:** Ahhh, I bain't looking to learn a new trade at my age. Lobbies, swordies an' tuna is enough fer ol' Stiles. Would ye like me to exchange yer fish now?
        - (other)
      - [Choice]: Okay, exchange all my fish for banknotes.
        - (above|exchange1)
      - [Choice]: Who are you and why are you here?
        - (above|background)
      - [Choice]: No thanks.
        - **Player:** No thanks.
  - [Choice]: No thanks.
    - **Player:** No thanks.

##### On Community Egg Hunt

- **Stiles:** Ay-uh, 'tis a grand day for the fishin'. Will ye be wantin' to exchange yer fish for banknotes?
- **Player:** Hello there, I have no time to exchange right now, I'm actually on a hunt for some golden eggs.
- **Stiles:** Ah-ha 'tis you that be huntin' for this then.
- [Stiles produces a golden egg from the nearby barrel and hands it to you.]
- You found a golden egg! Cracking it open you discover your next clue.
- (pop-up)
  - {{Pop-up|You found a golden egg! Cracking it open you discover your next clue.|colour=#00FF00}}
  - (continue)
- The following has been added to your currency pouch: 3 x Egg points.
- The following has been added to your currency pouch: 10 x Treasure Trail Points.
- **Player:** Perfect, thanks Stiles!
- **Stiles:** {{Sic|ol'}} Stiles wishes yer good luck findin' the rest of 'em.

#### Exchange option

- (Condition: If the player has not used the Exchange option nor asked "Which fish can you exchange?" before:)
  - **Stiles:** Ye want me to exchange all yer lobbies, yer swordies an' yer tuna fer banknotes?
    - (above|whichfish)
- (Condition: If the player has used the Exchange option or asked "Which fish can you exchange?" before:)
  - (above|exchange2)
