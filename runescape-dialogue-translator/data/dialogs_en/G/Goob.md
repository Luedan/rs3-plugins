# Goob

- **Original Wiki Page**: [Transcript:Goob](https://runescape.wiki/w/Transcript%3AGoob)
- **Letter**: `G`

---

## Dialogue Transcript


### Anachronia


#### Attempting to mine the boulder before talking to Goob

- **Goob:** Wait!
- **Goob:** I have plans for this big rock!

#### Talking to before starting mining


##### First time

- **Player:** What are you doing over here?
- **Goob:** Hello! I'm thinking about making a small garden here.
- **Goob:** This rock catches all the light from the sky! If we can say goodbye to the big rock, the ground here will make the perfect planting patch!
- **Player:** What do you want to plant?
- **Goob:** ...
- [The ancient zygomite furrows his brow, looks around slowly, and notices the huge cactus-like plant a short distance away.]
- **Goob:** Cactus!
- **Player:** What a surprise!
- **Player:** It has to be where the rock is?
- **Goob:** Yes.
- **Player:** Obviously.
- **Player:** I see. I could mine through that thing for you.
- **Goob:** Can you bring me some magic logs? I'll start making a patch perimeter and you can smash the rock! {{anchor|bringlogs}}
- (Condition: If the player does not have the magic logs:)
  - [Menu]: Select an Option
    - [Choice]: [Polite] I don't see why not.
      - **Goob:** Thank you!
      - (continue)
    - [Choice]: [Angry] You want me to provide the materials too!?
      - **Goob:** I'm not very good at gathering big wood bits myself. Sorry!
      - (continue)
    - [Choice]: [Sarcastic] Oh good, I love handing out my hard-earned items.
      - **Goob:** Glad to hear it!
      - (continue)
  - **Player:** Okay. How many magic logs do you need me to get?
  - **Goob:** 12 magic logs please! That will definitely be enough, I promise!
- (Condition: If the player already has the magic logs:)
  - **Player:** Sure, no problem!
  - (removes=12 magic logs)
  - **Goob:** You smash the rock, I'll craft the border.

##### 'Pay' option before helping

- **Goob:** Sorry, I can't help you until I finish building my little garden.

##### Talking to Goob afterwards without the magic logs

- **Player:** Should we go ahead and make this cactus patch?
- (continuea|bringlogs)

##### Talking to Goob afterwards with the magic logs

- **Player:** Should we go ahead and make this cactus patch?
- **Goob:** I can sense magic logs! Give them to me and I'll slice 'em up into planky-planks for the garden perimeter!
- **Player:** Sure, no problem!
- (removes=12 magic logs)
- **Goob:** You smash the rock, I'll craft the border.

##### Talking to Goob after giving the magic logs

- **Goob:** Can you smash the big rock for me please?

#### Mining the boulder

- *(One of the following is occasionally seen:)*
  - **Goob:** {{RSChat|Hooray! It's working!}}
  - **Goob:** {{RSChat|I see it cracking more!}}
  - **Goob:** {{RSChat|That's a nice rock breaker you have there.}}

#### Breaking the boulder into sandstone boulder

- **Goob:** You are really good at that!
- **Goob:** Let's smash it up into smaller bits and make it say goodbye!

#### Talking to once the boulder has been broken

- **Goob:** You're close to smashing up the big rock. I can sense it cracking apart.

#### Mining the sandstone boulder

- *(One of the following is occasionally seen:)*
  - **Goob:** {{RSChat|I'm making another magic plank now.}}
  - **Goob:** {{RSChat|Smashy smashy.}}
  - **Goob:** {{RSChat|The pieces are almost small enough.}}

#### Finishing mining

- **Goob:** Well done! I made some planks for the cactus garden.

#### Talking to once the sandstone boulder has been cleared

- **Goob:** I've placed the wood bits, could you build the patch perimeter please?

#### Finishing construction

- **Goob:** Oh you've done it already? Great! We make a good team.

#### Attempting to pay before building the patch

- **Goob:** Sorry, I can't help you until I finish building my little garden.

#### Attempting to pay after building the patch


##### With the cactus patch empty

- **Goob:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.

##### With the cactus growing


##### Without the required items

- **Goob:** I want [number] [items] for that.
- **Player:** Thanks, maybe another time.

##### With the required items, without confirmation toggled off

- [Menu]: Pay [number] [items]?
  - [Choice]: Yes.
    - (removes=requested items)
    - **Goob:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
    - The gardener is now looking after the patch for you.
  - [Choice]: Yes, and don't ask again.
    - (above)
  - [Choice]: No.
    - (end)

##### With the required items, with confirmation toggled off

- (removes=requested items)
- **Goob:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
- The gardener is now looking after the patch for you.

##### Having already paid for protection

- **Goob:** I don't know what you're talking about - I'm already looking after that patch for you.
- **Player:** Oh sorry, I forgot.

##### With the cactus fully grown

- **Goob:** That patch is already fully grown. I don't know what you want me to do with it.

#### Talking to after building the patch

- [Menu]: Choose an option:
  - [Choice]: Would you look after my crops for me?
    - **Player:** Would you look after my crops for me?
    - (Condition: If the player has no crops in the patch:)
      - **Goob:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.
    - (Condition: If the player has fully grown crops planted in the patch:)
      - **Goob:** That patch is already fully grown! I don't know what you want me to do with it!
    - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
      - **Goob:** I don't know what you're talking about - I'm already looking after that patch for you.
      - **Player:** Oh sorry, I forgot.
    - (Condition: If the crops in the patch are not yet fully grown:)
      - **Goob:** If you like, but I want [number] [item] for that.
      - (Condition: If the player does not have the required items:)
        - **Player:** I'm afraid I don't have enough of those at the moment.
        - **Goob:** Well, I'm not wasting my time for free.
      - (Condition: If the player has the required items:)
        - [Menu]: Select an Option
          - [Choice]: Okay, it's a deal.
            - **Player:** Okay, it's a deal.
            - (removes=requested items)
            - **Goob:** That'll do nicely, [Sir/Madam]. Leave it with me - I'll make sure it grows for you.
          - [Choice]: No, that's too much.
            - **Player:** No, that's too much.
            - **Goob:** Well, I'm not wasting my time for free.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Goob}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|Can you stop weeding my farming patches please.
    - **Player:** Can you stop weeding my farming patches please.
    - **Goob:** Sure, I'll stop weeding them now.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|Can you keep my farming patches weeded please?
    - **Player:** Can you keep my farming patches weeded please?
    - **Goob:** That shouldn't be a problem, Martin said I should give you special attention for your help with the fairies! Be sure to clear your allotment though as I don't want to interupt their growth!
  - [Choice]: Can you sell me something?
    - **Player:** Can you sell me something?
    - **Goob:** That depends on whether I have it to sell. What is it that you're looking for?
    - (opens=Farmer's Supplies)
  - [Choice]: That's all, thanks.
    - **Player:** That's all, thanks.

#### Showing Goob an item that can make compost

- **Goob:**  That looks like something that you can make normal compost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of compost.

#### Showing Goob an item that can make supercompost

- **Goob:**  That looks like something that you can make supercompost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of supercompost.

#### Historical sale dialogue prior to 18 July 2022

- **Player:** Can you sell me something?
- **Goob:** That depends on whether I have it to sell. What is it that you're looking for?
- [Menu]: Select an Option
  - [Choice]: Some plant cure.
    - **Player:** Some plant cure.
    - **Goob:** Plant cure, eh? I might have some put aside for myself. Tell you what, I'll sell you some plant cure for 25 gp if you like.
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
    - **Goob:** A bucket of compost, eh? I might have one spare... tell you what, I'll sell it to you for 35 gp if you like.
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
    - **Goob:** A rake, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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
        - **Goob:** A watering can, eh? I might have one spare... tell you what, I'll sell it to you for 25 gp if you like.
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
        - **Goob:** A gardening trowel, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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
        - **Goob:** A seed dibber, eh? I might have one spare... tell you what, I'll sell it to you for 15 gp if you like.
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

### Manor Farm


#### Help


##### Before completing the request

- [Menu]: What would you like to do?
  - [Choice]: Ask about their request.
    - **Player:** What're you requesting today?
    - **Goob:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **Goob:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - **Goob:** I'm also looking for a new animal, I'm currently after A [Animal]
    - **Goob:** If you complete this, I'll give you : Farming reputation boon (medium) x 1. I'm sure you'll gain some reputation with the farming guild too!
    - **Goob:** You'll have to be quick though!, I'm only here for [number] hours and [number] minutes. To be exact.
  - [Choice]: Give them the items & animals for their request
    - ((Without the requested items:))
      - **Goob:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **Goob:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - **Goob:** I'm also looking for a new animal, I'm currently after A [Animal]
    - ((With the requested items:))
      - (removes=the requested items) (receives=Farming reputation boon (medium) and possibly a Brassica primer)
      - ((If a Brassica primer was rewarded:))
        - For completing this request you've received Brassica primer x 1.
        - ((Repeated in a pop-up:))
          - For completing this request you've received Brassica primer x 1.
          - (continue)
      - [You've received : Farming reputation boon (medium) x 1 <br>And 2,750 farming reputation.]

##### After completing the request

- **Goob:** Thank you for your help!
- A new request will be available in [time]..

#### Hand in easy request


##### Before completing the request


##### Without requested items

- **Goob:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **Goob:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- **Goob:** I'm also looking for a new animal, I'm currently after A [Animal]

##### With requested items

- (removes=the requested items) (receives=Farming reputation boon (medium) and possibly a Brassica primer)
- ((If a Brassica primer was rewarded:))
  - For completing this request you've received Brassica primer x 1.
  - ((Repeated in a pop-up:))
    - For completing this request you've received Brassica primer x 1.
    - (continue)
- [You've received : Farming reputation boon (medium) x 1 <br>And 2,750 farming reputation.]

##### After completing the request

- You've already completed this request, there will be a new daily request in [time]..
