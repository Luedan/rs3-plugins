# Lifeguard

- **Original Wiki Page**: [Transcript:Lifeguard](https://runescape.wiki/w/Transcript%3ALifeguard)
- **Letter**: `L`

---

## Dialogue Transcript


### Talk to


#### When too far away from the north-eastern one

- You need to move closer to the lifeguard to talk.

#### When close enough to the north-eastern one or when talking to any other lifeguard

- (Condition: If Clawdia is absent:)
  - **Lifeguard:** Hey there. How can I help?
  - (continue)
- (Condition: If Clawdia is present:)
  - **Lifeguard:** H-h-hey there. How can I h-help?
  - (continue)
- **Player:** Just wondering how you are doing?
- (Condition: If Clawdia is absent:)
  - **Lifeguard:** I'm doing great. This beach is under my control and I am feeling good.
  - **Lifeguard:** If you are in any danger just shout and I'll be there to help you out.
- (Condition: If Clawdia is present:)
  - **Lifeguard:** You're going to make that thing go away, aren't you? That... that creature.
  - **Player:** Sure, I'll make it go away.
  - **Lifeguard:** Oh, ok, good. Thank you.

### Title progress


#### When too far away from the north-eastern one

- You need to move closer to the lifeguard to talk.

#### When close enough to the north-eastern one or when using any other lifeguard

- Clawdia kills: [number]/15<br>Ice creams eaten: [number]/10

### Announcing the portals (historical)

- *(The applicable line is seen whenever a portal becomes active in addition to a standard overhead message:)*
  - {{Colour: A game of Flish Flingers just opened up!}}
  - {{Colour: A Guthixian cache has just opened up!}}
  - {{Colour: A shooting star just crash landed!}}
  - {{Colour: A sinkhole and big chinchompa entrance have just spawned!}}
  - {{Colour: It looks like something is about to happen in the Wilderness!}}
  - {{Colour: Looks like you're able to get through to the spirit plane now for some Familiarisation!}}
  - {{Colour: There's an evil tree causing total havoc!}}

### Beach stats (historical)

- 2017 title progress<br />Thermometers filled: [number or 25+]<br />Clawdia kills: [number or 50+]<br />Ice creams eaten: [number or 10+]
- 2016 title progress<br />Thermometers filled: [number or 50+]<br />Clawdia kills: [number or 50+]<br />Ice creams eaten: [number or 10+]
- 2015 title progress<br />Thermometers filled: [number or 50+]<br />Clawdia kills: [number or 50+]<br />Ice creams eaten: [number or 10+]

### Northern one with the Sandy Clue Scroll (historical)

- **Lifeguard:** Ah, I found this inside one of my drinks. It's got your name on it!
- (Condition: Receiving a scroll box:)
  - (removes=Sandy Clue Scroll) (receives=Sandy Scroll box)
  - [scrollbox].}}
- (Condition: Receiving caskets:)
  - (Condition: Without free backpack space:)
    - [You need 1 free space in your backpack to receive your clue caskets.]
  - (Condition: With free backpack space:)
    - (removes=Sandy Clue Scroll) (receives=Sandy Casket and its red version)
    - [You are handed a casket!]
