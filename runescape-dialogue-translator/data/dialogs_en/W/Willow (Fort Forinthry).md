# Willow (Fort Forinthry)

- **Original Wiki Page**: [Transcript:Willow (Fort Forinthry)](https://runescape.wiki/w/Transcript%3AWillow%20%28Fort%20Forinthry%29)
- **Letter**: `W`

---

## Dialogue Transcript


### Pay


#### With the tree patch empty

- **Willow:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.

#### With the tree growing


##### Without the required items

- **Willow:** I want [number] [items] for that.
- **Player:** Thanks, maybe another time.

##### With the required items, without confirmation toggled off

- [Menu]: Pay [number] [items]?
  - [Choice]: Yes.
    - (removes=requested items)
    - **Willow:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
    - The gardener is now looking after the patch for you.
  - [Choice]: Yes, and don't ask again.
    - (above)
  - [Choice]: No.
    - (end)

##### With the required items, with confirmation toggled off

- (removes=requested items)
- **Willow:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
- The gardener is now looking after the patch for you.

##### Having already paid for protection

- **Willow:** I don't know what you're talking about - I'm already looking after that patch for you.
- **Player:** Oh sorry, I forgot.

#### With the tree fully grown


##### Before having checked its health

- **Willow:** I think you should claim the XP from that patch before having it chopped down.

##### After having checked its health, without confirmation toggled off

- [Menu]: Pay 200 gp to have the tree chopped down?
  - [Choice]: Yes, get rid of the tree.
    - ((Without 200 coins:))
      - **Willow:** I'll want 200 gp for chopping down that tree.
      - You can not afford that.
    - ((With 200 coins:))
      - (removes=200 coins)
      - {{Qact|The patch is cleared.}}
      - The gardener obligingly removes your tree.
  - [Choice]: Yes, and don't ask again.
    - (above)
  - [Choice]: No thanks.
    - (end)

##### After having checked its health, with confirmation toggled off

- ((Without 200 coins:))
  - **Willow:** I'll want 200 gp for chopping down that tree.
  - You can not afford that.
- ((With 200 coins:))
  - (removes=200 coins)
  - {{Qact|The patch is cleared.}}
  - The gardener obligingly removes your tree.

### Talk to

- [Menu]: Choose an option:
  - [Choice]: cond=If the tree is fully grown|Would you chop my tree down for me?
    - **Player:** Would you chop my tree down for me?
    - **Willow:** You look like you could chop it down yourself. I can chop the tree down for you if you like, but I'll want 200 gp to make it worth my while.
    - [Menu]: Select an Option
      - [Choice]: 200 gp? I'll do it myself.
        - **Player:** 200 gp? I'll do it myself.
      - [Choice]: Okay, go ahead.
        - ((Without 200 coins:))
          - **Player:** I don't have 200 gp I'm afraid.
          - You can not afford that.
        - ((With 200 coins:))
          - (removes=200 coins)
          - **Player:** Okay, go ahead.
          - {{Qact|The patch is cleared.}}
          - The gardener obligingly removes your tree.
  - [Choice]: cond=If the tree isn't fully grown|Would you look after my crops for me?
    - **Player:** Would you look after my crops for me?
    - (Condition: If the player has nothing planted in the patch:)
      - **Willow:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.
    - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
      - **Willow:** I don't know what you're talking about - I'm already looking after that patch for you.
      - **Player:** Oh sorry, I forgot.
    - (Condition: If the crops in the patch are not yet fully grown:)
      - **Willow:** If you like, but I want [number] [item] for that.
      - (Condition: If the player does not have the required items:)
        - **Player:** I'm afraid I don't have enough of those at the moment.
        - **Willow:** Well, I'm not wasting my time for free.
      - (Condition: If the player has the required items:)
        - [Menu]: Select an Option
          - [Choice]: Okay, it's a deal.
            - **Player:** Okay, it's a deal.
            - (removes=requested items)
            - **Willow:** That'll do nicely, [Sir/Madam]. Leave it with me - I'll make sure it grows for you.
          - [Choice]: No, that's too much.
            - **Player:** No, that's too much.
            - **Willow:** Well, I'm not wasting my time for free.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Willow}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|Can you stop weeding my farming patches please.
    - **Player:** Can you stop weeding my farming patches please.
    - **Willow:** Sure, I'll stop weeding them now.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|Can you keep my farming patches weeded please?
    - **Player:** Can you keep my farming patches weeded please?
    - **Willow:** That shouldn't be a problem, Martin said I should give you special attention for your help with the fairies! Be sure to clear your allotment though as I don't want to interupt their growth!
  - [Choice]: Can you sell me something?
    - **Player:** Can you sell me something?
    - **Willow:** That depends on whether I have it to sell. What is it that you're looking for?
    - (opens=Farmer's Supplies)
  - [Choice]: That's all, thanks.
    - **Player:** That's all, thanks.

### Using items on Willow


#### Showing Willow an item that can make compost

- **Willow:**  That looks like something that you can make normal compost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of compost.

#### Showing Willow an item that can make supercompost

- **Willow:**  That looks like something that you can make supercompost out of. Fill up the compost bin with stuff like that, and you'll eventually have a bin full of supercompost.
