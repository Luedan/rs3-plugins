# Henutemipet

- **Original Wiki Page**: [Transcript:Henutemipet](https://runescape.wiki/w/Transcript%3AHenutemipet)
- **Letter**: `H`

---

## Dialogue Transcript


### Standard dialogue

- **Henutemipet:** I'm often the very last person to lay hands upon the deceased before they are entombed. There is a beautiful finality in everything, if you look for it.

### City quest dialogue

- **Henutemipet:** There is something I need help with, do you have some time?
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Henutemipet:** Gods smile upon you.
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
    - **Henutemipet:** The gods will send someone my way soon enough.

#### Attacked by wildlife

- {{transcript missing}}

#### Awaiting delivery

- {{transcript missing}}

#### Children can't sleep

- {{transcript missing}}

#### Collector of curiosities

- {{transcript missing}}

#### Crondis is angry


##### Task #1

- **Henutemipet:** The magnificent Crondis has been angered by [monster]. She requires a blood sacrifice and a tribute.
- **Henutemipet:** First, go and kill [number] [monster].
- **Player:** What have the [monster] done to anger the almighty Crondis?
- **Henutemipet:** You don't need to know. Will you go to kill them?
- [Menu]: Select an option
  - [Choice]: Yes.
    - **Henutemipet:** Gods smile upon you.
  - [Choice]: No.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Henutemipet:** The gods will send someone my way soon enough.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Henutemipet:** The gods will send someone my way soon enough.
      - [Choice]: No.
        - **Henutemipet:** The gods will send someone my way soon enough.

##### Task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Henutemipet:** Have you vanquished the [number] [monster] for Lady Crondis? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Henutemipet:** Have you vanquished the [number] [monster] for Lady Crondis? ([number] remaining)
    - **Player:** Yes, I have slaughtered the [monster].
    - (receives=Slayer experience)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task #2


##### First time

- **Henutemipet:** Praise be to Crondis!
- **Henutemipet:** Now the pitiful wretches have paid for their transgressions, we require a burnt offering.

##### Afterwards

- **Henutemipet:** The next things I need are [item].
- **Player:** Right. Why [item]?
- **Henutemipet:** The first step towards appeasing Crondis is traditionally a burnt offering of [item].
- **Henutemipet:** So please go and get [number] [item].
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Henutemipet:** Gods smile upon you.
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Henutemipet:** The gods will send someone my way soon enough.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Henutemipet:** The gods will send someone my way soon enough.
      - [Choice]: No.
        - **Henutemipet:** The gods will send someone my way soon enough.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Henutemipet:** Do you have the tribute for Crondis? She grows impatient. I need [number] [item]. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Henutemipet:** Do you have the tribute for Crondis? She grows impatient. I need [number] [item]. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Henutemipet ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Henutemipet:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Henutemipet:** Do you have the tribute for Crondis? She grows impatient. I need [number] [item]. ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Henutemipet ([number]/[number])
    - **Henutemipet:** May the great crocodile smile upon you!
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Henutemipet:** Finally, as per tradition, Crondis requires a liquid offering to be poured into the Elid.
- **Player:** A liquid offering?
- **Henutemipet:** Yes, gather [number] [item] for me and I will have workers liquidise them.
- [Menu]: Select an option
  - [Choice]: Sure.
    - **Henutemipet:** Gods smile upon you.
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Henutemipet:** The gods will send someone my way soon enough.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Henutemipet:** The gods will send someone my way soon enough.
      - [Choice]: No.
        - **Henutemipet:** The gods will send someone my way soon enough.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Henutemipet:** Have you gathered the [number] [item]? We need to appease Crondis as soon as possible! ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Henutemipet:** Have you gathered the [number] [item]? We need to appease Crondis as soon as possible! ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Henutemipet ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Henutemipet:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Henutemipet:** Have you gathered the [number] [item]? We need to appease Crondis as soon as possible! ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Henutemipet ([number]/[number])
    - **Henutemipet:** Aren't you industrious! Good job.
    - **Henutemipet:** Thank you so much for helping me!
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - (above)

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


##### Task #1

- **Henutemipet:** I've been tasked to procure supplies for the war effort.
- **Player:** Who are we- Who are YOU at war with?
- **Henutemipet:** All will be revealed. First up I need [number] [item]. Can I rely on you?
- [Menu]: Select an option
  - [Choice]: Affirmative.
    - **Henutemipet:** Gods smile upon you.
  - [Choice]: Negative.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - {{transcript missing}}
      - [Choice]: No.
        - **Henutemipet:** The gods will send someone my way soon enough.

##### With no item

- {{transcript missing}}

##### With some of the item

- {{transcript missing}}

##### With all of the item

- {{transcript missing}}

##### Task #2


##### First time

- {{transcript missing}}

##### Afterwards

- {{transcript missing}}

##### With no item

- {{transcript missing}}

##### With some of the item

- {{transcript missing}}

##### With all of the item

- {{transcript missing}}

##### Task #3

- {{transcript missing}}

##### Task incomplete

- {{transcript missing}}

##### Task complete

- {{transcript missing}}
