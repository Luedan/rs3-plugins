# Smokey

- **Original Wiki Page**: [Transcript:Smokey](https://runescape.wiki/w/Transcript%3ASmokey)
- **Letter**: `S`

---

## Dialogue Transcript


### Upon appearing

- {{Qact|Smokey the coal appears near the stove with a red progress bar overhead.}}
- {{Colour AAH! TOO HOT! TOO HOT!}}
- **Smokey:** {{RSChat|AAH! TOO HOT! TOO HOT!}}

### Pelt snowball


#### Before Smokey has cooled


##### Without a snowball equipped

- You need to equip a snowball to cool down the coal.
- (pop-up)
  - {{Pop-up|You need to equip a snowball to cool down the coal.|warning=yes}}

##### With a snowball equipped

- (removes=one equipped snowball)
- (Condition: If this was the third snowball pelted:)
  - (Condition: With less than 49,926 Christmas spirit:)
    - (receives=75 Christmas spirit)
    - The following has been added to your currency pouch: 75 x Christmas spirit.
    - (continue)
  - (Condition: With at least 49,926 Christmas spirit:)
    - (Condition: With under 50,000 Christmas spirit:)
      - (receives=as much Christmas spirit as is missing from 50,000)
      - The following has been added to your currency pouch: [number] x Christmas spirit.
      - (continue)
    - You have reached the Christmas spirit soft cap of 50,000. You need to spend some tokens in the Christmas Spirit Shop before you can earn more.
    - (continue)
  - You fully cool down the coal.
  - (pop-up)
    - {{Pop-up|You fully cool down the coal.|colour=#00FF00}}
    - (continue)
  - {{Colour Thank you Player!}}
  - **Smokey the coal:** {{RSChat|Thank you Player!}}

#### After Smokey has cooled

- The coal has already cooled down!
- (pop-up)
  - {{Pop-up|The coal has already cooled down!|warning=yes}}

### Failing to pelt Smokey three times before 18 seconds have elapsed

- {{Colour Ah. The fresh snow air is nice and cooling.}}
- **Smokey the coal:** {{RSChat|Ah. The fresh snow air is nice and cooling.}}
