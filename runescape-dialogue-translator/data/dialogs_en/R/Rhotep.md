# Rhotep

- **Original Wiki Page**: [Transcript:Rhotep](https://runescape.wiki/w/Transcript%3ARhotep)
- **Letter**: `R`

---

## Dialogue Transcript

{{Incomplete|Missing city quest dialogue.}}

### Standard dialogue

- **Rhotep:** I swear the master blacksmith is going crazy. He thinks someone keeps breaking in and making off with our anvils, yet they're still here.

### City quest dialogue

- **Rhotep:** Please, spare an ounce of your time to help an apprentice?
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Rhotep:** Thank you so much.
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
    - **Rhotep:** Oh, what will I do?

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

- **Rhotep:** The magnificent Crondis has been angered by [monster]. She requires a blood sacrifice and a tribute.
- **Rhotep:** First, go and kill [number] [monster].
- **Player:** What have the [monster] done to anger the almighty Crondis?
- **Rhotep:** You don't need to know. Will you go to kill them?
- [Menu]: Select an option
  - [Choice]: Yes.
    - **Rhotep:** Thank you so much.
  - [Choice]: No.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Rhotep:** Oh, what will I do?
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Rhotep:** Oh, what will I do?
      - [Choice]: No.
        - **Rhotep:** Oh, what will I do?

##### Task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Rhotep:** Have you vanquished the [number] [monster] for Lady Crondis? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Rhotep:** Have you vanquished the [number] [monster] for Lady Crondis? ([number] remaining)
    - **Player:** Yes, I have slaughtered the [monster].
    - (receives=Slayer experience)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task #2


##### First time

- **Rhotep:** Praise be to Crondis!
- **Rhotep:** Now the pitiful wretches have paid for their transgressions, we require a burnt offering.

##### Afterwards

- **Rhotep:** The next things I need are [item].
- **Player:** Right. Why [item]?
- **Rhotep:** The first step towards appeasing Crondis is traditionally a burnt offering of [item].
- **Rhotep:** So please go and get [number] [item].
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Rhotep:** Thank you so much.
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Rhotep:** Oh, what will I do?
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Rhotep:** Oh, what will I do?
      - [Choice]: No.
        - **Rhotep:** Oh, what will I do?

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Rhotep:** Do you have the tribute for Crondis? She grows impatient. I need [number] [item]. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Rhotep:** Do you have the tribute for Crondis? She grows impatient. I need [number] [item]. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Rhotep ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Rhotep:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Rhotep:** Do you have the tribute for Crondis? She grows impatient. I need [number] [item]. ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Rhotep ([number]/[number])
    - **Rhotep:** May the great crocodile smile upon you!
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Rhotep:** Finally, as per tradition, Crondis requires a liquid offering to be poured into the Elid.
- **Player:** A liquid offering?
- **Rhotep:** Yes, gather [number] [item] for me and I will have workers liquidise them.
- [Menu]: Select an option
  - [Choice]: Sure.
    - **Rhotep:** Thank you so much.
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Rhotep:** Oh, what will I do?
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Rhotep:** Oh, what will I do?
      - [Choice]: No.
        - **Rhotep:** Oh, what will I do?

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Rhotep:** Have you gathered the [number] [item]? We need to appease Crondis as soon as possible! ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Rhotep:** Have you gathered the [number] [item]? We need to appease Crondis as soon as possible! ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Rhotep ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Rhotep:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Rhotep:** Have you gathered the [number] [item]? We need to appease Crondis as soon as possible! ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Rhotep ([number]/[number])
    - **Rhotep:** Aren't you industrious! Good job.
    - **Rhotep:** Thank you so much for helping me!
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

- {{transcript missing}}
