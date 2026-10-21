# Steven (salamander commander)

- **Original Wiki Page**: [Transcript:Steven (salamander commander)](https://runescape.wiki/w/Transcript%3ASteven%20%28salamander%20commander%29)
- **Letter**: `S`

---

## Dialogue Transcript


### Sell Animals

- **Steven (salamander commander):** I have a special request for [breed]. Especially if it has the [Trait] trait!
- **Steven (salamander commander):** I'm also after some Salamanders, in fact I'll buy up to [number] more while I'm here.
- ((Repeated for each salamander in backpack:))
  - {{Transcript missing}}

### Quick-sell animals

- **Steven (salamander commander):** Are you sure you want me to take all the Salamanders you're holding? I won't take any of your favourites.
- **SELL ALL OF YOUR SALAMANDERS?**
  - Yes
    - ((With salamanders in backpack:))
      - ((If the player has a million beans:))
        - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
        - **Steven (salamander commander):** You can't hold anymore beans, I can't purchase this animal off you.
        - You don't have any animals to sell. Zero animals, Zero beans!
      - ((If transaction would take the player over a million beans:))
        - {{Transcript missing}}
      - ((Otherwise:))
        - {{Qact|The animals are sold.}}
        - ((Repeated for each animal sold, then continues below:))
          - [number] beans added to your currency pouch.
        - ((If multiple animals were sold:))
          - You've sold [number] animals for [number] total beans.
    - ((Without salamanders in backpack:))
      - You don't have any animals to sell. Zero animals, Zero beans!
  - No
    - (end)
