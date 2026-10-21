# Kharl

- **Original Wiki Page**: [Transcript:Kharl](https://runescape.wiki/w/Transcript%3AKharl)
- **Letter**: `K`

---

## Dialogue Transcript

{{incomplete|City quest dialogue.}}

### Standard dialogue

- **Kharl:** Do you ever like to just...dance? It's certainly an affordable hobby.

### Overhead dialogue

*Occasionally Kharl will talk to himself in overhead dialogue.*
- {{RSChat|Dance, Kharl, dance.|colour=yellow|shadow=yes}}

### City quest dialogue

- **Kharl:** Please...spare some time. I need some help.
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Kharl:** Ah...so kind!
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
    - **Kharl:** Nevermind.

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

- {{transcript missing}}

#### New product

- {{transcript missing}}

#### Slayer master

- {{transcript missing}}

#### War effort


##### Task #1

- **Kharl:** I've been tasked to procure supplies for the war effort.
- **Player:** Who are we- Who are YOU at war with?
- **Kharl:** All will be revealed. First up I need [number] [items]. Can I rely on you?
- [Menu]: Select an option
  - [Choice]: Affirmative.
    - **Kharl:** Ah...so kind!
  - [Choice]: Negative.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Kharl:** Oh, well, maybe someone else will pop along.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Kharl:** Oh, well, maybe someone else will pop along.
      - [Choice]: No.
        - **Kharl:** Oh, well, maybe someone else will pop along.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Kharl:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Kharl:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Kharl ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Kharl:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Kharl:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Kharl ([number]/[number])
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2


##### First time

- **Kharl:** Good work, soldier!
- **Kharl:** Now that's done, we need the next block of supplies.

##### Afterwards

- **Kharl:** The next supplies I require are a load of [item].
- **Player:** Right. Why [item]?
- **Kharl:** Have you ever tried to fight a war without [item]? I didn't think so.
- **Kharl:** The war effort requires [number] [item]. I assume I can trust you to obtain the [item]?
- [Menu]: Select an option
  - [Choice]: You sure can.
    - **Kharl:** Ah...so kind!
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Kharl:** Oh, well, maybe someone else will pop along.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Kharl:** Oh, well, maybe someone else will pop along.
      - [Choice]: No.
        - **Kharl:** Oh, well, maybe someone else will pop along.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Kharl:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Kharl:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Kharl ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Kharl:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Kharl:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Kharl ([number]/[number])
    - **Kharl:** Great! Now we are ready to drive the offensive home!
    - **Player:** Can I ask why you're talking like this?
    - **Kharl:** Whatever do you mean, soldier?
    - **Player:** You're talking like an imperial general. It's a bit off-putting.
    - **Kharl:** ...
    - **Kharl:** The guards are always watching. I have to keep up appearances.
    - **Player:** Right...fair enough. What else do...we...need for the war effort?
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Kharl:** Now is the time you have been waiting for, soldier! The killing!
- **Kharl:** We will finally vanquish our dreaded enemy, the [monster]!
- **Player:** What?
- **Kharl:** Yes, kill [number] [monster] in the name of the Pharaoh himself!
- [Menu]: Select an option
  - [Choice]: Okay.
    - **Kharl:** Ah...so kind!
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Kharl:** Oh, well, maybe someone else will pop along.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Kharl:** Oh, well, maybe someone else will pop along.
      - [Choice]: No.
        - **Kharl:** Oh, well, maybe someone else will pop along.

##### Task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - (Condition: If the monster is kalphites:)
      - **Kharl:** Have you killed [number] kalphites? They're found inside Kalphite hives under the desert sands. We might win this war yet! ([number] remaining)
    - (Condition: If the monster is plague frogs:)
      - **Kharl:** Have you killed [number] plague frogs? They're usually sliming around Sophanem. We might win this war yet! ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - (Condition: If the monster is kalphites:)
      - **Kharl:** Have you killed [number] kalphites? They're found inside Kalphite hives under the desert sands. We might win this war yet! ([number] remaining)
      - (continue)
    - (Condition: If the monster is plague frogs:)
      - **Kharl:** Have you killed [number] plague frogs? They're usually sliming around Sophanem. We might win this war yet! (0 remaining)
      - (continue)
    - **Player:** Yes, I have killed the [monster].
    - (receives=Slayer experience)
    - **Kharl:** Have you danced, as they say, in the blood of your enemies? Have you sent the souls of [number] [monster] to the Underworld?
    - **Kharl:** Not that those [monster] have souls, I believe they are truly beyond help.
    - **Kharl:** Thank you so much for helping me!
    - **Player:** I fear you still need a lot more help.
    - **Kharl:** Sorry, what?
    - **Player:** Nothing. It was my pleasure.
    - (receives=a Menaphite gift offering and 2,000 reputation in their chosen faction)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.
