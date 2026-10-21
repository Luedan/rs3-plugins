# Pickpocketing trainer

- **Original Wiki Page**: [Transcript:Pickpocketing trainer](https://runescape.wiki/w/Transcript%3APickpocketing%20trainer)
- **Letter**: `P`

---

## Dialogue Transcript


### In the Thieves' Guild


#### Talking to him


##### First time

- **Player:** Hello there.
- **Pickpocketing trainer:** Ah, Player. I'm doing classes on picking pockets, if you're interested.
- [Menu]: Select an Option
  - [Choice]: What are these handkerchiefs for?
    - **Player:** What are these handkerchiefs for?
    - **Pickpocketing trainer:** Oh, we use them to keep track of our members' training regimen. Blue handkerchiefs will earn you one point, red ones are worth four. You can claim a reward from any trainer with your hanky points.
    - (other)
  - [Choice]: How often can I do this?
    - **Pickpocketing trainer:** The number of hanky points you can claim for depends on your dedication to the art. At the moment, you can claim [number] hanky points' worth of training per week.
    - (other)
  - [Choice]: Which activities give which handkerchiefs?
    - **Player:** Which activities give which handkerchiefs?
    - **Pickpocketing trainer:** Our pickpocketing trainers and chests all carry blue hankies at present. We're looking to expand when we get more staff.
    - (other)
  - [Choice]: Bye for now.
    - ** Player:** Bye for now.

##### Subsequently

- **Player:** Hello there.
- **Pickpocketing trainer:** Ah, Player. I'm doing classes on picking pockets, if you're interested.
- [Menu]: Select an Option
  - [Choice]: About those hankies...
    - [Menu]: Select an Option
      - [Choice]: What are these handkerchiefs for?
        - **Pickpocketing trainer:** Oh, we use them to keep track of our members' training regimen. Blue handkerchiefs will earn you one point, red ones are worth four. You can claim a reward from any trainer with your hanky points.
        - [Menu]: Select an Option
          - [Choice]: How often can I do this?
            - **Pickpocketing trainer:** The number of hanky points you can claim for depends on your dedication to the art. At the moment, you can claim [number] hanky points' worth of training per week.
            - (other)
          - [Choice]: Which activities give which handkerchiefs?
            - (Condition: Before From Tiny Acorns:)
              - **Pickpocketing trainer:** Our pickpocketing trainers and chests all carry blue hankies at present. We're looking to expand when we get more staff.
            - (Condition: After From Tiny Acorns:)
              - **Pickpocketing trainer:** Our pickpocketing trainers, safes and easy chests carry blue hankies; red hankies can be found on the coshing trainers and behind harder locks.
            - (other)
          - [Choice]: Bye for now.
            - ** Player:** Bye for now.
      - [Choice]: How many hanky points do I have?
        - (below|Check-points)
  - [Choice]: Not at the moment, thanks.
    - **Pickpocketing trainer:** You can give it a try with myself or my colleagues, although we've not got anything but hankies.
  - [Choice]: Give me a few pointers, then.
    - **Pickpocketing trainer:** Picking a pocket is a simple thing, really.
    - **Pickpocketing trainer:** Just act casual, keep your fingers loose, and be sure you can take a beating if you're spotted.
    - **Pickpocketing trainer:** Most people don't take kindly to someone running a hand through their belongings, and they'll give you a good whack if they catch you at it.
    - ** Player:** Thank you for that stunning revelation.
    - **Pickpocketing trainer:** You can give it a try with myself or my colleagues, although we've not got anything but hankies.

#### Pickpocket


##### Failing

- **Pickpocketing trainer:** {{RSChat|No, no, not like that.}}
- You attempt to pick the man's pocket.
- You fail to pick the trainer's pocket.
- You've been stunned.

##### Succeeding

- You attempt to pick the man's pocket.
- You retrieve a blue handkerchief and hand it back to the trainer.
- (Condition: If hanky points can still be gained for the week:)
  - [You gain a hanky point.]
- (Condition: If no more hanky points can be gained for the week:)
  - You have reached the maximum number of hanky points allowed at your level.

#### Check-points

- **Player:** How many hanky points do I have?
- **Pickpocketing trainer:** You have collected [no hanky points yet/(number) hanky points]. You may claim the reward for up to [number] more hanky points this week.
- [Menu]: Select an Option
  - [Choice]: What are all these handkerchiefs for?
    - (above)
  - [Choice]: I'd like to claim a reward for my hanky points.
    - **Player:** I'd like to claim a reward for my hanky points!
    - (Condition: With no hanky points to claim:)
      - **Pickpocketing trainer:** You have no hanky points to claim! Try some of the guild's training exercises.
    - (Condition: With hanky points to claim:)
      - **Pickpocketing trainer:** Sure thing! Let's see now...
      - (receives=Thieving XP)
      - [You gain [number] Thieving XP. You have 0 points remaining, and may turn in up to [number] more points this week.]
    - (Condition: Having claimed the maximum hanky points for the week:)
      - **Pickpocketing trainer:** Sorry, you've claimed as many hanky points this week as you may at your level.
  - [Choice]: Bye for now.
    - ** Player:** Bye for now.
