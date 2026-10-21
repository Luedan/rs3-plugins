# Peckish

- **Original Wiki Page**: [Transcript:Peckish](https://runescape.wiki/w/Transcript%3APeckish)
- **Letter**: `P`

---

## Dialogue Transcript


### Talk to

- **Peckish:** You got any of that good stuff for me?
- [Menu]: Select an Option
  - [Choice]: What are you after?
    - **Player:** What are you after?
    - **Peckish:** Valuables, riches, long lost treasures. Anything I can sell to help fill the clan coffers.
    - **Peckish:** You see, things around here don't tend to stay buried. Some of these tombs are so laden in riches they're quite literally bursting.
    - **Peckish:** Every now and then coffins and mausoleums will spring open and become accessible to any nearby light-fingered folk.
    - **Peckish:** If any of these ancient curios do somehow find their way into your possession I'd be happy to pay for them; I've got quite a reputable fence.
    - (previous)
  - [Choice]: I've got some goods for you.
    - **Player:** I've got some goods for you.
    - **Peckish:** Sssh, ssh! Keep it down. Let me see what you've got there...
    - (Condition: Without ancient heirlooms or ancient valuables:)
      - You have nothing to give to Peckish.
      - (popup)
        - {{Pop-up|You have nothing to give to Peckish.|warning=yes}}
        - (previous)
    - (Condition: With ancient heirlooms or ancient valuables:)
      - (Condition: If not surpassing 150,000 spooky tokens if all ancient heirlooms and ancient valuables in backpack would be handed in:)
        - (removes=all ancient heirlooms and ancient valuables)
        - You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.
        - (popup)
          - {{Pop-up|You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.|colour=#FF6600}}
          - (continue)
        - The following has been added to your currency pouch: [number after potential multiplication] x Spooky tokens.
        - (previous)
      - (Condition: If surpassing 150,000 spooky tokens if all ancient heirlooms and ancient valuables in backpack would be handed in:)
        - (Condition: With something to hand in without surpassing 150,000 spooky tokens:)
          - **Peckish:** Woah there, friend. That's too rich for my bones. I can take some of those, but you'll have to spend some spooky tokens before I take the rest.
          - (removes=just enough ancient heirlooms and ancient valuables to not surpass 150,000 spooky tokens, with as many as possible ancient heirlooms included)
          - You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.
          - (popup)
            - {{Pop-up|You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.|colour=#FF6600}}
            - (continue)
          - (Condition: If reaching exactly 150,000 spooky tokens:)
            - You have reached the Spooky token soft cap of 150,000. You need to spend some tokens in the Spooky Reward Shop before you can earn more.
            - (pop-up)
              - {{Pop-up|You have reached the Spooky token soft cap of 150,000. You need to spend some tokens in the Spooky Reward Shop before you can earn more.|warning=yes}}
              - (continue)
          - The following has been added to your currency pouch: [number] x Spooky tokens.
          - (previous)
        - (Condition: Without anything to hand in without surpassing 150,000 spooky tokens:)
          - **Peckish:** Can't be taking any more of those right now; you need to go spend some of your spooky tokens or I can't pay you.
          - (previous)
  - [Choice]: Farewell.
    - **Player:** Farewell.
    - **Peckish:** *sniffle* Bye bye.

### Hand in


#### With ancient heirlooms or ancient valuables


##### If not surpassing 150,000 spooky tokens if all ancient heirlooms and ancient valuables in backpack would be handed in

- (removes=all ancient heirlooms and ancient valuables)
- You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.
- (popup)
  - {{Pop-up|You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.|colour=#FF6600}}
  - (continue)
- The following has been added to your currency pouch: [number after potential multiplication] x Spooky tokens.

##### If surpassing 150,000 spooky tokens if all ancient heirlooms and ancient valuables in backpack would be handed in


##### With something to hand in without surpassing 150,000 spooky tokens

- **Peckish:** Woah there, friend. That's too rich for my bones. I can take some of those, but you'll have to spend some spooky tokens before I take the rest.
- (removes=just enough ancient heirlooms and ancient valuables to reach 150,000 spooky tokens, with as many as possible ancient heirlooms included)
- You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.
- (popup)
  - {{Pop-up|You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.|colour=#FF6600}}
  - (continue)
- (Condition: If reaching exactly 150,000 spooky tokens:)
  - You have reached the Spooky token soft cap of 150,000. You need to spend some tokens in the Spooky Reward Shop before you can earn more.
  - (pop-up)
    - {{Pop-up|You have reached the Spooky token soft cap of 150,000. You need to spend some tokens in the Spooky Reward Shop before you can earn more.|warning=yes}}
    - (continue)
- The following has been added to your currency pouch: [number] x Spooky tokens.

##### Without anything to hand in without surpassing 150,000 spooky tokens

- **Peckish:** Can't be taking any more of those right now; you need to go spend some of your spooky tokens or I can't pay you.

#### Without ancient heirlooms or ancient valuables

- You have nothing to give to Peckish.
- (popup)
  - {{Pop-up|You have nothing to give to Peckish.|warning=yes}}
