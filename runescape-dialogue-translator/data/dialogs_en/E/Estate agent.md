# Estate agent

- **Original Wiki Page**: [Transcript:Estate agent](https://runescape.wiki/w/Transcript%3AEstate%20agent)
- **Letter**: `E`

---

## Dialogue Transcript


### Talk to


#### Before starting There's No Place Like Home...


##### Outside Rimmington

- **Estate agent:** If it's a house you're wanting, you'll want ot head over to Rimmington and chat to the estate agent there.

##### In Rimmington

- **Estate agent:** I'm sure it's a house you're wanting, but seeing as we've recently recruited Alfred Stonemason, I'll let him give you the rundown on housing. Pop over to him for a chat.

#### During There's No Place Like Home...

- (see|There's No Place Like Home...)

#### After completing There's No Place Like Home...

- **Estate agent:** Welcome to the Gielinorian Housing Agency! What can I do for you?
- [Menu]: Select an Option
  - [Choice]: Tell me about houses.
    - **Player:** Tell me about houses.
    - **Estate agent:** It all came out of the wizards' experiments. They found a way to fold space, so that they could pack many acres of land into an area only a foot across.
    - **Estate agent:** They created several folded-space regions across the world. Each one contains hundreds of small plots where people can build houses.
    - **Player:** Ah, so that's how everyone can have a house without them cluttering up the world!
    - **Estate agent:** Quite. The wizards didn't want to get bogged down in the business side of things so they hired me to sell the houses.
    - **Estate agent:** There are various other people across Gielinor who can help you furnish your house. Or if you're a dab hand at Construction, construct furniture yourself at a furniture workbench.
    - **Estate agent:** You should start by getting some planks to construct furniture with. Try buying them at the Grand Exchange, or making them yourself at a sawmill.
    - (previous)
  - [Choice]: How can I train construction?
    - **Player:** How can I train construction?
    - (Condition: In Rimmington:)
      - **Estate agent:** You can train it right here! You'll find a furniture workbench, as well as members of the Gielinorian Housing Agency who can turn your logs into planks, or turn your noted materials into raw materials.
      - **Estate agent:** Once you've constructed some furniture, you can place it in a furniture storage chest for use within your house.
      - (previous)
    - (Condition: Elsewhere:)
      - **Estate agent:** You can get started with construction training by visiting our headquarters over in Rimmington!
      - **Estate agent:** There you'll find a plethora of amenities to get you well under way with constructing furniture to make your house a home.
      - (previous)
  - [Choice]: Can you switch my preferred exit portal location please?
    - ((The following is shown in an interface titled "SELECT AN OPTION":))
      - Where would you like your house portal moved to?
        - [Choice]: 1. Rimmington (2,500 coins)
          - (continue)
        - [Choice]: 2. Taverley (2,500 coins)
          - (continue)
        - [Choice]: 3. Pollnivneach (3,750 coins)
          - (continue)
        - [Choice]: 4. Rellekka (5,000 coins)
          - (continue)
        - [Choice]: 5. Brimhaven (7,500 coins)
          - (continue)
        - [Choice]: 6. Yanille (12,500 coins)
          - (continue)
        - [Choice]: 7. Menaphos (25,000 coins)
          - (continue)
        - [Choice]: 8. Otot (Mazcab) (25,000 coins)
          - (continue)
        - [Choice]: 9. Prifddinas (25,000 coins)
          - (continue)
      - (Condition: With the house already in the selected location:)
        - Your house portal is already there!
        - (pop-up)
          - {{Pop-up|Your house portal is already there!|warning=yes}}
      - (Condition: Without the house already in the selected location:)
        - (Condition: Without enough coins:)
          - You need [number] coins to move your house portal there.
          - (pop-up)
            - {{Pop-up|You need [number] coins to move your house portal there.|warning=yes}}
        - (Condition: With enough coins:)
          - (The interface closes and the dialogue continues below.)
      - ((Tooltips on the options:))
        - ((Location where the portal is:))
          - {{Interface tooltip|Your main portal is already there!}}
        - ((Other locations without enough coins:))
          - {{Interface tooltip|You need [number] coins.}}
    - (removes=coins depending on the selected location)
    - [Your house portal has been moved to [Location].]
  - [Choice]: Can you tell me about construction contracts?
    - (continue|Contracts)
  - [Choice]: Can you tell me about the Construction skillcape?
    - (Condition: With below 99 Construction:)
      - **Player:** Can you tell me about the Construction skillcape.
      - **Estate agent:** As you may know, skillcapes are only available to masters in a skill. I have spent my entire life building houses and now I spend my time selling them! As a sign of my abilities I wear this Skillcape of Construction. If you ever have enough skill to build a demonic throne, come and talk to me and I'll sell you a skillcape like mine.
    - (Condition: With at least 99 Construction:)
      - [Menu]: Select an Option
        - [Choice]: I'm wondering if you've got any skillcapes lying about?
          - **Player:** I'm wondering if you've got any skillcapes lying about?
          - **Estate agent:** I hope they're not laying about! Any old sod could pick one up and flaunt it around, but...
          - **Estate agent:** I have had something made especially for you, the skillcape of Construction as a token of your mastery in the field.
          - **Estate agent:** Unfortunately, it's quite costly to procure the materials needed to craft such an impressive cape, so it is yours at a cost.
          - [Menu]: Which skillcape would you like to purchase?
            - [Choice]: 99 skillcape.
              - **Player:** I'd like the 99 skillcape please.
              - (Condition: If the player has a ring of charos (a) equipped:)
                - **Estate agent:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
                - [Menu]: Choose an option:
                  - [Choice]: 92,000 coins? That's much too expensive.
                    - **Player:** I know where to find you if I change my mind.
                  - [Choice]: I think I have the money right here, actually.
                    - (Condition: If the player has no backpack space:)
                      - **Estate agent:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some backpack space before I can sell you one.
                    - (Condition: If the player does not have enough money:)
                      - **Player:** But unfortunately, I was mistaken.
                      - **Estate agent:** Well, come back and see me when you do.
                    - (Condition: If the player has enough money:)
                      - (receives=Construction cape and Construction hood) (removes=92,000 coins)
                      - **Estate agent:** Excellent! Wear that cape with pride my friend.
                  - [Choice]: cond=If the player has 120 Construction|I've mastered this skill. Is there anything else?
                    - **Estate agent:** There is something...though I have kept it a secret for a very long time. It is something that can only be worn by a true master.
                    - **Estate agent:** Not even I can wear it - that's how hard it is to achieve.
                    - **Estate agent:** You say you're a master. Stand straight, let me take a look at you...
                    - **Estate agent:** You...really have mastered it. What an honour! It would be my pleasure to sell you a Construction master cape.
                    - (continue|120)
              - (Condition: If the player does not have a ring of charos (a) equipped:)
                - **Estate agent:** For that I require 99,000 coins.
                - [Menu]: Choose an option:
                  - [Choice]: 99,000 coins? That's much too expensive.
                    - **Player:** I know where to find you if I change my mind.
                  - [Choice]: I think I have the money right here, actually.
                    - (Condition: Without 99,000 coins:)
                      - **Player:** But, unfortunately, I don't have enough coins.
                      - **Estate agent:** Well, come back and see me when you do.
                    - (Condition: With 99,000 coins:)
                      - (Condition: Without two free backpack slots:)
                        - **Estate agent:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some backpack space before I can sell you one.
                      - (Condition: With two free backpack slots:)
                        - (removes=99,000 coins) (receives=Construction cape and Construction hood)
                        - **Estate agent:** Excellent! Wear that cape with pride my friend.
                  - [Choice]: cond=If the player has 120 Construction|I've mastered this skill. Is there anything else?
                    - **Estate agent:** There is something...though I have kept it a secret for a very long time. It is something that can only be worn by a true master.
                    - **Estate agent:** Not even I can wear it - that's how hard it is to achieve.
                    - **Estate agent:** You say you're a master. Stand straight, let me take a look at you...
                    - **Estate agent:** You...really have mastered it. What an honour! It would be my pleasure to sell you a Construction master cape.
                    - (continue|120)
            - [Choice]: 120 Master skillcape.
              - **Player:** I'd like the Master cape please.
              - **Estate agent:** You really have proven yourself, not only to the guild, but to me, Player. I'm beyond impressed with what you've accomplished.
              - **Estate agent:** With that, it'd be my {{Sic|honor}} to offer you the Master skillcape for the cost of 120,000 coins.
              - [Menu]: Buy Construction master cape for 120,000 coins?
                - [Choice]: Yes.
                  - (Condition: Without free backpack space:)
                    - **Estate agent:** You do not have enough room in your backpack. Please come back when you have some more.
                  - (Condition: With free backpack space:)
                    - (Condition: Without 120,000 coins:)
                      - You do not have enough money to purchase this cape.
                      - (pop-up)
                        - {{Pop-up|You do not have enough money to purchase this cape.|warning=yes}}
                    - (Condition: With 120,000 coins:)
                      - (removes=120,000 coins) (receives=Construction master cape)
                      - {{Qact|Master cape music plays.}}
                - [Choice]: No.
                  - (end)
        - [Choice]: I've noticed there are a couple of versions of each skillcape.
          - **Estate agent:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
          - (Condition: If you use the old model:)
            - **Estate agent:** It looks like you're currently using the old model for your Construction skillcape. Would you like to change to the newer one?
            - (continue)
          - (Condition: If you use the new model:)
            - **Estate agent:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
            - (continue)
          - [Menu]: Select an Option
            - [Choice]: Yes, I would like to wear the [new/old] version of the skillcape.
              - **Estate agent:** Would you like to wear the [old/newer] model for just this cape, or for the Quest Cape and all of the skillcapes you own?
              - [Menu]: Select an Option
                - [Choice]: I would just like to change the Construction skillcape.
                  - **Estate agent:** No problem, you will now use the [older/newer] model for your Construction skillcape.
                - [Choice]: I would like to change all my skillcapes.
                  - **Estate agent:** No problem, you will now use the [older/newer] model for all of your skillcapes!
                - [Choice]: I've changed my mind!
                  - (end)
            - [Choice]: No, thank you.
              - **Estate agent:** Great! I'm glad you're still enjoying the [old/new] version!
              - (Condition: If the player uses the new model for any other skillcape:)
                - **Estate agent:** If you want, I can make it so you use the old model for all of the skillcapes you own!
                - [Menu]: Select an Option
                  - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
                    - **Estate agent:** Great, you will now use the old model for all of your skillcapes!
                  - [Choice]: No, thanks.
                    - (end)

### Redecorate


#### Before starting There's No Place Like Home...


##### Outside Rimmington

- **Estate agent:** If it's a house you're wanting, you'll want ot head over to Rimmington and chat to the estate agent there.

##### In Rimmington

- **Estate agent:** I'm sure it's a house you're wanting, but seeing as we've recently recruited Alfred Stonemason, I'll let him give you the rundown on housing. Pop over to him for a chat.

#### During There's No Place Like Home...

- (see|There's No Place Like Home...)

#### After completing There's No Place Like Home...

- **Estate agent:** Certainly. My magic can rebuild the exterior of your house in a completely new style! Which one would you like?
- ((The following is shown in an interface titled "SELECT AN OPTION":))
  - Which house style would you like?
    - [Choice]: 1. Basic wood (1,250)
      - ((The interface closes and the dialogue continues below.))
    - [Choice]: 2. Basic stone (2,500)
      - ((The interface closes and the dialogue continues below.))
    - [Choice]: 3. Fancy stone (12,500)
      - ((The interface closes and the dialogue continues below.))
    - [Choice]: 4. Dark stone (12,500)
      - ((The interface closes and the dialogue continues below.))
    - [Choice]: 5. Fremennik-style wood (5,000)
      - ((The interface closes and the dialogue continues below.))
- (removes=coins corresponding to the cost of the selected option)
- **Estate agent:** Your house has been re-decorated.

### Contracts

- [Menu]: Choose an option:
  - [Choice]: cond=Without a contract|I want a new contract.
    - (Condition: Without free backpack space:)
      - **Estate agent:** You're going to require some space in your backpack for a contract.
    - (Condition: With free backpack space:)
      - (receives=Construction contract)
      - You're handed a Construction contract.
      - **Estate agent:** Here you are, this just came in for [character] over in [location].
      - **Player:** Thanks! I'll see what I can do.
  - [Choice]: cond=With a contract|What's my current contract?
    - **Estate agent:** It looks like you're in the middle of helping out [character] over in [location].
    - (Condition: If the Construction contract has been lost:)
      - (Condition: Without free backpack space:)
        - **Estate agent:** You're going to require some space in your backpack for a contract.
      - (Condition: With free backpack space:)
        - (receives=Construction contract)
        - You're handed a Construction contract.
  - [Choice]: Tell me about contracts
    - **Estate agent:** There are many homeowners around Gielinor that are struggling to keep up with repairs on a regular basis.
    - **Estate agent:** So right now there's a market opportunity to put your construction skills to use and help them out.
    - **Estate agent:** We estate agents can provide you with a contract. This contract will tell you who needs help and what they need repairing.
    - **Estate agent:** All you need to do is head on over and repair all the broken furniture.
    - **Estate agent:** You can either use basic materials for a cheaper, but slower repair job. Or you can use more expensive materials for a faster return and more experience.
    - **Estate agent:** Whatever you choose, you'll gain a chunk of experience once you've repaired all the pieces of furniture that need repairing.
    - **Estate agent:** We'll also reward you with contract credits, which you can redeem from any estate agent for assorted rewards.
    - (previous|Contracts)
  - [Choice]: cond=If the player has lost their plank box|I've lost my plank box.
    - **Player:** I've lost my plank box.
    - **Estate agent:** Not to worry, I have another lying around.
    - (Condition: Without free backpack space:)
      - **Estate agent:** Come back when you have some free space in your backpack.
    - (Condition: With free backpack space:)
      - (receives=plank box)
      - **Estate agent:** Try not to lose this one though.
  - [Choice]: Do you have anything I can buy?
    - (opens=Estate Agents Shop)
  - [Choice]: [Leave]
    - (end)

### Shop

- (opens=Estate Agents Shop)
