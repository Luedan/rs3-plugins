# Villager

- **Original Wiki Page**: [Transcript:Villager](https://runescape.wiki/w/Transcript%3AVillager)
- **Letter**: `V`

---

## Dialogue Transcript


### Talk-to

- {{trandom}}
  - (Condition: Dialogue 1:)
    - **Player:** Hello, how's it going?
    - **Player:** Do you wish to trade? {{anchor|one}}
    - **Villager:** No, I have nothing I wish to get rid of. If you want to do some trading, there are plenty of shops and market stalls around though.
  - (Condition: Dialogue 2:)
    - **Player:** Hello, how's it going?
    - **Player:** I'm in search of a quest. {{anchor|two}}
    - **Villager:** I'm sorry I can't help you there.
  - (Condition: Dialogue 3:)
    - **Player:** Hello, how's it going?
    - **Player:** I'm in search of enemies to kill. {{anchor|three}}
    - **Villager:** Well there's always those wild Ugthanki, snakes and wolves to kill on the outskirts of town.
  - (Condition: Dialogue 4:)
    - **Player:** Hello, how's it going?
    - **Villager:** You know, even a stopped clock tells the right time twice a day.
    - **Player:** What are you talking about?
    - **Villager:** Uneducated fool! It will die, it will die!
    - **Player:** Ohhh kaaay, I'll leave you to it then.
  - (Condition: Dialogue 5:)
    - **Player:** Hello, how's it going?
    - **Villager:** I'm busy right now.
  - (Condition: Dialogue 6:)
    - **Player:** Hello, how's it going?
    - **Villager:** I'm very well thank you.
  - (Condition: Dialogue 7:)
    - **Player:** Hello, how's it going?
    - **Villager:** Get out of my way, I'm in a hurry!
  - (Condition: Dialogue 8:)
    - **Player:** Hello, how's it going?
    - **Villager:** I'm fine, how are you?
    - **Player:** Very well, thank you.
  - (Condition: Dialogue 9:)
    - **Player:** Hello, how's it going?
    - **Villager:** Do I know you? I'm in a hurry!
  - (Condition: Dialogue 10:)
    - **Player:** Hello, how's it going?
    - **Villager:** Hello there! Nice weather we've been having.
  - (Condition: Dialogue 11:)
    - **Player:** Hello, how's it going?
    - **Villager:** Not too bad, thanks.
  - (Condition: Dialogue 12:)
    - **Player:** Hello, how's it going?
    - **Villager:** None of your business.
  - (Condition: Dialogue 13:)
    - **Player:** Hello, how's it going?
    - **Villager:** I think we need a new mayor. The one we've got isn't very good.
  - (Condition: Dialogue 14:)
    - **Player:** Hello, how's it going?
    - **Villager:** That is classified information.
  - (Condition: Dialogue 15:)
    - **Player:** Hello, how's it going?
    - **Villager:** Here here here.
    - **Player:** What are you talking about?
    - **Villager:** Uneducated fool! It will die, it will die!
    - **Player:** Ohhh kaaay, I'll leave you to it then
  - (Condition: Dialogue 16:)
    - **Player:** Hello, how's it going?
    - **Villager:** Who are you?
    - **Player:** I'm a bold adventurer.
    - **Villager:** Ah, a very noble profession.
  - (Condition: Dialogue 17:)
    - **Player:** Hello, how's it going?
    - **Villager:** How can I help you?
    - [Menu]: Select an Option
      - [Choice]: Do you wish to trade?
        - (above|one)
      - [Choice]: I'm in search of a quest.
        - (above|two)
      - [Choice]: I'm in search of enemies to kill.
        - (above|three)

### Pickpocket


#### If the villager is conscious{{anchor|thief}}

- {{trandom}}
  - (Condition: Dialogue 1:)
    - **Villager:** {{RSChat|What do you think you're doing?}}
    - You fail to pick the villager's pocket.
    - You've been stunned.
  - (Condition: Dialogue 2:)
    - **Villager:** {{RSChat|Thief! Thief! Get away from me.}}
    - You fail to pick the villager's pocket.
    - You've been stunned.

#### If the villager is unconscious

- (receives=5 coins)

### Lure

- **Player:** Psst. Come here. I want to show you something.
- **Villager:** What is it?
- **Player:** It's a surprise! Follow me.

### Knock-Out


#### If there are other NPCs around

- Perhaps I shouldn't do this just yet. I think someone will see me.

#### If the player does not have a blackjack equipped

- I need a different weapon to do this, I want to knock them out, not kill them.

#### If the player has a blackjack equipped

- {{Qact|The player hits the villager over the head with the blackjack. The villager falls to the ground.}}
- You smack the villager over the head and render them unconscious.
- **Villager:** {{RSChat|Zzzzzz}}
- {{Qact|The villager gets up.}}
- **Villager:** {{RSChat|Aghh, my head.}}
- (Condition: If the player had pickpocketed the villager:)
  - (continuea|thief)
