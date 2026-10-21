# Beekeeper

- **Original Wiki Page**: [Transcript:Beekeeper](https://runescape.wiki/w/Transcript%3ABeekeeper)
- **Letter**: `B`

---

## Dialogue Transcript

{{Incomplete|Missing non-quest dialogue before/during Troll Romance quests. Missing some random event dialogue pre-2012, possibly unchanged in OSRS.}}

### Standard dialogue

- **Beekeeper:** Hello! What do you think of my apiary? Nice, isn't it?
- **Player:** You mean all these beehives?
- **Beekeeper:** Yup! They're filled with bees. Also wax, and delicious honey too! You're welcome to help yourself to as much wax and honey as you like.
- (Condition: If the player doesn't have insect repellent in their tool belt or backpack:)
  - **Beekeeper:** Oh, but you'll need some insect repellent - here.
  - The beekeeper hands you some insect repellent.
  - (receives=Insect repellent)
  - **Player:** Thank you!
  - (continue)
- **Beekeeper:** Leave the bees, though. The bees are mine! I love bees!
- {{anchor|beekeepoptions}}[Menu]: Select an option
  - [Choice]: What is honey good for?
    - **Beekeeper:** Ah, well, it's more the honeycomb that you'll want. I hear some people use it to infuse pouches to summon the dreaded honey badger! So long as you are carrying some repellent, you can just grab as much as you like.
    - (previous|beekeepoptions)
  - [Choice]: About beeswax...
    - **Beekeeper:** Hmm, well, you'll need an empty bucket to collect some beeswax. There's a spare bucket around here somewhere you can have. It's trickier to get hold of than honeycomb. You'll have to actually use some repellent on the hive before filling your bucket with wax. I'm not sure what you'd want it for, though - it doesn't have many uses.
    - (previous|beekeepoptions)
  - [Choice]: See you later.
    - **Beekeeper:** Okay, but 'bee' good. Haha! Geddit? You know, because 'bees'...

### Beekeeper's random event

*When participating in the Beekeeper random event before its removal in the 24 October 2012 update.*
- **Beekeeper:** Ah, Player. I'm sorry to drag you away like this, but I need some help building a new hive for my bees.
- **Player:** What do you want me to do?
- **Beekeeper:** All the components of the beehive are jumbled up. You've got to put them in the correct order for building a hive.
- **Player:** Oh, very well. Let's take a look...
- {{qact|Beekeeper random event interface opens}}
- (Condition: If the player attempts to finish the puzzle without moving all pieces into a slot:)
  - shadow=yes
- (Condition: If the player doesn't complete the puzzle correctly:)
  - **Beekeeper:** No, that doesn't look right. You have to put the components in the right order, otherwise it'll be no good as a beehive. I'll let you have (amount between 5-1) more tries.
  - {{qact|Beekeeper random event interface opens again with each piece removed}}
- (Condition: If the player completes the puzzle correctly:)
  - **Beekeeper:** That's perfect! I'll get some bees moved in immediately. Now, I'm sure I must have something to offer you for all your help...
  - {{qact|Dialogue ends and the player is teleported away from the event, and they receive a random event gift}}
- (Condition: If the player fails to complete the puzzle and has no more tries left:)
  - {{transcript missing|The bees attack the player before beekeeper teleports him away -- }}
- (Condition: If the player exits out of the dialogue and then speaks to the beekeeper again:)
  - {{transcript missing|The beekeeper would remind the player what to do with unique dialogue --}}

#### Talking to someone else's beekeeper

(Condition: Attempting to talk to a beekeeper that is after another player:)
- **Beekeeper:** Sorry, you're not the person I need.
