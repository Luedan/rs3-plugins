# Charming imp

- **Original Wiki Page**: [Transcript:Charming imp](https://runescape.wiki/w/Transcript%3ACharming%20imp)
- **Letter**: `C`

---

## Dialogue Transcript


### Standard dialogue

*Starts with one of the following lines:*
- **Charming imp:** Hello Player! It's always an honour to spend time with you. How can I help you?
- **Charming imp:** It's a pleasure to see you, Player. How can I help you?
- **Charming imp:** You're looking positively radiant today! How can I help you?
- **Charming imp:** Seeing you, Player, always brightens my day! How can I help you?
*Continues with:*
- [Menu]: Choose an option:
  - [Choice]: Who are you?
    - **Charming imp:** I am a charming imp. It's lovely to see you! I'm looking forward to working with someone as talented as you are.
    - [Menu]: Select an Option
      - [Choice]: It's nice to meet you too!
        - **Charming imp:** Then both of us are having a good day already. So, how can I help you?
        - [Menu]: Select an Option
          - [Choice]: What do you do?
            - (below|role)
          - [Choice]: I don't need anything right now.
            - (below|bye)
      - [Choice]: What do you do?
        - (below|role)
      - [Choice]: I have to go now.
        - (below|bye)
  - [Choice]: What do you do? {{anchor|imp-role}}
    - **Charming imp:** Like all charming imps, I am a collector...nay, a connoisseur of charms. I could tell you all sorts of fascinating stories and facts about charms... Ah - my apologies! I can get a little carried away talking about charms, and there's adventuring to be done! However, as you go about your duties, I can help you and you can help me! If you should slay some vile beast that drops a charm, I will bring it straight into your backpack. However, I can't collect them for you if you don't have anywhere to put them, so make sure there's space in your backpack.
    - [Menu]: Select an Option
      - [Choice]: What's in it for you? {{anchor|imp-goal}}
        - **Charming imp:** I love charms! It's a pleasure just to be able to get my hands on them for a while. Just to experience them... You know, to hold them, catalogue them, count them, sit in baths full of them...that's reward enough for me.
        - **Player:** Um... Baths?
        - **Charming imp:** Yes, of course baths! Anyway if you let me keep some - well, my day would be complete! If you do let me keep any, I'll impart a little of my knowledge of summoning for each one, too. Is there anything else you need?
        - [Menu]: Select an Option
          - [Choice]: Which charms do you keep?
            - (below|keep-charms)
          - [Choice]: Can you tell me more about charms?
            - (below|about-charms)
          - [Choice]: Isn't it cramped in my backpack?
            - (below|backpack)
          - [Choice]: That sounds great! Thanks!
            - (below|thanks)
      - [Choice]: Do you keep any of the charms? {{anchor|keep-charms}}
        - **Charming imp:** I take any that you don't want. I trust your judgement.
        - (opens=Charming imp)
      - [Choice]: Can you tell me more about charms? {{anchor|about-charms}}
        - **Charming imp:** Charms are the essence of a living being - you could think of them as part of a creature's soul. Without the link to a creature of this plane, it would be impossible to summon a spirit creature here. But to me they are more than just tokens used for summoning. They're an exciting world of collecting! It's very hard to express the joy of charms to a non-collector though.
        - [Menu]: Select an Option
          - [Choice]: What's in it for you?
            - (above|imp-goal)
          - [Choice]: Do you keep any of the charms?
            - (above|keep-charms)
          - [Choice]: Isn't it cramped in my backpack?
            - (below|backpack)
          - [Choice]: Right! Well, I have to go now.
            - (below|bye)
      - [Choice]: Isn't it cramped in my backpack? {{anchor|backpack}}
        - **Charming imp:** It's better than being outside! I really don't like wide open spaces. Besides, I get to be near the charms I collect this way. Oh, and don't forget that is there's no room in your backpack, I won't be able to collect any charms! Is there anything else you need?
        - [Menu]: Select an Option
          - [Choice]: What's in it for you?
            - (above|imp-goal)
          - [Choice]: Do you keep any of the charms?
            - (above|keep-charms)
          - [Choice]: Can you tell me more about charms?
            - (above|about-charms)
          - [Choice]: Right! Well, I have to go now.
            - (below|bye)
      - [Choice]: That sounds great. Thanks! {{anchor|thanks}}
        - **Charming imp:** Always a pleasure!
  - [Choice]: I don't need anything right now {{anchor|bye}}
    - **Charming imp:** I hope you have a good day! Goodbye!

### Attempting to add to tool belt

- ((If the player has not learned how to do so from a slayer master:))
  - You need to be taught how to add this to your tool belt by a slayer master.
  - (popup)
    - {{Popup|You need to be taught how to add this to your tool belt by a slayer master.|warning=yes}}
  - (end)
- ((The following is shown in an interface titled 'ADD TO TOOL BELT':))
  - Are you sure you want to add this to your tool belt?<br><br>You will not be able to reclaim it.
    - [Choice]: CANCEL
      - (end)
    - [Choice]: OK
      - (removes=the charming imp)
      - You add the charming imp to your tool belt. You can configure it via the tool belt.
      - (popup)
        - {{Popup|You add the charming imp to your tool belt. You can configure it via the tool belt.|colour=#ebe0bc}}

### Attempting to destroy

- **Charming imp:** Don't send me away! I'm scared of the big wide world out there.
- **Are you sure you want to destroy this object?** If you get rid of the charming imp, there's no way to get him back except by buying him again with 100,000 Dungeoneering tokens.
  - [Choice]: Yes
    - **Charming imp:** I thought we were a team!
  - [Choice]: No
    - **Charming imp:** Please don't scare me like that again!

### Consuming a charm

- The charming imp finds the following charm[s] and teaches you about summoning: [number]x [Type] charm.  <!-- filtered -->

### Collecting a charm

- The charming imp finds the following charm[s] and puts [it/them] in your backpack: [number]x [Type] charm. <!-- filtered -->
Category:Item transcripts
