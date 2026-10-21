# Sennefer

- **Original Wiki Page**: [Transcript:Sennefer](https://runescape.wiki/w/Transcript%3ASennefer)
- **Letter**: `S`

---

## Dialogue Transcript

{{incomplete|city quest}}

### Standard dialogue

- **Sennefer:** I don't serve outsiders. Sorry.

### Overhead dialogue

- **Sennefer:** {{RSChat|I have wares at a reasonable price.}}

### City Quest

- **Sennefer:** What brings you here, adventurer? Will you assist me?
- [Menu]: Would you like to help?
  - [Choice]: Yes.
    - **Sennefer:** You've done well.
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


##### Task #1

- **Sennefer:** Those pesky [monster] are eating my crops!
- **Player:** Well, that is a problem. Anything I can do to help?
- **Sennefer:** Yes, I have a plan.
- **Sennefer:** I believe if we coat the crops with some sort of disgusting mixture it will deter them.
- **Player:** Yeah, that seems reasonable.
- **Sennefer:** First of all I need [number] of [item]. Could you get these for me?
- [Menu]: Select an option
  - [Choice]: Yes.
    - **Sennefer:** You’ve done well.
    - **Player:** Where could I find [item]?
    - (Condition: If the item assigned is a seed:)
      - {{anchor|first}} **Sennefer:** [Herb] seeds are often dropped by monsters, or they can be procured from master farmers across Gielinor. Hurry, though, before all my crops are gone.
  - [Choice]: No.
    - {{transcript missing}}

##### Talking to her again without the first item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** Have you got the [number] of [item]? ([number] remaining)
    - **Player:** Not yet. Where could I find [item] again?
    - (continuea|first)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Talking to her again with some of the first item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** Have you got the [number] of [item]? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Sennefer ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Sennefer:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### Talking to her again with all of the first item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** Have you got the [number] of [item]? ([number] remaining)
    - **Player:** Yeah, got the [item]!
    - (removes=the requested items) (receives= experience)
    - **Sennefer:** Excellent, the [item] will make a great base for the concoction!
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2

- **Sennefer:** Now, let’s think about what we will need next.
- **Sennefer:** What we need is fuel for the furnace.
- **Player:** How about [item]?
- **Sennefer:** Perfect! I think if you get me [number] of [item] we are good to go.
- [Menu]: Select an option
  - [Choice]: Alright.
    - **Sennefer:** You’ve done well.
    - **Player:** Do you know where I could get [item]?
    - (Condition: If the item requested is coal:)
      - {{anchor|second}} **Sennefer:** You can mine coal north of Al Kharid..
  - [Choice]: No, sorry.
    - {{transcript missing}}

##### Talking to her again without the second item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** Have you found [number] of [item] yet? ([number] remaining)
    - **Player:** Nope, where should I be looking for the [item]?
    - (continuea|second)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### Talking to her again with some of the second item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** Have you found [number] of [item] yet? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Sennefer ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Sennefer:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### Talking to her again with all of the second item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** Have you found [number] of [item] yet? ([number] remaining)
    - **Player:** I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Sennefer ([number]/[number])
    - **Sennefer:** Well, now we can finish our deterrent.
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Player:** Is something wrong?
- **Sennefer:** While you were gone, the [monster] came back and ate even more of my crops!.
- **Sennefer:** This deterrent is not going to be enough! I need you to send a message that nobody messes with my crops!
- **Player:** Uh… Well, we haven’t tried the det-
- **Sennefer:** Forget the deterrent! I need you to kill [number] of [monster] for me!
- [Menu]: Select an option
  - [Choice]: Sure.
    - **Player:** What do you know about [monster]?
    - (Condition: If the monster is desert lizards:)
      - {{anchor|third}} **Sennefer:** Other than the fact that they are crop-stealing fiends? They can be found out to the east in the desert.
  - [Choice]: Nope.
    - {{transcript missing}}

##### Talking to her again with the slayer task incomplete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** Did you deal with the [number] of [monster]? ([number] remaining)
    - **Player:** Not yet. Could you point me in the direction of some [monster]?
    - (continuea|third)
  - [Choice]: Abandon this city quest.
    - (above)

##### Talking to her again with the slayer task complete

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** Did you deal with the [number] of [monster]? (0 remaining)
    - **Player:** Yes, your crops should be safe now.
    - (receives= Slayer experience)
    - **Sennefer:** At last, my crops are safe!
    - **Sennefer:** So…
    - **Sennefer:** I don’t suppose you want to buy some [first item] and [second item]?
    - **Player:**No thanks.
    - (receives=Menaphite gift offering)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - (above)

#### Delivery help

- {{transcript missing}}

#### Friend's son slowly dying

- {{transcript missing}}

#### New product


##### Task #1

- **Sennefer:** I've had a brilliant idea for a new product I can sell in the city. It is so brilliant that it would be a bad move to share with you what it is...yet.
- **Sennefer:** I could tell you if you helped me out by sourcing what I'll need to create my invention!
- **Sennefer:** What do you think? Could you please bring me [number] [item]?
- [Menu]: Select an option
  - [Choice]: Sure thing.
    - **Sennefer:** You've done well.
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Sennefer:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Sennefer:** Nevermind.
      - [Choice]: No.
        - **Sennefer:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** How are you getting along with getting me [number] [item]? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** How are you getting along with getting me [number] [item]? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Sennefer ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Sennefer:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** How are you getting along with getting me [number] [item]? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Sennefer ([number]/[number])
    - **Sennefer:** Just the ticket!
    - **Sennefer:** Now I have the base items, I need to add a few more components to complete my product!
    - **Sennefer:** Let me see... Yes, yes, that's what I would need!
    - **Player:** What's that?
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #2

- **Sennefer:** I would need...some [item].
- **Player:** Some [item]? But why?
- **Sennefer:** And reveal my trade secrets? No, Player, you won't get that knowledge out of me!
- **Sennefer:** Don't worry. If you get me [number] [item], then I will make sure to reimburse you for your time.
- [Menu]: Select an option
  - [Choice]: Okay, then.
    - **Sennefer:** You've done well.
  - [Choice]: No, sorry.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Sennefer:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Sennefer:** Nevermind.
      - [Choice]: No.
        - **Sennefer:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:**How goes your quest of finding me [number] [item], Player? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:**How goes your quest of finding me [number] [item], Player? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Sennefer ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Sennefer:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** How goes your quest of finding me [number] [item], Player? ([number] remaining)
    - **Player:** There. Your [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Sennefer ([number]/[number])
    - **Sennefer:** My project is nearing completion! You've been so helpful!
    - **Sennefer:** My invention is almost ready!
    - (continue)
  - [Choice]: Abandon this city quest.
    - (above)

##### Task #3

- **Sennefer:** There is one more type of component I need to finish this amazing invention of mine!
- **Player:** Please do tell...
- **Sennefer:** It is none other than...[number] [item].
- **Sennefer:** If you do me this last favour, I will be rich! And you can reap the benefits, too!
- [Menu]: Select an option
  - [Choice]: Sure, fine, whatever.
    - **Sennefer:** You've done well.
  - [Choice]: Nope.
    - [Menu]: Would you like to abandon this city quest?
      - [Choice]: Yes.
        - [Menu]: Are you sure you wish to abandon this city quest?
          - [Choice]: Yes.
            - **Sennefer:** Nevermind.
            - {{qact|The quest is cleared.}}
            - A new Menaphos city quest is now available.
          - [Choice]: No.
            - **Sennefer:** Nevermind.
      - [Choice]: No.
        - **Sennefer:** Nevermind.

##### With no item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** Ah, Player! Please tell me you have managed to acquire [number] [item]? ([number] remaining)
  - [Choice]: Abandon this city quest.
    - {{qact|The quest is cleared.}}
    - A new Menaphos city quest is now available.

##### With some of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** Ah, Player! Please tell me you have managed to acquire [number] [item]? ([number] remaining)
    - (removes=the requested items)
    - Number of [item] given to Sennefer ([number]/[number])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Just one for now. Take it. I'll be back.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** I have some. Take them. I'll be back.
      - (continue)
    - **Sennefer:** Great. Thank you.
  - [Choice]: Abandon this city quest.
    - (above)

##### With all of the item

- [Menu]: Select an option
  - [Choice]: Talk about your current task.
    - **Sennefer:** Ah, Player! Please tell me you have managed to acquire [number] [item]? ([number] remaining)
    - **Player:** Yes, I have the [item].
    - (removes=the requested items) (receives=experience)
    - Number of [item] given to Sennefer ([number]/[number])
    - **Sennefer:** Brilliant! As brilliant as my invention, I must say! Time to put it together!
    - **Player:** So... What's that amazing invention you came up with, then?
    - **Sennefer:** Ah, the fruit of my hard labour, the apple of my eyes, my newest creation, the thing that will revolutionise the life of adventurers around the world...for which I have yet to come up with a good name for!
    - **Sennefer:** Wait, it's really not wise to talk to you about it until the prototype is fully working... I cannot risk having you steal my idea and getting it manufactured somewhere else for less.
    - **Player:** Thanks for the vote of confidence.
    - **Sennefer:** I hope I haven't offended you! Please, Player, accept this reward as token of my appreciation.
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - A new Menaphos city quest is now available.
  - [Choice]: Abandon this city quest.
    - (above)

#### Slayer master

- {{transcript missing}}

#### War effort

- {{transcript missing}}
