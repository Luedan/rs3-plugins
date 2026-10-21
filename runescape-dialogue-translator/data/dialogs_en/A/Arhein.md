# Arhein

- **Original Wiki Page**: [Transcript:Arhein](https://runescape.wiki/w/Transcript%3AArhein)
- **Letter**: `A`

---

## Dialogue Transcript

{{transcript npc|Arhein}}

### Standard dialogue

- **Arhein:** Hello! Would you like to trade? I've a variety of wares for sale, as well as a special supply of pineapples and seaweed!
- **Select an Option**
  - {{topt|Let's trade.}}
    - **Player:** Let's trade.
    - {{tact|opens=Arhein's Store}}
  - {{topt|Is that your ship?}}
    - **Player:** Is that your ship?
    - **Arhein:** Yes, I use it to make deliveries to my customers up and down the coast. These crates here are all ready for my next trip.
    - **Select an Option**
      - {{topt|Where do you deliver to?}}
        - **Player:** Where do you deliver to?
        - **Arhein:** Oh, various places up and down the coast. Mostly Karamja and Port Sarim.
        - **Select an Option**
          - {{topt|I don't suppose I could get a lift anywhere?}}
            - **Player:** I don't suppose I could get a lift anywhere?
            - **Arhein:** Sorry pal, but I'm afraid I'm not quite ready to sail yet.
            - **Arhein:** I'm waiting on a big delivery of candles which I need to deliver further along the coast.
          - {{topt|Well, good luck with your business.}}
            - **Player:** Well, good luck with your business.
            - **Arhein:** Thanks buddy!
      - {{topt|Are you rich then?}}
        - **Player:** Are you rich then?
        - **Arhein:** Business is going reasonably well... I wouldn't say I was the richest of merchants ever, but I'm doing fairly well all things considered.
  - {{topt|No, thank you.}}
    - **Player:** No thanks.

### Pineapples option

- ((If the player hasn't purchased all of Arhein's stock of pineapples:))
  - **Arhein:** I've got [#] [pineapple/pineapples] in stock, going for 2 coins each. How many would you like?
  - ((If the player doesn't have at least 2 coins:))
    - **Player:** Sorry, I can't afford any.
    - (end)
  - Arhein has [#] [pineapple/pineapples]. You can afford [#].
    - ((Player is prompted for a number))
  - ((If a non-zero number was entered:))
    - (receives=noted pineapples)
    - {{tbox|pic=Pineapple detail.png|Arhein gives you [#] [pineapple/pineapples].}}
- ((If Arhein has no pineapples remaining:))
  - **Arhein:** I've run out of pineapples. Come back tomorrow and I should have some more.

### Seaweed option

- ((If the player hasn't purchased all of Arhein's stock of seaweed:))
  - **Arhein:** I've got [#] seaweed at the moment and they cost 2 coins each. How many would you like?
  - ((If the player doesn't have at least 2 coins:))
    - **Player:** Sorry, I can't afford any.
    - (end)
  - Arhein has [#] seaweed. You can afford [#].
    - ((Player is prompted for a number))
  - (receives=noted seaweed)
  - {{tbox|pic=Seaweed detail.png|Arhein gives you [#] seaweed.}}
- ((If Arhein has no seaweed remaining:))
  - **Arhein:** I've run out of seaweed. Come back tomorrow and I should have some more.

### Treasure Trails

- (removes=the old clue scroll (easy))
- ((If the trail continues:))
  - (receives=a new clue scroll (easy))
  - {{tbox|pic=Clue scroll (easy) detail.png|Arhein has given you another clue scroll!}}
- ((If the trail ends:))
  - (receives=reward casket (easy))
  - {{tbox|pic=Casket (easy) detail.png|You've found a casket!}}
- **Arhein:** Awesome stuff!
