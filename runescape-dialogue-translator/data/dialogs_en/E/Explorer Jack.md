# Explorer Jack

- **Original Wiki Page**: [Transcript:Explorer Jack](https://runescape.wiki/w/Transcript%3AExplorer%20Jack)
- **Letter**: `E`

---

## Dialogue Transcript


### In Lumbridge


#### Before Myths of the White Lands

- **Explorer Jack:** Now, do you have a question about the Task System? Or perhaps I know of a quest that might interest you.
- [Menu]: What do you wish to say?
  - [Choice]: I'd like to ask about achievements and task rewards.
    - (below|Task System)
  - [Choice]: You mentioned a quest?
    - **Explorer Jack:** I did, I did! So, you're interested? Spiffing! I can see the exploring fibre in you!
    - **Player:** Er...
    - **Explorer Jack:** Oh, that exploring flames in your eyes! Just like me in my younger days - eager to discover and take on new challenges, eh?
    - **Player:** Um... so you're going to give me a quest?
    - **Explorer Jack:** A quest? But indeed! A tale of riches is what you need, what?
    - **Player:** Is it?
    - **Explorer Jack:** Yes, and I have just the thing. A snow imp wandered through my door one day and I, curious about foreign lands, as every good explorer should be, asked him for tales of his homeland.
    - (see|Myths of the White Lands)
  - [Choice]: Nothing.
    - (end)

#### After Myths of the White Lands

- **Explorer Jack:** So, how can I help you?
- [Menu]: What do you wish to say?
  - [Choice]: I'd like to ask about achievements and task rewards.
    - (below|Task System)
  - [Choice]: About Myths of the White Lands...
    - (continue|Post-quest dialogue)
  - [Choice]: Nothing.
    - (end)

#### Task System

- (Condition: If the player has completed the Beginner tasks in the Lumbridge and Draynor set and the rewards not claimed:)
  - **Player:** I think I've finished all of the Beginner Tasks in the Lumbridge set.
  - **Explorer Jack:** You have? Oh, well done! We'll make an explorer of you yet.
  - **Player:** Thank you. Is there a reward?
  - **Explorer Jack:** Ah, yes indeed.
  - (receives=Explorer ring 1 and Antique lamp (Beginner Lumbridge Tasks))
  - **Explorer Jack:** Having completed the beginner tasks, you have been granted the ability to use the Explorer emote to show to your friends.
  - **Explorer Jack:** I have also given you an explorer's ring. Now, this is more than just any old ring. Aside from looking good, it also has magical properties giving you a small but useful boost to your Magic and Prayer.
  - **Explorer Jack:** Your ring has the ability to restore some of your run energy for you.
  - **Explorer Jack:** For each of the first three sections of the diary you complete, your ring will gain an extra charge, so the ring you receive from the medium level tasks will have 3 charges for example.
  - **Explorer Jack:** If they should run out, the ring is recharged by the sun each day, so you will be able to use it again tomorrow and so on.
  - **Explorer Jack:** As an extra reward, you can have this old magical lamp to help with your skills. I was going to use it myself, but I don't really need it.
  - **Player:** Thanks very much.
  - **Explorer Jack:** If you should lose your ring, come back to see me and I'm sure I'll have another. Now, did you have anything further to ask?
  - (continue)
- (Condition: If the player has lost their Explorer's ring 1:)
  - **Explorer Jack:** What ho, there! How's that ring working out for you?
  - **Player:** I lost it.
  - (receives=Explorer ring 1)
  - **Explorer Jack:** Lost it, eh? Well, I have another one here that you can have. Try not to lose this one; it doesn't do for explorers like us to go losing things, what?
  - (continue)
- {{anchor|cheevos}} [Menu]: Choose an option:
  - [Choice]: Tell me about the Achievement System.
    - **Explorer Jack:** Well, the Achievement System is a method of guiding yourself while you explore the world.
    - **Explorer Jack:** You can earn special rewards for completing certain achievements; at the very least, each is worth a cash bounty from me.
    - **Explorer Jack:** Some also give items that will help complete other achievements, and many count as progress towards the set for the area that they're in.
    - [Menu]: Choose an option:
      - [Choice]: Tell me about the set reward for this locality.
        - **Explorer Jack:** For completing the Lumbridge and Draynor set, you are presented with an explorer's ring.
        - **Explorer Jack:** This ring will become increasingly useful with each difficultly level of the set that you complete.
        - **Explorer Jack:** When you are presented with your rewards, you will be told of their uses.
        - You may also see what rewards a set item provides by hovering over the Rewards icon for its Exploration Achievement set in the Achievements interface.
        - (previous2|cheevos)
      - [Choice]: How do I claim these rewards?
        - **Player:** How do I claim these rewards?
        - **Explorer Jack:** You need to complete all of the Tasks in the set of a particular difficulty, then you can claim your reward. Most of the Lumbridge set's Tasks are straightforward, although you might find some require quests to be started, if not finished.
        - **Explorer Jack:** To claim the Lumbridge set reward, speak to Bob in Bob's Axes in Lumbridge, Ned in Draynor Village, or myself.
        - (previous2|cheevos)
      - [Choice]: Sorry, I was just leaving.
        - (end)
  - [Choice]: Can I claim any rewards from you?
    - (below|Claim-rewards option)
  - [Choice]: cond=If you have completed any difficulty level of the Lumbridge set tasks:|Could I buy a spare of the reward?
    - [Menu]: Choose an option:
      - [Choice]: Explorer's ring 1
        - **Explorer Jack:** Explorer's ring 1? Yes, but I'm afraid it would cost you 500 coins.
        - [Menu]: Purchase another for 500 coins?
          - [Choice]: Yes
            - [You're handed another Explorer's ring 1.]
            - (receives=Explorer's ring 1) (removes= 500 coins)
          - [Choice]: No
            - **Player:** No thanks.
      - [Choice]: Explorer's ring 2
        - **Explorer Jack:** Explorer's ring 2? Yes, but I'm afraid it would cost you 1,000 coins.
        - [Menu]: Purchase another for 1,000 coins?
          - [Choice]: Yes
            - [You're handed another Explorer's ring 2.]
            - (receives=Explorer's ring 2) (removes= 1,000 coins)
          - [Choice]: No
            - **Player:** No thanks.
      - [Choice]: Explorer's ring 3
        - **Explorer Jack:** Explorer's ring 3? Yes, but I'm afraid it would cost you 2,000 coins.
        - [Menu]: Purchase another for 2,000 coins?
          - [Choice]: Yes
            - [You're handed another Explorer's ring 3.]
            - (receives=Explorer's ring 3) (removes= 2,000 coins)
          - [Choice]: No
            - **Player:** No thanks.
      - [Choice]: Explorer's ring 4
        - **Explorer Jack:** Explorer's ring 4? Yes, but I'm afraid it would cost you 10,000 coins.
        - [Menu]: Purchase another for 10,000 coins?
          - [Choice]: Yes
            - [You're handed another Explorer's ring 4.]
            - (receives=Explorer's ring 4) (removes= 10,000 coins)
          - [Choice]: No
            - **Player:** No thanks.
  - [Choice]: Sorry, I was just leaving.
    - (end)

#### Claim-rewards

- (Condition: Without rewards to claim:)
  - **Explorer Jack:** Sorry, you're not owed any achievement rewards at the moment. Look at your Achievement System for things to do to earn more.
- (Condition: With rewards to claim:)
  - **Explorer Jack:** I'll just fill your inventory with what you need, then.
  - (receives=rewards)
  - (Condition: Without enough backpack space:)
    - **Explorer Jack:** There you go. You didn't have enough space for everything you're owed, so I've held on to the rest.
  - (Condition: With enough backpack space:)
    - **Explorer Jack:** There you go.

#### Attempting to open the trapdoor

- (see|Trapdoor (Explorer Jack))

#### Post-quest dialogue


##### Before claiming the cash reward from the yeti dung

- **Explorer Jack:** Eh, I haven't made any progress with the stones. Please come back later.

##### Claiming the cash reward from the yeti dung, if the player doesn't tell Explorer Jack the truth

- **Explorer Jack:** I let those stones thaw, making a very smelly discovery.
- **Player:** I'm sorry.
- **Explorer Jack:** You knew about it?
- **Player:** I did. When I exited the cave with the 'stones' I met some snow imps, who let me into a secret. This whole quest was a prank on you, as they judged you nosy, greedy and annoying. It was meant to teach you a lesson. They didn't leave me much choice but to complete their plan.
- **Explorer Jack:** Haha, that's a good one, chum! I suppose I deserve it. Nosy, haha!
- **Player:** Glad to see you're taking it lightly.
- **Explorer Jack:** Eh, I've got good news! While you were gone, I managed to sell them to a wandering witch for a goodly sum. She identified it as yeti dung, and said it was a key ingredient in some very advanced ancient potions.
- **Player:** Really?
- **Explorer Jack:** Yes indeed! I've kept some of the money for you. There you go.
- (receives=5,000 coins)
- **Player:** Thank you!

##### After claiming the cash reward from the yeti dung

- [Choice]: About Myths of the White Lands...
  - **Explorer Jack:** I've been to that ice cave the snow imp mentioned. Sliding is great fun! You should go back there sometime.
  - (If the player has discovered some but not all wall paintings:)
    - **Explorer Jack:** Oh and I made a fascinating discovery! in some places, there are paintings on the walls that appear to have been made by a primitive civilisation.
    - **Player:** I know the ones you mean. They're how I figured how to defeat the yeti. I also found more in the other rooms.
    - (If no paintings have been found:)
      - **Explorer Jack:** Ha, but there are some other ones! I could see some behind roots and things. Do go and have a look sometime.
    - (If all but one painting have been found:)
      - **Explorer Jack:** From the sound of it, there's one you haven't seen.

#### Historical dialogue


##### After the Lumbridge Rebuildathon

- **Explorer Jack:** Stupendous! Look what Foreman George and his team of builders have done! This house is perfect!
- **Explorer Jack:** I just need to get a carpet and a few decorations and those months of sleeping rough in the ruins of my house will become a distant memory.
- ((Continues with regular dialogue.))

##### During the Lumbridge Rebuildathon

- **Explorer Jack:** Since the battle between Saradomin and Zamorak started, my house has been a complete wreck!
- **Explorer Jack:** But Foreman George and his team are on the case now. I can't wait to see what they do to it.
- **Explorer Jack:** One thing's for sure: it can't be any worse than the ruin the battle left me with!
- ((Continues with regular dialogue.))

##### During the Battle of Lumbridge and before the Lumbridge Rebuildathon

- **Explorer Jack:** My house! There I was, sat in the living room, having a nice cup of tea and minding my own business, and BANG! My house collapses around me!
- **Explorer Jack:** I went to look - after all I am an explorer - and there, right outside my house, I found Saradomin and Zamorak fighting it out!
- **Explorer Jack:** Seems that their battle had a rather unfortunate effect on my foundations. So, I went back inside and made another cup of tea.
- **Explorer Jack:** I thought to myself that it'll take more than a world-destroying battle between two gigantic all-powerful gods to stop me!
- **Explorer Jack:** So I'm not letting it get me down. I'm still a taskmaster and I have a job to do!
- **Explorer Jack:** Glad to see the battle is over now. I'm not sure how Zamorak will recover from that defeat.
- ((Continues with regular dialogue.))
