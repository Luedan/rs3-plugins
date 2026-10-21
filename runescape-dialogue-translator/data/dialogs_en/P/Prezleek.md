# Prezleek

- **Original Wiki Page**: [Transcript:Prezleek](https://runescape.wiki/w/Transcript%3APrezleek)
- **Letter**: `P`

---

## Dialogue Transcript


### Spring Fayre

- **Prezleek:** Welcome to the Bucking Baroo!
  - [Choice]: What's going on here?
    - *(Only in 2017:)*
      - **Prezleek:** This is the Bucking Baroo - pay 10 tokens, and then hold on for dear life!
      - (continue)
    - *(Only in 2018:)*
      - **Prezleek:** This is the Bucking Baroo - climb on, and then hold on for dear life!
      - (continue)
    - **Player:** Is it safe?
    - **Prezleek:** Really? You're going to question if this, out of all the things you've done on Gielinor, is safe?
    - **Player:** ...is it?
    - **Prezleek:** ...
    - **Prezleek:** Probably not.
    - (other)
  - [Choice]: Don't I recognise you?
    - **Prezleek:** How astute! You've probably seen a fair amount of my fantastic art work here and there.
    - **Player:** Oh, now I remember. You do the funny comics!
    - **Prezleek:** I prefer 'unique masterpieces'.
    - **Player:** They're pretty funny!
    - **Prezleek:** ...thanks.
    - (other)
  - [Choice]: What slayer task are you currently on?
    - **Prezleek:** It's lame. I want Nex.
    - **Player:** But what ab...
    - **Prezleek:** Nex.
    - **Player:** Isn't that a li...
    - **Prezleek:** Nex.
    - **Player:** But how do yo...
    - **Prezleek:** GIMMIE NEX.
    - **Player:** Ugh, forget I asked.
    - (other)
  - [Choice]: Bye
    - **Prezleek:** Have fun!

### Manor Farm


#### During the tutorial

{{Main|Transcript:Player-owned farm Tutorial}}

#### After the tutorial


##### Sell Animals

- **Prezleek (yak trader):** I have a special request for [breed]. Especially if it has the [Trait] trait!
- **Prezleek (yak trader):** I'm also after some Yaks, in fact I'll buy up to [number] more while I'm here.
- ((Repeated for each yak in backpack:))
  - Would you like to sell [name] for [number] beans?
  - [Menu]: Sell [name] for [number] beans?
    - [Choice]: Yes.
      - ((If the player has a million beans:))
        - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
        - **Prezleek (yak trader):** You can't hold anymore beans, I can't purchase this animal off you.
        - (continue)
      - ((If transaction would take the player over a million beans:))
        - This transaction would take you over the cap of one million beans. In doing so, you would lose out on [number] beans.
        - [Menu]: Complete transaction anyway?
          - [Choice]: Yes.
            - {{Qact|The animal is sold.}}
            - [number] beans added to your currency pouch.
            - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - [Choice]: No.
            - **Prezleek (yak trader):** You can't hold anymore beans, I can't purchase this animal off you.
      - ((Otherwise:))
        - {{Qact|The animal is sold.}}
        - [number] beans added to your currency pouch.
        - (continue)
    - [Choice]: No.
      - (end)
- ((If animals were not sold:))
  - **Player:** Let me check what animals I have which match your request.
- ((If animals were sold:))
  - ((If Prezleek can still buy more:))
    - (end)
  - ((If Prezleek can't buy more:))
    - **Prezleek (yak trader):** I've bought all the animals I need for now, catch you later!
    - {{Qact|Prezleek teleports away.}}

##### Quick-sell animals

- **Prezleek (yak trader):** Are you sure you want me to take all the Yaks you're holding? I won't take any of your favourites.
- [Menu]: Sell all of your yaks?
  - [Choice]: Yes
    - ((With yaks in backpack:))
      - ((If the player has a million beans:))
        - ((Repeated for each remaining animal, then continues below:))
          - Your currency pouch is full of beans! You need to spend some beans before you can earn any more.
          - **Prezleek (yak trader):** You can't hold anymore beans, I can't purchase this animal off you.
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
                - **Prezleek (yak trader):** You can't hold anymore beans, I can't purchase this animal off you.
              - ((If multiple animals were sold:))
                - You've sold [number] animals for [number] total beans.
            - [Choice]: No.
              - **Prezleek (yak trader):** You can't hold anymore beans, I can't purchase this animal off you.
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
    - ((Without yaks in backpack:))
      - You don't have any animals to sell. Zero animals, Zero beans!
  - [Choice]: No
    - (end)
