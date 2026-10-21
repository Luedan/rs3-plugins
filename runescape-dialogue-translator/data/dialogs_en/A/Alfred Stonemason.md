# Alfred Stonemason

- **Original Wiki Page**: [Transcript:Alfred Stonemason](https://runescape.wiki/w/Transcript%3AAlfred%20Stonemason)
- **Letter**: `A`

---

## Dialogue Transcript

{{Transcript npc|Alfred Stonemason}}

### Before There's No Place Like Home...

- (see|There's No Place Like Home...#Talking to Alfred Stonemason)

### After There's No Place Like Home...

- **Alfred Stonemason:** I hope you're getting along well with your housing journey!<br>Remember if you ever need a refresher on how things work, you can thumb through the Construction guidebook.
- **Alfred Stonemason:** Would you like one?
- [Menu]: Take a construction guidebook?
  - [Choice]: I'll take one!
    - (Condition: Without space in backpack:)
      - **Alfred Stonemason:** Clear some space in your backpack and I'll give you one.
    - (Condition: With space in backpack:)
      - (receives=construction guide)
      - **Alfred Stonemason:** Here you go!
  - [Choice]: No thanks.
    - (end)

### Historical dialogue prior to 13 July 2026


#### If the player doesn't own a house yet

- **Alfred Stonemason:** Do you need Construction help?
- [Menu]: Choose an option:
  - [Choice]: Tell me how I can get my own house.
    - **Alfred Stonemason:** See there were these wizards, right, and they needed more living space. So they figured out a way of making it so that stuff doesn't take up any room.
    - **Alfred Stonemason:** I don't really understand it myself, but now everyone can have their own two acres and it's all easily accessible right here.
    - **Alfred Stonemason:** Yeah, somewhere to hang your hat. Your roots. Your castle. A home of your own.
    - **Alfred Stonemason:** A fine magical house right here in Rimmington will set you back a mere 1,000 coins. You can always move the portal somewhere else later if you want. ''(Note: Alfred says 'Taverley' instead of 'Rimmington' in his voiceover.)
    - ((The following is shown in an interface titled "Buy a House":))
      - [Choice]: Cancel
        - **Alfred Stonemason:** Well, enjoy your player-owned cardboard box, or wherever it is you're going to sleep tonight!
        - (previous)
      - [Choice]: OK
        - (Condition: If the player does not have 1,000 coins:)
          - You can not afford that.
          - You need 1,000 coins to purchase a house.
          - (pop-up)
            - {{Pop-up|You need 1,000 coins to purchase a house.|warning=yes}}
        - (Condition: If the player has 1,000 coins:)
          - (removes=1,000 coins)
          - {{RSFontAchievement|Unreal Estate, Man|Buy a house of your own.}}
          - **Alfred Stonemason:** Great! Go on through that big purple portal over there and you can start adding rooms to the house! Actually, I have a guide book about it here somewhere.
          - (Condition: If the player does not have space in backpack:)
            - Your backpack is full. You can claim the construction guide from an estate agent.
            - (pop-up)
              - {{Pop-up|Your backpack is full. You can claim the construction guide from an estate agent.|warning=yes}}
          - (Condition: If the player has space in backpack:)
            - (receives=construction guide)
            - [This book will help you to start building your house.]
  - [Choice]: I need construction supplies.
    - (opens=Alfred Stonemason's Construction Shop)

#### If the player already owns a house

- **Alfred Stonemason:** Do you need Construction help?
- [Menu]: Choose an option:
  - [Choice]: I need construction supplies.
    - (opens=Alfred Stonemason's Construction Shop)
  - [Choice]: Tell me about the house I own.
    - **Alfred Stonemason:** See there were these wizards, right, and they needed more living space. So they figured out a way of making it so that stuff doesn't take up any room.
    - **Alfred Stonemason:** I don't really understand it myself, but now everyone can have their own two acres and it's all easily accessible right here.
    - **Alfred Stonemason:** Yeah, somewhere to hang your hat. Your roots. Your castle. A home of your own.
    - (previous)
  - [Choice]: Can you re-decorate my house please?
    - **Alfred Stonemason:** I most certainly can! I can have that done for you in a jiffy. What style were you looking for?
    - ((The following is shown in an interface titled "SELECT AN OPTION":))
    - What part of your house do you want to re-decorate?
      - [Choice]: House
        - ((The following is shown in an interface titled "SELECT AN OPTION":))
        - What house style do you want?
          - [Choice]: Basic wood (2,500 coins) ''(Original style)
            - (below2|zxz)
          - [Choice]: Basic stone (5,000 coins) ''(Requires level 10 Construction)
            - (below2|zxz)
          - [Choice]: Whitewashed stone (7,500 coins) ''(Requires level 20 Construction)
            - (below2|zxz)
          - [Choice]: Fremennik-style wood (10,000 coins) ''(Requires level 30 Construction)
            - (below2|zxz)
          - [Choice]: Tropical wood (15,000 coins) ''(Requires level 40 Construction)
            - (below2|zxz)
          - [Choice]: Fancy stone (25,000 coins) ''(Requires level 50 Construction)
            - (below2|zxz)
          - [Choice]: Dark stone (free) ''(Complete the 'Love Story' quest)
            - (below2|zxz)
          - [Choice]: Back
            - (previous)
      - [Choice]: Grounds
        - ((The following is shown in an interface titled "SELECT AN OPTION":))
        - What ground do you want??
          - [Choice]: Rough grass (5,000 coins) ''(Original style)
            - (below2|zxz)
          - [Choice]: Desert (7,500 coins) ''(Requires level 20 Construction)
            - (below2|zxz)
          - [Choice]: Barren earth (10,000 coins) ''(Requires level 30 Construction)
            - (below2|zxz)
          - [Choice]: Mown grass (15,000 coins) ''(Requires level 40 Construction)
            - (below2|zxz)
          - [Choice]: Tundra (100,000 coins) ''(Requires level 70 Construction)
            - (below2|zxz)
          - [Choice]: Back
            - (previous)
      - [Choice]: Dungeon
        - ((The following is shown in an interface titled "SELECT AN OPTION":))
        - What dungeon style do you want?
          - [Choice]: Rough stone (2,500 coins) ''(Original style)
            - (below2|zxz)
          - [Choice]: Smooth stone (5,000 coins)''(Requires level 10 Construction)
            - (below2|zxz)
          - [Choice]: Desert dungeon (7,500 coins) ''(Requires level 20 Construction)
            - (below2|zxz)
          - [Choice]: Mountain mine (10,000 coins) ''(Requires level 30 Construction)
            - (below2|zxz)
          - [Choice]: Tropical cave (15,000 coins) ''(Requires level 40 Construction)
            - (below2|zxz)
          - [Choice]: Stone blocks (25,000 coins) ''(Requires level 50 Construction)
            - (below2|zxz)
          - [Choice]: Back
            - (previous)
      - [Choice]: Lighting
        - ((The following is shown in an interface titled "SELECT AN OPTION":))
        - What lighting do you want?
          - [Choice]: Daytime (5,000 coins) ''(Original style)
            - (below2|zxz)
          - [Choice]: Dusk (1,500,000 coins)''(Requires level 75 Construction)
            - (below2|zxz)
          - [Choice]: Night (250,000 coins) ''(Requires level 85 Construction)
            - (below2|zxz)
          - [Choice]: Back
            - (previous)
  - [Choice]: Can you move my house please?
    - ((The following is shown in an interface titled "SELECT AN OPTION":))
    - Where would you like your house moved to?
      - [Choice]: Rimmington (5,000) ''(Original area)
        - (below2|xzx)
      - [Choice]: Taverley (5,000) ''(Requires level 1 Construction)
        - (below2|xzx)
      - [Choice]: Pollnivneach (7,500) ''(Requires level 20 Construction)
        - (below2|xzx)
      - [Choice]: Rellekka (10,000) ''(Requires level 30 Construction)
        - (below2|xzx)
      - [Choice]: Brimhaven (15,000) ''(Requires level 40 Construction)
        - (below2|xzx)
      - [Choice]: Yanille (25,000) ''(Requires level 50 Construction)
        - (below2|xzx)
      - [Choice]: Menaphos (50,000) ''(Requires level 50 Construction)
        - (below2|xzx)
      - [Choice]: Otot (Mazcab) (50,000) ''(Requires level 60 Construction)
        - (below2|xzx)
      - [Choice]: Prifddinas (50,000) ''(Requires level 75 Construction)
        - (below2|xzx)

#### Upon picking a redecoration option {{anchor|zxz}}


##### Without enough money

- You require [number] coins.
- (pop-up)
  - {{Pop-up|You require [number] coins.|warning=yes}}

##### Without the Construction level requirement

- You require level [number] Construction to use that style.
- (pop-up)
  - {{Pop-up|You require level [number] Construction to use that style.|warning=yes}}

##### Selecting dark stone without Love Story completed

- You must first complete the 'Love Story' quest.
- (pop-up)
  - {{Pop-up|You must first complete the 'Love Story' quest.|warning=yes}}

##### Selecting dark stone with Love Story completed

- **Alfred Stonemason:** Ah, you know Zenevivia? Classy lady, that.<br>Alright. The re-decoration is done.
- ((Returns to "SELECT AN OPTION" interface.))

##### Picking the same option as current

- Your [house/grounds/dungeon/lighting] is already in that style!
- (pop-up)
  - {{Pop-up|Your [house/grounds/dungeon/lighting] is already in that style!|warning=yes}}

##### Otherwise

- (removes=coins)
- **Alfred Stonemason:** Good choice.<br>Alright. The re-decoration is done.
- ((Returns to "SELECT AN OPTION" interface.))

#### Upon picking a location option{{anchor|xzx}}


##### Without enough money

- You require [number] coins to move your house there.
- (pop-up)
  - {{Pop-up|You require [number] coins to move your house there.|warning=yes}}

##### Without the Construction level requirement

- You require level [number] Construction to move your house there.
- (pop-up)
  - {{Pop-up|You require level [number] Construction to move your house there.|warning=yes}}

##### Picking the same option as current

- Your house is already there!
- (pop-up)
  - {{Pop-up|Your house is already there!|warning=yes}}

##### Otherwise

- (removes=coins)
- Your house has been moved to [location].
