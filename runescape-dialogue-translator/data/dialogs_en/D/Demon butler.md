# Demon butler

- **Original Wiki Page**: [Transcript:Demon butler](https://runescape.wiki/w/Transcript%3ADemon%20butler)
- **Letter**: `D`

---

## Dialogue Transcript


### In Servants' Guild

- **Demon butler:** Greetings! I am Alathazdar, butler to the Demon Lords, and I offer thee my services for a mere [number] coins!
- [Menu]: Select an Option
  - [Choice]: What can you do?
    - **Player:** What can you do?
    - **Demon butler:** I have learned my trade under the leash of some of the harshest masters of the Demon Dimensions. I can cook to satisfy the most infernal stomachs, and fly on wings of flame to deposit thine items in the bank or bring planks from the sawmill in seconds.
  - [Choice]: Tell me about your previous jobs
    - **Player:** Tell me about your previous jobs.
    - **Demon butler:** For millennia I have served and waited on the mighty Demon Lords of the Infernal Dimensions. I began as a humble footman in the household of Lord Thammaron, and for several centuries I was the private valet to Delrith. I have also worked in the Grim Underworld, escorting the souls of the dead to their final abodes. But the incessant shadows and hellfire wary me, so I have come to serve mortal masters in the realms of light.
  - [Choice]: You're hired!
    - **Demon butler:** As fun as tumbling through pocket-dimensions sounds, I'll stay put.

#### Historical dialogue

- **Demon butler:** Greetings! I am Alathazdar, butler to the Demon Lords, and I offer thee my services for a mere [number] coins!
- [Menu]: Select an Option
  - [Choice]: What can you do?
    - (above)
  - [Choice]: Tell me about your previous jobs
    - (above)
  - [Choice]: You're hired!
    - (Condition: If the player doesn't have a servant:)
      - (Condition: If the player doesn't have a second bedroom:)
        - [You need a second bedroom with a bed for your servant to sleep in.]
      - **Player:** You're hired!
      - (removes=some coins)
      - **Demon butler:** I shall devote my every art to thy service, my Master.
      - {{Qact|Demon butler disappears from the Servants' Guild}}
    - (Condition: If the player already has a servant:)
      - [You already have a servant.]

### In a player-owned house

- **Demon butler:** I am at thy command, my master.
- [Menu]: Select an option
  - [Choice]: Go to the bank/sawmill...
    - [Menu]: Select an option
      - [Choice]: Take something to the bank
      - **Player:** Can you take something to the bank for me?
        - **Demon butler:** Give any item to me, and I shall take it swiftly to the bank where it will be safe from thieves and harm.
      - [Choice]: Bring something from the bank
        - [Menu]: What would you like from the bank?
          - [Choice]: cond=If previously fetched some items|Fetch [another/another [amount]] [item name].
            - (below)
          - [Choice]: Wooden planks.
            - [Enter amount: [amount]]
              - (Condition: If there are enough items in the bank:)
                - The servant goes to the bank.
                - {{Qact|Demon butler disappears from the house}}
                - {{Qact|Demon butler appears in the house}}
                - **Demon butler:** Master, I have returned with what you asked me to retrieve.
              - (Condition: If there is not enough item in the bank:)
                - **Demon butler:** My Lord, I cannot conjure items out of the air. You do not have any of those items in your bank!
          - [Choice]: Oak planks.
            - (above)
          - [Choice]: Teak planks.
            - (above)
          - [Choice]: More...
            - [Menu]: What would you like from the bank?
              - [Choice]: Mahogany planks.
                - (above)
              - [Choice]: Soft clay.
                - (above)
              - [Choice]: Limestone brick.
                - (above)
              - [Choice]: Steel bar.
                - (above)
              - [Choice]: More...
                - [Menu]: What would you like from the bank?
                  - [Choice]: Cloth.
                    - (above)
                  - [Choice]: Gold leaf.
                    - (above)
                  - [Choice]: Marble block.
                    - (above)
                  - [Choice]: Magic housing stone.
                    - (above)
                  - [Choice]: More...
                    - (previous)
      - [Choice]: Take something to the sawmill
        - **Demon butler:** Give me some logs and I will bound tot the sawmill in mighty demonic strides!
  - [Choice]: Misc...
    - [Menu]: Select an option
      - [Choice]: Make tea
        - **Demon butler:** Thou shalt taste the very tea of the Demon Lords themselves!
        - {{Qact|Demon butler appears in the kitchen and makes tea}}
        - {{Qact|Demon butler appears in front of the player}}
        - **Demon butler:** Behold, thy beverage is complete. Dost thou wish its dark heart softened by the milk of the cow?
        - [Menu]: Select an option
          - [Choice]: Yes please
            - **Player:** Yes please.
            - (receives=Cup of tea with milk)
          - [Choice]: No thanks
            - **Player:** No thanks.
            - (receives=Cup of tea)
          - [Choice]: Actually I don't want any
            - {{Transcript missing}}
      - [Choice]: Serve dinner
        - **Demon butler:** I shall prepare thee a banquet fit for the lords of Pandemonium!
        - **Demon butler:** My powers do not extend to making food levitate, Master. I cannot serve food unless you own a dining table.
      - [Choice]: Serve drinks
        - **Player:** Serve drinks please.
        - **Demon butler:** I shall keep the drink flowing, Master!
        - {{Qact|Demon butler appears in the kitchen}}
        - {{Qact|Demon butler appears in front of the player}}
        - **Demon butler:** Desire'st thou a beverage, my Lord?
        - [Menu]: Select an option
          - [Choice]: Yes please
            - **Player:** Yes please!
            - (receives=a drink)
            - **Demon butler:** Enjoy thy drink!
          - [Choice]: No thanks
            - **Player:** No thanks.
          - [Choice]: Something else
            - (initial)
      - [Choice]: Greet guests
        - **Player:** Stay at the entrance and greet guests.
        - **Demon butler:** Yes, Master. I shall spread the aura of thy hospitality to all visitors!
  - [Choice]: Stop following me
    - (end)
  - [Choice]: You're fired
    - {{Transcript missing}}
