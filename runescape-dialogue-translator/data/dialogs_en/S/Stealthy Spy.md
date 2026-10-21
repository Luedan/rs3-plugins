# Stealthy Spy

- **Original Wiki Page**: [Transcript:Stealthy Spy](https://runescape.wiki/w/Transcript%3AStealthy%20Spy)
- **Letter**: `S`

---

## Dialogue Transcript


### Pickpocket

- {{Qact|The player starts pickpocketing the Stealthy Spy.}}
- (Condition: For each successful attempt:)
  - You pick the target's pocket.
  - You snatch the spies' notes. Smearing them in chocolate beyond repair.
  - (Condition: With under 30,000 spring tokens:)
    - The following has been added to your currency pouch: [number] Spring tokens.
    - (continue)
  - (Condition: With at least 30,000 spring tokens:)
    - You have reached the Spring token soft cap of 30,000. You need to spend some tokens in Gummy's store before you can earn more.
    - (pop-up)
      - {{Pop-up|You have reached the Spring token soft cap of 30,000. You need to spend some tokens in Gummy's store before you can earn more.|warning=yes}}
      - (continue)
  - (Condition: If the success chance drops below 100%:)
    - Your pickpocket target becomes aware of your presence.
- (Condition: With full backpack:)
  - You cannot keep pickpocketing as you have a full inventory.
- (Condition: Getting caught:)
  - **Stealthy Spy:** {{RSChat|What do you think you're doing?}}
  - {{Qact|The Stealthy Spy hits the player.}}
  - You fail to steal from the target.
  - You've been stunned.
