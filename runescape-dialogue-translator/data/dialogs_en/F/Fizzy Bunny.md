# Fizzy Bunny

- **Original Wiki Page**: [Transcript:Fizzy Bunny](https://runescape.wiki/w/Transcript%3AFizzy%20Bunny)
- **Letter**: `F`

---

## Dialogue Transcript


### Talk to


#### With "the Egg" title before having unlocked its "Cracked" variant

- **Fizzy Bunny:** That's an interesting title... I was the same until my pal, the Makeover Mage, helped me out.
- You've unlocked the 'Cracked' colour for the 'the Egg' title!
- ((Repeated in a pop-up:))
  - You've unlocked the 'Cracked' colour for the 'the Egg' title!
  - (continue)
- **Fizzy Bunny:** Let me slap some new colours on that title for you, maybe they'll serve you well.

#### Standard dialogue

- **Fizzy Bunny:** Well met, Player!
- [Menu]: Select an Option
  - [Choice]: What's going on here?
    - **Player:** What's going on here?
    - **Fizzy Bunny:** I was overseeing the creation of some delicious statuettes - modelled after yours truly - when I was hit with a scrumptious epiphany!
    - **Fizzy Bunny:** Cocoamancy! Animated chocolate goodies! Not just a tasty treat, but an exciting toy!
    - **Fizzy Bunny:** Unfortunately I was led astray by the confidence of a peer I sought assitance from; seems he was lying a bit about his experience, and now the bunnies are loose!
    - **Fizzy Bunny:** They've started inhabiting chocolate burrows nearby, and every few minutes the rascals seem to pop up in a different place.
    - **Fizzy Bunny:** If you manage to track them down, I would be ecstatic to offer you spring tokens in exchange for any you return to me.
    - (previous)
  - [Choice]: I've got something for you.
    - (Condition: Without chocolate rabbits:)
      - **Fizzy Bunny:** Are you pulling my leg? You don't have any rabbits! Come back when you've got something for me.
    - (Condition: With chocolate rabbits:)
      - (Condition: With at least 30,000 spring tokens:)
        - [Menu]: You will not receive any Spring tokens for this. Hand in ayway?
          - [Choice]: Yes.
            - (removes=all chocolate rabbits in backpack)
            - You have reached the Spring token soft cap of 30,000. You need to spend some tokens in Gummy's store before you can earn more.
            - (pop-up)
              - {{Pop-up|You have reached the Spring token soft cap of 30,000. You need to spend some tokens in Gummy's store before you can earn more.|warning=yes}}
              - (continue)
          - [Choice]: No.
            - (end)
      - (Condition: With less than 30,000 spring tokens:)
        - (removes=all chocolate rabbits in backpack)
        - The following has been added to your currency pouch: [number] x Spring tokens
        - (continue)
      - **Fizzy Bunny:** Amazing work, Player! Take these as payment and get back out there, stat!
  - [Choice]: Farewell.
    - **Player:** Farewell, Fizzy.
    - **Fizzy Bunny:** Come back soon! With as many chocolate rabbits as you can hold!

### Hand in

- (above|I've got something for you)
