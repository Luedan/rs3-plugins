# Rumbleguts (spider shopper)

- **Original Wiki Page**: [Transcript:Rumbleguts (spider shopper)](https://runescape.wiki/w/Transcript%3ARumbleguts%20%28spider%20shopper%29)
- **Letter**: `R`

---

## Dialogue Transcript


### Sell Animals

- **Rumbleguts (spider shopper):** I have a special request for [breed]. Especially if it has the [Trait] trait!
- **Rumbleguts (spider shopper):** I'm also after some Spiders, in fact I'll buy up to [number] more while I'm here.
- ((Repeated for each spider in backpack:))
  - Would you like to sell [name] for [number] beans?
  - [Menu]: Sell [name] for [number] beans?
    - [Choice]: Yes.
      - ((If the player has a million beans:))
        - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
        - **Rumbleguts (spider shopper):** You can't hold anymore beans, I can't purchase this animal off you.
        - (continue)
      - ((If transaction would take the player over a million beans:))
        - This transaction would take you over the cap of one million beans. In doing so, you would lose out on [number] beans.
        - [Menu]: Complete transaction anyway?
          - [Choice]: Yes.
            - {{Qact|The animal is sold.}}
            - [number] beans added to your currency pouch.
            - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - [Choice]: No.
            - **Rumbleguts (spider shopper):** You can't hold anymore beans, I can't purchase this animal off you.
      - ((Otherwise:))
        - {{Qact|The animal is sold.}}
        - [number] beans added to your currency pouch.
        - (continue)
    - [Choice]: No.
      - (end)
- ((If animals were not sold:))
  - **Player:** Let me check what animals I have which match your request.
- ((If animals were sold:))
  - ((If Rumbleguts can still buy more:))
    - (end)
  - ((If Rumbleguts can't buy more:))
    - **Rumbleguts (spider shopper):** I've bought all the animals I need for now, catch you later!
    - {{Qact|Rumbleguts teleports away.}}

### Quick-sell animals

- **Rumbleguts (spider shopper):** Are you sure you want me to take all the Spiders you're holding? I won't take any of your favourites.
- [Menu]: Sell all of your spiders?
  - [Choice]: Yes
    - ((With spiders in backpack:))
      - ((If the player has a million beans:))
        - ((Repeated for each remaining animal, then continues below:))
          - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - **Rumbleguts (spider shopper):** You can't hold anymore beans, I can't purchase this animal off you.
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
                - **Rumbleguts (spider shopper):** You can't hold anymore beans, I can't purchase this animal off you.
              - ((If multiple animals were sold:))
                - You've sold [number] animals for [number] total beans.
            - [Choice]: No.
              - **Rumbleguts (spider shopper):** You can't hold anymore beans, I can't purchase this animal off you.
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
    - ((Without spiders in backpack:))
      - You don't have any animals to sell. Zero animals, Zero beans!
  - [Choice]: No
    - (end)
