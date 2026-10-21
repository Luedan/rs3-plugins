# May

- **Original Wiki Page**: [Transcript:May](https://runescape.wiki/w/Transcript%3AMay)
- **Letter**: `M`

---

## Dialogue Transcript


### When talked to

- **May:** Greetings [traveler{{fact|spelling with 1 L}}/World Guardian]! What can I do for you today?
- (Condition: Only on the first conversation:)
  - **Player:** Who are you? What is all of this?
  - **May:** Well, I'm May, and this...
  - **May:** This is my latest endeavour! I want to help adventurers like you to become the heroes that you're made to be!
  - **Player:** How can you help me?
  - **May:** Well I have an assortment of items and benefits to help make your life a little bit easier.
  - (continue)
- [Menu]: Choose an option:
  - [Choice]: Open the shop.
    - (opens=May's Quest Caravan)
  - [Choice]: Reclaim items.|cond=If there are items to reclaim:
    - (Condition: If only non-combat items can be reclaimed:)
      - (Condition: Without enough backpack space:)
        - **May:** You don't have enough inventory space for me to give you everything right now.
      - (Condition: With enough backpack space:)
        - (receives=missing items)
        - **May:** I've placed your rewards in your inventory.
    - (Condition: If only combat items can be reclaimed:)
      - (Condition: Without enough backpack space:)
        - (Condition: If only Vanquish can be reclaimed:)
          - **May:** You don't have enough free space to reclaim Vanquish.
        - (Condition: If items other than Vanquish can be reclaimed:)
          - **May:** You don't have enough free space to reclaim the Outfit of Trials parts you're missing.
      - (Condition: With enough backpack space:)
        - (Condition: If only Vanquish can be reclaimed:)
          - [pic=Coins 250 detail.png]
          - (continue)
        - (Condition: If items other than Vanquish can be reclaimed:)
          - [pic=Coins 250 detail.png]
          - (continue)
        - [Menu]: Reclaim missing parts for [100,000-1,000,000]?
          - [Choice]: Yes.
            - (removes=coins) (receives=missing Armour of Trials piece(s) and/or Vanquish (melee))
            - (Condition: If only reclaiming Vanquish:)
              - [pic=Vanquish detail.png]
            - (Condition: If reclaiming something other than Vanquish:)
              - [pic=Helm of Trials detail.png]  <!-- image is independent of reclaimed piece -->
          - [Choice]: No.
            - (end)
    - (Condition: If both combat and non-combat items can be reclaimed:)
      - [Menu]: Select an Option
        - [Choice]: Reclaim Outfit of Trials.
          - (above|combat)
        - [Choice]: Reclaim other items.
          - (above|noncombat)
  - [Choice]: [Talk about rewards.]
    - [Menu]: Select an Option
      - [Choice]: Tell me about the Outfit of Trials.
        - **May:** Isn't it glorious? I'm really proud of it!
        - **May:** I once met a woman called Xenia who showed me a helmet that inspired the design of this whole outfit.
        - **May:** It wasn't easy, but I tried to embody what it means to be an adventurer in this outfit. It's ok to struggle, but if you get back up, and keep going you will succeed eventually!
        - **May:** Is there anything else I can help you with?
        - (initial)
      - [Choice]: Tell me about your pets.
        - **May:** They're wonderful, right? I found them when they were just puppies, lost and alone. I have no idea where they came from, and since that day I've never seen another like them.
          - (Condition: If the player hasn't unlocked the Lorehound pet:)
            - **May:** I've trained both to be helpful on an adventure - something which Didymus had quite the natural talent for.
            - **May:** I'll be sad to say goodbye to him, but unlike Fenton he's just dying to get back out into the fray with a worthy hero!
            - (continue)
        - (Condition: If the player has unlocked the Lorehound pet:)
            - **May:** Didymus seems to be having a great time adventuring with you, I hope he's being as well behaved as I trained him to be!
            - (continue)
        - **May:** Is there anything else I can help you with?
        - (initial)
      - [Choice]: Tell me about everything else.
        - **May:** Well there's lots here to help you as you progress in your adventures. There's a way to quickly join other adventurers on their latest endeavour and a title to show off your prowess.
        - **May:** I'll even keep hold of some of the assortment of stuff you're sure to pick up as you travel the land, I've a dedicated chest just for that!
        - **May:** Is there anything else I can help you with?
        - (initial)
      - [Choice]: Goodbye.
        - **May:** Best of luck in your adventures!
  - [Choice]: [Talk about something else.]
    - [Menu]: Select an Option
      - [Choice]: What is all of this?
        - **May:** Well as you can see I'm not the most organised, so there's quite a bit of stuff from my own adventures just strewn about.
        - **May:** Not all of it is mine though, there's also some bits and bobs that I'm just keeping an eye on.
        - **May:** What's really important is what I've got for you! I'm so excited to show you all of it.
        - **May:** Is there anything else I can help you with?
        - (initial)
      - [Choice]: Who are you?
        - **May:** My name is May, and I used to be an adventurer just like you.
        - **May:** I'd always dreamed of building a name for myself, becoming famous around the world! For a while Dionysius even recognised my achievements!
        - **May:** I came to realise that being the star of the shoe is fun, but what I really care about is helping people. So, I hung up my cape, and put my skills to work helping other adventurers.
        - **May:** It's taken me a while to get myself all set up, but now here I am, ready to help adventurers at any stage in their journey!
        - **May:** Is there anything else I can help you with?
        - (initial)
      - [Choice]: Goodbye.
        - **May:** Best of luck in your adventures!

### When attempting to use a locked feature

- **May:** You'll have to unlock that using quest points before you can use it!

### When reclaiming


#### Without anything to reclaim

- **May:** You don't have any items to reclaim at the minute.

#### With items to reclaim


##### Without enough space in backpack

- **May:** You don't have enough inventory space for me to give you everything right now.

##### With enough space in backpack

- **May:** I've placed your rewards in your inventory.

### When using the Armadyl's feather on her

- **May:** I think this may or may not be useful in your future adventures.
- You've unlocked the title: {{Colour Player}}
