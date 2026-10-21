# Fairy trader

- **Original Wiki Page**: [Transcript:Fairy trader](https://runescape.wiki/w/Transcript%3AFairy%20trader)
- **Letter**: `F`

---

## Dialogue Transcript


### Pickpocket


#### With under 113 Thieving

- You need to be a level 113 thief to steal from this target.
- (popup)
  - {{Popup|You need Thieving level 113.|warning=yes}}

#### With at least 113 Thieving


##### Unsuccessfully


##### With full backpack

- You cannot keep pickpocketing as you have a full inventory.

##### Getting caught

- **Fairy trader:** {{RSChat|What do you think you're doing?}}
- {{Qact|The fairy transforms the player into a random object.}}

##### Successfully

- ((The following repeats until interrupted, out of backpack space, or caught:))
  - You pick the target's pocket.
  - (Condition: If receiving coins:)
    - [number] coins have been added to your money pouch.
  - (Condition: If receiving other items:)
    - (receives=loot)
    - (Condition: If reaching full backpack:)
      - You cannot keep pickpocketing as you have a full inventory.
