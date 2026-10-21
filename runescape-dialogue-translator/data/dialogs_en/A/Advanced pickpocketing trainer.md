# Advanced pickpocketing trainer

- **Original Wiki Page**: [Transcript:Advanced pickpocketing trainer](https://runescape.wiki/w/Transcript%3AAdvanced%20pickpocketing%20trainer)
- **Letter**: `A`

---

## Dialogue Transcript


### Standard dialogue


#### Without a blackjack equipped

- The trainer does his best to focus on you.
- ** Advanced pickpocketing trainer: ** I teach 'Aggressive Pickpocketing'. You need t' be be'er equipped before I can 'elp yer - git yerself a blackjack.

#### With a blackjack equipped

- The trainer does his best to focus on you.
- ** Advanced pickpocketing trainer: ** A cosh is a fan'astic tool, and that's no 'yperbole. Know 'ow to use it?
- [Menu]: Select an option
  - [Choice]: About those hankies...|cond=If it is not the first time:
    - [Menu]: Select an option
      - [Choice]: What are these handkerchiefs for?
        - **Advanced pickpocketing trainer:** Oh, we use them to keep track of our members' training regimen. Blue handkerchiefs will earn you one point, red ones are worth four. You can claim a reward from any trainer with your hanky points.
        - [Menu]: Select an option
          - [Choice]: What are these handkerchiefs for?|cond=Only if previously not selected:
            - (above|handkerchiefs-for)
          - [Choice]: How often can I do this?
            - **Advanced pickpocketing trainer:** The number of hanky points you can claim for depends on your dedication to the art. At the moment, you can claim <number> hanky points' worth of training per week.
            - {{tact|other}}
          - [Choice]: Which activities give which handkerchiefs?
            - **Advanced pickpocketing trainer:** Our pickpocketing trainers, safes and easy chests carry blue hankies; red hankies can be found on the coshing trainers and behind harder locks.
            - {{tact|other}}
          - [Choice]: Bye for now.
            - ** Player:** Bye for now.
      - [Choice]: How many hanky points do I have?
        - **Advanced pickpocketing trainer:** You have collected <number> hanky points. You may claim the reward for up to <number> more hanky points this week.
      - [Choice]: I'd like to claim a reward for my hanky points.
        - ''If the player has hanky points
          - **Advanced pickpocketing trainer:** Wicked, mate. Le's get you set up.
          - You gain <number> Thieving XP. You have <number> points remaining, and may turn in up to <number> more points this week.
        - ''If the player has no hanky points
          - **Advanced pickpocketing trainer:** You what? You've got no hanky points to 'and in.
      - [Choice]: Bye for now.
        - ** Player:** Bye for now.
  - [Choice]: What are these handkerchiefs for?|cond=Only for the first time:
    - ** Player:** What are these handkerchiefs for?
    - (above|handkerchiefs-for)
  - [Choice]: I've had some experience, yes.
    - ** Player:** I've had some experience, yes.
    - **Advanced pickpocketing trainer:{{anchor|ngabh}}** You can prac'ise on me if yer want, but only wiv a training cosh...
  - [Choice]: Remind me of the finer points, please.
    - ** Player:** Remind me of the finer points, please?
    - **Advanced pickpocketing trainer:** A blackjack, cosh or sap is a tool for openin' the pockets of people who keep a be'er eye on their wallet than on the back of their own 'ed.
    - **Advanced pickpocketing trainer:** First you need to get 'em out of the reach of pryin' eyes, then just give 'em a good whack right 'ere and down they'll go.
    - **Advanced pickpocketing trainer:** Then you can see what they've got that you migh' want. Got it?
    - ** Player:** Yes, that was blunt enough. Thank you.
    - {{tact|continuea|ngabh}}

### Blackjack dialogue


#### Lure

''One of the following dialogues plays at random:

##### Dialogue 1

- ** Player:** Watch out! The fellow behind you has a club!
- **Advanced pickpocketing trainer:** Wha?

##### Dialogue 2

- ** Player:** Behind you! A three-headed monkey!
- **Advanced pickpocketing trainer:** Wha?

##### Dialogue 3

- ** Player:** That's the third biggest platypus I've ever seen!
- **Advanced pickpocketing trainer:** Wha?

##### Dialogue 4

- ** Player:** Look over THERE!
- **Advanced pickpocketing trainer:** Wha?

##### Dialogue 5

- ** Player:** Look! An eagle!
- **Advanced pickpocketing trainer:** Wha?

##### Dialogue 6

- ** Player:** Your shoelace is untied.
- **Advanced pickpocketing trainer:** Wha?

##### If a wooden blackjack is equipped

- ** Player:** I'll need a training cosh to practise my technique with.

#### Knock-out

- **Advanced pickpocketing trainer:**{{RSChat|Blarg!}}
- You smack the trainer over the head as politely as you can.
- **Advanced pickpocketing trainer:**{{RSChat|Anuvva bruise for me collection...}}

##### Without luring

- ** Player:** I need to divert his attention first.

##### Without level 40 Thieving

- You need a Thieving level of at least 40 to practise coshing.

#### Loot

- You empty the man's pocket and drape the red handkerchief over him.
- You gain 4 hanky points.

##### Without being knocked out

- You should knock him out before attempting to loot him.
