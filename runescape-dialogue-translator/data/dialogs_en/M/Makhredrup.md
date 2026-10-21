# Makhredrup

- **Original Wiki Page**: [Transcript:Makhredrup](https://runescape.wiki/w/Transcript%3AMakhredrup)
- **Letter**: `M`

---

## Dialogue Transcript


### Standard dialogue

- **Makhredrup:** Raja is a gentle giant. He is here by request of the pharaoh and I hope they do not keep him long. He is not used to such temperatures.

### City quest dialogue

- **Makhredrup:** Welcome, welcome. Do you have a moment to help me out?
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Makhredrup:** Yes! You're just the best.
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


##### Task #1

- (Condition: If the item desired is bones:)
  - **Makhredrup:** So, I have an acquaintance whom I regularly deliver bones to. They rely on me to make deliveries on a regular schedule.
  - **Makhredrup:** I have no idea why it is always bones that are requested. I'm not going to question why someone needs some regular old bones, dropped from creatures.
  - (continue)
- (Condition: If the item desired is fire battlestaves:)
  - **Makhredrup:** So, I have an acquaintance whom I regularly deliver fire battlestaves to. They rely on me to make deliveries on a regular schedule.
  - **Makhredrup:** I have no idea why it is always fire battlestaves that are requested. I'm not going to question why someone needs a staff infused with fire magic.
  - (continue)
- **Makhredrup:** Could you please bring me [number] [item]?
- [Menu]: Select an option
  - [Choice]: Okay, then.
    - **Makhredrup:** Yes! You're just the best.
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Makhredrup:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Makhredrup:** Nevermind.
      - [Choice]: No.
        - **Makhredrup:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Makhredrup:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Makhredrup:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Makhredrup ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Makhredrup:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Makhredrup:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Makhredrup ([number]/[number])
    - **Makhredrup:** Yes! You're just the best.
    - **Makhredrup:** While you were off gathering [item], I remembered that my cart has a broken wheel, and I need to get it fixed before I can even begin to think abut making a delivery.
    - **Makhredrup:** The wheelwright in the port district doesn't accept gold coins as payment, and I'll need to trade goods with her to get my wheel fixed.
    - **Player:** What do you need to trade her?
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2

- **Makhredrup:** In order for me to get the wheelwright to fix my wheels, I often need to trade her a load of [item].
- **Player:** Right. Why [item]?
- (Condition: If the item desired is copper ore:)
  - **Makhredrup:** I have no idea. Who am I to ask why a wheelwright needs rocks rich in copper?
  - (continue)
- (Condition: If the item desired is raw beltfish:)
  - **Makhredrup:** I have no idea. Who am I to ask why a wheelwright needs a leathery fish, ready to be cooked?
  - (continue)
- **Makhredrup:** If you could please fetch me [number] [item], then I will make sure to reimburse you for your time.
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Makhredrup:** Yes! You're just the best.
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Makhredrup:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Makhredrup:** Nevermind.
      - [Choice]: No.
        - **Makhredrup:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Makhredrup:** I'm hoping to get my wheel fixed sooner rather than later, Player. Do you have [number] [item]? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Makhredrup:** I'm hoping to get my wheel fixed sooner rather than later, Player. Do you have [number] [item]? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Makhredrup ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Makhredrup:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Makhredrup:** I'm hoping to get my wheel fixed sooner rather than later, Player. Do you have [number] [item]? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Makhredrup ([number]/[number])
    - **Makhredrup:** I am grateful. Helping me with the [item 1] and now some [item 2], I appreciate it.
    - **Makhredrup:** It seems like my cart will meander through the sand for many more days to come.
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Makhredrup:** Now all that is left is to get some supplies for the journey.
- **Player:** No kidding. What do you need?
  - (Condition: If the item desired is barberry seeds:)
    - **Makhredrup:** I have everything I need except for seeds that grow into barberry bushes.
    - (continue)
  - (Condition: If the item desired is sharks:)
    - **Makhredrup:** I have everything I need except for some nicely cooked sharks.
    - (continue)
- **Makhredrup:** If you could please obtain [number] [item] for me, then I can be on my way.
- [Menu]: Select an option
  - [Choice]: Sure, fine, whatever.
    - **Makhredrup:** Yes! You're just the best.
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Makhredrup:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Makhredrup:** Nevermind.
      - [Choice]: No.
        - **Makhredrup:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Makhredrup:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Makhredrup:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Makhredrup ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Makhredrup:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Makhredrup:** Do you have [number] [item]? I'm a bit pushed for time. ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Makhredrup ([number]/[number])
    - **Makhredrup:** I am grateful. The [item] are packed and ready to go, and now I have some [item] for the journey.
    - **Makhredrup:** Thank you so much for helping me!
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

### Overhead dialogue

*Makhredrup will occasionally produce overhead dialogue.*
- **Makhredrup:** {{RSChat|There, there. I know it's warm here, Raja.|colour=yellow|shadow=yes}}
