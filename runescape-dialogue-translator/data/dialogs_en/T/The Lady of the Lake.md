# The Lady of the Lake

- **Original Wiki Page**: [Transcript:The Lady of the Lake](https://runescape.wiki/w/Transcript%3AThe%20Lady%20of%20the%20Lake)
- **Letter**: `T`

---

## Dialogue Transcript

{{Incomplete|Check initial dialogue before earning Excalibur, check dialogue for 'Excalibur' option after destroying it}}

### Talk to

- **The Lady of the Lake:** Good day to you, [sir/madam].
- [Menu]: What would you like to say?
  - [Choice]: cond=With Excalibur in the backpack and without previously enhancing it:|Sir Kay said you'd reward me.
    - **Player:** Sir Kay said you'd reward me.
    - **The Lady of the Lake:** Indeed, I hear that you have earned his trust. You shall be rewarded handsomely!
    - (removes=Excalibur|receives=enhanced Excalibur)
    - [The Lady of the Lake reaches out and touches the blade Excalibur which seems to vibrate with new power.]
    - **Player:** What does that do then?
    - **The Lady of the Lake:** The enhanced Excalibur is wielded in your left hand, not your right, and its blade is far more powerful.
    - **Player:** Thanks!
  - [Choice]: cond=With Excalibur in the backpack and having previously enhanced it:|Can you enchant Excalibur for me, please?
    - **Player:** Can you enchant Excalibur for me, please?
    - (removes=Excalibur|receives=enhanced Excalibur)
    - [The Lady of the Lake reaches out and touches the blade Excalibur which seems to vibrate with new power.]
  - [Choice]: cond=With Excalibur having previously been obtained:|Who are you?
    - **Player:** Who are you?
    - **The Lady of the Lake:** I am the Lady of the Lake.
  - [Choice]: cond=If Excalibur was destroyed or lost:|I seek the sword Excalibur.
    - **Player:** I seek the sword Excalibur.
    - **The Lady of the Lake:** I recall you have already proven yourself to be worthy of wielding it. I shall return it to you if you can prove yourself to still be worthy.
    - **Player:** And how can I do that?
    - **The Lady of the Lake:** Why, by proving yourself to be above material goods.
    - **Player:** ... And how can I do that?
    - **The Lady of the Lake:** 500 coins ought to do it.
    - [Menu]: What would you like to say?
      - [Choice]: Okay, here you go.
        - **Player:** Okay, here you go.
        - **The Lady of the Lake:** Thanks for the cash! I'm saving up for a new dress.
        - [Menu]: Which version of Excalibur would you like back?
          - [Choice]: Excalibur - the original.
            - (removes=500 coins|receives=Excalibur)
            - [The Lady of the Lake hands you Excalibur.]
          - [Choice]: Enhanced Excalibur.
            - (removes=500 coins|receives=enhanced Excalibur)
            - [The Lady of the Lake hands you the enhanced version of Excalibur.]
      - [Choice]: 500 coins? No thanks!
        - **Player:** 500 coins? No thanks!
        - **The Lady of the Lake:** Your materialistic attitude saddens me.
  - [Choice]: Good day.
    - **Player:** Good day.

### Excalibur

- (Condition: With Excalibur in the backpack:)
  - (above|rewardme)
- (Condition: Having lost Excalibur:)
  - {{Transcript missing}}
- (Condition: If the player's backpack is full:)
  - **The Lady of the Lake:** You're going to drop it if I try to hand it to you while your inventory's full!
- [Menu]: Pay 500 coins for Excalibur?
  - [Choice]: Buy Excalibur.
    - (removes=500 coins|receives=Excalibur)
    - [The Lady of the Lake hands you Excalibur.]
  - [Choice]: Cancel.
    - (end)
