# Rionasta

- **Original Wiki Page**: [Transcript:Rionasta](https://runescape.wiki/w/Transcript%3ARionasta)
- **Letter**: `R`

---

## Dialogue Transcript


### In Tai Bwo Wannai, after Jungle Potion

- **Rionasta:** Hello there...thanks for helping out Trufitus commune with the gods Bwana. We've been able to return to the village thanks to your help.
- [Menu]: Select an Option
  - [Choice]: What do you do here?
    - **Player:** What do you do here?
    - **Rionasta:** Well, it's funny you should ask that actually, I run the local parcel service to the mainland.
    - **Player:** Parcel service?
    - **Rionasta:** Yes, we sometimes get asked to send items back to the mainland. We can send items to individuals' bank accounts, for a small fee of course.
    - [Menu]: Select an Option{{anchor|opts-2}}
      - [Choice]: How much does it cost?
        - **Player:** How much does it cost?
        - **Rionasta:** It costs 10 trading sticks per item, unfortunately, even stackable items cost the same.
        - [Menu]: Select an Option
          - [Choice]: What are trading sticks and how do I get some?
            - **Player:** What are trading sticks and how do I get some?
            - **Rionasta:** Trading sticks are our local currency, you could perhaps earn some trading sticks by doing some work around the village.
            - **Rionasta:** Have a chat with Murcaily, I think he was looking for someone to help him, he works near the hardwood grove to the east of Trufitus' hut.
            - (previous2|opts-2)
          - [Choice]: Can I send a parcel please?
            - **Player:** Can I send a parcel please?
            - (Condition: With less than 10 trading sticks in backpack:)
              - **Rionasta:** It costs at least 10 trading sticks to use this service. Sorry but you don't have enough.
              - [Menu]: Select an Option
                - [Choice]: What are trading sticks and how do I get some?
                  - (above)
                - [Choice]: Ok, thanks.
                  - (below)
            - (Condition: With at least 10 trading sticks in backpack:)
              - **Rionasta:** Of course...which items would you like to send to your bank?
              - (opens=Parcel service)
          - [Choice]: Ok, thanks.
            - **Player:** Ok, thanks.
      - [Choice]: Can I send a parcel please?
        - (above)
      - [Choice]: Ok, thanks.
        - (above)
  - [Choice]: Is there anything interesting to do here?
    - **Player:** Is there anything interesting to do around here?
    - **Rionasta:** Well, I think that there's some work to be done...perhaps Murcaily can help you. He usually tends to the hardwood grove to the east of Trufitus' hut.
  - [Choice]: cond=With Tai Bwo Wannai Cleanup started|I've been doing some work around the village.
    - (Condition: With unclaimed Tai Bwo Wannai favour:)
      - **Rionasta:** Hey, I've seen you working around the village. You've been doing a lot of good work around here for us. Let me give you something for your trouble.
      - (receives=trading sticks)
    - (Condition: Without unclaimed Tai Bwo Wannai favour:)
      - **Rionasta:** I've already given you some trading sticks and I don't have any more on me at the moment. Why not go and talk to some of the other villagers and get some contributions?
  - [Choice]: Ok, thanks.
    - **Player:** Ok, thanks.

#### Occasionally with unclaimed favour

- **Rionasta:** Hey, I've seen you working around the village. You've been doing a lot of good work around here for us. Let me give you something for your trouble.
- (receives=trading sticks)
- You get [number] trading sticks. Your remaining favour totals [percentage].

#### With a tribal mask equipped

- {{Trandom}}
  - (Dialogue 1:)
    - **Rionasta:** Ahhhhhhhh - Get away from me you beast!
    - (continue)
  - (Dialogue 2:)
    - **Rionasta:** Ahhhhhhhh!
    - (continue)
  - (Dialogue 3:)
    - **Rionasta:** Ahhhhhhhh - It's a monster!
    - (continue)
  - (Dialogue 4:)
    - **Rionasta:** Waahhhhh! - It's da evil broodoo beast come ta eat my very soul!
    - (continue)
- **Player:** What's the problem... oh, I'm wearing this big scary mask! I'd better take it off before I start talking to the natives.
