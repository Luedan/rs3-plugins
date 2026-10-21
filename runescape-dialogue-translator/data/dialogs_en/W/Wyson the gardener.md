# Wyson the gardener

- **Original Wiki Page**: [Transcript:Wyson the gardener](https://runescape.wiki/w/Transcript%3AWyson%20the%20gardener)
- **Letter**: `W`

---

## Dialogue Transcript


### Talk to

- **Wyson the gardener:** I'm the head gardener around here.<br>If you're looking for woad leaves, or if you need help with anything, I'm your man.
- [Menu]: What would you like to talk about?
  - [Choice]: Ask about the unusual flower bed.
    - **Player:** What's up with the strange flower bed?
    - **Wyson the gardener:** Oh, the new lilies? Yes, we've just started...
    - **Player:** No, I meant the distorted plants whose exposed roots reach down into darkness unknowable.
    - **Wyson the gardener:** Ah.
    - **Wyson the gardener:** I was hoping it wasn't that noticeable.
    - **Wyson the gardener:** I just wanted to make sure Falador had the best park in Gielinor, but I got carried away with some of 'Malignius Mortifer's Super-Ultra-Flora-Growth potion'.
    - **Wyson the gardener:** To make matters worse, it's affected one of the local moles and she keeps ruining my flowerbeds.
    - **Player:** Is there anything I can do to help?
    - **Wyson the gardener:** Maybe someone could squeeze down there and deal with her.
    - **Wyson the gardener:** Could you do it? I can offer you some bird nests in exchange for any claws or hides you find.
    - [Menu]: Select an Option
      - [Choice]: Okay.
        - **Player:** Okay, I'll put a stop to it.
        - **Wyson the gardener:** Thank you, adventurer.
      - [Choice]: Why are you even collecting mole claws?
        - **Wyson the gardener:** The wife loves them.
        - [Menu]: Select an Option
          - [Choice]: ... Okay.
            - **Player:** Okay, I'll put a stop to it.
            - **Wyson the gardener:** Thank you, adventurer.
          - [Choice]: Leave
          - **Player:** Sorry, but I'm not interested.
          - **Wyson the gardener:** Fair enough.
      - [Choice]: Leave.
      - **Player:** Sorry, but I'm not interested.
      - **Wyson the gardener:** Fair enough.
  - [Choice]: Ask about trading for bird nests.
    - (below|exchange-mole-bits)
  - [Choice]: Ask about woad leaves.
    - **Player:** Yes please, I need woad leaves.
    - **Wyson the gardener:** How much are you willing to pay?
    - [Menu]: What would you like to say?
      - [Choice]: How about 5 coins?
        - **Player:** How about 5 coins?
        - **Wyson the gardener:** No no, that's far too little. Woad leaves are hard to get. I used to have plenty but someone kept stealing them off me.
      - [Choice]: How about 10 coins?
        - **Player:** How about 10 coins?
        - **Wyson the gardener:** No no, that's far too little. Woad leaves are hard to get. I used to have plenty but someone kept stealing them off me.
      - [Choice]: How about 15 coins?
        - **Player:** How about 15 coins?
        - **Wyson the gardener:** Mmmm... Okay, that sounds fair.
        - (removes=15 coins)
        - (receives=woad leaf)
        - **Player:** Thanks.
        - You buy a woad leaf from Wyson.
        - **Wyson the gardener:** I'll be around if you have any more gardening needs.
      - [Choice]: How about 20 coins?
        - **Player:** How about 20 coins?
        - **Wyson the gardener:** Ok that's more than fair.
        - **Wyson the gardener:** Here, have two. You're a generous person.
        - (removes=20 coins)
        - (receives=two woad leaves)
        - **Player:** Thanks.
        - Wyson gives you a pair of woad leaves.
      - [Choice]: Tell me your price.
        - **Player:** Tell me your price.
        - **Wyson the gardener:** Hmph. The art of haggling really is lost these days. Fine. 25 coins a piece.
        - {{AnchorText|How many would you like? (25 coins each)}}
        - ((After entering a positive amount:))
          - (removes=coins)
          - (receives=woad leaves)
          - **Player:** Thanks.
          - Wyson gives you a pair of woad leaves.
          - Wyson sells you: [number] x Woad leaf
  - [Choice]: Ask for advice for fighting the Giant Mole.
    - **Player:** Could you give me some advice for fighting the Giant Mole?
    - **Wyson the gardener:** Alright. I'll give you some tips while you're down there.
  - [Choice]: Leave.
    - **Player:** Sorry, but I'm not interested.
    - **Wyson the gardener:** Fair enough.

### {{Anchor|exchange-mole-bits}}Exchange mole bits


#### Without mole bits

- **Wyson the gardener:** If you get any mole claws, skins or noses from that giant beastie down there, I'll happily exchange them for some bird nests.
- **Player:** Okay, I'll come back if I find any.

#### With mole bits


##### On a free-to-play world

- You need to be on a members' world to use this feature.

##### On a members' world, without the Falador hard tasks complete

- **Wyson the gardener:** If I'm not mistaken, you've got some bits from a big mole there! I'll trade them for bird nests, if you like.
- [Menu]: Choose an option:
  - [Choice]: cond=If the player has mole claws|Yes, I will trade the mole claws.
    - **Player:** Yes, I will trade the mole claws.
    - (removes=all mole claws in backpack)
    - (receives=a noted bird nest for each mole claw)
  - [Choice]: cond=If the player has mole skin|Okay, I will trade the mole skin.
    - **Player:** Okay, I will trade the mole skin.
    - (removes=all mole skin in backpack)
    - (receives=a noted bird nest for each mole skin)
  - [Choice]: cond=If the player has mole nose|Can I trade the mole nose?
    - **Player:** Can I trade the mole nose?
    - (removes=all mole noses in backpack)
    - (receives=a noted bird nest for each mole nose)
  - [Choice]: cond=If the player has two types of mole bits|I'd like to trade both.
    - **Player:** I'd like to trade both.
    - (removes=all mole bits in backpack)
    - (receives=a noted bird nest for each mole claw, skin or nose)
  - [Choice]: cond=If the player has all three types of mole bits|I'd like to trade all three.
    - **Player:** I'd like to trade all three.
    - (removes=all mole bits in backpack)
    - (receives=a noted bird nest for each mole claw, skin or nose)
  - [Choice]: Actually, I've changed my mind.
    - (continuea|Talk to)

##### On a members' world, with the Falador hard tasks complete

- **Wyson the gardener:** If I'm not mistaken, you've got some mole bits there! I'll trade them for bird nests, if you like. I also see that you're a shield holder; a champion of Falador, eh? I'll throw some special seeds into the bargain.
- [Menu]: Choose an option:
  - [Choice]: cond=If the player has mole claws|Yes, I will trade the mole claws.
    - **Player:** Yes, I will trade the mole claws.
    - (removes=all mole claws in backpack)
    - (receives=a noted bird nest for each mole claw)
  - [Choice]: cond=If the player has mole skin|Okay, I will trade the mole skin.
    - **Player:** Okay, I will trade the mole skin.
    - (removes=all mole skin in backpack)
    - (receives=a noted bird nest and a white lily seed for each mole skin)
    - **Wyson the gardener:** If you don't plan on using those seeds, some of the other gardeners may be interested in them.
  - [Choice]: cond=If the player has mole nose|Can I trade the mole nose?
    - **Player:** Can I trade the mole nose?
    - (removes=all mole noses in backpack)
    - (receives=a noted bird nest for each mole nose)
  - [Choice]: cond=If the player has two types of mole bits|I'd like to trade both.
    - **Player:** I'd like to trade both.
    - (removes=all mole bits in backpack)
    - (receives=a noted bird nest for each mole claw, skin or nose, and a white lily seed for each mole skin)
    - (Condition: If white lily seeds were received:)
      - **Wyson the gardener:** If you don't plan on using those seeds, some of the other gardeners may be interested in them.
  - [Choice]: cond=If the player has all three types of mole bits|I'd like to trade all three.
    - **Player:** I'd like to trade all three.
    - (removes=all mole bits in backpack)
    - (receives=a noted bird nest for each mole claw, skin or nose, and a white lily seed for each mole skin)
    - (Condition: If white lily seeds were received:)
      - **Wyson the gardener:** If you don't plan on using those seeds, some of the other gardeners may be interested in them.
  - [Choice]: Actually, I've changed my mind.
    - (continuea|Talk to)

### Buy woad leaves

- (above|How many would you like? (25 coins each))
