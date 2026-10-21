# Marius Giste

- **Original Wiki Page**: [Transcript:Marius Giste](https://runescape.wiki/w/Transcript%3AMarius%20Giste)
- **Letter**: `M`

---

## Dialogue Transcript

{{Incomplete|Lacking backpack space to claim a replacement replica piece}}

### In Varrock Museum


#### Talking to him before finding a strange rock

- **Marius Giste:** Hello there. Welcome to Varrock Museum! Feel free to look around.

#### First time dialogue after finding a strange rock

- **Marius Giste:** Hello there. Welcome to Varrock Museum! Feel free to look around.
- **Player:** I found a rock while I was training.
- **Marius Giste:** A rock? Well, let's have a look, though I doubt we can help you with rocks; that's more of a geologi-
- **Marius Giste:** Oh my!
- **Player:** What?
- **Marius Giste:** Caden Azro! Am I right? Could it be?
- **Caden Azro:** Yes, you see the notch here...and lines there...
- **Player:** What is it? What did I find?
- **Marius Giste:** My dear [sir/madam], my esteemed colleague and I both agree that you have discovered part of Dahmaroc, a mage from the very early days of magic.
- **Marius Giste:** Until now, we believed that the myth was just that: a myth. It seems, however, that the stories may be true.
- **Player:** What stories?
- **Marius Giste:** Well, we've only been able to piece bits together here and there, but it appears that he was a mage of great power who was caught up in an almighty battle back in the Second Age.
- **Marius Giste:** It seems this battle was over who should have the lion's share of runes that the sentient races had found around Gielinor.
- **Player:** Runes? As in the ones I use for magic now? Surely they're unlimited.
- **Marius Giste:** Now they are, yes, but back then there was a limited supply. At least, that's what the scraps of information we've found indicate.
- **Player:** Interesting. So what happened to Dahmaroc?
- **Marius Giste:** As far as we can gather, he lost, was turned to stone and then cursed. It's said he was doomed to spend eternity with the thing he loved most...
- **Player:** That doesn't sound so bad. Did he have a wife?
- **Marius Giste:** Well, we're not sure about that. We do know that he loved to gain knowledge and skill in new disciplines. No taste for fighting, though. Indeed, it was combat that proved to be his downfall.
- [Menu]: Select an Option
  - [Choice]: I'm going to try to put him back together.
    - **Player:** I'm going to try to put him back together. Can I use that plinth over there?
    - **Marius Giste:** Well, I'm not sure. We were reserving that for a statue of Saradomin...
    - **Player:** Oh, go on. What's the worst that could happen? There are already tons of bits of rock around here.
    - **Marius Giste:** Go on then. Be sure you get the rocks paired right, though. They interlock, you see.
    - {{anchor|givebag}}(Condition: If you don't have a statue collection bag, and you have a free inventory space:)
      - **Marius Giste:** By the way, if you want a bag to keep further finds in, I can supply one.
      - (continue)
    - [Menu]: Select an Option
      - [Choice]: Yes please.
        - **Player:** Yes please.
        - (Condition: Without space in backpack:)
          - **Marius Giste:** Unfortunately, you don't have space for it.
          - (other|initialoptions)
        - (Condition: With space in backpack:)
          - [Marius Giste hands you a sturdy bag.]
          - (receives=statue collection bag)
          - (other|initialoptions)
      - [Choice]: No thanks.
        - **Player:** No thanks.
        - (other|initialoptions)
    - (other|initialoptions)
  - [Choice]: How can I stop getting these rocks?
    - (below|stoprocks)

#### Normal dialogue

- **Marius Giste:** Hello there. Welcome to Varrock Museum! Feel free to look around.
- {{anchor|initialoptions}} [Menu]: Select an Option
  - [Choice]: Tell me again where the statue comes from.
    - **Player:** Tell me again where the statue comes from.
    - (above2|statueisfrom)
  - [Choice]: Twin? How do I get its twin?
    - **Player:** Twin? How do I get its twin?
    - **Marius Giste:** Well, I'm not sure, but I suspect the same way you got the first one.
    - **Player:** Why do I even need a twin?
    - **Marius Giste:** Because, rather intriguingly, they interlock in pairs to make up the whole statue without any kind of adhesive being required.
    - (Condition: If the player already has a statue collection bag:)
      - **Marius Giste:** You already have a statue collection bag.
    - (Condition: If the player does not have a statue collection bag:)
      - (continuea|givebag)
  - [Choice]: How do I add it to the statue?
    - **Player:** How do I add it to the statue?
    - **Marius Giste:** If you  have strange rocks you've found from training, simply use the pairs of parts on the plinth over there.
    - **Marius Giste:** If you mean one of the replicas we made for you, use the pairs of replica parts on the plinth in your house.
    - (continuea|givebag2)
  - [Choice]: More...
    - [Menu]: Choose an option:
      - [Choice]: Back...
        - (initial|initialoptions)
      - [Choice]: I found a rock while I was training.
        - **Player:** I found a rock while I was training.
        - **Marius Giste:** One of those rocks for the statue? Well, if you have its twin, go ahead and add it on, by all means.
        - (continuea|givebag2)
      - [Choice]: I'll have to keep a list of pieces.
        - **Player:** I'll have to keep a list of pieces.
        - (Condition: Without space in backpack:)
          - **Marius Giste:** Yes, that is indeed wise. Let me know when you have some space and I'll give you some paper.
          - (continuea|givebag2)
        - (Condition: With space in backpack:)
          - **Marius Giste:** Yes, that would be wise. Here's some paper to use.
          - [Marius Giste hands you a piece of paper which you quickly scribble on.]
          - (receives=Statue of Dahmaroc list)
          - (initial|initialoptions)
        - (Condition: With the list already in backpack:)
          - **Marius Giste:** Yes, that would be wise. I see you already have one there.
          - (initial|initialoptions)
      - [Choice]: cond=If the player has completed the statue at least once before, and destroyed a replica piece:|I've lost a replica piece.
        - (Condition: Without space in backpack:)
          - {{Tmissing}}
        - (Condition: With space in backpack:)
          - **Player:** I've lost a replica piece.
          - The archaeologist hands you a .
          - (receives=Replica statue piece)
          - **Marius Giste:** There you go.
          - (initial|initialoptions)
      - {{anchor|stoprocks}} [Choice]: cond=With collecting rocks turned on|How can I stop getting these rocks?
        - **Player:** How can I stop getting these rocks?
        - **Marius Giste:** Ah, I do recall an incantation that might help. I believe it was...
        - {{qact|Marius Giste casts a spell}}
        - {{RSChat|shadow=yes|colour=yellow|Incanto Negato Silicis}}
        - (initial|initialoptions)
      - [Choice]: cond=With collecting rocks turned off|How can I get these rocks again?
        - **Player:** How can I get these rocks again?
        - **Marius Giste:** Ah, I do recall an incantation that might help. I believe it was...
        - {{qact|Marius Giste casts a spell}}
        - {{RSChat|shadow=yes|colour=yellow|Incanto Additto Silicis}}
        - (continuea|givebag)
      - [Choice]: I'd like to reset my statue.
        - **Player:** I'd like to reset my statue.
        - (Condition: If the plinth is empty:)
          - **Marius Giste:** Ah, there's a slight problem there. You have no  to reset.
        - (Condition: If the plinth has at least a pair of rocks added to it:)
          - **Marius Giste:** Are you sure? You'll lose all of your progress!
          - Warning: You will lose all your progress, including any statue built in your house. This can not be reversed.
          - [Menu]: Choose an option:
            - [Choice]: Yes
              - {{Qact|The statue is cleared.}}
            - [Choice]: No
              - (end)

#### Upon completing the statue

- {{qact|A cutscene of the finished statue gaining lifelike colour and then beginning to shake on the plinth}}
- **Player:** {{RSChat|shadow=yes|colour=yellow|What the...}}
- {{qact|A cutscene of the statue crumbling into pieces and pushing the player backwards and stunning them}}
- **Player:**{{RSChat|shadow=yes|colour=yellow|Oof!}}
- **Player:** I did it! I finished the statue!
- Marius Giste picks small pieces of rock from himself.
- **Marius Giste:** Yes... I saw it explode. Seems the curse is still active.
- **Marius Giste:** You did well. We've been studying the statue as you have been building it, and have managed to make a replica of one of the pieces for you. Perhaps you'd like to start building yourself a statue at home in your study.
- (Condition: If the player has never completed the statue before:)
  - (Condition: Without one free backpack space:)
    - **Marius Giste:** When you have space, come back and collect the plinth to stand it on.
  - (Condition: With one free backpack space:)
    - **Marius Giste:** Here's a plinth for you to build the statue at your house.
    - (receives=statue plinth)
    - [The archaeologist hands over a strong, yet surprisingly light, plinth for your replica statue.]
    - (continue)
- (Condition: Without one free backpack space:)
  - **Marius Giste:** When you have space, pop back and collect the replica piece.
- (Condition: With one free backpack space:)
  - **Marius Giste:** There you go.
  - (receives=replica statue piece)
  - [The archaeologist hands you a replica piece of the statue.]
  - **Marius Giste:**There you go.
  - (initial|initialoptions)

#### Collect rock bag

- (above|givebag2)

#### Toggle rock collection


##### With collecting rocks turned on

- You will no longer find strange rocks.
- (pop-up)
  - {{Pop-up|You will no longer find strange rocks.}}

##### With collecting rocks turned off

- You will now find strange rocks.
- (pop-up)
  - {{Pop-up|You will now find strange rocks.}}
