# Metarialus

- **Original Wiki Page**: [Transcript:Metarialus](https://runescape.wiki/w/Transcript%3AMetarialus)
- **Letter**: `M`

---

## Dialogue Transcript


### Standard dialogue

- **Metarialus:** Hello. Do you need any help with brewing?
- [Menu]: Select an option
  - [Choice]: How do I brew ales?
    - **Player:** How do I brew ales?
    - **Metarialus:** Well first off you need to fill the vat with water - two bucketfuls should do the trick. Then you'll need to put in two handfuls of barley malt - that's roasted barley by the way.
    - **Metarialus:** After that you'll be putting your main ingredient in - this will decide which ale it is you're brewing. There should be some good guides around with recipes in.
    - **Metarialus:** Lastly you pour a pot full of ale yeast in, which'll start it off fermenting. Then all you have to do is wait for the good stuff.
    - (initial)
  - [Choice]: How do I brew cider?
    - **Player:** How do I brew cider?
    - **Metarialus:** First you'll need some apples. You'll need to crush them using this cider-press - four apples should make a full bucket of apple-mush. Take four buckets of mush and fill up the vat.
    - **Metarialus:** After that you pour a pot full of ale yeast in, which'll start it off fermenting. Then all you have to do is wait for the good stuff.
    - (initial)
  - [Choice]: What do I do once my ale has matured?
    - **Player:** What do I do once my ale has matured?
    - **Metarialus:** Well, once you've got a full vat of the good stuff, just turn the valve and your barrel will fill up with eight pints of whatever your chosen tipple is. Mind it's an empty barrel, though.
    - (initial)
  - [Choice]: Can you sell me any ale yeast?
    - **Player:** Can you sell me any ale yeast?
    - *(If the player doesn't have an empty pot:)*
      - **Metarialus:** I'm afraid you'll need a pot for me to put the yeast in.
    - *(If the player has an empty pot:)*
      - **Metarialus:** I'll want 5 ectotokens for each pot of yeast.
      - '''Fill your pot with yeast for 5 ectotokens?
        - [Choice]: Fill your pot
          - (removes=empty pot and five ecto-tokens)
          - (receives=ale yeast)
          - **Metarialus:** Can I help you with anything else?
          - (initial)
        - [Choice]: Ask about something else
          - (initial)
  - [Choice]: Nothing, thanks!
    - **Player:** Nothing, thanks!
