# Golrie

- **Original Wiki Page**: [Transcript:Golrie](https://runescape.wiki/w/Transcript%3AGolrie)
- **Letter**: `G`

---

## Dialogue Transcript


### In the Gnome Village Dungeon


#### Before Waterfall Quest

- **Golrie:** What are you doing down here?<br>Leave before you get yourself into trouble.

#### After Waterfall Quest

- **Player:** Hello Golrie. How's it going?
- (Condition: With Glarial's pebble in backpack or bank:)
  - **Golrie:** Better now that I'm on the right side of them bars. I hope that pebble helped you out.
  - (continue|cadarn)
- (Condition: Without Glarial's pebble in backpack or bank:)
  - **Golrie:** Better now that I'm on the right side of them bars. Anyhow... It's funny you should show up.
  - **Player:** Why's that?
  - **Golrie:** You know that pebble I gave to you? Well it turned up on the floor in here, would you like it back?
  - [Menu]: Select an Option
    - [Choice]: Yes please.
      - **Player:** Yes please.
      - (receives=Glarial's pebble)
      - [Golrie hands you a pebble.]
      - (continue|cadarn)
    - [Choice]: No thank you.
      - **Player:** No thank you.
      - **Golrie:** Alright then, but it's here if you need it.
      - (continue|cadarn)
- (Condition: With Cadarn lineage in backpack or bank:)
  - **Golrie:** Anyway I have lots to do. Them Hob-gobs left my stuff out here in a huge mess.
  - (continue|a-key)
- (Condition: Without Cadarn lineage in backpack or bank:)
  - **Golrie:** Oh... that reminds me... Seeing as you like elven things, I found this.
  - (receives=Cadarn lineage)
  - [Golrie hands you an old book.]
  - (continue|a-key)
- (Condition: With a key in backpack or bank:)
  - **Player:** Well goodbye.
- (Condition: Without a key in backpack or bank:)
  - [Menu]: Select an Option
    - [Choice]: Can I use your key?
      - **Player:** Can I use your key?
      - **Golrie:** If you wanna go in there with them hob-gobs that's your business.
      - (receives=a key)
      - [Golrie hands you a key.]
      - **Player:** Thanks, see you later.
    - [Choice]: Goodbye Golrie.
      - **Player:** Goodbye Golrie.
      - **Golrie:** See you later.

#### After The Path of Glouphrie

- **Player:** Hey Golrie! How are you doing?
- **Golrie:** Hey, Player! Nice of you to come down for a natter. I'm busy sorting the stuff into alpha-numeri-chronological order. Anything I can do for you?
- [Menu]: Select an Option
  - [Choice]: Actually, I came here for Glarial's pebble.
    - (above|After Waterfall Quest)
  - [Choice]: I'll be okay, thanks.
    - **Player:** I'll be okay, thanks.

#### After The Prisoner of Glouphrie

- **Golrie:** Hello, Player. Did you come to tell me about Gramps?
- [Menu]: Select an Option
  - [Choice]: [Talk about Prisoner of Glouphrie]
    - **Golrie:** Player! I can't thank you enough for getting Gramps out of that pickle! You can't imagine the trouble you would have been in if anything had happened to him. Can't believe you left that letter in a book.
    - **Player:** It's okay, Golrie. It all worked out in the end. Although, I'm fairly certain your granddad hasn't given up with his plans to bring down Glouphrie and Arposandra. Keep an eye on him and make sure he doesn't go and do anything silly, will you?
    - **Golrie:** Mum will help with that, don't you worry. I'll keep doing what I do. You know, cataloguing and stuff.
    - **Player:** I heard your mum's staying around the village now, to train as a tree whisperer. Your mum is full of surprises.
    - **Golrie:** Yeah? Well, your mum...
    - **Golrie:** Naah, just kidding!
    - **Golrie:** Anyway! Thanks again, Player! I'll see you around!
    - **Player:** Bye!
  - [Choice]: Actually, I came here for Glarial's pebble.
    - **Player:** Actually, I came here for Glarial's pebble.
    - (Condition: With Glarial's pebble in backpack or bank:)
      - **Golrie:** I haven't seen it recently. I assume you have it?
      - **Player:** Indeed! Thank you.
      - (continue|cadarn)
    - (Condition: Without Glarial's pebble in backpack or bank:)
      - **Golrie:** You're in luck: someone threw it at me the other day.
      - (receives=Glarial's pebble)
      - [Golrie hands you a pebble.]
      - (continue|cadarn2)
    - (Condition: Without Cadarn lineage in backpack or bank:)
      - **Golrie:** Oh... that reminds me: seeing as you are an elfophile, I found this.
      - (receives=Cadarn lineage)
      - [Golrie hands you an old book.]
      - (continue|a-key2)
    - (Condition: With a key in backpack or bank:)
      - **Player:** Goodbye Golrie.
      - **Golrie:** See you later.
    - (Condition: Without a key in backpack or bank:)
      - [Menu]: Select an Option
        - [Choice]: Can I use your key?
          - **Player:** Can I use your key?
          - **Golrie:** If you wanna go in there with them hob-gobs that's your business.
          - (receives=a key)
          - [Golrie hands you a key.]
          - **Player:** Thanks, see you later.
        - [Choice]: Goodbye Golrie.
          - **Player:** Goodbye Golrie.
          - **Golrie:** See you later.
