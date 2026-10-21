# Galahad

- **Original Wiki Page**: [Transcript:Galahad](https://runescape.wiki/w/Transcript%3AGalahad)
- **Letter**: `G`

---

## Dialogue Transcript


### Talk-to


#### Before Holy Grail

- **Galahad:** Welcome to my home. It's rare for me to have guests! Would you like a cup of tea? I'll just put the kettle on.
- Brother Galahad hangs a kettle over the fire.
- **Player:** Do you get lonely out here on your own?
- **Galahad:** Sometimes I do, yes. Still not many people to share my solidarity, as the Saradomin I know is so unlike the one worshipped here.
- **Galahad:** Half a moment, your cup of tea is ready.
- [Brother Galahad gives you a cup of tea.]
- (receives=cup of tea)
- (Condition: If the player is speaking to him for the first time:)
  - {{RSFontAchievement|Stir, Galahad|Have Sir Galahad make you a cup of tea.}}

#### After Holy Grail

- **Galahad:** Welcome back! Would you like a cup of tea? I'll just put the kettle on.
- Brother Galahad hangs a kettle over the fire.
- [Menu]: What would you like to say?
  - [Choice]: I returned the Holy Grail to Camelot!
    - **Player:** I returned the Holy Grail to Camelot!
    - **Galahad:** I'm impressed! That's something I was never able to do. Half a moment, your cup of tea is ready.
    - (Condition: If the player does not have at least one free backpack space:)
      - [Brother Galahad offers you a cup of tea.]
      - **Galahad:** Oh dear, you don't have room to hold it.<br/>I'd better not let it go to waste...
      - {{Qact|Galahad drinks the cup of tea.}}
      - **Galahad:** {{RSChat|Aaah, nothing like a nice cuppa tea!}}
    - (Condition: If the player has at least one free backpack space:)
      - (receives=cup of tea)
      - [Brother Galahad gives you a cup of tea.]
  - [Choice]: cond=If the player lost the holy table napkin:|I have lost the holy table napkin.
    - **Player:** I have lost the holy table napkin.
    - (Condition: If the player does not have at least one free backpack space:)
      - **Galahad:** Oh dear. But I can't give you another one unless you free up some inventory space.
      - **Galahad:** Adventurers always have too many possessions; I'm glad I chose a simpler life. Now, let's see about that tea...
      - (continuea|receive-tea)
    - (Condition: If the player has at least one free backpack space:)
      - **Galahad:** Lucky I had more than one, eh?
      - [Galahad gives you another table napkin.<br/>He winks at you.]
      - **Galahad:** Try not to lose this one!<br/>Oh, I see your cup of tea is ready.
      - (continuea|receive-tea)
  - [Choice]: It's very peaceful here.
    - **Player:** It's very peaceful here.
    - **Galahad:** Yes, I find the tranquility helps me come ever closer to understanding the true meaning of life.
    - **Player:** The true meaning of life?<br/>Can you tell me what it is?
    - **Galahad:** Half a moment, your cup of tea is ready.
    - (continuea|receive-tea)
