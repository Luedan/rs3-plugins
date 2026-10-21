# Bartender (Jolly Boar Inn)

- **Original Wiki Page**: [Transcript:Bartender (Jolly Boar Inn)](https://runescape.wiki/w/Transcript%3ABartender%20%28Jolly%20Boar%20Inn%29)
- **Letter**: `B`

---

## Dialogue Transcript


### Talk-to


#### Normally

- **Bartender:** Can I help you?
- [Menu]: Select an Option
  - [Choice]: I'll have a beer please.
    - **Player:** I'll have a pint of beer please.
    - **Bartender:** Ok, that'll be two coins please.
    - (Condition: If the player has enough money:)
      - (removes=2 coins) (receives=beer)
      - **Player:** Thanks, Bartender.
    - (Condition: If the player does not have enough money:)
      - You can not afford that.
      - **Bartender:** I said 2 coins! You haven't got 2 coins!
      - **Player:** Sorry, I'll come back another day.
  - [Choice]: Any hints where I can go adventuring?
    - **Player:** Any hints on where I can go adventuring?
    - **Bartender:** Ooh, now. Let me see...
    - **Bartender:** Well there is the Varrock sewers. There are tales of untold horrors coming out at night and stealing babies from houses.
    - **Player:** Sounds perfect! Where's the entrance?
    - **Bartender:** It's just to the east of the palace.
  - [Choice]: Heard any good gossip?
    - **Player:** Heard any gossip?
    - **Bartender:** I'm not that well up on the gossip out here. I've heard that the bartender in the Blue Moon Inn has gone a little crazy, he keeps claiming he is part of something called a computer game.
    - **Bartender:** What that means, I don't know. That's probably old news by now though.

#### With a keg of mead before making a delivery to Jolly Boar Inn during The Need for Mead event

- **Bartender:** Can I help you?
- **Player:** Leslie has sent me here to ask if you could give some feedback on their latest batch of mead.
- **Bartender:** For Leslie, happily!
- (removes=keg of mead) (receives=50 nectar)
- (see|nectar)
- ((Shown in a pop-up:))
  - {{Pop-up|You find 50 x Nectar as you hand over the keg of mead.|colour=#00FF00}}
  - (continue)
- **Player:** I wasn't expecting you to drink it all.
- **Bartender:** It's the best way.
- **Player:** I somehow doubt that.
- **Bartender:** That was pretty good though!
- **Bartender:** The intensity is right. The flavour is good but it just tastes too weak!
- **Bartender:** I know they're always after perfection. This is good, but not perfect!
- **Player:** Thanks, I'll let them know.
