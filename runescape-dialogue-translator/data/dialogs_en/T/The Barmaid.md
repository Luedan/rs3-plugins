# The Barmaid

- **Original Wiki Page**: [Transcript:The Barmaid](https://runescape.wiki/w/Transcript%3AThe%20Barmaid)
- **Letter**: `T`

---

## Dialogue Transcript


### Standard dialogue

- **The Barmaid:** Hello there, love. Alright?
- [Menu]: Select an option:
  - [Choice]: How are things going, Surula?
    - **The Barmaid:** Oh, I can't complain, Portmaster. The adventurers and captains who turn up here every day keep my busy. Mind you, John was here last night. Drunk of course. Shouting something about sailing one of the ships eastwards. Bless him. I'm glad you're here. We've needed someone to sort this place out for a long time. For the past few years its felt like we've been trapped in cobwebs and shadows. With you here, it feels light again.
    - (previous|PreviousOptions)
  - [Choice]: Could I ask a personal question?
    - **The Barmaid:** You want to know about the tentacles, right?
    - **Player:** Er - yes.
    - **The Barmaid:** Oh, dont blush, little octopus. You see there's an afflication in the east, no one knows the cause of it, but some of us are born with gills, tentacles, even fins. One poor man had flippers; meant he couldn't wear shoes. You'd reckon looking like this we'd have some special powers, like that siren sulking around the docks, but you'd be wrong. I can swim better than most, sure, but that's about it. Of course, there's many folks who are distrustful of us. They call us sea orphans, which says a lot. And some are more than just distrustful. The Purists in the Scythe region hate us with a real passion. They spread lies about us, beat us up, kill us when they get the chance, scare mothers into drowning us at birth. No one does much about them. Cruel folks, them Purists. Ah...sorry, love. You don't want to hear me prattle on.
    - (previous|PreviousOptions)
  - [Choice]: Got any gossip?
    - (Condition: If it's not Thursday or A Barmaid's Tip has already been sent out:)
      - **The Barmaid:** There's nothing doing the rounds at the moment, love, but I'll keep my tentacles to the ground.
      - Speak to the barmaid on Thursday for new gossip.
      - Speak to the barmaid on Thursday for new gossip.
    - (Condition: If it's Thursday:)
      - (Condition: Without having received A Barmaid's Tip:)
        - **The Barmaid:** Got word of a special little something your crews might find appealing, if you're up for it.
        - [Menu]: Replace your third listed mission with the Barmaid's Tip?
          - [Choice]: Yes.
            - **The Barmaid:** Oh, you're gonna love this!
            - (Voyages interface opens with the third listed mission replaced with A Barmaid's Tip.)
          - [Choice]: No.
            - (previous|PreviousOptions)
      - ((Having received A Barmaid's Tip but not yet sent it out:))
        - **The Barmaid:** Hope that tip worked out well for you, my love.
  - [Choice]: Any chance of a beer?
    - (Condition: If player has at least 1 coin in their inventory or money pouch:)
      - One coin has been removed from your money pouch.
      - **The Barmaid:** There you go, my little barnacle, nice and frothy.
      - [You buy a poorly poured beer, missing most of its head.]
      - (previous|PreviousOptions)
    - (Condition: If player has no coins)
      - **The Barmaid:** Poor little octopus. You don't have even the coin to buy a beer. Times must be tough around here.
      - (previous|PreviousOptions)
  - [Choice]: I better be going. Things to do.
    - **The Barmaid:** You take care, now.

### Last Orders random event

- (see|Player-owned port/Random events#Last Orders)

### Reminder

- Rumour has it that Surula the barmaid has some juicy gossip for you.
{{Player-owned port}}
{{DEFAULTSORT|Barmaid, The}}
