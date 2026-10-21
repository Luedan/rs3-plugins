# Zahra (Menaphos)

- **Original Wiki Page**: [Transcript:Zahra (Menaphos)](https://runescape.wiki/w/Transcript%3AZahra%20%28Menaphos%29)
- **Letter**: `Z`

---

## Dialogue Transcript


### Before mining the big sandstone boulder


#### When talked to


##### First time

- **Player:** What are you doing over here?
- **Zahra:** The Pharaoh, along with a number of other benefactors, would like a cactus patch over in this corner.
- **Zahra:** Of course the location had to have a giant sandstone boulder sat on it...
- **Player:** Yeah...
- **Zahra:** Tell you what. If you construct the cactus patch for me, I'll let you use it to practice your farming skills.
- **Player:** Sounds fair. I could mine through that thing in no time at all.
- **Zahra:** Before I let you get started, Bring me 12 Acadia logs, and I'll work on a basic plot perimeter.
- **Player:** Only 12?
- **Zahra:** 12 Acadia logs is fine. I'm not crafting the Dominion Tower!

##### Afterwards


##### Without logs

- **Player:** Should we go ahead and make this cactus patch?
- **Zahra:** Before I let you get started, bring me 12 Acadia logs, and I'll work on a basic plot perimeter.
- **Player:** Only 12?
- **Zahra:** 12 Acadia logs is fine. I'm not crafting the Dominion Tower!

##### With logs

- **Player:** Should we go ahead and make this cactus patch?
- **Zahra:** I see you have 12 Acadia logs, give them to me and I'll work on a basic plot perimeter while you mine away that boulder.
- **Player:** Sure, no problem.
- **Zahra:** Good. I will fashion these into planks and pegs for the edge of the cactus patch. Go ahead and mine that...thing.

##### After handing the logs

- **Zahra:** Mine that boulder for me please.

#### Paying for protection

- **Zahra:** Sorry, I can't help you until I finish building this cactus patch...

#### Mining the sandstone boulder

- **Zahra:** Wait!
- **Zahra:** Hold on a second. We could make short work of this together.

### While mining the big sandstone boulder

- *(One of the following is seen randomly:)*
  - **Zahra:** I see it cracking more!
  - **Zahra:** Nicely done.
  - **Zahra:** That's a nice pickaxe you have there.
  - **Zahra:** Smashy, smashy.

### After mining the big sandstone boulder


#### First time

- **Zahra:** You have the strength and guile of Scabaras himself!
- **Zahra:** If you could break it down to even smaller pieces, that'd be great. Less like sandstone and more like...sand.

#### Afterwards

- **Zahra:** You're close to smashing up the sandstone boulder completely. It's almost rubble.

### While mining the broken down sandstone boulder

- *(One of the following is seen randomly:)*
  - **Zahra:** I see it cracking more!
  - **Zahra:** Smashy smashy.
  - **Zahra:** That's a nice pickaxe you have there.
  - **Zahra:** The pieces are almost small enough.

### After mining the broken down sandstone boulder


#### First time

- **Zahra:** Excellent work. Acadia wood isn't too great as a building material, but these basic planks will do for a farming patch.

#### Afterwards

- **Zahra:** I've placed the materials, could you construct the perimeter please?

### After constructing the planks

- **Zahra:** Oh you've done it already? Great! We make a good team.

### Standard dialogue


#### Pay


##### With the cactus patch empty

- **Zahra:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.

##### With the cactus growing


##### Without the required items

- **Zahra:** I want [number] [items] for that.
- **Player:** Thanks, maybe another time.

##### With the required items, without confirmation toggled off

- [Menu]: Pay [number] [items]?
  - [Choice]: Yes.
    - (removes=requested items)
    - **Zahra:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
    - The gardener is now looking after the patch for you.
  - [Choice]: Yes, and don't ask again.
    - (above)
  - [Choice]: No.
    - (end)

##### With the required items, with confirmation toggled off

- (removes=requested items)
- **Zahra:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
- The gardener is now looking after the patch for you.

##### Having already paid for protection

- **Zahra:** I don't know what you're talking about - I'm already looking after that patch for you.
- **Player:** Oh sorry, I forgot.

##### With the cactus fully grown

- **Zahra:** That patch is already fully grown. I don't know what you want me to do with it.

#### Talk to

- [Menu]: Choose an option:
  - [Choice]: Would you look after my crops for me?
    - **Player:** Would you look after my crops for me?
    - **Zahra:** For you? Not a problem.
    - (Condition: If the player has no crops in the patch:)
      - **Zahra:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.
    - (Condition: If the player has fully grown crops planted in the patch:)
      - **Zahra:** That patch is already fully grown! I don't know what you want me to do with it!
    - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
      - **Zahra:** I don't know what you're talking about - I'm already looking after that patch for you.
      - **Player:** Oh sorry, I forgot.
    - (Condition: If the crops in the patch are not yet fully grown:)
      - **Zahra:** If you like, but I want [number] [item] for that.
      - (Condition: If the player does not have the required items:)
        - **Player:** I'm afraid I don't have enough of those at the moment.
        - **Zahra:** Well, I'm not wasting my time for free.
      - (Condition: If the player has the required items:)
        - [Menu]: Select an Option
          - [Choice]: Okay, it's a deal.
            - **Player:** Okay, it's a deal.
            - (removes=requested items)
            - **Zahra:** That'll do nicely, [Sir/Madam]. Leave it with me - I'll make sure it grows for you.
          - [Choice]: No, that's too much.
            - **Player:** No, that's too much.
            - **Zahra:** Well, I'm not wasting my time for free.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Zahra}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|Can you stop weeding my farming patches please.
    - **Player:** Can you stop weeding my farming patches please.
    - **Zahra:** Sure, I'll stop weeding them now.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|Can you keep my farming patches weeded please?
    - **Player:** Can you keep my farming patches weeded please?
    - **Zahra:** That shouldn't be a problem, Martin said I should give you special attention for your help with the fairies! Be sure to clear your allotment though as I don't want to interupt their growth!
  - [Choice]: Can you sell me something?
    - **Player:** Can you sell me something?
    - **Zahra:** That depends on whether I have it to sell. What is it that you're looking for?
    - (opens=Farmer's Supplies)
  - [Choice]: That's all, thanks.
    - **Player:** That's all, thanks.

#### Historical sale dialogue prior to 18 July 2022

- **Player:** Can you sell me something?
- **Zahra:** That depends on whether I have it to sell. What is it that you're looking for?
- [Menu]: Select an Option
  - [Choice]: Some plant cure.
    - **Player:** Some plant cure.
    - **Zahra:** Plant cure, eh? I might have some put aside for myself. Tell you what, I'll sell you some plant cure for 25 gp if you like.
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
    - **Zahra:** A bucket of compost, eh? I might have one spare... tell you what, I'll sell it to you for 35 gp if you like.
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
    - **Zahra:** A rake, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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
        - **Zahra:** A watering can, eh? I might have one spare... tell you what, I'll sell it to you for 25 gp if you like.
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
        - **Zahra:** A gardening trowel, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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
        - **Zahra:** A seed dibber, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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

#### Using items on Zahra


##### Showing Zahra an item that can make compost

- **Zahra:**  That looks like something that you can make normal compost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of compost.

##### Showing Zahra an item that can make supercompost

- **Zahra:**  That looks like something that you can make supercompost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of supercompost.

### Manor Farm


#### Help


##### Before completing the request

- [Menu]: What would you like to do?
  - [Choice]: Ask about their request.
    - **Player:** What're you requesting today?
    - **Zahra:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **Zahra:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - (Condition: With 3 requested animals:)
      - **Zahra:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
      - (continue)
    - (Condition: With 4 requested animals:)
      - **Zahra:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal]
      - (continue)
    - **Zahra:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - **Zahra:** If you complete this, I'll give you : Menaphite gift offering (medium) x 1. I'm sure you'll gain some reputation with the farming guild too!
    - **Zahra:** You'll have to be quick though!, I'm only here for [number] days, [number] hours and [number] minutes. To be exact.
  - [Choice]: Give them the items & animals for their request
    - (Condition: Without the requested items:)
      - **Zahra:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **Zahra:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - (Condition: With 3 requested animals:)
        - **Zahra:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
        - (continue)
      - (Condition: With 4 requested animals:)
        - **Zahra:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal]
        - (continue)
      - **Zahra:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - (Condition: With the requested items:)
      - (removes=the requested items) (receives=Menaphite gift offering (medium) and Brassica primer)
      - For completing this request you've received Brassica primer x 1.
      - ((Repeated in a pop-up:))
        - For completing this request you've received Brassica primer x 1.
        - (continue)
      - [You've received : Menaphite gift offering (medium) x 1<br>And 5,500 farming reputation.]

##### After completing the request

- **Zahra:** Thank you for your help!
- A new request will be available in [time]{{Sic|..}}

#### Hand in medium request


##### Before completing the request


##### Without requested items

- **Zahra:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **Zahra:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- **Zahra:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal
- **Zahra:** I'm also looking for some produce, so I'll need : [Produce] x [number]

##### With requested items

- (Condition: With multiple applicable animals:)
  - [Menu]: Which animal would you like to hand in?
    - ((The following is repeated for each applicable animal:))
      - [Choice]: [Animal name]
        - (continue)
- (removes=the requested items) (receives=Menaphite gift offering (medium) and Brassica primer)
- For completing this request you've received Brassica primer x 1.
- ((Repeated in a pop-up:))
  - For completing this request you've received Brassica primer x 1.
  - (continue)
- [You've received : Menaphite gift offering (medium) x 1<br>And 5,500 farming reputation.]

##### After completing the request

- You've already completed this request, there will be a new bi-daily request in [time]{{Sic|..}}
