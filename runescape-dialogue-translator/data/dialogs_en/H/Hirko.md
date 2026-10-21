# Hirko

- **Original Wiki Page**: [Transcript:Hirko](https://runescape.wiki/w/Transcript%3AHirko)
- **Letter**: `H`

---

## Dialogue Transcript


### In Keldagrim marketplace


#### Talking to Hirko

- **Hirko:** Hello there!
- **Player:** Hello, what's in those boxes?
- **Hirko:** Aha, interested in my crossbows are you?
- **Player:** Are they any good?
- **Hirko:** They're dwarven engineering at its best. If you've got enough skill in crafting, smithing and fletching, you can even make them yourself. You can buy some of the parts here and make the rest yourself.
- [Menu]: Select an Option
  - [Choice]: How do I make one for myself?
    - **Player:** How do I make one for myself?
    - **Hirko:** Well, firstly you'll need to chop yourself some wood, then use a knife on the wood to whittle out a nice crossbow stock like these here.
    - **Player:** Wood fletched into stock... check.
    - **Hirko:** Then get yourself some metal and a hammer and smith yourself some limbs for the bow, mind that you use the right metals and woods though as some wood is too light to use with some metal and vice versa.
    - **Player:** Which goes with which?
    - **Hirko:** Wood and Bronze as they're basic materials, Oak and Blurite, Willow and Iron, Steel and Teak, Mithril and Maple, Adamant and Mahogany and finally Rune and Yew.
    - **Player:** Ok, so I have my stock and a pair of limbs... what now?
    - **Hirko:** Simply take a hammer and smack the limbs firmly onto the stock. You'll then need a string, only they're not the same as normal bows. You'll need to dry some large animal's meat to get sinew, then spin that on a spinning wheel, it's the only thing we've found to be strong enough for a crossbow.
    - [Menu]: Select an Option
      - [Choice]: What about magic logs?
        - **Player:** What about magic logs?
        - **Hirko:** Well.. I don't rightly know... us dwarves don't work with magic, we prefer gold and rock. Much more stable. I guess you could ask the humans at the rangers guild to see if they can do something but I don't want anything to do with it!
        - **Player:** Thanks for telling me. Bye!
        - (continue|thanks)
      - [Choice]: Thanks for telling me. Bye!
        - (below|thanks)
  - [Choice]: What about ammo?
    - **Player:** What about ammo?
    - **Hirko:** You can smith yourself lots of different bolts, don't forget to flight them with feathers like you do arrows though. There's also the option of tipping any untipped bolt with gems then enchanting them with runes. This can have some pretty powerful effects.
    - **Player:** Oh my poor bank, how will I store all those?!
    - **Hirko:** Don't you worry, I have just the thing here, a bolt pouch designed specially for holding 4 different types of crossbow bolt.
    - **Player:** Wow, how much?
    - (Condition: If the player does not already own a bolt pouch:)
      - **Hirko:** Well let's see now... for you? 1500 gold pieces should do the trick.
      - [Menu]: Would you like to buy a pouch?
        - [Choice]: Yes I'll pay the 1500gp.
          - **Player:** Yes I'll pay the 1500gp.
          - **Hirko:** Hand it over then.
          - (Condition: If the player does not have enough money:)
            - **Player:** Oh, I don't have that much on me.
            - **Hirko:** Best go make some money then, shouldn't take you too long.
          - (Condition: If the player has enough money:)
            - (removes=1,500 coins) (receives=a bolt pouch)
            - [You hand over your gold and receive a well made leather pouch.]
        - [Choice]: Thanks for telling me. Bye!
          - (below|thanks)
    - (Condition: Otherwise:)
      - **Hirko:** Hmm... didn't I see you down here buying one the other day? You can only have one at a time I'm afraid.
  - [Choice]: Thanks for telling me. Bye!
    - {{anchor|thanks}} **Player:** Thanks for telling me. Bye!
    - **Hirko:** Take care, straight shooting.

#### Getting caught while attempting to steal from his stall

- **Hirko:** {{RSChat|Hey! Get your hands off there!}}

#### Trading or speaking to him after stealing from his stall

- **Hirko:** {{RSChat|Halt, thief!}}
- **Hirko:** {{RSChat|Guards, catch that thief!}}
