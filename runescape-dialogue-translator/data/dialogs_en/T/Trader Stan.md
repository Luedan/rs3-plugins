# Trader Stan

- **Original Wiki Page**: [Transcript:Trader Stan](https://runescape.wiki/w/Transcript%3ATrader%20Stan)
- **Letter**: `T`

---

## Dialogue Transcript


### In Port Sarim


#### Standard dialogue

- **Trader Stan:** Can I help you?
- [Menu]: Choose an option:
  - [Choice]: Yes, who are you?
    - **Player:** Yes, who are you?
    - **Trader Stan:** Why, I'm Trader Stan, owner and operator of the largest fleet of trading ships and chartered vessels to ever sail the seas!
    - **Trader Stan:** If you want to get to a port in a hurry then you can charter one of my ships to take you there - if the price is right...
    - **Player:** So, where exactly can I go with your ships?
    - **Trader Stan:** We run ships from Port Phasmatys over to Port Tyras, stopping at Port Sarim, Catherby, Brimhaven, Musa Point, Oo'glog and Port Khazard.
    - **Trader Stan:** We might dock at Mos Le'Harmless once in a while, as well, if you catch my meaning...
    - **Player:** Wow, that's a lot of ports. I take it you have some exotic stuff to trade?
    - **Trader Stan:** We certainly do! I and my crewmen have access to items bought and sold from around the world.
    - **Trader Stan:** Would you like to take a look?
    - [Menu]: Select an Option
      - [Choice]: Yes
        - **Player:** Yes.
        - (opens=Trader Stan's Trading Post)
      - [Choice]: No
        - **Player:** No.
        - **Trader Stan:** Well, that's fine, would you like to charter a ship instead?
        - [Menu]: Select an Option
          - [Choice]: Yes, I would like to charter a ship.
            - (below|charter)
          - [Choice]: No.
            - (end)
  - [Choice]: Talk about the Skulls pirate, Jed.
    - (Condition: Before Impressing the Locals:)
      - (see|Impressing the Locals)
    - (Condition: After Impressing the Locals:)
      - **Trader Stan:** Go get him, captain!
    - (Condition: After Jed Hunter:)
      - **Player:** Jed's dead, Stan. Jed's dead.
    - (Condition: After Eye for an Eye:)
      - **Player:** Jed's undead, Stan. And now also dead. Again. Properly this time, I think.
  - [Choice]: Talk about charter ships.
    - **Player:{{anchor|charter}}** Yes, I would like to charter a ship.
    - **Trader Stan:** Certainly [sir/madam], where would you like to go?
    - ((Charter Ship destination interface opens.))

#### Treasure Trails


##### Receiving the puzzle box

- **Trader Stan:** Here you are!
- (receives=puzzle box)
- [Trader Stan has given you a puzzle box!]

##### When talked to again without solving the puzzle

- **Trader Stan:** Nope, that's not completed yet.

##### When talked to with the puzzle solved

- (If the trail continues:)
  - (removes=the old clue scroll (hard) and puzzle box) (receives= the new clue scroll (hard))
  - [Trader Stan has given you another clue scroll!]
  - (continue)
- (If the trail ends:)
  - (removes=the old clue scroll (hard) and puzzle box) (receives=reward casket (hard))
  - [You've found a casket!]
  - (continue)
- **Trader Stan:** That's brilliant, you deserve your treasure!
