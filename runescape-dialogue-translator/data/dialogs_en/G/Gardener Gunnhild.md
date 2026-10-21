# Gardener Gunnhild

- **Original Wiki Page**: [Transcript:Gardener Gunnhild](https://runescape.wiki/w/Transcript%3AGardener%20Gunnhild)
- **Letter**: `G`

---

## Dialogue Transcript


### Before Throne of Miscellania

- **Gardener Gunnhild:** Hello.
- [Menu]: What would you like to talk about?
  - [Choice]: Gardener Gunnhild.
    - **Player:** Good day. What are you doing?
    - **Gardener Gunnhild:** I'm weeding this herb garden. It's hard work! I also sell a few gardening supplies.
    - [Menu]: Select an option
      - [Choice]: Good luck with that.
        - **Player:** Good luck with that.
        - **Gardener Gunnhild:** Thanks.
      - [Choice]: What do you have for sale?
        - **Player:** What do you have for sale?
        - **Gardener Gunnhild:** At the moment I'm selling garden rakes and iron sickles. They're 15gp each, if you'd like one?
        - [Menu]: Select an option
          - [Choice]: I'd like a rake, please.
            - **Player:** I'd like a rake, please.
            - (Condition: If the player has at least 15 coins:)
              - (removes=15 coins)
              - **Gardener Gunnhild:** Thank you! Here you go.
              - (receives=rake)
          - [Choice]: I'd like an iron sickle, please.
            - **Player:** I'd like an iron sickle, please.
            - (Condition: If the player has at least 15 coins:)
              - (removes=15 coins)
              - **Gardener Gunnhild:** Thank you! Here you go.
              - (receives=iron sickle)
          - [Choice]: No, thank you.
            - **Player:** No, thank you.
          - [Choice]: What are iron sickles for?
            - **Player:** What are iron sickles for?
            - **Gardener Gunnhild:** I can't think of anything just now. But you can buy one if you like!
            - (other)
  - [Choice]: Your approval rating.
    - **Player:** What do people think of me around here?
    - (Condition: If your approval rating is below 25%:)
      - **Gardener Gunnhild:** You've not been making many friends since you arrived here. At the last poll, only [approval rating]% of the population liked you.
    - (Condition: If your approval rating is between 25% and 49%:)
      - **Gardener Gunnhild:** You haven't really won the heart of the locals, if you see what I mean. At the last poll, only [approval rating]% of the population liked you.
    - (Condition: If your approval rating is between 50% and 74%:)
      - **Gardener Gunnhild:** You haven't been here for very long, but people are reasonably fond of you. At the last poll, [approval rating]% of the population liked you.
    - (Condition: If your approval rating is at 75% or higher:)
      - **Gardener Gunnhild:** You seem remarkably popular for a newcomer to these lands. At the last poll, [approval rating]% of the population liked you.

#### Attempting to rake flax or herbs

*At below 100% approval rating*
- **Gardener Gunnhild:** {{RSChat|Thanks!}}
*At 100% approval rating*
- **Gardener Gunnhild:** Don't trouble yourself further, [Sir/Madam], you've already done so much!

### After [[Throne of Miscellania]]


#### Talking to Gardener Gunnhild

- **Gardener Gunnhild:** Good day, Your Royal Highness
  - [Menu]: What would you like to talk about?
    - [Choice]: Gardener Gunnhild.
      - **Player:** Good day. What are you doing?
      - **Gardener Gunnhild:** I'm weeding this herb garden. It's hard work! I also sell a few gardening supplies.
        - [Choice]: Good luck with that.
          - **Player:** Good luck with that.
          - **Gardener Gunnhild:** Thank you, Your Royal Highness.
        - [Choice]: What do you have for sale?
          - **Player:** What do you have for sale?
          - **Gardener Gunnhild:** At the moment I'm selling garden rakes and iron sickles. If you'd like one, Your Royal Highness, they're 15gp each.
            - [Choice]: I'd like a rake, please.
              - **Player:** I'd like a rake, please.
                - (Condition: If you have sufficient money with you:)
                  - (Condition: If money to be paid is taken from your money pouch:)
                    - 15 coins have been removed from your money pouch.
                  - **Gardener Gunnhild:** Thank you! Here you go.
            - [Choice]: I'd like an iron sickle, please.
              - **Player:** I'd like an iron sickle, please.
                - (Condition: If you have sufficient money with you:)
                  - (Condition: If money to be paid is taken from your money pouch:)
                    - 15 coins have been removed from your money pouch.
                  - **Gardener Gunnhild:** Thank you! Here you go.
            - [Choice]: No, thank you.
              - **Player:** No, thank you.
            - [Choice]: What are iron sickles for?
              - **Player:** What are iron sickles for?
              - **Gardener Gunnhild:** I can't think of anything just now. But you can buy one if you like, Your Highness!
                - [Choice]: I'd like a rake, please.
                  - *(Same as above)*
                - [Choice]: I'd like an iron sickle, please.
                  - *(Same as above)*
                - [Choice]: No, thank you.
                  - *(Same as above)*
    - [Choice]: Your approval rating.
      - **Player:** What do people think of me around here?
      - (Condition: If your approval rating is between 25% and 49%:)
        - **Gardener Gunnhild:** Your people are growing dissatisfied with the regime, Your Royal Highness. At the last poll, only [approval rating]% of the population supported you.
      - (Condition: If your approval rating is between 50% and 74%:)
        - **Gardener Gunnhild:** You are well regarded, Your Royal Highness. At the last poll, [approval rating]% of the population supported you.
      - (Condition: If your approval rating is at 75% or higher:)
        - **Gardener Gunnhild:** You are universally adored, Your Royal Highness. At the last poll, [approval rating]% of the population supported you.

#### Attempting to rake flax or herbs

*At below 100% approval rating*
- **Gardener Gunnhild:** {{RSChat|Thanks!}}
*At 100% approval rating*
- **Gardener Gunnhild:** Don't trouble yourself further, Your Highness, you've already done so much!
