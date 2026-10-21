# Brimstail

- **Original Wiki Page**: [Transcript:Brimstail](https://runescape.wiki/w/Transcript%3ABrimstail)
- **Letter**: `B`

---

## Dialogue Transcript


### In Brimstail's cave


#### Before The Grand Tree

- **Brimstail:** Hello adventurer, what can I do for you?
- [Menu]: Choose an option:
  - [Choice]: Can you teleport me to the Rune Essence?
    - **Player:** Can you teleport me to the Rune Essence?
    - **Brimstail:** Okay. Hold onto your hat!
    - **Brimstail:** {{RSChat|Senventior disthine molenko!}}
    - {{Qact|Brimstail teleports you to the Rune Essence mine}}
  - [Choice]: Nothing for now, thanks!
    - **Player:** Nothing for now, thanks!
    - **Brimstail:** Ok. Just remember that a friend of a wizard is a friend of mine!

#### After The Grand Tree

- (see|The Eyes of Glouphrie)

#### After The Eyes of Glouphrie

- **Brimstail:** Hello adventurer, what can I do for you?
- [Menu]: Choose an option:
  - [Choice]: Hello, just wanted a chat.
    - **Player:** Hello, just wanted a chat.
    - **Brimstail:** It's always a pleasure to catch up with another mage! Especially one who has helped me so much!
    - (Condition: If the player has lost the small crystal seed:)
      - **Brimstail:** Oh, by the way, I found this odd thing lying around, does it belong to you?
      - [Brimstail shows you a small crystal seed.]
      - **Player:** Oh, yes - I was wondering where that had gone...
      - (receives=small crystal seed)
      - **Brimstail:** You should look after your things more carefully you know...
      - **Player:** Thanks!
    - (Condition: If the player has the small crystal seed:)
      - **Brimstail:** How are your researches going?
      - **Player:** Oh, not so bad. I'll let you know if I find anything I think you'll find interesting...
      - **Brimstail:** Thanks! I'd appreciate that.
      - (Condition: If the seed has been made into a chime:)
        - (end)
      - (Condition: If the seed is still a seed:)
        - **Player:** What's this seed do?
        - **Brimstail:** Fascinating... a crystal seed. You should have a look at the crystal bowl in the other room, must be related.
        - **Player:** Thanks, I'll do that.
      - (Condition: If the seed has been made into a saw:)
        - **Player:** What's this crystal saw do?
        - (Condition: Before While Guthix Sleeps:)
          - **Brimstail:** I've no idea, it must have been Oaknock's, he liked talking to the elves.
          - **Player:** Where would I find out how the thing works?
          - **Brimstail:** Errrm, I'm not sure. Have a chat with Hazelmere, maybe he'll know. He was around when Oaknock was alive and might have seen him use it.
          - **Player:** Excellent idea, I'll do that. Thanks.
        - (Condition: After While Guthix Sleeps:)
          - **Brimstail:** I recently read that Oaknock used something like this to help him construct devices that were too complicated for him to build using his skill alone. Perhaps that's what this saw does.
          - [The saw will add three levels to your effective Construction level when you are building something that requires a saw.]
  - [Choice]: cond=After The Path of Glouphrie|I've been investigating another watcher in the Tree Gnome Village.
    - **Player:** I've been investigating another watcher in the Tree Gnome Village.
    - **Player:** And, as a consequence, I've found an underground cave complex full of warped terrorbirds and tortoises. It seems to be underneath Arposandra or, at least, a city with gnomes in that use talking terrorbirds as guards.
    - **Brimstail:** Wow! You've really found Arposandra.
    - **Player:** I think so, though I can't get in. It's all blocked up. But I'll find a way...eventually.
    - **Brimstail:** Well, good luck!
  - [Choice]: I need to mine some rune essence.
    - (above)

### Treasure Trails


#### Easy

- **Brimstail:** Well done!
- (removes=the old clue scroll (easy))
- (If the trail continues:)
  - (receives=a new clue scroll (easy))
  - [Brimstail has given you another clue scroll!]
- (If the trail ends:)
  - (receives=reward casket (easy))
  - [You've found a casket!]

#### Medium (replacement for Hazelmere)

- (Condition: Only the first time:)
  - **Brimstail:** Ah, I know what you're here for.
  - **Player:** You do?
  - **Brimstail:** Yes. But before I let you move on, you must help me with this challenge.
- (receives=challenge scroll (medium))
- [Brimstail has given you a challenge scroll!]

##### When talked to again

- **Brimstail:** Do you know the answer to the question?
- Enter amount:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Brimstail:** This doesn’t sound right.
- (Condition: When given the correct answer:)
  - (removes=the clue scroll (medium) and challenge scroll (medium))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [Brimstail has given you another clue scroll!]
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [You've found a casket!]
  - **Brimstail:** Thank you!
