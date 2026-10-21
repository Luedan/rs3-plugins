# Runvastr

- **Original Wiki Page**: [Transcript:Runvastr](https://runescape.wiki/w/Transcript%3ARunvastr)
- **Letter**: `R`

---

## Dialogue Transcript


### Before Love Story

- **Runvastr:** Oh, leave an old dwarf in peace will you?
- **Player:** Why, what's wrong?
- **Runvastr:** Ninety years down in the mines, and this is all I got out of it. All my life wasted away.
- **Player:** You've still got a nice house, don't you?
- **Runvastr:** A crummy old house in East, that's all my life amounts to.
- **Player:** I'll leave you alone then.

### After Love Story

- **Runvastr:** Why are you bothering me, human? I laboured in the mines for ninety years, and I want a bit of peace now that I'm retired.
- [Menu]: What would you like to say?
  - [Choice]: cond=If the player has not yet received the miner's diary|Tell me about your life as a miner.
    - **Player:** Tell me about your life as a miner.
    - **Runvastr:** You want me to talk about mining, huh? Ahhh, I remember swinging my pickaxe hour after hour, day after day, down in the dark and damp mines.
    - **Runvastr:** Old Saggy-face, the supervisor, would be there with his sharpest pickaxe, looking out for slackers to impale. Of course, the trolls got him in the end.
    - **Runvastr:** Poor old Saggy-face. We'd found a tribe of trolls roaming the tunnels: huge trolls from the mountains.
    - **Runvastr:** Saggy-face tried to take them on single-handed, and they ripped his head clean off his shoulders.
    - **Runvastr:** Fortunately, we had that mad human, Dissy, staying in the city at the time. He drove those trolls right out of the mines with his magicks.
    - **Player:** Dissy, huh? Was his full name Dionysius?
    - **Runvastr:** All human names sound the same to me. Here, I've got my old diary from that time. Take it and read all about those days.
    - (receives=miner's diary)
    - [The old dwarf gives you a tatty book.]
  - [Choice]: cond=If the player has already received the miner's diary before|I need another copy of your diary.
    - (Condition: If the player lost the diary:)
      - **Player:** I need another copy of your diary.
      - **Runvastr:** Bah! Young people are so careless. I suppose I'll have to give you another copy.
      - (receives=miner's diary)
      - [The old dwarf gives you a tatty book.]
    - (Condition: If the player had given the diary to the Wise Old Man:)
      - **Player:** I need another copy of your diary.
      - **Runvastr:** Bah! Young people are so careless.
      - **Player:** I gave it to Dionysius, the mage who helped you drive out the trolls from your mines.
      - **Runvastr:** I'm glad I'm not the only person from those days who's still alive. Here, I'll give you another copy.
      - (Condition: If the player has no backpack space:)
        - **Player:** My inventory's too full.
        - **Runvastr:** Ah, you young people always have so much stuff. In my day, we just carried a pickaxe, and that was enough for us.
      - (Condition: If the player has at least one backpack space:)
        - (receives=miner's diary)
        - [The old dwarf gives you a tatty book.]
  - [Choice]: Can you give me any free stuff?
    - **Player:** Can you give me any free stuff?
    - **Runvastr:** Bah! In my day, people worked for a living, and anyone who wouldn't work got a short, sharp shock with a pickaxe. That's how it was. Ahhh.
    - **Player:** So that's 'no', then?
    - **Runvastr:** Go away!
  - [Choice]: Sorry, I'll leave you alone.
    - **Player:** Sorry, I'll leave you alone.
    - **Runvastr:** Good!
