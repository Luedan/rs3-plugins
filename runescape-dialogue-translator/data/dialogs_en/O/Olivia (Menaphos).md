# Olivia (Menaphos)

- **Original Wiki Page**: [Transcript:Olivia (Menaphos)](https://runescape.wiki/w/Transcript%3AOlivia%20%28Menaphos%29)
- **Letter**: `O`

---

## Dialogue Transcript


### Standard dialogue

*When speaking to Olivia at the Ports District docks in Menaphos.*
- **Olivia:** I've been havin' a gander at the local wildlife, but them guards won't let me back in.

### City quest dialogue

- **Olivia:** Fancy meetin' you 'ere. Are you busy? I need a bit of 'elp.
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Olivia:** Cheers, love!
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
    - **Olivia:** Oh, well, maybe someone else will pop along.

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

- **Olivia:** The magnificent Crondis has been angered by [monster]. She requires a blood sacrifice and a tribute.
- **Olivia:** First, go and kill [number] [monster].
- **Player:** What have the [monster] done to anger the almighty Crondis?
- **Olivia:** You don't need to know. Will you go to kill them?
- [Menu]: Select an option
  - [Choice]: Yes.
    - **Olivia:** Cheers, love!
  - [Choice]: No.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Olivia:** Oh, well, maybe someone else will pop along.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Olivia:** Oh, well, maybe someone else will pop along.
      - [Choice]: No.
        - **Olivia:** Oh, well, maybe someone else will pop along.

##### Task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Have you vanquished the [number] [monster] for Lady Crondis? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Have you vanquished the [number] [monster] for Lady Crondis? ([number] remaining)
    - **Player:** Yes, I have slaughtered the [monster].
    - (receives=Slayer experience)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task #2


##### First time

- **Olivia:** Praise be to Crondis!
- **Olivia:** Now the pitiful wretches have paid for their transgressions, we require a burnt offering.

##### Afterwards

- **Olivia:** The next things I need are [item].
- **Player:** Right. Why [item]?
- **Olivia:** The first step towards appeasing Crondis is traditionally a burnt offering of [item].
- **Olivia:** So please go and get [number] [item].
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Olivia:** Cheers, love!
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Olivia:** Oh, well, maybe someone else will pop along.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Olivia:** Oh, well, maybe someone else will pop along.
      - [Choice]: No.
        - **Olivia:** Oh, well, maybe someone else will pop along.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Do you have the tribute for Crondis? She grows impatient. I need [number] [item]. ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Do you have the tribute for Crondis? She grows impatient. I need [number] [item]. ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Olivia ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Olivia:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Do you have the tribute for Crondis? She grows impatient. I need [number] [item]. ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Olivia ([number]/[number])
    - **Olivia:** May the great crocodile smile upon you!
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Olivia:** Finally, as per tradition, Crondis requires a liquid offering to be poured into the Elid.
- **Player:** A liquid offering?
- **Olivia:** Yes, gather [number] [item] for me and I will have workers liquidise them.
- [Menu]: Select an option
  - [Choice]: Sure.
    - **Olivia:** Cheers, love!
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Olivia:** Oh, well, maybe someone else will pop along.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Olivia:** Oh, well, maybe someone else will pop along.
      - [Choice]: No.
        - **Olivia:** Oh, well, maybe someone else will pop along.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Have you gathered the [number] [item]? We need to appease Crondis as soon as possible! ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Have you gathered the [number] [item]? We need to appease Crondis as soon as possible! ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Olivia ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Olivia:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Have you gathered the [number] [item]? We need to appease Crondis as soon as possible! ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Olivia ([number]/[number])
    - **Olivia:** Aren't you industrious! Good job.
    - **Olivia:** Thank you so much for helping me!
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


##### Task #1

- **Olivia:** I'm ready for a change in career.
- **Player:** Oh, really? How can I help?
- **Olivia:** Well, I really want to be a Slayer master, though I could do with some practice.
- **Player:** Alright, give it your best shot.
- **Olivia:** Greetings, adventurer! It is I, the Slayer master!
- **Olivia:** How was that?
- **Player:** Yeah, that was great, but you have to tell me what you want me to slay.
- **Olivia:** Oh, right!
- **Olivia:** Adventurer! I need you to slay...uh...
- **Olivia:** I need you to slay...[number]...[monster]?
- [Menu]: Select an option
  - [Choice]: I can do that.
    - **Olivia:** Cheers, love!
    - **Player:** Where could I find [monster]?
    - (Condition: If the monster assigned is Bandits:)
      - {{anchor|first}} **Olivia:** There's a large bandit camp north of here, past the quarry, I think.
  - [Choice]: No.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - {{transcript missing}}
      - [Choice]: No.
        - **Olivia:** Oh, well, maybe someone else will pop along.

##### Task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Did you slay the [number] [monster]? ([number] remaining)
    - **Player:** Not yet. Where could I find [monster] again?
    - (continuea|first)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Did you slay the [number] [monster]? (0 remaining)
    - **Player:** Yeah, the [monster] have been slain!
    - **Olivia:** Great job, adventurer!
    - **Olivia:** So what do I do now?
    - **Player:** Tell me what I need to slay next.
    - **Olivia:** Again? Okay!
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2

- **Olivia:** Adventurer! I need to you slay more things for me!
- **Player:** What must I slay for you, Slayer master?
- **Olivia:** I have decided that you must slay [number] [monster].
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Olivia:** Cheers, love!
    - **Player:** Where could I find [monster]?
    - (Condition: If the monster assigned is kalphites:)
      - {{anchor|first}} **Olivia:** They're found inside Kalphite hives under the desert sands. At least that's where I was told...
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - {{transcript missing}}
      - [Choice]: No.
        - **Olivia:** Oh, well, maybe someone else will pop along.

#### War effort


##### Task #1

- **Olivia:** I've been tasked to procure supplies for the war effort.
- **Player:** Who are we- Who are YOU at war with?
- **Olivia:** All will be revealed. First up I need [number] [items]. Can I rely on you?
- [Menu]: Select an option
  - [Choice]: Affirmative.
    - **Olivia:** Cheers, love!
  - [Choice]: Negative.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Olivia:** Oh, well, maybe someone else will pop along.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Olivia:** Oh, well, maybe someone else will pop along.
      - [Choice]: No.
        - **Olivia:** Oh, well, maybe someone else will pop along.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Olivia ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Olivia:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Olivia ([number]/[number])
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2


##### First time

- **Olivia:** Good work, soldier!
- **Olivia:** Now that's done, we need the next block of supplies.

##### Afterwards

- **Olivia:** The next supplies I require are a load of [item].
- **Player:** Right. Why [item]?
- **Olivia:** Have you ever tried to fight a war without [item]? I didn't think so.
- **Olivia:** The war effort requires [number] [item]. I assume I can trust you to obtain the [item]?
- [Menu]: Select an option
  - [Choice]: You sure can.
    - **Olivia:** Cheers, love!
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Olivia:** Oh, well, maybe someone else will pop along.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Olivia:** Oh, well, maybe someone else will pop along.
      - [Choice]: No.
        - **Olivia:** Oh, well, maybe someone else will pop along.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Olivia ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Olivia:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Olivia:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Olivia ([number]/[number])
    - **Olivia:** Great! Now we are ready to drive the offensive home!
    - **Player:** Can I ask why you're talking like this?
    - **Olivia:** Whatever do you mean, soldier?
    - **Player:** You're talking like an imperial general. It's a bit off-putting.
    - **Olivia:** ...
    - **Olivia:** The guards are always watching. I have to keep up appearances.
    - **Player:** Right...fair enough. What else do...we...need for the war effort?
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Olivia:** Now is the time you have been waiting for, soldier! The killing!
- **Olivia:** We will finally vanquish our dreaded enemy, the [monster]!
- **Player:** What?
- **Olivia:** Yes, kill [number] [monster] in the name of the Pharaoh himself!
- [Menu]: Select an option
  - [Choice]: Okay.
    - **Olivia:** Cheers, love!
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Olivia:** Oh, well, maybe someone else will pop along.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Olivia:** Oh, well, maybe someone else will pop along.
      - [Choice]: No.
        - **Olivia:** Oh, well, maybe someone else will pop along.

##### Task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - (Condition: If the monster is kalphites:)
      - **Olivia:** Have you killed [number] kalphites? They're found inside Kalphite hives under the desert sands. We might win this war yet! ([number] remaining)
    - (Condition: If the monster is plague frogs:)
      - **Olivia:** Have you killed [number] plague frogs? They're usually sliming around Sophanem. We might win this war yet! ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - (Condition: If the monster is kalphites:)
      - **Olivia:** Have you killed [number] kalphites? They're found inside Kalphite hives under the desert sands. We might win this war yet! ([number] remaining)
      - (continue)
    - (Condition: If the monster is plague frogs:)
      - **Olivia:** Have you killed [number] plague frogs? They're usually sliming around Sophanem. We might win this war yet! (0 remaining)
      - (continue)
    - **Player:** Yes, I have killed the [monster].
    - (receives=Slayer experience)
    - **Olivia:** Have you danced, as they say, in the blood of your enemies? Have you sent the souls of [number] [monster] to the Underworld?
    - **Olivia:** Not that those [monster] have souls, I believe they are truly beyond help.
    - **Olivia:** Thank you so much for helping me!
    - **Player:** I fear you still need a lot more help.
    - **Olivia:** Sorry, what?
    - **Player:** Nothing. It was my pleasure.
    - (receives=a Menaphite gift offering and 2,000 reputation in their chosen faction)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

### Overhead dialogue

*Olivia will occasionally produce overhead dialogue.*
- **Olivia:** {{RSChat|Blimey.|colour=yellow|shadow=yes}}
