# Light Romancer

- **Original Wiki Page**: [Transcript:Light Romancer](https://runescape.wiki/w/Transcript%3ALight%20Romancer)
- **Letter**: `L`

---

## Dialogue Transcript


### Talk to

- **Player:** Hello!
- **Light Romancer:** Hello!
- **Player:** What are you doing here?
- **Light Romancer:** It's the most loving time of the year of course, so I'm looking for Love Letters.
- **Player:** Love Letters?
- **Light Romancer:** Yes! They're just the best!
- [Bring Light Romancer Love Letters before the end of the 17th of February to make progress towards 'the Lover' title and colour variants, as well as one of the following:]
- [20% XP boost for +5 minutes (up to 60 minutes max).<br>25% Bonus XP Burn boost +5 minutes (up to 60 minutes max).<br>250x Heartments.]
- [If you don't want to deliver Love Letters, or Light Romancer has left, they can be ripped up instead, giving a 5% XP boost for +5 minutes (up to 60 minutes max) to all players that see it.]
- (Condition: Without Love Letters:)
  - **Player:** If I find any, I'll bring them to you!
  - **Light Romancer:** Thank you!
- (Condition: With Love Letters:)
  - (continue|I've)

### Give Love Letter

- **Player:** I've got something to give you.
- (Condition: Without Love Letters:)
  - You do not have a Love Letter to give.
  - (pop-up)
    - {{Pop-up|You do not have a Love Letter to give.}}
- (Condition: With Love Letters:)
  - {{Tinput|How many letters do you want to give?}}
  - (Condition: After entering a positive number:)
    - ((A random dialogue is selected from the following, then continues below:))
      - **Light Romancer:** For me?
      - **Light Romancer:** How nice!
      - **Light Romancer:** Oh that's lovely!
      - **Light Romancer:** So sweet!
      - **Light Romancer:** Very cute!
    - **Light Romancer:** Thanks you! I'd like to give you something in return.
    - [Menu]: What would you like (per 1 letter)?
      - [Choice]: +20% XP for +5 minutes (up to 60 minutes max)
        - (Condition: If the player is already receiving a +5% XP boost from witnessing a love letter being ripped up:)
          - You have an active 5% XP Boost from witnessing a Love Letter rip. Activating this will clear the current boost.
          - [Menu]: Continue?
            - [Choice]: Yes.
              - (continue)
            - [Choice]: No.
              - (end)
        - (Condition: With at least 55 minutes of the buff active:)
          - [Your Love Letter BXP boost duration will cap at 60 minutes. Do you want to continue?]
          - [Menu]: Continue?
            - [Choice]: Yes.
              - (continue)
            - [Choice]: No.
              - (end)
        - (removes=the chosen number of love letters)
        - You now have a 20% XP boost for [number] minutes and [number] seconds.
        - ((Repeated in a pop-up:))
          - {{Pop-up|You now have a 20% XP boost for [number] minutes and [number] seconds.|colour=#63D21D}}
          - (continue)
        - (continue|Upon giving letters)
      - [Choice]: +25% Bonus XP Burn for +5 minutes (up to 60 minutes max)
        - (Condition: With at least 55 minutes of the buff active:)
          - [Your Love Letter BXP burn boost duration will cap at 60 minutes. Do you want to continue?]
          - [Menu]: Continue?
            - [Choice]: Yes.
              - (continue)
            - [Choice]: No.
              - (end)
        - (removes=the chosen number of love letters)
        - (Condition: Not having given over 20 Love Letters previously:)
          - (continue|Upon giving letters)
      - [Choice]: 250x Heartments
        - (removes=the chosen number of love letters) (receives=250 heartments per letter handed in)
        - You gain [number] heartments.
        - (Condition: Not having given over 20 Love Letters previously:)
          - (continue|Upon giving letters)

#### Upon giving letters


##### Below five letters

- Progress towards 'the Lover' Red title: [1/2/3/4]/5

##### Upon giving in the fifth letter

- Congratulations! You've unlocked: the Lover. Your new item(s) can be found in the Customisations Interface.
- ((Repeated in a pop-up:))
  - {{Pop-up|Congratulations! You've unlocked: the Lover. Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}

##### Between five and ten letters

- Progress towards 'the Lover' Pink variant title: [5/6/7/8/9]/10

##### Upon giving the tenth letter

- Congratulations! You've unlocked: the Lover (pink). Your new item(s) can be found in the Customisations Interface.
- ((Repeated in a pop-up:))
  - {{Pop-up|Congratulations! You've unlocked: the Lover (pink). Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}

##### Between ten and twenty letters

- Progress towards 'the Lover' Red & Pink variant title: [10/11/12/13/14/15/16/17/18/19]/20

##### Upon handing in the twentieth letter

- Congratulations! You've unlocked: the Lover (red & pink). Your new item(s) can be found in the Customisations Interface.
- ((Repeated in a pop-up:))
  - {{Pop-up|Congratulations! You've unlocked: the Lover (red & pink). Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}
