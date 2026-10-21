# Amaethwr

- **Original Wiki Page**: [Transcript:Amaethwr](https://runescape.wiki/w/Transcript%3AAmaethwr)
- **Letter**: `A`

---

## Dialogue Transcript


### Pay


#### With the fruit tree patch empty

- **Amaethwr:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.

#### With the fruit tree growing


##### Without the required items

- **Amaethwr:** I want [number] [items] for that.
- **Player:** Thanks, maybe another time.

##### With the required items, without confirmation toggled off

- [Menu]: Pay [number] [items]?
  - [Choice]: Yes.
    - (removes=the requested items)
    - **Amaethwr:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
    - The gardener is now looking after the patch for you.
  - [Choice]: Yes, and don't ask again.
    - (above)
  - [Choice]: No.
    - (end)

##### With the required items, with confirmation toggled off

- (removes=the requested items)
- **Amaethwr:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
- The gardener is now looking after the patch for you.

##### Having already paid for protection

- **Amaethwr:** I don't know what you're talking about - I'm already looking after that patch for you.
- **Player:** Oh sorry, I forgot.

#### With the fruit tree fully grown

- **Amaethwr:** That patch is already fully grown. I don't know what you want me to do with it.

### Talk to


#### Standard dialogue

- [Menu]: Choose an option:
  - [Choice]: Would you look after my crops for me?
    - **Player:** Would you look after my crops for me?
    - (Condition: If the player has no crops in the patch:)
      - **Amaethwr:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.
    - (Condition: If the player has fully grown crops planted in the patch:)
      - **Amaethwr:** That patch is already fully grown! I don't know what you want me to do with it!
    - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
      - **Amaethwr:** I don't know what you're talking about - I'm already looking after that patch for you.
      - **Player:** Oh sorry, I forgot.
    - (Condition: If the crops in the patch are not yet fully grown:)
      - **Amaethwr:** If you like, but I want [number] [item] for that.
      - (Condition: If the player does not have the required items:)
        - **Player:** I'm afraid I don't have enough of those at the moment.
        - **Amaethwr:** Well, I'm not wasting my time for free.
      - (Condition: If the player has the required items:)
        - [Menu]: Select an Option
          - [Choice]: Okay, it's a deal.
            - **Player:** Okay, it's a deal.
            - (removes=the requested items)
            - **Amaethwr:** That'll do nicely, [Sir/Madam]. Leave it with me - I'll make sure it grows for you.
          - [Choice]: No, that's too much.
            - **Player:** No, that's too much.
            - **Amaethwr:** Well, I'm not wasting my time for free.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Amaethwr}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|Can you stop weeding my farming patches please.
    - **Player:** Can you stop weeding my farming patches please.
    - **Amaethwr:** Sure, I'll stop weeding them now.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|Can you keep my farming patches weeded please?
    - **Player:** Can you keep my farming patches weeded please?
    - **Amaethwr:** That shouldn't be a problem, Martin said I should give you special attention for your help with the fairies! Be sure to clear your allotment though as I don't want to interupt their growth!
  - [Choice]: Can you sell me something?
    - **Player:** Can you sell me something?
    - **Amaethwr:** That depends on whether I have it to sell. What is it that you're looking for?
    - (opens=Farmer's Supplies)
  - [Choice]: That's all, thanks.
    - **Player:** That's all, thanks.

#### Historical sale dialogue prior to 18 July 2022

- **Player:** Can you sell me something?
- **Amaethwr:** That depends on whether I have it to sell. What is it that you're looking for?
- [Menu]: Select an Option
  - [Choice]: Some plant cure.
    - **Player:** Some plant cure.
    - **Amaethwr:** Plant cure, eh? I might have some put aside for myself. Tell you what, I'll sell you some plant cure for 25 gp if you like.
    - (Condition: If the player does not have enough money:)
      - **Player:**  I don't have enough money for that, I'm afraid.
    - (Condition: If the player has enough money:)
      - [Menu]: Select an Option
        - [Choice]: Yes, that sounds like a fair price.
          - **Player:** Yes, that sounds like a fair price.
          - (removes=25 coins) (receives=plant cure)
        - [Choice]: No thanks, I can get that much cheaper elsewhere.
          - **Player:** No thanks, I can get that much cheaper elsewhere.
  - [Choice]: A bucket of compost.
    - **Player:** A bucket of compost.
    - **Amaethwr:** A bucket of compost, eh? I might have one spare... tell you what, I'll sell it to you for 35 gp if you like.
    - (Condition: If the player does not have enough money:)
      - **Player:**  I don't have enough money for that, I'm afraid.
    - (Condition: If the player has enough money:)
      - [Menu]: Select an Option
        - [Choice]: Yes, that sounds like a fair price.
          - **Player:** Yes, that sounds like a fair price.
          - (removes=35 coins) (receives=compost)
        - [Choice]: No thanks, I can get that much cheaper elsewhere.
          - **Player:** No thanks, I can get that much cheaper elsewhere.
  - [Choice]: A rake.
    - **Player:** A rake.
    - **Amaethwr:** A rake, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
    - (Condition: If the player does not have enough money:)
      - **Player:**  I don't have enough money for that, I'm afraid.
    - (Condition: If the player has enough money:)
      - [Menu]: Select an Option
        - [Choice]: Yes, that sounds like a fair price.
          - **Player:** Yes, that sounds like a fair price.
          - (removes=15 coins) (receives=a rake)
        - [Choice]: No thanks, I can get that much cheaper elsewhere.
          - **Player:** No thanks, I can get that much cheaper elsewhere.
  - [Choice]: (See more items)
    - [Menu]: Select an Option
      - [Choice]: A watering can
        - **Player:** A watering can.
        - **Amaethwr:** A watering can, eh? I might have one spare... tell you what, I'll sell it to you for 25 gp if you like.
        - (Condition: If the player does not have enough money:)
          - **Player:**  I don't have enough money for that, I'm afraid.
        - (Condition: If the player has enough money:)
          - [Menu]: Select an Option
            - [Choice]: Yes, that sounds like a fair price.
              - **Player:** Yes, that sounds like a fair price.
              - (removes=25 coins) (receives=a watering can)
            - [Choice]: No thanks, I can get that much cheaper elsewhere.
              - **Player:** No thanks, I can get that much cheaper elsewhere.
      - [Choice]: A gardening trowel
        - **Player:** A gardening trowel.
        - **Amaethwr:** A gardening trowel, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
        - (Condition: If the player does not have enough money:)
          - **Player:**  I don't have enough money for that, I'm afraid.
        - (Condition: If the player has enough money:)
          - [Menu]: Select an Option
            - [Choice]: Yes, that sounds like a fair price.
              - **Player:** Yes, that sounds like a fair price.
              - (removes=15 coins) (receives=a gardening trowel)
            - [Choice]: No thanks, I can get that much cheaper elsewhere.
              - **Player:** No thanks, I can get that much cheaper elsewhere.
      - [Choice]: A seed dibber
        - **Player:** A seed dibber.
        - **Amaethwr:** A seed dibber, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
        - (Condition: If the player does not have enough money:)
          - **Player:**  I don't have enough money for that, I'm afraid.
        - (Condition: If the player has enough money:)
          - [Menu]: Select an Option
            - [Choice]: Yes, that sounds like a fair price.
              - **Player:** Yes, that sounds like a fair price.
              - (removes=15 coins) (receives=a seed dibber)
            - [Choice]: No thanks, I can get that much cheaper elsewhere.
              - **Player:** No thanks, I can get that much cheaper elsewhere.
      - [Choice]: (See previous items)
        - (previous)
  - [Choice]: Forget it.
    - **Player:** Forget it, you don't have anything I need.

### Using items on Amaethwr


#### Showing Amaethwr an item that can make compost

- **Amaethwr:**  That looks like something that you can make normal compost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of compost.

#### Showing Amaethwr an item that can make supercompost

- **Amaethwr:**  That looks like something that you can make supercompost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of supercompost.

### Treasure Trails

- {{tact|receives=lockbox (master)}}
- **Amaethwr:** Can you solve this for me?
- [Amaethwr has given you a lockbox!]

#### Talking to him with the unsolved lockbox in the backpack

- **Amaethwr:** Nope, that's not completed yet.

#### Talking to him with the unsolved lockbox in the bank

- **Player:** I left the puzzle scroll in the bank.
- **Amaethwr:** Well then, go and get it, so I can check you've done it.

#### Talking to him with the solved lockbox in the backpack

- **Amaethwr:** Excellent, here is your reward!
- (Condition: If the trail continues:)
  - (removes=the old clue scroll (master) and lockbox (master)) (receives=the new clue scroll (master))
  - [You've found another clue!]
- (Condition: If the trail ends:)
  - (removes=the old clue scroll (master) and lockbox (master)) (receives=reward casket (master))
  - [You've found a casket!]

### Manor Farm


#### Help


##### Before completing the request

- **What would you like to do?**
  - Ask about their request.
    - **Player:** What're you requesting today?
    - **Amaethwr:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **Amaethwr:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - **Amaethwr:** I'm also looking for a new animal, I'm currently after A [animal]
    - **Amaethwr:** If you complete this, I'll give you : Grenwall spikes x 20. I'm sure you'll gain some reputation with the farming guild too!
    - **Amaethwr:** You'll have to be quick though!, I'm only here for [number] hours and [number] minutes. To be exact.
  - Give them the items & animals for their request
    - ((Without the requested items:))
      - **Amaethwr:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **Amaethwr:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - **Amaethwr:** I'm also looking for a new animal, I'm currently after A [animal]
    - ((With the requested items:))
      - (removes=the requested items) (receives=20 Grenwall spikes and possibly a Brassica primer)
      - ((If a Brassica primer was rewarded:))
        - For completing this request you've received Brassica primer x 1.
        - ((Repeated in a pop-up:))
          - For completing this request you've received Brassica primer x 1.
          - (continue)
      - [You've received : Grenwall spikes x 20<br>And 2,750 farming reputation.]

##### After completing the request

- **Amaethwr:** Thank you for your help!
- A new request will be available in [time]..

#### Hand in easy request


##### Before completing the request


##### Without requested items

- **Amaethwr:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **Amaethwr:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- **Amaethwr:** I'm also looking for a new animal, I'm currently after A [animal]

##### With requested items

- (removes=the requested items) (receives=20 Grenwall spikes and possibly a Brassica primer)
- ((If a Brassica primer was rewarded:))
  - For completing this request you've received Brassica primer x 1.
  - ((Repeated in a pop-up:))
    - For completing this request you've received Brassica primer x 1.
    - (continue)
- [You've received : Grenwall spikes x 20<br>And 2,750 farming reputation.]

##### After completing the request

- You've already completed this request, there will be a new daily request in [time]..
