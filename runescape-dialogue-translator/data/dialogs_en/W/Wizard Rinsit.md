# Wizard Rinsit

- **Original Wiki Page**: [Transcript:Wizard Rinsit](https://runescape.wiki/w/Transcript%3AWizard%20Rinsit)
- **Letter**: `W`

---

## Dialogue Transcript


### When talked to

- **Wizard Rinsit:** Hey there, what can I do for you?
- [Menu]: Choose an option:|anchor=Rinsit-options
  - [Choice]: What do you do in the Wizards' Tower?
    - **Wizard Rinsit:** I'm an apprentice at the Wizards' Tower. I'm here to share knowledge of the Runespan and help others within their travels.
    - (previous|Rinsit-options)
  - [Choice]: What do you sell?
    - **Wizard Rinsit:** You can buy various things from me that should aid you within the Runespan.
    - **Wizard Rinsit:** I have runesphere and yellow wizard teleports which will allow you to get around easier.
    - **Wizard Rinsit:** I can also provide you with the master runecrafters outfit should you be ready for it.
    - **Wizard Rinsit:** Lastly, I have a range of altar teleportation tablets that can be used to take you directly to the centre of the mysterious ruins containing rune altars!
    - (previous|Rinsit-options)
  - [Choice]: Can I see your shop?
    - (opens=Wizard Rinsit's Runecrafting Shop)
  - [Choice]: Do you know if I could make a bigger essence pouch?
    - **Player:** Do you know if I could make a bigger essence pouch?
    - **Wizard Rinsit:** In theory, yes!
    - (Condition: Without Runecrafting level 105:)
      - **Wizard Rinsit:** However, I don't think it's something someone of your skill would be capable of.
      - Creation of an expansive pouch requires Runecrafting level 105.
    - [Menu]: Choose an option:|anchor=Rinsit-pouch
      - [Choice]: Where could I make it?
        - **Player:** Where could I make it?
        - **Wizard Rinsit:** At an altar, of course! Only something like that should have the binding energy to create such an item.
        - (previous|Rinsit-pouch)
      - [Choice]: What would I need to make it?
        - **Player:** What would I need to make it?
        - **Wizard Rinsit:** Powerful materials, that's for sure.
        - **Wizard Rinsit:** You could possibly repurpose a Wicked hood as the basis of the pouch - I happen to have a Hungry hood I could sell you for that purpose.
        - **Wizard Rinsit:** Of course, you'd probably also need the power of other essence pouches, too.
        - **Wizard Rinsit:** Something that taps into dimensional energy like that would definitely need a protective sleeve of some kind, perhaps made from some strong types of leather...
        - **Wizard Rinsit:** Oh! You'll need a way to bind it shut, too. I've heard talk of a magic thread that was spotted when crafting runes after entering the altar ruins directly, which could work.
        - (previous|Rinsit-pouch)
      - [Choice]: I lost some of the parts.|cond=If any parts are missing or destroyed
        - (Condition: Without enough free backpack space for all the missing items:)
          - **Wizard Rinsit:** I found some things you may have misplaced, but you don't seem to have room in your backpack to take them.
        - (Condition: With enough free backpack space for all the missing items:)
          - (receives=missing items)
          - **Wizard Rinsit:** I've put some things you may have misplaced into your backpack for you.
          - (previous|Rinsit-pouch)
      - [Choice]: Nevermind.
        - (previous2|Rinsit-options)
  - [Choice]: Goodbye.
    - (end)

### When directing portal


#### If the portal redirection hasn't been purchased

- **Wizard Rinsit:** I can direct that portal over there to take you directly to the top floor of the Runespan, however it's not an easy task, it's going to cost you.
- You must purchase the 'Portal redirection' reward from Wizard Rinsit's store before he can do this.

#### If the portal redirection has been purchased

- **Wizard Rinsit:** I can direct that portal over there to take you directly to the top floor of the Runespan if you're an experienced runecrafter.
- [Menu]: Where would you like the portal to be directed to?
  - [Choice]: Mid-level Runespan.
    - (Condition: If the portal is already directed there:)
      - **Wizard Rinsit:** It looks like the portal is already directed to that destination.
    - (Condition: If the portal is directed to high-level Runespan:)
      - **Wizard Rinsit:** There, all redirected for you!
  - [Choice]: High-level Runespan
    - (Condition: If the portal is already directed there:)
      - **Wizard Rinsit:** It looks like the portal is already directed to that destination.
    - (Condition: If the portal is directed to mid-level Runespan:)
      - **Wizard Rinsit:** There, all redirected for you!

### When using the [[rusty chest]] on him


#### Before 13 August 2018


##### First time

- **Player:** I was wondering if you could take a look at this chest for me?
- **Wizard Rinsit:** What do we have here then? Hmm... Interesting, this chest appears to be sealed by a magical lock...
- **Player:** That's actually the reason I've brought this to you. I followed a treasure map and it led me to this chest, however I've had no luck opening it.
- **Wizard Rinsit:** Not to worry Player, I can remove that lock for you! Unfortunately this isn't going to be as easy as I thought. I'm going to need some time to research this, please come back later.

##### If the chest has already been used on him

- **Wizard Rinsit:** I'm still researching for more information, please come back later.

#### After 13 August 2018


##### With the locked chest

*If you have talked to him before*
- **Wizard Rinsit:** I've spent a very long time researching this kind of lock now - hand it over and I'll remove it for you.
- {{qact| Wizard Rinsit removes the lock from the Rusty Chest}}
- **Wizard Rinsit:** There you are Player! It's always nice to see hard work paying off.
*If talking to him for the first time*
- **Player:** I was wondering if you could take a look at this chest for me?
- **Wizard Rinsit:** What do we have here then? Ah yes, I spent a very long time researching this kind of lock.
- **Player:** That's actually the reason I've brought this to you. I followed a treasure map and it led me to this chest, however I've had no luck opening it.
- **Wizard Rinsit:** Not to worry Player, I can remove that lock for you!
- {{qact| Wizard Rinsit removes the lock from the Rusty Chest}}
- **Wizard Rinsit:** There you are Player! It's always nice to see hard work paying off.

##### With the opened chest

- **Wizard Rinsit:** I'm not sure what you want me to do with that, I've already removed the lock for you!
- **Wizard Rinsit:** Come and see me again if you run into any other issues.

### When using the [[ancient scroll]] on him

- **Wizard Rinsit:** Unfortunately, this isn't my area of expertise so I can't help you here.
