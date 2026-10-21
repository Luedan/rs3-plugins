# Doric

- **Original Wiki Page**: [Transcript:Doric](https://runescape.wiki/w/Transcript%3ADoric)
- **Letter**: `D`

---

## Dialogue Transcript


### North of Falador


#### Before What's Mine is Yours


##### First time talking to Doric

- [What's Mine is Yours is fully voice-acted and features atmospheric music and effects. We suggest that you turn your sound on in order to get the most out of it.]
- **Doric:** It's over, it's over...
- **Player:** Are you okay? What's over?
- **Doric:** My business, my life...everything! It's all in ruins.
- **Player:** Calm down and tell me what's happened.
- **Doric:** Nurmof should have sent his pickaxe order through this week but I've heard nothing. He's been my most loyal customer for years, and he's not the only one to stop. I'm ruined!
- [Menu]: Select an Option
  - [Choice]: Don't worry, I'll help you.
    - (Condition: Without 5 Smithing:)
      - **Doric:** Perhaps you should get some more experience first. I'd love the help but I need someone who will be able to assist me if we're going to do this.
      - [This quest requires level 5 Smithing.]
    - (Condition: With 5 Smithing:)
      - (see|What's Mine is Yours)
  - [Choice]: I'm too busy to help right now.
    - **Doric:** Don't worry adventurer, you go about your business. I don't expect anyone to put themselves out for me.
    - **Doric:** Goodbye adventurer.
  - [Choice]: I wanted to use your anvil.
    - **Doric:** I got bigger problems than letting random adventurers use my anvil right now – if you help me, perhaps I could allow you to work with it then.
    - [Menu]: Select an Option
      - [Choice]: I'll help you.
        - (above|doric-accept-quest)
      - [Choice]: I'm too busy right now.
        - (above|doric-too-busy)
  - [Choice]: Do you have any advice for aspiring adventurers?
    - **Player:** Do you have any advice for aspiring adventurers?
    - **Doric:** Aye, I know about adventuring, young'un.
    - **Doric:** I fought the Kinshra alongside Kara-Meir, and I accompanied her to the dark lands of Morytania!
    - **Player:** Young'un?
    - **Doric:** You humans are all young to me.
    - **Player:** I suppose that's true. Tell me more about Kara-Meir and Falador.
    - **Doric:** Kara broke the back of the Kinshra's siege and challenged their leader. But the cost was high.
    - **Player:** What about Morytania?
    - **Doric:** That's a dark story. How could any of us have guessed the truth about Gar'rth?
    - **Player:** Tell me more!
    - **Doric:** No, not all adventures end well. Reldo, the Varrock librarian, might be willing to tell you more.

##### Talking to Doric again before accepting the quest

- **Doric:** Back again, adventurer? Unfortunately business isn't looking any better than last time we spoke.
- (continuea|starting)

#### After What's Mine is Yours

- **Doric:** Hello traveller, what brings you to my humble smithy?
- [Menu]: Choose an option:
  - [Choice]: Do you have any more Smithing tasks for me?
    - (see|Doric and Boric tasks)
  - [Choice]: cond=If either the Gofannon amulet, task list or wizard's diary has been lost|I lost an item you gave me.
    - (Condition: If only one item has been lost:)
      - (Condition: Without space in backpack:)
        - **Doric:** You don't have any space to hold it, though. Come back to me once you have room.
      - (Condition: With space in backpack:)
        - (receives=Gofannon amulet, task list or wizard's diary)
        - **Doric:** Thankfully, one of our workers found it. Be more careful next time.
      - (Condition: If two or more items have been lost:)
        - **Doric:** What item did you want back?
        - [Menu]: Choose an option:
          - [Choice]: Gofannon amulet
            - (above|careful)
          - [Choice]: Task list
            - (above|careful)
          - [Choice]: Wizard's diary
            - (above|careful)
  - [Choice]: How's the business doing?
    - (Condition: Up to Doric's Task III:)
      - **Doric:** Getting there. I'm really starting to imagine a new future now; one that I would never have been living had it not been for Boric.
      - (continue)
    - (Condition: After Doric's Task III and before Doric's Task VI:)
      - **Doric:** Well, at the moment, Boric can't stop grinning like a fool. That's a good thing, right?
      - (continue)
    - (Condition: After Doric's Task VI and before Doric's Task VIII:)
      - **Doric:** Our business has stretched out across the globe, we're receiving orders from all kinds of people, our future has never looked brighter.
      - (continue)
    - **Doric:** Was there anything else you wanted?
    - (initial)
  - [Choice]: I wanted to use your anvils.
    - **Doric:** Go right ahead. Least I can do after the help you gave me.
  - [Choice]: Do you have any advice for aspiring adventurers?
    - (above|doric-advice)

#### After Doric's Task VIII

- **Doric:** Hello traveller, what brings you to my humble smithy?
- [Menu]: Choose an option:
  - [Choice]: Do you have any more Smithing tasks for me?
    - **Doric:** Not at the moment, we have it all under control now. Thank you for all the assistance in helping us grow.
  - [Choice]: cond=If either the Gofannon amulet, monkey's note or wizard's diary has been lost|I lost an item you gave me.
    - (Condition: If only one item has been lost:)
      - (Condition: Without space in backpack:)
        - **Doric:** You don't have any space to hold it, though. Come back to me once you have room.
      - (Condition: With space in backpack:)
        - (receives=Gofannon amulet, monkey's note or wizard's diary)
        - **Doric:** Thankfully, one of our workers found it. Be more careful next time.
      - (Condition: If two or more items have been lost:)
        - **Doric:** What item did you want back?
        - [Menu]: Choose an option:
          - [Choice]: Gofannon amulet
            - (above|careful2)
          - [Choice]: Wizard's diary
            - (above|careful2)
          - [Choice]: Monkey's note
            - (above|careful2)
  - [Choice]: How's the business doing?
    - **Doric:** You wouldn't believe how well we're doing. It's all thanks to you giving me that one initial push. Was there anything else you wanted?
    - **Doric:** Was there anything else you wanted?
    - (initial)
  - [Choice]: I wanted to use your anvils.
    - **Doric:** Go right ahead. Least I can do after the help you gave me.
  - [Choice]: Do you have any advice for aspiring adventurers?
    - (above|doric-advice)
  - [Choice]: I have some information about that note.
    - **Player:** I'm not sure you'll believe this but there was just a pile of banana skins in its place.
    - **Doric:** You're kidding me.  What do you think monkeys would want with weapons?
    - **Player:** Maybe they're planning on invading.
    - **Doric:** Haha good one!
    - **Player:** I was being serious.  Those were some spooky greataxes I gave them.  How could monkeys even wield such huge weapons?
    - **Player:** They must be stronger than we think.  Who knows what havoc the monkeys could wreak?
    - **Player:** Have I doomed us all?
    - **Doric:** Stop, you're cracking me up!

#### Attempting to climb down the stairs in Doric's house (only before What's Mine is Yours)

- **Doric:** Get away from there! It's not safe to go down there.

#### Attempting to climb up the ladder in Doric's house

- **Doric:** Where do you think you're going?
- **Player:** I just wanted to see what was up here.
- **Doric:** This is my home! If I wanted you going up there, I would have invited you. Now please step away.
