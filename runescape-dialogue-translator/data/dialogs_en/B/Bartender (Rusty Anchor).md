# Bartender (Rusty Anchor)

- **Original Wiki Page**: [Transcript:Bartender (Rusty Anchor)](https://runescape.wiki/w/Transcript%3ABartender%20%28Rusty%20Anchor%29)
- **Letter**: `B`

---

## Dialogue Transcript


### Talk-to


#### Normally


##### Before completing the Visions of Havenhythe quest

- [Menu]: Select an Option
  - [Choice]: Talk about 'Visions of Havenhythe'
    - (see|Visions of Havenhythe)
  - [Choice]: Talk about something else.
    - (below|After completing the Visions of Havenhythe quest)

##### After completing the Visions of Havenhythe quest

- **Player:** Good day to you!
- **Bartender:** Hello there!
- (Condition: If the player has completed A Void Dance:)
  - **Bartender:** Thanks for sorting out my cellar.
  - (continue)
- [Menu]: Choose an option:
  - [Choice]: Could I buy a beer, please?
    - **Player:** Could I buy a beer, please?
    - **Bartender:** Sure, that will be two gold coins, please.
    - (Condition: If the player has enough money:)
      - (removes=2 coins) (receives=beer)
      - **Player:** Thanks, Bartender.
    - (Condition: If the player does not have enough money:)
      - You can not afford that.
      - **Bartender:** I said 2 coins! You haven't got 2 coins!
      - **Player:** Sorry, I'll come back another day.
  - [Choice]: cond=After Rocking Out|Ask about 'rum'.
    - **Player:** How's things?
    - **Bartender:** Not good! The demand for Braindeath's drain-scouring solution has dropped completely off.
    - **Player:** Wow! It must have been one of those marketing peaks you hear about.
    - **Bartender:** Whatever it was, I'm now in a 10-year contract to stock that old jackal's noxious swill.
    - **Bartender:** You wouldn't want some, would you?
    - [Menu]: Select an Option
      - [Choice]: Oh, okay.
        - **Player:** Oh, okay.
        - (Condition: If the player has enough money:)
          - (removes=30 coins) (receives=Braindeath 'rum')
          - **Bartender:** Thanks! I know that it's wrong to take advantage of your crippling addiction to this dangerous substance, but I have a bar to run.
          - **Player:** How community-minded of you.
        - (Condition: If the player does not have enough money:)
          - You can not afford that.
          - **Bartender:** Oh, you poor 'rum'-addled urchin! You don't have the money for it, but you still want the stuff.
          - **Bartender:** *Sniff* It's sad to see someone brought so low.
          - **Player:** Hey! I am NOT an urchin!
      - [Choice]: Sorry. Not right now.
        - **Player:** Sorry. Not right now.
        - **Bartender:** Pah! I should never have listened to you.
  - [Choice]: Bye, then.
    - **Player:** Bye, then.
    - **Bartender:** Come back soon!

#### Treasure Trails

- **Bartender:** Congratulations! Here you go.
- (removes=the old clue scroll (easy))
- ((If the trail continues:))
  - (receives=a new clue scroll (easy))
  - [The bartender has given you another clue scroll.]
- ((If the trail ends:))
  - (receives=reward casket (easy))
  - [You've found a casket!]

#### With a keg of mead before making a delivery to Rusty Anchor during The Need for Mead event

- **Player:** I was wondering if you could give some feedback on this mead?
- **Bartender:** Where was it brewed? Who's the brewer?
- **Player:** I have no idea where it was brewed but the brewer is called Leslie.
- **Bartender:** I'm not trying anything they make, ever again. Not after last time...
- **Player:** What happened last time?
- **Bartender:** That's not for you to know.
- **Bartender:** Actually, you know what, hand it over. Let me have a look.
- (removes=keg of mead) (receives=50 nectar)
- (see|nectar)
- ((Shown in a pop-up:))
  - {{Pop-up|You find 50 x Nectar as you hand over the keg of mead.|colour=#00FF00}}
  - (continue)
- **Player:** Whoa! Don't tip it all away.
- **Bartender:** I'm doing a justice to Gielinor by ensuring no one else has to drink this.
- **Player:** Okay then...
- **Player:** Mr. Grumpy...
- **Bartender:** What did you say?!
- **Player:** Bye!

#### Historical dialogue

- [Menu]: Select an Option
  - [Choice]: Could I buy a beer please?
    - (above)
  - [Choice]: Have you heard any rumours here?
    - **Player:** Have you heard any rumours here?
    - (Condition: Before Goblin Diplomacy:)
      - **Bartender:** Well, there was a guy in here earlier saying the goblins up by the mountain are arguing again, about the colour of their armour of all things.
      - **Bartender:** Knowing the goblins it could easily turn into a full blown war, which wouldn't be good. Goblin wars make such a mess of the countryside.
      - **Player:** Well if I have the time I'll go and see if I can knock some sense into them.
    - (Condition: After Goblin Diplomacy:)
      - **Bartender:** No, it hasn't been very busy lately.
