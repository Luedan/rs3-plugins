# Tindel Marchant

- **Original Wiki Page**: [Transcript:Tindel Marchant](https://runescape.wiki/w/Transcript%3ATindel%20Marchant)
- **Letter**: `T`

---

## Dialogue Transcript


### Standard dialogue


#### Talking to him

- **Tindel Marchant:{{anchor|start}}** Hello there! Welcome to my special antiques boutique.
- [Menu]: Select an option
  - [Choice]: What do you do here?
    - **Player:** What do you do here?
    - **Tindel Marchant:** I'm a specialist at identifying exotic and antique weapons, specifically swords, but I plan to branch out. If you have any old and rusty weapons that you want me to check out, just show them to me, pay me 100 Gold and I'll see if you have an antique on your hands. I can also repair some antique weapons and armours, just show me the item and I'll let you know if I can repair it and for how much.
    - (Condition: If the 'They're Long and Pointy' achievement hasn't been completed:)
      - {{RSFontAchievement|They're Long and Pointy}}
      - (continue)
    - (initial|init)
  - [Choice]: What's involved?
    - **Player:** What's involved?
    - **Tindel Marchant:** Well, pay me 100 Gold and I'll see if any rusty swords that you've found are actually worth anything. Some of them might be worth some money! If it's an antique item though, I reserve the right to purchase it immediately for adding to my own personal collection. I'll give you fair price for it.
    - (initial|init)
  - [Choice]: What do I get from this?
    - **Player:** What do I get from this?
    - **Tindel Marchant:** If I can reclaim the sword with my own specialist skills, I'll return it to you in peak condition. If it's an antique, I'll just give you what I think it's worth and I generally pay quite well. However, if it's just a piece of junk, I'll simply give you the bad news and get rid of the item for you.
    - (initial|init)
  - [Choice]: Ok, I'll give it a go!
    - **Player:** Ok, I'll give it a go!
    - (Condition: If the player has no rusty swords in the inventory:) {{anchor|identify}}
      - **Tindel Marchant:** Sorry my friend, but you don't seem to have any swords that need to be identified.
    - (Condition: If the player has a rusty sword in the inventory:)
      - (removes=100 coins)
      - [You hand Tindel 100 coins plus the rusty sword.]
      - (removes=rusty sword) (receives=a sword of a random metal)
      - **Tindel Marchant:** There you go my friend, it turned out to be a <sword name>.
      - [Tindel gives you a <sword name>.]
  - [Choice]: Ok, thanks.
    - **Player:** Ok, thanks.

#### Give-Sword option

- (above2|identify)

#### Repair-all option

- **Tindel Marchant:** Repairing or recharging degradable items costs money. If you want me to repair all of your items, I will take the correct fee from your inventory or money pouch.
- [Menu]: Repair or recharge all your items?
  - [Choice]: Yes {{anchor|repair}}
    - (Condition: If the player has no items that can be repaired:)
      - **Tindel Marchant:** You do not have any items that can be repaired or recharged.
    - (Condition: If the player has items that can be repaired:)
      - **Tindel Marchant:** All done! That cost you <amount> coins.
      - All your items have been fixed for <amount> coins.
  - [Choice]: No
    - (end)
  - [Choice]: Yes, and don't ask again.
    - (above|repair)

### Ring-bell option of the Antiques Shop Stall

- [You ring for attention.]
- (continuea|start)
