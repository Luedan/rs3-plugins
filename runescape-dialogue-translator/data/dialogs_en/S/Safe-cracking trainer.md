# Safe-cracking trainer

- **Original Wiki Page**: [Transcript:Safe-cracking trainer](https://runescape.wiki/w/Transcript%3ASafe-cracking%20trainer)
- **Letter**: `S`

---

## Dialogue Transcript


### In the Thieves' Guild


#### First time dialogue

- **Player:** Hello there. What do you do?
- **Safe-cracking trainer:** I'm the trainer of safes like these ones.
- **Player:** They don't look like they take much training...
- **Safe-cracking trainer:** Har-dee-har. No, I train thieves to open them. Wanna hear more?
- [Menu]: Select an Option
  - [Choice]: With pleasure.
    - (Condition: Before A Guild of Our Own:)
      - **Safe-cracking trainer:** The fatal flaw of safes is that their lock mechanisms are really loud.
      - **Safe-cracking trainer:** If you listen, you can hear the tumblers clicking when you get 'em in the right place. But I'm sure a thief of your calibre will have 'em open in no time.
      - **Safe-cracking trainer:**Once you've contributed more to the guild I'll even teach you on how to open these intricate safes.
      - **Safe-cracking trainer:** You're more than welcome to give your fingers a workout on my dummy wall safes. There's nothing in them but hankies though, got to store them somewhere.
    - (Condition: After A Guild of Our Own:)
      - (below|youllcomeacross)
  - [Choice]: About those hankies...
    - [Menu]: Select an Option
      - [Choice]: What are these handkerchiefs for?{{anchor|hankies}}
        - **Player:** What are these handkerchiefs for?
        - **Safe-cracking trainer:** Oh, we use them to keep track of our members' training regiment. Blue handkerchiefs will earn you one point, red ones are worth four. You can claim a reward from any trainer with your hanky points.
        - [Menu]: Select an Option
          - [Choice]: What are these handkerchiefs for?
            - (above)
          - [Choice]: How often can I do this?
            - **Player:** How often can I do this?
            - **Safe-cracking trainer:** The number of hanky points you can claim for depends on your dedication to the art. At the moment, you can claim hanky [amount] points'{{Sic}} worth of training per week.
            - (other)
          - [Choice]: Which activities give which handkerchiefs?
            - **Player:** Which activities give which handkerchiefs?
            - **Safe-cracking trainer:** Our pickpocketing trainers, safes and easy chests carry blue hankies; red hankies can be found on the coshing trainers and behind harder locks.
            - (other)
          - [Choice]: Bye for now.
            - **Player:** Bye for now.
      - [Choice]: How many hanky points do I have?
        - **Player:** How many hanky points do I have?
        - (Condition: With no points:)
          - **Safe-cracking trainer:** You have collected no hanky points yet. You may claim the reward up to [amount] more hanky points this week.
        - (Condition: With points:)
          - **Safe-cracking trainer:** You have collected [amount] hanky points. You may claim the reward up to [amount] more hanky points this week.
          - (other)
      - [Choice]: I'd like to claim a reward for my hanky points.
        - **Player:** I'd like to claim a reward for my hanky points.
        - (Condition: With hanky points left to claim:)
          - **Safe-cracking trainer:** Sure thing! Let's see now...
          - You gain [amount] Thieving XP. You have [amount] points remaining, and may turn in up to [amount] more points this week.
        - (Condition: Without hanky points left to claim:)
          - **Safe-cracking trainer:** Sorry, you've claimed as many hanky points this week as you may at your level.
      - [Choice]: Bye for now.
        - **Player:** Bye for now.
  - [Choice]: Not interested, thank you.
    - **Player:** Not interested, thank you.
    - **Safe-cracking trainer:** Give your fingers a workout on my dummy safes, if you'd like, although there's nothing in 'em but hankies. Got to store them somewhere.

#### Inspecting a safe before learning about safe-cracking


##### Before A Guild of Our Own

- **Safe-cracking trainer:**Once you've contributed more to the guild I'll teach you on how to open these intricate safes.

##### After A Guild of Our Own, without space in backpack{{anchor|youllcomeacross}}

- **Safe-cracking trainer:** You need some free space in your bag, so make some room and let's discuss safecracking once you're done.

##### After A Guild of Our Own, with space in backpack

- **Safe-cracking trainer:** You'll come across safes like the one next to me in a few places. They've often got 'portable' valuables inside.
- **Safe-cracking trainer:** Fatal flaw of safes is that their lock mechanisms are really loud.
- **Safe-cracking trainer:** If you listen, you can hear the tumblers clicking when you get 'em in the right place. But I'm sure a thief of your calibre will have 'em open in no time.
- **Safe-cracking trainer:** Although, without a stethoscope, you might find it harder to hear the tumblers clicking on more intricate safes.
- **Safe-cracking trainer:** See, there are different difficulties of safe that'll test your thieving abilities to increasin' degrees.
- **Safe-cracking trainer:** Got all that?
- **Player:** I think I've cracked it.
- (receives=loot bag and stethoscope)
- The trainer hands you a loot bag and a stethoscope.
- **Player:** What's the loot bag for?
- **Safe-cracking trainer:** When you loot safes, you'll automatically swipe the contents in the bag. Loot bags make stuff easy to carry, less suspicious and they're incredibly fashionable.
- **Safe-cracking trainer:** You got any more questions?
- [Menu]: What would you like to know?{{anchor|cracksafe}}
  - [Choice]: Are there any rewards?
    - **Safe-cracking trainer:** Other than training your sleight of hand and acquiring wealth? Well, you will be able to earn Pilfer Points, I suppose.
    - **Safe-cracking trainer:** Fill up that bag with any amount of loot, then take it over to Robin at the entrance and he'll fence it for Pilfer Points.
    - **Safe-cracking trainer:** Then visit Dodgy Derek's shop to spend them on his downright dirty deals. He has some sweet items, like a shock absorber. It'll stop you getting stunned when you're caught stealing from pockets.
    - (previous)
  - [Choice]: What do I do with the items I steal?
    - **Safe-cracking trainer:** Ah, good question! The problem with stolen goods is that selling them to general stores will get your fingers chopped off, if the courts are feelin' mean.
    - **Safe-cracking trainer:** Thankfully, at the Thieves' Guild, we offer our fencing services. You've proven to be a heck of a thief, so you get full access.
    - **Safe-cracking trainer:** Simply speak to Robin at the entrance, and he'll sort your stolen goods problem. Although, he will take a cut. Literally, if he doesn't like you.
    - (previous)
  - [Choice]: Do you know where I can find the high-level safes?
    - (Condition: With 68 Thieving or lower:)
      - **Safe-cracking trainer:** With your skills, I would recommend searching for safes in the Kingdom of Misthalin. You know: Lumbridge, Varrock.
      - (previous)
    - (Condition: With 69 to 75 Thieving:)
      - **Safe-cracking trainer:** With your skills, I would recommend searching for safes in the Kharidian desert. You know: Al Kharid, Menaphos, Pollnivneach.
      - (previous)
    - (Condition: With 76 to 82 Thieving:)
      - **Safe-cracking trainer:** With your skills, I would recommend searching for safes in the Kingdom of Asgarnia. You know: Falador, Burthorpe, Rimmington.
      - (previous)
    - (Condition: With 83 to 89 Thieving:)
      - **Safe-cracking trainer:** With your skills, I would recommend searching for safes in the Kingdom of Kandarin. You know: Ardougne, Seers' Village, Catherby.
      - (previous)
    - (Condition: With 90 Thieving or higher:)
      - **Safe-cracking trainer:** With your skills, I would recommend searching the furthest reaches of Gielinor. You're an incredible thief, and the most valuable safes are those that are hardest to find.
      - (previous)
  - [Choice]: That's all, thanks.
    - **Player:** Goodbye.

#### Inspecting a safe after learning about safe-cracking

- **Safe-cracking trainer:** This is one of those intricate safes I was talking about. You'll find them all over Gielinor, some harder to crack than others.
- **Safe-cracking trainer:** To crack them effectively, you'll want to bring a stethoscope. This will allow you to turn the dial faster, as you can listen for the clicks.
- {{qact|The safe momentarily flashes blue.}}
- **Safe-cracking trainer:** When the dial is in the correct position, you'll hear a click. Now, if you're quick enough, you can 'brute force' the lock: clicking on the safe to crack it instantly!

#### Subsequent dialogue

- **Safe-cracking trainer:** Hey there. How can I help you?
- [Menu]: Choose an option:
  - [Choice]: About cracking safes...
    - (above|cracksafe)
  - [Choice]: cond=Having lost the loot bag|I lost my loot bag.
    - (Condition: Without space in backpack:)
      - **Safe-cracking trainer:** You need some free space in your inventory or I can't return your bag to you.
    - (Condition: With space in backpack:)
      - (receives=small, medium or large loot bag, depending on tier unlocked)
      - **Safe-cracking trainer:** Here you go. Try not to lose this one.
  - [Choice]: About those hankies...
    - (above|hankies)
  - [Choice]: Nothing.
    - **Player:** Goodbye.
