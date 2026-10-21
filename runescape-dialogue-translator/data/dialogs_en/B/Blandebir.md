# Blandebir

- **Original Wiki Page**: [Transcript:Blandebir](https://runescape.wiki/w/Transcript%3ABlandebir)
- **Letter**: `B`

---

## Dialogue Transcript


### In the Laughing Miner pub in Keldagrim

- **Blandebir:** Hello. Do you need any help with brewing?
- [Menu]: Select an Option
  - [Choice]: How do I brew ales?
    - **Player:** How do I brew ales?
    - **Blandebir:** Well first off you need to fill the vat with water - two bucketfuls should do the trick. Then you'll need to put in two handfuls of barley malt - that's roasted barley by the way.
    - **Blandebir:** After that you'll be putting your main ingredient in - this will decide which ale it is you're brewing. There should be some good guides around with recipes in.
    - **Blandebir:** Lastly you pour a pot full of ale yeast in, which'll start it off fermenting. Then all you have to do is wait for the good stuff.
    - (initial)
  - [Choice]: How do I brew cider?
    - **Player:** How do I brew cider?
    - **Blandebir:** First you'll need some apples. You'll need to crush them using this cider-press - four apples should make a full bucket of apple-mush. Take four buckets of mush and fill up the vat.
    - **Blandebir:** After that you pour a pot full of ale yeast in, which'll start it off fermenting. Then all you have to do is wait for the good stuff.
    - (initial)
  - [Choice]: What do I do once my ale has matured?
    - **Player:**What do I do once my ale has matured
    - **Blandebir:** Well, once you've got a full vat of the good stuff, just turn the valve and your barrel will fill up with eight pints of whatever your chosen tipple is. Mind it's an empty barrel, though.
    - (initial)
  - [Choice]: Can you sell me any ale yeast?
    - **Player:**Can you sell me any ale yeast?
    - (Condition: With no empty pots in backpack:)
      - **Blandebir:** I'm afraid you'll need a pot for me to put the yeast in.
    - (Condition: With less than 25 coins:)
      - **Blandebir:** I'm afraid you'll need 25 coins to pay me for the yeast.
    - (Condition: With empty pots in backpack:)
      - **Blandebir:** I'll want 25 coins for each pot of yeast.
      - [Menu]: Fill a pot with yeast for 25 coins?
        - [Choice]: Fill your pot
          - (removes=one pot and 25 coins) (receives=one pot of ale yeast)
          - (initial)
        - [Choice]: cond=With multiple pots in backpack|Fill all your pots
          - (Condition: With enough money for only some pots:)
            - (removes=pots and 25 coins for each pot) (receives=one pot of ale yeast for each pot)
            - You can not afford that.
            - **Blandebir:** I'm afraid you seem to have run out of money. Can I help you with anything else?
            - (initial)
          - (Condition: With enough money for all pots:)
            - (removes=pots and 25 coins for each pot) (receives=one pot of ale yeast for each pot)
            - (initial)
        - [Choice]: Ask about something else.
          - (initial)
  - [Choice]: Nothing, thanks!
    - **Player:** Nothing, thanks!
