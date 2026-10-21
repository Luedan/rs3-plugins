# Anhur

- **Original Wiki Page**: [Transcript:Anhur](https://runescape.wiki/w/Transcript%3AAnhur)
- **Letter**: `A`

---

## Dialogue Transcript


### Standard dialogue

- **Anhur:** Who on Gielinor are you?

### City quest dialogue

- **Anhur:** What do you want? Actually...if you're not doing anything, make yourself useful?
- {{tselect|Would you like to help?}}
  - {{topt|Yes.}}
    - **Anhur:** That will suffice.
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
    - **Anhur:** Nevermind.

#### Attacked by wildlife

- {{transcript missing}}

#### Awaiting delivery

- **Anhur:** I've been awaiting a delivery that contains some [item 1] and some [item 2]. I urgently need the [item 1], but folks on the pier say that there's no sign of the ship for miles.
- {{tcond|If the item desired is copper ore:}}
  - **Anhur:** Do you think you could get me [number]chunks of copper ore? I'm desperate for rocks rich in copper.
  - **Player:** Where could I find a chunk of copper ore?
  - **Anhur:** Copper ore can be found south-east of Varrock. Is that okay?
  - {{tact|continue}}
- {{tcond|If the item desired is barberry seeds:}}
  - **Anhur:** Do you think you could get me [number] barberry seeds? I'm desperate for seeds that grow into barberry bushes.
  - **Player:** Where could I find a barberry seed?
  - **Anhur:** Barberry seeds are often dropped by monsters, or they can be procured from master farmers around Gielinor. Is that okay?
  - {{tact|continue}}
- {{tcond|If the item desired is rosemary seeds:}}
  - **Anhur:** Do you think you could get me [number] rosemary seeds? I'm desperate for seeds that grow into rosemary plants.
  - **Player:** Where could I find a rosemary seed?
  - **Anhur:** Rosemary seeds are often dropped by monsters, or they can be procured from master farmers around Gielinor. Is that okay?
  - {{tact|continue}}
- {{tselect|Select an option}}
  - {{topt|Yes.}}
    - **Anhur:** That will suffice.
  - {{topt|No.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Anhur:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Anhur:** Nevermind.
      - {{topt|No.}}
        - **Anhur:** Nevermind.

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Do you have [number] [item]? It's fairly urgent. ([number] remaining)
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Do you have [number] [item]? It's fairly urgent. ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Anhur ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Anhur:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Do you have [number] [item]? It's fairly urgent. ([number] remaining)
    - **Player:** Yep! I have the [item].
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Anhur ([number]/[number])
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### Task #2


##### First time

- **Anhur:** Yes! Thank you.
- **Anhur:** Now that's done, we need the next block of supplies.

##### Afterwards

- **Anhur:** The next supplies I'm missing are a load of [item].
- **Player:** ...and they still haven't arrived yet?
- {{tcond|If the item desired is spirit kalphite pouches:}}
  - **Anhur:** Nope! All I need is instant kalphites, summonable from pouches and the ports workers tell me it will be days before I see them.
  - {{tact|continue}}
- {{tcond|If the item desired is fire battlestaves:}}
  - **Anhur:** Nope! All I need is a staff infused with fire magic and the ports workers tell me it will be days before I see them.
  - {{tact|continue}}
- {{tcond|If the item desired is potatoes:}}
  - **Anhur:** Nope! All I need is a starchy, tuberous crop and the ports workers tell me it will be days before I see them.
  - {{tact|continue}}
- **Anhur:** Could you get me some to tide me over for now? About [number] [item] should do.
- {{tselect|Select an option}}
  - {{topt|Sure thing.}}
    - **Anhur:** That will suffice.
  - {{topt|No, sorry.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Anhur:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Anhur:** Nevermind.
      - {{topt|No.}}
        - **Anhur:** Nevermind.

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Do you have [number] [item]? ([number] remaining)
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Do you have [number] [item]? ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Anhur ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Anhur:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Do you have [number] [item]? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Anhur ([number]/[number])
    - **Anhur:** Excellent. Saving the day with the [item 1] and now some [item 2], I appreciate your generosity.
    - {{tact|continue}}
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### Task #3

- **Anhur:** Seeing as you're so resourceful, I wonder if you could save me a trip around the city...
- **Player:** Go on…
- {{tcond|If the item desired is strips of cloth:}}
  - **Anhur:** I need some material for bandages to see the month through. Approximately [number] strips of cloth will save me a lot of hassle.
  - {{tact|continue}}
- {{tcond|If the item desired is dwarf weed seeds:}}
  - **Anhur:** I need a way to grow dwarf weed herb bushes to see the month through. Approximately [number] dwarf weed seeds will save me a lot of hassle.
  - {{tact|continue}}
- {{tcond|If the item desired is goat horns:}}
  - **Anhur:** I need potion supplies to see the month through. Approximately [number] goat horns will save me a lot of hassle.
  - {{tact|continue}}
- **Anhur:** Are [number] [item] too much to ask for? Will you find me some?
- {{tselect|Select an option}}
  - {{topt|Of course.}}
    - **Anhur:** That will suffice.
  - {{topt|It's too much.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Anhur:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Anhur:** Nevermind.
      - {{topt|No.}}
        - **Anhur:** Nevermind.

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - {{tcond|If the item desired is strips of cloth:}}
      - **Anhur:** Do you have [number] strips of cloth? You could make these at a loom. ([number] remaining)
    - {{tcond|If the item desired is dwarf weed seeds:}}
      - **Anhur:** Do you have [number] dwarf weed seeds? Dwarf weed seeds are often dropped by monsters, or they can be procured from master farmers around Gielinor. ([number] remaining)
    - {{tcond|If the item desired is goat horns:}}
      - **Anhur:** Do you have [number] goat horns? Goats can be found out around Nardah or west of the Kalphite Hive. ([number] remaining)
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - {{tcond|If the item desired is strips of cloth:}}
      - **Anhur:** Do you have [number] strips of cloth? You could make these at a loom. ([number] remaining)
      - {{tact|continue}}
    - {{tcond|If the item desired is dwarf weed seeds:}}
      - **Anhur:** Do you have [number] dwarf weed seeds? Dwarf weed seeds are often dropped by monsters, or they can be procured from master farmers around Gielinor. ([number] remaining)
      - {{tact|continue}}
    - {{tcond|If the item desired is goat horns:}}
      - **Anhur:** Do you have [number] goat horns? Goats can be found out around Nardah or west of the Kalphite Hive. ([number] remaining)
      - {{tact|continue}}
    - {{tact|removes=the requested items}}
    - Number of [item] given to Anhur ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Anhur:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - {{tcond|If the item desired is strips of cloth:}}
      - **Anhur:** Do you have [number] strips of cloth? You could make these at a loom. ([number] remaining)
      - {{tact|continue}}
    - {{tcond|If the item desired is dwarf weed seeds:}}
      - **Anhur:** Do you have [number] dwarf weed seeds? Dwarf weed seeds are often dropped by monsters, or they can be procured from master farmers around Gielinor. ([number] remaining)
      - {{tact|continue}}
    - {{tcond|If the item desired is goat horns:}}
      - **Anhur:** Do you have [number] goat horns? Goats can be found out around Nardah or west of the Kalphite Hive. ([number] remaining)
      - {{tact|continue}}
    - **Player:** Yes, I have the [item].
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Anhur ([number]/[number])
    - **Anhur:** Thank you so much for helping me!
    - {{tact|receives=a Menaphite gift offering and reputation in their chosen faction}}
    - A new Menaphos city quest is now available.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

#### Children can't sleep


##### Task #1

- **Anhur:** I am exhausted because my children are unable to sleep at night.
- **Player:** Oh, that's awful, how come they cannot sleep?
- **Anhur:** My oldest son is too afraid to sleep because of the [monster].
- **Anhur:** Would you be able to go and find some [monster] and thin their numbers?
- **Player:** Seems a little excessive... How many would I need to deal with?
- **Anhur:** Could you kill [number] [monster] for me?
- {{tselect|Select an option}}
  - {{topt|Yes.}}
    - **Anhur:** That will suffice.
    - **Player:** Where could I find [monster]?
    - {{tcond|If the monster assigned is Menaphite thugs:}}
      - **Anhur:** They were exiled. Rumour has it they've set themselves up in Pollnivneach. That's what I've heard.
    - {{tcond|If the monster assigned is mining camp guards:}}
      - **Anhur:** The mining camp is somewhere out in the desert to the north. That's what I've heard.
  - {{topt|No.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Anhur:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Anhur:** Nevermind.
      - {{topt|No.}}
        - **Anhur:** Nevermind.

##### Task incomplete

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Did you deal with the [number] [monster]? ([number] remaining)
    - **Player:** Not yet. Where could I find [monster] again?
    - {{tcond|If the monster assigned is Menaphite thugs:}}
      - **Anhur:** They were exiled. Rumour has it they've set themselves up in Pollnivneach.
    - {{tcond|If the monster assigned is mining camp guards:}}
      - **Anhur:** The mining camp is somewhere out in the desert to the north.
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task complete

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Did you deal with the [number] [monster]? ([number] remaining)
    - **Player:** Yeah, the [monster] won't be scaring your son again anytime soon.
    - {{tact|receives=Slayer experience}}
    - **Anhur:** Thank you. As excessive as it may have seemed, it was necessary!
    - **Anhur:** Now that he can sleep peacefully, let us talk about my daughter.
    - {{tact|continue}}
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Task #2

- **Anhur:** Ever since she was a little baby, she has been unable to sleep without [item].
- **Player:** Right. Why [item]?
- **Anhur:** Yes, I know it's a bit strange, but [item] were the only thing that would help her drift off.
- **Anhur:** So, please, if you could get [number] [item] I would greatly appreciate it.
- {{tselect|Select an option}}
  - {{topt|Alright.}}
    - **Anhur:** That will suffice.
    - **Player:** Do you know where I could get [item]?
    - {{tcond|If the item desired is copper ore:}}
      - **Anhur:** Copper ore can be found south-east of Varrock.
  - {{topt|No, sorry.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Anhur:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Anhur:** Nevermind.
      - {{topt|No.}}
        - **Anhur:** Nevermind.

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you found [number] [item] yet? ([number] remaining)
    - **Player:** Nope, where should I be looking for the [item]?
    - {{tact|continuea}}
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you found [number] [item] yet? ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Anhur ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Anhur:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you found [number] [item] yet? ([number] remaining)
    - **Player:** I have the [item].
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Anhur ([number]/[number])
    - **Anhur:** Excellent, my daughter will be able to sleep like a baby once again!
    - {{tact|continue}}
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### Task #3

- **Anhur:** Now, my youngest son, he recently lost his teddy bear.
- **Player:** You want me to find him a new teddy bear?
- **Anhur:** No, no. I may not look like it, but I am quite skilled in crafting. I plan to make him a new one if you could get me the materials.
- **Player:** What do you need?
- **Anhur:** I need [number] [item] to make it out of.
- **Player:** ...
- **Anhur:** ...
- **Anhur:** So, could you get [number] [item] for me?
- {{tselect|Select an option}}
  - {{topt|Sure.}}
    - **Anhur:** That will suffice.
    - **Player:** What do you know about [item]?
    - {{tcond|If the item desired is black candles:}}
      - **Anhur:** I hear there is a renowned candlemaker in Catherby.
  - {{topt|Nope.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{tselect|Are you sure you wish to abandon this city quest?}}
          - {{topt|Yes.}}
            - **Anhur:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - {{topt|No.}}
            - **Anhur:** Nevermind.
      - {{topt|No.}}
        - **Anhur:** Nevermind.

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Did you bring [number] [item]? This teddy bear won't build itself! ([number] remaining)
    - **Player:** Not yet. Could you point me in the direction of some [item]?
    - {{tact|continuea}}
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Did you bring [number] [item]? This teddy bear won't build itself! ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Anhur ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Anhur:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Did you bring [number] [item]? This teddy bear won't build itself! ([number] remaining)
    - **Player:** Yes, I have brought the [item].
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Anhur ([number]/[number])
    - **Player:** So how do you make a teddy bear from...
    - **Player:** No. I think it's better to not know.
    - **Anhur:** Excellent! I'll get right to work!
    - **Anhur:** So, my other son...
    - **Player:** Uh... Bye.
    - {{tact|receives=a Menaphite gift offering and reputation in their chosen faction}}
    - A new Menaphos city quest is now available.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

#### Collector of curiosities


##### Task #1

- **Anhur:** I am a collector of curiosities, and I currently have the greatest collection of [item] in all of Menaphos!
- **Anhur:** Well, I did...
- **Player:** What happened?
- **Anhur:** Another collector has arrived in the city and their collection is dwarfing mine.
- **Player:** How many more [item] do they have?
- **Anhur:** I've heard they have [number] more [item] than I do.
- **Player:** So, if someone were to bring you [number] [item], you would have the greatest collection again?
- **Anhur:** Yes! Would you do this for me?
- {{tselect|Select an option}}
  - {{topt|Okay, then.}}
    - **Anhur:** That will suffice.
    - **Player:** Where could I find [item]?
    - {{tcond|If the item desired is dragon bones:}}
      - **Anhur:** Kill some dragons and bring back their bones.
  - {{topt|No, sorry.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{transcript missing}}
      - {{topt|No.}}
        - **Anhur:** Nevermind.

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you got the [number] [item]? ([number] remaining)
    - **Player:** Not yet. Where could I find [item] again?
    - {{tact|above}}
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you got the [number] [item]? ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Anhur ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Anhur:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you got the [number] [item]? ([number] remaining)
    - **Player:** Yeah, got the [item]!
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Anhur ([number]/[number])
    - **Anhur:** Well, I guess this is a start...
    - **Player:** A start?
    - **Anhur:** I've just heard that my rival has just brought in new shipment of [item]...
    - {{tact|continue}}
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### Task #2

- **Anhur:** He heard that you brought me some [item 1], he now has [number] more [item 2] than I do, just to spite me.
- **Player:** What does that mean for you?
- **Anhur:** This is an arms race! You need to get me [number] more [item 2].
- **Player:** You collect [item 1] AND [item 2]?
- **Anhur:** I collect many things! I collect collections!
- **Player:** ...
- **Anhur:** So about those [number] more [item 2]...
- {{tselect|Select an option}}
  - {{topt|Fine, okay.}}
    - **Anhur:** That will suffice.
    - {{tcond|If the item desired is copper ore:}}
      - **Anhur:** Copper ore can be found south-east of Varrock.
  - {{topt|No, sorry.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{transcript missing}}
      - {{topt|No.}}
        - **Anhur:** Nevermind.

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you got [number] [item] yet? ([number] remaining)
    - **Player:** Nope, where can I find the [item] again?
    - {{tact|above}}
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you got [number] [item] yet? ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Anhur ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Anhur:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you got [number] [item] yet? ([number] remaining)
    - **Player:** I have the [item].
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Anhur ([number]/[number])
    - **Anhur:** Thank you so much.
    - **Player:** No problem.
    - {{tact|continue}}
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### Task #3

- **Anhur:** Could you perhaps do one more tiny job for me?
- **Player:** Does it involve [item 1] or [item 2]?
- **Anhur:** No, of course not!
- **Player:** Really?
- **Anhur:** ...
- **Anhur:** Yes I promise, I need [number] more [item] for my final collection!
- **Anhur:** This is the last time I ask. I promise.
- **Anhur:** [number] [item]?
- {{tselect|Select an option}}
  - {{topt|[number] [item]...}}
    - **Anhur:** You're a good person.
  - {{topt|Nope.}}
    - {{tselect|Would you like to abandon this city quest?}}
      - {{topt|Yes.}}
        - {{transcript missing}}
      - {{topt|No.}}
        - **Anhur:** Nevermind.

##### With no item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you got the [item]? I need [number]. ([number] remaining)
    - **Player:** Not yet. Could you point me in the direction of some [item]?
    - {{tcond|If the item desired is bolts of cloth:}}
      - **Anhur:** You could make these at a loom.
  - {{topt|Abandon this city quest.}}
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you got the [item]? I need [number]. ([number] remaining)
    - {{tact|removes=the requested items}}
    - Number of [item] given to Anhur ([number]/[number])
    - {{tcond|If the player gave only one of the item:}}
      - **Player:** Just one for now. Take it. I'll be back.
      - {{tact|continue}}
    - {{tcond|If the player had multiple of the item:}}
      - **Player:** I have some. Take them. I'll be back.
      - {{tact|continue}}
    - **Anhur:** Great. Thank you.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

##### With all of the item

- {{tselect|Select an option}}
  - {{topt|Talk about your current task.}}
    - **Anhur:** Have you got the [item 3]? I need [number]. ([number] remaining)
    - **Player:** Yes, but I'm not getting you any more [item 3], [item 1] OR [item 2] after this.
    - {{tact|removes=the requested items}} {{tact|receives=experience}}
    - Number of [item] given to Anhur ([number]/[number])
    - **Anhur:** Finally, I once again have the greatest collection of [item 3] in Menaphos!
    - **Player:** What do you plan to do with the [item 1], [item 2], and the [item 3] now that you have them?
    - **Anhur:** I really don't know.
    - **Player:** Well, then...
    - **Player:** Good luck with that.
    - {{tact|receives=a Menaphite gift offering and reputation in their chosen faction}}
    - A new Menaphos city quest is now available.
  - {{topt|Abandon this city quest.}}
    - {{tact|above}}

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

#### War effort

- {{transcript missing}}
