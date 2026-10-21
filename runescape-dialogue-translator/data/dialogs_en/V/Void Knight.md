# Void Knight

- **Original Wiki Page**: [Transcript:Void Knight](https://runescape.wiki/w/Transcript%3AVoid%20Knight)
- **Letter**: `V`

---

## Dialogue Transcript


### Standard dialogue

- **Void Knight:** Hi, how can I help you?
- **CHOOSE AN OPTION:**
  - Who are you?
    - **Player:** Who are you?
    - **Void Knight:** I'm a Void Knight, one of the order of Guthix. We are warriors of balance who do Guthix's work here in Gielinor.
    - **SELECT AN OPTION**
      - Wow, can I join?
        - **Player:** Wow, can I join?
        - **Void Knight:** Entry is strictly invite only, however we do need help continuing Guthix's work.
        - **SELECT AN OPTION**
          - What kind of work?
            - (below|what-kind-of-work)
          - Good luck with that.
            - **Player:** Good luck with that.
      - What kind of work?
        - **Player:** What kind of work?
        - **Void Knight:** Ah well you see we try to keep Gielinor as Guthix intended, it's very challenging. Actually we've been having some problems recently, maybe you could help us?
        - **SELECT AN OPTION**
          - What's the problem?
            - **Player:** What's the problem?
            - **Void Knight:** Well the order has become quite diminished over the years, it's a very long process to learn the skills of a Void Knight. Recently there have been breaches into our realm from somewhere else, and strange creatures have been pouring through. We can't let that happen, and we'd be very grateful if you'd help us.
            - (continue|help-options)
          - What's 'Gielinor'?
            - (below|whats-gielinor)
          - I'd rather not, sorry.
            - **Player:** I'd rather not, sorry.
      - What's 'Gielinor'?
        - **Player:** What's 'Gielinor'?
        - **Void Knight:** It is the name that Guthix gave to this world, so we honour him with its use.
      - Uh huh, sure.
        - **Player:** Uh huh, sure.
  - What is this place?
    - **Player:** What is this place?
    - **Void Knight:** This is our outpost. From here we send launches out to the nearby islands to beat back the invaders.
    - **SELECT AN OPTION**
      - What invaders?
        - **Player:** What invaders?
        - **Void Knight:** Recently there have been breaches into our realm from somewhere else, and strange creatures have been pouring through. We can't let that happen, and we'd be very grateful if you'd help us.
        - **SELECT AN OPTION**
          - How can I help?
            - (below|how-can-i-help)
          - Sorry, but I can't.
            - **Player:** Sorry, but I can't.
      - How can I help?
        - **Player:** How can I help?
        - **Void Knight:** We send launchers from our outpost to the nearby islands. If you go and wait in the lander there that'd really help.
      - Good luck with that.
        - **Player:** Good luck with that.
  - Can you exchange my Commendations for training?
    - (opens=Commendation Rewards)
  - I'm fine thanks.
    - **Player:** I'm fine, thanks.

### Using a Void knight commendation on Void Knight

- **Player:** I'd like to redeem this commendation.
- **Void Knight:** Certainly.
- You now have a total of [number] Commendations!

### Manor Farm


#### Help


##### Before having completed the request

- **WHAT WOULD YOU LIKE TO DO?**
  - Ask about their request.
    - **Player:** What're you requesting today?
    - **Void Knight:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **Void Knight:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - ((If three animal variants are accepted:))
      - **Void Knight:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
      - (continue)
    - ((If four animal variants are accepted:))
      - **Void Knight:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal]
      - (continue)
    - **Void Knight:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - **Void Knight:** If you complete this, I'll give you : Shifter, Ravager, Tocher or Spinner Charms x 15. I'm sure you'll gain some reputation with the farming guild too!
    - **Void Knight:** You'll have to be quick though!, I'm only here for [number] days, [number] hours and [number] minutes. To be exact.
  - Give them the items & animals for their request
    - ((Without the requested items:))
      - **Void Knight:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **Void Knight:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - ((If three animal variants are accepted:))
        - **Void Knight:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
        - (continue)
      - ((If four animal variants are accepted:))
        - **Void Knight:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal]
        - (continue)
      - **Void Knight:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - ((With the requested items:))
      - (Condition: With multiple applicable animals:)
        - [Menu]: Which animal  would you like to hand in?
          - ((The following option is given for each applicable animal:))
            - [Choice]: [Animal name]
              - (continue)
      - (removes=the requested items) (receives=the reward)
      - For completing this request you've received Brassica primer x 1.
      - ((Repeated in a pop-up:))
        - For completing this request you've received Brassica primer x 1.
        - (continue)
      - You've received : [Reward] x 15<br>And 5,500 farming reputation.

##### After having completed the request

- **Void Knight:** Thank you for your help!
- A new request will be available in [time]{{Sic|..}}

#### Hand in medium request


##### Before having completed the request


##### Without requested items

- **Void Knight:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **Void Knight:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- ((If three animal variants are accepted:))
  - **Void Knight:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
  - (continue)
- ((If four animal variants are accepted:))
  - **Void Knight:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal], or [Animal]
  - (continue)
- **Void Knight:** I'm also looking for some produce, so I'll need : [Produce] x [number]

##### With requested items

- (removes=the requested items) (receives=the reward)
- For completing this request you've received Brassica primer x 1.
- ((Repeated in a pop-up:))
  - For completing this request you've received Brassica primer x 1.
  - (continue)
- You've received : [Reward] x 15<br>And 5,500 farming reputation.

##### After having completed the request

- You've already completed this request, there will be a new tri-daily request in [time]{{Sic|..}}
