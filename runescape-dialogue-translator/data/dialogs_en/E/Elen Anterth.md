# Elen Anterth

- **Original Wiki Page**: [Transcript:Elen Anterth](https://runescape.wiki/w/Transcript%3AElen%20Anterth)
- **Letter**: `E`

---

## Dialogue Transcript


### First time entering the Max Guild garden

- **Elen:** Hey, welcome to the Max Guild garden!

### Talk to

- **Elen:** Oh, hey there!
- [Menu]: What would you like to say?
  - [Choice]: What's your name?
    - **Elen:** I'm Elen! It's great to meet you! Welcome to the Max Guild!
    - (Condition: If the player is in the Max Guild:)
      - **Elen:** Well done on getting in here - it's well deserved!
      - (continue)
    - **Player:** Elen? Shouldn't you be called Maxine or something?
    - **Elen:** Maxine? What a strange name that would be for an elf! Haha, I like it!
    - **Elen:** But no, it's Elen - Elen Anterth. My family falls under the auspices of Clan Cadarn.
    - **Player:** How are you so skilled if the city's only recently been regrown?
    - **Elen:** Oh, I've been all over! My family travelled east with the Cadarn way back.
    - **Elen:** I was only young, but I saw so much and learned a lot. You'd be surprised what sticks with you.
    - (initial)
  - [Choice]: Nice cape you have there...
    - **Elen:** Thanks! It took me ages to get, but I got there in the end: I'm fully proficient in every skill.
    - (Condition: If the player has not maxed all skills:){{anchor|notmaxed}}
      - To do this you need in the following skill levels:<br>99 [Skill]
      - **Player:** Wow, that's quite impressive.
      - **Elen:** Thanks. I have faith in you, Player. Just take your time and you'll get there too, I know it!
      - **Player:** Yeah, maybe...
      - **Elen:** Just remember: don't rush it. It's the journey, not the destination!
    - (Condition: If the player has maxed all skills:){{anchor|maxed}}
      - **Player:** I've maxed all skills!
      - **Elen:** Really? Good for you! Would you like a cape to show off your achievement? It's 2,871,000 coins - 99,000 for each skill!
      - [Menu]: Pay 2,871,000 for a max cape?
        - [Choice]: I'll take one!
          - **Player:** Sure!
          - ((Without two free spaces in backpack:))
            - You don't have enough inventory space to withdraw that many.
            - **Elen:** Oh, but you'll need room in your inventory for a cape and hood.
          - ((With two free spaces in backpack:))
            - ((Without enough coins:))
              - You can not afford that.
              - ((Repeated in a pop-up:))
                - You can not afford that.
                - (continue)
              - **Elen:** Sorry, hun, but you don't have enough coins on you.
            - ((With enough coins:))
              - (removes=2,871,000 coins) (receives=a max cape and max hood)
              - **Elen:** Thanks. Enjoy!
              - (initial)
        - [Choice]: No, thanks.
          - **Player:** No, thanks.
          - (initial)
  - [Choice]: cond=Historical, only occurs when a skill is recently released|What happened to your Max cape?
    - **Elen:** Oh, I'm training [Recently released skill]! No rush, taking my time. You'll probably beat me to max!
    - ((If you have not gotten [Recently released skill] to 99:))
      - (above|notmaxed)
    - ((If you have gotten [Recently released skill] to 99:))
      - (above|maxed)
  - [Choice]: Do you know someone called Max?
    - **Elen:** You don't mean that bullish human from Varrock, do you?
    - **Player:** Bullish? Well, I guess he is always running from place to place.
    - **Elen:** Urgh, I hate that guy.
    - **Player:** When did you meet him?
    - **Elen:** Since the city was regrown, he shows up here sometimes. Never stops long.
    - **Elen:** Just rushes about the place training, doesn't take the time to just relax and enjoy things.
    - **Player:** That sounds like Max.
    - **Elen:** I tried talking to him the first few times I saw him, but he always just said he was 'doing his dailies' and didn't have time.
    - **Elen:** There's more to our beautiful city than 'dailies'.
    - **Player:** Does he come in here at all?
    - **Elen:** There's no gain for him here, he says. It'd be a waste, he says.
    - **Elen:** You're not welcome here then, I said.
    - (initial)
  - [Choice]: cond=Only in the Max Guild|Can I toggle my Max Guild teleport?
    - **Elen:** Of course! You're currently set to arrive in the [garden/tower]. Do you want to arrive in the [tower/garden] instead?
    - [Menu]: Change Max Guild teleport?
      - [Choice]: Yes.
        - (initial)
      - [Choice]: No.
        - (initial)
  - [Choice]: More...
    - [Menu]: Select an Option
      - [Choice]: About the Task System...
        - ((If the player has completed the elite Tirannwn achievements and the rewards have not been claimed:))
          - **Player:** I've completed all of the Elite tasks in the Tirannwn set.
          - **Elen Anterth:** Well done Player. I have special quiver kept for you.
          - [Elen hands you a quiver, a few lamps and a lot of resources.]
          - **Elen Anterth:** Take this well deserved reward - you have impressed us all. The quiver will allow you to teleport to the resource dungeon, fight dark beasts easier and use our Lords and Ladies' likeness when in the photobooth.
          - **Player:** Thanks! What else does it do?
          - **Elen Anterth:** Because you completed the Elite task set, you will be able to persuade Coeden to give you some logs, use less charges when using Most Wanted cards and your attuned crystal bow and ward.
          - (continue)
        - (Condition: If the player has lost their Tirannwn quiver 4:)
          - **Elen Anterth:** Ah, quiver-bearer! How is it going?
          - **Player:** I lost it.
          - **Elen Anterth:** Oh, no!
          - **Elen Anterth:** Never mind, I have another one. Here...
          - [Elen hands you a quiver.]
          - (continue)
        - [Menu]: Choose an option:
          - [Choice]: Tell me about the Achievement System.
            - **Elen Anterth:** Very well: the Achievement System is a collection of deeds you may wish to complete while adventuring around the world.
            - **Elen Anterth:** You can earn special rewards for completing certain achievements; at the very least, each is worth a cash bounty from Explorer Jack in Lumbridge.
            - **Elen Anterth:** Some also give items that will help complete other achievements, and many count as progress towards the set for the area they're in.
            - [Menu]: Choose an option:
              - [Choice]: Tell me about the set reward for this locality.
                - **Player:** Tell me about the set reward for this area.
                - **Elen Anterth:** For completing the Tirannwn set, you are presented with a quiver.
                - **Elen Anterth:** This quiver will become increasingly useful as you complete greater difficulties of task sets.
                - **Elen Anterth:** When you are presented with your rewards, you will be told of its uses.
                - You may also see what rewards a set item provides by hovering over the Rewards icon for its Exploration Achievement set in the Achievements interface.
                - (previous2)
              - [Choice]: How do I claim these rewards?
                - **Player:** How do I claim the rewards?
                - **Elen Anterth:** You need to complete all of the Tasks in a set of a particular difficulty, then you can claim your reward.
                - **Elen Anterth:** Some of the Tirannwn set's Tasks are simple, some will require skill levels, and others require quests to be started or completed.
                - **Elen Anterth:** To claim your Tirannwn set rewards, speak to the Elven Tracker near the Lodestone, Gwir in Lletya, Elen in the city or myself.
                - (previous2)
              - [Choice]: Sorry, I was just leaving.
                - (end)
          - [Choice]: Could I buy a spare of the reward?
            - [Menu]: Choose an option:
              - [Choice]: Tirannwn quiver 1
              - **Elen Anterth:** Tirannwn quiver 1? Yes, but I'm afraid it would cost you 5,000 coins.
                - [Menu]: Purchase another for 5,000 coins?
                  - [Choice]: Yes
                    - [You're handed another Tirannwn quiver 1.]
                    - (receives=Tirannwn quiver 1) (removes= 5,000 coins)
                  - [Choice]: No
                    - **Player:** No thanks.
              - [Choice]: Tirannwn quiver 2
                - **Elen Anterth:** Tirannwn quiver 2? Yes, but I'm afraid it would cost you 10,000 coins.
                - [Menu]: Purchase another for 10,000 coins?
                  - [Choice]: Yes
                    - [You're handed another Tirannwn quiver 2.]
                    - (receives=Tirannwn quiver 2) (removes= 10,000 coins)
                  - [Choice]: No
                    - **Player:** No thanks.
              - [Choice]: Tirannwn quiver 3
                - **Elen Anterth:** Tirannwn quiver 3? Yes, but I'm afraid it would cost you 25,000 coins.
                - [Menu]: Purchase another for 25,000 coins?
                  - [Choice]: Yes
                    - [You're handed another Tirannwn quiver 3.]
                    - (receives=Tirannwn quiver 3) (removes= 25,000 coins)
                  - [Choice]: No
                    - **Player:** No thanks.
              - [Choice]: Tirannwn quiver 4
                - **Elen Anterth:** Tirannwn quiver 4? Yes, but I'm afraid it would cost you 50,000 coins.
                - [Menu]: Purchase another for 50,000 coins?
                  - [Choice]: Yes
                    - [You're handed another Tirannwn quiver 4.]
                    - (receives=Tirannwn quiver 4) (removes= 50,000 coins)
                  - [Choice]: No
                    - **Player:** No thanks.
          - [Choice]: Sorry, I was just leaving.
            - (end)
      - [Choice]: Bye.
        - **Player:** Bye.

### Trade


#### Outside the Max Guild building

- **Elen:** Sorry, hun, I only sell skill capes in the tower.
- **Elen:** Ooh, but I could tell you who DOES sell skill capes - want me to tell you where all the skill masters are?
- [Menu]: Ask about the skill masters?
  - [Choice]: Yes.
    - **Elen:** I'll break it down for you, or I'll be droning on for ages!
    - [Menu]: Ask about which category of cape?
      - [Choice]: Combat.
        - **Elen:** There's a couple you can get from the Warriors' Guild in Burthorpe - the attack cape from Ajjat, and the strength cape from Yadech Strongarm.
        - **Elen:** The magic cape is sold by the robe store owner in Yanille's Wizards' Guild, and the ranged cape by the armour salesman in the Ranging Guild at Hemenster.
        - **Elen:** If you're after the Defence cape, talk to Harlan at the Lumbridge Combat Academy. For Constitution, talk to Surgeon General Tafani in her house near the north entrance of Al Kharid.
        - **Elen:** For Necromancy's cape, you'll want to search the City of Um for a phantom named the Spirit of Accomplishment.
        - **Elen:** Oh, and they're more like support skills, but the prayer cape can be bought from Brother Jered at Edgeville Monstary, and Pikkupstix in Taverley sells the summoning cape.
        - (continue|hearmore)
      - [Choice]: Gathering.
        - **Elen:** I made a new friend in Orla Fairweather - she sells the cape for divination. It's a skill close to my heart.
        - **Elen:** The master fisher at the Fishing Guild north of Ardougne sells that cape. I don't like fish - yuck!
        - **Elen:** If you're after a mining cape, talk to the dwarf who runs the Mining Guild in Falador.
        - **Elen:** If you want a woodcutting cape, head to the forest north of Falador and find Wilfred!
        - **Elen:** Oh, and if you're a fan of the past you could get the archaeology cape from Reiniger at the Archaeology Guild.
        - (continue|hearmore)
      - [Choice]: Artisan.
        - **Elen:** I don't keep my house well-maintained since I set myself up here, but I have my construction cape - I got it from an estate agent.
        - **Elen:** And the master crafter in the Crafting Guild north of Rimmington sorted me out with that cape.
        - **Elen:** Ignatius Vulcan is a strange one, but he more than earned his firemaking cape - he's in the forests south of Seers' Village.
        - **Elen:** Not far from him, in Catherby, you'll find Hickton - he sells the fletching cape.
        - **Elen:** And who can forget Thurgo in his hut at Mudskipper Point? He sells the smithing cape...and eats redberry pies!
        - **Elen:** Oh, and as for Invention...you could probably invent your OWN skillcape! Or go see Doc in the Invention Guild.
        - (continue|hearmore)
      - [Choice]: Naturalist.
        - **Elen:** The Varrock Cooks' Guild's head chef will dish out a cooking cape for you.
        - **Elen:** Head to Draynor Village market and talk to Martin the master gardener if you're after a farming cape.
        - **Elen:** If you'd like a herblore cape, talk to Kaqemeex at the stone circle in Taverley.
        - **Elen:** Oh, and Larriar in the Runecrafting Guild atop the Wizards' Tower will sell you that cape!
        - (continue|hearmore)
      - [Choice]: Survivalist.
        - **Elen:** Cap'n Izzy No-Beard in Brimhaven Agility Arena sells the agility cape.
        - **Elen:** He's not quite a master, but Thok Thokson sells the dungeoneering cape over at Daemonheim. He's a bit of a mumbler, that one, doesn't always make sense.
        - **Elen:** Track down the hunting expert in the Feldip Hills if you're after a hunter cape.
        - **Elen:** I'm sure Morvran of Clan Iorwerth would dispute this, but Kuradal in the Ancient Cavern is a master slayer.
        - **Elen:** And finally, you can pilfer the thieving cape from Martin Thwait - he's found in the Rogues' Den, beneath the Pick and {{Sic|Loot}} pub in Taverley.
        - (continue|hearmore)
    - {{anchor|hearmore}}**Elen:** Wanna hear about more, or have you heard enough?
    - [Menu]: Hear about more?
      - [Choice]: Yes - tell me more!
        - (previous2)
      - [Choice]: No - I've heard enough!
        - (end)
  - [Choice]: No.
    - **Elen:** Okay, well, see you around!

#### In the Max Guild building


##### With an inverted cape unlocked

- (Condition: With an inverted cape unlocked:)
  - [Menu]: Choose an option:
    - [Choice]: View regular capes
      - (opens=The Max Cape Marketplace)
    - [Choice]: View inverted capes
      - (opens=The Inverted Max Cape Marketplace)

##### Without an inverted cape unlocked

- (opens=The Max Cape Marketplace)
