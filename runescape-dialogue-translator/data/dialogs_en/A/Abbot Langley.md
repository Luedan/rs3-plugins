# Abbot Langley

- **Original Wiki Page**: [Transcript:Abbot Langley](https://runescape.wiki/w/Transcript%3AAbbot%20Langley)
- **Letter**: `A`

---

## Dialogue Transcript

{{dialogue|npc}}
{{transcript npc|Abbot Langley}}

### Standard dialogue

- **Abbot Langley:** Greetings traveller.
- {{tselect|Choose an option:}}
  - {{topt|Can you heal me? I'm injured.}}
    - **Player:** Can you heal me? I'm injured.
    - **Abbot Langley:** Ok.
    - Abbot Langley places his hands on your head. You feel a little better.
  - {{topt|Isn't this place built a bit out the way?}}
    - **Player:** Isn't this place built a bit out the way?
    - **Abbot Langley:** We like it that way actually! We get disturbed less. We still get rather a large amount of travellers looking for sanctuary and healing here as it is!
  - {{topt|cond=If the player has not gained access to the upper level of the Monastery|How do I get further into the Monastery?}}
    - **Player:** How do I get further into the Monastery?
    - **Abbot Langley:** I'm sorry but only members of our order are allowed in the second level of the monastery.
    - {{tselect|Select an Option|anchor=join}}
      - {{topt|Well can I join your order?}}
        - **Player:** Well can I join your order?
        - {{tcond|If the player is below level 31 Prayer:}}
          - **Abbot Langley:** No. I am sorry, but I feel you are not devout enough.
          - You need a prayer level of 31 to join the order.
        - {{tcond|If the player is level 31 Prayer or greater:}}
          - **Abbot Langley:** Ok, I see you are someone suitable for our order. You may join.
      - {{topt|Oh, sorry.}}
        - **Player:** Oh, sorry.

### Attempting to climb a ladder before joining the monastery


#### Eastern ladder

- **Abbot Langley:** Only members of our order can go up there.
- {{tact|continuea|join}}

#### Western ladder

- A nearby monk glares at you. Maybe you should talk to him before climbing the ladder.

### Treasure Trails

- **Abbot Langley:** Congratulations, traveller!
- (removes=the old clue scroll (hard))
- ((If the trail continues:))
  - (receives=a new clue scroll (hard))
  - {{tbox|pic=Clue scroll (hard) detail.png|Abbot Langley has given you another clue scroll.}}
- ((If the trail ends:))
  - (receives=reward casket (hard))
  - {{tbox|pic=Reward casket (hard) detail.png|You've found a casket!}}
