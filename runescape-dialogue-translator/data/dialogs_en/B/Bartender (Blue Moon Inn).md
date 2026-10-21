# Bartender (Blue Moon Inn)

- **Original Wiki Page**: [Transcript:Bartender (Blue Moon Inn)](https://runescape.wiki/w/Transcript%3ABartender%20%28Blue%20Moon%20Inn%29)
- **Letter**: `B`

---

## Dialogue Transcript


### In Varrock


#### Normally

- **Bartender:** What can I do yer for?
- (Condition: With a construction contract:)
  - [Menu]: Select an Option
    - [Choice]: Ask about contracts
      - [Menu]: Select an Option
        - [Choice]: What do you need repairing?
          - **Bartender:** Let me see, right now I need you to repair the following pieces of furniture.
          - **Bartender:** [Furniture 1], [Furniture 2], [Furniture 3], [Furniture 4], [Furniture 5]
          - (previous)
        - [Choice]: What materials do I need?
          - **Bartender:** You need: Planks x [number], Steel nails x [number]
          - (previous)
        - [Choice]: [Leave]
          - (end)
    - [Choice]: Ask about something else
      - (below|standard)
- (Condition: Otherwise:)
  - {{anchor|standard}}[Menu]: Select an Option
    - [Choice]: A glass of your finest ale please.
      - **Player:** A glass of your finest ale please.
      - **Bartender:** No problemo. That'll be 2 coins.
      - (Condition: If the player has enough money:)
        - (removes=2 coins) (receives=beer)
        - **Player:** Thanks, Bartender.
      - (Condition: If the player does not have enough money:)
        - You can not afford that.
        - **Bartender:** I said 2 coins! You haven't got 2 coins!
        - **Player:** Sorry, I'll come back another day.
    - [Choice]: Can you recommend where an adventurer might make [his/her] fortune?
      - **Player:** Can you recommend where an adventurer might make [his/her] fortune?
      - **Bartender:** Ooh I don't know if I should be giving away information, makes the computer game too easy.
      - [Menu]: Select an Option
        - [Choice]: Oh ah well...
          - **Player:** Oh ah well...
        - [Choice]: Computer game? What are you talking about?
          - **Player:** Computer game? What are you talking about?
          - **Bartender:** This world around us... is a computer game... called RuneScape.
          - **Player:** Nope, still don't understand what you are talking about. What's a computer?
          - **Bartender:** It's a sort of magic box thing, which can do all sorts of stuff.
          - **Player:** I give up. You're obviously completely mad!
        - [Choice]: Just a small clue?
          - **Player:** Just a small clue?
          - **Bartender:** Go and talk to the bartender at the Jolly Boar Inn, he doesn't seem to mind giving away clues.
    - [Choice]: Do you know where I can get some good equipment?
      - **Player:** Do you know where I can get some good equipment?
      - **Bartender:** Well, there's the sword shop across the road, or there's also all sorts of shops up around the market.

#### With the clue scroll requiring to talk to him

- (removes=the old clue scroll (easy))
- ((If the trail continues:))
  - (receives=a new clue scroll (easy))
  - [The bartender has given you your next clue scroll!]
  - (continue)
- ((If the trail ends:))
  - (receives=reward casket (easy))
  - [You've found a casket!]
  - (continue)
- **Bartender:** Perfect.

#### With a keg of mead before making a delivery to Blue Moon Inn during The Need for Mead event

- **Bartender:** What can I do yer for?
- **Player:** I've been sent here to see if you'd be interested in trying and giving some feedback on this mead. I have an entire keg for you.
- **Bartender:** More mead from Leslie? They just don't give up!
- **Player:** Yeah, they were hoping you'd have some constructive feedback on this latest batch?
- **Bartender:** Let me have a try.
- (removes=keg of mead) (receives=50 nectar)
- (see|nectar)
- ((Shown in a pop-up:))
  - {{Pop-up|You find 50 x Nectar as you hand over the keg of mead.|colour=#00FF00}}
  - (continue)
- **Bartender:** Hmm...
- **Bartender:** Better than the last batch...
- **Bartender:** Something isn't quite right though...
- **Bartender:** Yer, there's a nasty after taste. I wouldn't stock this.
- **Player:** Okay, I'll let them know. Thanks.

### In New Varrock

- **Bartender:** What can I do yer for?
- [Menu]: Select an Option
  - [Choice]: A glass of your finest ale.
    - **Bartender:** That's two zemomarks.
    - (Condition: If the player does not have enough zemomarks:)
      - **Bartender:** No money, no beer.
      - (initial)
    - (Condition: If the player has enough zemomarks:)
      - (removes=two zemomarks) (receives=beer)
      - **Bartender:** Enjoy.
      - (initial)
  - [Choice]: Where can an adventurer earn their fortune here?
    - **Bartender:** Nope.<br>Not any more.<br>No adventurers left.
    - (initial)
  - [Choice]: Where can I get some good equipment here?
    - **Bartender:** Shops.<br>Picking pockets.
    - (initial)
  - [Choice]: Nothing, thanks.
  - (end)
