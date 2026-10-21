# Teplin Macagan

- **Original Wiki Page**: [Transcript:Teplin Macagan](https://runescape.wiki/w/Transcript%3ATeplin%20Macagan)
- **Letter**: `T`

---

## Dialogue Transcript


### Standard dialogue

- [Menu]: Select an Option
  - [Choice]: What brings you to Oo'glog?
    - **Teplin Macagan:** There is red sandstone in this area, of the finest quality in all the land and great for making potion flasks.
    - **Teplin Macagan:** At first, it didn't seem safe to venture into a town full of ogresses, but it seems Oo'glog has become a holiday resort. So my associate Rutmir and myself have come here to see what we can find.
    - **Player:** Would it be possible for me to make these potion flasks too?
    - **Teplin Macagan:** You need to talk to Rutmir. He's the better craftsdwarf. He's northeast of here. Maybe he will let you use his marvellous glassmaking machine.
  - [Choice]: Can you decant some potions for me?
    - (below|Decant option)
  - [Choice]: I've got to go.
    - **Teplin Macagan:** See you later then.

### Decant option

- ((The following is shown in an interface titled "Decanting Options":))
  - [Choice]: Decant flasks
    - (Condition: If the player has no viable flasks of potions to decant:)
      - **Teplin Macagan:** Sorry, you don't seem to have anything I can use. Make sure you have 2 flasks that aren't completely full!
    - (Condition: If the player has flasks to decant:)
      - **Teplin Macagan:** Let's see what you have. I will decant your potion flasks back into 6 dosed flasks. I can make use of the flasks, so I'll take those as payment.
      - {{qact|Teplin decants as many as he can to full 6-dose flasks}}
      - **Teplin Macagan:** Here you go. That's the best I can do! If the flasks don't look too different, I gave them a clean
  - [Choice]: Convert vials to flasks
    - (Condition: If the player has no empty flasks in backpack:)
      - **Teplin Macagan:** You'll need to supply the empty flasks yourself; they're not cheap. You can bring them to me noted or unnoted.
    - (Condition: If the player has empty flasks in backpack:)
      - **Teplin Macagan:** Let's see what you have. I will decant potion vials and all flasks up to 4 doses into 6 dose flasks. You'll need to supply the empty flasks yourself; they're not cheap.
      - (Condition: If the player has potions to decant into flasks:)
        - {{qact|Teplin decants as many potions as he can to full 6-dose flasks}}
        - **Teplin Macagan:** Here you go. That's the best I can do!
      - (Condition: If the player has no potions to decant:)
        - **Teplin Macagan:** Sorry you don't seem to have anything I can help you with! Make sure you have the correct potions and some free space in your inventory and I can try again.
  - [Choice]: Convert flasks to vials
    - (Condition: If the player has no viable flasks of potions to decant:)
      - **Teplin Macagan:** Sorry, you don't seem to have anything I can use. Make sure you have at least 1 flask!
    - (Condition: If the player has flasks of potions to decant to vials:)
      - **Teplin Macagan:** Certainly. I think I can make use of the flasks, so I'll give you the vials for free.
      - {{qact|Teplin decants as many potions as he can to noted vials}}
      - **Teplin Macagan:** There you go, that's the best I can do!
  - [Choice]: Cancel
    - ((The interface closes.))
