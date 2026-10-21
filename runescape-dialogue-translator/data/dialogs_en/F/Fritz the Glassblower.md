# Fritz the Glassblower

- **Original Wiki Page**: [Transcript:Fritz the Glassblower](https://runescape.wiki/w/Transcript%3AFritz%20the%20Glassblower)
- **Letter**: `F`

---

## Dialogue Transcript


### Before learning about glassblowing

- **Fritz the Glassblower:** Hello adventurer, welcome to the Entrana furnace.
- **Fritz the Glassblower:** Would you like me to explain my craft to you?
- [Menu]: Select an Option
  - [Choice]: Yes please. I'd be fascinated to hear what you do.
    - **Player:** Yes please. I'd be fascinated to hear what you do.
    - **Fritz the Glassblower:** I'm extremely pleased to hear that! I've always wanted an apprentice. Let me talk you through the secrets of glassblowing.
    - {{anchor|glassblowing-tutorial}} **Fritz the Glassblower:** Glass is made from soda ash and silica. We get our soda ash by collecting seaweed from the rocks - the prevailing currents make the north-east and south-west corners of the island the best place to find it, it can also be found in
    - **Fritz the Glassblower:** your nets sometimes when you're fishing, on Karamja island or at the Piscatoris Fishing Colony in the nets there. To turn seaweed into soda ash, all you need to do is burn it on a fire. Feel free to use the range in my house for
    - **Fritz the Glassblower:** that; it's the one directly west of here. Next we collect sand from the sandpit that you'll also find just west of here, there are others located in Yanille and Shilo Village.
    - (Condition: If the player has not received an empty bucket from Fritz the Glassblower:)
      - (Condition: If the player has an empty bucket:)
        - **Fritz the Glassblower:** I see you already have a bucket that you can use for carrying it in.
        - (continue|bring-the-sand)
      - (Condition: If the player does not have an empty bucket:)
        - **Fritz the Glassblower:** You'll need a bucket to carry it in. Tell you what, you can have this old one of mine.
        - (receives=empty bucket)
        - (continue|bring-the-sand)
    - (Condition: If the player has already received an empty bucket from Fritz the Glassblower:)
      - **Fritz the Glassblower:** You can use the bucket I gave you earlier.
      - (Condition: If the player has an empty bucket:)
        - (continue|bring-the-sand)
      - (Condition: If the player does not have an empty bucket:)
        - **Player:** I'm afraid I don't have that bucket with me. Could you give me another one, please?
        - **Fritz the Glassblower:** Do I look like I'm made of buckets? You'll just have to buy another from a general store.
        - **Fritz the Glassblower:** And don't interrupt me when I'm speaking - it's rude. Anyway, as I was saying ...
        - (continue|bring-the-sand)
    - {{anchor|bring-the-sand}} **Fritz the Glassblower:** Bring the sand and the soda ash back here and melt them together in the furnace, and there you have it - molten glass!
    - **Fritz the Glassblower:** There are many things you can use the molten glass for once you have made it. Depending on how talented you are, you could try turning it into something, like a fishbowl, for example. If you'd like to try your hand at the
    - **Fritz the Glassblower:** fine art of glassblowing you can use my spare glassblowing pipe. I think I left it on the chest of drawers in my house this morning.
    - **Fritz the Glassblower:** Alternatively I am always happy to buy the molten glass from you, saves me running about making it for myself.
    - **Player:** That sounds good. How much will you pay me?
    - **Fritz the Glassblower:** Tell you what, because you've been interested in my art, I'll pay you the premium price of 20 gold pieces for each piece of molten glass you bring me.
  - [Choice]: No thanks, I doubt I'll ever turn my hand to glassblowing.
    - **Player:** No thanks, I doubt I'll ever turn my hand to glassblowing.
    - **Fritz the Glassblower:** Ok, suit yourself. Nobody seems to be interested in the skilled crafts these days.
    - **Fritz the Glassblower:** If you should change your mind, come back and talk to me.

### After learning about glassblowing

- **Fritz the Glassblower:** Ah Player, have you come to sell me some molten glass?
- [Menu]: Select an Option
  - [Choice]: Yes.
    - **Player:** Yes.
    - (Condition: If the player does not have molten glass:)
      - **Fritz the Glassblower:** Umm, not much point me trying to pay you for glass you don't have, is there?
      - **Player:** Well, actually, if you don't mind...
      - **Fritz the Glassblower:** I guess you've never heard of a rhetorical question then. I'll make it simple for you. You bring glass, me pay shiny gold coins.
    - (Condition: If the player has molten glass:)
      - **Fritz the Glassblower:** Fantastic! Let's see, for that much glass I could pay you ... ... <number> gold pieces!
      - [Menu]: Select an Option
        - [Choice]: Are you mad? I've run all over the island to make this glass.
          - **Player:** Are you mad? I've run all over the island to make this glass.
          - **Fritz the Glassblower:** Pity. Well you can find me here if you change your mind.
        - [Choice]: Sure, that sounds like a fair price.
          - **Player:** Sure, that sounds like a fair price.
          - **Fritz the Glassblower:** Here you are then.
          - (removes=molten glass)
          - (receives=20 coins)
          - **Fritz the Glassblower:** Thanks very much, Player. I'll buy any more that you bring.
  - [Choice]: No.
    - **Player:** No.
    - **Fritz the Glassblower:** Oh.
    - **Fritz the Glassblower:** ...errr, well should you get any I'm quite happy to pay for it. Remember, I'll pay you 20 gold pieces for each piece of molten glass you get for me.
    - **Fritz the Glassblower:** So what did you want to talk to me about then?
    - [Menu]: Select an Option
      - [Choice]: Could you tell me how to make molten glass again, please?
        - **Player:** Could you tell me how to make molten glass again, please?
        - **Fritz the Glassblower:** Well, I am very busy at the moment, but I guess I can take 5 minutes off for my favourite student.
        - (continuea|glassblowing-tutorial)
      - [Choice]: I just thought I'd drop in and say hello.
        - **Player:** I just thought I'd drop in and say hello.
        - **Fritz the Glassblower:** Hello then. I'm afraid I don't have any time to chat though. The druids of Taverley have placed a huge order for glass vials, so I'm very busy.
