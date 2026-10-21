# Shantay

- **Original Wiki Page**: [Transcript:Shantay](https://runescape.wiki/w/Transcript%3AShantay)
- **Letter**: `S`

---

## Dialogue Transcript


### Standard dialogue


#### First-time dialogue

- **Shantay:** Hello, effendi. I am Shantay.
- *If the player is on a free-to-play world:*
  - (continue|free-to-play)
- *If the player is on a members' world:*
  - **Shantay:** I see you're new.
  - (continue|members)

#### Subsequent dialogue

- *If the player is on a free-to-play world:*
  - **Shantay:** Hello, effendi. Welcome to Shantay Pass!
  - **SELECT AN OPTION**
    - What is this place?
      - (below|what-is-this-place)
    - I must be going.
      - (below|going)
- *If the player is on a members' world:*
  - **Shantay:** Hello, effendi.
  - **Shantay:** Please read the billboard poster before going into the desert. It'll give you details on the dangers you can face.
  - **SELECT AN OPTION**
    - What is this place?
      - **Player:** What is this place?
      - **Shantay:** This is Shantay Pass. I guard this area with my men. I am responsible for keeping this pass open and repaired.
      - **Shantay:** My men and I prevent outlaws from getting out of the desert. And we stop the inexperienced from a dry death in the sands. Which would you say you were?
      - **SELECT AN OPTION**
        - I am definitely an outlaw, prepare to die!
          - **Player:** I am definitely an outlaw, prepare to die!
          - **Shantay:** Haha, very funny... Guards, arrest [him/her]!
          - *{{Qact|Shantay guards seize you and lock you up.}}*
          - **Shantay:** That's how we treat troublemakers around here. Now, if you pay a fine I will release you. Otherwise you will be deported to a maximum security jail in Port Sarim. Choose!
          - **WHAT WOULD YOU LIKE TO SAY?**
            - I'll pay.
              - **Player:** I'll pay.
              - Shantay takes 5 coins and unlocks the door.
              - 5 coins have been removed from your money pouch.
            - Deport me to Port Sarim!
              - **Player:** Deport me to Port Sarim!
              - **Shantay:** I hope this teaches you a lesson!
              - *{{qact|You are teleported inside Prison Pete's jail cell in the Port Sarim jail}}*
              - You find yourself in a prison.
            - I'll just stay in here, thanks.
              - **Player:** I'll just stay in here, thanks.
              - **Shantay:** Ah, it is good that you are willing to spend time reflecting on your misdeeds.
        - I am a little inexperienced.
          - **Player:** I am a little inexperienced.
          - **Shantay:** Can I recommend that you take at least one full waterskin into the desert. The sun is very hot, and without water to drink you may die of thirst. I see you carry a knife already on your tool belt. If your waterskins are running dry, you can cut the cacti you see to replenish them.
          - **SELECT AN OPTION**
            - Can I see what you have to sell, please?
              - (below|sell)
            - I must be going.
              - (below|going)
        - Er, neither, I'm an adventurer.
          - **Player:** Er, neither, I'm an adventurer.
          - **Shantay:** Good, I have just the thing for the desert adventurer: clothes that will keep you cool in the heat of the sun. I also sell waterskins, which will help you survive from dying of thirst. And you are free to use the bank chest here. It is unwise to travel the desert wearing thick and heavy armour - you will only dehydrate faster.
          - **SELECT AN OPTION**
            - Can I see what you have to sell, please?
              - (below|sell)
            - I must be going.
              - (below|going)
    - Can I see what you have to sell, please?{{anchor|sell}}
      - **Player:** Can I see what you have to sell, please?
      - **Shantay:** Absolutely, effendi!
      - (opens=Shantay Pass Shop)
    - I must be going.{{anchor|going}}
      - **Player:** I must be going.
      - **Shantay:** So long...

### When trying to open the door after getting arrested

- **Shantay:** Aha, a troublemaker! Now, you have a choice: If you pay a fine of 5 coins, I will release you. Otherwise you will be deported to a maximum security jail in Port Sarim.
- **WHAT WOULD YOU LIKE TO SAY?**
  - I'll pay.
    - (above)
  - Deport me to Port Sarim!
    - (above)
  - I'll just stay in here, thanks.
    - (above)
