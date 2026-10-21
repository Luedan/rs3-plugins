# King Bolren

- **Original Wiki Page**: [Transcript:King Bolren](https://runescape.wiki/w/Transcript%3AKing%20Bolren)
- **Letter**: `K`

---

## Dialogue Transcript


### In Tree Gnome Village


#### Before Tree Gnome Village

- (see|Tree Gnome Village)

#### After Tree Gnome Village

- **Player:** Hello again Bolren.
- **King Bolren:** Well hello, it's good to see you again.
- (Condition: If the gnome amulet has been lost:)
  - **Player:** I've lost my amulet.
  - **King Bolren:** Oh dear. Here, take another. We are truly indebted to you.
  - (receives=gnome amulet)

#### After The Eyes of Glouphrie

- **Player:** Hello again Bolren.
- **King Bolren:** Well hello, it's good to see you again.
- (Condition: If the gnome amulet has been lost:)
  - **Player:** I've lost my amulet.
  - **King Bolren:** Oh dear. Here, take another. We are truly indebted to you.
  - (receives=gnome amulet)
  - (continue)
- ((Quest Overview interface for The Path of Glouphrie opens.))
  - [Choice]: Not Right Now
    - (end)
  - [Choice]: Accept Quest
    - (Condition: Without meeting the quest's requirements:)
      - You do not meet the requirements to start : 'The Path of Glouphrie'.
      - (pop-up)
        - {{Pop-up|You do not meet the requirements to start : 'The Path of Glouphrie'.|warning=yes}}
    - (Condition: Meeting the quest's requirements:)
      - (see|The Path of Glouphrie)

#### After The Path of Glouphrie

- (Condition: If the gnome amulet has been lost:)
  - **Player:** I've lost my amulet.
  - **King Bolren:** Oh dear. Here, take another. We are truly indebted to you.
  - (receives=gnome amulet)
  - (continue)
- **Player:** I think I know where Arposandra is now!
- **King Bolren:** Really? Have you been there?
- **Player:** Not exactly. I've found a way in, although I can't open the vent to get in there yet.
- **King Bolren:** So, you haven't actually been there. Well, I'm still not convinced that it's a real place. There's something about lost cities that gets explorers and adventurers obsessed.
- **Player:** I'm not obsessed, but I *will* find a way in. Eventually.
- **King Bolren:** Of course you will.

#### After The Prisoner of Glouphrie

- (Condition: If the gnome amulet has been lost:)
  - **Player:** I've lost my amulet.
  - **King Bolren:** Oh dear. Here, take another. We are truly indebted to you.
  - (receives=gnome amulet)
  - (continue)
- **Player:** I found Arposandra!
- **King Bolren:** Really? You've actually been there?
- **Player:** Briefly, yes. It really is a dangerous place.
- **King Bolren:** I don't believe you! You've got to be joking.
- **Player:** Maybe, one day, you'll believe me.

#### Treasure Trails

- **King Bolren:** Congratulations, human!
- (removes=the old clue scroll (medium))
- ((If the trail continues:))
  - (receives=a new clue scroll (medium))
  - [King Bolren has given you your next clue scroll!]
- ((If the trail ends:))
  - (receives=reward casket (medium))
  - [You've found a casket!]

#### Gnome Restaurant delivery

- **King Bolren:** Thank you. I don't have any gnome cooks here. I should really do something about that.
