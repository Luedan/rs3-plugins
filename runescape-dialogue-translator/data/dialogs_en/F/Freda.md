# Freda

- **Original Wiki Page**: [Transcript:Freda](https://runescape.wiki/w/Transcript%3AFreda)
- **Letter**: `F`

---

## Dialogue Transcript


### Before Death Plateau

- **Player:** Hello!
- **Freda:** Well hello there! My, you're a cheerful one! How can I help you?
- [Menu]: Select an Option
  - [Choice]: Who are you?
    - **Freda:** I'm Freda, welcome to my humble home!
    - **Freda:** My husband, Sabbot, and I came here to start a trading post. You know, selling dwarven arms to the Guard.
    - **Freda:** Then the trolls came and took over the plateau before we could get established, so I came to live here.
    - **Player:** What about your husband?
    - **Freda:** That stubborn old mule won't leave the cave we were in! He'd rather die than let the trolls win.
    - **Freda:** I send him soup and letters now and then, and those nice men in town make sure he's okay.
    - **Freda:** Is there anything else you want?
    - (other)
  - [Choice]: Aren't you afraid of the trolls up here?
    - **Freda:** Not at all. There used to be a few around here, but I soon dealt with them.
    - **Player:** How? Aren't trolls really fierce in combat?
    - **Freda:** Yes, but I'm fiercer!
    - **Freda:** I'll have you know I've not been a trader all my life. I do know which end of an axe will do the most damage to a troll.
    - **Freda:** Besides, some of those nice young men from town give me a hand if the trolls come in numbers. But after the last time the trolls seem to have got the hint.
    - **Freda:** It's astonishing what waving an axe at groin height will do to break the will of even the biggest troll!
    - **Player:** So why don't you live with your husband then?
    - **Freda:** Well, I can take on the occasional wandering troll, but a whole horde of them is something else entirely.
    - **Freda:** This place may not be that safe, but at least it's not the middle of a warzone.
    - **Freda:** Anything else I can help you with?
    - (other)
  - [Choice]: That's all, thanks.
    - **Freda:** Oh? Well you take care on your way back.

### After Death Plateau

- **Player:** Hello, Freda.
- **Freda:** Hello there. I heard from some of the boys in town that you really gave those trolls a thrashing!
- **Freda:** You keep it up. Every little helps.
- **Player:** I will!
- **Freda:** Anything else you need?
- [Menu]: Select an Option
  - [Choice]: Who are you?
    - (above)
  - [Choice]: Aren't you afraid of the trolls up here?
    - (above)
  - [Choice]: Can I buy some Climbing boots?
    - **Freda:** I don't see why not. Let me see what I've got in your size.
    - [Menu]: Select an Option
      - [Choice]: Buy standard boots for 12gp.
        - (Condition: With climbing boots already in backpack or bank:)
          - (opens=Freda's Boots)
        - (Condition: Without space in backpack:)
          - **Freda:** Sorry, you don't have anywhere to put these.
          - (opens=Freda's Boots)
        - (Condition: Without 12 gold:)
          - You can not afford that.
          - (pop-up)
            - {{Pop-up|You can not afford that.|warning=yes}}
          - **Freda:** Oops, it looks like you're a little short there. That's 12 gold you need to buy these boots.
          - (opens=Freda's Boots)
        - (Condition: With at least 12 gold:)
          - [You purchase the climbing boots.]
          - (removes=12 coins) (receives=climbing boots)
          - (opens=Freda's Boots)
      - [Choice]: See full range of stock.
        - (opens=Freda's Boots)
  - [Choice]: That's all, thanks.
    - (above)
