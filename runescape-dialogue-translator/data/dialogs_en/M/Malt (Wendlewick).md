# Malt (Wendlewick)

- **Original Wiki Page**: [Transcript:Malt (Wendlewick)](https://runescape.wiki/w/Transcript%3AMalt%20%28Wendlewick%29)
- **Letter**: `M`

---

## Dialogue Transcript


### Talk to

- **Malt:** Hello. Do you need any help with brewing?
- [Menu]: Select an Option
  - [Choice]: How do I brew ales?
    - **Player:** How do I brew ales?
    - **Malt:** Well, first off you need to fill the vat with water - two bucketfuls should do the trick.
    - **Malt:** Then you'll need to put in two handfuls of barley malt - that's barley cooked on a range, by the way.
    - **Malt:** After that you'll be putting your main ingredient in - this will decide what ale it is you're brewing.
    - **Malt:** Lastly, you pour a pot full of ale yeast in, which'll start it off fermenting. Then all you have to do is wait for the good stuff!
    - **Player:** How can I get ale yeast?
    - **Malt:** Just ask me! If you bring me a pot I can fill it up with yeast for 25 coins.
    - (previous)
  - [Choice]: How do I brew cider?
    - **Player:** How do I brew cider?
    - **Malt:** First, you'll need some apples. You'll crush them using this cider-press - four apples should make a full bucket of apple-mush. Take four buckets of mush and fill up the vat.
    - **Malt:** After that you pour a pot full of ale yeast in, which'll start it off fermenting. Then all you have to do is wait for the good stuff!
    - **Player:** How can I get ale yeast?
    - **Malt:** Just ask me! If you bring me a pot I can fill it up with yeast for 25 coins.
    - (previous)
  - [Choice]: What do I do once my drink has matured?
    - **Player:** What do I do once my drink has matured?
    - **Malt:** Well, once you've got a full vat of the good stuff, just turn the valve and your barrel will fill up with eight pinks of whatever your chosen tipple is.
    - **Malt:** Once your barrel is full, you can drain it into an empty beer glass or a calquat keg.
    - (previous)
  - [Choice]: Can you sell me any ale yeast?
    - **Player:** Can you sell me any ale yeast?
    - (continue|Buy yeast)
  - [Choice]: Goodbye.
    - **Player:** Goodbye.

### Buy yeast


#### Without 25 coins or an empty pot

- **Malt:** You'll need a pot for me to put the yeast in, as well as 25 coins to pay me.

#### With 25 coins but without an empty pot

- **Malt:** You'll need a pot for me to put the yeast in.

#### With an empty pot but without 25 coins

- **Malt:** You'll need 25 coins to pay me for the yeast.

#### With 25 coins and an empty pot

- [Menu]: Fill your pot with yearst for 25 coins?
  - [Choice]: Fill your pot
    - (removes=25 coins and empty pot) (receives=ale yeast)
  - [Choice]: Nevermind.
    - (end)
