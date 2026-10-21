# Feng, the Bounty Master

- **Original Wiki Page**: [Transcript:Feng, the Bounty Master](https://runescape.wiki/w/Transcript%3AFeng%2C%20the%20Bounty%20Master)
- **Letter**: `F`

---

## Dialogue Transcript


### Talking to Feng, the Bounty Master

- **Feng, the Bounty Master:**  Welcome, fellow mercenary, welcome.
- **CHOOSE AN OPTION:**
  - Can you assign me a bounty?
    - ((If you do not currently have a bounty and have bounties left:))
      - **Feng, the Bounty Master:**  Which faction do you fight for today, my friend?
      - **SELECT A FACTION TO EARN REPUTATION WITH.**
        - Sliske.
          - **Feng, the Bounty Master:**  Very well. Your bounty is to slay those loyal to [Faction] in the name of Sliske!
          - (previous2)
        - Zamorak.
          - **Feng, the Bounty Master:**  Very well. Your bounty is to slay those loyal to [Faction] in the name of Zamorak!
          - (previous2)
        - Seren.
          - **Feng, the Bounty Master:**  Very well. Your bounty is to slay those loyal to [Faction] in the name of Seren!
          - (previous2)
        - Zaros.
          - **Feng, the Bounty Master:**  Very well. Your bounty is to slay those loyal to [Faction] in the name of Zaros!
          - (previous2)
    - ((If you do not currently have a bounty and don't have bounties left:))
      - **Feng, the Bounty Master:**  So bloodthirsty! You have had your quota of bounties, my friend. Come back another day.
      - (previous)
    - ((If you currently have a bounty:))
      - ((If you are earning reputation with Sliske:))
        - **Feng, the Bounty Master:**  You already have a bounty to slay those loyal to [Faction] in the name of Sliske!
        - (previous)
      - ((If you are earning reputation with Zamorak:))
        - **Feng, the Bounty Master:**  You already have a bounty to slay those loyal to [Faction] in the name of Zamorak!
        - (previous)
      - ((If you are earning reputation with Seren:))
        - **Feng, the Bounty Master:**  You already have a bounty to slay those loyal to [Faction] in the name of Seren!
        - (previous)
      - ((If you are earning reputation with Zaros:))
        - **Feng, the Bounty Master:**  You already have a bounty to slay those loyal to [Faction] in the name of Zaros!
        - (previous)
  - How many bounties do I have available?
    - ((With bounties left:))
      - ((If you do not currently have a bounty:))
        - **Feng, the Bounty Master:**  I can assign you [number] [bounty/bounties] before you reach your quota. You can have one now, if you like?
          - Yes, I'd like a bounty.
            - (above|get-bounty)
          - No, not right now.
            - (previous)
      - ((If you currently have a bounty:))
        - **Feng, the Bounty Master:**  I can assign you [number] [bounty/bounties] before you reach your quota.
        - (previous)
    - ((Without bounties left:))
      - **Feng, the Bounty Master:**  So bloodthirsty! You have had your quota of bounties, my friend. Come back another day.
      - (previous)
  - ((If you currently have a bounty:))
    - I'd like to abandon my current bounty.
      - **Feng, the Bounty Master:**  Hmm, abandon your bounty? I must warn you, it will still count towards your quota. Are you sure?
      - **ABANDON YOUR CURRENT BOUNTY?**
        - Yes, abandon my bounty.
          - (The bounty is removed.)
          - (previous2)
        - No, keep my bounty.
          - (previous2)
  - Can you tell me more about your bounties?
    - **Feng, the Bounty Master:**  I assign bounties to fellow mercenaries like yourself. This is a war, you see, and there's killin' to be done. The deals I cut with the faction representatives here mean you can pick one to do your bounties for, earning reputation with them in return.
    - **Player:** What does a bounty entail?
    - **Feng, the Bounty Master:**  Well, killin' of course. One hundred kills of the faction I assign you, to be precise, but if you kill their general it counts as twenty-five! You pick the faction you fight for, I pick the faction you fight against, then away you go. Happy hunting.
    - **Player:** So why are you even here in the first place?
    - **Feng, the Bounty Master:**  I'm a mercenary, much like anyone else in this war-torn place. 'Course I have my own nefarious agenda, but that's for me to know.
    - (previous)
  - Goodbye.
    - **Feng, the Bounty Master:** Happy hunting.

### Get bounty

- (above|get-bounty)

### Hand in bounty


#### Without a bounty

- **Feng, the Bounty Master:** You can't hand in a bounty, I haven't assigned you one...
- (above|options)

#### With an incomplete bounty

- **Feng, the Bounty Master:** You haven't completed your bounty yet. Go and slay some more.
- (above|options)

#### With a complete bounty

- **Feng, the Bounty Master:** Ah yes, I see you've completed your bounty. Good hunting, here's your reward.
- ((If a Serenist bounty was handed in:))
  - You have gained 150 reputation with the Serenist forces!
  - (above|bounties-available)
- ((If a Sliskean bounty was handed in:))
  - You have gained 150 reputation with the Sliskean forces!
  - (above|bounties-available)
- ((If a Zamorakian bounty was handed in:))
  - You have gained 150 reputation with the Zamorakian forces!
  - (above|bounties-available)
- ((If a Zarosian bounty was handed in:))
  - You have gained 150 reputation with the Zarosian forces!
  - ((If ilujankan components were unlocked:))
    - You can now discover the blueprint for Ilujankan components if you have at least 89 Invention.
    - (continue)
  - (above|bounties-available)

### Using the broken disguise kit

- **Feng, the Bounty Master:**  Interestin' find. You've brought it to the right place.
- **Select an Option**
  - Of course I did.
    - **Player:** It was a matter of time. There's only five people up here.
  - I did?
    - (continue)
- **Player:** What could you possibly want it for?
- **Feng, the Bounty Master:** I've heard of a [gal/guy] that collects weird trinkets. Might be able to extract a fair price.
- **Feng, the Bounty Master:** Maybe you yourself would be interested in a reasonable trade? I've acquired an enchanted signal horn that I'd be willing to let go.
- **Exchange your chest of junk for a signal horn?**
  - Yes
    - (removes=the broken disguise kit) (receives=a signal horn)
    - [Feng gives you a horn in exchange for the chest. Whoever he's talking about must like some weird stuff.]
  - No
    - (end)
