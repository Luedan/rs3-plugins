# Wizard Rosalina

- **Original Wiki Page**: [Transcript:Wizard Rosalina](https://runescape.wiki/w/Transcript%3AWizard%20Rosalina)
- **Letter**: `W`

---

## Dialogue Transcript


### Talk to


#### First time

- **Wizard Rosalina:** I don't think I've seen your face before! I'm Wizard Rosalina.
- **Player:** Nice to meet you! I'm Player.
- (continue|Rosalina-options)

#### Afterwards


##### Normally

- **Wizard Rosalina:** Hi there, Player!
- [Menu]: Choose an option:|anchor=Rosalina-options
  - [Choice]: What do you have for sale?
    - **Player:** What do you have for sale?
    - **Wizard Rosalina:** Oh, all sorts of doodads related to my studies! Runes, gems, telescopes, Mining enhancements...
    - **Wizard Rosalina:** I should note that I only accept stardust as payment, though. I'm in need of it more than gold!
    - [Menu]: Open reward shop?
      - [Choice]: Yes
        - (opens=Shooting Star Reward Shop)
      - [Choice]: No
        - (previous|Rosalina-options)
  - [Choice]: What are you doing?
    - **Player:** What are you doing?
    - **Wizard Rosalina:** I'm studying the skies, building upon the knowledge of the great Scorpius who came before us!
    - **Player:** How exciting!
    - **Wizard Rosalina:** I'm glad you think so too! Astromancy has received a lot of criticism from other wizards in the past.
    - **Wizard Rosalina:** But since my fellow astromancer, Wizard Chambers, used it to save Gielinor from Tuska they've slowly been coming around to its legitimacy.
    - **Wizard Rosalina:** My particular specialism is in star sprites, though.
    - (Condition: Before talking to a star sprite:)
      - **Player:** What are star sprites?
      - (continue)
    - (Condition: After talking to a star sprite:)
      - **Player:** The odd-looking aliens that can be found in shooting stars? I've met one of those before!shooting star.
      - **Wizard Rosalina:** Yes! Charming, aren't they!
      - (continue)
    - **Wizard Rosalina:** Ever since I first laid eyes on one of the curious little fellows, I fell in love.
    - **Wizard Rosalina:** I couldn't find a single piece of research on them, so I knew I had to be the one to change that.
    - (previous|Rosalina-options)
  - [Choice]: Talk about shooting stars.
    - [Menu]: Select an Option|anchor=Shooting-stars-options
      - [Choice]: What are shooting stars?
        - **Player:** What are shooting stars?
        - **Wizard Rosalina:** Shooting stars are large chunks of rock that occasionally fall down to Gielinor from the skies above.
        - **Player:** Well, if I didn't already have a fear of being knocked out from a space rock appearing out of nowhere, now I do.
        - **Wizard Rosalina:** Statistically, you have nothing to worry about!
        - **Player:** ...
        - **Wizard Rosalina:** Assuming you stumble across a crash star and have managed to avoid getting knocked out cold, you can mine through it to free its inhabitant at its core.
        - **Player:** I see, thanks!
        - (previous|Shooting-stars-options)
      - [Choice]: How can I find shooting stars?
        - **Player:** How can I find shooting stars?
        - **Wizard Rosalina:** You can scour the skies for nearby shooting stars using a telescope.
        - **Wizard Rosalina:** Telescopes can be built in your player-owned house, but you can also find some public telescopes in Varrock Palace library, and the observatory.
        - **Player:** What about your telescope over there?
        - **Wizard Rosalina:** Oh, I wish that beauty was mine! Alas, it belongs to Wizard Rosalina.
        - **Wizard Rosalina:** He gave me permission to use it, though, so I suppose I can pass that permission on down to you.
        - **Wizard Rosalina:** I should also mention that not all telescopes are built equally. You might find that some, due to having been constructed with lower-tiered woods, are a bit less accurate than others.
        - **Player:** What does their accuracy affect?
        - **Wizard Rosalina:** Well, the more accurate a telescope is, the shorter the timeframe it'll give for when the next shooting star will land. It will also give you a more accurate estimate of the star's size.
        - **Player:** That's good to know.
        - (previous|Shooting-stars-options)
      - [Choice]: What can I get from shooting stars?
        - **Player:** What can I get from shooting stars?
        - **Wizard Rosalina:** Crashed stars are jam-packed with stardust, I use stardust in my studies, so feel free to bring some to me and I can trade you for some things you might find useful.
        - **Wizard Rosalina:** If you mine the star all the way to the core, I've also heard that the star sprite inside may aid you with some sort of temporary Mining enhancement!
        - **Player:** Intriguing!
        - (previous|Shooting-stars-options)
      - [Choice]: [Previous options]
        - (previous2|Rosalina-options)
  - [Choice]: cond=Having lost a portable telescope:|I'd like to reclaim my portable telescope.
    - (Condition: Without free backpack space:)
      - **Wizard Rosalina:** You'll have to come back when you have a free space in your backpack.
    - (Condition: With free backpack space:)
      - **Player:** I've lost my portable telescope.
      - **Wizard Rosalina:** Not to worry, I keep plenty of spares!
      - (receives=portable telescope)
      - [Wizard Rosalina hands you a shiny new portable telescope.]
      - (previous|Shooting-stars-options)
  - [Choice]: Do you know anything about starblooms?
    - **Player:** Do you know anything about starblooms?
    - **Wizard Rosalina:** Ooh, starbloom flowers! I've never seen one myself, but I once interviewed a star sprite who cultivated fields of starblooms back home. They're full of magic and very pretty.
    - **Wizard Rosalina:** The starbloom flowers, that is. Star sprites are move cute than pretty.
    - **Wizard Rosalina:** Anyway, some of the stardust I've magically analysed contained trace amounts of otherworldly pollen. Most of it gets burnt up when a shooting star lands, but over time, it's soaked into Gielinorian soil.
    - **Wizard Rosalina:** That organic residue is then absorbed by other seeds, or eaten by monsters, that get eaten by bigger nastier monsters, that poop out the indigestible bits of less big and less naster monsters...
    - **Wizard Rosalina:** And that's how you get starbloom seeds.
    - **Player:** So you're saying I can get starbloom seeds by pickpocketing farmers who carry seeds and defeating particularly nasty monsters?
    - **Wizard Rosalina:** I'm...not saying that? But if that's how you choose to interpret what I'm saying, I guess I can't stop you.
    - **Player:** So how would I grow starbloom seeds?
    - **Wizard Rosalina:** Well, it's not my area of expertise, but starblooms come from an entirely different animasphere.
    - **Wizard Rosalina:** To tune starbloom seeds to our anima mundi, you'd need to ground them in the magical field of our world's runescape.
    - **Player:** So stick a battlestaff in a flower patch, and the starbloom flower will grow up that, like a grapevine frame?
    - **Wizard Rosalina:** Well...yes, actually. You seem to know more about this than I do!
    - (previous2|Rosalina-options)
  - [Choice]: Goodbye.
    - **Player:** Bye!
    - **Wizard Rosalina:** So long!

##### During the 25th Anniversary celebrations task

- **Wizard Rosalina:** 'Star sprite, starlight, first shooting star I see tonight...'
- **Player:** Hey there, what are you up to?
- **Wizard Rosalina:** Oh, hi, I'm tracking shooting stars!
- **Wizard Rosalina:** Looking to see if any crash, so I can send out word and get the stranded star sprites some help!
- {{RSFontAchievement|Wish Upon a Star|Talk to Wizard Rosalina on the second floor of the Wizards' Tower about Shooting Stars.}}
- ((Shown in a task completion pop-up:))
  - {{Colour|#F0BE79|&nbsp;25TH ANNIVERSARY TASK&nbsp;|#181513}}
  - Wish Upon a Star
  - Talk to Wizard Rosalina on the second floor of the Wizards' Tower about Shooting Stars.
  - (continue)
- **Player:** Nice! Well, keep up the good work!
- (Condition: If all the tasks have been completed:)
  - **Player:** Looks like I've completed everything. I'd better go and see Hans about that reward!

### Attempting to place a cannon on Zolarea

- **Wizard Rosalina:** Player? What are you doing?
- **Player:** Rosalina? How are you talking to me?
- **Wizard Rosalina:** The contact spell. We've been through this.
- **Player:** I'm not sure that's how it works, but okay.
- **Wizard Rosalina:** So, what were you doing?
- **Player:** Just, er, setting up this cannon here... I wanted to check out those meteorite cannonballs...
- **Wizard Rosalina:** Really? After all the hospitality the star sprites showed you, and you're taking to shooting their planet?
- **Wizard Rosalina:** I expected better of you. If any harm comes to just one of them...
- **Player:** No, ma'am. I'll take the cannon down right away.
- (Condition: First time attempting this:)
  - {{RSFontAchievement|Gielinor Attacks!}}
