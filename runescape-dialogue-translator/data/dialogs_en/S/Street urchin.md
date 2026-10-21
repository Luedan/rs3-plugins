# Street urchin

- **Original Wiki Page**: [Transcript:Street urchin](https://runescape.wiki/w/Transcript%3AStreet%20urchin)
- **Letter**: `S`

---

## Dialogue Transcript


### Before The Feud

- **Player:** Hello there little fellow.
- **Street urchin:** I'm not little and if you say that again I'll gut you.
- **Player:** Easy there, I didn't mean to offend.
- **Street urchin:** I'll let you off this once. Well what do you want? Information?
- **Player:** Yes tell me about...
- [Menu]: Select an Option
  - [Choice]: The Menaphites
    - **Player:** Tell me about the Menaphites.
    - **Street urchin:** They're a bad bunch, always starting fights down in the Asp and Snake. Word on the street is that they're led by some deranged priest. Though nobody gets to see him as he deals through Rashid the Operator. They are planning something but they're such a close knit group that little ever slips out.
    - **Street urchin:** Well do you need any other information then?
    - [Menu]: Select an Option
      - [Choice]: Yes tell me about...
        - **Player:** Yes tell me about...
        - (initial|initial-options)
      - [Choice]: No thanks.
        - **Player:** No thanks{{Sic}}
        - **Street urchin:** Come back if you need any info about anything in the town.
        - **Player:** I will do thanks.
  - [Choice]: The bandits
    - **Player:** Tell me about the bandits.
    - **Street urchin:** There's not much really to say about them, they're just a group of local thugs led by the largest amongst them. They don't harbour the ambitions of the Menaphites.
    - **Street urchin:** Well do you need any other information then?
    - (continuea|other-info)
  - [Choice]: The Mayor
    - **Player:** Tell me about the mayor.
    - **Street urchin:** The mayor is a spineless coward. The current state of the town is all his fault. He didn't stand up to the Menaphites when they first came to town. When he finally realised his mistake he hired a group of thugs to try get rid of them.
    - **Street urchin:** When they discovered him to be weak they turned against him too. Thus causing an even larger mess.
    - **Street urchin:** Well do you need any other information then?
    - (continuea|other-info)
  - [Choice]: The town
    - **Player:** Tell me about the town.
    - **Street urchin:** Not much to say about it. Pollivneach is a small town located between Al Kharid and Menaphos and has a particularly bad crime problem. Besides that nothing much happens here.
    - **Street urchin:** Well do you need any other information then?
    - (continuea|other-info)

### After partial completion of The Feud


#### First-time dialogue

- **Player:** Hey there!
- **Street urchin:** Did you see the way I distracted that guy? Man I'm one smooth operator!
- **Player:** Ya you were good alright.
- **Street urchin:** So where's my money?
- [Menu]: Select an Option
  - [Choice]: What money?
    - **Player:** What money?
    - **Street urchin:** Don't play stupid with me, I'm better at it. Where's my money?
    - **Player:** Oh that money! I don't think you deserve it!
    - **Street urchin:** Liar, thief!
    - **Player:** How observant of you!
    - **Street urchin:** Give me my money!
    - **Player:** Make me!
    - **Street urchin:** You'll be sorry!
  - [Choice]: Here you go, thanks.
    - **Player:** Here you go, thanks.
    - (Condition: Without at least 10 coins:)
      - colour=#EB2F2F
      - (Condition: Repeated in a pop-up:)
        - {{Pop-up|You can not afford that.|warning=yes}}
        - (continue)
      - **Street urchin:**Here I go what? You haven't got any money!
      - **Player:** What money?
      - (continuea|what-money)
    - (Condition: With at least 10 coins:)
      - (removes=10 coins)
      - **Street urchin:** Thanks [sir/ma'am], I didn't think you would hold up your side of the deal. There's not much honour among thieves, you know.
      - **Street urchin:** Well do you need any other information then?
      - [Menu]: Select an Option
        - [Choice]: Yes tell me about....
          - **Player:** Yes tell me about....
          - [Menu]: Select an Option
            - [Choice]: The Menaphites
              - **Player:** Tell me about the Menaphites.
              - **Street urchin:** They're a bad bunch, always starting fights down in the Asp and Snake. Word on the street is that they're led by some deranged priest. Though nobody gets to see him as he deals through Rashid the Operator. They are planning something but they're such a close knit group that little ever slips out.
            - [Choice]: The bandits
              - **Player:** Tell me about the bandits.
              - **Street urchin:** There's not much really to say about them, they're just a group of local thugs led by the largest among them. They don't harbour the ambitions of the Menaphites.
            - [Choice]: The Mayor
              - **Player:** Tell me about the Mayor.
              - **Street urchin:** The mayor is a spineless coward. The current state of the town is all his fault. He didn't stand up to the Menaphites when they first came to town. When he finally realised his mistake he hired a group of thugs to try get rid of them.
              - **Street urchin:** When they discovered him to be weak they turned against him too. Thus causing an even larger mess.
            - [Choice]: Ali Morrisane's nephew
              - **Player:** Tell me about Ali Morrisane's nephew.
              - **Street urchin:** He was ok, although he used to kick us when he caught any of us stealing from his stall.
              - **Player:** Do you know where he is now then?
              - **Street urchin:** He disappeared around a week ago, he was involved in some dodgy business with both the gangs. I think he scammed them. Whether he got away with it or they got him I don't know, but I reckon if you gained either of the gangs' trust they may let you in on some more info.
            - [Choice]: The town
              - **Player:** Tell me about the town.
              - **Street urchin:** Not much really to say about it. Pollnivneach is a small town located between Al Kharid and Menaphos and has a particularly bad crime problem. Besides that nothing much happens here.
            - (continuea|info)
        - [Choice]: No thanks.
          - **Player:** No thanks{{Sic}}
          - **Street urchin:** Come back if you need any info about anything in the town.
          - **Player:** I will do thanks.

#### After refusing to pay the street urchin

- **Player:** Hey there!
- **Street urchin:** Thief! Thief!
- **Player:** Shut up! Don't cause any more trouble or you'll regret it.
- **Street urchin:** Give me double and I'll be quiet!
- (Condition: If the player does not have at least 20 coins:)
  - colour=#EB2F2F
  - (Condition: Repeated in a pop-up:)
    - {{Pop-up|You can not afford that.|warning=yes}}
    - (continue)
  - **Player:** Sorry, I don't have enough money on me, I'll give it to you the next time we meet.
  - **Street urchin:** I've heard that before. If you don't give me the money, you will be sorry.
- (Condition: If the player has at least 20 coins:)
  - **Player:** Ok here you go - you thief.
  - (removes=20 coins)
  - **Street urchin:** How observant of you!

#### After paying the street urchin

- **Player:** Hey there!
- **Street urchin:** Hi! Do you want to go rob some more people? I could do with some more money.
- **Player:** Ok, lets do it again.
- (Condition: If there are no villagers nearby:)
  - **Street urchin:** There doesn't seem to be anyone around to rob at the moment. Perhaps we can try again later.
- (Condition: If there is a villager nearby:)
  - **Street urchin:** {{RSChat|Hey you, camel features! Come here.}}
  - **Villager:** {{RSChat|I know your game guttersnipe.}}
  - **Street urchin:** {{RSChat|???}}
  - **Villager:** {{RSChat|You wont{{Sic}} fool anyone with that trick again.}}
  - **Player:** I don't think that trick will work here again! It's a small town and people talk.
  - **Street urchin:** Well do you need any information then?
  - **Player:** No thanks, I think I have a fair idea of what is going on in the town now.

#### After assisting the street urchin again

- **Player:** Hey there!
- **Street urchin:** Hi! Do you want to go rob some more people? I could do with some more money.
- **Player:** I don't think that trick will work here again! It's a small town and people talk.
- **Street urchin:** Well do you need any information then?
- **Player:** No thanks, I think I have a fair idea of what is going on in the town now.
