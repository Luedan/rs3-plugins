# Peer the Seer

- **Original Wiki Page**: [Transcript:Peer the Seer](https://runescape.wiki/w/Transcript%3APeer%20the%20Seer)
- **Letter**: `P`

---

## Dialogue Transcript


### Before The Fremennik Trials


#### Talking to him

- **Peer the Seer:** Uuuh... What was that dark presence I felt?
- **Peer the Seer:** !
- **Peer the Seer:** Ahem, sorry about that.
- (Condition: If the player has completed the easy Fremennik achievements:)
  - [Menu]: What would you like to ask about?
    - [Choice]: Deposit service
      - **Player:** Hello, Peer. Could you deposit some things for me, please?
      - **Peer the Seer:** I will oblige you, but it pains me that you are still an outerlander.
      - {{qact|Peer the Seer's deposits interface opens.}}
    - [Choice]: The Fremennik Trials
      - **Peer the Seer:** I have no interest in talking to you just now outerlander.
- (Condition: If the player has not completed the easy Fremennik achievements:)
  - **Peer the Seer:** I have no interest in talking to you just now outerlander.

#### Deposit option

- (Condition: If the player has completed the easy Fremennik achievements:)
  - {{qact|Peer the Seer's deposits interface opens.}}
- (Condition: If the player has not completed the easy Fremennik achievements:)
  - **Peer the Seer:** Do not pester me, outerlander! I will only deposit items into the banks of those who have earned Fremennik sea boots!

#### Attempting to open the door to his house

- **Peer the Seer:** Hey! Outerlander! That is my house! Who do you think you are to just barge into my home without asking?
- **Player:** Um... My name is Player.
- **Peer the Seer:** It was a rhetorical question, outerlander. Now get lost. I do not appreciate intruders in my home.

### After The Fremennik Trials


#### Talking to him

- **Peer the Seer:** Uuuh... What was that dark presence I felt?
- **Peer the Seer:** !
- **Peer the Seer:** Ahem, sorry about that.
- [Menu]: What would you like to ask about?
  - (Condition: If the player has completed the easy Fremennik achievements:)
    - [Choice]: Deposit service
      - **Player:** Hello, Peer. Could you deposit some things for me, please?
      - **Peer the Seer:** Of course, [Fremennik name]. I am always happy to aid those who have earned the right to wear Fremennik sea boots.
      - {{qact|Peer the Seer's deposits interface opens.}}
  - (Condition: If the player has at least one skull, ribcage, or fibula piece in their inventory:)
    - [Choice]: Wallasalki bone armour
      - **Player:** Hello there. I have some wallasalki bone fragments, and I understand you may be able to use them to make some armour for me...?
      - **Peer the Seer:** As you wish, [Fremennik name]. What kind of armour were you thinking of exactly?
      - [Menu]: Select an Option
        - [Choice]: A fine helm
          - **Peer the Seer:** I am afraid it will cost you 5,000 coins to make that for you... Is that okay?
          - [Menu]: Select an Option
            - [Choice]: YES
              - ((If the player does not have the required materials:))
                - **Peer the Seer:** My apologies [Fremennik name], but I will need you to bring me 1 piece of dark daggermouth hide, 1 skull piece and 5,000 coins before I can make this helm for you.
                - (end)
              - (removes=1 dagannoth hide, 1 skull piece, and 5,000 coins) (receives=a skeletal helm)
              - **Peer the Seer:** Ah, a helm to make any seer proud! Did you want me to make you another while I am at it?
              - (continuea|skelehelm)
            - [Choice]: NO
              - (continuea|armour)
        - [Choice]: Sturdy bodyarmour
          - **Peer the Seer:** I am afraid it will cost you 10,000 coins to make that for you... Is that okay?
          - Select an Option
            - [Choice]: YES
              - ((If the player does not have the required materials:))
                - **Peer the Seer:** I am sorry [Fremennik name], but I need 3 pieces of dark daggermouth hide, 1 ribcage piece and 10,000 coins to make you this armour...
                - (end)
              - (removes=3 dagannoth hides, 1 ribcage piece, and 10,000 coins) (receives=a skeletal top)
              - **Peer the Seer:** The seers of legend all wore just such armour! Did you want me to craft you another piece?
              - (continuea|skeletop)
            - [Choice]: NO
              - (continuea|armour)
        - [Choice]: Powerful leg armour
          - **Peer the Seer:** I am afraid it will cost you 7,500 coins to make that for you... Is that okay?
          - [Menu]: Select an Option
            - [Choice]: YES
              - ((If the player does not have the required materials:))
                - **Peer the Seer:** I am very sorry [Fremennik name], but I will require 2 pieces of dark daggermouth hide, 1 fibula piece and 7,500 coins to make this type of leg armour.
                - (end)
              - (removes=2 dagannoth hides, 1 fibula piece, and 7,500 coins) (receives=a skeletal bottoms)
              - **Peer the Seer:** Ah, I used to wear just such a piece of armour to battle in my youth... Do you want me to make you another pair of legs while I am doing it anyway?
              - (continuea|skeleleg)
            - [Choice]: NO
              - (continuea|armour)
        - [Choice]: Nothing
          - **Player:** Actually, I don't want anything.
          - **Peer the Seer:** {{Sic|AS}} you wish.
  - [Choice]: The Fremennik Trials
    - **Player:** Hello Peer.
    - **Peer the Seer:** Greetings to you, [brother/sister] [Fremennik name]! What brings you to see me again?
    - [Menu]: Choose an option:
      - [Choice]: Can you tell my future?
        - **Player:** I was wondering if you could give me a reading on my future...?
        - **Peer the Seer:** Ah, you would like a prediction? I do not see that that would be so difficult... wait a moment...
        - *(One of the following predictions are given, and the selected word within [] is randomly picked:)*
          - *(Prediction 1:)*
            - **Peer the Seer:** Here is your prediction: You will find luck today with the number [one/two/three/four/five/six/seven/eight/nine/ten].
          - *(Prediction 2:)*
            - **Peer the Seer:** Here is your prediction: The colour [black/blue/brown/cyan/green/pink/purple/red/yellow] will bring you luck this day.
          - *(Prediction 3:)*
            - **Peer the Seer:** Here is your prediction: The enemy called [fire giant/ghosts/giant/goblin/green dragon/hobgoblin/lesser demon/moss giant/ogre/zombie] is your lucky totem this day.
          - *(Prediction 4:)*
            - **Peer the Seer:** Here is your prediction: The place called [Al Kharid/Ardougne/Burthorpe/Canifis/Catherby/Falador/Karamja/Varrock/The Wilderness/Yanille] will be worth your time to visit.
          - *(Prediction 5:)*
            - **Peer the Seer:** Here is your prediction: The stars tell me that you should use a [battleaxe/crossbow/dagger/javelin/long sword/mace/scimitar/short sword/spear/warhammer] in combat today.
          - *(Prediction 6:)*
            - **Peer the Seer:** Here is your prediction: You would be wise to train the skill [Agility/Cooking/Crafting/Fishing/Fletching/Herblore/Mining/Runecrafting/Smithing/Thieving] today.
      - [Choice]: Nothing really.
        - **Player:** Nothing really, I just stopped by to say hello.
        - **Peer the Seer:** Well, hello to you too!
