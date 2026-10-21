# Urluk

- **Original Wiki Page**: [Transcript:Urluk](https://runescape.wiki/w/Transcript%3AUrluk)
- **Letter**: `U`

---

## Dialogue Transcript


### Talk to


#### Before The Jack of Spades

- **Urluk:** Hey, Hassan and the leaders were looking for you. Best you talk to them first.
- Complete the Jack of Spades quest to get access to Urluk.

#### After The Jack of Spades

- (Condition: Only on first time:)
  - **Urluk:** I try to give people help and directions around here.
  - **Urluk:** People just make fun of me though.
  - **Player:** What are you talking about? Why would I make fun of you?
  - **Urluk:** Well if I told you that you would make fun of me...
  - **Urluk:** Everyone always makes fun of me behind my back, but camels have brilliant hearing, you know?
  - **Player:** I think I'm starting to see the problem here, I'll get going.
  - **Urluk:** No, wait! They make fun of me because I haven't moved in fifty human years. I just like to sit here and smoke cinchor.
  - **Player:** How have you kept yourself in food and water? I'm not even mad I'm impressed.
  - **Urluk:** Not gonna lie; I store it in my humps. Haven't needed to eat for decades. You seem nice. Need any advice on what to do round here?
  - (continue|initial-options)
- [Menu]: Choose an option: {{anchor|initial-options}}
  - [Choice]: What can I do here?
    - (Condition: Responses cycle through the following:)
      - (Condition: Woodcutting:)
        - **Urluk:** You should try cutting Acadia Trees. You will find them on the raised plateau in the Imperial District, ask a guard if you get lost!
        - **Urluk:** This is a great way to grow your reputation with a faction of your choice.
        - (initial|initial-options)
      - (Condition: Thieving:)
        - **Urluk:** You should try some Thieving in the market place next to us.
        - **Urluk:** You might find that you earn reputation for doing so.
        - (initial|initial-options)
      - (Condition: Fishing:)
        - **Urluk:** You should try fishing some Beltfish in the ports district.
        - **Urluk:** This is a great way to grow your reputation with a faction of your choice.
        - (initial|initial-options)
      - (Condition: Hunter:)
        - **Urluk:** You should go hunt some Plover Birds across the river in Sophanem.
        - **Urluk:** This is a great way to grow your reputation with a faction of your choice.
        - (initial|initial-options)
      - (Condition: Shifting Tombs:)
        - **Urluk:** You should do some Shifting Tombs in any of the four districts. Look for the spire.
        - **Urluk:** This is a great way to grow your reputation with a faction of your choice.
        - (initial|initial-options)
      - (Condition: City Quests:)
        - (Condition: If a City Quest is active:)
          - **Urluk:** Someone around the city was looking for help. I can't remember the name... [NPC] maybe?
          - (initial|initial-options)
        - (Condition: If a City Quest isn't active:)
          - **Urluk:** You should do one of the City Quests. Try a citizen in need to talk to.
          - (initial|initial-options)
      - (Condition: Slayer:)
        - **Urluk:** You should go do some Slayer in the Sophanem Slayer dungeon. Make sure to pick up some feathers of Ma'at from the general store.
        - **Urluk:** This is a great way to grow your reputation with a faction of your choice.
        - (initial|initial-options)
      - (Condition: Divination:)
        - **Urluk:** You should go do some Divination in Sophanem, look for the Luminous Wisps near the river.
        - (initial|initial-options)
      - (Condition: Crafting:)
        - **Urluk:** You should try training your Crafting on the spinning wheel in the Port district.
        - (initial|initial-options)
      - (Condition: Smithing:)
        - **Urluk:** You should try training your Smithing on the furnace and anvil in the Worker or Port districts.
        - (initial|initial-options)
      - (Condition: Cooking and Firemaking:)
        - **Urluk:** You should try training your Cooking or Firemaking on the fire pit in the Worker's district.
        - (initial|initial-options)
  - [Choice]: What should I aim for?
    - (Condition: Responses cycle through the following:)
      - (Condition: Quest:)
        - (Condition: If the player is between 1 and 2 city reputation:)
          - **Urluk:** You could do a quest. You aren't well known enough round these parts to be eligible for one, however.
          - Level 3 Reputation is required for 'Crocodile Tears'.
          - (initial|initial-options)
      - (Condition: No quest:)
        - **Urluk:** I can't think of anything more right now, talk to me in a second!
        - Level 3 Reputation is required for 'Crocodile Tears'.
        - (initial|initial-options)
      - (Condition: If the player is below level 72 Hunter:)
        - **Urluk:** You should go train your Hunter in order to catch plover birds.
        - Level 72 Hunter required to catch plover birds.
        - (initial|initial-options)
      - (Condition: If the player is below level 50 Crafting:)
        - **Urluk:** You should train your Crafting to do Shifting Tombs.
        - Level 50 Crafting required to do Shifting Tombs.
        - (initial|initial-options)
      - (Condition: If the player has not completed Spirits of the Elid quest:)
        - **Urluk:** You could do a quest. The citizens of Nardah are undergoing a drought. That could be something to fix beforehand.
        - Completion of Spirits of the Elid is required for Crocodile Tears.
        - (initial|initial-options)
      - (Condition: If the player is missing any of the below requirements:)
        - (Condition: If the player is below level 88 Slayer:)
          - **Urluk:** You need to improve your slaying to get into the Sophanem Slayer Dungeon.
          - 88 Slayer is required for the Sophanem Slayer dungeon.
        - (Condition: If the player is below level 90 Divination:)
          - **Urluk:** You should improve your divining ability to utilise the colony in Sophanem.
          - 90 Divination is required to harvest the Sophanem luminous wisp colony.
        - (continue|more-things)
      - (Condition: If Urluk has been asked about all the things that can be aimed for:)
        - **Urluk:{{anchor|more-things}}** Hmm, well, here's a few more things you could aim for...but I'll let you discover them yourself.
        - (initial|initial-options)
      - (Condition: Earned Sandy title:)
        - **Urluk:** Oh! You've done a LOT of things in Menaphos. This deserves a greater reward than a mere cape of the palapa!
        - You have unlocked the '{{Coloury}}' title!|colour=#AAC371}}
        - ((Repeated in a pop-up:))
          - You have unlocked the '{{Coloury}}' title!|colour=#AAC371|shadow=no}}
          - (initial|initial-options)
      - (Condition: After obtaining Sandy title:)
        - **Urluk:** You know what? I think you're all good.
        - (initial|initial-options)
  - [Choice]: Can I get your cape?
    - (Condition: If not eligible for the cape:)
      - **Urluk:** The Cape of the Palapa is only for those who have seen the world.
      - **Urluk:** Do a Shifting Tomb as well as trying out the Woodcutting, Thieving, Mining, Fishing and Hunter in Menaphos and Sophanem to recieve{{Sic}} the cape.
    - (Condition: If eligible for the cape:)
      - (Condition: If the cape has not been claimed yet:)
        - Congratulations! You have completed: 'Jack of all Menaphos' - Do a bit of everything in Menaphos and claim the cape of the palapa from Urluk.
        - You have unlocked the cape of the palapa!
        - (continue)
      - **Urluk:** Made out of braided cloth strands. You'll never feel exposed again.
    - (initial|initial-options)
  - [Choice]: Do you have any rumours about City Quests?
    - (Condition: If a City Quest is active:)
      - **Urluk:** Someone around the city was looking for help. I can't remember the name.... [NPC] maybe?
    - (Condition: If a City Quest isn't active:)
      - **Urluk:** You should do one of the city Quests. From time to time a citizen will need help, I guarantee it.
      - (initial|initial-options)
  - [Choice]: How can I understand you?
    - **Urluk:** During my travels, I found an amulet of humanspeak. I have to say it has come in very handy in stopping you lot from attacking me.
    - (initial|initial-options)
