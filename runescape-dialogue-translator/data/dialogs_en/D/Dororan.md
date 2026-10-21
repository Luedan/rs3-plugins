# Dororan

- **Original Wiki Page**: [Transcript:Dororan](https://runescape.wiki/w/Transcript%3ADororan)
- **Letter**: `D`

---

## Dialogue Transcript


### Before Gunnar's Ground, at the Gunnarsgrunn gate

- (see|Gunnar's Ground)

### After Gunnar's Ground, at the Leptoc manor


#### Before engraving the ruby bracelet

- **Dororan:** Come in, my friend, come in! There is another matter I could use your assistance with.
- [Menu]: Select an Option
  - [Choice]: What is it?
    - **Dororan:** I have some more jewellery for Gudrun and I need your help to engrave them.
    - [Menu]: Select an Option
      - [Choice]: What's the first piece?
        - **Dororan:** A magnificent ruby bracelet.
        - {{anchor|with-beauty-blessed}}**Dororan:** 'With beauty blessed.'
        - [Menu]: Select an Option
          - [Choice]: Engrave the bracelet.
            - (Condition: Without at least level 42 Crafting:)
              - [You need a Crafting level of at least 42 to engrave the ruby bracelet.]
              - **Dororan:** That's a shame. Maybe you can try again another time.
            - (Condition: With at least level 42 Crafting:)
              - You gained 2000 Crafting XP.
              - [You carefully engrave 'With beauty blessed' onto the ruby bracelet.]
              - **Dororan: ** Magnificent! Outstanding! I will give this to her immediately. Please, come back when you have time.
          - [Choice]: Don't engrave the bracelet.
            - **Dororan:** That's a shame. Maybe you can try again another time.
      - [Choice]: I want to talk about something else.
        - (below|something-else)
      - [Choice]: I don't have time right now.
        - (end)
  - [Choice]: I want to talk about something else.{{anchor|something-else}}
    - **Dororan:** What can I do for you?
    - [Menu]: Choose an option:
      - [Choice]: How are things?
        - **Dororan:** Every morning I wake to sunshine and birdsong! Life is marvellous!
        - [Menu]: Select an Option
          - [Choice]: I want to talk about something else.
            - (above|something-else)
          - [Choice]: Goodbye.
            - **Dororan:** Goodbye!
      - [Choice]: This is a very large house.
        - **Dororan:** I know! I don't know where Gunthor would have got such a thing. Maybe Gudrun has some idea.
        - (continuea|something-else-sub-options)
      - [Choice]: I'd like to see the poem you wrote for Gunthor.
        - (Condition: Without space in backpack:)
          - [You don't have room for the poem.]
        - (Condition: With space in backpack:)
          - [Dororan gives you a copy of the poem.]
          - (receives=Gunnar's Ground)
          - **Dororan:** There you go!
      - [Choice]: cond=Having lost the swanky boots:|I seem to have mislaid my swanky boots.
        - **Player:** I seem to have mislaid my swanky boots.
        - (Condition: If free pairs of swanky boots can still be claimed:)
          - **Dororan:** Not to worry! There are some left. Here you go.
          - (Condition: Without space in backpack:)
            - [You don't have room for the boots.]
          - (Condition: With space in backpack:)
            - [Dororan gives you some more boots.]
            - (receives=swanky boots)
            - **Dororan:** Be more careful with these ones! I don't have an infinite supply.
        - (Condition: If all 12 free pairs of swanky boots have been claimed:)
          - **Dororan:** You've exhausted my supply of boots!
          - **Dororan:** I could rustle up another pair for you, but I'd have to trade for them.
          - **Dororan:** I have been thinking of giving Gudrun a ruby ring. If you bring me one, I'll trade it for some more boots.
          - [Menu]: Choose an option:
            - [Choice]: cond=Without a ruby ring in backpack:|I don't have one with me.
              - (end)
            - [Choice]: cond=With a ruby ring in backpack:|Here's a ruby ring.
              - [You trade Dororan a ruby ring for the boots.]
              - (removes=ruby ring) (receives=swanky boots)
            - [Choice]: No thanks.
              - (end)
      - [Choice]: Goodbye.
        - **Dororan:** Goodbye!
  - [Choice]: I don't have time right now.
    - (end)

##### After declining to engrave the ruby bracelet

- **Dororan:** Do you want to try engraving the ruby bracelet again?
- [Menu]: Select an Option
  - [Choice]: What do you want engraved on it?
    - (above|with-beauty-blessed)
  - [Choice]: I want to talk about something else.
    - (above|something-else)
  - [Choice]: I don't have time right now.
    - (end)

#### After engraving the ruby bracelet

- **Dororan:** I have another piece of jewellery to engrave.
- [Menu]: Select an Option
  - [Choice]: What's this one?
    - **Dororan:** A fine dragonstone necklace.
    - **Dororan:** There's not much room...how about just 'Gudrun'?
    - [Menu]: Select an Option
      - [Choice]: Engrave the necklace.
        - (Condition: Without at least level 72 Crafting:)
          - [You need a Crafting level of at least 72 to engrave the dragonstone necklace.]
          - **Dororan:** That's a shame. Maybe you can try again another time.
        - (Condition: With at least level 72 Crafting:)
          - You gained 10,000 Crafting XP.
          - [You skilfully engrave 'Gudrun' onto the dragonstone necklace.]
          - **Dororan:** Another astonishing piece of work! Please, come back later to see if I have other crafting tasks.
      - [Choice]: Don't engrave the necklace.
        - **Dororan:** That's a shame. Maybe you can try again another time.
  - [Choice]: I want to talk about something else.
    - (above|something-else)
  - [Choice]: I don't have time right now.
    - (end)

##### After declining to engrave the dragonstone necklace

- **Dororan:** Do you want to try engraving the dragonstone necklace again?
- [Menu]: Select an Option
  - [Choice]: What do you want engraved on it?
    - (above|just-gudrun)
  - [Choice]: I want to talk about something else.
    - (above|something-else)
  - [Choice]: I don't have time right now.
    - (end)

#### After engraving the dragonstone necklace

- **Dororan:** I have one last piece of jewellery to engrave.
- [Menu]: Select an Option
  - [Choice]: What is it?
    - **Dororan:** An onyx amulet!
    - {{anchor|most-beautiful}}**Dororan:** 'The most beautiful girl in the room.'
    - [Menu]: Select an Option
      - [Choice]: Engrave the amulet.
        - (Condition: Without at least level 90 Crafting:)
          - [You need a Crafting level of at least 90 to engrave the onyx amulet.]
          - **Dororan:** That's a shame. Maybe you can try again another time.
        - (Condition: With at least level 90 Crafting:)
          - Congratulations! You have completed: 'Gunning for Jewellery' - Engrave all of Dororan's jewellery.
          - You gained 20,000 Crafting XP.
          - [You expertly engrave 'The most beautiful girl in the room' onto the onyx amulet.]
          - **Dororan:** That's fantastic! Excellent work.
      - [Choice]: Don't engrave the amulet.
        - **Dororan:** That's a shame. Maybe you can try again another time.
  - [Choice]: I want to talk about something else.
    - (above|something-else)
  - [Choice]: I don't have time right now.
    - (end)

##### After declining to engrave the onyx amulet

- **Dororan:** Do you want to try engraving the onyx amulet again?
- [Menu]: Select an Option
  - [Choice]: What do you want engraved on it?
    - (above|most-beautiful)
  - [Choice]: I want to talk about something else.
    - (above|something-else)
  - [Choice]: I don't have time right now.
    - (end)

#### After engraving the onyx amulet

- **Dororan:** Thanks so much for everything you've done for us!
- (continuea|something-else)
