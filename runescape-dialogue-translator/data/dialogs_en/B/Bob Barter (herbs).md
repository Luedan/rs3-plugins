# Bob Barter (herbs)

- **Original Wiki Page**: [Transcript:Bob Barter (herbs)](https://runescape.wiki/w/Transcript%3ABob%20Barter%20%28herbs%29)
- **Letter**: `B`

---

## Dialogue Transcript


### Before doing the Grand Exchange tutorial

- **Player:{{anchor|hello}}** Hello.
- **Bob Barter (herbs):** Mate, I haven't got time for you yet. I suggest you speak with Brugsen Bursen or the Grand Exchange Tutor near the entrance for a lesson. Brugsen will give an interesting lesson on the Grand Exchange and the Tutor will give a simpler, plain lesson.

#### Info-herb option

- **Bob Barter (herbs):** You'll need a tiny bit of training first, chum. I suggest you speak with Brugsen Bursen or the Grand Exchange Tutor near the entrance for a lesson. Brugsen will give an interesting lesson on the Grand Exchange and the Tutor will give a smaller, plain lesson.

#### Decant option

- (above2|hello)

### After doing the Grand Exchange tutorial

- **Player:** Hi.
- **Bob Barter (herbs):** Hello, chum, fancy buyin' some designer jewellery? They've come all the way from Ardougne! Most pukka!
- **Player:** erm, no. I'm all set, thanks.
- **Bob Barter (herbs):** Okay, chum, so what can I do for you? I can tell you the very latest herb prices, or perhaps I could help you decant your potions.
- [Menu]: Select an Option
  - [Choice]: Who are you?
    - **Player:** Who are you?
    - **Bob Barter (herbs):** Why, I'm Bob! Your friendly seller of smashin' goods!
    - **Player:** So what do you have to sell?
    - **Bob Barter (herbs):** Oh, not much at the moment. Cuz, ya know. Business being so well and cushie.
    - **Player:** You don't really look like you're being so successful.
    - **Bob Barter (herbs):** You plonka! It's all a show, innit! If I let people knows I'm in good business they'll want a share of the moolah!
    - **Player:** You conveniently have a response for everything.
    - **Bob Barter (herbs):** That's the Ardougne way, my son.
    - (initial)
  - [Choice]: Can you...
    - [Menu]: Select an Option
      - [Choice]: Can you decant some potions for me?
        - (below2|Decant option 2)
      - [Choice]: Help me out with the prices for herbs?
        - ((Guide Prices: Herbs opens up.))
      - [Choice]: Tell me the cost to decant potions?
        - **Bob Barter (herbs):** If you want potions decanted into 4, 3, 2 or 1 dose versions, I charge 2 coins for each normal vial, 2 coins for each juju vial and 2 coins for each powerburst vial.
      - [Choice]: Tell me what I can do with empty vials?
        - **Player:** Can you tell me what I can do with empty vials?
        - **Bob Barter (herbs):** Why certainly! When you finish your last dose you can either keep the vial or simply throw it out!
        - [Menu]: When finishing the last dose, what would you like to do?
          - [Choice]: Keep the vial.
            - color=white
          - [Choice]: Throw the vial away.
            - color=white
      - [Choice]: Sorry, I've got to split.
        - (below|split)
  - [Choice]: Sorry, I've got to split.
    - **Player:** Sorry, I've got to split.
    - **Bob Barter (herbs):** Buying bananas, then?
    - **Player:** What?
    - **Bob Barter (herbs):** You know, split? Banana? Banana split?
    - **Player:** Hahaha. No wait. That's not funny.

#### Info-herbs option

- ((Guide Prices: Herbs opens up.))

#### Decant option

- ((The following is shown in an interface titled "Decanting Options":))
  - [Choice]: Decant vials
    - [Menu]: How many doses do you want to decant into?
      - [Choice]: One dose
        - (Condition: With decantable potions in backpack:)
          - **Bob Barter (herbs):** There you go, chum.
        - (Condition: Without decantable potions in backpack:)
          - **Bob Barter (herbs):** Sorry, I can't do anything with [that potion/those potions].
        - (Condition: Without enough money for extra vials:)
          - **Bob Barter (herbs):** Sorry, you don't have enough money to pay for enough empty vials.
        - (Condition: Without space in backpack for extra vials:)
          - **Bob Barter (herbs):** Your inventory's a bit too full for me to do anything for you.
      - [Choice]: Two doses
        - (above)
      - [Choice]: Three doses
        - (above)
      - [Choice]: Four doses
        - (above)
  - [Choice]: Decant flasks
    - (Condition: With no viable flasks of potions to decant:)
      - **Bob Barter (herbs):** Sorry, you don't seem to have anything I can use. Make sure you have 2 flasks that aren't completely full!
    - (Condition: With flasks to decant:)
      - **Bob Barter (herbs):** Let's see what you have. I will decant your potion flasks back into 6 dosed flasks. I can make use of the flasks, so I'll take those as payment.
      - {{qact|Bob decants as many as he can to full 6-dose flasks}}
      - **Bob Barter (herbs):** Here you go. That's the best I can do! If the flasks don't look too different, I gave them a clean
  - [Choice]: Convert vials to flasks
    - (Condition: With no empty flasks in backpack:)
      - **Bob Barter (herbs):** You'll need to supply the empty flasks yourself; they're not cheap. You can bring them to me noted or unnoted.
    - (Condition: With empty flasks in backpack:)
      - **Bob Barter (herbs):** Let's see what you have. I will decant potion vials and all flasks up to 4 doses into 6 dose flasks. You'll need to supply the empty flasks yourself; they're not cheap.
      - (Condition: With potions to decant into flasks:)
        - {{qact|Bob decants as many potions as he can to full 6-dose flasks}}
        - **Bob Barter (herbs):** Here you go. That's the best I can do!
      - (Condition: With no potions to decant:)
        - **Bob Barter (herbs):** Sorry you don't seem to have anything I can help you with! Make sure you have the correct potions and some free space in your inventory and I can try again.
  - [Choice]: Convert flasks to vials
    - (Condition: With no viable flasks of potions to decant:)
      - **Bob Barter (herbs):** Sorry, you don't seem to have anything I can use. Make sure you have at least 1 flask!
    - (Condition: With flasks of potions to decant to vials:)
      - **Bob Barter (herbs):** Certainly. I think I can make use of the flasks, so I'll give you the vials for free.
      - {{qact|Bob decants as many potions as he can to noted vials}}
      - **Bob Barter (herbs):** There you go, that's the best I can do!
  - [Choice]: Cancel
    - ((The interface closes.))

### Overhead dialogue

- {{Trandom}}
- **Bob Barter (herbs):** {{RSChat|Now, what should I buy?}}
- **Bob Barter (herbs):** {{RSChat|I'm in the money!}}
- **Bob Barter (herbs):** {{RSChat|I could have sworn that would have worked.}}
- **Bob Barter (herbs):** {{RSChat|Hope this item sells well.}}
- **Bob Barter (herbs):** {{RSChat|Please, please, please work.}}
