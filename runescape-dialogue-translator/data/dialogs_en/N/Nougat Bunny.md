# Nougat Bunny

- **Original Wiki Page**: [Transcript:Nougat Bunny](https://runescape.wiki/w/Transcript%3ANougat%20Bunny)
- **Letter**: `N`

---

## Dialogue Transcript


### Talk to


#### Normally


##### Without rewards to claim


##### Without the first Blooming Burrow Egg Hunt in progress

- **Nougat Bunny:** Hey there, Player! Did you know you're talking to Uncle's new egg hunt supervisor for this year?
- (Condition: Without having participated in Blooming Burrow Egg Hunts before this year:)
  - **Player:** Egg hunt? There's an egg hunt this year!?
  - **Nougat Bunny:** This isn't just any egg hunt, this is the Hunt for the Golden Eggs! I've set up three different egg hunts for adventurers to tackle this year.
  - **Nougat Bunny:** But I'm not sure you're ready to tackle all three just yet.
  - **Nougat Bunny:** You'll have to prove your egg hunting prowess by completing a Blooming Burrow egg hunt first!
  - **Player:** This sounds interesting, could you tell me about the Blooming Burrow egg hunt then?
  - (continue|The Blooming Burrow egg hunt)
- (Condition: On the first time of the year having participated in Blooming Burrow Egg Hunts during previous years:)
  - **Player:** The egg hunts are back this year!?
  - **Nougat Bunny:** They sure are! You'll have to prove your egg hunting skills are still sharp by completing the Blooming Burrow egg hunt first, but then you'll be ready to take on this year's other hunts.
  - **Player:** Could you remind me about the Blooming Burrow egg hunt then?
  - (continue|The Blooming Burrow egg hunt)
- [Menu]: Choose an option:
  - [Choice]: Talk about the Blooming Burrow Egg Hunt.
    - **Nougat Bunny:** The Blooming Burrow egg hunt takes place right here, where I'll hide a batch of golden eggs around the burrow for you to find.
    - **Nougat Bunny:** Each day, if you can find all 12 of the hidden eggs, and bring them back to me...
    - **Nougat Bunny:** Then I'll give you a special, egg seekers approved, prize!
    - (Condition: Without having participated in Blooming Burrow Egg Hunts this year:)
      - **Nougat Bunny:** I've just finished hiding today's batch, so take a look around and see if you can find them all.
    - (Condition: Having participated in Blooming Burrow Egg Hunts:)
      - (Condition: Without having participated in a Blooming Burrow Egg Hunt today:)
        - **Nougat Bunny:** I've hidden another set of eggs for you to find around the burrow today, good luck!
        - (Condition: If asking about Blooming Burrow Egg Hunt:)
          - (previous)
      - (Condition: With today's Blooming Burrow Egg Hunt started but without having found all the golden eggs:)
        - **Nougat Bunny:** It looks like you're in the middle of a burrow egg hunt already. Good luck finding the rest of the eggs!
        - Eggs found: [number]/12
        - (previous)
      - (Condition: Having found all the golden eggs for today's Blooming Burrow Egg Hunt:)
        - (continue|With rewards to claim)
      - (Condition: Having claimed rewards for today's Blooming Burrow Egg Hunt:)
        - **Nougat Bunny:** You've already completed the hunt for today. Come back tomorrow and I'll have hidden a new batch of eggs for you to find.
  - [Choice]: Talk about the Gielinor Egg Hunt.
    - **Nougat Bunny:** To keep you busy during the Easter celebrations, I've hidden a bunch of golden eggs all over Gielinor!
    - **Nougat Bunny:** To help point you in their direction, I've put together a book of clues.
    - **Nougat Bunny:** You'll earn spring tokens for any of these golden eggs you're able to find around Gielinor.
    - (Condition: Without having completed a Blooming Burrow Egg Hunt:)
      - **Nougat Bunny:** But I'm not giving clue books out to just anyone. You'll have to prove your egg hunting prowess by completing a Blooming Burrow egg hunt first!
      - (continue)
    - (Condition: Having completed a Blooming Burrow Egg Hunt with the second Gielinor Egg Hunt locked after the start of the second Monday of the event:)
      - You add the additional clues to your egg hunt clue book.
      - (pop-up)
        - {{Pop-up|You add the additional clues to your egg hunt clue book.|colour=#00FF00}}
        - (continue)
      - **Nougat Bunny:** The second week of eggs for the Gielinor egg hunt are now ready to find, here are your clues. Best of luck!
      - (continue)
    - (Condition: Having completed a Blooming Burrow Egg Hunt with the third Gielinor Egg Hunt locked after the start of the third Monday of the event:)
      - You add the additional clues to your egg hunt clue book.
      - (pop-up)
        - {{Pop-up|You add the additional clues to your egg hunt clue book.|colour=#00FF00}}
        - (continue)
      - **Nougat Bunny:** The third week of eggs for the Gielinor egg hunt are now ready to find, here are your clues. Best of luck!
      - (continue)
    - (previous)
  - [Choice]: cond=Having lost the egg hunt clue book:|Reclaim Egg Hunt clue book.
    - **Player:** Nougat, I've unfortunately misplaced my egg hunt clue book. Do you happen to have any spare ones?
    - **Nougat Bunny:** No need to worry, with so much activity around the burrow this year I made plenty to go around.
    - (Condition: Without free space in backpack:)
      - **Nougat Bunny:** Oh, I'm afraid you need at least 1 backpack space free for your clue book. Come and speak to me again when you have the space.
    - (Condition: With free space in backpack:)
      - (receives=egg hunt clue book)
      - [Nougat Bunny hands you a new Egg hunt clue book.]
      - **Player:** Thanks, I'll try to keep track of this one.
      - (previous)
  - [Choice]: Farewell.
    - **Player:** Take care, Nougat.
    - **Nougat Bunny:** You too! Remember to keep an eye out for any of those golden eggs!

##### With the first Blooming Burrow Egg Hunt in progress

- **Nougat Bunny:** Welcome back, Player. It looks like you've still got some eggs left to find around the burrow.
- Eggs found: [number]/12
- **Nougat Bunny:** Come speak with me again once you've found them all and I'll share the details of the other egg-citing hunts!

##### With rewards to claim

- **Nougat Bunny:** Congratulations on finding all 12 eggs, please take this reward for your eagle-eyed effort.
- (Condition: When on the first Blooming Burrow Egg Hunt:)
  - (Condition: Without two free slots in backpack:)
    - **Nougat Bunny:** Oh, I'm afraid you need at least 2 backpack spaces for your reward and clue book. Come and speak to me again when you have the space.
  - (Condition: With two free slots in backpack:)
    - (Condition: As a free-to-play player:)
      - (receives=egg hunt clue book and holiday reward casket (free))
      - [Nougat Bunny hands you an Egg hunt clue book and a Holiday reward casket (free).]
      - (continue)
    - (Condition: As a member:)
      - (receives=egg hunt clue book and holiday reward casket)
      - [Nougat Bunny hands you an Egg hunt clue book and a Holiday reward casket.]
      - (continue)
    - **Nougat Bunny:** That's your very own egg hunt clue book. Now that you've proven yourself as an expert egg hunter, you're ready to take on the Gielinor egg hunt.
    - **Nougat Bunny:** The first week of eggs are ready to find - don't forget you can read the clues in your egg hunt clue book. Best of luck!
- (Condition: When not on the first Blooming Burrow Egg Hunt:)
  - (Condition: Without a free slot in backpack:)
    - **Nougat Bunny:** Oh, I'm afraid you need at least 1 backpack space for your reward. Come and speak to me again when you have the space.
    - (above|Choose an option)
  - (Condition: With a free slot in backpack:)
    - (Condition: As a free-to-play player:)
      - (receives=holiday reward casket (free))
      - [Nougat Bunny hands you a Holiday reward casket (free).]
      - (above|Choose an option)
    - (Condition: As member:)
      - (receives=holiday reward casket)
      - [Nougat Bunny hands you a Holiday reward casket.]
      - The following has been added to your currency pouch: 5 x Treasure Trail Points.
      - (Condition: With at least 30,000 spring tokens:)
        - You have reached the Spring token soft cap of 30,000. You need to spend some tokens in Gummy's store before you can earn more.
        - (pop-up)
          - {{Pop-up|You have reached the Spring token soft cap of 30,000. You need to spend some tokens in Gummy's store before you can earn more.|warning=yes}}
          - (continue)
      - (Condition: If on the first Blooming Burrow Egg Hunt of the year:)
        - (receives=egg hunt clue book)
        - **Nougat Bunny:** Now that you've proven yourself to still be an expert egg hunter, you're ready to take on this {{Sic|years}} Gielinor egg hunt. Check out the clues in this book and see if you can crack where the eggs have been hidden this year.
        - **Nougat Bunny:** The first week of eggs are ready to find - don't forget you can ready the clues in your egg hunt clue book. Best of luck!
        - (continue)
      - (above|Choose an option)

#### With "the Egg" title before having unlocked its "Yolk" variant

- **Nougat Bunny:** That title suits you! Are you going to go hide with the other eggs?
- You've unlocked the 'Yolk' colour for the 'the Egg' title!
- ((Repeated in a pop-up:))
  - You've unlocked the 'Yolk' colour for the 'the Egg' title!
  - (continue)
- **Nougat Bunny:** Just make sure you're careful, or you'll end up scrambled!

### Daily egg hunt


#### Before having claimed the rewards for Blooming Burrow Egg Hunt today


##### Without a Blooming Burrow Egg Hunt in progress

- (above|The Blooming Burrow egg hunt quick)

##### With a Blooming Burrow Egg Hunt in progress


##### Before having found all the golden eggs

- **Nougat Bunny:** It looks like you're in the middle of a burrow egg hunt already. Good luck finding the rest of the eggs!
- Eggs found: [number]/12

##### After having found all the golden eggs

- **Nougat Bunny:** Congratulations on finding all 12 eggs, please take this reward for your eagle-eyed effort.
- (Condition: When on the first Blooming Burrow Egg Hunt of the year:)
  - (Condition: Without two free slots in backpack:)
    - **Nougat Bunny:** Oh, I'm afraid you need at least 2 backpack spaces for your reward and clue book. Come and speak to me again when you have the space.
  - (Condition: With two free slots in backpack:)
    - The following has been added to your currency pouch: 5 x Treasure Trail Points.
    - (receives=egg hunt clue book and holiday reward casket)
    - [Nougat Bunny hands you an Egg hunt clue book and a Holiday reward casket.]
    - **Nougat Bunny:** Now that you've proven yourself to still be an expert egg hunter, you're ready to take on this {{Sic|years}} Gielinor egg hunt. Check out the clues in this book and see if you can crack where the eggs have been hidden this year.
    - **Nougat Bunny:** The first week of eggs are ready to find - don't forget you can read the clues in your egg hunt clue book. Best of luck!
- (Condition: When not on the first Blooming Burrow Egg Hunt of the year:)
  - (Condition: Without a free slot in backpack:)
    - **Nougat Bunny:** Oh, I'm afraid you need at least 1 backpack space for your reward. Come and speak to me again when you have the space.
  - (Condition: With a free slot in backpack:)
    - The following has been added to your currency pouch: 5 x Treasure Trail Points.
    - (receives=holiday reward casket)
    - [Nougat Bunny hands you a Holiday reward casket.]

#### After having claimed the rewards for Blooming Burrow Egg Hunt today

- **Nougat Bunny:** You've already completed the hunt for today. Come back tomorrow and I'll have hidden a new batch of eggs for you to find.

### Overheads (historical)


#### Every 5 minutes when there are 30 or fewer minutes to a Community Egg Hunt starting

- ((The following is also shown as a regular overhead message:))
  - {{Colour: {{Colour|#99FF99|The community egg hunt will be starting in [number] minutes!}}}}

#### The first Community Egg Hunt starting

- ((The following is also shown as a regular overhead message:))
  - {{Colour: {{Colour|#99FF99|The first community egg hunt has now begun. Hop to it everyone!}}}}

#### The second Community Egg Hunt starting

- ((The following is also shown as a regular overhead message:))
  - {{Colour: {{Colour|#99FF99|The second community egg hunt is starting now. Good luck everyone!}}}}

### Trade (historical)

- (opens=Egg Hunter's Hoard)
