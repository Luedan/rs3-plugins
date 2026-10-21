# Beefy Bill

- **Original Wiki Page**: [Transcript:Beefy Bill](https://runescape.wiki/w/Transcript%3ABeefy%20Bill)
- **Letter**: `B`

---

## Dialogue Transcript


### Standard dialogue

- **Beefy Bill:** Beefy Bill at your service! <br/>I can bank your beef, your cowhides and your flour, and I've got other stuff for trade. What's it to be?
- [Menu]: What would you like to say?
  - [Choice]: Let's trade.
  - (opens=Beefy Bill's Supplies)
  - [Choice]: I want you to bank things for me.
    - **Beefy Bill:** Excellent. Just hand me the items, and I'll work out a price for you. I charge a 10% commission.
  - [Choice]: Who are you?
    - **Beefy Bill:** I'm Beefy Bill, specialist meat transporter and general merchant.
    - **Beefy Bill:** People bring me their beef, cowhides and flour, and I transport it all to the bank, keeping a mere 10% for my services. I also have stuff for sale.
    - [Menu]: What would you like to say?
      - [Choice]: I want you to bank things for me.
        - (above)
      - [Choice]: Let's trade.
        - (above)
      - [Choice]: How do you pull your wagon?
        - **Beefy Bill:** Oh, I don't pull it myself! <br/>I use cattle to pull it for me.
        - [Menu]: What would you like to say?
          - [Choice]: Isn't that disgusting?
            - **Beefy Bill:** Oh, stop being naive! I'm not letting your petty personal ethics stand in the way of my right to run a successful business.
            - **Beefy Bill:** Now, do you want my services or not?
            - (other)
          - [Choice]: I want you to bank things for me.
            - (above)
          - [Choice]: Let's trade.
            - (above)
          - [Choice]: I'll have a think about it.
            - (below)
      - [Choice]: I'll have a think about it.
        - (below)
  - [Choice]: I'll have a think about it.
    - **Beefy Bill:** Don't waste too much time thinking; time is money.

### Using items on Bill


#### Cowhides, raw beef or pots of flour

- [Menu]: Bill keeps 1 item out of every 10:
  - (Condition: If the player has less than 11 of the relevant item:)
    - [Choice]: Bank [number], Bill keeps 1.
      - **Beefy Bill:** Pleasure doing business with ya, mate!
    - [Choice]: Forget it.
      - (end)
    - [Choice]: cond=With a ring of charos(a) equipped|[Charm] Bank [number], Bill keeps 0.
      - **Beefy Bill:** Um...okay, I suppose I'll do it for free.
  - (Condition: If the player has 12 to 22 of the relevant item:)
    - [Choice]: Bank [number], Bill keeps 1.
      - **Beefy Bill:** Pleasure doing business with ya, mate!
    - [Choice]: Bank [number], Bill keeps 2.
      - **Beefy Bill:** Pleasure doing business with ya, mate!
    - [Choice]: Forget it.
      - (end)
    - [Choice]: cond=With a ring of charos(a) equipped|[Charm] Bank [number], Bill keeps 0.
      - **Beefy Bill:** Um...okay, I suppose I'll do it for free.
  - (Condition: If the player has 23 or greater of the relevant item:)
    - [Choice]: Bank [number], Bill keeps 2.
      - **Beefy Bill:** Pleasure doing business with ya, mate!
    - [Choice]: Bank [number], Bill keeps 3.
      - **Beefy Bill:** Pleasure doing business with ya, mate!
    - [Choice]: Forget it.
      - (end)
    - [Choice]: cond=With a ring of charos(a) equipped|[Charm] Bank [number], Bill keeps 0.
      - **Beefy Bill:** Um...okay, I suppose I'll do it for free.

#### Any other item

- **Beefy Bill:** Sorry, I don't transport that sort of thing.
