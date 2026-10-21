# Trader Crewmember

- **Original Wiki Page**: [Transcript:Trader Crewmember](https://runescape.wiki/w/Transcript%3ATrader%20Crewmember)
- **Letter**: `T`

---

## Dialogue Transcript


### Standard dialogue

- **Trader Crewmember:** Can I help you?
- [Menu]: Choose an option:
  - [Choice]: Yes, who are you?
    - **Player:** Yes, who are you?
    - **Trader Crewmember:** I'm one of Trader Stan's crew; we are all part of the largest fleet of trading and sailing vessels to ever sail the seven seas.
    - **Trader Crewmember:** If you want to get to a port in a hurry then you can charter one of our ships to take you there - if the price is right...
    - **Player:** So, where exactly can I go with your ships?
    - **Trader Crewmember:** We run ships from Port Phasmatys over to Port Tyras, stopping at Port Sarim, Catherby, Brimhaven, Karamja, the Shipyard, Oo'glog and Port Khazard.
    - **Trader Crewmember:** We might dock at Mos Le'Harmless once in a while, as well, if you catch my meaning...
    - **Player:** Wow, that's a lot of ports. I take it you have some exotic stuff to trade?
    - **Trader Crewmember:** We certainly do! We have access to items bought and sold from around the world.
    - **Trader Crewmember:** Would you like to take a look?
    - [Menu]: Select an option
      - [Choice]: Yes
        - **Player:** Yes.
        - (opens=Trader Stan's Trading Post)
      - [Choice]: No
        - **Player:** No.
        - **Trader Crewmember:** Well, that's fine, would you like to charter a ship instead?
        - [Menu]: Select an option
          - [Choice]: Yes, I would like to charter a ship.
            - (below|charter)
          - [Choice]: No.
            - (end)
      - [Choice]: Isn't it tricky to sail about in those clothes?
        - **Player:** Isn't it tricky to sail about in those clothes?
        - **Trader Crewmember:** Tricky? Tricky!
        - **Trader Crewmember:** With all due credit, Trader Stan is a great employer, but he insists we wear the latest in high fashion even when sailing.
        - **Trader Crewmember:** Do you have even the slightest idea how tricky it is to sail in this stuff?
        - **Trader Crewmember:** Some of us tried tearing it and arguing that it was too fragile to wear when on a boat, but he just had it enchanted to re-stitch itself.
        - **Trader Crewmember:** It's hard to hate him when we know how much he shells out on this gear, but if I fall overboard because of this getup one more time, I'm going to quit.
        - **Player:** Wow, that's kind of harsh.
  - [Choice]: Talk about charter ships. {{anchor|charter}}
    - (Condition: If the player has confirmation turned off:)
      - [Menu]: Choose an option:
        - [Choice]: Charter a ship
          - (below)
        - [Choice]: Confirm payments
          - **Player:** Could you warn me again before I travel on your charter ships?
          - **Trader Crewmember:** Certainly Player, I've informed the rest of the crewmembers to check you're sure you want to travel in future.
          - **Trader Crewmember:** Was there anything else?
          - **Player:** Yes, I would like to charter a ship.
          - **Trader Crewmember:** Certainly sir, where would you like to go?
          - ((Charter Ship destination interface opens.))
    - (Condition: Otherwise:)
      - **Player:** Yes, I would like to charter a ship.
      - **Trader Crewmember:** Certainly [sir/madam], where would you like to go?
      - (Condition: If the player has a bedsheet:)
        - **Trader Crewmember:** Sorry, we  a laundry ship, you'll need to leave those dirty bedsheets behind.
        - **Player:** Would you let me bring it if I told you it was a security blanket?
        - **Trader Crewmember:** No, then we would just mock you.
        - **Player:** Ah, I see.
      - (Condition: If the player has a slime-covered bedsheet:)
        - **Trader Crewmember:** Is that your bedsheet covered in filthy slime?
        - **Player:** I can say in all honesty that it is not.
        - **Trader Crewmember:** Well whoever it belongs to, it's not coming on this ship!
      - (Condition: Otherwise:)
        - ((Charter Ship destination interface opens.))
