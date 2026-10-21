# Malala

- **Original Wiki Page**: [Transcript:Malala](https://runescape.wiki/w/Transcript%3AMalala)
- **Letter**: `M`

---

## Dialogue Transcript

{{incomplete|Missing city quest dialogue.}}

### Standard dialogue

- **Malala:** When the whole world is silent, even one voice becomes powerful.

### City quest dialogue

- **Malala:** Greetings, stranger. As much as I'd rather not ask for help, I have a serious problem. Would you please assist me?
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Malala:** Thank you, you are kind.
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
    - **Malala:** That is a shame, though maybe someone else will help. I hope...

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


##### Task #1

- **Malala:** I'm ready for a change in career.
- **Player:** Oh, really? How can I help?
- **Malala:** Well, I really want to be a Slayer master, though I could do with some practice.
- **Player:** Alright, give it your best shot.
- **Malala:** Greetings, adventurer! It is I, the Slayer master!
- **Malala:** How was that?
- **Player:** Yeah, that was great, but you have to tell me what you want me to slay.
- **Malala:** Oh, right!
- **Malala:** Adventurer! I need you to slay...uh...
- **Malala:** I need you to slay...[number]...[monster]?
- [Menu]: Select an option
  - [Choice]: I can do that.
    - **Malala:** Thank you, you are kind.
    - **Player:** Where could I find [monster]?
    - (Condition: If the monster assigned is desert lizards:)
<!-- This needs double-checking -->
      - {{anchor|first}} **Malala:** They can be found out to the east in the desert.
    - (Condition: If the monster assigned is bandits:)
<!-- This needs double-checking -->
      - {{anchor|first}} **Malala:** There's a large bandit camp north of here, past the quarry, I think.
    - (Condition: If the monster assigned is scorpions:)
      - {{anchor|first}} **Malala:** They are far to the north, in the mine near Al Kharid. I think.
  - [Choice]: No.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Malala:** That is a shame, though maybe someone else will help. I hope...
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Malala:** That is a shame, though maybe someone else will help. I hope...
      - [Choice]: No.
        - **Malala:** That is a shame, though maybe someone else will help. I hope...

##### Task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Malala:** Did you slay the [number] [monster]? ([number] remaining)
    - **Player:** Not yet. Where could I find [monster] again?
<!-- Seems to continue the above but removes ". I think." -->
    - (continuea|first)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Malala:** Did you slay the [number] [monster]? ([number] remaining)
    - **Player:** Yeah, the [monster] have been slain!
    - (receives=Slayer experience)
    - **Malala:** Great job, adventurer!
    - **Malala:** So what do I do now?
    - **Player:** Tell me what I need to slay next.
    - **Malala:** Again? Okay!
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2

- **Malala:** Adventurer! I need to you slay more things for me!
- **Player:** What must I slay for you, Slayer master?
- **Malala:** I have decided that you must slay [number] [monster].
- [Menu]: Select an option
  - [Choice]: You sure can.
    - **Malala:** Thank you, you are kind.
    - **Player:** Where could I find [monster]?
    - (Condition: If the monster assigned is bandits:)
      - {{anchor|first}} **Malala:** There's a large bandit camp north of here, past the quarry. At least that's where I was told...
    - (Condition: If the monster assigned is kalphites:)
      - {{anchor|first}} **Malala:** They're found inside Kalphite hives under the desert sands. At least that's where I was told...
    - (Condition: If the monster assigned is scabarites:)
      - {{anchor|first}} **Malala:** They mainly dwell in the Scabarite Hive. At least that's where I was told...
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Malala:** That is a shame, though maybe someone else will help. I hope...
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Malala:** That is a shame, though maybe someone else will help. I hope...
      - [Choice]: No.
        - **Malala:** That is a shame, though maybe someone else will help. I hope...

##### Task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Malala:** Have you dealt with the [number] [monster] yet? ([number] remaining)
    - **Player:** Nope. Where can I find the [monster] again?
    - (Condition: If the monster assigned is bandits:)
      - {{anchor|first}} **Malala:** There's a large bandit camp north of here, past the quarry.
    - (Condition: If the monster assigned is scabarites:)
      - {{anchor|first}} **Malala:** They mainly dwell in the Scabarite Hive.
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Malala:** Have you dealt with the [number] [monster] yet? ([number] remaining)
    - **Player:** Yep, the [monster] are no more.
    - (receives=Slayer experience)
    - **Malala:** I am getting really good at this!
    - **Malala:** Adventurer! I have one more task for you!
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Malala:** I want you to slay [number] [monster]!
- **Player:** Wow, straight to the point.
- [Menu]: Select an option
  - [Choice]: I'll do it.
    - **Malala:** Thank you, you are kind.
    - **Player:** Where could I find [monster]?
    - (Condition: If the monster assigned is exiled kalphites:)
      - {{anchor|first}} **Malala:** They're found inside the Exiled Kalphite Hives just North of the city.
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Malala:** That is a shame, though maybe someone else will help. I hope...
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Malala:** That is a shame, though maybe someone else will help. I hope...
      - [Choice]: No.
        - **Malala:** That is a shame, though maybe someone else will help. I hope...

##### Task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Malala:** Have you finished the task to kill [number] [monster]? ([number] remaining)
    - **Player:** Not yet. Could you point me in the direction of some [monster]?
    - (continuea|first)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Malala:** Have you finished the task to kill [number] [monster]? ([number] remaining)
    - **Player:** Yes, I have.
    - (receives=Slayer experience)
    - **Malala:** Delightful! Thank you for all the practice. I can't wait to tell more people to slay stuff.
    - **Malala:** Best of luck in the future, adventurer!
    - **Player:** Thanks!
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

#### War effort

- {{transcript missing}}
