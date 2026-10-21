# Inhamat

- **Original Wiki Page**: [Transcript:Inhamat](https://runescape.wiki/w/Transcript%3AInhamat)
- **Letter**: `I`

---

## Dialogue Transcript


### Standard dialogue

- **Inhamat:** I used to be a merchant, famed for my wines. All it takes is two bad harvests in a row to ruin a man.

### City quest dialogue

- **Inhamat:** Please...spare some time. I could really use some help.
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Inhamat:** Ah...thank you.
    - (Condition: If the city quest type is "Attacked by wildlife":)
      - (continue)
    - (Condition: If the city quest type is "Awaiting delivery":)
      - (continue)
    - (Condition: If the city quest type is "Children can't sleep":)
      - (continue)
    - (Condition: If the city quest type is "Collector of curiosities":)
      - (continue)
    - (Condition: If the city quest type is "Crondis is angry":)
      - (continue)
    - (Condition: If the city quest type is "Crop pests":)
      - (continue)
    - (Condition: If the city quest type is "Delivery help":)
      - (continue)
    - (Condition: If the city quest type is "Friend's son slowly dying":)
      - (continue)
    - (Condition: If the city quest type is "New product":)
      - (continue)
    - (Condition: If the city quest type is "Slayer master":)
      - (continue)
    - (Condition: If the city quest type is "War effort":)
      - (continue)
  - [Choice]: Not right now.
    - **Inhamat:** Nevermind.

#### Attacked by wildlife

- {{transcript missing}}

#### Awaiting delivery


##### Task #1

- **Inhamat:** I've been awaiting a delivery that contains some [item 1] and some [item 2]. I urgently need the [item 1], but folks on the pier say that there's no sign of the ship for miles.
- (Condition: If the item desired is barberry seeds:)
  - **Inhamat:** Do you think you could get me [number] barberry seeds? I'm desperate for seeds that grow into barberry bushes.
  - **Player:** Where could I find a barberry seed?
  - **Inhamat:** Barberry seeds are often dropped by monsters, or they can be procured from master farmers around Gielinor. Is that okay?
  - (continue)
- (Condition: If the item desired is rosemary seeds:)
  - **Inhamat:** Do you think you could get me [number] rosemary seeds? I'm desperate for seeds that grow into rosemary plants.
  - **Player:** Where could I find a rosemary seed?
  - **Inhamat:** Rosemary seeds are often dropped by monsters, or they can be procured from master farmers around Gielinor. Is that okay?
  - (continue)
- (Condition: If the item desired is bones:)
  - **Inhamat:** Do you think you could get me [number] rosemary seeds? I'm desperate for some regular old bones, dropped from creatures.
  - **Player:** Where could I find a pile of bones?
  - **Inhamat:** Almost every living thing has bones, right? It shouldn't be too hard to find some. Is that okay?
  - (continue)
- [Menu]: Select an option
  - [Choice]: Yes.
    - **Inhamat:** Ah...thank you.
  - [Choice]: No.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Inhamat:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Inhamat:** Nevermind.
      - [Choice]: No.
        - **Inhamat:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Inhamat:** Do you have [number] [item]? It's fairly urgent. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Inhamat:** Do you have [number] [item]? It's fairly urgent. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Inhamat ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Inhamat:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Inhamat:** Do you have [number] [item]? It's fairly urgent. ([number] remaining)
    - **Player:** Yep! I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Inhamat ([number]/[number])
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2


##### First time

- **Inhamat:** Yes! Thank you.
- **Inhamat:** Now that's done, we need the next block of supplies.

##### Afterwards

- **Inhamat:** The next supplies I'm missing are a load of [item].
- **Player:** ...and they still haven't arrived yet?
- (Condition: If the item desired is fire battlestaves:)
  - **Inhamat:** Nope! All I need is a staff infused with fire magic and the ports workers tell me it will be days before I see them.
  - (continue)
- (Condition: If the item desired is potatoes:)
  - **Inhamat:** Nope! All I need is a starchy, tuberous crop and the ports workers tell me it will be days before I see them.
  - (continue)
- (Condition: If the item desired is molten glass:)
  - **Inhamat:** Nope! All I need is some hot glass and the ports workers tell me it will be days before I see them.
  - (continue)
- **Inhamat:** Could you get me some to tide me over for now? About [number] [item] should do.
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Inhamat:** Ah...thank you.
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Inhamat:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Inhamat:**Nevermind.
      - [Choice]: No.
        - **Inhamat:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Inhamat:** Do you have [number] [item]? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Inhamat:** Do you have [number] [item]? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Inhamat ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Inhamat:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Inhamat:** Do you have [number] [item]? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Inhamat ([number]/[number])
    - **Inhamat:** Excellent. Saving the day with the [item 1] and now some [item 2], I appreciate your generosity.
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Inhamat:** Seeing as you're so resourceful, I wonder if you could save me a trip around the city...
- **Player:** Go on...
- (Condition: If the item desired is dwarf weed seeds:)
  - **Inhamat:** I need a way to grow dwarf weed herb bushes to see the month through. Approximately [number] dwarf weed seeds will save me a lot of hassle.
  - (continue)
- (Condition: If the item desired is goat horns:)
  - **Inhamat:** I need potion supplies to see the month through. Approximately [number] goat horns will save me a lot of hassle.
  - (continue)
- (Condition: If the item desired is rope:)
  - **Inhamat:** I need gear for climbing to see the month through. Approximately [number] lengths of rope will save me a lot of hassle.
  - (continue)
- **Inhamat:** Are [number] [item] too much to ask for? Will you find me some?
- [Menu]: Select an option
  - [Choice]: Of course.
    - **Inhamat:** Ah...thank you.
  - [Choice]: It's too much.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Inhamat:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Inhamat:** Nevermind.
      - [Choice]: No.
        - **Inhamat:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - (Condition: If the item desired is dwarf weed seeds:)
      - **Inhamat:** Do you have [number] dwarf weed seeds? Dwarf weed seeds are often dropped by monsters, or they can be procured from master farmers around Gielinor. ([number] remaining)
    - (Condition: If the item desired is goat horns:)
      - **Inhamat:** Do you have [number] goat horns? Goats can be found out around Nardah or west of the Kalphite Hive. ([number] remaining)
    - (Condition: If the item desired is rope:)
      - **Inhamat:** Do you have [number] lengths of rope? They should be in any general store. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - (Condition: If the item desired is dwarf weed seeds:)
      - **Inhamat:** Do you have [number] dwarf weed seeds? Dwarf weed seeds are often dropped by monsters, or they can be procured from master farmers around Gielinor. ([number] remaining)
      - (continue)
    - (Condition: If the item desired is goat horns:)
      - **Inhamat:** Do you have [number] goat horns? Goats can be found out around Nardah or west of the Kalphite Hive. ([number] remaining)
      - (continue)
    - (Condition: If the item desired is rope:)
      - **Inhamat:** Do you have [number] lengths of rope? They should be in any general store. ([number] remaining)
      - (continue)
    - (removes=the requested items)
    - Number of [item] given to Inhamat ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Inhamat:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - (Condition: If the item desired is dwarf weed seeds:)
      - **Inhamat:** Do you have [number] dwarf weed seeds? Dwarf weed seeds are often dropped by monsters, or they can be procured from master farmers around Gielinor. ([number] remaining)
      - (continue)
    - (Condition: If the item desired is goat horns:)
      - **Inhamat:** Do you have [number] goat horns? Goats can be found out around Nardah or west of the Kalphite Hive. ([number] remaining)
      - (continue)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Inhamat ([number]/[number])
    - **Inhamat:** Thank you so much for helping me!
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - (above)

#### Children can't sleep

- {{transcript missing}}

#### Collector of curiosities

- {{transcript missing}}

#### Crondis is angry

- {{transcript missing}}

#### Crop pests

- {{transcript missing}}

#### Delivery help

- {{transcript missing}}

#### Friend's son slowly dying

- {{transcript missing}}

#### New product

- {{transcript missing}}

#### Slayer master

- {{transcript missing}}

#### War effort

- {{transcript missing}}

### During the Gielinor Egg Hunt

- (see|Gielinor Egg Hunt (2024)#Talking to Inhamat)
