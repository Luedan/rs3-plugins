# Gabooty

- **Original Wiki Page**: [Transcript:Gabooty](https://runescape.wiki/w/Transcript%3AGabooty)
- **Letter**: `G`

---

## Dialogue Transcript


### In Tai Bwo Wannai, after Jungle Potion

- **Gabooty:** Hello there...thanks for helping out Trufitus commune with the gods Bwana. We've been able to return to the village thanks to your help.
- [Menu]: Select an Option {{anchor|init}}
  - [Choice]: What do you do here?
    - **Player:** What do you do here?
    - **Gabooty:** Not much really... I run a local shop which earns me a few trading sticks, but that's about it. I keep myself to myself really.
    - [Menu]: Select an Option
      - [Choice]: What are trading sticks? {{anchor|trading-sticks}}
        - **Player:** What are trading sticks?
        - **Gabooty:** They're the local currency Bwana, it's used in Tai Bwo Wannai, there's usually some odd jobs that need doing around the village which you could do to earn some trading sticks.
        - **Gabooty:** Or, if you have something which the local villagers might like, you could sell it to me and I'll pay you for it in trading sticks.
        - [Menu]: Select an Option
          - [Choice]: What sort of things do the local villagers like?
            - **Player:** What sort of things do the local villagers like?
            - **Gabooty:** Gnome cocktails! It's amazing but we all just love them! Luckily I've managed to get stocks of the gnome made cocktails and I supply those to my favourite customers. However, many of the customers really like the cocktails
            - **Gabooty:** made by the adventurers passing through this way. If you ever happen to have any, bring them my way! I'll give you a good deal on it that's for sure!
            - **Player:** How did the villagers ever get to try any gnome cocktails?
            - **Gabooty:** I think it was that gnome pilot who crashed his glider, perhaps he had a little mini-bar on board? Come to think about it, you'd expect the little guy to get his stuff together and move on out of here wouldn't you? He must love the jungle to have stayed here so long!
            - (initial|init)
          - [Choice]: You run a shop?
            - (below|about-shop)
          - [Choice]: I want to ask another question.
            - (below|another-question)
          - [Choice]: Ok, thanks.
            - **Player:** Ok, thanks.
      - [Choice]: ou run a shop? {{anchor|about-shop}}
        - **Player:** You run a shop?
        - **Gabooty:** Yes, it's the Tai Bwo cooperative... catchy name huh! We sell a few local village trinkets and tools. Also, there are a few items that we're actually looking to stock for the locals' sake.
        - **Gabooty:** If you happen across any of them please bring them to me, I'll pay a good price for them. I'm sure you'll find the prices very reasonable.
        - [Menu]: Select an Option{{anchor|options-2}}
          - [Choice]: What are trading sticks?
            - (above|trading-sticks)
          - [Choice]: You run a shop?
            - (above|about-shop)
          - [Choice]: Can I take a look at what you have to sell?
            - **Player:** Can I take a look at what you have to sell?
            - **Gabooty:** Sure you can...which shop would you like to see? The Cooperative or Drinks store?
            - [Menu]: Select an Option
              - [Choice]: The Cooperative
                - (opens=Gabooty's Tai Bwo Wannai Cooperative)
              - [Choice]: The Drinks Store
                - (opens=Gabooty's Tai Bwo Wannai Drinky Store)
              - [Choice]: None thanks...
                - **Player:** None thanks...
          - [Choice]: Why do you only take one sort of Gnome cocktail?
            - **Player:** Why do you only take one sort of Gnome cocktail?
            - **Gabooty:** It's funny that actually. I've managed to get a good deal with the pilot of that gnome glider. He can supply me directly now. However, it's really interesting that the local villagers really like the gnome cocktails made by the adventurers passing through this way.
            - **Player:** Why, what's the difference?
            - **Gabooty:** I think it may just be that they're made fresher, or there is a slight twist in the flavour of the drink, you know, a little more of this, a little less of that, it all adds up and makes for an interesting tipple!
            - (previous2|options-2)
          - [Choice]: I want to ask another question.
            - (below|another-question)
      - [Choice]: I want to ask another question.
        - **Player:** I want to ask another question.
        - **Gabooty:** Sure, what do you want to ask?
        - (initial|init)
      - [Choice]: Ok, thanks.
        - **Player:** Ok, thanks.
  - [Choice]: Is there anything interesting to do here?
    - **Player:** Is there anything interesting to do here?
    - {{Trandom}}
      - (Dialogue 1:)
        - **Gabooty:** Bwana, if anyone else asks me that question today, I'll explode! Go and ask Murcaily!
      - (Dialogue 2:)
        - **Gabooty:** I'm just enjoying the sunshine, Bwana. Try asking Murcaily.
      - (Dialogue 3:)
        - **Gabooty:** Well, I think that there's some work to be done...perhaps Murcaily can help you. He usually tends to the hardwood grove to the east of Trufitus' hut.
      - (Dialogue 4:)
        - **Gabooty:** Sorry Bwana, I'm already busy, why not go and talk to Murcaily! He's around the village somewhere.
  - [Choice]: cond=With Tai Bwo Wannai Cleanup started|I've been doing some work around the village.
    - (Condition: With unclaimed Tai Bwo Wannai favour:)
      - **Gabooty:** Hey, I've seen you working around the village. You've been doing a lot of good work around here for us. Let me give you something for your trouble.
      - (receives=trading sticks)
    - (Condition: Without unclaimed Tai Bwo Wannai favour:)
      - **Gabooty:** I've already given you some trading sticks and I don't have any more on me at the moment. Why not go and talk to some of the other villagers and get some contributions?
  - [Choice]: Ok, thanks.
    - **Player:** Ok, thanks.

#### Occasionally with unclaimed favour

- **Gabooty:** Hey, I've seen you working around the village. You've been doing a lot of good work around here for us. Let me give you something for your trouble.
- (receives=trading sticks)
- You get [number] trading sticks. Your remaining favour totals [percentage].

#### With a tribal mask equipped

- {{Trandom}}
  - (Dialogue 1:)
    - **Gabooty:** Ahhhhhhhh - Get away from me you beast!
    - (continue)
  - (Dialogue 2:)
    - **Gabooty:** Ahhhhhhhh!
    - (continue)
  - (Dialogue 3:)
    - **Gabooty:** Ahhhhhhhh - It's a monster!
    - (continue)
  - (Dialogue 4:)
    - **Gabooty:** Waahhhhh! - It's da evil broodoo beast come ta eat my very soul!
    - (continue)
- **Player:** What's the problem... oh, I'm wearing this big scary mask! I'd better take it off before I start talking to the natives.

#### Treasure Trails

- (Condition: Only the first time:)
  - **Gabooty:** Hey there. If you can solve a question for me then you can move on.
  - **Player:** What is the question?
  - **Gabooty:** Here, I wrote it down for you.
- (receives=challenge scroll (medium))
- [Gabooty has given you a challenge scroll!]

##### When talked to again

- **Gabooty:** Please enter the answer to the question.
- Enter amount:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Gabooty:** Wrong answer!
- (Condition: When given the correct answer:)
  - (removes=the old clue scroll (medium) and challenge scroll (medium))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [Gabooty has given you another clue scroll!]
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [You've found a casket!]
  - **Gabooty:** Sounds right!
