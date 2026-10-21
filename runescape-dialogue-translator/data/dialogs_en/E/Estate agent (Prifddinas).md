# Estate agent (Prifddinas)

- **Original Wiki Page**: [Transcript:Estate agent (Prifddinas)](https://runescape.wiki/w/Transcript%3AEstate%20agent%20%28Prifddinas%29)
- **Letter**: `E`

---

## Dialogue Transcript


### Talk to


#### Before completing There's No Place Like Home...

- **Estate agent:** If it's a house you're wanting, you'll want ot head over to Rimmington and chat to the estate agent there.

#### After completing There's No Place Like Home...

- {{Transcript missing}}

### Redecorate


#### Before completing There's No Place Like Home...

- **Estate agent:** If it's a house you're wanting, you'll want ot head over to Rimmington and chat to the estate agent there.

#### After completing There's No Place Like Home...

- {{Transcript missing}}

### Contracts

- [Menu]: Choose an option:
  - [Choice]: cond=Without a contract|I want a new contract.
    - (Condition: Without free backpack space:)
      - **Estate agent:** You're going to require some space in your backpack for a contract.
    - (Condition: With free backpack space:)
      - (receives=Construction contract)
      - You're handed a Construction contract.
      - **Estate agent:** Here you are, this just came in for [character] over in [location].
      - **Player:** Thanks! I'll see what I can do.
  - [Choice]: cond=With a contract|What's my current contract?
    - **Estate agent:** It looks like you're in the middle of helping out [character] over in [location].
    - (Condition: If the Construction contract has been lost:)
      - (Condition: Without free backpack space:)
        - **Estate agent:** You're going to require some space in your backpack for a contract.
      - (Condition: With free backpack space:)
        - (receives=Construction contract)
        - You're handed a Construction contract.
  - [Choice]: Tell me about contracts
    - **Estate agent:** There are many homeowners around Gielinor that are struggling to keep up with repairs on a regular basis.
    - **Estate agent:** So right now there's a market opportunity to put your construction skills to use and help them out.
    - **Estate agent:** We estate agents can provide you with a contract. This contract will tell you who needs help and what they need repairing.
    - **Estate agent:** All you need to do is head on over and repair all the broken furniture.
    - **Estate agent:** You can either use basic materials for a cheaper, but slower repair job. Or you can use more expensive materials for a faster return and more experience.
    - **Estate agent:** Whatever you choose, you'll gain a chunk of experience once you've repaired all the pieces of furniture that need repairing.
    - **Estate agent:** We'll also reward you with contract credits, which you can redeem from any estate agent for assorted rewards.
    - (previous|Contracts)
  - [Choice]: cond=If the player has lost their plank box|I've lost my plank box.
    - **Player:** I've lost my plank box.
    - **Estate agent:** Not to worry, I have another lying around.
    - (Condition: Without free backpack space:)
      - **Estate agent:** Come back when you have some free space in your backpack.
    - (Condition: With free backpack space:)
      - (receives=plank box)
      - **Estate agent:** Try not to lose this one though.
  - [Choice]: Do you have anything I can buy?
    - (opens=Estate Agents Shop)
  - [Choice]: [Leave]
    - (end)

### Shop

- (opens=Estate Agents Shop)
