# Moia

- **Original Wiki Page**: [Transcript:Moia](https://runescape.wiki/w/Transcript%3AMoia)
- **Letter**: `M`

---

## Dialogue Transcript


### Battle of Lumbridge

- (see|Battle of Lumbridge)

### [[Tuska Comes]]

- (see|Tuska Comes)

### Anachronia Dinosaur Farm


#### Sell Animals

- **Moia (malletops master):** I have a special request for [Breed]. Especially if they have the [Trait] trait!
- **Moia (malletops master):** I'm also after some Malletops, in fact I'll buy up to [number] more while I'm here.
- ((Repeated for each malletops in backpack:))
  - ((If the animal isn't favourited:))
    - Would you like to sell [name] for [number] beans?
    - (continue)
  - ((If the animal is favourited:))
    - Would you like to sell [name] for [number] beans? {{Colour|#AE0000|You have Etta marked as a favourite!}}
    - (continue)
  - '''SELL [NAME] FOR [NUMBER] BEANS?
    - Yes.
      - ((If the player has a million beans:))
        - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
        - **Moia (malletops master):** You can't hold anymore beans, I can't purchase this animal off you.
      - ((If transaction would take the player over a million beans:))
        - This transaction would take you over the cap of one million beans. In doing so, you would lose out on [number] beans.
        - **COMPLETE TRANSACTION ANYWAY?**
          - Yes.
            - {{Qact|The animal is sold.}}
            - [number] beans added to your currency pouch.
            - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - No.
            - **Moia (malletops master):** You can't hold anymore beans, I can't purchase this animal off you.
            - (continue)
      - ((Otherwise:))
        - {{Transcript missing}}
    - No.
      - (continue)

#### Quick-sell animals

- **Moia (malletops master):** Are you sure you want me to take all the Malletops you're holding? I won't take any of your favourites.
- **SELL ALL OF YOUR MALLETOPS?**
  - Yes
    - ((With non-favourited malletops in backpack:))
      - ((If the player has a million beans:))
        - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
        - **Moia (malletops master):** You can't hold anymore beans, I can't purchase this animal off you.
        - ((Without favourited malletops in backpack:))
          - You don't have any animals to sell. Zero animals, Zero beans!
          - ((Repeated in a pop-up:))
            - You don't have any animals to sell. Zero animals, Zero beans!
        - ((With favourited malletops in backpack:))
          - You don't have any animals to sell. Buyers won't buy favourited animals.
          - ((Repeated in a pop-up:))
            - You don't have any animals to sell. Buyers won't buy favourited animals.
      - ((If transaction would take the player over a million beans:))
        - This transaction would take you over the cap of one million beans. In doing so, you would lose out on [number] beans.
        - **COMPLETE TRANSACTION ANYWAY?**
          - Yes.
            - {{Qact|The animal is sold.}}
            - [number] beans added to your currency pouch.
            - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - No.
            - **Moia (malletops master):** You can't hold anymore beans, I can't purchase this animal off you.
            - ((With favourited malletops in backpack:))
              - You don't have any animals to sell. Buyers won't buy favourited animals.
              - ((Repeated in a pop-up:))
                - You don't have any animals to sell. Buyers won't buy favourited animals
            - ((Without favourited malletops in backpack:))
              - You don't have any animals to sell. Zero animals, Zero beans!
              - ((Repeated in a pop-up:))
                - You don't have any animals to sell. Zero animals, Zero beans!
      - ((Otherwise:))
        - {{Transcript missing}}
    - ((Without non-favourited malletops in backpack:))
      - ((With favourited malletops in backpack:))
        - You don't have any animals to sell. Buyers won't buy favourited animals.
        - ((Repeated in a pop-up:))
          - You don't have any animals to sell. Buyers won't buy favourited animals
      - ((Without favourited malletops in backpack:))
        - You don't have any animals to sell. Zero animals, Zero beans!
        - ((Repeated in a pop-up:))
          - You don't have any animals to sell. Zero animals, Zero beans!
  - No
    - (end)
