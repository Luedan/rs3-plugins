# Ogre boat

- **Original Wiki Page**: [Transcript:Ogre boat](https://runescape.wiki/w/Transcript%3AOgre%20boat)
- **Letter**: `O`

---

## Dialogue Transcript


### At the Feldip Hills

- **Bugs:** Dad says you can get a lift to Karamja with us if you want? But you's gives us two chompy first!
- [Menu]: Select an option
  - [Choice]: Yes please, I'll get a lift to Karamja with you.
    - (Condition: If the player does not have two chompies:)
      - **Ogre boat:** You's got no chompies...no boatsie trips!
    - (Condition: If the player has sufficient payment:)
    - (removes=two cooked chompies)
      - {{Qact|Player is transported west of Tai Bwo Wannai.}}
      - The barely sea-worthy log arrives at Karamja beach.
  - [Choice]: No thanks.
    - **Player:** No thanks.

### At Karamja

- **Bugs:** Dad says you can get a lift back with us if you want? But you's gives us two glug-glugs herbies first!
- [Menu]: Select an option
  - [Choice]: Yes please, I'll get a lift back with you.
    - (Condition: If the player is carrying any Karamjan rum:)
      - **Bugs:** Dad sez yous not bringin' da rummy stuff...das bad stuffsies un we get in big bads.
    - (Condition: If the player does not have two clean snake weed or two clean rogue's purse:)
      - **Ogre boat:** You's got no glug-glugs herbies...no boatsie trips!
    - (Condition: If the player has sufficient payment:)
      - (removes=two herbs)
      - You hand over two herbs and accept a ride from Fycie and Bugs on the makeshift boat.
      - {{Qact|Player is transported to eastern Feldip Hills.}}
      - The barely sea-worthy log arrives at the Feldip Hills.
  - [Choice]: What are 'glug-glugs herbies'?|cond=If previously not selected the option:
    - **Bugs:** Glug-glugs herbies! You know! Da thiefy-bag herbie or da snakey-weeed herbie!
    - **Player:** Wait, you mean rogue's purse or snake weed?
    - Yeah! Dem! Now dad says you can get a lift back with use if you want. But you's gives us two dem herbies first!
    - (initial)
  - [Choice]: What herbies did you want again?|cond=If previously selected the above option:
    - (above)
  - [Choice]: No thanks.
    - **Player:** No thanks.
