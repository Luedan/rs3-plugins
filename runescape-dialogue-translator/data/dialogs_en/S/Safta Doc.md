# Safta Doc

- **Original Wiki Page**: [Transcript:Safta Doc](https://runescape.wiki/w/Transcript%3ASafta%20Doc)
- **Letter**: `S`

---

## Dialogue Transcript


### West of Tai Bwo Wannai, after Jungle Potion

- **Safta Doc:** Hello there...thanks for helping out Trufitus commune with the gods Bwana. We've been able to return to the village thanks to your help.
- [Menu]: Select an Option
  - [Choice]: What do you do here?
    - **Player:** What do you do here?
    - **Safta Doc:** I's been making da machetes for Gabooty's shop Bwana!
    - (Condition: If the player has not repaired a part of the village:)
      - **Safta Doc:** If you're ever needing one Bwana, and you're doing some favours in da village, come let me know, we can work on a deal.
      - (previous)
    - (Condition: If the player has repaired a part of the village fence and talked to Murcaily afterwards:)
      - **Safta Doc:** If you want me to make you a machete we can do a deal if you like.
      - [Menu]: Select an Option
        - [Choice]: Yes, I'd like to get a machete.
          - **Player:** Yes, I'd like to get a machete.
          - **Safta Doc:** Ok Bwana, here's the deal. There are three gem bladed machete types, in order of quality and hacking proficiency, they're ordered from low to high as follows.
          - [Menu]: Select an Option
            - [Choice]: Opal machete.
              - Opal bladed machete - Safta doc needs the following to make this machete : 3 opals - cut or uncut, 1 gout tuber plant and 300 trading sticks.
              - [Menu]: Select an Option
                - [Choice]: Order the Opal machete.
                  - Ok Bwana, if you want to order the  machete, I need 3 opals, either cut or uncut, 1 gout plant tuber and 300 trading sticks please.
                  - (continue)
                - [Choice]: Go back to machete descriptions
                  - (previous)
            - [Choice]: Jade machete.
              - Jade bladed machete - Safta doc needs the following to make this machete : 3  - cut or uncut, 1 gout tuber plant and 600 trading sticks.
              - [Menu]: Select an Option
                - [Choice]: Order the Jade machete.
                  - Ok Bwana, if you want to order the Jade machete, I need 3 jades, either cut or uncut, 1 gout plant tuber and 600 trading sticks please.
                  - (continue)
                - [Choice]: Go back to machete descriptions
                  - (previous)
            - [Choice]: Red Topaz machete.
              - Red Topaz bladed machete - Safta doc needs the following to make this machete : 3  - cut or uncut, 1 gout tuber plant and 1200 trading sticks.
              - [Menu]: Select an Option
                - [Choice]: Order the Red Topaz machete.
                  - Ok Bwana, if you want to order the Red Topaz machete, I need 3 , either cut or uncut, 1 gout plant tuber and 1200 trading sticks please.
                  - (continue)
                - [Choice]: Go back to machete descriptions
                  - (previous)
        - (Condition: Without enough trading sticks:)
          - **Player:** I don't have enough trading sticks, sorry.
          - (continue)
        - (Condition: Without a gout tuber:)
          - **Player:** I don't have a gout plant tuber sorry.
          - (continue)
        - (Condition: Without enough gems:)
          - **Player:** I don't have three opals/jades/Red Topaz!
          - (continue)
        - **Safta Doc:** Ok Bwana, come back when you have them.
        - [Choice]: Talk to Safta-doc
          - **Safta Doc:** So Bwana, do you like the look of the machetes?
          - [Menu]: Select an Option
            - [Choice]: Why do you need gems?
              - **Player:** Why do you need gems?
              - **Safta Doc:** They're tougher than just metal on its own, plus it's the only such resource naturally available in this region.
            - [Choice]: Why do you need a gout plant tuber?
              - **Player:** Why do you need a gout plant tuber?
              - **Safta Doc:** It's one of the harder to find resources which I mix with other ingredients in order to bind the ground down gem dust to the surface of the metal bladed machete. You can sometimes, if you're lucky, find the plant if you hack away at the jungle around here. You'll need to find a way to dig up the tubers though, they're the important part of the plant.
            - [Choice]: Why is it so expensive?
              - **Player:** Why is it so expensive?
              - **Safta Doc:** Expensive bwana, it's quite reasonably priced if you ask me. I can make it cheaper than Gabooty charges for it, that's for sure. And after all, I have to earn a living around here as well you know, I have children to feed!
            - [Choice]: Let me see the machetes again.
              - (previous)
            - [Choice]: Ok, thanks.
              - **Player:** Ok, thanks.
        - [Choice]: No thanks, but I'd like to ask another question.
          - (initial)
        - [Choice]: No thanks, I have to go.
          - **Player:** No thanks, I have to go.
  - [Choice]: Is there anything interesting to do here?
    - **Player:** Is there anything interesting to do here?
    - {{Trandom}}
      - (Dialogue 1:)
        - **Fanellaman:** Bwana, if anyone else asks me that question today, I'll explode! Go and ask Murcaily!
      - (Dialogue 2:)
        - **Fanellaman:** I'm just enjoying the sunshine, Bwana. Try asking Murcaily.
      - (Dialogue 3:)
        - **Fanellaman:** Well, I think that there's some work to be done...perhaps Murcaily can help you. He usually tends to the hardwood grove to the east of Trufitus' hut.
      - (Dialogue 4:)
        - **Fanellaman:** Sorry Bwana, I'm already busy, why not go and talk to Murcaily! He's around the village somewhere.
  - [Choice]: cond=With Tai Bwo Wannai Cleanup started|I've been doing some work around the village.
    - (Condition: With unclaimed Tai Bwo Wannai favour:)
      - **Safta Doc:** Hey, I've seen you working around the village. You've been doing a lot of good work around here for us. Let me give you something for your trouble.
      - (receives=trading sticks)
    - (Condition: Without unclaimed Tai Bwo Wannai favour:)
      - **Safta Doc:** I've already given you some trading sticks and I don't have any more on me at the moment. Why not go and talk to some of the other villagers and get some contributions?
  - [Choice]: Ok, thanks.
    - **Player:** Ok, thanks.

#### Occasionally with unclaimed favour

- **Safta Doc:** Hey, I've seen you working around the village. You've been doing a lot of good work around here for us. Let me give you something for your trouble.
- (receives=trading sticks)
- You get [number] trading sticks. Your remaining favour totals [percentage].

#### With a tribal mask equipped

- {{Trandom}}
  - (Dialogue 1:)
    - **Safta Doc:** Ahhhhhhhh - Get away from me you beast!
    - (continue)
  - (Dialogue 2:)
    - **Safta Doc:** Ahhhhhhhh!
    - (continue)
  - (Dialogue 3:)
    - **Safta Doc:** Ahhhhhhhh - It's a monster!
    - (continue)
  - (Dialogue 4:)
    - **Safta Doc:** Waahhhhh! - It's da evil broodoo beast come ta eat my very soul!
    - (continue)
- **Player:** What's the problem... oh, I'm wearing this big scary mask! I'd better take it off before I start talking to the natives.
