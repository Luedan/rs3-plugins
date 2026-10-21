# Sir Amik Varze

- **Original Wiki Page**: [Transcript:Sir Amik Varze](https://runescape.wiki/w/Transcript%3ASir%20Amik%20Varze)
- **Letter**: `S`

---

## Dialogue Transcript

{{incomplete|Unknown conditionals for when talking to him about A Void Dance - his responses vary}}

### In the White Knights' Castle

- [Menu]: Choose an option:
  - [Choice]: Who are you?
    - **Sir Amik Varze:** I am the leader of the White Knights of Falador. Why do you seek my audience?
    - (initial|init)
  - [Choice]: cond=Before starting Recruitment Drive|I seek a quest!
    - (see|Recruitment Drive)
  - [Choice]: cond=After A Void Dance|Speak about the A Void Dance quest.
    - {{Transcript missing|unknown conditional - }}
      - **Sir Amik Varze:** Well Player, now that you are a White Knight, I expect you should be out hunting Black Knights for us!
      - (continue)
    - {{Transcript missing|unknown conditional - }}
      - **Sir Amik Varze:** How does life find you today, Player?
      - (continue)
    - [Menu]: Select an Option
      - [Choice]: Can you explain the White Knight honour system again?
        - **Sir Amik Varze:** Sadly we are not as rich as we once were, and there are many White Knights who foolishly lose their combat equipment.
        - **Sir Amik Varze:** We do not think it fair to make a profit from our brethren, so we will sell you equipment at cost, and rebuy it at the same cost, but we will only sell equipment to those we consider responsible enough to wield it correctly.
        - **Sir Amik Varze:**By killing Black Knights, you will increase your reputation with us, by killing White Knights we will obviously think less of you.
        - **Sir Amik Varze:**You can check your White Knight reputation level by looking at your quest journal for the Wanted! Quest, or Sir Vyvin will let you know what level you are at when you go to purchase equipment.
        - **Sir Amik Varze:** Sir Vyvin can be found in Falador Castle, and he will sell you any equipment appropriate to your reputation level.
        - **Sir Amik Varze:** Have fun, and go kill some Black Knights for me!
        - **Player:** Okay Amik, thanks for explaining!
      - [Choice]: Do you know anything about the siege of Falador?
        - (below|siege)
    - [Choice]: Okay, bye!
      - **Player:** Okay, 'bye then Amik!
  - [Choice]: Tell me about the Temple Knights.
    - **Sir Amik Varze:** I cannot tell you much... <br> They are called the Temple Knights, and are an organisation that was founded by Saradomin personally many centuries ago.
    - **Sir Amik Varze:** There are many rumours and fables about their works and actions, but official records of their presence are non-existent.
    - **Sir Amik Varze:** It is a secret organisation of extraordinary power and resourcefulness...
    - **Sir Amik Varze:** Let me put it this way: <br> Should you decide to take them up on their generous offer to join, you will find yourself in an advantageous position that many of this world would envy, and that few are called to occupy.
    - **Player:** Well, that wasn't quite as helpful as I thought it would be... but thanks anyway, I guess.
    - (initial|init)
  - [Choice]: Do you know anything about the siege of Falador?
    - {{anchor|siege}} **Player:** Do you know anything about the siege of Falador?
    - **Sir Amik Varze:** Ah yes, the Kinshra siege was a close-run thing indeed.
    - **Sir Amik Varze:** All hope seemed lost. Then she returned - Kara-Meir - with Sir Theodore at her side.
    - **Player:** Sir Theodore? I haven't seen anyone of that name around here.
    - **Sir Amik Varze:** No, you wouldn't have. He is...no longer with us.
    - **Player:** Oh, I'm sorry.
    - **Sir Amik Varze:** So am I, young [man/woman]. So am I.
  - [Choice]: cond=Historical, during the Battle of Lumbridge|Do you have any news?
    - **Player:** Do you have any news?
    - **Sir Amik Varze:** It's a glorious time for the White Knights - Saradomin has returned!
    - **Sir Amik Varze:** He is defending us from the evil wizardry of Zamorak west of Lumbridge castle, and he's asked our order for help!
    - **Sir Amik Varze:** So it is the duty of all White Knights to heed the call, and take up arms against the ancient enemy.
    - **Sir Amik Varze:** By the grace of Saradomin, we shall be victorious!
  - [Choice]: Farewell.
    - (end)

### Manor Farm


#### Help


##### Before having completed the request

- [Menu]: What would you like to do?
  - [Choice]: Ask about their request.
    - **Player:** What're you requesting today?
    - **Sir Amik Varze:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **Sir Amik Varze:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - **Sir Amik Varze:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal]
    - **Sir Amik Varze:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - **Sir Amik Varze:** If you complete this, I'll give you : Some White knight armour x 15. I'm sure you'll gain some reputation with the farming guild too!
    - **Sir Amik Varze:** You'll have to be quick though!, I'm only here for [number] days, [number] hours and [number] minutes. To be exact.
  - [Choice]: Give them the items & animals for their request
    - ((Without the requested items:))
      - **Sir Amik Varze:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **Sir Amik Varze:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - **Sir Amik Varze:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal]
      - **Sir Amik Varze:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - ((With the requested items:))
      - (removes=the requested items) (receives=the reward)
      - For completing this request you've received Brassica primer x 3.
      - ((Repeated in a pop-up:))
        - {{Pop-up|For completing this request you've received Brassica primer x 3.|color=#EBE0BC}}
        - (continue)
      - [You've received : [Reward] x 15<br>And 13,750 farming reputation.]

##### After having completed the request

- **Sir Amik Varze:** Thank you for your help!
- A new request will be available in [time]{{Sic|..}}

#### Hand in hard request


##### Before having completed the request


##### Without requested items

- **Sir Amik Varze:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **Sir Amik Varze:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- **Sir Amik Varze:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal]
- **Sir Amik Varze:** I'm also looking for some produce, so I'll need : [Produce] x [number]

##### With requested items

- (Condition: With multiple applicable animals:)
  - [Menu]: Which animal would you like to hand in?
    - ((Repeated for each applicable animal:))
      - [Choice]: [Animal name]
        - (continue)
- (removes=the requested items) (receives=the reward)
- For completing this request you've received Brassica primer x 3.
- (pop-up)
  - {{Pop-up|For completing this request you've received Brassica primer x 3.}}
  - (continue)
- [You've received : [Reward] x 15<br>And 13,750 farming reputation.]

##### After having completed the request

- You've already completed this request, there will be a new weekly request in [time]{{Sic|..}}
