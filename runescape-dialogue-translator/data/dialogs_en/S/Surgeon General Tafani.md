# Surgeon General Tafani

- **Original Wiki Page**: [Transcript:Surgeon General Tafani](https://runescape.wiki/w/Transcript%3ASurgeon%20General%20Tafani)
- **Letter**: `S`

---

## Dialogue Transcript


### Talk to


#### Normally

- **Player:** Hi!
- **Surgeon General Tafani:** Hi. How can I help?
- Select an option
  - Can you heal me?
    - **Player:** Can you heal me?
    - **Surgeon General Tafani:** Of course!
    - {{Qact|Surgeon General Tafani attempts to heal the player.}}
    - *(If the player has full health:)*
      - **Surgeon General Tafani:** You look healthy to me!
      - (continue)
    - *(If the player does not have full health:)*
      - {{Qact|The player is healed for some life points.}}
      - You feel a little better.
      - (continue)
  - Do you see a lot of injured fighters?
    - **Player:** Do you see a lot of injured fighters?
    - ((Before the destruction of Duel Arena:))
      - **Surgeon General Tafani:** Yes, I do. Thankfully, we can cope with almost anything. Jaraah really is a wonderful surgeon; his methods are a little unorthodox but he gets the job done. I shouldn't tell you this, but his nickname is 'The Butcher'.
      - **Player:** That's reassuring.
    - ((After the destruction of Duel Arena:))
      - **Surgeon General Tafani:** Not so much these days, but back when the Duel Arena was still around I saw my fair share of injuries.
      - **Surgeon General Tafani:** Thankfully, we could cope with almost anything. Jaraah really is a wonderful surgeon. His methods were a little unorthodox, but he got the job done.
      - **Surgeon General Tafani:** I shouldn't tell you this, but his nickname is 'The Butcher'.
      - **Player:** That's reassuring.
      - (previous)
  - Do you come here often?
    - **Player:** Do you come here often?
    - ((Before the destruction of Duel Arena:))
      - **Surgeon General Tafani:** I work here, so yes. You're silly!
    - ((After the destruction of Duel Arena:))
      - **Surgeon General Tafani:** Well, this is where I work now, so yes. Here's as good a place as any to set up a hospital.
      - (previous)
  - ((Only if not returning from another question:))
    - Can I buy a Skillcape of Constitution from you?
      - *(If the player has any of the Ring of Charos variants equipped:)*
        - **Surgeon General Tafani:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
        - Choose an option:
          - 92,000 coins? That's much too expensive.
            - (below|expensive)
          - I think I have the money right here, actually.
            - (below|buy-cape)
      - *(If the player doesn't have any of the Ring of Charos variants equipped:)*
        - **Surgeon General Tafani:** Why, certainly my friend. However, owning such an item makes you part of an elite group, and that privilege will cost you 99,000 coins.
        - Choose an option:
          - 99,000 coins? That's much too expensive.
            - **Surgeon General Tafani:{{anchor|expensive}}** Not at all; there are many other adventurers who would love the opportunity to purchase such a prestigious item! You can find me here if you change your mind.
          - I think I have the money right here, actually.{{anchor|buy-cape}}
            - *(If the player has the required amount of coins:)*
              - (removes=the required coins) (receives=Constitution cape (if the player only has level 99 in Constitution) or Constitution cape (t) (if the player has level 99 in multiple skills) and Constitution hood)
              - **Surgeon General Tafani:** Excellent! Wear that cape with pride my friend.
            - *(If the player doesn't have the required amount of coins:)*
              - **Player:** But, unfortunately, I was mistaken.
              - **Surgeon General Tafani:** Well, come back and see me when you do.
          - [Choice]: cond=Only with true skill mastery in Constitution:|I've mastered this skill. Is there anything else?
            - **Surgeon General Tafani:** There is something...though I have kept it a secret for a very long time. It is something that can only be worn by a true master.
            - **Surgeon General Tafani:** Not even I can wear it - that's how hard it is to achieve.
            - **Surgeon General Tafani:** You say you're a master. Stand straight, let me take a look at you...
            - **Surgeon General Tafani:** You...really have mastered it. What an honour! It would be my pleasure to sell you a Constitution master cape.
            - [Menu]: Buy Constitution master cape for 120,000 coins?
              - (Yes.)
                - (Condition: Without free backpack space:)
                  - **Surgeon General Tafani:** You do not have enough room in your backpack. Please come back when you have some more.
                - (Condition: With free backpack space:)
                  - (Condition: Without 120,000 coins:)
                    - You do not have enough money to purchase this cape.
                    - ((Repeated in a pop-up:))
                      - You do not have enough money to purchase this cape.
                  - (Condition: With 120,000 coins:)
                    - (removes=120,000 coins) (receives=Constitution master cape)
                    - {{Qact|Master cape music plays.}}
              - [Choice]: No.
                - (end)
  - ((Only if not returning from another question:))
    - I've noticed there are a couple of versions of each skillcape.
      - **Surgeon General Tafani:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
      - *(If the player has chosen the new skillcape models:)*
        - **Surgeon General Tafani:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
        - Select an option
          - Yes, I would like to wear the old version of the skillcape.
            - **Surgeon General Tafani:** Would you like to wear the old model for just this cape, or for the Quest point cape and all of the skillcapes you own?
            - Select an option
              - I would just like to change the Constitution skillcape.
                - **Surgeon General Tafani:** No problem, you will now use the older model for your Constitution skillcape.
                - I would like to change all my skillcapes.
                - **Surgeon General Tafani:** No problem, you will now use the older model for all of your skillcapes!
              - I've changed my mind!
                - (end)
          - No, thank you.
            - **Surgeon General Tafani:** Great! I'm glad you're enjoying our new version!
            - *(If the player is using the old skillcape models except for the Constitution cape:)*
              - **Surgeon General Tafani:** If you want, I can make it so you use the newer model for all of the skillcapes you own!
              - Select an option
                - Ok, I'd like to wear the newer version for all my skillcapes.
                  - **Surgeon General Tafani:** Great, you will now use the newer model for all of your skillcapes!
                - No, thanks.
                  - (end)
      - *(If the player has chosen the old skillcape models:)*
        - **Surgeon General Tafani:** It looks like you're currently using the old model for your Constitution skillcape. Would you like to change to the newer one?
        - Select an option
          - Yes, I would like to wear the new version of the skillcape.
            - **Surgeon General Tafani:** Would you like to wear the newer model for just this cape, or all of the skillcapes you own?
            - Select an option
              - I would just like to change the Constitution skillcape.
                - **Surgeon General Tafani:** No problem, you will now use the newer model for your Constitution skillcape.
              - I would like to change all my skillcapes.
                - **Surgeon General Tafani:** No problem, you will now use the newer model for all of your skillcapes!
              - I've changed my mind!
                - (end)
          - No, thank you.
            - **Surgeon General Tafani:** Great! I'm glad you're still enjoying the old version!
            - *(If the player is using the new skillcape models except for the Constitution cape:)*
              - **Surgeon General Tafani:** If you want, I can make it so you use the old model for all of the skillcapes you own!
              - Select an option
                - Ok, I'd like to wear the old version for all my skillcapes.
                  - **Surgeon General Tafani:** Great, you will now use the old model for all of your skillcapes!
                - No, thanks.
                  - (end)
  - ((Only if returning from another question:))
    - Goodbye
      - (end)

#### During the "check in with the doc" task in Oasis Restoration event

- **Player:** Hi!
- **Surgeon General Tafani:** Hi. How can I help?
- **Player:** Are you all okay, after - you know - the Duel Arena collapsed?
- **Surgeon General Tafani:** Oh quite. We've all been through much worse.
- **Player:** Really? Like what?
- **Surgeon General Tafani:** Well...there was...the pineapple incident.
- **Player:** What happened there?
- **Surgeon General Tafani:** We do not talk about it. EVER! I still hear the screams when I dream.
- You have completed: 'Check in with the doc' and gained progress towards the Oasis Restoration event.
- **Surgeon General Tafani:** The horror! The sweet sticky horror!
- (above|options)

### Heal

- (above|heal)
