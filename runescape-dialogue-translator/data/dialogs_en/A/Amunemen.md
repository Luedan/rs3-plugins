# Amunemen

- **Original Wiki Page**: [Transcript:Amunemen](https://runescape.wiki/w/Transcript%3AAmunemen)
- **Letter**: `A`

---

## Dialogue Transcript

{{incomplete|Missing city quest dialogue.}}
{{transcript NPC|Amunemen}}

### Standard dialogue

- **Amunemen:** What we need is a visionary. Vision is scary. They could start a revolution, confuting the enclave, a rebel...

### City quest dialogue

- **Amunemen:** I'm beginning to feel like a lapdog, lapdog. Don't suppose you could help me out?
- {{tselect|Would you like to help?}}
  - {{topt|Yes.}}
    - **Amunemen:** I just want to thank you.
    - {{tcond|If the city quest type is "Attacked by wildlife":}}
      - {{tact|continue}}
    - {{tcond|If the city quest type is "Awaiting delivery":}}
      - {{tact|continue}}
    - {{tcond|If the city quest type is "Children can't sleep":}}
      - {{tact|continue}}
    - {{tcond|If the city quest type is "Collector of curiosities":}}
      - {{tact|continue}}
    - {{tcond|If the city quest type is "Crondis is angry":}}
      - {{tact|continue}}
    - {{tcond|If the city quest type is "Crop pests":}}
      - {{tact|continue}}
    - {{tcond|If the city quest type is "Delivery help":}}
      - {{tact|continue}}
    - {{tcond|If the city quest type is "Friend's son slowly dying":}}
      - {{tact|continue}}
    - {{tcond|If the city quest type is "New product":}}
      - {{tact|continue}}
    - {{tcond|If the city quest type is "Slayer master":}}
      - {{tact|continue}}
    - {{tcond|If the city quest type is "War effort":}}
      - {{tact|continue}}
  - {{topt|Not right now.}}
    - **Amunemen:** It's fine. Everything will just go up in smoke...

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


##### Task #1

- **Amunemen:** I've had a brilliant idea for a new product I can sell in the city. It is so brilliant that it would be a bad move to share with you what it is...yet.
- **Amunemen:** I could tell you if you helped me out by sourcing what I'll need to create my invention!
- **Amunemen:** What do you think? Could you please bring me [number] [item]?
- {{tselect|Select an option}}
  - {{topt|Sure thing.}}
    - **Amunemen:** I just want to thank you.
  - {{topt|No, sorry.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke...
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke...
      - {{topt|No.}}
        - **Amunemen:** It's fine. Everything will just go up in smoke...

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** How are you getting along with getting me [number] [item]? ([number] remaining)
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** How are you getting along with getting me [number] [item]? ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Amunemen ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Amunemen:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** How are you getting along with getting me [number] [item]? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Amunemen ([number]/[number])
    - **Amunemen:** Just the ticket!
    - **Amunemen:** Now I have the base items, I need to add a few more components to complete my product!
    - **Amunemen:** Let me see... Yes, yes, that's what I would need!
    - **Player:** What's that?
    - {{tact|continue}}
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### Task #2

- **Amunemen:** I would need...some [item].
- **Player:** Some [item]? But why?
- **Amunemen:** And reveal my trade secrets? No, Player, you won't get that knowledge out of me!
- **Amunemen:** Don't worry. If you get me [number] [item], then I will make sure to reimburse you for your time.
- {{tselect|Select an option}}
  - {{topt|Okay, then.}}
    - **Amunemen:** I just want to thank you.
  - {{topt|No, sorry.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke...
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke...
      - {{topt|No.}}
        - **Amunemen:** It's fine. Everything will just go up in smoke...

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:**How goes your quest of finding me [number] [item], Player? ([number] remaining)
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:**How goes your quest of finding me [number] [item], Player? ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Amunemen ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Amunemen:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** How goes your quest of finding me [number] [item], Player? ([number] remaining)
    - **Player:** There. Your [item].
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Amunemen ([number]/[number])
    - **Amunemen:** My project is nearing completion! You've been so helpful!
    - **Amunemen:** My invention is almost ready!
    - {{tact|continue}}
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### Task #3

- **Amunemen:** There is one more type of component I need to finish this amazing invention of mine!
- **Player:** Please do tell...
- **Amunemen:** It is none other than...[number] [item].
- **Amunemen:** If you do me this last favour, I will be rich! And you can reap the benefits, too!
- {{tselect|Select an option}}
  - {{topt|Sure, fine, whatever.}}
    - **Amunemen:** I just want to thank you.
  - {{topt|Nope.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke...
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke...
      - {{topt|No.}}
        - **Amunemen:** It's fine. Everything will just go up in smoke...

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** Ah, Player! Please tell me you have managed to acquire [number] [item]? ([number] remaining)
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** Ah, Player! Please tell me you have managed to acquire [number] [item]? ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Amunemen ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Amunemen:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** Ah, Player! Please tell me you have managed to acquire [number] [item]? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Amunemen ([number]/[number])
    - **Amunemen:** Brilliant! As brilliant as my invention, I must say! Time to put it together!
    - **Player:** So... What's that amazing invention you came up with, then?
    - **Amunemen:** Ah, the fruit of my hard labour, the apple of my eyes, my newest creation, the thing that will revolutionise the life of adventurers around the world...for which I have yet to come up with a good name for!
    - **Amunemen:** Wait, it's really not wise to talk to you about it until the prototype is fully working... I cannot risk having you steal my idea and getting it manufactured somewhere else for less.
    - **Player:** Thanks for the vote of confidence.
    - **Amunemen:** I hope I haven't offended you! Please, Player, accept this reward as token of my appreciation.
    - {{tact|receives=a Menaphite gift offering and reputation in their chosen faction}}
    - A new Menaphos city quest is now available.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

#### Slayer master

- {{transcript missing}}

#### War effort


##### Task #1

- **Amunemen:** I've been tasked to procure supplies for the war effort.
- **Player:** Who are we- Who are YOU at war with?
- **Amunemen:** All will be revealed. First up I need [number] [items]. Can I rely on you?
- {{tselect|Select an option}}
  - {{topt|Affirmative.}}
    - **Amunemen:** I just want to thank you.
  - {{topt|Negative.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke.
      - {{topt|No.}}
        - **Amunemen:** It's fine. Everything will just go up in smoke.

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Amunemen ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Amunemen:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** Do you have the [number] [item] at hand, soldier? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Amunemen ([number]/[number])
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### Task #2


##### First time

- **Amunemen:** Good work, soldier!
- **Amunemen:** Now that's done, we need the next block of supplies.

##### Afterwards

- **Amunemen:** The next supplies I require are a load of [item].
- **Player:** Right. Why [item]?
- **Amunemen:** Have you ever tried to fight a war without [item]? I didn't think so.
- **Amunemen:** The war effort requires [number] [item]. I assume I can trust you to obtain the [item]?
- {{tselect|Select an option}}
  - {{topt|You sure can.}}
    - **Amunemen:** I just want to thank you.
  - {{topt|No, sorry.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke.
      - {{topt|No.}}
        - **Amunemen:** It's fine. Everything will just go up in smoke.

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Amunemen ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Amunemen:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Amunemen:** Do you have the supplies, soldier? This war won't fund itself! We need [number] [item]! ([number] remaining)
    - **Player:** Yes, I have the [item].
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Amunemen ([number]/[number])
    - **Amunemen:** Great! Now we are ready to drive the offensive home!
    - **Player:** Can I ask why you're talking like this?
    - **Amunemen:** Whatever do you mean, soldier?
    - **Player:** You're talking like an imperial general. It's a bit off-putting.
    - **Amunemen:** ...
    - **Amunemen:** The guards are always watching. I have to keep up appearances.
    - **Player:** Right...fair enough. What else do...we...need for the war effort?
    - {{tact|continue}}
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### Task #3

- **Amunemen:** Now is the time you have been waiting for, soldier! The killing!
- **Amunemen:** We will finally vanquish our dreaded enemy, the [monster]!
- **Player:** What?
- **Amunemen:** Yes, kill [number] [monster] in the name of the Pharaoh himself!
- {{tselect|Select an option}}
  - {{topt|Okay.}}
    - **Amunemen:** I just want to thank you.
  - {{topt|Nope.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Amunemen:** It's fine. Everything will just go up in smoke.
      - {{topt|No.}}
        - **Amunemen:** It's fine. Everything will just go up in smoke.

##### Task incomplete

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - {{tcond|If the monster is kalphites:}}
      - **Amunemen:** Have you killed [number] kalphites? They're found inside Kalphite hives under the desert sands. We might win this war yet! ([number] remaining)
    - {{tcond|If the monster is plague frogs:}}
      - **Amunemen:** Have you killed [number] plague frogs? They're usually sliming around Sophanem. We might win this war yet! ([number] remaining)
    - {{tcond|If the monster is crocodiles:}}
      - **Amunemen:** Have you killed [number] crocodiles? Crocodiles are found roaming around the river to the north. We might win this war yet! ([number] remaining)
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - {{tcond|If the monster is kalphites:}}
      - **Amunemen:** Have you killed [number] kalphites? They're found inside Kalphite hives under the desert sands. We might win this war yet! ([number] remaining)
      - {{tact|continue}}
    - {{tcond|If the monster is plague frogs:}}
      - **Amunemen:** Have you killed [number] plague frogs? They're usually sliming around Sophanem. We might win this war yet! (0 remaining)
      - {{tact|continue}}
    - {{tcond|If the monster is crocodiles:}}
      - **Amunemen:** Have you killed [number] crocodiles? Crocodiles are found roaming around the river to the north. We might win this war yet! ([number] remaining)
      - {{tact|continue}}
    - **Player:** Yes, I have killed the [monster].
    - {{tact|receives=Slayer experience}}
    - **Amunemen:** Have you danced, as they say, in the blood of your enemies? Have you sent the souls of [number] [monster] to the Underworld?
    - **Amunemen:** Not that those [monster] have souls, I believe they are truly beyond help.
    - **Amunemen:** Thank you so much for helping me!
    - **Player:** I fear you still need a lot more help.
    - **Amunemen:** Sorry, what?
    - **Player:** Nothing. It was my pleasure.
    - {{tact|receives=a Menaphite gift offering and 2,000 reputation in their chosen faction}}
    - A new Menaphos city quest is now available.
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.
