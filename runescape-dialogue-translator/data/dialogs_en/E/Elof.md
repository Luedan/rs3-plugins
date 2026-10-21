# Elof

- **Original Wiki Page**: [Transcript:Elof](https://runescape.wiki/w/Transcript%3AElof)
- **Letter**: `E`

---

## Dialogue Transcript


### Talking to Elof


#### If speaking to Elof without an Artisan's workshop flyer on you

- **Player:{{anchor|standard}}** Hello. What do you do here?
- **Elof:** I can exchange metal tokens for you, custom fit a set of Trimmed Masterwork Armour or add spikes to your custom-fit armour.<div id="Standard"></div>
- [Menu]: Select an option
  - [Choice]: Metal tokens
    - **Elof:** What're metal tokens, you may ask? Well, we did a large recall of some of the older smithing items, due to hazardous smithing conditions when they were created!
    - **Elof:** As such, we’ve replaced items with tokens of the appropiate metal type, which you can purchase from me, if you’ve got any tokens.
    - [Menu]: Any other questions?
      - [Choice]: How can I obtain more tokens?
        - **Elof:** You can’t obtain any more tokens. We only did the recall once.
        - (previous)
      - [Choice]: Can I trade these tokens?
        - **Elof:** No, you can’t trade these tokens, but you can trade the items you can get by exchanging the tokens.
        - (previous)
      - [Choice]: What if I want my old stuff back?
        - **Elof:** You should be able to buy most of your items back with the tokens we’ve swapped out for you. If you can’t, however, you should be able to smith your old items at a much lower level now.
        - (previous)
      - [Choice]: I want to exchange these tokens.
        - **Elof:** What sort of tokens would you like to exchange?
        - [Menu]: Select an option
          - [Choice]: Steel.
            - (opens=Steel item token exchange)
          - [Choice]: Mithril.
            - (opens=Mithril item token exchange)
          - [Choice]: Adamant.
            - (opens=Adamant item token exchange)
          - [Choice]: Rune.
            - (opens=Rune item token exchange)
      - [Choice]: Nope.
        - (end)
    - [Choice]: Custom-fitting masterwork armour.
      - (below|custom)

#### If speaking to Elof with an Artisan's workshop flyer on you

- **Elof:** Ah, I see you have an Artisans' Workshop flyer. In exchange, I have an exclusive pack of sample items for you! You will need 11 spaces in your backpack!
- [Menu]: Redeem Flyer?
  - [Choice]: Yes.
    - *(If you have enough space in your backpack:)*
      - Elof crumples your flyer into a tight ball, and pops it into his mouth. Chewing thoughtfully, he bestows upon you a generous variety of Mining and Smithing supplies!
      - **Player:** Wow, thanks!<br>Is there anything else you can give me?<!--It's split into two lines in one dialogue box as per in-game-->
      - (continuea|standard)
    - *(If you do not have enough space in your backpack:)*
      - **Elof:** Come back with 11 spaces in your backpack and I'll give you your free stuff!
  - [Choice]: No.
    - (continuea|standard)

### "Metal token exchange" option

- **Elof:**What sort of tokens would you like to exchange?
- [Menu]: Exchange which tokens?
  - [Choice]: Steel.
    - (opens=Steel item token exchange)
  - [Choice]: Mithril.
    - (opens=Mithril item token exchange)
  - [Choice]: Adamant.
    - (opens=Adamant item token exchange)
  - [Choice]: Rune.
    - (opens=Rune item token exchange)

### "Custom-fit Trimmed Masterwork" option

- **Elof:{{anchor|custom}}** If you've got a fully equipped set of trimmed masterwork, I can custom fit it for you. If it's augmented it'll remain augmented and you'll repair it the same way you repair trimmed masterwork.
- **Player:** What does custom-fitting do?
- **Elof:** It will become untradable.
- **Elof:** It will degrade 50% slower so it'll last longer.
- **Elof:** It will also never degrade while on a slayer or reaper task.
- **Elof:** But the process is irreversable. Once custom fitted, your masterwork will always be custom fitted.
- *(If you are wearing a full set of trimmed masterwork:)*
  - [Are you sure you want to custom-fit your Trimmed Masterwork armour?<br />This process will make them permanently un-tradeable, make them degrade 50% slower and never degrade when on a slayer or reaper task.]
  - [Menu]: Custom-fit your trimmed masterwork?
    - [Choice]: Yes
      - (removes=the equipped trimmed masterwork armour set) (receives=custom-fit trimmed masterwork armour set)
    - [Choice]: No
      - (end)
- *(If you are not wearing a full set of trimmed masterwork:)*
  - [You must be wearing a full set of trimmed masterwork in order to custom-fit it

### "Spiked Masterwork armour" option

- **Elof:** Hello. I can add or remove spikes from your custom fit masterwork armour.
- [Menu]: Do you want to add or remove spikes from your armour?
  - [Choice]: Add
    - *(If you do not have any pieces of custom-fit masterwork armour equipped:)*
      - [You must be wearing at least one piece of eligible armour for me to modify it.]
    - *(If you have pieces of custom-fit masterwork armour equipped:)*
      - [Menu]: Are you sure you want to add spikes to your custom-fit Masterwork armour? This process will cost you X Glorious bars.
        - [Choice]: Yes
          - (removes=the equipped custom-fit trimmed masterwork armour set) (receives=custom-fit trimmed spiked masterwork armour set)
        - [Choice]: No
          - (end)
  - [Choice]: Remove
    - *(If you do not have any pieces of armour with spikes attached equipped:)*
      - [You must be wearing at least one piece of eligible armour for me to modify it.]

### At Thalmund's forge

- ((One of the following sequences is seen.))

#### Sequence 1

- (Elof appears at the northern doors.)
- (Elof walks to the debris in the south.)
- **Elof:** {{RSChat|Needs a clean.}}
- (Elof walks to the lever.)
- **Elof:** {{RSChat|Smells like pie and slag.}}
- (Elof walks to the room with the imcando anvil and investigates it.)
- (Elof walks to the furnace.)
- **Elof:** {{RSChat|Impressive.}}
- (Elof walks to the goblin weapon rack, investigates it, and teleports out.)

#### Sequence 2

- (Elof appears at the northern doors.)
- (Elof walks to the debris in the south.)
- **Elof:** {{RSChat|What a mess!}}
- (Elof walks to the lever.)
- **Elof:** {{RSChat|Hmmm...}}
- (Elof walks to the room with the imcando anvil and investigates it.)
- (Elof walks to the furnace.)
- **Elof:** {{RSChat|Not bad.}}
- (Elof walks to the goblin weapon rack, investigates it, and teleports out.)
