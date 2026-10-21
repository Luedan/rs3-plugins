# Rich Bunny

- **Original Wiki Page**: [Transcript:Rich Bunny](https://runescape.wiki/w/Transcript%3ARich%20Bunny)
- **Letter**: `R`

---

## Dialogue Transcript


### Talk to

- (Condition: Initially:)
  - **Rich Bunny:** Well hello there, Player!
  - **Player:** How do you know my name?
  - **Rich Bunny:** Oh, I hear word of all the adventurers who come to visit our wonderful Burrow. Have you come to marvel at the wonders of carrot boats?
  - **Player:** I think so?
  - (continue|Rich-Bunny-options)
- (Condition: Afterwards:)
  - **Rich Bunny:** Good day, Player! Come to take my carrot boats for a spin?
  - (continue|Rich-Bunny-options)
- [Menu]: Select an Option|anchor=Rich-Bunny-options
  - [Choice]: What's going on here?
    - **Player:** What's going on here?
    - **Rich Bunny:** I've come down to visit my dear old brother for the springtime season, and thought this would be the most fabulous opportunity in which to test out my latest creation - carrot boats!
    - **Rich Bunny:** The ultra-nutritious soil here allows for quick iterations of new models, and the swathes of bushy-eyed adventurers make for ripe test sailors.
    - **Player:** Hold on - test sailors? Boats made out of rot-able vegetables? I'm not sure I'm on board with this.
    - **Rich Bunny:** Oh, Player! There really is little to worry about. My team have done plenty of rigorous durability and safety tests earlier on in development. I'd never promote anything I wouldn't use myself!
    - **Player:** Alright, that was enough to convince me. Sign me up!
    - **Rich Bunny:** Wonderful!
    - (previous|Rich-Bunny-options)
  - [Choice]: Tell me more about boating.
    - **Player:** So, what does boating involve?
    - **Rich Bunny:** For starters, my team and I have gone to the effort of placing some obstacles around the lake. There are hoops, slaloms, ramps, and half-pipes, all of which you can train Agility on.
    - **Rich Bunny:** But that's not all! Every 30 minutes, you can also take part in the Blooming Burrow race. I start setting these up on the hour and half past the hour, with the races properly kicking off at five minutes later.
    - (previous|Rich-Bunny-options)
  - [Choice]: What can I get in return?
    - **Player:** What can I get in return? I'd rather not be a lab bunny in one of your carrot boats for free.
    - **Rich Bunny:** Oh, dear Player! I would never ask you for free labour!
    - **Rich Bunny:** In addition to Agility experience, I will personally make sure that you're paid in spring tokens for your endeavors.
    - **Rich Bunny:** I've also commissioned some unique golden, silver, and bronze titles, and skins for your carrot boat, should you finish a boat race in good time.
    - (previous|Rich-Bunny-options)
  - [Choice]: Can I customise my boat?
    - **Player:** Can I customise my boat?
    - **Rich Bunny:** Of course! You can be the most stylish carrot boater around with my custom-made boat decorations.
    - ((Boat customisations interface opens with the following tooltips.))
      - (Condition: Locked customisations:)
        - ((Bronze:))
          - {{Interface tooltip|Bronze skin<br>{{Colour|#EB2F2F|This can be unlocked by completing a boat race in 2 minutes.}}}}
        - ((Silver:))
          - {{Interface tooltip|Silver skin<br>{{Colour|#EB2F2F|This can be unlocked by completing a boat race in 1 minute 45 seconds.}}}}
        - ((Gold:))
          - {{Interface tooltip|Gold skin<br>{{Colour|#EB2F2F|This can be unlocked by completing a boat race in 1 minute 30 seconds.}}}}
        - ((Ornament:))
          - {{Interface tooltip|Ornament decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
        - ((Bunting:))
          - {{Interface tooltip|Bunting decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
        - ((Flowers:))
          - {{Interface tooltip|Flowers decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
        - ((Eggs:))
          - {{Interface tooltip|Eggs decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
      - (Condition: Unlocked customisations:)
        - ((Bronze:))
          - {{Interface tooltip|Bronze skin}}
        - ((Silver:))
          - {{Interface tooltip|Silver skin}}
        - ((Gold:))
          - {{Interface tooltip|Gold skin}}
        - ((Ornament:))
          - {{Interface tooltip|Ornament decoration}}
        - ((Bunting:))
          - {{Interface tooltip|Bunting decoration}}
        - ((Flowers:))
          - {{Interface tooltip|Flowers decoration}}
        - ((Eggs:))
          - {{Interface tooltip|Eggs decoration}}
  - [Choice]: Goodbye.
    - **Player:** I'll be off now.
    - **Rich Bunny:** Good day, Player.

### Customise boat

- (above|customise-boat)

### Blooming Burrow race

- ((The following are also shown as regular chat overhead messages:))
  - (Condition: Every minute before the race starts:)
    - {{Colour: {{Colour|#99FF99|The Blooming Burrow race is due to start in [1–5] [minutes/minute]!}}}}
  - (Condition: When the race is starting:)
    - {{Colour: {{Colour|#99FF99|Get ready in...}}}}
    - {{Colour: {{Colour|#99FF99|3...}}}}
    - {{Colour: {{Colour|#99FF99|2...}}}}
    - {{Colour: {{Colour|#99FF99|1...}}}}
    - {{Colour: {{Colour|#99FF99|GO!}}}}
