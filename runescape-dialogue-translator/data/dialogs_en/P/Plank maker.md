# Plank maker

- **Original Wiki Page**: [Transcript:Plank maker](https://runescape.wiki/w/Transcript%3APlank%20maker)
- **Letter**: `P`

---

## Dialogue Transcript


### Buy plank


#### Before starting There's No Place Like Home...

- ((The following is shown in an interface titled "CONSTRUCTION":))
  - 54px You need to complete the Construction tutorial before you can use this.
  - Speak to Alfred Stonemason, northwest of Rimmington, to learn more.
    - [Choice]: OK
      - ((The interface closes.))

#### During There's No Place Like Home...

- (see|There's No Place Like Home...)

#### After completing There's No Place Like Home...


##### Without any suitable logs in backpack

- (Shown in a pop-up:)
  - {{Pop-up|You are not carrying any logs to cut into planks.|colour=#EBE0BC}}

##### With suitable logs in backpack

- ((The following is shown in an interface titled "SAWMILL":))
- Choose a plank to make.
  - [Choice]: Plank<br>Cost each: 100 x coins
    - (below2|Upon picking an option)
  - [Choice]: Oak plank<br>Cost each: 250 x coins
    - (below2|Upon picking an option)
  - [Choice]: Willow plank<br>Cost each: 250 x coins
    - (below2|Upon picking an option)
  - [Choice]: Teak plank<br>Cost each: 500 x coins
    - (below2|Upon picking an option)
  - [Choice]: Maple plank<br>Cost each: 250 x coins
    - (below2|Upon picking an option)
  - [Choice]: Acadia plank<br>Cost each: 500 x coins
    - (below2|Upon picking an option)
  - [Choice]: Mahogany plank<br>Cost each: 1,500 x coins
    - (below2|Upon picking an option)
  - [Choice]: More
    - Choose a plank to make.
      - [Choice]: Yew plank<br>Cost each: 2,000 x coins
        - (below2|Upon picking an option)
      - [Choice]: Magic plank<br>Cost each: 3,500 x coins
        - (below2|Upon picking an option)
      - [Choice]: Elder plank<br>Cost each: 5,000 x coins
        - (below2|Upon picking an option)
      - [Choice]: More
        - (previous)

##### Upon picking an option

- {{Tinput|How many [type] logs would you like to make into planks? (0 - [number])<br>Cost each: [number])}}
- ((After entering a positive amount:))
  - (Condition: Without sufficient money:)
    - You cannot afford to make that many planks.
    - ((Repeated in a pop-up:))
      - {{Pop-up|You cannot afford to make that many planks.|colour=#EBE0BC}}
  - (Condition: With sufficient money:)
    - (removes=coins) (receives=planks)

### Talk to


#### Before starting There's No Place Like Home...

- ((The following is shown in an interface titled "CONSTRUCTION":))
  - 54px You need to complete the Construction tutorial before you can use this.
  - Speak to Alfred Stonemason, northwest of Rimmington, to learn more.
    - [Choice]: OK
      - ((The interface closes.))

#### During There's No Place Like Home...

- (see|There's No Place Like Home...)

#### After completing There's No Place Like Home...

- **Plank maker:** Hello. Do you want me to make some planks for you?
- [Menu]: Choose an option:
  - [Choice]: Planks, please.
    - **Plank maker:** What kind of planks do you want?
    - (continue|Buy plank option)
  - [Choice]: What kind of planks can you make?
    - **Plank maker:** I can make planks from wood, oak, teak and mahogany. I don't make planks from other woods as they're no good for making furniture.
    - **Plank maker:** Wood and oak are all over the place, but teak and mahogany can only be found in a few places like Karamja and Etceteria.
  - (initial)
  - [Choice]: Nothing, thanks.
    - **Player:** Nothing, thanks.
    - **Plank maker:** Well, come back when you want some. You can't get good quality planks anywhere but here!

### Trade


#### Before starting There's No Place Like Home...

- ((The following is shown in an interface titled "CONSTRUCTION":))
  - 54px You need to complete the Construction tutorial before you can use this.
  - Speak to Alfred Stonemason, northwest of Rimmington, to learn more.
    - [Choice]: OK
      - ((The interface closes.))

#### During There's No Place Like Home...

- (see|There's No Place Like Home...)

#### After completing There's No Place Like Home...

- (opens=Sawmill Co. - A 'G.H.A' Subsidiary)
