# Captain Shanks

- **Original Wiki Page**: [Transcript:Captain Shanks](https://runescape.wiki/w/Transcript%3ACaptain%20Shanks)
- **Letter**: `C`

---

## Dialogue Transcript


### After completing Shilo Village

- **Captain Shanks:** Hello there shipmate! I sail to Khazard Port and to Port Sarim. Where are you bound?
- **Player:** Hmm, I'm interested in a boat trip.
- (Condition: Without a ship ticket:)
  - **Captain Shanks:** I see you don't have a ticket for the ship, my colleague normally only sells them in Shilo village. But I could sell you one for a small additional charge. Shall we say [26-45] gold pieces
    - [Menu]: Buy a ticket for [26-45] gold pieces
      - [Choice]: Yes, I'll buy a ticket for the ship.
        - **Player:** Yes, I'll buy a ticket for the ship.
        - **Captain Shanks:** It's a good deal and no mistake. Here you go me old shipmate, here's your ticket.
        - (receives=Ship ticket) (removes=coins)
        - **Captain Shanks:** Ok, now you have your ticket, do you want to sail anywhere?
        - [Menu]: Captain Shanks asks, 'Do you want to sail anywhere?'
          - [Choice]: Khazard Port please.
            - **Player:** Khazard Port please.{{anchor|Khazard}}
            - (removes=Ship ticket)
            - (The player journeys on the ship and arrives at Port Khazard, near Tindel Marchant.)
            - **Captain Shanks:** Very well then me old shipmate, I'll just take your ticket and then we'll set sail.
          - [Choice]: Port Sarim please.
            - **Player:** Port Sarim please.{{anchor|Sarim}}
            - **Captain Shanks:** Very well then me old shipmate, I'll just take your ticket and then we'll set sail.
            - (removes=Ship ticket)
            - (The player journeys on the ship and arrives at Port Sarim, near the monks of Entrana.)
          - [Choice]: Nowhere just at the moment thanks.
            - **Player:** Nowhere just at the moment thanks.
            - **Captain Shanks:** Very well then me old shipmate, Just let me know if you change your mind.
      - [Choice]: No thanks, not just at the moment.
        - **Player:** No thanks, not just at the moment.
        - **Captain Shanks:** Very well me old shipmate,  come back if you change your mind now.
- (Condition: With a ship ticket:)
  - [Menu]: Captain Shanks asks, 'Where are you bound?'
    - [Choice]: Khazard Port please.
      - (continuea|Khazard)
    - [Choice]: Port Sarim please.
      - (continuea|Sarim)
    - [Choice]: Nowhere just at the moment thanks.
      - **Player:** Nowhere just at the moment thanks.
      - **Captain Shanks:** Very well then me old shipmate, Just let me know if you change your mind.
