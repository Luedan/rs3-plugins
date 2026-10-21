# Jhonatan

- **Original Wiki Page**: [Transcript:Jhonatan](https://runescape.wiki/w/Transcript%3AJhonatan)
- **Letter**: `J`

---

## Dialogue Transcript

{{incomplete|city quest}}

### Standard dialogue

- **Jhonatan:** You are welcome in our home.

### Overhead dialogue

- {{trandom}}
  - (Condition: Dialogue 1)
    - **Jhonatan:** {{RSChat|I love you, my dear.}}
    - **Sabrina:** {{RSChat|I know, my sweet.}}
  - (Condition: Dialogue 2)
    - **Jhonatan:** {{RSChat|We should go see a show or something.}}
    - **Sabrina:** {{RSChat|There's a performer nearby, I already bought tickets.}}
    - **Jhonatan:** {{RSChat|Haha! Of course.}}

### City Quest

- **Jhonatan:** Greetings. Do you have a moment to spare? I need some help.
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Jhonatan:** My appreciation.
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


##### Task #1

- **Jhonatan:** I am exhausted because my children are unable to sleep at night.
- **Player:** Oh, that's awful, how come they cannot sleep?
- **Jhonatan:** My oldest son is too afraid to sleep because of the [monster].
- **Jhonatan:** Would you be able to go and find some [monster] and thin their numbers?
- **Player:** Seems a little excessive... How many would I need to deal with?
- **Jhonatan:** Could you kill [number] [monster] for me?
- [Menu]: Select an option
  - [Choice]: Yes.
    - **Jhonatan:** My appreciation.
    - **Player:** Where could I find [monster]?
    - (Condition: If the monster assigned is Menaphite thugs:)
      - **Jhonatan:** They were exiled. Rumour has it they've set themselves up in Pollnivneach. That's what I've heard.
    - (Condition: If the monster assigned is mining camp guards:)
      - **Jhonatan:** The mining camp is somewhere out in the desert to the north. That's what I've heard.
  - [Choice]: No.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Jhonatan:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Jhonatan:** Nevermind.
      - [Choice]: No.
        - **Jhonatan:** Nevermind.

##### Task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Did you deal with the [number] [monster]? ([number] remaining)
    - **Player:** Not yet. Where could I find [monster] again?
    - (Condition: If the monster assigned is Menaphite thugs:)
      - **Jhonatan:** They were exiled. Rumour has it they've set themselves up in Pollnivneach.
    - (Condition: If the monster assigned is mining camp guards:)
      - **Jhonatan:** The mining camp is somewhere out in the desert to the north.
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Did you deal with the [number] [monster]? ([number] remaining)
    - **Player:** Yeah, the [monster] won't be scaring your son again anytime soon.
    - (receives=Slayer experience)
    - **Jhonatan:** Thank you. As excessive as it may have seemed, it was necessary!
    - **Jhonatan:** Now that he can sleep peacefully, let us talk about my daughter.
    - (continue)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task #2

- **Jhonatan:** Ever since she was a little baby, she has been unable to sleep without [item].
- **Player:** Right. Why [item]?
- **Jhonatan:** Yes, I know it's a bit strange, but [item] were the only thing that would help her drift off.
- **Jhonatan:** So, please, if you could get [number] [item] I would greatly appreciate it.
- [Menu]: Select an option
  - [Choice]: Alright.
    - **Jhonatan:** My appreciation.
    - **Player:** Do you know where I could get [item]?
    - (Condition: If the item desired is copper ore:)
      - **Jhonatan:** Copper ore can be found south-east of Varrock.
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Jhonatan:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Jhonatan:** Nevermind.
      - [Choice]: No.
        - **Jhonatan:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Have you found [number] [item] yet? ([number] remaining)
    - **Player:** Nope, where should I be looking for the [item]?
    - (continuea)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Have you found [number] [item] yet? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Jhonatan ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Jhonatan:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Have you found [number] [item] yet? ([number] remaining)
    - **Player:** I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Jhonatan ([number]/[number])
    - **Jhonatan:** Excellent, my daughter will be able to sleep like a baby once again!
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Jhonatan:** Now, my youngest son, he recently lost his teddy bear.
- **Player:** You want me to find him a new teddy bear?
- **Jhonatan:** No, no. I may not look like it, but I am quite skilled in crafting. I plan to make him a new one if you could get me the materials.
- **Player:** What do you need?
- **Jhonatan:** I need [number] [item] to make it out of.
- **Player:** ...
- **Jhonatan:** ...
- **Jhonatan:** So, could you get [number] [item] for me?
- [Menu]: Select an option
  - [Choice]: Sure.
    - **Jhonatan:** My appreciation.
    - **Player:** What do you know about [item]?
    - (Condition: If the item desired is black candles:)
      - **Jhonatan:** I hear there is a renowned candlemaker in Catherby.
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Jhonatan:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Jhonatan:** Nevermind.
      - [Choice]: No.
        - **Jhonatan:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Did you bring [number] [item]? This teddy bear won't build itself! ([number] remaining)
    - **Player:** Not yet. Could you point me in the direction of some [item]?
    - (continuea)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Did you bring [number] [item]? This teddy bear won't build itself! ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Jhonatan ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Jhonatan:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Did you bring [number] [item]? This teddy bear won't build itself! ([number] remaining)
    - **Player:** Yes, I have brought the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Jhonatan ([number]/[number])
    - **Player:** So how do you make a teddy bear from...
    - **Player:** No. I think it's better to not know.
    - **Jhonatan:** Excellent! I'll get right to work!
    - **Jhonatan:** So, my other son...
    - **Player:** Uh... Bye.
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - (above)

#### Collector of curiosities

- {{transcript missing}}

#### Crondis is angry


##### Task #1

- **Jhonatan:** The magnificent Crondis has been angered by [monster]. She requires a blood sacrifice and a tribute.
- **Jhonatan:** First, go and kill [number] [monster].
- **Player:** What have the [monster] done to anger the almighty Crondis?
- **Jhonatan:** You don't need to know. Will you go to kill them?
- [Menu]: Select an option
  - [Choice]: Yes.
    - **Jhonatan:** My appreciation.
  - [Choice]: No.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - {{transcript missing}}
      - [Choice]: No.
        - **Jhonatan:** Nevermind.

##### Talking to him again with the slayer task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Have you vanquished the [number] [monster] for Lady Crondis? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

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

- **Jhonatan:** I've been tasked to procure supplies for the war effort.
- **Player:** Who are we- Who are YOU at war with?
- **Jhonatan:** All will be revealed. First up I need [number] [items]. Can I rely on you?
- [Menu]: Select an option
  - [Choice]: Affirmative.
    - **Jhonatan:** My appreciation.
  - [Choice]: Negative.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - {{transcript missing}}
      - [Choice]: No.
        - **Jhonatan:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Jhonatan ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Jhonatan:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Jhonatan ([number]/[number])
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2


##### First time

- **Jhonatan:** Good work, soldier!
- **Jhonatan:** Now that's done, we need the next block of supplies.

##### Afterwards

- **Jhonatan:** The next supplies I require are a load of [item].
- **Player:** Right. Why [item]?
- **Jhonatan:** Have you ever tried to fight a war without [item]? I didn't think so.
- **Jhonatan:** The war effort requires [number] [item]. I assume I can trust you to obtain the [item]?
- [Menu]: Select an option
  - [Choice]: You sure can.
    - **Jhonatan:** My appreciation.
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Jhonatan:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Jhonatan:** Nevermind.
      - [Choice]: No.
        - **Jhonatan:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Jhonatan ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Jhonatan:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Jhonatan:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Jhonatan ([number]/[number])
    - **Jhonatan:** Great! Now we are ready to drive the offensive home!
    - **Player:** Can I ask why you're talking like this?
    - **Jhonatan:** Whatever do you mean, soldier?
    - **Player:** You're talking like an imperial general. It's a bit off-putting.
    - **Jhonatan:** ...
    - **Jhonatan:** The guards are always watching. I have to keep up appearances.
    - **Player:** Right...fair enough. What else do...we...need for the war effort?
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Jhonatan:** Now is the time you have been waiting for, soldier! The killing!
- **Jhonatan:** We will finally vanquish our dreaded enemy, the [monster]!
- **Player:** What?
- **Jhonatan:** Yes, kill [number] [monster] in the name of the Pharaoh himself!
- [Menu]: Select an option
  - [Choice]: Okay.
    - **Jhonatan:** My appreciation.
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - {{transcript missing}}
      - [Choice]: No.
        - **Jhonatan:** Nevermind.

##### Task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - (Condition: If the monster is plague frogs:)
    - **Jhonatan:** Have you killed [number] [monster]? They're usually sliming around Sophanem. We might win this war yet! ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - (Condition: If the monster is plague frogs:)
      - **Jhonatan:** Have you killed [number] [monster]? They're usually sliming around Sophanem. We might win this war yet! (0 remaining)
      - (continue)
    - **Player:** Yes, I have killed the [monster].
    - (receives=Slayer experience)
    - **Jhonatan:** Have you danced, as they say, in the blood of your enemies? Have you sent the souls of [number] [monster] to the Underworld?
    - **Jhonatan:** Not that those [monster] have souls, I believe they are truly beyond help.
    - **Jhonatan:** Thank you so much for helping me!
    - **Player:** I fear you still need a lot more help.
    - **Jhonatan:** Sorry, what?
    - **Player:** Nothing. It was my pleasure.
    - {{qact|The quest is cleared.}}
    - (receives=a Menaphite gift offering and 2,000 reputation in their chosen faction)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.
