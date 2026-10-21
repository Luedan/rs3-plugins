# Wythien

- **Original Wiki Page**: [Transcript:Wythien](https://runescape.wiki/w/Transcript%3AWythien)
- **Letter**: `W`

---

## Dialogue Transcript


### Talk to

- **Wythien:** Hey, you. Have any motherlode maw shards left and want some items I grabbed from the motherlode maw before it closed? Ten motherlode shards for one item: can't say fairer than that.
- [Menu]: Select an Option
  - [Choice]: I'm interested.
    - (Condition: With at least 10 motherlode shards:)
      - **Wythien:** Good good. You sure you want to exchange ten shards? I'm not a refunding kind of guy.
      - (continue)
    - (Condition: With less than 10 motherlode shards:)
      - **Wythien:** You'll need ten motherlode shards for your one item. You're a little shy of ten.
      - (continue)
    - [Menu]: Select an Option
      - [Choice]: Yes. {{anchor|accept}}
        - (Condition: With less than 10 motherlode shards:)
          - **Wythien:** Come back to me when you have more motherlode shards. Ten will do.
        - (Condition: With at least 10 motherlode shards:)
          - (Condition: Before having exchanged motherlode shards on a given day:)
            - (removes=10 crystal motherlode shards) (receives=Motherlode Maw loot)
            - [pic=Crystal motherlode shard detail.png] <!-- pic2 = received reward -->
          - (Condition: After having exchanged motherlode shards on a given day:)
            - [You have already exchanged motherlode shards today.]
      - [Choice]: No...Bye.
        - (end)
      - [Choice]: I'd like to ask something else.
        - (initial|initial-options)
  - [Choice]: Who are you exactly?
    - **Wythien:** Me? An entrepreneur who's not afraid of taking the odd risk.
    - (initial|initial-options)
  - [Choice]: What else have you got?
    - [Menu]: Select an Option
      - [Choice]: Enhancers.
        - ((Enhancer's Exchange interface opens.))
      - [Choice]: Dungeoneering shop.
        - (opens=Daemonheim Rewards)
      - [Choice]: Ask about something else.
        - (initial|initial-options)
  - [Choice]: This sounds shifty. Bye
    - (end)

### Exchange motherlode shards

- (above|accept)

### Enhancers

- [Menu]: Select an Option
  - [Choice]: Focus enhancers.
    - ((Enhancers Exchange interface opens.))
  - [Choice]: Swap enhancers for motherlod shards.
    - ((Maw Enhancers interface opens with 'Exchange' buttons next to all enhancers types.))
  - [Choice]: Toggle enhancer effects.
    - ((Maw Enhancers interface opens with checkboxes next to enhancer types.))  <!-- and 'Activate' buttons next to the final three -->
  - [Choice]: Nothing.
    - (end)

### Dungeoneering shop

- (opens=Daemonheim Rewards)
