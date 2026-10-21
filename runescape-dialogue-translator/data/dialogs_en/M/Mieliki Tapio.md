# Mieliki Tapio

- **Original Wiki Page**: [Transcript:Mieliki Tapio](https://runescape.wiki/w/Transcript%3AMieliki%20Tapio)
- **Letter**: `M`

---

## Dialogue Transcript


### Tree Gnome Stronghold

- **Mieliki Tapio:** What do you want, human? Mieliki is working.
- [Menu]: What would you like to say?
  - [Choice]: What is this place?{{anchor|place}}
    - **Mieliki Tapio:** This is Mieliki's shop. People help Mieliki's stupid husband to get supplies for the alchemy. They are awarded competence points for working. Here, in this shop, Mieliki exchanges competence points for rewards. Mieliki admires competence, and is pleased to reward people who possess it.
    - [Menu]: What would you like to say?
      - [Choice]: What are you doing?
        - (below|doing)
      - [Choice]: What are the portals for?
        - (below|portal)
      - [Choice]: I have some competence points to exchange.
        - (below|points)
      - [Choice]: I'll be off now.{{anchor|off}}
        - **Mieliki Tapio:** Very well, human. Work hard.
  - [Choice]: What are you doing?{{anchor|doing}}
    - **Mieliki Tapio:** Mieliki is working. Humans have no idea of work. Humans expect free stuff! But Mieliki is a hard worker. Mieliki is an alchemist. She experiments with chemicals, working hard. One day, Mieliki hopes to invent something good, and sell it for lots of money. When that day comes, Mieliki will be rewarded for all this work. That is how success should come, through hard work.
    - [Menu]: What would you like to say?
      - [Choice]: What are you trying to invent?
        - **Mieliki Tapio:** Mieliki does not mind. Big chinchompa chemicals are good for explosions, but Mieliki does not like violence. Success should come through hard work, not violence.
        - (other)
      - [Choice]: What is this place?
        - (above|place)
      - [Choice]: What are the portals for?
        - (below|portal)
      - [Choice]: I have some competence points to exchange.
        - (below|points)
      - [Choice]: I'll be off now.
        - (above|off)
  - [Choice]: What are the portals for?{{anchor|portal}}
    - **Mieliki Tapio:** First, Mieliki will talk about Nyriki's portal, the orange one. It leads to the place where Nyriki is hunting. Humans can go through to work for him. Nyriki can explain what help he wants. Talk to him when you see him. Other portals lead to secret places, places no-one can reach without Mieliki's magic. Mieliki puts creatures in these places for stupid Nyriki to practice his hunting. Nyriki thinks he is good at hunting, but he is incorrect. Humans can practice their hunting there too, if they buy tickets. Each ticket lets them catch one creature.
    - [Menu]: What would you like to say?
      - [Choice]: What is this place?
        - (above|place)
      - [Choice]: What are you doing?
        - (above|doing)
      - [Choice]: I have some competence points to exchange.
        - (below|points)
      - [Choice]: I'll be off now.
        - (above|off)
  - [Choice]: cond=If the player has competence points:|I have some competence points to exchange.{{anchor|points}}
    - **Mieliki Tapio:** Oh, you have been helping Nyriki. Time is money; you have given us your time, so you deserve a reward. That is the way.
    - (opens=Reward Shop (Big Chinchompa))
  - [Choice]: cond=If the player does not have any competence points:|Have you any rewards to offer?
    - **Mieliki Tapio:** Mieliki has rewards, yes, but people must help Nyriki to earn them. Mieliki is not some stupid goblin giving rewards for free.
    - (opens=Reward Shop (Big Chinchompa))
  - [Choice]: Nothing, thanks.
    - **Mieliki Tapio:** You want nothing, human? If you aim for nothing, nothing shall be your reward! Be warned.

### Player-owned farm


#### Sell Animals

- **Mieliki Tapio (chinchompa collector):** I have a special request for [breed]. Especially if it has the [Trait] trait!
- **Mieliki Tapio (chinchompa collector):** I'm also after some Chinchompas, in fact I'll buy up to [number] more while I'm here.
- ((Repeated for each chinchompa in backpack:))
  - Would you like to sell [name] for [number] beans?
  - [Menu]: Sell [name] for [number] beans?
    - [Choice]: Yes.
      - ((If the player has a million beans:))
        - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
        - **Mieliki Tapio (chinchompa collector):** You can't hold anymore beans, I can't purchase this animal off you.
        - (continue)
      - ((If transaction would take the player over a million beans:))
        - This transaction would take you over the cap of one million beans. In doing so, you would lose out on [number] beans.
        - [Menu]: Complete transaction anyway?
          - [Choice]: Yes.
            - {{Qact|The animal is sold.}}
            - [number] beans added to your currency pouch.
            - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - [Choice]: No.
            - **Mieliki Tapio (chinchompa collector):** You can't hold anymore beans, I can't purchase this animal off you.
      - ((Otherwise:))
        - {{Qact|The animal is sold.}}
        - [number] beans added to your currency pouch.
        - (continue)
    - [Choice]: No.
      - (end)
- ((If animals were not sold:))
  - **Player:** Let me check what animals I have which match your request.
- ((If animals were sold:))
  - ((If Mieliki Tapio can still buy more:))
    - (end)
  - ((If Mieliki Tapio can't buy more:))
    - **Mieliki Tapio (chinchompa collector):** I've bought all the animals I need for now, catch you later!
    - {{Qact|Mieliki Tapio teleports away.}}

#### Quick-sell animals

- **Mieliki Tapio (chinchompa collector):** Are you sure you want me to take all the Chinchompas you're holding? I won't take any of your favourites.
- [Menu]: Sell all of your chinchompas?
  - [Choice]: Yes
    - ((With chinchompas in backpack:))
      - ((If the player has a million beans:))
        - ((Repeated for each remaining animal, then continues below:))
          - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - **Mieliki Tapio (chinchompa collector):** You can't hold anymore beans, I can't purchase this animal off you.
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
                - **Mieliki Tapio (chinchompa collector):** You can't hold anymore beans, I can't purchase this animal off you.
              - ((If multiple animals were sold:))
                - You've sold [number] animals for [number] total beans.
            - [Choice]: No.
              - **Mieliki Tapio (chinchompa collector):** You can't hold anymore beans, I can't purchase this animal off you.
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
    - ((Without chinchompas in backpack:))
      - You don't have any animals to sell. Zero animals, Zero beans!
  - [Choice]: No
    - (end)
