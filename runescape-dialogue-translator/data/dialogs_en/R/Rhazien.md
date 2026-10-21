# Rhazien

- **Original Wiki Page**: [Transcript:Rhazien](https://runescape.wiki/w/Transcript%3ARhazien)
- **Letter**: `R`

---

## Dialogue Transcript


### Pay


#### With the bush patch empty

- **Rhazien:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.

#### With the bush growing


##### Without the required items

- **Rhazien:** I want [number] [items] for that.
- **Player:** Thanks, maybe another time.

##### With the required items, without confirmation toggled off

- [Menu]: Pay [number] [items]?
  - [Choice]: Yes.
    - (removes=the requested items)
    - **Rhazien:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
    - The gardener is now looking after the patch for you.
  - [Choice]: Yes, and don't ask again.
    - (above)
  - [Choice]: No.
    - (end)

##### With the required items, with confirmation toggled off

- (removes=the requested items)
- **Rhazien:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
- The gardener is now looking after the patch for you.

##### Having already paid for protection

- **Rhazien:** I don't know what you're talking about - I'm already looking after that patch for you.
- **Player:** Oh sorry, I forgot.

#### With the bush fully grown

- **Rhazien:** That patch is already fully grown. I don't know what you want me to do with it.

#### If the bush is a poison ivy bush

- **Rhazien:** There is no need for me to look after that poison ivy.
- **Player:** Really?
- **Rhazien:** Yes, poison ivy is pretty hardy stuff, and most animals will avoid eating it.
- **Rhazien:** Hence, there is no reason to worry about it.
- **Player:** Great.

### Talk to


#### Standard dialogue

- [Menu]: Choose an option:
  - [Choice]: Would you look after my crops for me?
    - **Player:** Would you look after my crops for me?
    - (Condition: If the player has no crops in the patch:)
      - **Rhazien:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.
    - (Condition: If the player has fully grown crops planted in the patch:)
      - **Rhazien:** That patch is already fully grown! I don't know what you want me to do with it!
    - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
      - **Rhazien:** I don't know what you're talking about - I'm already looking after that patch for you.
      - **Player:** Oh sorry, I forgot.
    - (Condition: If a poison ivy bush is growing:)
      - **Rhazien:** There is no need for me to look after that poison ivy.
      - **Player:** Really?
      - **Rhazien:** Yes, poison ivy is pretty hardy stuff, and most animals will avoid eating it.
      - **Rhazien:** Hence, there is no reason to worry about it.
      - **Player:** Great.
    - (Condition: If the crops in the patch are not yet fully grown:)
      - **Rhazien:** If you like, but I want [number] [item] for that.
      - (Condition: If the player does not have the required items:)
        - **Player:** I'm afraid I don't have enough of those at the moment.
        - **Rhazien:** Well, I'm not wasting my time for free.
      - (Condition: If the player has the required items:)
        - [Menu]: Select an Option
          - [Choice]: Okay, it's a deal.
            - **Player:** Okay, it's a deal.
            - (removes=the requested items)
            - **Rhazien:** That'll do nicely, [Sir/Madam]. Leave it with me - I'll make sure it grows for you.
          - [Choice]: No, that's too much.
            - **Player:** No, that's too much.
            - **Rhazien:** Well, I'm not wasting my time for free.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Rhazien}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|Can you stop weeding my farming patches please.
    - **Player:** Can you stop weeding my farming patches please.
    - **Rhazien:** Sure, I'll stop weeding them now.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|Can you keep my farming patches weeded please?
    - **Player:** Can you keep my farming patches weeded please?
    - **Rhazien:** That shouldn't be a problem, Martin said I should give you special attention for your help with the fairies! Be sure to clear your allotment though as I don't want to interupt their growth!
  - [Choice]: Can you sell me something?
    - **Player:** Can you sell me something?
    - **Rhazien:** That depends on whether I have it to sell. What is it that you're looking for?
    - (opens=Farmer's Supplies)
  - [Choice]: That's all, thanks.
    - **Player:** That's all, thanks.

#### Historical sale dialogue prior to 18 July 2022

- **Player:** Can you sell me something?
- **Rhazien:** That depends on whether I have it to sell. What is it that you're looking for?
- [Menu]: Select an Option
  - [Choice]: Some plant cure.
    - **Player:** Some plant cure.
    - **Rhazien:** Plant cure, eh? I might have some put aside for myself. Tell you what, I'll sell you some plant cure for 25 gp if you like.
    - (Condition: If the player does not have enough money:)
      - **Player:** I don't have enough money for that, I'm afraid.
    - (Condition: If the player has enough money:)
      - [Menu]: Select an Option
        - [Choice]: Yes, that sounds like a fair price.
          - **Player:** Yes, that sounds like a fair price.
          - (removes=25 coins) (receives=plant cure)
        - [Choice]: No thanks, I can get that much cheaper elsewhere.
          - **Player:** No thanks, I can get that much cheaper elsewhere.
  - [Choice]: A bucket of compost.
    - **Player:** A bucket of compost.
    - **Rhazien:** A bucket of compost, eh? I might have one spare... tell you what, I'll sell it to you for 35 gp if you like.
    - (Condition: If the player does not have enough money:)
      - **Player:** I don't have enough money for that, I'm afraid.
    - (Condition: If the player has enough money:)
      - [Menu]: Select an Option
        - [Choice]: Yes, that sounds like a fair price.
          - **Player:** Yes, that sounds like a fair price.
          - (removes=35 coins) (receives=compost)
        - [Choice]: No thanks, I can get that much cheaper elsewhere.
          - **Player:** No thanks, I can get that much cheaper elsewhere.
  - [Choice]: A rake.
    - **Player:** A rake.
    - **Rhazien:** A rake, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
    - (Condition: If the player does not have enough money:)
      - **Player:** I don't have enough money for that, I'm afraid.
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
        - **Rhazien:** A watering can, eh? I might have one spare... tell you what, I'll sell it to you for 25 gp if you like.
        - (Condition: If the player does not have enough money:)
          - **Player:** I don't have enough money for that, I'm afraid.
        - (Condition: If the player has enough money:)
          - [Menu]: Select an Option
            - [Choice]: Yes, that sounds like a fair price.
              - **Player:** Yes, that sounds like a fair price.
              - (removes=25 coins) (receives=a watering can)
            - [Choice]: No thanks, I can get that much cheaper elsewhere.
              - **Player:** No thanks, I can get that much cheaper elsewhere.
      - [Choice]: A gardening trowel
        - **Player:** A gardening trowel.
        - **Rhazien:** A gardening trowel, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
        - (Condition: If the player does not have enough money:)
          - **Player:** I don't have enough money for that, I'm afraid.
        - (Condition: If the player has enough money:)
          - [Menu]: Select an Option
            - [Choice]: Yes, that sounds like a fair price.
              - **Player:** Yes, that sounds like a fair price.
              - (removes=15 coins) (receives=a gardening trowel)
            - [Choice]: No thanks, I can get that much cheaper elsewhere.
              - **Player:** No thanks, I can get that much cheaper elsewhere.
      - [Choice]: A seed dibber
        - **Player:** A seed dibber.
        - **Rhazien:** A seed dibber, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
        - (Condition: If the player does not have enough money:)
          - **Player:** I don't have enough money for that, I'm afraid.
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

### Using items on Rhazien


#### Showing Rhazien an item that can make compost

- **Rhazien:** That looks like something that you can make normal compost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of compost.

#### Showing Rhazien an item that can make supercompost

- **Rhazien:** That looks like something that you can make supercompost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of supercompost.

### Manor Farm


#### Help


##### Before having completed the request

- [Menu]: What would you like to do?
  - [Choice]: Ask about their request.
    - **Player:** What're you requesting today?
    - **Rhazien:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **Rhazien:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - (Condition: With three requested animals:)
      - **Rhazien:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
      - (continue)
    - (Condition: With four requested animals:)
      - **Rhazien:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal]
      - (continue)
    - **Rhazien:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - **Rhazien:** If you complete this, I'll give you : A Rock-shell, Spined, or Skeletal armour piece x 1. I'm sure you'll gain some reputation with the farming guild too!
    - **Rhazien:** You'll have to be quick though!, I'm only here for [number] days, [number] hours and [number] minutes. To be exact.
  - [Choice]: Give them the items & animals for their request
    - ((Without the requested items:))
      - **Rhazien:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **Rhazien:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - (Condition: With two requested animals:)
        - **Rhazien:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal]
        - (continue)
      - (Condition: With three requested animals:)
        - **Rhazien:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
        - (continue)
      - **Rhazien:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - ((With the requested items:))
      - (removes=the requested items) (receives=the reward)
      - For completing this request you've received Brassica primer x 1.
      - ((Repeated in a pop-up:))
        - For completing this request you've received Brassica primer x 1.
        - (continue)
      - You've received : [Reward] x 1<br>And 5,500 Farming reputation.

##### After having completed the request

- **Rhazien:** Thank you for your help!
- A new request will be available in [time]{{Sic|..}}

#### Hand in medium request


##### Before having completed the request


##### Without requested items

- **Rhazien:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **Rhazien:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- (Condition: With three requested animals:)
  - **Rhazien:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
  - (continue)
- (Condition: With four requested animals:)
  - **Rhazien:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal]
  - (continue)
- **Rhazien:** I'm also looking for some produce, so I'll need : [Produce] x [number]

##### With requested items

- (Condition: With multiple applicable animals:)
  - [Menu]: Which animal would you like to hand in?
    - ((Repeated for each applicable animal:))
      - [Choice]: [Name]
        - (continue)
- (removes=the requested items) (receives=the reward)
- For completing this request you've received Brassica primer x 1.
- ((Repeated in a pop-up:))
  - For completing this request you've received Brassica primer x 1.
  - (continue)
- You've received : [Reward] x 1<br>And 5,500 farming reputation.

##### After having the request

- You've already completed this request, there will be a new tri-daily request in [time]{{Sic|..}}
