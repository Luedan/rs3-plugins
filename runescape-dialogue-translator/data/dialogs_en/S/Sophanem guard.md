# Sophanem guard

- **Original Wiki Page**: [Transcript:Sophanem guard](https://runescape.wiki/w/Transcript%3ASophanem%20guard)
- **Letter**: `S`

---

## Dialogue Transcript


### Standard dialogue

- **Sophanem guard (male/female):** How can I help you?
- [Menu]: Select an Option
  - [Choice]: What are you doing down here?
    - **Player:** What are you doing down here?
    - **Sophanem guard (male/female):** We're guarding this place to make sure that nothing comes up from that trap door and that nobody unnecessarily goes down there.
    - [Menu]: Select an Option
      - [Choice]: What's down there?{{anchor|whats-down}}
        - **Player:** What's down there?
        - **Sophanem guard (male):** The nastiest creatures imaginable!
        - **Sophanem guard (female):** They seem to be a cross between humans and scarabs.
        - **Sophanem guard (male):** Rumour has it they may be connected to the ancient Sect of Scabaras!
        - **Player:** What do you know about this sect?
        - **Sophanem guard (female):** Little, aside from the odd fairy tale from childhood.
      - [Choice]: Why are you stopping people from going down there?{{anchor|why-stop}}
        - **Player:** Why are you stopping people from going down there?
        - **Sophanem guard (male):** Too many people have died down there for us not to take action.
        - **Sophanem guard (female):** There are fiendish traps and ghastly scarab monsters down there.
        - **Sophanem guard (male):** When we were first posted down here, we had a look down there and only just escaped with our lives.
        - **Player:** Gosh, that sounds quite scary. I might investigate this place in the future.
        - **Sophanem guard (male):** Sorry to be rude, but we really need to get back to guarding the door. The scarab beasts might come back at any time.
  - [Choice]: Do you have a tinderbox?
    - **Player:** Do you have a tinderbox?
    - **Sophanem guard (male/female):** I do, but I'd like to hold on to it for now.
    - **Player:** That's okay; I've one with me anyway.
  - [Choice]: Do you have a torch?
    - **Player:** Do you have a torch?
    - **Sophanem guard (male/female):** I'll sell you an unlit torch for 200gp.
    - [Menu]: Select an Option
      - [Choice]: I'll take it.
        - **Player:** I'll take it.
        - (Condition: If the player has no inventory space:)
          - **Player:** Oh dear; I don't seem to have enough room in my bags to carry it. I'll be back.
          - **Sophanem guard (male/female):** I'll be here when you get back.
        - (Condition: If the player has less than 200 coins:)
          - You can not afford that.
          - **Player:** I don't have enough money on me. I'll come back when I have enough.
        - (Condition: If the player has 200 coins:)
          - (removes=200 coins)
          - (receives=unlit torch)
          - [The guard hands you an unlit torch in exchange for 200gp.]
      - [Choice]: Sorry, that's too expensive.
        - **Player:** Sorry, that's too expensive.
        - **Sophanem guard (male/female):** No problem; come back if you change your mind.
  - [Choice]: How come you're not spotty?
    - **Player:** How come you're not spotty?
    - **Sophanem guard (male/female):** Oh, the plague of spots. Well, I wasn't here when the outbreak took place.
    - **Sophanem guard (male/female):** We were out of town trying to catch an antiques thief called Simon Templeton.
    - **Player:** Aren't you afraid that the plague is contagious?
    - **Sophanem guard (male/female):** Sophanem is my home town so it would take a lot more than the threat of a few spots to keep me away.
  - [Choice]: What is this place?
    - **Player:** What is this place?
    - (Condition: Before Contact!)
      - **Sophanem guard (male/female):** This is the remains of the Sophanem Bank.
      - **Player:** What happened to this place? It's all smashed up...
      - **Sophanem guard (male/female):** Some time back, these scarab creatures started coming up from the basement. We fought them off, but they kept coming and coming and eventually destroyed the place. We've now fought them back again and barricaded the trap door.
    - (Condition: After Contact!)
      - **Sophanem guard (male/female):** This is the recently renovated Sophanem Bank.
      - **Player:** Wow, this place is all fixed up.
      - **Sophanem guard (male/female):** Once all the townsfolk returned, we decided to patch the place up and return it to normal.
      - **Player:** Aren't you afraid that the scarabs will come back?
      - **Sophanem guard (male/female):** I suppose it is a worry, but ever since the townsfolk have returned the scarab attacks have become more sporadic and a lot less organised.
      - **Player:** True enough. There are also many adventurers passing through the dungeon now, which also has an effect.
      - **Sophanem guard (male/female):** That must be reducing the scarab numbers.

### Attempting to climb down the trapdoor


#### Before and during Contact!

- **Sophanem guard (female):** Halt! You may not go down there!
- **Player:** Why not?
- **Sophanem guard (male):** We're guarding the trapdoor, making sure nothing comes up or down!
- **Sophanem guard (female):** Besides, the way we have it set up, I doubt you'd be able to get that trapdoor open!
- **Player:** Oh really? I'd like to have a try.
- You attempt to open the trapdoor but fail.
- **Sophanem guard (male):** If you really want to go down there, you really should talk to Jex first.
- [Menu]: Select an Option
  - [Choice]: What's down there?
    - (above|whats-down)
  - [Choice]: Why are you stopping people from going down there?
    - (above|why-stop)
  - [Choice]: Thanks.
    - **Player:** Thanks.

#### After Contact!

- **Sophanem guard (female):** Be careful down there!
- You enter the trapdoor once more.
- {{qact|The player enters the maze level of the dungeon.}}
