# Kuradal

- **Original Wiki Page**: [Transcript:Kuradal](https://runescape.wiki/w/Transcript%3AKuradal)
- **Letter**: `K`

---

## Dialogue Transcript

{{Incomplete|needs Raptor meeting dialogue}}

### At the [[Ancient Cavern]]


#### Talking to Kuradal

- **Kuradal:** Heya, can I help you?
- [Menu]: Select an option
  - [Choice]: I need another assignment.
    - **Player:** I need another assignment.
    - (Condition: If the player is not level 110 Combat and 75 Slayer:)
      - **Kuradal:** Sorry, but you're not strong enough to be taught by me.
  - [Choice]: Can we talk about items and incentives?
    - **Player:** Can we talk about items and incentives?
    - **Kuradal:** Of course, what would you like to discuss: items for sale or incentives?
    - [Menu]: Select an option
      - [Choice]: Let's talk items.
        - **Player:** Let's talk items.
        - **Player:** I have a wide selection of Slayer equipment - take a look!
        - (opens=Slayer Equipment)
      - [Choice]: Let's talk incentives.
        - [Menu]: Select an Option
          - [Choice]: View rewards.
            - (opens=Slayer Rewards)
          - [Choice]: How do I earn co-op points to spend on rewards?
            - **Kuradal:** You'll gain co-op reward points if you complete at least half of your contribution to a task with a friend. That means you need to be in a group for most of the time you're working on the task, but it doesn't matter if your friend beats you to the majority of kills! You'll still have been in a group for most of your contribution, so you're still entitled to a co-op reward point.
              - [Choice]: View rewards.
                - (above)
              - [Choice]: Where can I use the co-op food and potion rewards?
                - (below)
              - [Choice]: That's all, thanks.
                - (end)
          - [Choice]: Where can I use the co-op food and potion rewards?
            - **Kuradal:** The rewards can be used in most of the areas we commonly send you to complete your tasks.
            - [Choice]: View rewards.
              - (above)
            - [Choice]: How do I earn co-op points to spend on rewards?
              - (above)
            - [Choice]: That's all, thanks.
  - [Choice]: cond=If the player does not have 99 Slayer|Tell me about your skillcape, please.
    - **Player:** Tell me about your skillcape, please.
    - **Kuradal:** This is a Slayer's Skillcape. Only a true Slayer master is permitted to wear one. You need more training before you earn that honour.
  - [Choice]: cond=If the player has 99 Slayer:|Can you sell me a Slayer skillcape?
    - **Kuradal:** Well you have performed well as a student. I guess you have earned the right to wear such a prestigious cape now. That will be 99,000 coins, please.
    - ((If the player has a Ring of charos (a) equipped, the message is replaced with the following:))
      - **Kuradal:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
    - (Condition: If the player has an inverted skillcape token or inverted master skillcape token in their inventory attuned to Slayer:)
      - **Kuradal:** I see you have one of Hans' cape inversion tokens! I'll take that off your hands, and will sell you any inverted cape you're eligible for.
      - (removes=any inverted skillcape token and inverted master skillcape token)
        - (continue)
    - [Menu]: Choose an option:
      - [Choice]: 99,000 coins? That's much too expensive. ((or 92,000 coins with Ring of charos (a)))
        - **Kuradal:** Not at all; there are many other adventurers who would love the opportunity to purchase such a prestigious item! You can find me here if you change your mind.
      - [Choice]: I think I have the money right here, actually.
        - *(If the player has at least two free backpack spaces:)*
          - (removes=99,000 coins (or 92,000 coins with Ring of charos (a))) (receives=Slayer cape (or trimmed version if level 99 in at least two skills) and Slayer hood)
          - **Kuradal:** Excellent! Wear that cape with pride my friend.
        - (Condition: If the player doesn't have at least two free backpack spaces:)
          - **Kuradal:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some inventory space before I can sell you one.
      - [Choice]: cond=If the player has given Kuradal an inverted skillcape token:|I'd like a skillcape with the colours inverted.
        - (receives=Inverted Slayer skillcape)
      - [Choice]: cond=If the player has level 120 Slayer:|I've mastered this skill. Is there anything else?
        - **Kuradal:** There is something...though I have kept it a secret for a very long time. It is something that can only be worn by a true master.
        - **Kuradal:** Not even I can wear it - that's how hard it is to achieve.
        - **Kuradal:** You say you're a master. Stand straight, let me take a look at you...
        - **Kuradal:** You...really have mastered it. What an honour! It would be my pleasure to sell you a Slayer master cape.
          - Buy Slayer master cape for 120,000 coins?
            - Yes.
              - *(If the player has at least one free backpack space:)*
                - (removes=120,000 coins) (receives=Slayer master cape)
              - *(If the player does not have at least one free backpack space:)*
                - **Kuradal:** You do not have enough room in your inventory. Please come back when you have some more.
            - No.
            - (end)
      - [Choice]: cond=If the player has given Kuradal an inverted master skillcape token:|I'd like a master cape with the colours inverted.
        - ((Same as I've mastered this skill. Is there anything else?, except the receive an inverted master Slayer skillcape instead of a normal Slayer master cape))
  - [Choice]: I've noticed there are a couple versions of each skillcape.
    - **Kuradal:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
    - *(If the player has chosen the new skillcape models:)*
      - **Kuradal:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
      - Select an option
        - Yes, I would like to wear the old version of the skillcape.
          - **Kuradal:** Would you like to wear the old model for just this cape, or for the Quest point cape and all of the skillcapes you own?
          - Select an option
            - I would just like to change the Slayer skillcape.
              - **Kuradal:** No problem, you will now use the older model for your Slayer skillcape.
            - I would like to change all my skillcapes.
              - **Kuradal:** No problem, you will now use the older model for all of your skillcapes!
            - I've changed my mind!
              - (end)
        - [Choice]: No, thank you.
          - **Kuradal:** Great! I'm glad you're enjoying our new version!
          - *(If the player is using the old skillcape models except for the Slayer cape:)*
            - **Kuradal:** If you want, I can make it so you use the newer model for all of the skillcapes you own!
            - [Menu]: Select an option
              - [Choice]: Ok, I'd like to wear the newer version for all my skillcapes.
                - **Kuradal:** Great, you will now use the newer model for all of your skillcapes!
              - No, thanks.
                - (end)
    - *(If the player has chosen the old skillcape models:)*
      - **Kuradal:** It looks like you're currently using the old model for your Slayer skillcape. Would you like to change to the newer one?
      - [Menu]: Select an option
        - [Choice]: Yes, I would like to wear the new version of the skillcape.
          - **Kuradal:** Would you like to wear the newer model for just this cape, or all of the skillcapes you own?
          - Select an option
            - I would just like to change the Slayer skillcape.
              - **Kuradal:** No problem, you will now use the newer model for your Slayer skillcape.
            - I would like to change all my skillcapes.
              - **Kuradal:** No problem, you will now use the newer model for all of your skillcapes!
            - I've changed my mind!
              - (end)
        - No, thank you.
          - **Kuradal:** Great! I'm glad you're still enjoying the old version!
          - *(If the player is using the new skillcape models except for the Slayer cape:)*
            - **Kuradal:** If you want, I can make it so you use the old model for all of the skillcapes you own!
            - Select an option
              - Ok, I'd like to wear the old version for all my skillcapes.
                - **Kuradal:** Great, you will now use the old model for all of your skillcapes!
              - No, thanks.
                - (end)
  - [Choice]: Let's talk about you.
    - **Player:** Let's talk about you.
    - **Kuradal:** I'm Kuradal, daughter of Duradel. What more would you like to know?
      - Tell me more about your background.
        - **Player:** Tell me more about your background.
        - **Kuradal:** If you so desire. As I said, I am Kuradal, daughter of Duradel - another great master of Slayer. Unlike the others, though, I ventured out not only to slay, but also to capture. I've caught many different types of creatures and I hold them within this dungeon, reserved exclusively for my pupils to slay.
        - **Player:** So slaying runs in the family, then?
        - **Kuradal:** Of course. One cannot simply 'grow up' with someone like my father. My childhood was all combat training, taking on the beasts of this land side by side with my father.
          - So who is your mother?
            - **Player:** So who is your mother?
            - **Kuradal:** I'd rather not say. Can we talk about something else?
              - About your father...
                - *(Same as below)*
              - That's all for now.
                - **Player:** That's all for now.
                - **Kuradal:** Fine. I'll be here if you need me.
          - Sounds like you had a hectic childhood!
            - **Player:** Sounds like you had a hectic childhood!
            - **Kuradal:** You could say that, but I am thankful for it as it made me the person I am today.
              - About your father...
                - *(Same as below)*
              - That's all for now.
                - *(Same as above)*
      - About your father...
        - *If you have not yet completed While Guthix Sleeps*
          - **Player:** About your father... How come you aren't with him now?
          - **Kuradal:** We are still close, but combat and competition runs deep in both our veins. I strive to be the best, so took up a Slayer Master position and want to give people a greater challenge than that of my father.
        - *If you have completed Ritual of the Mahjarrat*
          - **Player:** About your father... Lucien is dead!
          - **Kuradal:** I know. I saw his corpse up at the ritual site.
          - **Player:** What? You were there? I didn't see you.
          - **Kuradal:** Nor I you, but I was there, fighting off Mahjarrat and their minions. None of them were Lucien, though. I chased one of them into a cave, full of ice elementals called glacors. After killing a couple hundred of those, I managed to escape, but by then it was all over: everyone had gone.
          - **Player:** You sound angry. I'd have thought you'd be glad he's dead!
          - **Kuradal:** I am, but Lucien was my kill! Mine alone! No one had the right to take that from me! No one! ... How will I honour my father's memory?
            - You honour him every day.
              - **Player:** You honour him every day.
              - **Kuradal:** Bah! Any more of that touchy-feely nonsense and I'll be forced to revoke your Slayer licence...
              - **Player:** But, yo-
              - **Kuradal:** Hahaha! The look on your face! That cheered me up some. Thanks, Player. 'You honour him every day.'
              - **Player:** I'm, er, glad I could help.
              - **Kuradal:** Now, can I help with anything else?
            - By helping to defeat what killed Lucien!
              - **Player:** By helping to defeat what killed Lucien!
              - **Kuradal:** Which was what, exactly?
              - **Player:** A dragonkin. Three of them, in fact.
              - **Kuradal:** Hmm, now that sounds like a challenge worthy of a slayer master. I've got some preparations to make. Collecting those for a dungeon could be tricky...
              - **Player:** Collecting them? You're crazy!
              - **Kuradal:** Now, can I help with anything else?
      - So what's in this dungeon then?
        - **Player:** So what's in this dungeon then?
        - **Kuradal:** Well, I've been all over and managed to capture hellhounds, greater demons, gargoyles, abyssal demons, airut, dark beasts, blue, iron, and steel dragons.
          - *If you're playing as male character* **Player:** You caught them single-handedly?
          - **Kuradal:** You doubt my skills?
          - I didn't mean anything by it.
            - **Player:** I didn't mean anything by it.
            - **Kuradal:** I'm glad to hear so. *(continues as below)*
          - Well, come on. You are just a girl and I'm a tough warrior!
            - **Player:** Well, come on. You are just a girl and I'm a tough warrior!
            - **Kuradal:** Just a girl, am I? Right? *(Kuradal knocks you out, and you wake up outside the ancient caverns.)*
        - **Player:** So is there anything else that's special about this dungeon?
        - **Kuradal:** I'm glad you asked. You might find creatures inside the dungeon drop something called a ferocious ring - they must have foraged them from remains in the area.
        - **Player:** Well, that's great and all, but what exactly does it do?
        - **Kuradal:** Well, for one thing, they are bound to these caves, so you'll find it has teleport charges that will return you to this place if you command it.
        - **Player:** Sounds good, but is that it?
        - **Kuradal:** Oh, no. As I said, it is bound to this area, so you'll find that you do more damage to creatures in the dungeon if you are wearing it. Also, if you happen to be near death in the dungeon, it'll save you in a similar manner to a ring of life, teleporting you back to the safety of my presence.
        - **Player:** Even if I'm using ranged or magical combat? And what if I'm not in the dungeon when I die wearing it?
        - **Kuradal:** Calm down, one question at a time. First, it is a powerful artefact and will affect all combat styles. Second, I would be careful about dying outside wearing it. I do not believe it will work anywhere but inside the dungeon here.
        - **Player:** Thanks for your help, Kuradal.
        - **Kuradal:** No problem. Anything else?
          - (initial)
  - [Choice]: cond=If the player has special slayer assignments disabled, the "Let's talk about you" option is replaced with the following|Can I receive special slayer assignments again?
    - **Kuradal:** Sure, I will now start giving you special slayer assignments again.
  - [Choice]: Er...nothing...
    - **Player:** Er...nothing...
    - (end)

#### Attempting to enter her dungeon

*Without a task from her:*
- **Kuradal:** Sorry, my dungeon is exclusive only to those who need to go in there.
- **Player:** Exclusive?
- **Kuradal:** Yes, I only allow pupils of Slayer into this dungeon and only if they need to slayer the creatures I've caught inside.
- **Player:** I see. So what creatures do I need to be assigned to kill; what creatures are inside?
- **Kuradal:** Well, I took a holiday tour of Gielinor and brought back some 'souvenirs'. Of course, as a Slayer master, 'souvenirs' means hellhounds, greater demons, gargoyles, abyssal demons, airut, dark beasts, and blue, iron, and steel dragons.
- **Player:** I'd usually keep it simple with a postcard.
- **Kuradal:** What was that?
- **Player:** I said that must have been hard.
*With a cannon:*
- **Kuradal:** Sorry, no cannons allowed in there. Now I've rounded all these creatures up, I don't particularly want their lair being blasted apart.

### Activating the [[enchanted gem]]


#### If Kuradal is your current Slayer Master

- **Kuradal:**  Hello there, Player, what can I help you with?
  - How am I doing so far?
    - **Player:**  How am I doing so far?
      - *If you are currently on a Slayer task that is not yet complete: *
        - **Kuradal:**  You're currently assigned to kill [assigned creatures]; only X more to go.
          - Who are you?
            - *(Same as below)*
          - Where are you?
            - *(Same as below)*
          - Got any tips for me?
            - *(Same as below)*
          - That's all thanks.
            - **Player:**  That's all thanks.
      - *If you have completed your most recent Slayer task: *
        - {{Transcript missing}}
  - Who are you?
    - **Player:**  Who are you?
    - **Kuradal:**  My name is Kuradal; I'm a Slayer Master.
      - How am I doing so far?
        - *(Same as above)*
      - Where are you?
        - *(Same as below)*
      - Got any tips for me?
        - *(Same as below)*
      - That's all thanks.
        - *(Same as above)*
  - Where are you?
    - **Player:**  Where are you?
    - **Kuradal:**  You'll find me in the ancient cavern, near the Dragonkin Forge. I'll be here when you need a new task.
      - How am I doing so far?
        - *(Same as above)*
      - Who are you?
        - *(Same as above)*
      - Got any tips for me?
        - *(Same as below)*
      - That's all thanks.
  - Got any tips for me?
    - **Player:**  Got any tips for me?
    - **Kuradal:**  The last [assigned creature] I killed I found [weapons] took them down effectively.
    - [Task hint]
      - How am I doing so far?
        - *(Same as above)*
      - Who are you?
        - *(Same as above)*
      - Where are you?
        - *(Same as above)*
      - That's all thanks.
        - *(Same as above)*
  - Nothing really.
    - **Player:**  Nothing really.

### Casting [[NPC Contact]]

- **Player:** Hello?
- **Kuradal:** 'Ello, who's this?
- **Player:** It's Player. I'm using my magic to communicate with you.
- **Kuradal:** A useful application of magical talent. How can I help?
  - Select an option
    - I need another assignment.
      - *(Same as above)*
    - Er...nothing.
      - **Player:** Er...nothing.

### Assignment advice


#### Aberrant spectres

- **Kuradal:** Aberrant spectres are fetid, vile ghosts. The very smell of them will paralyse and harm you. A nosepeg will help ignore their stink when fighting them. They can be found in the Slayer Tower near Canifis and I have heard rumours that they also live beneath Pollnivneach in the desert.

#### Abyssal demons

- **Kuradal:** Abyssal demons are nasty creatures to deal with. They aren't really part of this realm and are able to move very quickly to trap their prey. I've managed to trap a few in the dungeon I'm guarding.

#### Acheron mammoths

- **Kuradal:** Acheron Mammoths are honourable yet powerful beasts from the frozen north. When they charge you, get out of the way! They can be found on an iceberg that is accessible from a dock near Rellekka.

#### Adamant dragons

- **Kuradal:** Adamant dragons are even more dangerous than mithril dragons. Look for them in Brimhaven dungeon, beneath a staircase north-west of the iron and steel dragons.

#### Airut

- **Kuradal:** The Airut are aggressive creatures from another world. They have powerful arms and attack with great vigour, certain abilities are able to counter and stun the Airut.

#### Aquanites

- **Kuradal:** Aquanites are amphibious creatures that attract prey using the glowing lures on their heads. They attack stronger opponents from a distance with water magic, and dislike those who pray against it. They dwell in the Fremennik Slayer Dungeon, in a chamber past the kurasks.

#### Ascension members

- **Kuradal:** The Order of Ascension are magic users. It is strongly suggested you use ranged attacks. Their tactics can make them tough one-on-one, so bringing a friend along would be beneficial.

#### Aviansies

- **Kuradal:** Aviansies can be found in the Godwars Dungeon north of Trollheim. As they are flying, you'll find melee attacks are not going to cut it.

#### Black demons

- **Kuradal:** Black demons are weak to ranged attacks. They're still the strongest demon and very dangerous, however. Seek them out in the Edgeville or Brimhaven dungeons.

#### Black dragons

- **Kuradal:** Black dragons are among the strongest dragons and are very fierce. Watch out for their fiery breath. I am sure you will have seen them in your travels and have honed your techniques on lesser dragons.

#### Bloodveld

- **Kuradal:** Bloodvelds are strange, demonic creatures. They use their long, rasping tongue to feed on just about anything they can find. Remember that their tongues are magical in nature, but, more so, they deserve to die.

#### Blue dragons

- **Kuradal:** Blue dragons aren't as strong as other dragons, but they're still very powerful. I've managed to trap a few in the dungeon I'm guarding.

#### Camel warriors

- **Kuradal:** Camel warriors can use ancient magics to attack you. They also have the blessings of Akthanakos and can create powerful, disorientating mirages.  They can be found in the deep desert.

#### Celestial dragons

- **Kuradal:** Celestial dragons are one of the strangest dragons I assign. They use melee but have a powerful dragonfire as well as a fascinating ability to momentarily stop time. You can find them in the depths of Dragontooth Island.

#### Chaos giants

- **Kuradal:** You can find Chaos giants out in the Barendir tunnels, beyond Keldagrim. Be careful, as they can launch their Dragon throwing axe at range or take a swipe at you if you get close. Perhaps you could recover some.

#### Corrupted creatures

- **Kuradal:** You can find corrupted creatures in the Sophanem Slayer Dungeon.

#### Cres's automatons

- **Kuradal:** Without their master, Cres's automatons roam Guthix's chambers, attacking any who enter. They are programmed to use magic, melee or ranged and do a violent area-of-effect attack. Guthix's chambers may be reached via his shrine, or the excavation west of the Legends' Guild.

#### Dagannoth

- **Kuradal:** Dagannoth are large, sea-dwelling creatures that are very aggressive. You'll often find them in caves near sea water. There is no joy so great as to cleanse these from the face of Gielinor.

#### Dark beasts

- **Kuradal:** The last Dark beast I killed I found a crossbow with bolts took them down effectively.
- [Dark beasts are large, dog-like predators with massively muscled bodies that protect them from crushing weapons. I've managed to trap a few in the dungeon I'm guarding.]

#### Desert strykewyrms

- **Kuradal:** You'll find these East of Al Kharid, atop the mountain. Watch out for their vicious ranged attacks!

#### Dust devils

- **Kuradal:** Dust devils use clouds of dust, sand, ash and whatever else they can inhale to blind and disorientate their victims. Good luck on obtaining a dragon chainmail from their dusty remains.

#### Edimmu

- **Kuradal:** Edimmu are ghosts which failed to escape their body. They're ghosts and zombies, yet somehow different altogether. They use ranged attacks and are highly aggressive. You can find them in a resource dungeon, which the Meilyr clan in Prifddinas has access to.

#### Elves

- **Kuradal:** Elves are skilled fighters across all disciplines from whom you could learn a lot. I recommend challenging only one type of elf combatant at a time.

#### Fire giants

- **Kuradal:** Like other giants, fire giants often wield large weapons. Learn to recognise what kind of weapon it is and act accordingly. Remember the days when these were a challenge to you and laugh.

#### Ganodermic creatures

- **Kuradal:** Ganodermic beasts and runts live in the depths of a cave north-east of the Mage Training Arena. The creatures of that dungeon are coated in toxic fungus, so you should fight them from a distance. The fungus helps them repair physical damage, so you might prefer using magical attacks.

#### Gargoyles

- **Kuradal:** Gargoyles are winged creatures of stone. You'll need to fight them until they are close to death before breaking them apart with a rock hammer. I've managed to trap a few in the dungeon I'm guarding.

#### Gemstone dragons

- **Kuradal:** You can find gemstone dragons beneath the gem mine in Shilo Village.

#### Glacors

- **Kuradal:** Glacors were brought to this world by Lucien. They use magic, ranged and melee attacks. You can find them in an underground cavern on the Frozen Plateau.

#### Greater demons

- **Kuradal:** Greater demons are weak to ranged attacks. Though not the strongest of demons, they are still dangerous. I've managed to trap a few in the dungeon I'm guarding.

#### Grifolapines

- **Kuradal:** Grifolapines live in the depths of a cave north-east of the Mage Training Arena. The creatures of that dungeon are coated in toxic fungus, so you should fight them from a distance, and dodge when they charge at you. The fungus helps them repair physical damage, so you might prefer using magical attacks.

#### Grifolaroos

- **Kuradal:** Grifolaroos live in the depths of a cave north-east of the Mage Training Arena. The creatures of that dungeon are coated in toxic fungus, so you should fight them from a distance, although they'll try to hop over obstacles towards you. The fungus helps them repair physical damage, so you might prefer using magical attacks.

#### Grotworms

- **Kuradal:** Grotworms have recently been spotted in a cave near Rimmington. They will bite and attack with some sort of acid spit. Be careful - they are very aggressive.

#### Hellhounds

- **Kuradal:** Hellhounds are a cross between dogs and demons; they are also dangerous with a fierce bite. I've managed to trap a few in the dungeon I'm guarding.

#### Ice strykewyrms

- **Kuradal:** The coldest of their kind, they are found beneath the Fremennik mountains. As they are beings of ice, I've found that fire spells inflict far more damage against them.

#### Iron dragons

- **Kuradal:** Iron dragons are some of the weaker metallic dragons, with iron scales that are far thicker than normal iron armour. Their fiery breath and sharp claws can be negated by a number of means. I've managed to trap a few in the dungeon I'm guarding.

#### Jungle strykewyrms

- **Kuradal:** These tricky creatures burrow beneath the jungle north west of Oo'glog. Be careful, as these poisonous jungle wyrms like to use magical attacks from a distance, while they should be weak to stab attacks.

#### Kal'gerion demons

- **Kuradal:** Kal'gerion demons are powerful creatures that use both magic and melee. They reside in a storage dungeon near Daemonheim. I would recommend you take cover when they smash the ground, or when they use magic to pull you towards them.

#### Kalphites

- **Kuradal:** Kalphites are large insects that live in hives under the desert sands. I am sure that, by now, you have seen them to the south-west of Shantay Pass.

#### Lava strykewyrms

- **Kuradal:** Lava strykewyrms are the most powerful of their kind. They attack with all combat styles and are weak to nothing. They can be found deep within the Wilderness so I would watch your back while slaying them.

#### Living rock creatures

- **Kuradal:** Found beneath the Dwarven mines, these are tough beings of rock. They can use ranged or melee attacks against you, so plan accordingly!

#### Living wyverns

- **Kuradal:** Living wyverns breathe a poison that will kill you rapidly unless you are freezing. But watch out; the colder you are the harder their regular attacks will hit you.  They can be found in the Asgarnia Ice dungeon.

#### Mithril dragons

- **Kuradal:** Mithril dragons are very dangerous opponents. They live just north of where we are now. You are a battle master - test your skills.

#### Muspah

- **Kuradal:** Muspah are creatures born of nightmares. Ancient magic is the most effective thing to use against them. You can find them by travelling to Freneskae. They'll be aggressive unless you wear your shard of Zaros.

#### Mutated jadinkos

- **Kuradal:** These warped jade vine creatures will not hesitate to use their environment to help them in combat if they cannot retaliate otherwise. The baby jadinkos are easiest to kill, but the males offer the greatest rewards. Ranged weapons made from vines are best against them.

#### Nechryael

- **Kuradal:** Nechryael are demons of decay that summon small winged beings to help them fight their victims. They can be found in the Chaos Tunnels or in Canifis Slayer Tower.

#### Nightmare creatures

- **Kuradal:** You can find nightmare creatures on Freneskae, which can be accessed through the world gate.

#### Nihil

- **Kuradal:** The surviving subjects of Zaros's experiments. They have powerful charge attacks and fight in packs of four. You can find them by travelling to Freneskae. They'll be aggressive unless you wear your shard of Zaros.

#### Ripper demons

- **Kuradal:** Ripper Demons are driven crazy by the scent of blood. They will hit you harder the worse your injuries are. And watch out; they can sometimes drop on you from above, which is lethal.  They can be found in a fissure near Al Kharid.

#### Sanguine werewolves

- **Kuradal:** The last Sanguine werewolf I killed I found earth spells took them down effectively.
- [Sanguine werewolves are werewolves twisted by the Sanguine. You will find them in Berylbrook on Havenhythe.]

#### Skeletal wyverns

- **Kuradal:** Skeletal wyverns are extremely dangerous, and they are hard to hit with arrows as they slip right through. To stand a good chance of surviving, you'll need some elemental shielding from their icy breath.

#### Soul devourers

- **Kuradal:** You can find soul devourers in the Sophanem Slayer Dungeon.

#### Spiritual mages

- **Kuradal:** Spiritual mages are the strongest of the spiritual guardians. They are devastating against warriors, but a smart ranger can sometimes defeat them. Of course, Prayer might serve you well, too. They can be found in the icy caverns near Trollheim, supporting the cause of their chosen god.

#### Stalker creatures

- **Kuradal:** The last Soulgazer I killed I found a bow and arrows took them down effectively.
- [You can find stalker creatures within Zamorak's hideout.]

#### Steel dragons

- **Kuradal:** Steel dragons are dangerous and metallic, with steel scales that are far thicker than normal steel armour. I've managed to trap a few in the dungeon I'm guarding.

#### Suqahs

- **Kuradal:** Suqahs can only be found on the mystical Lunar Isle. They use melee and magical attacks, and they often drop hide, teeth and herbs.

#### Terror dogs

- **Kuradal:** Terror dogs are, unsurprisingly, dogs that terrorise the weak. You'll find them in the Haunted Mine, near Tarn's lair.

#### Tormented demons

- **Kuradal:** Tormented demons are powerful creatures that use magic, ranged and melee attacks. They also have the ability to shield themselves. You can find them below the Tears of Guthix cave.

#### Tzhaar

- **Kuradal:** The TzHaar contains some mighty warriors, prove yourself against them. You'll find them deep within the Karamja volcano.

#### Volcanic creatures

- **Kuradal:** These are the creatures that live within the TzHaar fightcaves. You'll have to venture down into the cave in the Karamja volcano to take them on.

#### Vyrewatch

- **Kuradal:** These foul creatures can be found throughout Meiyerditch and Darkmeyer in Morytania. They have a telepathic ability which enables them to dodge incoming attacks, so you'll need a weapon specially created to harm them.

#### Warped tortoises

- **Kuradal:** Warped tortoises are creatures tainted by magical waste. They are vulnerable to an elven chime. I know you have seen them in your adventures, so go crack some carapace.

#### Waterfiends

- **Kuradal:** Waterfiends are creatures of water that live just north of us. Those followed by familiars are keen to slay these elemental forces.
