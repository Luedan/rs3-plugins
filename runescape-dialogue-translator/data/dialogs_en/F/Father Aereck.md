# Father Aereck

- **Original Wiki Page**: [Transcript:Father Aereck](https://runescape.wiki/w/Transcript%3AFather%20Aereck)
- **Letter**: `F`

---

## Dialogue Transcript


### Standard dialogue

- (Condition: Before The Restless Ghost:)
  - **Father Aereck:** Welcome to the church of holy Saradomin.
  - (continue)
- (Condition: After The Restless Ghost:)
  - **Father Aereck:** Welcome back to the church of holy Saradomin, my friend! What can I do for you today?
  - (continue)
- [Menu]: What would you like to say?
  - [Choice]: cond=With a construction contract for Father Aereck:|Ask about your construction contract.
    - [Menu]: Select an option
      - [Choice]: What do you need repairing?
        - **Father Aereck:** Let me see, right now I need you to repair the following pieces of furniture.
        - **Father Aereck:** [Furniture 1], [Furniture 2], [Furniture 3], [Furniture 4], [Furniture 5]
        - (previous)
      - [Choice]: What materials do I need?
        - **Father Aereck:** You need: Planks x [number], Steel nails x [number], [Additional material] x [number]
        - (previous)
      - [Choice]: [Leave]
        - (end)
  - [Choice]: cond=Before The Restless Ghost:|I'm looking for a quest! {{anchor|quest}}
    - (see|The Restless Ghost)
  - [Choice]: cond=After The Restless Ghost:|Can you change my gravestone now? {{anchor|gravestone}}
    - **Father Aereck:** Certainly. All proceeds are donated to the Varrockian Guards' Widows & Orphans Fund.
    - {{qact|Gravestone interface opens}}
  - {{anchor|saradomin}}
  - [Choice]: Who's Saradomin?
    - **Father Aereck:** Surely you have heard of our god, Saradomin?
    - **Father Aereck:** He who created the forces of goodness and purity in this world? I cannot believe your ignorance!
    - **Father Aereck:** This is the god with more followers than any other...at least in this part of the world.
    - **Father Aereck:** He defeated the evil Zamorak in the battle of Lumbridge nearby, and he defends us from evil!
    - [Menu]: Select an option
      - [Choice]: Oh, THAT Saradomin.
        - **Father Aereck:** There is only one Saradomin.
        - **Player:** Yeah. I, uh, thought you said something else.
      - [Choice]: Oh, sorry, I'm not from this world.
        - **Father Aereck:** ...
        - **Father Aereck:** That's...strange.
        - **Father Aereck:** I thought things not from this world were all, you know, slime and tentacles.
        - [Menu]: Select an option
          - [Choice]: Not me.
            - **Father Aereck:** Well, I can see that. Still, there's something special about you.
            - **Player:** Thanks, I think.
          - [Choice]: I am! Do you like my disguise?
            - **Father Aereck:** Argh! Avaunt, foul creature from another dimension! Avaunt! Begone in the name of Saradomin!
            - **Player:** Okay, okay, I was only joking!
      - [Choice]: Can you tell me about the battlefield?
        - (continue|battlefield)
  - [Choice]: Nice place you've got here. {{anchor|place}}
    - **Father Aereck:** It is, isn't it? It was built over two centuries ago.
  - [Choice]: cond=With a clay ring:|Can you bless my ring?
    - **Father Aereck:** Ah, you wish to show your devotion to Saradomin by dedicating a ring to him? Very well, it would be my pleasure to assist.
    - (removes=clay ring) (receives=ring of devotion)
    - (Condition: If the Bless Is More achievement hasn't been completed:)
      - {{RSFontAchievement|Bless Is More}}
      - (continue)
    - [Father Aereck inscribes the symbol of Saradomin on your ring's signet face, and offers a brief benediction over it.]
  - [Choice]: Can you tell me about the crater? {{anchor|battlefield}}
    - **Father Aereck:** Ah, Lumbridge Battlefield - the site of the return of Saradomin! That was a momentous day for the church, and I was there!
    - **Father Aereck:** In a titanic battle that lasted for months, the mighty Saradomin drove back the forces of Zamorak to the Underworld where they belong.
    - **Father Aereck:** And now Saradomin is here, we can be sure that we will be safe under his divine protection.
    - **Father Aereck:** All praise Saradomin!

### Historical dialogue during the Battle of Lumbridge

- (Condition: Before The Restless Ghost:)
  - **Father Aereck:** Welcome to the church of holy Saradomin.
  - (continue)
- (Condition: After The Restless Ghost:)
  - **Father Aereck:** Welcome back to the church of holy Saradomin, my friend! What can I do for you today?
  - (continue)
- [Menu]: What would you like to say?
  - [Choice]: I'm looking for a quest!
    - (above|quest)
  - [Choice]: Can you change my gravestone now?
    - (above|gravestone)
  - [Choice]: Who's Saradomin?
    - (above|saradomin)
  - [Choice]: Nice place you've got here.
    - (above|place)
  - [Choice]: Can you tell me about the battlefield?
    - **Father Aereck:** Lumbridge battlefield is where Saradomin himself is currently fighting Zamorak! Thank goodness that he is here! If he'd not shown up when he did, we'd all be thralls of Zamorak now! But he came to us from far away in our time of need, and even now he fights evil on Lumbridge Battlefield. Oh, you must be on your way to Saradomin's war camp in order to help out. It's to the northwest of here. We cannot let evil conquer! Good luck! And may Saradomin be with you!
