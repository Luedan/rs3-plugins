# Demetrius

- **Original Wiki Page**: [Transcript:Demetrius](https://runescape.wiki/w/Transcript%3ADemetrius)
- **Letter**: `D`

---

## Dialogue Transcript


### Pay (north) or pay (south)


#### With the allotment patch empty

- **Demetrius:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.

#### With the crop growing


##### Without the required items

- **Demetrius:** I want [number] [items] for that.
- **Player:** Thanks, maybe another time.

##### With the required items, without confirmation toggled off

- [Menu]: Pay [number] [items]?
  - [Choice]: Yes.
    - (removes=the requested items)
    - **Demetrius:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
    - The gardener is now looking after the patch for you.
  - [Choice]: Yes, and don't ask again.
    - (above)
  - [Choice]: No.
    - (end)

##### With the required items, with confirmation toggled off

- (removes=the requested items)
- **Demetrius:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
- The gardener is now looking after the patch for you.

##### Having already paid for protection

- **Demetrius:** I don't know what you're talking about - I'm already looking after that patch for you.
- **Player:** Oh sorry, I forgot.

#### With the crop fully grown

- **Demetrius:** That patch is already fully grown. I don't know what you want me to do with it.

### Talk to

- [Menu]: Choose an option:
  - [Choice]: Would you look after my crops for me?
    - **Player:** Would you look after my crops for me?
    - **Demetrius:** I might. Which one were you thinking of?
    - [Menu]: Select an Option
      - [Choice]: The northern allotment
        - **Player:** The northern allotment.
        - (above|Pay (north) or pay (south))
      - [Choice]: The southern allotment
        - **Player:** The southern allotment.
        - (above|Pay (north) or pay (south))
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Demetrius}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded:|Can you stop weeding my farming patches please.
    - **Player:** Can you stop weeding my farming patches please.
    - **Demetrius:** Sure, I'll stop weeding them now.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded:|Can you keep my farming patches weeded please?
    - **Player:** Can you keep my farming patches weeded please?
    - **Demetrius:** That shouldn't be a problem, Martin said I should give you special attention for your help with the fairies! Be sure to clear your allotment though as I don't want to interupt their growth!
  - [Choice]: Can you sell me something?
    - **Player:** Can you sell me something?
    - **Demetrius:** That depends on whether I have it to sell. What is it that you're looking for?
    - (opens=Farmer's Supplies)
  - [Choice]: That's all, thanks.
    - **Player:** That's all, thanks.

### Using items on Demetrius


#### Showing Demetrius an item that can make compost

- **Demetrius:** That looks like something that you can make normal compost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of compost.

#### Showing Demetrius an item that can make supercompost

- **Demetrius:** That looks like something that you can make supercompost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of supercompost.
