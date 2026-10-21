# Kragen

- **Original Wiki Page**: [Transcript:Kragen](https://runescape.wiki/w/Transcript%3AKragen)
- **Letter**: `K`

---

## Dialogue Transcript


### Pay (North) or Pay (South)


#### With the allotment patch empty

- **Kragen:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.

#### With the crop growing


##### Without the required items

- **Kragen:** I want [number] [items] for that.
- **Player:** Thanks, maybe another time.

##### With the required items, without confirmation toggled off

- [Menu]: Pay [number] [items]?
  - [Choice]: Yes.
    - (removes=the requested items)
    - **Kragen:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
    - The gardener is now looking after the patch for you.
  - [Choice]: Yes, and don't ask again.
    - (above)
  - [Choice]: No.
    - (end)

##### With the required items, with confirmation toggled off

- (removes=the requested items)
- **Kragen:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
- The gardener is now looking after the patch for you.

##### Having already paid for protection

- **Kragen:** I don't know what you're talking about - I'm already looking after that patch for you.
- **Player:** Oh sorry, I forgot.

#### With the crop fully grown

- **Kragen:** That patch is already fully grown. I don't know what you want me to do with it.

### Talk to


#### Standard dialogue

- [Menu]: Choose an option:
  - [Choice]: Would you look after my crops for me?
    - **Player:** Would you look after my crops for me?
    - **Kragen:** I might. Which one were you thinking of?
    - [Menu]: Select an Option
      - [Choice]: The northern allotment.
        - (Condition: If the player has no crops in the patch:)
          - **Kragen:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.
        - (Condition: If the player has fully grown crops planted in the patch:)
          - **Kragen:** That patch is already fully grown! I don't know what you want me to do with it!
        - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
          - **Kragen:** I don't know what you're talking about - I'm already looking after that patch for you.
          - **Player:** Oh sorry, I forgot.
        - (Condition: If the crops in the patch are not yet fully grown:)
          - **Kragen:** If you like, but I want [number] [item] for that.
          - (Condition: If the player does not have the required items:)
            - **Player:** I'm afraid I don't have enough of those at the moment.
            - **Kragen:** Well, I'm not wasting my time for free.
          - (Condition: If the player has the required items:)
            - [Menu]: Select an Option
              - [Choice]: Okay, it's a deal.
                - **Player:** Okay, it's a deal.
                - (removes=the requested items)
                - **Kragen:** That'll do nicely, [Sir/Madam]. Leave it with me - I'll make sure it grows for you.
              - [Choice]: No, that's too much.
                - **Player:** No, that's too much.
                - **Kragen:** Well, I'm not wasting my time for free.
      - [Choice]: The southern allotment.
        - (above)
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Kragen}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|Can you stop weeding my farming patches please.
    - **Player:** Can you stop weeding my farming patches please.
    - **Kragen:** Sure, I'll stop weeding them now.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|Can you keep my farming patches weeded please?
    - **Player:** Can you keep my farming patches weeded please?
    - **Kragen:** That shouldn't be a problem, Martin said I should give you special attention for your help with the fairies! Be sure to clear your allotment though as I don't want to interupt their growth!
  - [Choice]: Can you sell me something?
    - **Player:** Can you sell me something?
    - **Kragen:** That depends on whether I have it to sell. What is it that you're looking for?
    - (opens=Farmer's Supplies)
  - [Choice]: That's all, thanks.
    - **Player:** That's all, thanks.

#### Historical sale dialogue prior to 18 July 2022

- **Player:** Can you sell me something?
- **Kragen:** That depends on whether I have it to sell. What is it that you're looking for?
- [Menu]: Select an Option
  - [Choice]: Some plant cure.
    - **Player:** Some plant cure.
    - **Kragen:** Plant cure, eh? I might have some put aside for myself. Tell you what, I'll sell you some plant cure for 25 gp if you like.
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
    - **Kragen:** A bucket of compost, eh? I might have one spare... tell you what, I'll sell it to you for 35 gp if you like.
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
    - **Kragen:** A rake, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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
        - **Kragen:** A watering can, eh? I might have one spare... tell you what, I'll sell it to you for 25 gp if you like.
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
        - **Kragen:** A gardening trowel, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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
        - **Kragen:** A seed dibber, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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

### Using items on Kragen


#### Showing Kragen an item that can make compost

- **Kragen:** That looks like something that you can make normal compost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of compost.

#### Showing Kragen an item that can make supercompost

- **Kragen:** That looks like something that you can make supercompost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of supercompost.
