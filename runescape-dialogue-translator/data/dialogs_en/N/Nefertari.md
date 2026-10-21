# Nefertari

- **Original Wiki Page**: [Transcript:Nefertari](https://runescape.wiki/w/Transcript%3ANefertari)
- **Letter**: `N`

---

## Dialogue Transcript

{{incomplete|Missing city quest dialogue.}}

### Standard dialogue

- **Nefertari:** Welcome to my stall! Would you like some bread?
- (opens=Nefertari's Bread Stall)

### Overhead dialogue

- **Nefertari:** {{RSChat|Buy my grains! Flour for sale!}}

### City quest dialogue

- **Nefertari:** Welcome to my stall! Would you like some bread? Actually...could you help me please?
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Nefertari:** Thank you!
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
    - **Nefertari:** Nevermind.

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


##### Task #1

- (Condition: If the item desired is bones:)
  - **Nefertari:** So, I have an acquaintance whom I regularly deliver bones to. They rely on me to make deliveries on a regular schedule.
  - **Nefertari:** I have no idea why it is always bones that are requested. I'm not going to question why someone needs some regular old bones, dropped from creatures.
  - (continue)
- (Condition: If the item desired is fire battlestaves:)
  - **Nefertari:** So, I have an acquaintance whom I regularly deliver fire battlestaves to. They rely on me to make deliveries on a regular schedule.
  - **Nefertari:** I have no idea why it is always fire battlestaves that are requested. I'm not going to question why someone needs a staff infused with fire magic.
  - (continue)
- **Nefertari:** Could you please bring me [number] [item]?
- [Menu]: Select an option
  - [Choice]: Okay, then.
    - **Nefertari:** Thank you!
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Nefertari:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Nefertari:** Nevermind.
      - [Choice]: No.
        - **Nefertari:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Nefertari:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Nefertari:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Nefertari ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Nefertari:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Nefertari:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Nefertari ([number]/[number])
    - **Nefertari:** Thank you!
    - **Nefertari:** While you were off gathering [item], I remembered that my cart has a broken wheel, and I need to get it fixed before I can even begin to think abut making a delivery.
    - **Nefertari:** The wheelwright in the port district doesn't accept gold coins as payment, and I'll need to trade goods with her to get my wheel fixed.
    - **Player:** What do you need to trade her?
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2

- **Nefertari:** In order for me to get the wheelwright to fix my wheels, I often need to trade her a load of [item].
- **Player:** Right. Why [item]?
- (Condition: If the item desired is copper ore:)
  - **Nefertari:** I have no idea. Who am I to ask why a wheelwright needs rocks rich in copper?
  - (continue)
- (Condition: If the item desired is raw beltfish:)
  - **Nefertari:** I have no idea. Who am I to ask why a wheelwright needs a leathery fish, ready to be cooked?
  - (continue)
- **Nefertari:** If you could please fetch me [number] [item], then I will make sure to reimburse you for your time.
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Nefertari:** Thank you!
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Nefertari:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Nefertari:** Nevermind.
      - [Choice]: No.
        - **Nefertari:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Nefertari:** I'm hoping to get my wheel fixed sooner rather than later, Player. Do you have [number] [item]? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Nefertari:** I'm hoping to get my wheel fixed sooner rather than later, Player. Do you have [number] [item]? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Nefertari ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Nefertari:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Nefertari:** I'm hoping to get my wheel fixed sooner rather than later, Player. Do you have [number] [item]? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Nefertari ([number]/[number])
    - **Nefertari:** I am grateful. Helping me with the [item 1] and now some [item 2], I appreciate it.
    - **Nefertari:** It seems like my cart will meander through the sand for many more days to come.
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Nefertari:** Now all that is left is to get some supplies for the journey.
- **Player:** No kidding. What do you need?
  - (Condition: If the item desired is barberry seeds:)
    - **Nefertari:** I have everything I need except for seeds that grow into barberry bushes.
    - (continue)
  - (Condition: If the item desired is sharks:)
    - **Nefertari:** I have everything I need except for some nicely cooked sharks.
    - (continue)
- **Nefertari:** If you could please obtain [number] [item] for me, then I can be on my way.
- [Menu]: Select an option
  - [Choice]: Sure, fine, whatever.
    - **Nefertari:** Thank you!
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Nefertari:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Nefertari:** Nevermind.
      - [Choice]: No.
        - **Nefertari:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Nefertari:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Nefertari:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Nefertari ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Nefertari:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Nefertari:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Nefertari ([number]/[number])
    - **Nefertari:** I am grateful. The [item] are packed and ready to go, and now I have some [item] for the journey.
    - **Nefertari:** Thank you so much for helping me!
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - (above)

#### Friend's son slowly dying

- {{transcript missing}}

#### New product

- {{transcript missing}}

#### Slayer master

- {{transcript missing}}

#### War effort

- {{transcript missing}}
