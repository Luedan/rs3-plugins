# Hungry reindeer

- **Original Wiki Page**: [Transcript:Hungry reindeer](https://runescape.wiki/w/Transcript%3AHungry%20reindeer)
- **Letter**: `H`

---

## Dialogue Transcript


### Feed


#### During a Christmas event


##### Without any Christmas food or with only noted Christmas food

- **Player:** They don't seem interested in eating anything I have with me. What would a Christmas-loving reindeer prefer to eat?

##### With unnoted Christmas food

- [Menu]: Feed the reindeer the Christmas food you are carrying?
  - [Choice]: Yes
    - (Condition: Before feeding 25 daily pieces of Christmas food:)
      - (removes=all or as many as is missing from the daily 25 unnoted Christmas food)
      - (Condition: If one piece of unnoted Christmas food was fed:)
        - You feed the hungry reindeer a piece of Christmas food.
        - (pop-up)
          - {{Pop-up|You feed the hungry reindeer a piece of Christmas food.}}
          - (continue)
      - (Condition: If multiple pieces of unnoted Christmas food were fed:)
        - You feed the hungry reindeer [number] pieces of Christmas food.
        - (pop-up)
          - {{Pop-up|You feed the hungry reindeer [number] pieces of Christmas food.}}
          - (continue)
      - (Condition: Reaching 50,000 Christmas spirit:)
        - You have reached the Christmas spirit soft cap of 50,000. You need to spend some tokens in the Christmas Spirit Shop before you can earn more.
        - (pop-up)
          - {{Pop-up|You have reached the Christmas spirit soft cap of 50,000. You need to spend some tokens in the Christmas Spirit Shop before you can earn more.|warning=yes}}
          - (continue)
      - (Condition: With under 50,000 Christmas spirit before:)
        - The following has been added to your currency pouch: [number] x Christmas spirit.
        - (continue)
      - (Condition: If Rudi is obtained:)
        - (receives=Rudi)
        - Whilst feeding the reindeer you find Rudi, the Christmas Village reindeer pet.
        - (pop-up)
          - {{Pop-up|Whilst feeding the reindeer you find Rudi, the Christmas Village reindeer pet.|colour=#00FF00}}
    - (Condition: After feeding 25 daily pieces of Christmas food:)
      - **Player:** It looks like he's eaten all he can for today.
      - Extra Christmas food can be added to the nearby trough instead.
  - [Choice]: No
    - (end)

#### Outside a Christmas event

- [The Christmas festivities have now ended.]

### Check

- [Times fed today: [number]/25<br>Times fed total: [number]]

### Using items


#### During a Christmas event


##### Incompatible item

- **Player:** They don't seem interested in eating that. What would a Christmas-loving reindeer prefer to eat?

##### Compatible item

- (above|feed)

#### Outside a Christmas event

- [The Christmas festivities have now ended.]
