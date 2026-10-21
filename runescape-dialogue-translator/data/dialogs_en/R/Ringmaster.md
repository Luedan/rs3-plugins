# Ringmaster

- **Original Wiki Page**: [Transcript:Ringmaster](https://runescape.wiki/w/Transcript%3ARingmaster)
- **Letter**: `R`

---

## Dialogue Transcript

{{incomplete|missing dialogue for Summer Sweepstakes; missing dialogue when completing performances and unlocking outfits}}

### In Balthazar's Big Top Bonanza


#### First-time dialogue

- **Ringmaster:** Ah, a new face. Could you be our new performer?
- [Menu]: Select an Option
  - [Choice]: Yes, I am.
    - **Ringmaster:** WONDERFUL! Wonderful. But you're human? Well, beggars can't be choosers.
    - **Player:** What's wrong with-
    - **Ringmaster:** Now, we have several acts that need a performer. What act would you like to perform in?
    - [Menu]: Choose an option:
      - [Choice]: Agility
        - (below|agility)
      - [Choice]: Magic
        - (below|magic)
      - [Choice]: Ranged
        - (below|ranged)
      - [Choice]: Firemaking {{clarify|Does this only appear if the Firemaking act has been unlocked?}}
        - (below|firemaking)
      - [Choice]: Thieving {{clarify|Does this only appear if the Thieving act has been unlocked?}}
        - (below|thieving)
  - [Choice]: Err, no. I was just having a look around.
    - **Ringmaster:** Ah, very well. I suppose not all are meant for the spotlight.

#### Subsequent dialogue

- **Ringmaster:** Ah, my little performer. What can I do for you?
- [Menu]: Could you tell me about...
  - [Choice]: The performances
    - {{anchor|performances-opts}}[Menu]: Choose an option:
      - [Choice]: What performances have I done?
        - (Condition: If the player has only done the one performance:)
          - **Ringmaster:** You have done your _____ performance.
          - (continue|tell-me-about)
        - (Condition: If the player has done all the performances:)
          - **Ringmaster:** You have done all your performances for this week. What dedication you have.
          - (continue|tell-me-about)
      - [Choice]: Agility.{{anchor|agility}}
        - **Ringmaster:** Ah, this is a truly fearsome act! You must walk the tightrope and perform daring feats of agility. Flips, twirls, juggling chinchompas; it is truly only for the brave.
        - **Player:** Chinchompas? Juggling?
        - **Ringmaster:** We shall provide you with a costume; simply go to the changing tent by the ladder. You will change there and be taken to the platform. You can either get started straight away, or speak to the assistant on the platform at the top of the ladder who will explain the details to you.
        - {{anchor|whats-in-it}}[Menu]: Select an Option
          - [Choice]: What's in it for me?
            - (below|rewards)
          - [Choice]: How do I leave the circus?
            - (below|leave)
      - [Choice]: Magic.{{anchor|magic}}
        - **Ringmaster:** Ah, an ancient practice, ideal for the spotlight. Dazzle the audience with your displays of impossible feats. You won't need any runes. Speak to the fairy in the wizard's outfit and she'll explain the details to you, or if you feel you're already ready you can just get stuck in!
        - (continuea|whats-in-it)
      - [Choice]: Ranged.{{anchor|ranged}}
        - **Ringmaster:** A perfect place to put your shooting ability to the test. You must successfully hit 10 targets from a distance of your choice. Don't kill your assistant, though, as fairies are expensive to import. We shall provide you with equipment, so there is no cost to you. Either speak to the fairy in the green outfit near the bullseye to get more information, or get started straight away.
        - (continuea|whats-in-it)
      - [Choice]: More. {{clarify|Does this only appear if either the Firemaking/Thieving acts have been unlocked?}}
        - [Menu]: Choose an option:
          - [Choice]: Firemaking.{{anchor|firemaking}}{{clarify|Does this only appear if the Firemaking act has been unlocked?}}
            - **Ringmaster:** Certainly! Which would you like to know about?
            - [Menu]: Select an Option
              - [Choice]: Fire poi
                - **Ringmaster:** Ah, be careful with that one! You must successfully perform 6 flaming poi tricks! Be careful not to ignite anything... we don't want that happening again.
                - **Player:** Again?
                - **Ringmaster:** Never mind that, my little performer! Speak to Emmett over in the firemakers' area and he will explain the details to you, or you can start straight away by taking your place on the star near him.
                - (continuea|whats-in-it)
              - [Choice]: Fire-breathing
                - **Ringmaster:** A daring, colourful event indeed! You must successfully breath fires 6 times, in a multitude of colours!
                - **Ringmaster:** Speak to Sera over in the firemakers' area and she will explain the details to you, or you can start straight away by taking your place on the star near her.
                - (continuea|whats-in-it)
          - [Choice]: Thieving.{{anchor|thieving}}{{clarify|Does this only appear if the Thieving act has been unlocked?}}
            - **Ringmaster:** Want to put your skills at sleight of hand to the test, eh? In a world filled with impossible feats, often the most simple are the most amazing.
            - **Ringmaster:** You can speak to Teddy, the polar bear, to get more details, or you can start straight away by taking your position on the star near him.
            - (continuea|whats-in-it)
          - [Choice]: Back
            - (previous)
  - [Choice]: Improving my performance{{anchor|improve-performance}}
    - **Ringmaster:** Ah, there is so much that goes into being a true virtuoso! The audience is key to any great performance. You must listen to what they want and appease them. They love seeing their requests performed. They also hate repetition, so don't keep doing the same safe move. Be dangerous! Try more difficult moves and who knows, you might succeed. Everything you can do here is rated by difficulty in relation to your skill levels, but they're only recommended levels. You're welcome to attempt anything you like, you're just more likely to succeed if you have the relevant skill level.
    - **Player:** What if I can't do more difficult moves? I can't help repeating!
    - **Ringmaster:** Then perform an emote in between moves! That will make the audience happy; however, don't repeat them. Our audiences are very fickle and HATE repetition. Also, we only give you a point bonus for the first 10 that you perform.
    - **Player:** Isn't there an easier way to improve my performance? The audience can be so demanding.
    - **Ringmaster:** Certainly. Wear crazy costumes - the crazier the better! I will not tell you which clothes to wear, as it is to the taste of the performer, but do experiment. See what works best for you. For safety reasons, you can only wear the costume we provide for the Agility performance. Also, keep an eye on where the ticket vendor moves to, and who populates our audience. Different locations have different preferences, and that will give you a bonus.
    - **Player:** Thanks for the advice!
    - **{{anchor|tell-me-about}}Ringmaster:** Would you like to know about anything else?
    - {{anchor|tell-me-about2}}[Menu]: Tell me about...
      - [Choice]: The performances
        - (above|performances-opts)
      - [Choice]: Improving my performance
        - (above|improve-performance)
      - [Choice]: The rewards
        - (below|rewards)
      - [Choice]: The circus
        - (below|circus)
      - [Choice]: Never mind
        - **Player:** Never mind.
  - [Choice]: The rewards{{anchor|rewards}}
    - [Menu]: Select an Option
      - [Choice]: I want to retrieve a costume.
        - (opens=Circus Rewards)
      - [Choice]: I want to know more about the rewards.
        - **Player:** Not that performing isn't great in itself, but what do I get for doing it? You can't expect me to work for free.
        - **Ringmaster:** What happened to the days when the thrill of performing was enough? Of course I reward my performers, but I work on a performance-related pay method. The better you do, the better I reward you. Your performance itself is a reward, because you gain more experience than you normally would in the skill you perform in. At the end of your performance, I review how well you did and I will reward you with extra experience and a part of a costume.
        - **Player:** What costume?
        - **Ringmaster:** Not just one, but several! For those that simply...put in the minimum effort, I reward them with peasant costume pieces and the occasional giant hand. For those that increasingly put in effort, they get performance costumes. I give out pieces for an acrobat costume, a clown costume and, for those that are truly amazing (like myself), I give out a ringmaster costume!
        - **Player:** That's not too bad, I suppose. I hope mine fits better than yours does.
        - **Ringmaster:** I'd like to see you find a tailor who can make size 115 trousers!
        - (continuea|tell-me-about)
      - [Choice]: Never mind.
        - **Player:** Never mind.
  - [Choice]: The circus{{anchor|circus}}
    - **Player:** Tell me about the circus. It's a little odd.
    - **Ringmaster:** It's a circus. It's *supposed* to be odd. What would you like to know?
    - [Menu]: Select an Option
      - [Choice]: Why are there so few people here?
        - **Player:** Why is there hardly any one here? And why am I your only performer?
        - **Ringmaster:** We are but a new business, and haven't attracted many customers yet. That is why there are so few people in the stands. But with a performer as good as you, we hope to attract more customers and more performers.
        - (continuea|tell-me-about2)
      - [Choice]: Where are we?
        - **Ringmaster:** Ah, we exist within the ticket vendor. We fold space in on itself to fit in something smaller than the space we take up. It's all very complex, but the fairies tell me it's quite easy.
        - **Player:** So, I'm currently folded in space? Is it going to hurt to unfold?
        - **Ringmaster:** No, of course not. It's no different to teleporting normally.
        - (continuea|tell-me-about)
      - [Choice]: How do I leave the circus?{{anchor|leave}}
        - **Player:** How do I leave the circus? All of the exits are roped off.
        - **Ringmaster:** Silly little performer, you were given a golden ticket when you entered Balthazar Beauregard's Big Top Bonanza, yes?
        - **Player:** Yes, I did.
        - **Ringmaster:** Well, read it! It says you just need to tear it to leave the circus. Tear the ticket and 'POOF', you are gone. Simple as that.
        - **Player:** Thanks.
  - [Choice]: Never mind
    - **Player:** Never mind.

#### Rewards option

- **Ringmaster:** Ah, little performer. Have you lost one of your rewards?
- [Menu]: Select an Option
  - [Choice]: Yes
    - **Ringmaster:** Very well, let's get you some replacements.
    - (opens=Circus Rewards)
  - [Choice]: No
    - **Player:** No.

### Balthazar's Big Raffle


#### During the raffle


##### Overhead lines

- {{Trandom}}
  - **Balthazar:** {{RSChat|Come get your RuneScape raffle tickets while they're hot!}}
  - **Balthazar:** {{RSChat|Roll up! Roll up! This month only the RuneScape Raffle!}}
  - **Balthazar:** {{RSChat|Win prizes in the RuneScape Raffle today!}}
  - **Balthazar:** {{RSChat|You've got to be in it to win it!}}

##### When talked to

- (Condition: If the daily ticket hasn't been claimed:)
  - **Balthazar:** Ahh, you haven't had a ticket. Roll up! Roll up! Get your ticket while it's hot!
    - (Condition: If the player has space in their backpack:))
      - You receive a free ticket for the raffle.
      - (Continues below)
    - (Continues below)
- [Menu]: Select an Option
  - [Choice]: What's all this about a raffle?
    - **Player:** What's all this about a raffle?
    - **Balthazar:** Roll up! Roll up! Enter my raffle! Win prizes!
    - **Balthazar:** Speak to me daily and I'll give you one ticket. You can get another one from Gilly Willikers the clown once a day or from doing a daily challenge.
    - **Balthazar:** If you've missed a ticket or two, you can use a bond to gain the ability to claim any that you've missed! And any that you might miss in the future!
    - **Balthazar:** Enter your tickets straight away or save them up - there will be one raffle draw daily!
    - [Menu]: Select an Option
      - [Choice]: Where is Gilly Willikers now?
        - *(Continues with the hint.)*
      - [Choice]: Thanks!
        - (initial)
  - [Choice]: I'd like to enter today's raffle.
    - **Player:** I'd like to enter today's raffle.
    - (opens RS Raffle interface)
  - [Choice]: What are the rewards for the raffle?
    - **Player:** What are the rewards for the raffle?
    - **Balthazar:** The prizes for the raffle change each day. If you're interested in something specific then you'll want to come back and enter on that day.
    - **Balthazar:** Make sure you roll up each day so I can give you your ticket!
    - (initial)
  - [Choice]: How many tickets have been entered in today's raffle so far?
    - (Condition: If the player hasn't entered today's raffle:)
      - **Balthazar:** A total of [number] tickets have been entered today with [number] total prizes available. You haven't entered today's draw. Would you like to?
      - [Menu]: Select an Option
        - [Choice]: I'd like to enter the raffle.
          - (opens RS Raffle interface)
        - [Choice]: No thanks.
          - (initial)
    - (Condition: If the player has entered today's raffle:)
      - **Balthazar:** You have entered [number] [ticket/tickets] in today's raffle and there have been a total of [number] tickets entered today with [number] total prizes available.
      - (initial)
  - [Choice]: Goodbye
    - **Player:** Goodbye.
    - **Balthazar:** Come back soon!

##### Attempting to use raffle tickets from previous years before 2019

- **Balthazar:** What's that there? They look like fakes! Give me those!
- **Balthazar:** {{RSChat|Don't trust Player! They tried to scam me with their dodgy tickets!}}

##### Getting hint

- **Player:** Where is Gilly Willikers at the moment?
  - (Condition: If Gilly is in Al Kharid:)
    - **Balhazar:** It seems he was last seen in Al Kharid.
    - **Player:** Thanks!
  - (Condition: If Gilly is in Draynor Village:)
    - **Balhazar:** I believe he's currently visiting Draynor.
    - **Player:** Thanks!
  - (Condition: If Gilly is in Edgeville:)
    - **Balhazar:** He is up in Edgeville apparently.
    - **Player:** Thanks!
  - (Condition: If Gilly is in Falador:)
    - **Balhazar:** Hmm, he was seen wandering around Falador's front gate recently.
    - **Player:** Thanks!
  - (Condition: If Gilly is in Lumbridge:)
    - **Balhazar:** He was exploring Lumbridge castle not long ago.
    - **Player:** Thanks!
  - (Condition: If Gilly is in Taverley:)
    - **Balhazar:** He was spotted around Taverley not long ago.
    - **Player:** Thanks!
  - (Condition: If Gilly is in Varrock:)
    - **Balhazar:** I'm hearing reports that he is in Varrock.
    - **Player:** Thanks!

#### After the raffle


##### When talked to

- [Menu]: Select an Option
  - [Choice]: What's all this about a raffle?
    - **Player:** What's all this about a raffle?
    - **Balthazar:** I'm sorry the RuneScape raffle has ended.
    - **Balthazar:** I'm just here to hand out the last few prizes.
    - **Player:** Do you have a prize for me?
      - (Condition: If there are unclaimed prizes:)
        - (opens the RS Raffle interface)
      - (Condition: If there are no unclaimed prizes:)
        - **Balthazar:** No, nothing for you. Move along.
  - [Choice]: What are the rewards for the raffle?
    - **Player:** What are the rewards for the raffle?
    - **Balthazar:** The prizes for the raffle change each day. If you're interested in something specific then you'll want to come back and enter on that day.
    - **Balthazar:** Unfortunately, the raffle has since been and gone. Try your luck next time.
    - (initial)

##### When opening the raffle

- The raffle has now ended.

##### When getting hint

- **Balthazar:** The main part of the raffle is not running at the moment, so Gilly is no longer handing out tickets.

### During Summer Sweepstake

- {{Transcript missing}}
