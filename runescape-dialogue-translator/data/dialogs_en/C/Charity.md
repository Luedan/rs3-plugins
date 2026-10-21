# Charity

- **Original Wiki Page**: [Transcript:Charity](https://runescape.wiki/w/Transcript%3ACharity)
- **Letter**: `C`

---

## Dialogue Transcript


### First time

- **Charity:** Hey, I'm Charity. For a limited time only, I'll be the host of the interactive trivia game, The Drop!
- **Player:** Sounds great! How does it work?
- **Charity:** You'll be asked a series of RuneScape themed questions. Answer every question correctly and you'll bag yourself a nice reward. Each time you play, Jagex will donate £1 to charity, up to a whopping maximum of £34,500! I know what you're thinking. Why are they giving all of that money to me?
- **Player:** ... Anyway, how do I take part?
- **Charity:** I'll announce each time The Drop opens. You'll then have 2 minutes to join before the game starts.
- **Player:** Thanks!
- **Charity:** Talk to me again for more information, or use the 'Quick join' option to jump straight into the game!

### Standard dialogue

- **Charity:** Hey again, how can I help you?
- Select an option{{anchor|init}}
  - Ask about The Drop.
    - **Player:** Could you tell me about The Drop?
    - **Charity:** Of course! The Drop is an interactive trivia game. You'll be asked a series of RuneScape themed questions. Answer every question correctly and you'll bag yourself a nice reward. Each time you play, Jagex will donate £1 to charity, up to a whopping maximum of £34,500!
    - **Player:** Great, thank you!
    - (initial|init)
  - Enter The Drop.
    - ((If The Drop is not currently open:))
      - The Drop is not currently open.
    - ((If The Drop is open:))
      - ((If the player has a follower out or a Summoning pouch in backpack:))
        - **Charity:** Sorry, no pets, followers or summoning pouches allowed in The Drop!
      - ((If the player doesn't have space in backpack:))
        - **Charity:** Sorry, you don't have enough inventory space to claim the reward if you win.
      - (The player is taken into The Drop.)
      - Welcome to The Drop - the next game will start soon!
  - Ask about rewards.
    - **Player:** Are there any rewards involved?
    - **Charity:** Of course! If you answer all of the questions correctly, you'll bag yourself the 'Apart Together' title. You'll also bag yourself some prismatic stars and lamps. Additionally, just for participating, Jagex will donate £1 to charity, up to a whopping maximum of £34,500!
    - **Player:** Great, thank you!
    - (initial|init)
  - Ask about charitable giving.
    - **Player:** Could you give me some more information about charity?
    - **Charity:** Of course! I'm Charity, I spend a lot of my time... Only joking! Jagex will be making a donation of £100,000 to our mental health charity partners. Players can help meet this goal by entering The Drop! For each participation, £1 will be donated to charity.
    - Would you like more information?
      - Yes, take me to the newspost.
        - ((Opens £100k+ for mental health - how to get involved!))
        - (initial|init)
      - No.
        - (initial|init)
  - Goodbye
    - **Player:** Goodbye.
    - **Charity:** Bye for now.

### "Claim rewards" option

*If the player hasn't claimed the rewards:*
- **Charity:** You can earn your rewards for this event by correctly answering all 12 questions in The Drop.
*If the player has claimed the rewards:*
- **Charity:** You've already received all of the rewards for this event.

### Overhead dialogue


#### When The Drop isn't active

- ((Every minute:))
  - **Charity:** {{RSChat|The Drop starts in [number] minute[s]!}}

#### When The Drop is active

- ((Every minute:))
  - **Charity:** {{RSChat|The Drop has started! Talk to me or use the 'Quick join' option to take part.}}
