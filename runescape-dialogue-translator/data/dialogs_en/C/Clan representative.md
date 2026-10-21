# Clan representative

- **Original Wiki Page**: [Transcript:Clan representative](https://runescape.wiki/w/Transcript%3AClan%20representative)
- **Letter**: `C`

---

## Dialogue Transcript


### Talk to option

- [Menu]: Choose an option:
  - [Choice]: Who are you?
    - **Player:** Who are you?
    - **Clan representative:** I'm one of War's clan representatives. He requested assistance with some of his less battle-focused hobbies, so the horsemen sent me along to help.
    - **Player:** What can you do?
    - **Clan representative:** Well, I'm a deft hand with potions, so I can help you decant any potions or flasks you have.
    - **Clan representative:** War's also given me access to his supply of Challenge Gems. I can sell you some, if you're interested.
    - **Clan representative:** Was there anything else?
    - (initial)
  - [Choice]: Can you decant some potions or jellyfish for me?
    - (below|Decant option)
  - [Choice]: Can you sell me some Challenge Gems?
    - **Player:** Can you sell me some Challenge Gems?
    - **Clan representative:** Of course! How many do you want?
    - (continue|Challenge gems option)
  - [Choice]: Goodbye.
    - **Player:** Goodbye!
    - **Clan representative:** Fight on!

### Decant option

- [Menu]: Select an Option
  - [Choice]: Decant vials
    - [Menu]: How many doses do you want to decant into?
      - [Choice]: One dose
        - (Condition: If the player has no viable vials of potions to decant:)
          - **Clan representative:** Sorry, I don't know how to decant anything that you're carrying.
        - (Condition: If the player has no backpack space:)
          - [Searching...]
          - **Clan representative:** Your inventory's a bit too full for me to do anything for you.
        - (Condition: If the player has viable vials of potions to decant:)
          - [Searching...]
          - (Condition: If additional vials were purchased from the clan representative:)
            - (receives=vials) (removes=two coins for each vial)
            - (continue)
          - **Clan representative:** There you go, chum.
      - [Choice]: Two doses
        - (above|decant-vials)
      - [Choice]: Three doses
        - (above|decant-vials)
      - [Choice]: Four doses
        - (above|decant-vials)
  - [Choice]: Decant flasks
      - **Clan representative:** Let's see what you have. I will decant your potion flasks back into 6 dosed flasks. I can make use of the flasks, so I'll take those as payment.
      - {{Qact|The clan representative decants as many as he can to full 6-dose flasks}}
      - **Clan representative:** Here you go. That's the best I can do! If the flasks don't look too different, I gave them a clean{{Sic}}
    - (Condition: If the player has no viable flasks of potions to decant:)
      - **Clan representative:** Sorry, you don't seem to have anything I can use. Make sure you have 2 flasks that aren't completely full!
  - [Choice]: Convert vials to flasks
    - (Condition: If the player has empty flasks in backpack:)
      - **Clan representative:**  see what you have. I will decant potion vials and all flasks with up to 4 doses into 6 dose flasks. You'll need to supply the empty flasks yourself; they're not cheap.
      - {{Qact|The clan representative decants as many potions as he can to full 6-dose flasks}}
      - **Clan representative:** Here you go. That's the best I can do!
    - (Condition: If the player has no empty flasks in backpack:)
      - **Clan representative:** You'll need to supply the empty flasks yourself; they're not cheap. You can bring them to me noted or unnoted.
  - [Choice]: Convert flasks to vials
    - (Condition: If the player has flasks of potions to decant to vials:)
      - **Clan representative:** Certainly. I think I can make use of the flasks, so I'll give you the vials for free.
      - {{Qact|The clan representative decants as many potions as he can to noted vials}}
      - **Clan representative:** There you go, that's the best I can do!
    - (Condition: If the player has no viable flasks of potions to decant:)
      - **Clan representative:** Sorry, you don't seem to have anything I can use. Make sure you have at least 1 flask!
  - [Choice]: Combine jellyfish
    - (Condition: If the player has viable jellyfish to combine:)
      - {{Qact|Jellyfish are combined where possible}}
      - **Clan representative:** There you go.
    - (Condition: If the player has no viable jellyfish to combine:)
      - **Clan representative:** Sorry, I don't know how to combine anything that you're carrying.
  - [Choice]: Cancel
    - (end)

### Challenge gems option

- [Menu]: How many would you like to buy?
  - [Choice]: One.
    - ((Purchase interface opens up for Challenge Gem (x1) for 10 RuneCoins))
  - [Choice]: Three.
    - ((Purchase interface opens up for Challenge Gem (x3) for 25 RuneCoins))
  - [Choice]: Six.
    - ((Purchase interface opens up for Challenge Gem (x6) for 40 RuneCoins))
  - [Choice]: None, I changed my mind.
    - **Player:** None, I have changed my mind.
    - **Clan representative:** Never fear, you know where to find them now. Anything else?
    - (initial)
