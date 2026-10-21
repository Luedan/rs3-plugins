# Reinald

- **Original Wiki Page**: [Transcript:Reinald](https://runescape.wiki/w/Transcript%3AReinald)
- **Letter**: `R`

---

## Dialogue Transcript


### In eastern Keldagrim

- **Reinald** Welcome to my home. I have a fine selection of home- made arm guards, as well as fine clothes imported from Thessalia in Varrock, if you're interested.
- (Condition: If the player does not have armour equipped:)
  - (opens=Reinald's Smithing Emporium)
- (Condition: If the player has armour equipped:)
  - **Reinald** You're not able to try on my clothes with all that armour. Take it off and then speak to me again.

#### Change armguards option

- (Condition: If the player does not have armour equipped:)
  - (opens=Reinald's Smithing Emporium)
- (Condition: If the player has armour equipped:)
  - **Reinald** You're not able to try on my clothes with all that armour. Take it off and then speak to me again.

### Manor Farm


#### Help


##### Before completing the request

- [Menu]: What would you like to do?
  - [Choice]: Ask about their request.
    - **Player:** What're you requesting today?
    - **Reinald:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **Reinald:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - (Condition: With 3 requested animals:)
      - **Reinald:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
      - (continue)
    - (Condition: With 4 requested animals:)
      - **Reinald:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal]
      - (continue)
    - **Reinald:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - **Reinald:** If you complete this, I'll give you : Light animica stone spirit x 10. I'm sure you'll gain some reputation with the farming guild too!
    - **Reinald:** You'll have to be quick though!, I'm only here for [number] days, [number] hours and [number] minutes. To be exact.
  - [Choice]: Give them the items & animals for their request
    - (Condition: Without the requested items:)
      - **Reinald:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **Reinald:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - (Condition: With 3 requested animals:)
        - **Reinald:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
        - (continue)
      - (Condition: With 4 requested animals:)
        - **Reinald:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal]
        - (continue)
      - **Reinald:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - (Condition: With the requested items:)
      - (removes=the requested items) (receives=ten light animica stone spirits and Brassica primer)
      - For completing this request you've received Brassica primer x 1.
      - ((Repeated in a pop-up:))
        - For completing this request you've received Brassica primer x 1.
        - (continue)
      - [You've received : Light animica stone spirit x 10<br>And 5,500 farming reputation.]

##### After completing the request

- **Reinald:** Thank you for your help!
- A new request will be available in [time]{{Sic|..}}

#### Hand in medium request


##### Before completing the request


##### Without requested items

- **Reinald:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **Reinald:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- **Reinald:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal
- **Reinald:** I'm also looking for some produce, so I'll need : [Produce] x [number]

##### With requested items

- (Condition: With multiple applicable animals:)
  - [Menu]: Which animal would you like to hand in?
    - ((The following is repeated for each applicable animal:))
      - [Choice]: [Animal name]
        - (continue)
- (removes=the requested items) (receives=ten light animica stone spirits and Brassica primer)
- For completing this request you've received Brassica primer x 1.
- ((Repeated in a pop-up:))
  - For completing this request you've received Brassica primer x 1.
  - (continue)
- [You've received : Light animica stone spirit x 10<br>And 5,500 farming reputation.]

##### After completing the request

- You've already completed this request, there will be a new bi-daily request in [time]{{Sic|..}}
