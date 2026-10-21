# Dalia

- **Original Wiki Page**: [Transcript:Dalia](https://runescape.wiki/w/Transcript%3ADalia)
- **Letter**: `D`

---

## Dialogue Transcript

{{Incomplete|Page should have standard dialogue post-The Lute of Love, any achievement related dialogue should be moved to its respective transcript.}}

### Any option before The Lute of Love achievement

- (see|The Lute of Love)

### After the Lute of Love achievement


#### Pay (Tree patch) or Pay (Fruit tree patch)


##### If patch is empty

- **Dalia:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.

##### If patch is growing something


##### Without the required items.

- **Dalia:** I want [number] [items] for that.
- **Player:** Thanks, maybe another time.

##### With the required items, without confirmation toggled off.

- [Menu]: Pay [number] [items]?
  - [Choice]: Yes.
    - (removes=the requested items)
    - **Dalia:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
    - The gardener is now looking after the patch for you.
  - [Choice]: Yes, and don't ask again.
    - (above)
  - [Choice]: No.
    - (end)

##### With the requires items, with confirmation toggled off.

- (removes=the requested items)
- **Dalia:** That'll do nicely, [sir/madam]. Leave it with me - I'll make sure it grows for you.
- The gardener is now looking after the patch for you.

##### With protection already paid for

- **Dalia:** I don't know what you're talking about - I'm already looking after that patch for you.
- **Player:** Oh sorry, I forgot.

##### If Patch is fully grown

- **Dalia:** That patch is already fully grown. I don't know what you want me to do with it.

#### Talk to

- [Menu]: Choose an option:
  - [Choice]: Would you look after my crops for me?
    - **Player:** Would you look after my crops for me?
    - **Dalia:** I might. Which one were you thinking of?
    - [Menu]: Select an Option
      - [Choice]: The tree patch.
        - (Condition: If the player has no crops in the patch:)
          - **Dalia:** You don't have anything planted in that patch. Plant something and I might agree to look after it for you.
        - (Condition: If the player has fully grown crops planted in the patch:)
          - **Dalia:** That patch is already fully grown! I don't know what you want me to do with it!
        - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
          - **Dalia:** I don't know what you're talking about - I'm already looking after that patch for you.
          - **Player:** Oh sorry, I forgot.
        - (Condition: If the crops in the patch are not yet fully grown:)
          - **Dalia:** If you like, but I want [number] [item] for that.
          - (Condition: If the player does not have the required items:)
            - **Player:** I'm afraid I don't have enough of those at the moment.
            - **Dalia:** Well, I'm not wasting my time for free.
          - (Condition: If the player has the required items:)
            - [Menu]: Select an Option
              - [Choice]: Okay, it's a deal.
                - **Player:** Okay, it's a deal.
                - (removes=the requested items)
                - **Dalia:** That'll do nicely, [Sir/Madam]. Leave it with me - I'll make sure it grows for you.
              - [Choice]: No, that's too much.
                - **Player:** No, that's too much.
                - **Dalia:** Well, I'm not wasting my time for free.
      - [Choice]: The fruit tree patch.
        - (above)
  - [Choice]: Can you tell me about the tree nursery?
    - **Dalia:** In exchange for your help, I'll let you use my tree nursery.
    - **Dalia:** It has a tree patch and a fruit tree patch.
    - **Dalia:** There are also three plots of high quality soil.
    - (Condition: Before completing "From Here to Eternity":)
      - **Dalia** They're empty, since I haven't come across any trees special enough to justify being planted in such great soil.
      - **Dalia** If you find any such trees in your adventures out there, I'd love to see them make the most of it.
    - (Condition: After completing "From Here to Eternity":)
      - **Dalia:** I'm still not used to the otherworldly beauty of the trees that you planted there.
      - **Dalia:** They are exactly the kind of special specimen that I reserved those plots for.
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|Can you stop weeding my farming patches please.
    - **Player:** Can you stop weeding my farming patches please.
    - **Dalia:** Sure, I'll stop weeding them now.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|Can you keep my farming patches weeded please?
    - **Player:** Can you keep my farming patches weeded please?
    - **Dalia:** That shouldn't be a problem, Martin said I should give you special attention for your help with the fairies! Be sure to clear your allotment though as I don't want to interupt their growth!
  - [Choice]: Can you sell me something?
    - **Player:** Can you sell me something?
    - **Dalia:** That depends on whether I have it to sell. What is it that you're looking for?
    - (opens=Farmer's Supplies)
  - [Choice]: That's all, thanks.
    - **Player:** That's all, thanks.

#### Trade

- {{Transcript missing}}
