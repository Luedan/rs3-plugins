# Apprentice Clara

- **Original Wiki Page**: [Transcript:Apprentice Clara](https://runescape.wiki/w/Transcript%3AApprentice%20Clara)
- **Letter**: `A`

---

## Dialogue Transcript

{{Transcript npc|Apprentice Clara}}

### In Burthorpe

- **Apprentice Clara:** So many runes...
- **Player:** Are you alright?
- **Apprentice Clara:** Oh! Don't worry. I'm trying to learn about runes from Mistress Carwen. It's a fascinating subject!
- [Menu]: Select an Option
  - [Choice]: I need runes.
    - (opens=Carwen Essencebinder Magical Runes Shop)
  - [Choice]: What can you tell me about Runecrafting?
    - **Apprentice Clara:** There's so much to talk about! I'm just learning the ropes though. You'd be better off talking to Mistress Carwen.
    - **Apprentice Clara:** As part of my duties I do help her by selling runes. Would you like to take a look?
    - [Menu]: Select an Option
      - [Choice]: I'll have a look.
        - (opens=Carwen Essencebinder Magical Runes Shop)
      - [Choice]: Maybe later.
        - **Apprentice Clara:** Sure thing. If you ever need to get that magic flowing, don't be shy - come see us!

### Manor Farm


#### Help


##### Before completing the request

- [Menu]: What would you like to do?
  - [Choice]: Ask about their request.
    - **Player:** What're you requesting today?
    - **Apprentice Clara:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **Apprentice Clara:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - **Apprentice Clara:** I'm also looking for a new animal, I'm currently after A [animal]
    - **Apprentice Clara:** If you complete this, I'll give you : Air rune x 250. I'm sure you'll gain some reputation with the farming guild too!
    - **Apprentice Clara:** You'll have to be quick though!, I'm only here for [number] hours and [number] minutes. To be exact.
  - [Choice]: Give them the items & animals for their request
    - ((Without the requested items:))
      - **Apprentice Clara:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **Apprentice Clara:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - **Apprentice Clara:** I'm also looking for a new animal, I'm currently after A [animal]
    - ((With the requested items:))
      - (removes=the requested items) (receives=the reward)
      - ((If a Brassica primer was rewarded:))
        - For completing this request you've received Brassica primer x 1.
        - ((Repeated in a pop-up:))
          - For completing this request you've received Brassica primer x 1.
          - (continue)
      - [You've received : Air rune x 250 <br>And 2,750 farming reputation.]

##### After completing the request

- **Apprentice Clara:** Thank you for your help!
- A new request will be available in [time]..

#### Hand in easy request


##### Before completing the request


##### Without requested items

- **Apprentice Clara:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **Apprentice Clara:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- **Apprentice Clara:** I'm also looking for a new animal, I'm currently after A [animal]

##### With requested items

- (removes=the requested items) (receives=the reward)
- ((If a Brassica primer was rewarded:))
  - For completing this request you've received Brassica primer x 1.
  - ((Repeated in a pop-up:))
    - For completing this request you've received Brassica primer x 1.
    - (continue)
- [You've received : Air rune x 250 <br>And 2,750 farming reputation.]

##### After completing the request

- You've already completed this request, there will be a new daily request in [time]..
