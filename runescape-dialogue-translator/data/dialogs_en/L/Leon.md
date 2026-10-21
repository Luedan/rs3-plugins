# Leon

- **Original Wiki Page**: [Transcript:Leon](https://runescape.wiki/w/Transcript%3ALeon)
- **Letter**: `L`

---

## Dialogue Transcript


### In Yanille

- [Menu]: Select an Option
  - [Choice]: What is this place?
    - **Player:** What is this place?
    - **Leon:** This is Aleck's Hunter Emporium. Basically, it's just a shop with a fancy name; you can buy various weapons and traps here.
    - [Menu]: Select an Option
      - [Choice]: Can I buy some equipment then?
        - **Player:** Can I buy some equipment then?
        - **Leon:** Oh, this isn't my shop; the owner is Aleck over there behind the counter.
        - **Leon:** I experiment with weapon designs. I'm here because I've been trying to convince people to back my research and maybe sell some of my products - like this one I'm holding - in their shops.
        - **Leon:** Aleck doesn't seem to be interested, though.
        - (other)
      - [Choice]: Can I have a go with your crossbow?
        - (below|crossbow)
      - [Choice]: What is that thing you're holding?
        - (below|holding)
  - {{anchor|crossbow}}[Choice]: Can I have a go with your crossbow?
    - **Player:** Could I have a go with your crossbow?
    - **Leon:** I'm afraid with it being a prototype, I've only got a few for my own testing purposes.
    - **Leon:** Of course, for the right price, it might be worth my while to make another prototype.
    - **Player:** How much?
    - **Leon:** To you, 1300 gold pieces.
    - [Menu]: Select an Option
      - [Choice]: Ok, here you go.
        - **Player:** Ok, here you go.
        - (Condition: Without any free backpack space:)
          - **Leon:** Well, you look a little overburdened there at the moment. Maybe you should free up some space to carry it in first.
        - (Condition: Without 1300 coins:)
          - You can not afford that.
          - **Player:** Oh, actually I don't have enough money with me.
        - (Condition: With backpack space and 1300 coins:)
          - (removes=1,300 coins) (receives=Hunters' crossbow)
          - You hand over the money and the weapon designer presents you with a prototype crossbow.
          - **Leon:** Here, you might as well take this one. Aleck over there doesn't seem interested and it'll save you a wait.
      - [Choice]: I'll give it a miss, thanks.
        - **Player:** I'll give it a miss, thanks.
        - **Leon:** Your loss; they'll probably become highly valuable and sought after once I convince someone to market the things.
      - {{anchor|bolts}}[Choice]: Does it use normal crossbow bolts?
        - **Player:** Does it use normal crossbow bolts?
        - **Leon:** Ah, I admit as a result of its er...unique construction, it won't take just any old bolts.
        - **Leon:** If you can supply the materials and a token fee, I'd be happy to make some for you.
        - **Player:** What materials do you need?
        - **Leon:** Kebbit spikes. Lots of 'em. Not all kebbits have spikes, mind you. You'll be needing to look for prickly kebbits or, even better, razor-backed kebbits to get material hard enough.
        - [Menu]: Select an Option
          - [Choice]: Let's see what you can make then.
            - ''(Hunting Bolts interface opens.)
          - [Choice]: I'll give it a miss, thanks.
            - **Player:** I'll give it a miss, thanks.
            - **Leon:** Well, if you ever find yourself in need of that innovative edge, you know who to contact.
            - **Player:** Er, yes, of course.
          - [Choice]: Can't I just make my own?
            - **Player:** Can't I just make my own?
            - **Leon:** Yes, I suppose you could, although you'll need a steady hand with a knife and chisel.
            - **Leon:** The bolts have an unusual diameter, but basically you'll just need to be able to carve kebbit spikes into straight shafts.
            - **Player:** Great; thanks.
  - {{anchor|holding}}[Choice]: What are you holding there?
    - **Player:** What are you holding there?
    - **Leon:** This? This is a prototype for a new type of crossbow I've been designing.
    - **Player:** It looks pretty weird.
    - **Leon:** It's good, isn't it? It includes the bones of various animals in its construction.
    - **Leon:** It's also a fair bit faster than an ordinary crossbow too; it'll take you far less time to reload between shots.
    - [Menu]: Select an Option
      - [Choice]: That's crazy, it'll never work!
        - **Player:** That's crazy, it'll never work!
        - **Leon:** That's what they said about my wind-powered mouse traps, too.
        - **Player:** And did they work?
        - **Leon:** Well, they only ran into problems because people kept insisting on trying to use them indoors.
      - [Choice]: Could I have a go with it?
        - (above|crossbow)
      - [Choice]: Does it use normal crossbow bolts?
        - (above|bolts)
  - [Choice]: cond=With a Hunters' crossbow in backpack|Where can I get suitable bolts for the crossbow that you sold to me?
    - **Player:** Where can I get suitable bolts for the crossbow that you sold to me?
    - (continuea|bolts)
