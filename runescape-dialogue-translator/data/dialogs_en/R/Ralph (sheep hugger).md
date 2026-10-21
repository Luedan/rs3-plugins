# Ralph (sheep hugger)

- **Original Wiki Page**: [Transcript:Ralph (sheep hugger)](https://runescape.wiki/w/Transcript%3ARalph%20%28sheep%20hugger%29)
- **Letter**: `R`

---

## Dialogue Transcript


### Sell Animals

- **Ralph (sheep hugger):** I have a special request for [breed]. Especially if it has the [Trait] trait!
- **Ralph (sheep hugger):** I'm also after some Sheep, in fact I'll buy up to [number] more while I'm here.
- ((Repeated for each sheep in backpack:))
  - Would you like to sell [name] for [number] beans?
  - [Menu]: Sell [name] for [number] beans?
    - [Choice]: Yes.
      - ((If the player has a million beans:))
        - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
        - **Ralph (sheep hugger):** You can't hold anymore beans, I can't purchase this animal off you.
        - (continue)
      - ((If transaction would take the player over a million beans:))
        - This transaction would take you over the cap of one million beans. In doing so, you would lose out on [number] beans.
        - [Menu]: Complete transaction anyway?
          - [Choice]: Yes.
            - {{Qact|The animal is sold.}}
            - [number] beans added to your currency pouch.
            - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - [Choice]: No.
            - **Ralph (sheep hugger):** You can't hold anymore beans, I can't purchase this animal off you.
      - ((Otherwise:))
        - {{Qact|The animal is sold.}}
        - [number] beans added to your currency pouch.
        - (continue)
    - [Choice]: No.
      - (end)
- ((If animals were not sold:))
  - **Player:** Let me check what animals I have which match your request.
- ((If animals were sold:))
  - ((If Ralph can still buy more:))
    - (end)
  - ((If Ralph can't buy more:))
    - **Ralph (sheep hugger):** I've bought all the animals I need for now, catch you later!
    - {{Qact|Ralph teleports away.}}

### Quick-sell animals

- **Ralph (sheep hugger):** Are you sure you want me to take all the Sheep you're holding? I won't take any of your favourites.
- [Menu]: Sell all of your sheep?
  - [Choice]: Yes
    - ((With sheep in backpack:))
      - ((If the player has a million beans:))
        - ((Repeated for each remaining animal, then continues below:))
          - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - **Ralph (sheep hugger):** You can't hold anymore beans, I can't purchase this animal off you.
        - You don't have any animals to sell. Zero animals, Zero beans!
      - ((If transaction would take the player over a million beans:))
        - ((Repeated for each animal not surpassing the cap, then continues below:))
          - {{Qact|The animal is sold.}}
          - [number] beans added to your currency pouch.
        - ((Repeated for each animal left to sell, then continues below:))
          - This transaction would take you over the cap of one million beans. In doing so, you would lose out on [number] beans.
          - [Menu]: Complete transaction anyway?
            - [Choice]: Yes.
              - {{Qact|The animal is sold.}}
              - [number] beans added to your currency pouch.
              - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
              - ((Repeated for each remaining animal, then continues below:))
                - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
                - **Ralph (sheep hugger):** You can't hold anymore beans, I can't purchase this animal off you.
              - ((If multiple animals were sold:))
                - You've sold [number] animals for [number] total beans.
            - [Choice]: No.
              - **Ralph (sheep hugger):** You can't hold anymore beans, I can't purchase this animal off you.
              - (continue)
        - ((If no animals were sold:))
          - You don't have any animals to sell. Zero animals, Zero beans!
        - ((If multiple animals were sold:))
          - You've sold [number] animals for [number] total beans.
      - ((Otherwise:))
        - ((Repeated for each animal not surpassing the cap, then continues below:))
          - {{Qact|The animal is sold.}}
          - [number] beans added to your currency pouch.
        - ((If multiple animals were sold:))
          - You've sold [number] animals for [number] total beans.
    - ((Without sheep in backpack:))
      - You don't have any animals to sell. Zero animals, Zero beans!
  - [Choice]: No
    - (end)
