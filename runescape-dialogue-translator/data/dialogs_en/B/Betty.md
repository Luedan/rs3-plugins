# Betty

- **Original Wiki Page**: [Transcript:Betty](https://runescape.wiki/w/Transcript%3ABetty)
- **Letter**: `B`

---

## Dialogue Transcript


### In Port Sarim

- **Betty:** Welcome to the magic emporium.
- [Menu]: Choose an option:
  - [Choice]: cond=After The Hand in the Sand, and on a members world|Talk to Betty about The Hand in the Sand.
    - **Betty:** Zavistic told me what a good job you did. If you want some more pink dye, I have made up a batch and you can have some for 20 gold.
    - [Menu]: Select an Option
      - [Choice]: No thanks, Betty.
        - **Player:** No thanks, Betty. Good luck with the shop. I might be back for some dye later.
        - **Betty:** Thanks, Player. See you soon.
      - [Choice]: Yes, please!
        - **Player:** Yes, please!
        - (Condition: If the player has no space in backpack for the dye:)
          - **Betty:** I'm afraid you don't have space in your pack for anything more, come back when you do.
        - (Condition: If the player does not have 20 coins:)
          - You can not afford that.
          - You don't have enough money at the moment, come back later.
        - (Condition: Otherwise:)
          - You hand over 20 gold pieces in return for the dye
          - (removes=20 coins) (receives=pink dye)
  - [Choice]: Can I see your wares?
    - (opens=Betty's Magic Emporium)
  - [Choice]: Sorry, I'm not into magic.
    - **Player:** Sorry, I'm not into magic.
    - **Betty:** Well, if you see anyone who is into magic, please send them my way.

### Manor Farm


#### Help


##### Before completing the request

- [Menu]: What would you like to do?
  - [Choice]: Ask about their request.
    - **Player:** What're you requesting today?
    - **Betty:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **Betty:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - **Betty:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]. or [Animal]
    - **Betty:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - **Betty:** If you complete this, I'll give you : Fire rune x 250. I'm sure you'll gain some reputation with the farming guild too!
    - **Betty:** You'll have to be quick though!, I'm only here for [number] days, [number] hours and [number] minutes. To be exact.
  - [Choice]: Give them the items & animals for their request
    - (Condition: Without the requested items:)
      - **Betty:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **Betty:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - **Betty:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal]
      - **Betty:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - (Condition: With the requested items:)
      - (removes=the requested items) (receives=250 fire runes and Brassica primer)
      - For completing this request you've received Brassica primer x 1.
      - ((Repeated in a pop-up:))
        - {{Pop-up|For completing this request you've received Brassica primer x 1.|colour=#EBE0BC|shadow=no}}
        - (continue)
      - [You've received : Fire rune x 250<br>And 5,500 farming reputation.]

##### After completing the request

- **Betty:** Thank you for your help!
- A new request will be available in [time]{{Sic|..}}

#### Hand in medium request


##### Before completing the request


##### Without requested items

- **Betty:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **Betty:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- **Betty:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal
- **Betty:** I'm also looking for some produce, so I'll need : [Produce] x [number]

##### With requested items

- (removes=the requested items) (receives=250 fire runes and Brassica primer)
- For completing this request you've received Brassica primer x 1.
- ((Repeated in a pop-up:))
  - {{Pop-up|For completing this request you've received Brassica primer x 1.|colour=#EBE0BC|shadow=no}}
  - (continue)
- [You've received : Fire rune x 250<br>And 5,500 farming reputation.]

##### After completing the request

- You've already completed this request, there will be a new bi-daily request in [time]{{Sic|..}}
