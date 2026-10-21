# TzHaar-Mej-Jal

- **Original Wiki Page**: [Transcript:TzHaar-Mej-Jal](https://runescape.wiki/w/Transcript%3ATzHaar-Mej-Jal)
- **Letter**: `T`

---

## Dialogue Transcript


### TzHaar City

- **Tzhaar-Mej-Jal:** You want help, [Title]-[Caste]-Player?
  - [Choice]: cond=With fire cape in backpack:|I'd like to sell my fire cape back to you.
    - **Tzhaar-Mej-Jal:** I give you 8,000 TokKul for fire cape.<br>But do you really want to sell cape? You must defeat TzTok-Jad again to get another one.
    - [Menu]: CHOOSE AN OPTION:
      - [Choice]: Yes, I understand I can't buy it back again.
        - (Condition: With only one fire cape in backpack:)
          - (removes=fire cape) (receives=8,000 TokKul)
          - **Player:** Thank you very much.
          - (previous2)
        - (Condition: With more than one fire cape in backpack:)
          - **Tzhaar-Mej-Jal:** How many do you want to sell?
          - {{Tinput|How many will you sell? You have [number] in your inventory.}}
          - (Condition: After entering 0:)
            - **Tzhaar-Mej-Jal:** Perhaps you changed your mind?
          - (Condition: After entering a positive number:)
            - (removes=specified number of fire capes) (receives=8,000 TokKul for each fire cape removed)
            - **Player:** Thank you very much.
            - (previous2)
      - [Choice]: You're still using TokKul?
        - **Tzhaar-Mej-Jal:** TzHaar do not need currency. Each TzHaar work hard, and does their duty according to their caste. TzHaar ensure they have food and shelter, and all needs are met.
        - **Tzhaar-Mej-Jal:** JalYt come to TzHaar City, with heads full of gold and wealth and greed. Gold no use to TzHaar. Soft and easily broken, like JalYt.
        - **Tzhaar-Mej-Jal:** JalYt need rare token to trade. TokKul is memories of dead TzHaar. Trapped. Precious.
        - **Tzhaar-Mej-Jal:** TokKul is only rare token TzHaar have. Until TzHaar find new token, or JalYt have less greed, must trade in TokKul.
        - (previous)
      - [Choice]: Actually, I think I'll keep my cape.
        - (previous2)
  - What is this place?
    - **Tzhaar-Mej-Jal:** This is the Fight Cave. TzHaar-Xil made it for practice, but many JalYt come here to fight, too. Just enter the cave and make sure you're prepared.
      - Are there any rules?
        - **Tzhaar-Mej-Jal:** Rules? Survival is the only rule in there.
          - Do I win anything?
            - **Tzhaar-Mej-Jal:** You ask a lot of questions. Might give you TokKul if you last long enough.
        - *(If the player has completed Brink of Extinction quest:)*
          - **Player:** You're still handing out TokKul as a reward? TzHaar-Mej-Jeh said it was going to be melted down in the sacred lava, to release your dead from their torment.
          - **TzHaar-Mej-Jal:** TzHaar do not need currency. Each TzHaar work hard, and does their duty according to their caste. TzHaar ensure they have food and shelter, and all needs are met. JalYt come to TzHaar City, with heads full of gold and wealth and greed. Gold no use to TzHaar. Soft and easily broken, like JalYt. JalYt need rare token to trade. TokKul is memories of dead TzHaar. Trapped. Precious. TokKul is only rare token TzHaar have. Until TzHaar find new token, or JalYt have less greed, must trade in TokKul.
        - *(Otherwise:)*
          - **Player:** ...
          - **TzHaar-Mej-Jal:** Before you ask, TokKul is like your coins.
          - **TzHaar-Mej-Jal:** Gold is like you JalYt: soft. We use hard obsidian, forged in fire like TzHaar!
          - Sounds good.
            - *(returns to previous options)*
      - Thanks.
        - *(dialogue terminates)*
  - What did you call me?
    - **TzHaar-Mej-Jal:** Are you not [Title]-[Caste]?
    - Select an Option
      - Why do you call me '[Title]-[Caste]'?
        - *(If the player is of the Ket caste:)*
          - **TzHaar-Mej-Jal:** That what you are...you tough and strong, no?
        - *(If the player is of the Xil caste:)*
          - **TzHaar-Mej-Jal:** That what you are...you agile and quick, no?
        - *(If the player is of the Mej caste:)*
          - **TzHaar-Mej-Jal:** That what you are...you user of mystic powers, no?
        - *(If the player is of the Hur caste:)*
          - **TzHaar-Mej-Jal:** That what you are...you skilled at making things, no?
        - *(If the player has completed The Brink of Extintion:)*
          - **TzHaar-Mej-Jal:** And you are JalYt no longer. You are TzHaar now.
        - **Player:** Well, yes, I suppose I am...
        - **TzHaar-Mej-Jal:** Then you [Title]-[Caste]!
        - Select an Option
          - What are you then?
            - *(If the player has not completed The Elder Kiln:)*
              - **TzHaar-Mej-Jal:** Foolish JalYt. I am TzHaar-Mej, one of the mystics of this city.
              - **TzHaar-Mej-Jal:** There are also the mighty TzHaar-Ket who guard us, the swift TzHaar-Xil who hunt our food, and the skilled TzHaar-Hur who craft our homes and tools.
            - *(Otherwise:)*
              - **TzHaar-Mej-Jal:** I am TzHaar-Mej, one of the mystics for the city. The TzHaar-Mej guide the TzHaar when change is necessary, and tend to TzHaar eggs to ensure they are hot and healthy. TzHaar-Mej are keeps of knowledge and magic.
              - **TzHaar-Mej-Jal:** There are also the mighty TzHaar-Ket who guard us, the swift TzHaar-Xil who hunt our food, and the skilled TzHaar-Hur who craft our homes and tools.
          - Thanks for explaining it.
            - (end)
      - *(If the player has not completed The Brink of Extinction:)*
        - I guess so...
          - **TzHaar-Mej-Jal:** Well, then. There is no problem.
        - No, I'm not!
          - **TzHaar-Mej-Jal:** Whatever you say, JalYt!
      - *(Otherwise:)*
        - Yes, I certainly am.
          - **TzHaar-Mej-Jal:** Then it is an honour to speak with you, TzHaar-[Caste]-Player. You great and powerful TzHaar, and defender of our city.
        - You must have me confused with another TzHaar.
          - **TzHaar-Mej-Jal:** I heard you are modest, TzHaar-[Caste]-Player. No need. Revel in our praise. You deserve all honour.
  - No, I'm fine. Thanks.
    - *(dialogue terminates)*

### Fight Cave

*If the player attempts to enter the Fight Cave with a familiar or pet following them:*
- **Tzhaar-Mej-Jal:** No Kimit-Zil in the cave! This is a fight for YOU, not your friends!
*Start of wave 1:*
- **Tzhaar-Mej-Jal:** You're on your own now, JalYt. Prepare to fight for your life!
*Start of wave 63:*
- **Tzhaar-Mej-Jal:** Look out, here comes TzTok-Jad!
*After defeating TzTok-Jad:*
- **Tzhaar-Mej-Jal:** You even defeated TzTok-Jad, I am most impressed! Please accept this gift as a reward.
*After dying in the Fight Cave:*
- **Tzhaar-Mej-Jal:** Well done in the cave, here take Tokkul as reward.
*After exiting or dying in the Fight Cave without earning TokKul:*
- **Tzhaar-Mej-Jal:** Well I suppose you tried... better luck next time.

### Manor Farm


#### Help


##### Before completing the request

- **WHAT WOULD YOU LIKE TO DO?**
  - Ask about their request.
    - **Player:** What're you requesting today?
    - **TzHaar-Mej-Jal:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **TzHaar-Mej-Jal:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - **TzHaar-Mej-Jal:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
    - **TzHaar-Mej-Jal:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - **TzHaar-Mej-Jal:** If you complete this, I'll give you : Obsidian charm x 15. I'm sure you'll gain some reputation with the farming guild too!
    - **TzHaar-Mej-Jal:** You'll have to be quick though!, I'm only here for [time]. To be exact.
  - Give them the items & animals for their request
    - ((Without the requested items:))
      - **TzHaar-Mej-Jal:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **TzHaar-Mej-Jal:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - **TzHaar-Mej-Jal:** I'm also looking for a new animal, I'm currently after one of the following :  [Animal], or [Animal], or [Animal]
      - **TzHaar-Mej-Jal:** I'm also looking for some produce, so I'll need : [Produce] x [number]
    - ((With the requested items:))
      - ((With multiple requested animals:))
        - **WHICH ANIMAL WOULD YOU LIKE TO HAND IN?**
          - ((Option repeated for each applicable animal:))
            - [Name]
              - (continue)
      - (removes=the requested items) (receives=the reward)
      - For completing this request you've received Brassica primer x 1.
      - ((Repeated in a pop-up:))
        - For completing this request you've received Brassica primer x 1.
        - (continue)
      - You've received : Obsidian charm x 15<br>And 5,500 farming reputation.

##### After completing the request

- **TzHaar-Mej-Jal:** Thank you for your help!
- A new request will be available in [time].

#### Hand in medium request


##### Before completing the request


##### Without requested items

- **TzHaar-Mej-Jal:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **TzHaar-Mej-Jal:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- **TzHaar-Mej-Jal:** I'm also looking for a new animal, I'm currently after one of the following : [Animal], or [Animal], or [Animal]
- **TzHaar-Mej-Jal:** I'm also looking for some produce, so I'll need : [Produce] x [number]

##### With requested items

- (removes=the requested items) (receives=the reward)
- For completing this request you've received Brassica primer x 1.
- ((Repeated in a pop-up:))
  - For completing this request you've received Brassica primer x 1.
  - (continue)
- You've received : Obsidian charm x 15<br>And 5,500 farming reputation.

##### After completing the request

- You've already completed this request, there will be a new tri-daily request in [time]..
