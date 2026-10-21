# Blaze Sharpeye

- **Original Wiki Page**: [Transcript:Blaze Sharpeye](https://runescape.wiki/w/Transcript%3ABlaze%20Sharpeye)
- **Letter**: `B`

---

## Dialogue Transcript


### Talk-to


#### Before All Fired Up

- **Player:** Hi there! Would you mind my asking what exactly it is you're doing... and what's that big contraption over there?
- **Blaze Sharpeye:** Oh I'm afraid it's top secret, really hush-hush important stuff. I can't tell you what it's all about, but if I could...
- **Blaze Sharpeye:** I'd tell you all about this amazing new network of beacons we're creating to guard against the mounting threats in Morytania and the Wilderness. Oops, did I say that out loud?
- **Player:** Yes. Yes, you did.
- (Condition: If the player has 43 Firemaking:)
  - **Blaze Sharpeye:** You know, you look lik you're pretty skilled with the old tinderbox yourself. Tell me, do you have a burning desire to set things alight?
  - **Player:** Uh...maybe?
  - **Blaze Sharpeye:** Well then, 'maybe' you're the [man/woman] for us!
  - **Player:** Um, okay...
  - **Blaze Sharpeye:** If you're ever looking for a job, why don't you have a chat with King Roald in Varrock. Tell 'im I sent you, and he might just sort you out with something.
  - **Player:** Thanks for that; I'll keep it in mind.
- (Condition: If the player is below 43 Firemaking:)
  - **Blaze Sharpeye:** Well, pretend you heard nothing, eh? As a favour to your old friend Blaze. Meanwhile, if you meet anyone with a particular knack for Firemaking, would you send 'em my way? I could use a hand, hehe.
  - [Menu]: Select an Option
    - [Choice]: Could I help?
      - **Blaze Sharpeye:** Not until you have a bit more of the pyromanical look in your eye. Go rub some sticks together and get a bit more practice. If you still want to help after that, talk to King Roald.
      - You need a Firemaking level of at least 43 to start All Fired Up.
    - [Choice]: Okay, sure.
      - **Player:** Okay, sure.

#### After All Fired Up


##### First time dialogue

- **Blaze Sharpeye:** Hello, Player! Back for more, are you?
- **Player:** Well, King Roald did say that you could use some help giving the entire beacon network some serious testing.
- **Blaze Sharpeye:** Could we ever! There are fourteen beacons in all, spanning the south and west borders of the Wilderness. What we really need is for someone to try to keep alight as many beacons as possible, all at the same time.
- **Blaze Sharpeye:** I should warn you: it's not as easy as it sounds - some beacons are harder to light than other and there may be burning issues you have to resolve before you can access each beacon.
- **Blaze Sharpeye:** The more testing we do, however, the more prepared we'll be in case of adversity.
- **Blaze Sharpeye:** If you're interested in helping, I suggest you plan a route and then give it a trial run or two, just to make sure that you can get where you need to go and you have everything you need.
- **Blaze Sharpeye:** It requires some specialist skills, but you'll be well rewarded. Not to mention the job satisfaction. You are not only doing a great service for the southern kingdoms, but...
- **Player:** But?
- **Blaze Sharpeye:** But what could be better than spending every moment of one's life starting BIG, LONG LINES OF FIRE!
- **Player:** Uh, Blaze?
- **Blaze Sharpeye:** Ahem. Sorry. So, yes. Do you have any burning questions for me?
- (continue|standard)

##### Subsequent dialogue

- **Blaze Sharpeye:** Hello, Player! Do you have any burning questions for me today?
- [Menu]: Select an Option
  - [Choice]: Could you look after this beacon for me?
    - **Player:** Could you look after this beacon for me?
    - (Condition: If the beacon is unlit:)
      - **Blaze Sharpeye:** Of course. Once the beacon is lit, just leave 5 logs with me and I'll take care of the fire for as long as I can.
    - (Condition: If the beacon is dying:)
      - **Blaze Sharpeye:** Well, I could, but since you're here, you might as well do it yourself.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Blaze Sharpeye does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - You must give the fire tender five of the same type of log for the beacon.
          - **Blaze Sharpeye:** I'm afraid you don't have enough of the right type of log for me to use.
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Blaze Sharpeye:** I'll need five logs to be able to tend the fire. Is that okay?
            - [Menu]: Do you want to give five logs to the fire tender?
              - [Choice]: Yes.
                - (removes=five logs)
                - **Player:** Here are five logs for you.
                - **Blaze Sharpeye:** Thank you! I'll use these five logs to keep the beacon burning while you're away.
              - [Choice]: No.
                - **Player:** I think I'll keep hold of my logs for now.
                - **Blaze Sharpeye:** Well, you know where I am if you change your mind.
              - [Choice]: Yes. Please don't ask me for confirmation in future.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Blaze Sharpeye has five logs:)
        - **Blaze Sharpeye:** Of course I will, don't worry. I'll use the logs you've already left with me.
  - [Choice]: Can you tell me about other beacons?
    - **Player:** Can you tell me about other beacons?
    - **Blaze Sharpeye:** But of course! Just have a look at my map.
    - (All Fired Up (minigame) beacon status map interface opens)
  - [Choice]: cond=If the player has not given a macaw pouch:|Is it possible to get information about beacons that are further away?
    - **Player:** Is it possible to get information about beacons that are further away?
    - **Blaze Sharpeye:** I can tell you about the state of the beacons in either direction, up to the last fires that are lit.
    - **Blaze Sharpeye:** I could probably tell you about the other beacons as well, but I'd need the help of a macaw.
    - **Player:** A macaw?
    - **Blaze Sharpeye:** Yes. Macaws have the ability to fly high into the air and see things that are much further away.
    - **Blaze Sharpeye:** They are also highly intelligent and can be trained to provide the exact information I'd need for a complete overview of the beacon network.
    - ((If the player has a macaw pouch in their backpack:))
      - **Blaze Sharpeye:** Come to think of it, the macaw you've got there in your pack would be perfect.
      - (continue|macaw)
  - [Choice]: I have some other questions for you.
    - **Player:** I have some other questions for you.
    - **Blaze Sharpeye:** Fire at will!
    - [Menu]: Select an Option
      - [Choice]: Can you explain what I'm meant to be doing again?
        - **Player:** Can you explain what I'm meant to be doing again?
        - **Blaze Sharpeye:** But of course! Essentially, King Roald would really like to give the entire beacon network some serious testing.
        - **Blaze Sharpeye:** There are fourteen beacons in all, spanning the south and west borders of the Wilderness. What we really need is for someone to try to keep alight as many beacons as possible, all at the same time.
        - **Blaze Sharpeye:** I should warn you: it's not as easy as it sounds - some beacons are harder to light than others and there may be burning issues you have to resolve before you can access each beacon.
        - **Blaze Sharpeye:** The more testing we do, however, the more prepared we'll be in case of adversity.
        - **Blaze Sharpeye:** If you're interested in helping, I suggest you plan a route and then give it a trial run or two, just to make sure you can get where you need to go and you have everything you need.
        - **Blaze Sharpeye:** It requires some specialist skills, but you'll be well rewarded. Not to mention the job satisfaction. You are not only doing a great service for the southern kingdoms, but...
        - **Player:** But?
        - **Blaze Sharpeye:** But what could be better than spending every moment of one's life starting BIG, LONG LINES OF FIRE!
        - **Player:** Uh, Blaze?
        - **Blaze Sharpeye:** Ahem. Sorry.
      - [Choice]: Does it make a difference what type of logs I use?
        - **Player:** Does it make a difference what type of logs I use?
        - **Blaze Sharpeye:** Of course it does! A beacon's fire will stay lit for a certain amount of time, depending on the type of log you use on it.
        - **Blaze Sharpeye:** In general, the harder a log is to light, the longer it will burn on the beacon.
        - **Player:** How long are we talking about, here?
        - **Blaze Sharpeye:** Well, a beacon loaded with normal logs will burn for roughly ten minutes, but a beacon loaded with magic logs will burn for about twenty minutes.
        - **Blaze Sharpeye:** So, if you want a beacon to burn for a long time, you're better off using logs that are more difficult to light.
        - **Player:** What about when I give logs to a fire tender to burn for me - does the log type matter then?
        - **Blaze Sharpeye:** Yes, to some extent. If you tend the fire yourself, I suspect you'll get a slightly better result, no matter what type of log you use.
        - **Blaze Sharpeye:** If you leave your logs with us, however, we'll do our best for you. All of us are pretty experienced at looking after fires, but there's only so much we can do.
      - [Choice]: Can you tell me about rewards?
        - **Player:** Can you tell me about rewards?
        - **Blaze Sharpeye:** I believe King Roald is offering rewards for keeping six, ten and all fourteen beacons alight simultaneously.
        - **Blaze Sharpeye:** A beacon counts as lit if it's in its blazing state or if it's dying down. If you manage to keep six, ten or fourteen beacons in either of those two states at the same time, talk to King Roald to claim your reward.
        - **Select an Option**
          - [Choice]: What kinds of rewards is he offering?
            - **Player:** What kinds of rewards is he offering? Anything good?
            - **Blaze Sharpeye:** Why, yes, in fact!
            - ((If the player has not already claimed the ring of fire:))
              - [When you keep six beacons alight simultaneously, King Roald will give you a ring that will aid you when Firemaking.]
              - (continue)
            - ((If the player has already claimed the ring of fire:))
              - [You've already claimed the Ring of Fire for keeping six beacons alight simultaneously. This ring can aid you when Firemaking.]
              - (continue)
            - ((If the player has not already claimed the flame gloves:))
              - [When you keep ten beacons alight simultaneously, King Roald will give you a pair of gloves. These are also of assistance when Firemaking and they work nicely in combination with the Ring of Fire.]
              - (continue)
            - ((If the player has already claimed the flame gloves:))
              - [You've already claimed the Flame Gloves for keeping ten beacons alight simultaneously. These are also of assistance when Firemaking and they work well in combination with the Ring of Fire.]
              - (continue)
            - ((If the player has not already claimed the inferno adze:))
              - [When you keep all fourteen beacons alight simultaneously, King Roald will give you the Inferno Adze. This item can be of incredible use when Woodcutting, Firemaking or Mining.]
              - (continue)
            - ((If the player has already claimed the inferno adze:))
              - [You've already managed to keep all fourteen beacons alight simultaneously and have received the Inferno Adze as a result. This item can be of incredible use when Woodcutting, Firemaking or Mining.]
              - (continue)
            - **Player:** Can I claim more than one of each of these items?
            - **Blaze Sharpeye:** Why would you need to? You can't wear, say, two pairs of gloves at the same time.
            - **Blaze Sharpeye:** Any more would just weigh you down when you're trying to...SET THINGS ON FIRE!
            - **Player:** So the answer is 'no', then?
            - **Blaze Sharpeye:** FIRE!
            - **Player:** Right.
            - **Blaze Sharpeye:** Any more questions about rewards?
            - (previous|rewards)
          - [Choice]: How do I claim my reward?
            - **Player:** How do I claim my reward?
            - **Blaze Sharpeye:** Just talk to King Roald in Varrock Palace once you've kept the right number of beacons alight - he'll sort you right out.
            - **Blaze Sharpeye:** Any more questions about rewards?
            - (previous|rewards)
          - [Choice]: What if I were to lose a reward item?
            - **Player:** What if I were to lose a reward item? Would I be able to claim it back?
            - **Blaze Sharpeye:** I suspect you'll have to repeat the trial. King Roald isn't the sort to give away freebies.
            - **Blaze Sharpeye:** Any more questions about rewards?
            - (previous|rewards)
          - [Choice]: That's all I need to know, thanks.
            - **Player:** That's all I need to know, thanks.
            - **Blaze Sharpeye:** Any time!
      - [Choice]: Can we talk about warnings?
        - **Blaze Sharpeye:** We fire tenders like to be useful, but we don't want to bother you with unnecessary chat when you're busy with urgent business.
        - **Blaze Sharpeye:** If you'd like, we can warn you before you use logs on the beacons or give us a stack of logs for beacon tending, or we can just keep quiet.
        - **Blaze Sharpeye:** What do you prefer?
        - [Menu]: Warn me about...
          - [Choice]: Everything!
            - **Player:** Warn me about everything!
            - **Blaze Sharpeye:** Will do! If you change your mind, just let me know.
          - [Choice]: Using logs on beacons, but not about giving logs to fire tenders.
            - **Player:** Warn me about using logs on beacons, but not about giving logs to fire tenders.
            - **Blaze Sharpeye:** Will do! If you change your mind, just let me know.
          - [Choice]: Giving logs to fire tenders, but not about using logs on beacons.
            - **Player:** Warn me about giving logs to fire tenders, but not about using logs on beacons.
            - **Blaze Sharpeye:** Will do! If you change your mind, just let me know.
          - [Choice]: Nothing!
            - **Player:** Warn me about nothing!
            - **Blaze Sharpeye:** Will do! If you change your mind, just let me know.
      - [Choice]: Why does your voice go all gooey when you talk about Squire Fyre?
        - **Player:** Why does your voice go all gooey when you talk about Squire Fyre?
        - **Blaze Sharpeye:** Oh, just the thought of her brilliance and spark lights up my life. She takes her firemaking so seriously - she's a shining example to us all.
        - **Blaze Sharpeye:** You won't say a word to anyone, will you? It's a little...*ember*-rassing.
        - **Player:** That was awful.
        - **Blaze Sharpeye:** I know, I know. I just can't help myself sometimes.
        - **Player:** No, seriously, that was really, really bad.
        - **Blaze Sharpeye:** I'm so sorry.
  - [Choice]: I'm done talking to you, now!
    - **Player:** I'm done talking to you, now!
    - **Blaze Sharpeye:** Off to light some fires, then? Brilliant. You're a [man/woman] after my own heart!

### Using a macaw pouch on Blaze Sharpeye


#### Before giving Blaze Sharpeye a macaw pouch{{Anchor|macaw}}

- [Menu]: Do you want to give the fire tender your macaw?
  - [Choice]: Yes.
    - (removes=a macaw pouch)
    - **Blaze Sharpeye:** Thank you very much. This macaw will help me give you more detailed information about the beacon network.
  - [Choice]: No.
    - **Player:** I think I'll keep my macaw for now.
    - **Blaze Sharpeye:** Suit yourself.

#### After giving Blaze Sharpeye a macaw pouch

- **Player:** I've already given him a macaw; he doesn't need another.

### Using logs on Blaze Sharpeye

- (Condition: If the beacon is unlit:)
  - There's no fire here for the fire tender to tend.
- (Condition: If the beacon is dying:)
  - **Player:** Since I'm here and the beacon's fire is dying down, I might as well tend the fire myself.
- (Condition: If the beacon is not dying:)
  - (Condition: If Blaze Sharpeye does not have five logs:)
    - (Condition: If the confirmation prompt is enabled:)
      - [Menu]: Do you want to give five logs to the fire tender?
        - [Choice]: Yes.
          - (Condition: If the player does not have at least five logs of the same type:)
            - The fire tender needs five of the same type of log to maintain this fire.
          - (Condition: If the player has at least five logs of the same type:)
            - (removes=five logs)
            - You give the fire tender 5 [type] logs.
        - [Choice]: No.
          - **Player:** I think I'll hang on to my logs after all.
        - [Choice]: Yes. Please don't ask me for confirmation again.
          - (above|use-give-logs)
    - (Condition: If the confirmation prompt is disabled:)
      - (above|use-give-logs)
  - (Condition: If Blaze Sharpeye has five logs:)
    - You've already left logs with this fire tender.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Blaze Sharpeye:** Oi! Get away from that! Until you've proven yourself a true ally of Varrock, you can't use that!
- You need to claim the reward for the elite set Tasks in Varrock to use this chest.
