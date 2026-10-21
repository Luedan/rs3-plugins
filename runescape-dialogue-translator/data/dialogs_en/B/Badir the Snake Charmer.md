# Badir the Snake Charmer

- **Original Wiki Page**: [Transcript:Badir the Snake Charmer](https://runescape.wiki/w/Transcript%3ABadir%20the%20Snake%20Charmer)
- **Letter**: `B`

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Excuse me...
- The snake charmer ignores you. You'll have to find some way to make him pay attention.
- '''Throw a coin into the money pot?
  - [Choice]: Yes.
    - (removes=one coin)
    - [The snake charmer snaps out of his trance and directs his full attention to you.]
    - '''Select an option
      - [Choice]: Wow, a snake charmer. Can I have a go? Please?
        - **Player:** Wow a snake charmer. Can I have a go? Can I have a go? Please?
        - ((If the player does not have a snake charm or snake basket in inventory:))
          - **Badir the Snake Charmer:**  If it means that you'll leave me alone, I would give you my snake charming super starter kit complete with flute and basket.
          - (receives=snake charm and snake basket)
          - [The snake charmer gives you a snake charming flute and a basket.]
        - ((If the player already has a snake charm and snake basket in inventory:))
          - **Badir the Snake Charmer:** Well what's holding you then? You have your own snake charming flute.
        - ((If the player has a snake basket in inventory but not a snake charm:))
          - **Badir the Snake Charmer:** Ah, I see you've lost your charming flute. Here you go, now leave me alone! You're distracting my punters... erm, I mean, crowd.
          - (receives=snake charm)
        - ((If the player has a snake charm in inventory but not a snake basket:))
          - **Badir the Snake Charmer:** Ah, I see you've lost your basket. Here you are, now leave me alone! You're ruining the show.
          - (receives=snake basket)
      - [Choice]: I want to talk to you about animal charming.
        - **Player:** I want to talk to you about animal charming.
        - ((If the player has lost their music scroll and flute:))
          - **Player:** I've lost some of the gear you gave me.
          - **Badir the Snake Charmer:** What do you need?
          - **Player:** I need a new flute and some music.
          - **Badir the Snake Charmer:** There you go. Now if you don't mind I'm busy trying to charm this here snake.
          - (receives=music scroll)
          - (receives=Snake Charm)
        - ((If the player has lost their music scroll only))
          - **Player:** I've lost some of the gear you gave me.
          - **Badir the Snake Charmer:** What do you need?
          - **Player:** I need some more music.
          - **Badir the Snake Charmer:** There you go. Now if you don't mind I'm busy trying to charm this here snake.
          - (receives=music scroll)
        - ((If the player has lost their flute only))
          - **Player:** I've lost some of the gear you gave me.
          - **Badir the Snake Charmer:** What do you need?
          - **Player:** I need another flute.
          - **Badir the Snake Charmer:** There you go. Now if you don't mind I'm busy trying to charm this here snake.
          - (receives=Snake Charm)
        - ((If the player has a music scroll and flute in their inventory:))
          - **Badir the Snake Charmer:** Yes?
          - **Player:** Can you teach me any more about animal charming.
          - **Badir the Snake Charmer:** No, I doubt it. I believe your talents lie in other areas.
  - [Choice]: No.
    - (end)
