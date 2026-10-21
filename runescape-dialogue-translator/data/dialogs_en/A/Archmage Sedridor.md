# Archmage Sedridor

- **Original Wiki Page**: [Transcript:Archmage Sedridor](https://runescape.wiki/w/Transcript%3AArchmage%20Sedridor)
- **Letter**: `A`

---

## Dialogue Transcript


### In the Wizards' Tower


#### Talk to


##### Normally

- (Condition: Without level 99 Magic and level 99 Runecrafting:)
  - **Archmage Sedridor:** Welcome, adventurer, to the world-renowned Wizards' Tower. How can I help you?
  - (continue)
- (Condition: With level 99 Magic and level 99 Runecrafting:)
  - **Archmage Sedridor:** Welcome to the tower, archmage. How can I help you?
  - (continue)
- {{anchor|init-tower}}[Menu]: Choose an option:
  - [Choice]: cond=With level 99 Magic and level 99 Runecrafting:|Did you just call me 'archmage'?
    - **Archmage Sedridor:** Indeed I did. The title is normally reserved for the head of the Wizards' Tower, but in light of your mastery of both Magic and Runecrafting I believe you have earned the right to use it.
    - (The 'Archmage' title is unlocked the first time this dialogue option is used.)
    - [Menu]: Select an Option
      - [Choice]: (Set your title to 'Archmage'.)
        - You are now known to others as Archmage Player.
        - **Archmage Sedridor:** Is there anything else I can do for you, Archmage?
        - (other|init-tower)
      - [Choice]: (Don't change your title.)
        - (other|init-tower)
  - [Choice]: cond=After Love Story:|Your wizards did well against the Wise Old Man.
    - **Archmage Sedridor:** Thank you. I must admit, we'd have lost if Traiborn hadn't helped. I've no idea what he summoned, but it certainly terrified the Wise Old Man and that woman.
  - [Choice]: Can you teleport me to the rune essence?
    - **Archmage Sedridor:** {{RSChat|Seventior disthine molenko!}}
    - {{Qact|Archmage Sedridor teleports the player to the Rune Essence mine.}}
  - [Choice]: Tell me about the Wizards' Tower.
    - **Archmage Sedridor:** The tower is the finest institute of magical learning in Misthalin, Asgarnia or Kandarin. The standard adventurer's spellbook and the teleportation lodestones are both products of tower wizards' research.
    - **Archmage Sedridor:** Most importantly, the tower guards the secret of rune essence, which allowed human civilisation to prevail over the monsters and barbarians and ushered in the Fifth Age of the world.
    - [Menu]: Select an Option
      - [Choice]: Can you teach me magic?
        - **Archmage Sedridor:** You already know the adventurer's spellbook! For an adventurer like you, the best way to learn is to go out and practice casting spells.
        - (other|about-wizards-tower-options)
      - [Choice]: What are the ruins I saw outside the tower?
        - **Archmage Sedridor:** Ah...they are the relic of a sad chapter in the tower's history.
        - **Archmage Sedridor:** Originally, the wizards of the tower were not as unified as they now are. There were orders devoted to different gods: notably Saradomin, god of goodness and order, and Zamorak, god of evil and chaos.
        - **Archmage Sedridor:** The orders worked together for seventy years, but eventually the Zamorakian wizards betrayed the others and burned the tower down.
        - **Archmage Sedridor:** Archmage Perien rebuilt the tower and forbade Zamorakian wizards from joining. The rebuilt Tower has been united and at peace for a hundred years.
        - (other|about-wizards-tower-options)
      - [Choice]: The secret of rune essence?
        - **Archmage Sedridor:** Yes - specifically, the secret of the teleportation spell that lets us reach it.
        - **Archmage Sedridor:** The discovery of the rune essence and the ability to make rune stones was the single greatest magical discovery in the history of Gielinor. It allows anyone to produce magical effects easily and reliably.
        - **Archmage Sedridor:** The rune essence lies in the frozen north, where the Eye of Saradomin once rested. The first wizards reached it by an arduous land route, but eventually they discovered a spell to teleport there directly.
        - **Archmage Sedridor:** After Zamorakian mages burned the tower down a hundred years ago, Archmage Perien decided to keep the spell secret rather than let it fall into evil hands.
        - **Archmage Sedridor:** We will cast the spell for anyone we think trustworthy, but the spell itself is an inner mystery of the tower and is taught only to select individuals.
        - (other|about-wizards-tower-options)
      - [Choice]: Other questions...
        - (initial|init-tower)
      - [Choice]: Goodbye.
        - (end)
  - [Choice]: Nothing, thanks. I'm just looking around.
    - (end)

##### During the 25th Anniversary celebrations task

- **Player:** Hello, Archmage Sedridor. Might I ask a question about the Lodestone Network?
- **Archmage Sedridor:** Why, of course. How may I be of assistance?
- **Player:** Do you think lodestones have improved everyone's lives or taken away a little bit of its magic?
- **Archmage Sedridor:** Hmm, a peculiar question. They are the height of convenience! They have done wonders for world trade. No doubt, they have spared many ex-walkers untold amounts of foot injury.
- **Archmage Sedridor:** Ah, but true...when does one take the time to casually stroll these days, to take in the sights and the sounds? What wonders we miss when when convenience is at the fore...
- {{RSFontAchievement|A Lode of Fun|Talk to Archmage Sedridor about the Lodestone Network.}}
- ((Shown in a task completion pop-up:))
  - {{Colour|#F0BE79|&nbsp;25TH ANNIVERSARY TASK&nbsp;|#181513}}
  - A Lode of Fun
  - Talk to Archmage Sedridor about the Lodestone Network.
  - (continue)
- **Archmage Sedridor:** Indeed, life should be somewhat 'bumpy', for you cannot have the highs without the lows. Thank you for reminding me of such. You know what, I think I'LL go out for a walk soon.
- (Condition: If all the tasks have been completed:)
  - **Player:** Looks like I've completed everything. I'd better go and see Hans about that reward!

#### Using the deposit box with rune or pure essence in backpack

- **Archmage Sedridor:** Sorry, but usage of this chest is prohibited while carrying essence.
- Sedridor does not want you banking rune essence in the tower.

### At summer events

- **Archmage Sedridor:** Foreman George continues to impress me with his sandcastle designs; I find it hard to believe there's no magic involved. I'd love to see a magic-inspired sandcastle while I'm here.
- **Player:** You're not very subtle about what you want are you?
