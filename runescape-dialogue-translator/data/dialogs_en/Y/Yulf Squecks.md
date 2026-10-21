# Yulf Squecks

- **Original Wiki Page**: [Transcript:Yulf Squecks](https://runescape.wiki/w/Transcript%3AYulf%20Squecks)
- **Letter**: `Y`

---

## Dialogue Transcript


### Pay


#### With the spirit tree patch empty

- **Yulf Squecks:** You don't have a sapling planted in that patch. Plant one and I might agree to look after it for you.

#### With the spirit tree growing


##### Without the required items

- **Yulf Squecks:** Alright, but it's not going to be cheap! I want [3/5] monkey nuts, a monkey bar and a ground-up Suqah tooth.
- **Player:** Thanks, maybe another time.

##### With the required items, without confirmation toggled off

- [Menu]: {{Tmissing|Exact message unknown - }}
  - [Choice]: Yes.
    - (removes=monkey nuts, monkey bar and ground tooth)
    - **Yulf Squecks:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
    - The gardener is now looking after the patch for you.
  - [Choice]: Yes, and don't ask again.
    - (above)
  - [Choice]: No.
    - (end)

##### With the required items, with confirmation toggled off

- (removes=monkey nuts, monkey bar and ground tooth)
- **Yulf Squecks:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
- The gardener is now looking after the patch for you.

##### Having already paid for protection

- **Yulf Squecks:** I don't know what you're talking about - I'm already looking after that patch for you.
- **Player:** Oh sorry, I forgot.

#### With the spirit tree fully grown

- **Yulf Squecks:** That patch is already fully grown. I don't know what you want me to do with it.

### Talk to


#### Standard dialogue

- [Menu]: Choose an option:
  - [Choice]: Would you look after my crops for me?
    - **Player:** Would you look after my crops for me?
    - (Condition: If the player has nothing planted in the patch:)
      - **Yulf Squecks:** You don't have a sapling planted in that patch. Plant something and I might agree to look after it for you.
    - (Condition: If the player has a fully grown spirit tree planted in the patch:)
      - **Yulf Squecks:** That patch is already fully grown! I don't know what you want me to do with it!
    - (Condition: If the spirit tree in the patch is not yet fully grown but the player has already paid the gardener:)
      - **Yulf Squecks:** I don't know what you're talking about - I'm already looking after that patch for you.
      - **Player:** Oh sorry, I forgot.
    - (Condition: If the spirit tree in the patch is not yet fully grown:)
      - **Frizzy:** First, I want [3/5] monkey nuts, a monkey bar and a ground up suqah tooth.
      - [Menu]: What would you like to say?
        - [Choice]: Where can I get all that stuff?
          - **Player:** Where can I get all that stuff?
          - **Yulf Squecks:** You can get a Suqah tooth from a Suqah's mouth, of course. Then you grind it up with a pestle and mortar. As for the monkey bar and nuts, try looking somewhere where there are lots of monkeys!
          - (other)
        - [Choice]: Alright, I'll pay.
          - **Player:** Alright, I'll pay.
          - (Condition: If the player does not have the required items:)
            - **Player:** I'm afraid I don't have enough of those at the moment.
            - **Yulf Squecks:** Well, I'm not wasting my time for free.
          - (Condition: If the player has the required items:)
            - (removes=monkey nuts, monkey bar and ground tooth)
            - **Yulf Squecks:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
        - [Choice]: What the heck do you want with THAT?
          - **Player:** What the heck do you want with THAT?
          - **Yulf Squecks:** They're for eating, silly! What else<br>can you do with a monkey bar?
          - **Player:** And the Suqah tooth?
          - **Yulf Squecks:** Lots of gnomes like a bit of ground-up Suqah tooth, just don't tell anyone about this, okay?
          - **Player:** Forget I asked.
        - [Choice]: Maybe some other time.
          - **Player:** Maybe some other time.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Yulf Squecks}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|Can you stop weeding my farming patches please.
    - **Player:** Can you stop weeding my farming patches please.
    - **Yulf Squecks:** Sure, I'll stop weeding them now.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|Can you keep my farming patches weeded please?
    - **Player:** Can you keep my farming patches weeded please?
    - **Yulf Squecks:** That shouldn't be a problem, Martin said I should give you special attention for your help with the fairies! Be sure to clear your allotment though as I don't want to interupt their growth!
  - [Choice]: Can you sell me something?
    - **Player:** Can you sell me something?
    - **Yulf Squecks:** That depends on whether I have it to sell. What is it that you're looking for?
    - (opens=Farmer's Supplies)
  - [Choice]: That's all, thanks.
    - **Player:** That's all, thanks.

#### Historical sale dialogue prior to 18 July 2022

- **Player:** Can you sell me something?
- **Yulf Squecks:** That depends on whether I have it to sell. What is it that you're looking for?
- [Menu]: Select an Option
  - [Choice]: Some plant cure.
    - **Player:** Some plant cure.
    - **Yulf Squecks:** Plant cure, eh? I might have some put aside for myself. Tell you what, I'll sell you some plant cure for 25 gp if you like.
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
    - **Yulf Squecks:** A bucket of compost, eh? I might have one spare... tell you what, I'll sell it to you for 35 gp if you like.
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
    - **Yulf Squecks:** A rake, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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
        - **Yulf Squecks:** A watering can, eh? I might have one spare... tell you what, I'll sell it to you for 25 gp if you like.
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
        - **Yulf Squecks:** A gardening trowel, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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
        - **Yulf Squecks:** A seed dibber, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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

### Using items on Yulf Squecks


#### Showing Yulf Squecks an item that can make compost

- **Yulf Squecks:**  That looks like something that you can make normal compost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of compost.

#### Showing Yulf Squecks an item that can make supercompost

- **Yulf Squecks:**  That looks like something that you can make supercompost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of supercompost.
