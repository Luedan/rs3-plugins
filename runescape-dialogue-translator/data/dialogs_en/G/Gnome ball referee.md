# Gnome ball referee

- **Original Wiki Page**: [Transcript:Gnome ball referee](https://runescape.wiki/w/Transcript%3AGnome%20ball%20referee)
- **Letter**: `G`

---

## Dialogue Transcript


### First-time dialogue

- **Player:** Hello.
- **Gnome ball referee:** Hi, welcome to Gnomeball. It's pretty simple really, you take the ball from me, charge at the gnome defence and try to throw the ball through the net using your ranged skill. It's a rough game but great fun. It's also great for improving agility. So do you fancy a game?
- [Menu]: Select an option
  - [Choice]: Looks too dangerous for me!
    - **Player:** Looks too dangerous for me!
    - **Gnome ball referee:** You may be right, we've seen humans die on this field.
  - [Choice]: Ok then, I'll have a go.
    - **Player:** Ok then, I'll have a go.
    - **Gnome ball referee:** Great stuff! There are few rules to Gnomeball, so it can get a bit rough.
    - **Gnome ball referee:** You can pass to the green winger gnomes. Then you can make a run and they'll pass back. Otherwise, if you're feeling brave, you can just charge and dodge.
    - **Player:** Sounds easy enough.
    - **Gnome ball referee:** The main aim is to leave with no broken limbs. I think you should be fine.
    - **Gnome ball referee:** {{RSChat|Peeeeeeeeeep}}
    - (receives=Gnomeball)

### Subsequent dialogue


#### When not wielding a Gnomeball

- **Player:** Hello.
- **Gnome ball referee:** Hi, welcome back to Gnomeball. Would you like to hear the rules again?
- [Menu]: Select an Option
  - [Choice]: Yes please.
    - **Gnome ball referee:** It's pretty simple really, you take the ball from me, charge at the gnome defence and try to throw the ball through the net using your ranged skill. It's a rough game but great fun. It's also great for improving agility.
    - **Gnome ball referee:** You can pass to the green winger gnomes. Then you can make a run and they'll pass back. Otherwise, if you're feeling brave, you can just charge and dodge.
    - **Player:** Sounds easy enough.
    - **Gnome ball referee:** The main aim is to leave with no broken limbs. I think you should be fine.
    - **Gnome ball referee:** {{RSChat|Peeeeeeeeeep}}
    - (receives=Gnomeball)
  - [Choice]: I just want to play.
    - **Player:** I just want to play.
    - **Gnome ball referee:** Ok... Let's play GNOMEBALL!
    - **Gnome ball referee:** {{RSChat|Peeeeeeeeeep}}
    - (receives=Gnomeball)
  - [Choice]: No, I don't want to play.
    - **Player:** No, I don't want to play.
    - **Gnome ball referee:** Ok, never mind. Maybe next time?

#### When wielding a Gnomeball

- **Gnome ball referee:** You have a ball in play. Do you need to hear the rules again?
- [Menu]: Select an Option
  - [Choice]: Yes please.
    - **Gnome ball referee:** It's pretty simple really, you take the ball from me, charge at the gnome defence and try to throw the ball through the net using your ranged skill. It's a rough game but great fun. It's also great for improving agility.
    - **Gnome ball referee:** You can pass to the green winger gnomes. Then you can make a run and they'll pass back. Otherwise, if you're feeling brave, you can just charge and dodge.
    - **Player:** Sounds easy enough.
    - **Gnome ball referee:** The main aim is to leave with no broken limbs. I think you should be fine.
    - **Gnome ball referee:** The ball you have in your hand is fine to play with... Game on.
  - [Choice]: No, thanks.
    - **Player:** No, thanks.
    - **Gnome ball referee:** Ok, good luck.

#### After scoring a goal

- **Gnome ball referee:** Have a new ball!
- **Gnome ball referee:** {{RSChat|Peeeeeeeeeep}}
- (receives=Gnomeball)

#### After winning the game

- (receives=Gnomeball)
- **Gnome ball referee:** You won! Here, have a gnomeball.

### Treasure Trails


#### Receiving the challenge scroll

- (Condition: Only the first time:)
  - **Gnome ball referee:** Right, you haven't finished quite yet.
  - **Player:** Ugh.
  - **Gnome ball referee:**Answer this for me.
- (receives=challenge scroll (medium))
- [ref] has given you a challenge scroll!}}

#### When talked to again

- **Gnome ball referee:** Please enter the answer to the question.
- Enter amount:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Gnome ball referee:** Wrong answer!
- (Condition: When given the correct answer:)
  - (removes=the clue scroll (medium) and challenge scroll (medium))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [The referee has given you another clue scroll!]
    - (continue)
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [You've found a casket!]
    - (continue)
  - **Gnome ball referee:** Well done!
