# Lisah

- **Original Wiki Page**: [Transcript:Lisah](https://runescape.wiki/w/Transcript%3ALisah)
- **Letter**: `L`

---

## Dialogue Transcript

{{incomplete|needs city quest dialogue}}

### Standard dialogue

- **Lisah:** You look like you could probably smell a little better!

### Overhead dialogue

- **Lisah:** {{RSChat|Fine perfumes for sale!}}

### City quest dialogue

- **Lisah:** People tend to ignore me because I perhaps try too hard to sell them my fragrances. Maybe you could help me?
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Lisah:** I appreciate it.
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
    - **Lisah:** You smell.

#### Attacked by wildlife

- {{transcript missing}}

#### Awaiting delivery

- {{transcript missing}}

#### Children can't sleep

- {{transcript missing}}

#### Collector of curiosities


##### Task #1

- **Lisah:** I am a collector of curiosities, and I currently have the greatest collection of [item] in all of Menaphos!
- **Lisah:** Well, I did...
- **Player:** What happened?
- **Lisah:** Another collector has arrived in the city and their collection is dwarfing mine.
- **Player:** How many more [item] do they have?
- **Lisah:** I've heard they have [number] more [item] than I do.
- **Player:** So, if someone were to bring you [number] [item], you would have the greatest collection again?
- **Lisah:** Yes! Would you do this for me?
- [Menu]: Select an option
  - [Choice]: Okay, then.
    - **Lisah:** I appreciate it.
    - **Player:** Where could I find [item]?
    - (Condition: If the item desired is dragon bones:)
      - **Lisah:** Kill some dragons and bring back their bones.
    - (Condition: If the item desired is molten glass:)
      - **Lisah:** Molten glass is craftable using a bucket of sand and some soda ash.
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Lisah:** You smell.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Lisah:** You smell.
      - [Choice]: No.
        - **Lisah:** You smell.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Lisah:** Have you got the [number] [item]? ([number] remaining)
    - **Player:** Not yet. Where could I find [item] again?
    - (above)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Lisah:** Have you got the [number] [item]? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Lisah ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Lisah:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Lisah:** Have you got the [number] [item]? ([number] remaining)
    - **Player:** Yeah, got the [item]!
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Lisah ([number]/[number])
    - **Lisah:** Well, I guess this is a start...
    - **Player:** A start?
    - **Lisah:** I've just heard that my rival has just brought in new shipment of [item]...
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2

- **Lisah:** He heard that you brought me some [item 1], he now has [number] more [item 2] than I do, just to spite me.
- **Player:** What does that mean for you?
- **Lisah:** This is an arms race! You need to get me [number] more [item 2].
- **Player:** You collect [item 1] AND [item 2]?
- **Lisah:** I collect many things! I collect collections!
- **Player:** ...
- **Lisah:** So about those [number] more [item 2]...
- [Menu]: Select an option
  - [Choice]: Fine, okay.
    - **Lisah:** I appreciate it.
    - (Condition: If the item desired is copper ore:)
      - **Lisah:** Copper ore can be found south-east of Varrock.
    - (Condition: If the item desired is bat bones:)
      - **Lisah:** Kill some bats and bring back their bones.
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Lisah:** You smell.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Lisah:** You smell.
      - [Choice]: No.
        - **Lisah:** You smell.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Lisah:** Have you got [number] [item] yet? ([number] remaining)
    - **Player:** Nope, where can I find the [item] again?
    - (above)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Lisah:** Have you got [number] [item] yet? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Lisah ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Lisah:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Lisah:** Have you got [number] [item] yet? ([number] remaining)
    - **Player:** I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Lisah ([number]/[number])
    - **Lisah:** Thank you so much.
    - **Player:** No problem.
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Lisah:** Could you perhaps do one more tiny job for me?
- **Player:** Does it involve [item 1] or [item 2]?
- **Lisah:** No, of course not!
- **Player:** Really?
- **Lisah:** ...
- **Lisah:** Yes I promise, I need [number] more [item] for my final collection!
- **Lisah:** This is the last time I ask. I promise.
- **Lisah:** [number] [item]?
- [Menu]: Select an option
  - [Choice]: [number] [item]...
    - **Lisah:** You're a good person.
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Lisah:** You smell.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Lisah:** You smell.
      - [Choice]: No.
        - **Lisah:** You smell.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Lisah:** Have you got the [item]? I need [number]. ([number] remaining)
    - **Player:** Not yet. Could you point me in the direction of some [item]?
    - (Condition: If the item desired is bolts of cloth:)
      - **Lisah:** You could make these at a loom.
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Lisah:** Have you got the [item]? I need [number]. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Lisah ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Lisah:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Lisah:** Have you got the [item 3]? I need [number]. ([number] remaining)
    - **Player:** Yes, but I'm not getting you any more [item 3], [item 1] OR [item 2] after this.
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Lisah ([number]/[number])
    - **Lisah:** Finally, I once again have the greatest collection of [item 3] in Menaphos!
    - **Player:** What do you plan to do with the [item 1], [item 2], and the [item 3] now that you have them?
    - **Lisah:** I really don't know.
    - **Player:** Well, then...
    - **Player:** Good luck with that.
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - (above)

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
