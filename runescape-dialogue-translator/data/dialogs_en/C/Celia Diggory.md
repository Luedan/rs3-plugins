# Celia Diggory

- **Original Wiki Page**: [Transcript:Celia Diggory](https://runescape.wiki/w/Transcript%3ACelia%20Diggory)
- **Letter**: `C`

---

## Dialogue Transcript


### At the Varrock Dig Site


#### Talking to her

- **Celia Diggory:** Hello adventurer. Have you come to help with the excavation effort?
- (Condition: If the player is carrying Senntisten scrolls:)
  - **Celia Diggory:** I see you've found something special amidst the rubble!
  - **Celia Diggory:** It really belongs in a museum. I could work on a translation and give you a copy?
  - (Condition: If player has one scroll:)
    - [Menu]: {{transcript missing}}
      - [Choice]: Yes, take my scroll for study.
        - **Celia Diggory:** Thank you! I'll make sure this gets safely to the Varrock museum.
        - [Celia spends a few minutes reading the scroll and scribbling in a notebook.] <!-- unchecked but probably tbox -->
        - **Celia Diggory:** Would you like a copy of the translation?
        - [Menu]: {{transcript missing}}
          - [Choice]: Yes, please.
            - (continue|transcript)
          - [Choice]: No thank you.
            - (continue)
      - [Choice]: No, I'd like to hold onto it.
        - (continue)
  - (Condition: If player has multiple scrolls:)
    - [Menu]: {{transcript missing}}
      - [Choice]: Yes, take my scrolls for study.
        - **Celia Diggory:** Thank you! I'll make sure these get safely to the Varrock museum.
        - [Celia spends a few minutes reading the scroll and scribbling in a notebook.] <!-- unchecked but probably tbox -->
        - **Celia Diggory:** Would you like a copy of the translation?
        - [Menu]: {{transcript missing}}
          - [Choice]: Yes, please.
            - (continue|transcript)
          - [Choice]: No thank you.
            - (continue)
      - [Choice]: No, I'd like to hold onto it.{{fact|Does this say 'it', not 'them'?}}
        - (continue)
- [Menu]: Choose an option:
  - {{anchor|excavation}} [Choice]: Excavation effort?|First time seeing these options:
    - **Celia Diggory:** One of our dig teams recently unearthed an ancient doorway. The entryway has mostly given way, hence the lift, but this chamber appears largely intact.
    - **Celia Diggory:** The architecture definitely reflects the second age Zarosian style, suggesting that this was part of the ancient city of Senntisten!
    - **Celia Diggory:** It appears to be a chamber of great importance. We suspect that this room would have served as Zaros' throne room!
    - **Celia Diggory:** There appears to be a large amount of residual divine energy around, suggesting a major divine event took place here!
    - (previous)
  - [Choice]: What's down there?|Only above, and after having seen these options before:  <!-- i.e. also after returning here from another option, don't have to go through the 'excavation' option dialogue -->
    - (above|excavation)
  - [Choice]: What is this place?|Only below, and after having seen these options before:
    - (above|excavation)
  - {{anchor|help}} [Choice]: Is there any way I can help out?|cond=Only outside:
    - **Celia Diggory:**We've been mining crystals out from the digsite. There are deposits of dark animica ore you can mine, as it's just getting in our way.
    - **Celia Diggory:** Next, if you're sufficiently skilled in Agility we need to transport the crystals up here. There are bikes you can use to move it.
    - **Celia Diggory:** Finally if you've practiced your Divination, we're asking for people to try to transmute the crystals.
    - **Celia Diggory:** There appears to be a large amount of residual divine energy around, suggesting a major divine event took place here!
    - **Celia Diggory:** We've noticed this energy moving around the room, even interacting with some of our equipment. It appears to be having a positive effect at least, so I suggest you direct your attention towards it.
    - [Menu]: Select an Option
      - [Choice]: Why are you mining out the crystals?
        - **Celia Diggory:** They appeared to be growing somehow. You should've seen the state of the place when we first found it. They were everywhere.
        - **Celia Diggory:** We've decided to make sure we mine them out entirely, it's the only way to be sure they won't continue to create problems as the restoration continues.
        - (other)
      - [Choice]: Why are you transmuting the crystals?
        - **Celia Diggory:** In order to render them inert. One of our sponsors requested the different colourations. He should be sending someone down to collect them.
        - (other)
      - [Choice]: Ask about something else.
        - (previous)
  - [Choice]: How can I help out here?|cond=Only inside:
    - (above|help)
  - [Choice]: Weren't you just outside?|cond=Only inside:
    - **Celia Diggory:** I rode down on the elevator. I was stood right next to you. Don't you recall?
    - (previous)
  - {{anchor|transcript}} [Choice]: Can you give me a copy of the translated letters?{{fact|Does this say 'letter' with only a single one handed in?|cond=After having returned a Senntisten scroll:}}
    - [Menu]: Which transcript would you like?
      - [Choice]: Scroll 1 - Letter signed 'Pontifex Madromurt'.
        - [pic=Letter signed 'Pontifex Madromurt' detail.png]
        - (previous)
      - [Choice]: Scroll 2 - Letter signed 'Pontifex Nabor'.|cond=With the second scroll handed in:
        - [pic=Letter signed 'Pontifex Nabor' detail.png]
        - (previous)
      - [Choice]: Scroll 3 - Letter signed 'Pontifex Bilrach'.|cond=With the third scroll handed in:
        - [pic=Letter signed 'Pontifex Bilrach' detail.png]
        - (previous)
      - [Choice]: [More...]
        - [Choice]: Scroll 4 - Damaged letter.|cond=With the fourth scroll handed in:
          - [pic=Damaged letter detail.png]
          - (initial)
        - [Choice]: All of them.
          - [pic=Damaged letter detail.png]
          - (initial)
        - [Choice]: Never mind.
          - (initial)
        - [Choice]: [More...]
          - (previous)
  - [Choice]: Bye.
    - **Player:** Bye.

#### Check progress

- So far you've gained {{Colour/800,000 experience in Agility, and {{Colour|#0f0|[number]}}/800,000 experience in Divination.}}
- You've also handed in {{Colour out of 4 Senntisten scrolls.}}

#### Treasure Trails

- {{transcript missing}}
