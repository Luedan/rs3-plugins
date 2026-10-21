# Gnome trainer

- **Original Wiki Page**: [Transcript:Gnome trainer](https://runescape.wiki/w/Transcript%3AGnome%20trainer)
- **Letter**: `G`

---

## Dialogue Transcript


### In the Tree Gnome Stronghold


#### Standard dialogue

- {{trandom}}
  - [Choice]: Dialogue 1
    - **Gnome trainer:** This is training, soldier. Little time for chat! What do you want?
    - (continue)
  - [Choice]: Dialogue 2
    - **Gnome trainer:** This is a serious training area. What do you want?
    - (continue)
  - [Choice]: Dialogue 3
    - **Gnome trainer:** This isn't a grannies' tea party. What do you want?
    - (continue)
- [Menu]: What do you want to say?
  - [Choice]: What is this place?
    - **Player:** What is this place?
    - **Gnome trainer:** This, my friend, is where we train and improve our Agility. It's an essential skill.
    - **Player:** It looks easy enough.
    - **Gnome trainer:** If you complete the course, from the slippery log to the end, your Agility will increase more rapidly than by repeating just one obstacle.
  - [Choice]: What's so special about this course, then?
    - **Player:** What's so special about this course, then?
    - **Gnome trainer:** Well, it's where most people tend to start training. We've also made an extension for those who are up for the challenge.
    - **Player:** An extension?
    - (Condition: If the player's Agility level is at least 85:)
      - **Gnome trainer:** Well, you look like you can handle it, so I'll fill you in.
      - **Gnome trainer:** If you follow the course as normal, you'll see a new branch before the balancing rope. This is the way up to the new route.
      - **Gnome trainer:** It's taken a while to strengthen the branch, but you should find yourself agile enough to get up to the next level. I suggest you check it out.
      - **Player:** I might just do that. Anything else I need to know?
      - **Gnome trainer:** Yes. If you do the tougher route, you'll get a much larger experience bonus at the end of it - just make sure you've completed all the obstacles leading up to the branch!
      - **Gnome trainer:** Oh, I nearly forgot: if you manage to do 250 laps of the advanced route without a fault, we'll give you a special item. We'll keep a tally of your laps, so you can always check your progress.
    - (Condition: If the player's Agility level is below 85:)
      - **Gnome trainer:** It's a challenge that I think is a bit out of your depth. I'll give you more information when you're slightly more experienced.
      - You need an Agility level of 85 to attempt the improved gnome course.
  - [Choice]: cond=If at least one lap of the Advanced Gnome Stronghold Course has been completed:|Can I talk about rewards?
    - **Player:** Can I talk about rewards?
    - (Condition: If the player has claimed the Agile legs:)
      - **Gnome trainer:** Of course. How can I help?
      - **Player:** Any chance of some more Agile legs?
      - (receives=agile legs)
      - **Gnome trainer:** Here you go, try not to lose them.
    - (Condition: If the player has not yet claimed the Agile legs:)
      - (Condition: If the player has completed 250 perfect advanced route laps:)
        - **Gnome trainer:** Well, it looks like you've completed our challenge!
        - **Gnome trainer:** Take this as a reward: some Agile legs. You'll find yourself much lighter than usual while wearing them.
        - **Gnome trainer:** They are made from the toughest material we gnomes could find, so it might even protect you in combat.
        - (receives=agile legs)
        - **Gnome trainer:** There you go. Enjoy!
      - (Condition: If the player has not completed 250 perfect advanced route laps yet:)
        - **Gnome trainer:** Well, you've still got work to do. Your lap count is *<number of laps completed>*. It's 250 successful laps for the reward!
  - [Choice]: I'm done for now.
    - **Player:** I'm done for now. Bye.
    - **Gnome trainer:** Bye for now. Come back if you need any assistance.

#### On the advanced route

- **Gnome trainer:** Wow, nice to see experienced people taking it to the next level of training.
- **Player:** Thanks. So this is the advanced route the other gnomes are talking about?
- **Gnome trainer:** It sure is. You've already made the climb up here, now all you need to do is run across this sign here.
- **Player:** Seriously?
- **Gnome trainer:** Oh yes, totally. When you've made it across, look for the swings to get to the northern section. When you land from them, try to vault the branches into the pipe and you should slide out to the finish line!
- **Player:** And will I still have my legs intact when I've done all this?
- **Gnome trainer:** Yes. Of course.

#### Treasure Trails


##### Receiving the puzzle box

- **Gnome trainer:** You're not done yet! Do this for me!
- (receives=puzzle box)
- [The gnome trainer has given you a puzzle box!]

##### When talked to again without solving the puzzle

- **Gnome trainer:** My baby sister can do puzzles better than that!

##### When talked to again after solving the puzzle

- (Condition: If the trail continues:)
  - (removes=the old clue scroll (hard) and puzzle box) (receives= the new clue scroll (hard))
  - [The gnome trainer has given you another clue scroll!]
  - (continue)
- (Condition: If the trail ends:)
  - (removes=the old clue scroll (hard) and puzzle box) (receives=reward casket (hard))
  - [You've found a casket!]
  - (continue)
- **Gnome trainer:** Well done!

#### Overhead dialogue


##### Walking across the log balance

- **Gnome trainer:** {{RSChat|Okay get over that log, quick quick!}}

##### Climbing over the first obstacle net

- **Gnome trainer:** {{RSChat|Move it, move it, move it!}}

##### Climbing the tree branch

- **Gnome trainer:** {{RSChat|That's it - straight up}}

##### Walking on the balancing rope

- **Gnome trainer:** {{RSChat|Come on scaredy cat, get across that rope!}}

##### Climbing over the second obstacle net

- **Gnome trainer:** {{RSChat|My Granny can move faster than you.}}

##### Climbing the tree leading to the advanced route

- **Gnome trainer:** {{RSChat|Terrorbirds could climb faster than that!}}

##### Running across the signpost

- **Gnome trainer:** {{RSChat|Come on! I'd be over there by now.}}
