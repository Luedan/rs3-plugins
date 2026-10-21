# Rhobert Dail (herbs)

- **Original Wiki Page**: [Transcript:Rhobert Dail (herbs)](https://runescape.wiki/w/Transcript%3ARhobert%20Dail%20%28herbs%29)
- **Letter**: `R`

---

## Dialogue Transcript


### In Prifddinas


#### Talking to him

- **Rhobert Dail (herbs):** The Tower of Voices is a wonderful place to do business, enrapt with the Voice of Seren as we are.
- **Rhobert Dail (herbs):** My specialty is anything related to herbs and potions. Can I help you with anything?
- [Menu]: Select an Option
  - [Choice]: Can you decant some potions for me?
    - (below|Decant option)
  - [Choice]: Can you help me out with the prices for herbs?
    - **Rhobert Dail (herbs):** I'd be happy to!
    - ((Guide Prices: Herbs opens up.))
  - [Choice]: How much do you charge for decanting potions?
    - **Rhobert Dail (herbs):** If you want potions decanted into 4, 3, 2 or 1 dose versions, I charge 2 coins for each normal vial, 2 coins for each juju vial and 15 coins for each powerburst vial.
  - [Choice]: Sorry, I've got to go.
    - **Rhobert Dail (herbs):** Okay, I'll be here if you ever need me, mesmerised by the lady's voice.

#### Decant option

- ((The following is shown in an interface titled "Decanting Options":))
  - [Choice]: Decant vials
    - [Menu]: How many doses do you want to decant into?
      - [Choice]: One dose
        - (Condition: With decantable potions in backpack:)
          - **Rhobert Dail (herbs):** There you go, chum.
        - (Condition: Without decantable potions in backpack:)
          - **Rhobert Dail (herbs):** Sorry, I don’t know how to decant anything that you’re carrying.
        - (Condition: Without enough money for extra vials:)
          - **Rhobert Dail (herbs):** Sorry, you don't have enough money to pay for enough empty vials.
        - (Condition: Without space in backpack for extra vials:)
          - **Rhobert Dail (herbs):** Your inventory's a bit too full for me to do anything for you.
      - [Choice]: Two doses
        - (above)
      - [Choice]: Three doses
        - (above)
      - [Choice]: Four doses
        - (above)
  - [Choice]: Decant flasks
    - (Condition: With no viable flasks of potions to decant:)
      - **Rhobert Dail (herbs):** Sorry, you don't seem to have anything I can use. Make sure you have 2 flasks that aren't completely full!
    - (Condition: With flasks to decant:)
      - **Rhobert Dail (herbs):** Let's see what you have. I will decant your potion flasks back into 6 dosed flasks. I can make use of the flasks, so I'll take those as payment.
      - {{qact|Rhobert decants as many as he can to full 6-dose flasks}}
      - **Rhobert Dail (herbs):** Here you go. That's the best I can do! If the flasks don't look too different, I gave them a clean
  - [Choice]: Convert vials to flasks
    - (Condition: With no empty flasks in backpack:)
      - **Rhobert Dail (herbs):** You'll need to supply the empty flasks yourself; they're not cheap. You can bring them to me noted or unnoted.
    - (Condition: With empty flasks in backpack:)
      - **Rhobert Dail (herbs):** Let's see what you have. I will decant potion vials and all flasks up to 4 doses into 6 dose flasks. You'll need to supply the empty flasks yourself; they're not cheap.
      - (Condition: With potions to decant into flasks:)
        - {{qact|Rhobert decants as many potions as he can to full 6-dose flasks}}
        - **Rhobert Dail (herbs):** Here you go. That's the best I can do!
      - (Condition: With no potions to decant:)
        - **Rhobert Dail (herbs):** Sorry you don't seem to have anything I can help you with! Make sure you have the correct potions and some free space in your inventory and I can try again.
  - [Choice]: Convert flasks to vials
    - (Condition: With no viable flasks of potions to decant:)
      - **Rhobert Dail (herbs):** Sorry, you don't seem to have anything I can use. Make sure you have at least 1 flask!
    - (Condition: With flasks of potions to decant to vials:)
      - **Rhobert Dail (herbs):** Certainly. I think I can make use of the flasks, so I'll give you the vials for free.
      - {{qact|Rhobert decants as many potions as he can to noted vials}}
      - **Rhobert Dail (herbs):** There you go, that's the best I can do!
  - [Choice]: Cancel
    - ((The interface closes.))
