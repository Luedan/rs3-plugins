# Henrietta (chicken chaser)

- **Original Wiki Page**: [Transcript:Henrietta (chicken chaser)](https://runescape.wiki/w/Transcript%3AHenrietta%20%28chicken%20chaser%29)
- **Letter**: `H`

---

## Dialogue Transcript


### Sell Animals

- **Henrietta (chicken chaser):** I have a special request for [breed]. Especially if it has the [Trait] trait!
- **Henrietta (chicken chaser):** I'll buy up to [number] more chickens.
- ((Repeated for each chicken in backpack:))
  - Would you like to sell [name] for [number] beans?
  - [Menu]: Sell [name] for [number] beans?
    - [Choice]: Yes.
      - ((If the player has a million beans:))
        - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
        - **Henrietta (chicken chaser):** You can't hold anymore beans, I can't purchase this animal off you.
        - (continue)
      - ((If transaction would take the player over a million beans:))
        - This transaction would take you over the cap of one million beans. In doing so, you would lose out on [number] beans.
        - [Menu]: Complete transaction anyway?
          - [Choice]: Yes.
            - {{Qact|The animal is sold.}}
            - [number] beans added to your currency pouch.
            - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - [Choice]: No.
            - **Henrietta (chicken chaser):** You can't hold anymore beans, I can't purchase this animal off you.
      - ((Otherwise:))
        - {{Qact|The animal is sold.}}
        - [number] beans added to your currency pouch.
        - (continue)
    - [Choice]: No.
      - (end)
- ((If animals were not sold:))
  - **Player:** Let me check what animals I have which match your request.
- ((If animals were sold:))
  - ((If Henrietta can still buy more:))
    - (end)
  - ((If Henrietta can't buy more:))
    - **Henrietta (chicken chaser):** I've bought enough animals for today!
    - {{Qact|Henrietta teleports away.}}

### Quick-sell animals

- **Henrietta (chicken chaser):** Are you sure you want me to take all the Chickens you're holding? I won't take any of your favourites.
- [Menu]: Sell all of your chickens?
  - [Choice]: Yes
    - ((With chickens in backpack:))
      - ((If the player has a million beans:))
        - ((Repeated for each remaining animal, then continues below:))
          - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - **Henrietta (chicken chaser):** You can't hold anymore beans, I can't purchase this animal off you.
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
                - **Henrietta (chicken chaser):** You can't hold anymore beans, I can't purchase this animal off you.
              - ((If multiple animals were sold:))
                - You've sold [number] animals for [number] total beans.
            - [Choice]: No.
              - **Henrietta (chicken chaser):** You can't hold anymore beans, I can't purchase this animal off you.
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
    - ((Without chickens in backpack:))
      - You don't have any animals to sell. Zero animals, Zero beans!
  - [Choice]: No
    - (end)
