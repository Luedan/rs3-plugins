# Estocada

- **Original Wiki Page**: [Transcript:Estocada](https://runescape.wiki/w/Transcript%3AEstocada)
- **Letter**: `E`

---

## Dialogue Transcript


### Talking to Estocada

- (Condition: If either variant of duellist's cap has never been claimed:)
  - **Estocada:** Ah, a new face. You are here to fi- Ah yes, I mean...you are here for fashionable attire, yes?
  - [Menu]: Select an Option
    - [Choice]: Yes, that's right.
      - **Player:** Yes, that's right.
      - **Estocada:** Glad to hear it! Then I have something for you.
      - (Condition: If there is no backpack space:)
        - **Estocada:** Once you have the space to carry it that is.
        - (continue|about-hat)
      - (receives=duellist's cap)
      - [Estocada gives you a wide-brimmed hat.]
      - **Estocada:** This hat is rather special, my friend. I don't often give gifts, but, when I do, I prefer to give them to duellists.
      - (continue|about-hat)
    - [Choice]: Erm, no.
      - **Player:** Erm, no.
      - **Estocada:** Oh. You surprise me.
      - (continue)
- (Condition: If either variant of the duellist's cap has been claimed before:)
  - (Condition: If the player has not lost both variants of duellist's cap:)
    - **Estocada:** Ahh, a duellist. Stay victorious, my friend.
    - (continue)
  - (Condition: If the player has lost either variant of duellist's cap:)
    - **Estocada:** My friend, you have not got your hat. Where is it gone to?
    - **Player:** I lost it.
    - **Estocada:** Well, it is not a problem, these things can be overcome.
    - (Condition: If there is no backpack space:)
      - **Estocada:** All you must do is talk to me once there is space to hold this replacement.
      - (continue)
    - (Condition: If the duellist's cap has been lost:)
      - (receives=duellist's cap)
      - (Condition: Before the removal of Duel Arena:)
        - **Estocada:** I don't often replace hats, but, when I do, I choose to replace duellists' caps.
        - (continue)
      - (Condition: After the removal of Duel Arena:)
        - **Estocada:** I don't often replace hats, but, when I do, I choose only the height of fashion.
        - (continue)
    - (Condition: If the antique duellist's cap has been lost and the duellist's cap wasn't just claimed:)
      - (receives=antique duellist's cap)
      - **Estocada:** I don't often replace hats, but, you were a fighter in the old arena. How could I say no?
      - (continue)
    - **Player:** Thanks!
    - (continue)
- [Menu]: Select an Option
  - [Choice]: Tell me more about this hat, then.
    - **Player:** Tell me more about this hat, then.
    - (Condition: Before the removal of Duel Arena:)
      - **Estocada:** All the time you have this hat on your person or in your bank, it will see you win or fall in the Duel Arena and take note. By its magic you can turn into a statue, which shows those who read its plaque how well you have fought - how many you defeat, your win streak, and the like. If you wish to, you can cause the hat to forget all it has seen of your prowess, or instruct it not to show certain elements.
      - (continue)
    - (Condition: After the removal of Duel Arena:)
      - (Condition: Players battled there before:)
        - **Estocada:** The Duel Arena was once a shining symbol of duelling prowess...until it was swallowed by the desert. If you remember the time of the Duel Arena and battled there, this hat will remember also.
        - **Estocada:** By its magic you can turn into a statue, which shows those who read its plaque how well you fought in the arena before it fell - how many you defeated, your win streak, and the like.
        - **Estocada:** If you wish to, you can cause the hat to forget all it has seen of your prowess. Though the Duel Arena may be gone, you may still reclaim glory through duelling other adventurers throughout Gielinor.
        - (continue)
      - (Condition: Players did not battle in Duel Arena:)
        - **Estocada:** The Duel Arena was once a shining symbol of duelling prowess...until it was swallowed by the desert. What little remains lie to the north of here.
        - **Estocada:** Back then, there hats were used to show off your skills - how many you defeated, your win streak, and the like.
        - **Estocada:** Nowadays, they are used to show off your success in duelling fellow adventurers across Gielinor.
        - (continue)
    - **Player:** Handy, thanks!
  - [Choice]: Farewell.
    - **Player:** Farewell.
