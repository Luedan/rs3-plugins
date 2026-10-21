# Palmer (The Beach)

- **Original Wiki Page**: [Transcript:Palmer (The Beach)](https://runescape.wiki/w/Transcript%3APalmer%20%28The%20Beach%29)
- **Letter**: `P`

---

## Dialogue Transcript


### Normally

- [Menu]: Select an Option
  - [Choice]: cond=Only before asking anything else:|What's going on here?
    - **Palmer:** These coconut trees have some fantastic produce on them, well worth farming them.
    - [Harvesting from the coconut trees gives you farming experience. You can gain extra experience for delivering the coconuts to the coconut shy.]
    - (previous)
  - [Choice]: How are things going?
    - (Condition: Only if not answered like this the last time:)
      - **Palmer:** My lovely bunch of coconuts is keeping me happy, although I would rather that big creature didn't keep popping out of the crater and scaring me.
      - **Palmer:** I thought moving here we would get away from it. But it turns out this is where it lives!
      - (previous)
    - (Condition: Only if answered like above this the last time:)
      - **Palmer:** These coconut trees have some fantastic produce on them, well worth farming them.
      - [Harvesting from the coconut trees gives you farming experience. You can gain extra experience for delivering the coconuts to the coconut shy.]
      - (previous)
  - [Choice]: cond=Only after asking something else:|Bye.
    - **Palmer:** Enjoy your time on the beach.

### Before 2026


#### Normally

- [Menu]: Select an Option
  - [Choice]: cond=Only before asking anything else:|What's going on here?
    - **Palmer:** These coconut trees have some fantastic produce on them, well worth farming them.
    - [Harvesting from the coconut trees gives you farming experience. You can gain extra experience for delivering the coconuts to the coconut shy.]
    - (previous)
    - (Condition: Only if not answered like this the last time:)
      - **Palmer:** My lovely bunch of coconuts is keeping me happy, although I would rather that big creature didn't keep popping out of the crater and scaring me.
      - **Palmer:** What is that thing? Reyna said it is something to do with the energy of the area and that it's tied to here, but I'm not sure that makes me feel any better.
      - (previous)
    - (Condition: Only if answered like above this the last time:)
      - **Palmer:** These coconut trees have some fantastic produce on them, well worth farming them.
      - [Harvesting from the coconut trees gives you farming experience. You can gain extra experience for delivering the coconuts to the coconut shy.]
      - (previous)
  - [Choice]: cond=Only after asking something else:|Bye.
    - **Palmer:** Enjoy your time on the beach.

#### With the Sandy Clue Scroll

- **Palmer:** Oo, a stranger left this for you!
- (Condition: Receiving a scroll box:)
  - (receives=Sandy Scroll box)
  - [scrollbox].}}
- (Condition: Receiving caskets:)
  - (Condition: Without free space in backpack:)
    - You need 1 free space in your backpack to receive your clue caskets.
  - (Condition: With free space in backpack:)
    - (removes=Sandy Clue Scroll)
    - (receives=Sandy Casket and its red version)
    - [You are handed a casket!]
