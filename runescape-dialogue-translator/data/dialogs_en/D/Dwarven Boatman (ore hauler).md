# Dwarven Boatman (ore hauler)

- **Original Wiki Page**: [Transcript:Dwarven Boatman (ore hauler)](https://runescape.wiki/w/Transcript%3ADwarven%20Boatman%20%28ore%20hauler%29)
- **Letter**: `D`

---

## Dialogue Transcript


### First conversation

- **Player:** Hello there. I don't think I've seen you here before.
- **Dwarven Boatman:** Oh, Dondakan's employed me recently. He needs a ship to take all his gold to the city.
- **Player:** The city? Can you take me there?
- **Dwarven Boatman:** There is only space on my boat for two things... me, and the gold. But if you want, I can take your gold ore to the city and bring it to the bank.
- **Player:** That's a good service! Will it cost me anything?
- **Dwarven Boatman:** Only a little bit. One piece of gold ore for every shipment, and one piece of gold ore for every five pieces of ore on top of that.
- **Player:** So... if I had ten pieces of ore, how much would you take?
- **Dwarven Boatman:** That would be three pieces. One for the shipment, two for the load. Seven pieces would go into your bank account. So, are you interested?
  - *If the player has exactly one Gold ore with them:*
    - (continue|anchor-one)
  - *If the player has two or more Gold ore with them:*
    - (continue|anchor-two)
  - *If the player does not have any Gold ore with them:*
    - (continue|anchor-none)

### Subsequent conversations:

- **Dwarven Boatman:** Do you have any gold ore that you want me to take to the bank in the city?
- *If the player has exactly one Gold ore with them:{{anchor|anchor-one}}*
  - **Player:** Well, I have this one piece of ore...
  - **Dwarven Boatman:** That wouldn't do  you much good, I'm afraid. My minimum fee is one piece of gold ore, there wouldn't be anything left for you.
- *If the player has two or more Gold ore with them:{{anchor|anchor-two}}*
  - Select an option
    - Yes, please take my gold to the city.
      - **Player:** Yes, please take my gold to the city. I've got [number] pieces of ore right here.
      - **Dwarven Boatman:** Let's see, if I take that to the bank for you, I'd keep [number] for myself and bring [number] to the bank for you. Does that sound fair?
      - Select an option
        - Yes.
          - **Player:** Yes, it does.
          - **Dwarven Boatman:** Excellent, it's been good doing business with you! I'll take these to the city with my next shipment.
          - {{qact|The Dwarven Boatman takes the Player's gold.}}
        - No.
          - **Player:** No, that's far too expensive for me.
    - No, I'll hang on to these myself.
      - **Player:** No, I'll hang on to these myself.
    - *If the player has a Ring of charos (a) equipped:*
      - [Charm] It all seems a bit expensive, really.
        - **Player:** It all seems a bit expensive, really.
        - **Dwarven Boatman:** I don't know... it's just what Dondakan told me, if someone wanted me to ship their gold.
        - **Player:** There's plenty of gold coming from that rock now, surely you can lower the price somewhat?
        - **Dwarven Boatman:** Alright. Tell you what, I'll only keep [number] for myself and bring [number] ores to the bank for you. Deal?
        - Select an option
          - Yes.
            - **Player:** Yes, much appreciated.
            - **Dwarven Boatman:** Excellent, it's been good doing business with you!
            - {{qact|The Dwarven Boatman takes the Player's gold.}}
          - No.
            - **Player:** No, I'll hang on to these myself, thanks.
- *If the player does not have any Gold ore with them:{{anchor|anchor-none}}*
  - **Player:** I don't have any, I'm afraid.
