# Banafrit

- **Original Wiki Page**: [Transcript:Banafrit](https://runescape.wiki/w/Transcript%3ABanafrit)
- **Letter**: `B`

---

## Dialogue Transcript

{{Incomplete|missing dialogue for city quests}}

### Standard dialogue

- **Banafrit:** Silly workers. Why don't they just come and live in this area instead? It's much nicer.

### City quest dialogue

- **Banafrit:** Oh, hi there, maybe you could help me?
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Banafrit:** I appreciate it!
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
    - Nevermind.

#### Attacked by wildlife

- {{transcript missing}}

#### Awaiting delivery

- {{transcript missing}}

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


##### Task #1

- **Banafrit:** The teenage son of a good friend of mine is slowly dying. Now it is not the time to let the sands take him from us.
- (Condition: If the item desired is balls of wool:)
  - {{anchor|first}} **Banafrit:** Could you please bring me [number] balls of wool? We could really use something for the cat to play with.
  - (continue)
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Banafrit:** I appreciate it!
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Banafrit:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Banafrit:** Nevermind.
      - [Choice]: No.
        - **Banafrit:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Banafrit:** Do you have [number] [item]? The boy really needs help. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Banafrit:** Do you have [number] of [item]? The boy really needs help. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Banafrit ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Banafrit:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Banafrit:** Do you have [number] of [item]? The boy really needs help. ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items)  (receives=experience)
    - Number of [item] given to Banafrit ([number]/[number])
    - **Banafrit:** Fantastic, thank you.
    - **Banafrit:** Good, thank you so much.
    - **Banafrit:** Now that's done, we need the next block of supplies.
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2

- **Banafrit:** The next supplies I require are a load of [item].
- **Player:** Right. Why [item]?
- **Banafrit:** The thaumaturge tells us that we need [item]. We didn't think it wise to argue.
- **Player:** Right. If this... thaumaturge thinks that a [item] could help, then I guess we should search for [item].
- **Banafrit:** I will make the preparations while you are away; is it a reasonable request?
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Banafrit:** I appreciate it!
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Banafrit:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Banafrit:** Nevermind.
      - [Choice]: No.
        - **Banafrit:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Banafrit:** Do you have [number] [item]? The boy needs help. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Banafrit:** Do you have [number] [item]? The boy needs help. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Banafrit ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Banafrit:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Banafrit:** Do you have [number] [item]? The boy needs help. ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Banafrit ([number]/[number])
    - **Banafrit:** I am grateful. Helping me with the [item 1] and now some [item 2], I appreciate it.
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Banafrit:** Oh no...
- **Player:** What?
- **Banafrit:** I am...hopeful. I worry that you have given us hope, only for the sands to snatch it from us.
- **Banafrit:** No matter. I will take this brief moment of solace for what it is.
- **Player:** A good idea. How else can I help?
- **Banafrit:** We have everything we need. If you still want to help: while we've been caring for the young boy, we've neglected our daily duties.
- (Condition: If the item desired is coal:)
  - {{anchor|first}} **Banafrit:** If you could obtain fuel for the furnace for us, you would allow us another day's peace.
  - (continue)
- (Condition: If the item desired is wolf bones:)
  - {{anchor|first}} **Banafrit:** If you could obtain wolf bones, dropped from wolves for us, you would allow us another day's peace.
  - (continue)
- **Banafrit:** Getting hold of [number] [item] should be sufficient.
- [Menu]: Select an option
  - [Choice]: Of course.
    - **Banafrit:** I appreciate it!
  - [Choice]: I don't have time right now.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Banafrit:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Banafrit:** Nevermind.
      - [Choice]: No.
        - **Banafrit:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Banafrit:** Do you have [number] [item]? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Banafrit:** Do you have [number] [item]? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Banafrit ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Banafrit:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Banafrit:** Do you have [number] of [item]? ([number] remaining)
    - **Player:** Yes, I have the [item]. I hope these will do.
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Banafrit ([number]/[number])
    - **Banafrit:** I am grateful. We all appreciate it.
    - **Banafrit:** Thank you so much for helping me!
    - (receives=Menaphite gift offering and 2,000 reputation in their chosen faction)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - (above)

#### New product

- {{transcript missing}}

#### Slayer master

- {{transcript missing}}

#### War effort

- {{transcript missing}}
