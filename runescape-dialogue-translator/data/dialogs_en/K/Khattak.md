# Khattak

- **Original Wiki Page**: [Transcript:Khattak](https://runescape.wiki/w/Transcript%3AKhattak)
- **Letter**: `K`

---

## Dialogue Transcript

{{incomplete|Missing city quest dialogue.}}

### Standard dialogue

- **Khattak:** The chariot driven by a crazy charioteer knows, he loves to keep greedy rats on their toes. While rushing on a path of woes, it crushes alike; friends and foes.

### Overhead dialogue

*Khattak will occasionally produce overhead dialogue.*
- {{RSChat|Roses are red.|colour=yellow|shadow=yes}}
- {{RSChat|Violets are blue.|colour=yellow|shadow=yes}}
- {{RSChat|No matter where,|colour=yellow|shadow=yes}}
- {{RSChat|They're watching you.|colour=yellow|shadow=yes}}

### City quest dialogue

- **Khattak:** Greetings. I am known by Khattak. I need a kind soul to release a valve that is building up pressure in my mind. Could you assist?
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Khattak:** My appreciation. I shall write another stanza depicting your kind deed...
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
    - **Khattak:** Maybe someone else will cast a rope into this gaping void...

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

- **Khattak:** The teenage son of a good friend of mine is slowly dying. Now it is not the time to let the sands take him from us.
- (Condition: If the item desired is balls of wool:)
  - {{anchor|first}} **Khattak:** Could you please bring me [number] balls of wool? We could really use something for the cat to play with.
  - (continue)
- (Condition: If the item desired is potatoes:)
  - {{anchor|first}} **Khattak:** Could you please bring me [number] potatoes? We could really use a starchy, tuberous crop.
  - (continue)
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Khattak:** My appreciation. I shall write another stanza depicting your kind deed...
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Khattak:** Maybe someone else will cast a rope into this gaping void...
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Khattak:** Maybe someone else will cast a rope into this gaping void...
      - [Choice]: No.
        - **Khattak:** Maybe someone else will cast a rope into this gaping void...

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Khattak:** Do you have [number] [item]? The boy really needs help. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Khattak:** Do you have [number] of [item]? The boy really needs help. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Khattak ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Khattak:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Khattak:** Do you have [number] of [item]? The boy really needs help. ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items)  (receives=experience)
    - Number of [item] given to Khattak ([number]/[number])
    - **Khattak:** Fantastic, thank you.
    - **Khattak:** Good, thank you so much.
    - **Khattak:** Now that's done, we need the next block of supplies.
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2

- **Khattak:** The next supplies I require are a load of [item].
- **Player:** Right. Why [item]?
- **Khattak:** The thaumaturge tells us that we need [item]. We didn't think it wise to argue.
- **Player:** Right. If this... thaumaturge thinks that a [item] could help, then I guess we should search for [item].
- **Khattak:** I will make the preparations while you are away; is it a reasonable request?
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Khattak:** My appreciation. I shall write another stanza depicting your kind deed...
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Khattak:** Maybe someone else will cast a rope into this gaping void...
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Khattak:** Maybe someone else will cast a rope into this gaping void...
      - [Choice]: No.
        - **Khattak:** Maybe someone else will cast a rope into this gaping void...

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Khattak:** Do you have [number] [item]? The boy needs help. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Khattak:** Do you have [number] [item]? The boy needs help. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Khattak ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Khattak:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Khattak:** Do you have [number] [item]? The boy needs help. ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Khattak ([number]/[number])
    - **Khattak:** I am grateful. Helping me with the [item 1] and now some [item 2], I appreciate it.
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Khattak:** Oh no...
- **Player:** What?
- **Khattak:** I am...hopeful. I worry that you have given us hope, only for the sands to snatch it from us.
- **Khattak:** No matter. I will take this brief moment of solace for what it is.
- **Player:** A good idea. How else can I help?
- **Khattak:** We have everything we need. If you still want to help: while we've been caring for the young boy, we've neglected our daily duties.
- (Condition: If the item desired is coal:)
  - {{anchor|first}} **Khattak:** If you could obtain fuel for the furnace for us, you would allow us another day's peace.
  - (continue)
- (Condition: If the item desired is wolf bones:)
  - {{anchor|first}} **Khattak:** If you could obtain wolf bones, dropped from wolves for us, you would allow us another day's peace.
  - (continue)
- **Khattak:** Getting hold of [number] [item] should be sufficient.
- [Menu]: Select an option
  - [Choice]: Of course.
    - **Khattak:** My appreciation. I shall write another stanza depicting your kind deed...
  - [Choice]: I don't have time right now.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Khattak:** Maybe someone else will cast a rope into this gaping void...
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Khattak:** Maybe someone else will cast a rope into this gaping void...
      - [Choice]: No.
        - **Khattak:** Maybe someone else will cast a rope into this gaping void...

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Khattak:** Do you have [number] [item]? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Khattak:** Do you have [number] [item]? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Khattak ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Khattak:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Khattak:** Do you have [number] of [item]? ([number] remaining)
    - **Player:** Yes, I have the [item]. I hope these will do.
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Khattak ([number]/[number])
    - **Khattak:** I am grateful. We all appreciate it.
    - **Khattak:** Thank you so much for helping me!
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
