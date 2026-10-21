# My Arm

- **Original Wiki Page**: [Transcript:My Arm](https://runescape.wiki/w/Transcript%3AMy%20Arm)
- **Letter**: `M`

---

## Dialogue Transcript


### At Troll Stronghold after My Arm's Big Adventure

- **My Arm:** What can My Arm do for you today, Player?
- [Menu]: Select an Option
  - [Choice]: cond=If the player has lost their farming manual|Can I get another copy of that farming book, please?
    - **Player:** Can I get another copy of that farming book, please?
    - **My Arm:** Here, have dis one.
    - (receives=Farming manual)
    - **Player:** Thanks.
  - [Choice]: How's your farming coming along?
    - **Player:** How's your farming coming along?
    - **My Arm:** My Arm is getting good at dis. I growin' plenty of goutweed for Burntmeat, an' he very happy.
    - **Player:** Good, good.
    - **My Arm:** Anyfing else?
    - **Player:** Nothing, thanks.
    - **My Arm:** Dat okay, Player. Come back anytime you like.
  - [Choice]: cond=After The Mighty Fall|I want to talk to you about the Kyzaj.
    - **My Arm:** Haw haw! Was great! Never seen anyfing like dat! Hope dey put on anuvva one soon.
    - [Menu]: Select an Option
      - [Choice]: cond=If Zanik was killed|What do you think about Zanik?
        - **My Arm:** Shame you had ta kill 'er but I guess Zarador made a convincin' argument.
        - **My Arm:** I just 'ope I nevva get chucked in a pit wiv you!
      - [Choice]: What do you think about Graardor?
        - **My Arm:** I never 'eard of 'im before this tournament. He's a pretty good fighter.
        - **My Arm:** Nuffin' on you of course!
      - [Choice]: cond=If Zanik was spared|You didn't go with Zanik?
        - **My Arm:** Naw. It sounds like pretty good adventure but I couldn't just leave. Dese herbs might die if I done that.
      - [Choice]: Goodbye.
        - (end)
  - [Choice]: Nothing, thanks.
    - **Player:** Nothing, thanks.
    - **My Arm:** Dat okay, Player. Come back anytime you like.

### In the Barendir Tunnels after King of the Dwarves

- [Menu]: Select an Option
  - [Choice]: What are you doing here?
    - **Player:** What are you doing here?
    - **My Arm:** Pretty Flower think someone try to poison him, so he make me grow new food ingredients for him.
  - [Choice]: How's your Farming coming along?
    - **Player:** How's your Farming coming along?
    - **My Arm:** My Arm getting good at dis. I growin' plenty of goutweed for Burntmeat, an' he very happy.
  - [Choice]: I need another pretty flower.
    - **Player:** I need another pretty flower.
    - (receives=Pretty flower)
    - [My Arm gives you another pretty flower.]
    - **My Arm:** My Arm hope you enjoy!
  - [Choice]: Bye.
    - **Player:** Bye.

### Manor Farm


#### Help


##### Before completing the request

- [Menu]: What would you like to do?
  - [Choice]: Ask about their request.
    - **Player:** What're you requesting today?
    - **My Arm:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **My Arm:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - **My Arm:** I'm also looking for a new animal, I'm currently after A [animal]
    - **My Arm:** If you complete this, I'll give you : Farming reputation boon (medium) x 1. I'm sure you'll gain some reputation with the farming guild too!
    - **My Arm:** You'll have to be quick though!, I'm only here for [number] hours and [number] minutes. To be exact.
  - [Choice]: Give them the items & animals for their request
    - ((Without the requested items:))
      - **My Arm:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **My Arm:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - **My Arm:** I'm also looking for a new animal, I'm currently after A [animal]
    - ((With the requested items:))
      - (removes=the requested items) (receives=Farming reputation boon (medium) and possibly a Brassica primer)
      - ((If a Brassica primer was rewarded:))
        - For completing this request you've received Brassica primer x 1.
        - ((Repeated in a pop-up:))
          - For completing this request you've received Brassica primer x 1.
          - (continue)
      - [You've received : Farming reputation boon (medium) x 1 <br>And 2,750 farming reputation.]

##### After completing the request

- **My Arm:** Thank you for your help!
- A new request will be available in [time]..

#### Hand in easy request


##### Before completing the request


##### Without requested items

- **My Arm:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **My Arm:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- **My Arm:** I'm also looking for a new animal, I'm currently after A [animal]

##### With requested items

- (removes=the requested items) (receives=Farming reputation boon (medium) and possibly a Brassica primer)
- ((If a Brassica primer was rewarded:))
  - For completing this request you've received Brassica primer x 1.
  - ((Repeated in a pop-up:))
    - For completing this request you've received Brassica primer x 1.
    - (continue)
- [You've received : Farming reputation boon (medium) x 1 <br>And 2,750 farming reputation.]

##### After completing the request

- You've already completed this request, there will be a new daily request in [time]..
