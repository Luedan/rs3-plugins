# Dark Romancer

- **Original Wiki Page**: [Transcript:Dark Romancer](https://runescape.wiki/w/Transcript%3ADark%20Romancer)
- **Letter**: `D`

---

## Dialogue Transcript


### Talk to

- **Player:** Hey there!
- **Dark Romancer:** Urrm... hello!
- **Player:** What are you doing here?
- **Dark Romancer:** I'm looking for Love Letters.
- **Player:** Love Letters?
- **Dark Romancer:** Yes! The more I can find and destroy, the less love that's shared around. I can't stand this time of year!
- [Bring Dark Romancer Love Letters before the end of the 17th of February to make progress towards 'the Hater' title and colour variants, as well as one of the following:]
- [20% XP boost for +5 minutes (up to 60 minutes max).<br>25% Bonus XP Burn boost +5 minutes (up to 60 minutes max).<br>250x Heartments.]
- [If you don't want to deliver Love Letters, or Dark Romancer has left, they can be ripped up instead, giving a 5% XP boost for +5 minutes (up to 60 minutes max) to all players that see it.]
- (Condition: Without Love Letters:)
  - **Player:** If I find any, I'll bring them to you!
  - **Dark Romancer:** Thank you!
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
      - **Dark Romancer:** I can't wait to burn this.
      - **Dark Romancer:** Nice!
      - **Dark Romancer:** Oh, okay.
      - **Dark Romancer:** Okay...
      - **Dark Romancer:** Yeah, I'll never open this.
    - **Dark Romancer:** Thanks, I guess! Here, take this.
    - [Menu]: What would you like (per 1 letter)?
      - [Choice]: +20% XP for +5 minutes (up to 60 minutes max)
        - (Condition: If the player is already receiving a +5% XP boost from witnessing a love letter being ripped up:)
          - You have an active 5% XP Boost from witnessing a Love Letter rip. Activating this will clear the current boost.
          - [Menu]: Continue?
            - [Choice]: Yes.
              - (continue)
            - [Choice]: No.
              - (end)
        - (removes=the chosen number of love letters)
        - You now have a 20% XP boost for [number] minutes and [number] seconds.
        - ((Repeated in a pop-up:))
          - {{Pop-up|You now have a 20% XP boost for [number] minutes and [number] seconds.|colour=#63D21D}}
      - [Choice]: +25% Bonus XP Burn for +5 minutes (up to 60 minutes max)
        - (removes=the chosen number of love letters)
        - You now have a 25% Bonus XP burn boost for [number] minutes and [number] seconds.
        - ((Repeated in a pop-up:))
          - {{Pop-up|You now have a 25% Bonus XP burn boost for [number] minutes and [number] seconds.|colour=#63D21D}}
      - [Choice]: 250x Heartments
        - (removes=the chosen number of love letters) (receives=250 heartments per letter handed in)
        - You gain [number] heartments.

#### Upon giving letters


##### Below five letters

- Progress towards 'the Hater' Red title: [1/2/3/4]/5

##### Upon giving in the fifth letter

- Congratulations! You've unlocked: the Hater. Your new item(s) can be found in the Customisations Interface.
- ((Repeated in a pop-up:))
  - {{Pop-up|Congratulations! You've unlocked: the Hater. Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}

##### Between five and ten letters

- Progress towards 'the Hater' Grey variant title: [5/6/7/8/9]/10

##### Upon giving the tenth letter

- Congratulations! You've unlocked: the Hater (grey). Your new item(s) can be found in the Customisations Interface.
- ((Repeated in a pop-up:))
  - {{Pop-up|Congratulations! You've unlocked: the Hater (grey). Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}

##### Between ten and twenty letters

- Progress towards 'the Hater' Red & Grey variant title: [10/11/12/13/14/15/16/17/18/19]/20

##### Upon handing in the twentieth letter

- Congratulations! You've unlocked: the Hater (red & grey). Your new item(s) can be found in the Customisations Interface.
- ((Repeated in a pop-up:))
  - {{Pop-up|Congratulations! You've unlocked: the Hater (red & grey). Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}
