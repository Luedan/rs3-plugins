# Jossik

- **Original Wiki Page**: [Transcript:Jossik](https://runescape.wiki/w/Transcript%3AJossik)
- **Letter**: `J`

---

## Dialogue Transcript


### Standard dialogue at the Lighthouse

- **Jossik:** Hello again adventurer. What brings you this way?
- [Menu]: Choose an option:
  - [Choice]: Can I see your wares?
    - **Player:** Can I see your wares?
    - **Jossik:** Sure thing! I think you'll agree, my prices are remarkable.
    - (opens=The Lighthouse Store)
  - [Choice]: Have you found any new prayer books?
    - (below|holy book)
    - [Choice]: I think I may have found your uncle.|cond=If the Blood Runs Deep quest has been completed:
      - **Player:** I think I may have found your uncle.
      - **Jossik:** Really? Where is he? How is he?
      - **Player:** Well, he was being looked after by the mages in Lunar Isle but, when he got better, he wanted to leave, so they had to let him go.
      - **Jossik:**  He just left? Oh my... Well, now I'll never find him.
      - **Player:** At least we know he's alive and well. I'm sure he'll show up sooner or later.

### Holy-book option

- {{anchor|holy book}}**Player:** Have you found any new prayer books?
- (Condition: If the player hasn't bought all the available damaged god books:)
  - **Jossik:** Funnily enough I have! I found these [number] books in caskets just the other day! I'll sell one to you for 5000 coins: what do you say?
  - [Menu]: Select an option
    - [Choice]: Buy a book
      - ("Choose a book" interface opens.)
      - (Condition: If you buy any of the books:)
        - (removes=5,000 coins) (receives=the selected damaged book)
        - **Jossik:** Here you go!
    - [Choice]: Don't buy anything
      - **Player:** No thanks.
      - **Jossik:** Okay! Suit yourself.
- (Condition: If the player has bought all the available damaged god books:)
  - **Jossik:** Nope. Sorry, adventurer, I guess you've found them all! I'll let you know if any new ones show up, though.
- (Condition: If the player has lost one of their previously purchased damaged god books:)
  - (receives=one of their missing god book with all previously attached pages intact)
  - **Jossik:** As a matter of fact, I did! This book washed up on the beach not so long ago, I recognised it as yours immediately! Here you go!
