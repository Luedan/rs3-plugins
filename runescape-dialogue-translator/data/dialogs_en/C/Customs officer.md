# Customs officer

- **Original Wiki Page**: [Transcript:Customs officer](https://runescape.wiki/w/Transcript%3ACustoms%20officer)
- **Letter**: `C`

---

## Dialogue Transcript


### Standard dialogue


#### Before Pirate's Treasure

- **Customs officer:** Can I help you?
- [Menu]: Select an option
  - [Choice]: Can I journey on this ship?
    - **Player:** Can I journey on this ship?
    - **Customs officer:** You need to be searched before you can board.
    - [Menu]: Select an option
      - [Choice]: Why?
        - **Player:** Why?
        - **Customs officer:**  Because Asgarnia has banned the import of intoxicating spirits.
        - (other)
      - [Choice]: Search away, I have nothing to hide.
        - **Player:** Search away, I have nothing to hide.
        - ''(If you have Karamjan rum in inventory:) {{anchor|aha}}
          - **Customs officer:**  Aha, trying to smuggle rum are we?
          - **Player:** {{anchor|personaluse}}Umm... it's for personal use?
          - (removes=Karamjan rum)
          - The customs officer confiscates your rum.
        - ''(If you have Karamjan rum in inventory and are wearing a ring of Charos (a):)
          - **Customs officer:**  Aha, trying to smuggle rum are we?
          - [Menu]: Select an option
            - [Choice]: Umm... it's for personal use?
              - (above|personaluse)
            - [Choice]: [Charm] This is not the Karamjan rum you're looking for.
              - **Player:** This is not the Karamjan rum you're looking for.
              - **Customs officer:** This is not the Karamjan rum we are looking for.
              - **Player:** Well that was easy!
              - You dance for joy...
              - ...and accidentally drop the rum.
              - (removes=Karamjan rum)
              - **Player:** Drat...
        - ''(If you do not have Karamjan rum in inventory:)
          - **Customs officer:** Well, you've got some odd stuff, but it's all legal. Now you need to pay a boarding charge of 30 coins.
          - [Menu]: Select an option {{anchor|30coins}}
            - [Choice]: Ok.
              - **Player:** Ok.
              - ''(If the player does not have enough money:)
                - **Player:** Oh dear, I don't seem to have enough money.
                - You can not afford that.
              - ''(If the player has earned Karamja gloves:)
                - **Customs officer:** Hang on a sec, didn't you earn Karamja gloves? I thought I'd seen you helping around the island. You can go on half price, mate.
                - You pay 15 coins and board the ship.
              - ''(Without Karamja gloves:)
                - You pay 30 coins and board the ship.
              - {{Qact|Screen fades in and out, the player arrives at Port Sarim}}
              - The ship arrives at Port Sarim.
            - [Choice]: Oh, I'll not bother then.
              - **Player:** Oh, I'll not bother then.
            - [Choice]: (*If wearing a ring of Charos (a):*) [Charm] Or perhaps you could let me travel for free?
              - **Player:** Or perhaps you could let me travel for free?
              - **Customs officer:** Yes, perhaps I could. Okay, jump aboard then.
              - {{Qact|Screen fades in an out, the player arrives at Port Sarim}}
              - The ship arrives at Port Sarim.
      - [Choice]: You're not putting your hands on my things!
        - **Player:** You're not putting your hands on my things!
        - **Customs officer:**  You're not getting on this ship then.
  - [Choice]: Does Karamja have unusual customs then?
    - **Player:** Does Karamja have unusual customs then?
    - **Customs officer:** I'm not that sort of customs officer.

#### After Pirate's Treasure

- **Customs officer:** Can I help you?
- Select an option
  - [Choice]: Can I journey on this ship?
    - **Player:** Can I journey on this ship?
    - ''(If you do not have Karamjan rum in inventory:)
      - **Customs officer:** Hey, I know you, you work at the plantation.
      - **Customs officer:** I don't think you'll try smuggling anything, you just need to pay a boarding charge of 30 coins.
      - (continuea|30coins)
    - ''(If you have Karamjan rum in inventory:)
      - **Customs officer:** Spot inspection. You don't mind do you?
      - **Customs officer:** Aha, trying to smuggle rum eh?
      - (continuea|aha)
  - [Choice]: Does Karamja have unusual customs then?
    - (above)

### Pay fare

- *(If you have completed the Karamja easy tasks but do not have 15 coins:)*
  - You can not afford that.
  - You do not have enough coins to pay passage. You need 15 coins as you have earned the Karamja gloves.
- ''(Without the Karamja easy tasks, and without 30 coins:)
  - You can not afford that.
  - You do not have enough coins to pay passage, you need 30.
- *(If you have completed the Karamja easy tasks:)*
  - The officer smiles as she recognises you as having earned Karamja gloves and so lets you pass for half price - 15 coins.
- ''(Without the Karamja easy tasks:)
  - You pay 30 coins and board the ship.
- ''(With Karamjan rum in inventory:)
  - **Customs officer:** Spot inspection. You don't mind do you?
  - **Customs officer:** Aha, trying to smuggle rum eh?
  - (continuea|aha)
