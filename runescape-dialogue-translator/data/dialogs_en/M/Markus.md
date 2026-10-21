# Markus

- **Original Wiki Page**: [Transcript:Markus](https://runescape.wiki/w/Transcript%3AMarkus)
- **Letter**: `M`

---

## Dialogue Transcript


### Talking to Markus


#### With a complete contract in the inventory

- (If the player has a special slayer contract:)
  - **Markus:** I see you've completed that contract. Good work. Would you like combat XP or cash?
- (If the player has a slayer contract:)
  - **Markus:** I see you've completed that special contract. Good work. Would you like combat XP or cash?
- Choose your reward:
  - Combat XP: [#] XP
    - (receives=a combat training book)
    - You receive a book about combat.
  - Cash: [#] coins
    - (receives=coins added directly to their money pouch)
    - You receive [#] coins.

#### With an incomplete contract in the inventory

- (If the player has a special slayer contract:)
  - **Markus:** Show me your special contract when you've finished it.
- (If the player has a slayer contract:)
  - **Markus:** Show me your contract when you've finished it.

#### Without a Slayer assignment for a Slayer Tower monster

- **Markus:** Can I interest you in a job? I'll pay you for your work.
- What would you like to say?
  - Tell me about yourself.
    - **Markus:** My name's Markus. I used to run a trading company in Falador, but now I'm a warrior, fighting the evils of Morytania. Actually, I've found that fighting isn't really my thing, so I'm hiring people to do all that stuff for me. If you're interested in doing some combat yourself, I'd be happy to give you a job. I can pay you.
    - What would you like to say?
      - What sort of job are you offering?
        - (continue|type)
      - That's very noble of you.
        - **Markus:** Thanks. I believe my business experience and my wealth are really making a difference to the struggle against evil here. Would you like a job now?
        - (initial)
      - Are you incapable of doing your own work?
        - **Markus:** Any meat-head can hit a monster. With my business experience and my wealth, I can direct an army to achieve far greater things. I just need to find enough people ready to work under me. So, would you like a job now?
        - (initial)
      - Okay, I'd like a job.
        - (continue|job)
      - No thanks.
        - (continue|no)
  - What sort of job are you offering?
    - **Markus:** I'm hiring people to kill the monsters in this tower. I'd do it myself, but I've found that fighting isn't really my thing. Instead, I use my wealth to hire people to kill the monsters for me. Effectively, I'm fighting the evils of Morytania through business! I can offer cash payments. Alternatively, I bought myself some books about combat, but they're too technical for me, so you could have one as your payment. Incidentally, if you already have an assignment from elsewhere to kill creatures that can be found within the tower, do come and see me. Fulfil your task within the tower, and I'll give you a special contract that'll work in tandem with it, and give you an additional reward on top. So would you like a job now?
    - (continuea|extraQs)
  - Okay, I'd like a job.
    - **Markus:** Excellent. Take a look at my contracts and see which one you'd like to do.
    - (opens=Slayer contracts)
    - (If the player accepts a slayer contract:)
      - (receives=a slayer contract)
      - The scroll can only track your progress if you carry it while slaying. Bring it back when you've finished.
  - No thanks.
    - **Markus:** Alright, but come back if you change your mind. I can pay you for your work.

#### With a Slayer assignment for a Slayer Tower monster

- **Markus:** I see you've got a Slayer assignment. I'll pay you extra if you take a contract to do your assignment in this tower.
- What would you like to say?
  - What are you offering?
    - **Markus:** You'll get a 20% bonus on Slayer XP earned from killing the monsters, plus a choice of [#] combat XP or [#] coins.
    - (prev)
  - Okay, I'll take it.
    - (receives=a special slayer contract)
    - The scroll can only track your progress if you carry it while slaying. Bring it back when you've finished.
  - Can I have a different contract instead?
    - (If the player already has a slayer contract:)
      - **Markus:** No, you've already got one.
      - (end)
    - (opens=Slayer contracts)
    - (If the player accepts a slayer contract:)
    - (receives=a slayer contract)
    - The scroll can only track your progress if you carry it while slaying. Bring it back when you've finished.
  - No thanks.
    - **Markus:** Alright, but come back if you change your mind. I can pay you for your work.

### Using the Contract interact option on Markus

- (If the player has a Slayer assignment for a Slayer Tower monster:)
  - (continuea|With a Slayer assignment for a Slayer Tower monster)
- (opens=Slayer Contracts)
- (If the player accepts a slayer contract:)
  - (receives=a slayer contract)
  - The scroll can only track your progress if you carry it while slaying. Bring it back when you've finished.
