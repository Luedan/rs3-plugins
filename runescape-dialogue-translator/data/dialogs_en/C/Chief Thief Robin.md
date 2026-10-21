# Chief Thief Robin

- **Original Wiki Page**: [Transcript:Chief Thief Robin](https://runescape.wiki/w/Transcript%3AChief%20Thief%20Robin)
- **Letter**: `C`

---

## Dialogue Transcript


### In the Thieves' Guild


#### Talking to him


##### Before Buyers and Cellars

- **Player:** Hello there.
- **Chief Thief Robin:** Greetings. I'm Robin, the Guildmaster's assistant.
- **Chief Thief Robin:** Now, what can I do for you?
- [Menu]: Select an Option
  - [Choice]: That's an appropriate name.
    - **Player:** That's an appropriate name.
    - **Chief Thief Robin:** Yes, I've never heard that one before.
    - **Chief Thief Robin:** Still, it's not so bad... If I hadn't been mocked for my name as a lad, I might never have decided in a fit of ironic pique to learn how to rob from the rich and give to the poor.
    - **Player:** Are you the poor in question?
    - **Chief Thief Robin:** Well, I was.
    - **Chief Thief Robin:** Having given myself the goods stolen from several rich people, I'm now of limited but comfortable means.
    - **Chief Thief Robin:** Now, what can I do for you?
    - (initial|init-options-robin-1)
  - [Choice]: How long have you known the Guildmaster?
    - **Player:** How long have you known the Guildmaster?
    - **Chief Thief Robin:** Oh, some time now. We started in business together when he was a con artist, talking people into handing over their hard-earned valuables with lies and vague promises of reward.
    - **Chief Thief Robin:** Obviously, that's all behind us now.
    - **Chief Thief Robin:** Now, what can I do for you?
    - (initial|init-options-robin-1)
  - [Choice]: Bye for now.
    - **Player:** Bye for now.

##### After Buyers and Cellars

- **Player:** Hello there.
- **Chief Thief Robin:** Ah, our rising star.
- **Chief Thief Robin:** Now, what can I do for you?
- [Menu]: Select an Option
  - [Choice]: That's an appropriate name.
    - (above|appropriate)
  - [Choice]: How long have you known the Guildmaster?
    - (above|known)
  - [Choice]: Where can I practice my art?
    - **Player:** Where can I practice my art?
    - **Chief Thief Robin:** I hear there's a fellow in Al Kharid who needs someone for some infiltration work.
    - (Condition: With 40 Agility:)
      - **Chief Thief Robin:** There's rumours of a pyramid out in the deep desert full of traps and valuables.
      - (continue)
    - (Condition: With 50 Agility and 50 Thieving:)
      - **Chief Thief Robin:** And a colleague of ours has set up a maze game in Burthorpe, if you feel light on your feet.
      - (continue)
    - **Player:** Thanks, Robin.
    - **Chief Thief Robin:** Now, what can I do for you?
    - (initial|init-options-robin-2)
  - [Choice]: Could you help me sell these items?
    - (below|Fence items)
  - [Choice]: Bye for now.
    - **Player:** Bye for now.

#### Fence items


##### Before A Guild of Our Own

- **Chief Thief Robin:** You will have to help the guild more before I will be able to fence items for you.

##### Before receiving a loot bag from the safe-cracking trainer

- **Chief Thief Robin:** You will have to talk to the safe cracking tutor before I can help you fence your items.

##### After A Guild of Our Own

- (Condition: Without a loot bag in backpack:)
  - **Chief Thief Robin:** You'll have to bring your looting bag if you want me to take a look and see what we could fence.
- (Condition: With an empty loot bag in backpack:)
  - **Chief Thief Robin:** It doesn't look like you've got anything we can fence right now. Come back when you've filled that bag of yours up.
- (Condition: With a filled loot bag in backpack:)
  - You have received [number] xp, [number] gold and [number] pilfer points.<br>You now have [number] pilfer points.
- (Condition: With a filled loot bag in backpack but with 60,000 pilfer points in currency pouch:)
  - You can't receive any more pilfer points. Please go spend some at Dodgy Derek's Dirty Deals.
