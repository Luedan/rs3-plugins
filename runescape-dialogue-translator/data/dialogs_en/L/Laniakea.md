# Laniakea

- **Original Wiki Page**: [Transcript:Laniakea](https://runescape.wiki/w/Transcript%3ALaniakea)
- **Letter**: `L`

---

## Dialogue Transcript


### Journey to Anachronia

- (see|Anachronia base camp tutorial)

### In the Anachronia base camp


#### First time

- [Menu]: Select an option
  - [Choice]: Who are you?
    - **Player:** Who are you?
    - **Laniakea:** My name is Laniakea, it's a pleasure to meet you.
    - [Menu]: Select an option
      - [Choice]: Can we talk about assignments?
        - (below)
      - [Choice]: The doorway at the top of the ruins.
        - **Laniakea:** Meet me at the ruins to the south-east and we can talk further.
      - [Choice]: Let's talk about you.
        - (below|about-you)
  - [Choice]: The doorway at the top of the ruins.
    - (above)
  - [Choice]: I am here to discuss any rewards I might be eligible for.
    - {{transcript missing}}
  - [Choice]: Er...nothing...
    - **Player:** Er...nothing...

#### Subsequent times


##### With a savage spear part in backpack

- [Menu]: Select an option
  - [Choice]: Ask Laniakea about constructing a spear.
    - (continue|Using savage spear parts on her)
  - [Choice]: Ask about something else.
    - (below|Otherwise)

##### Otherwise

- [Menu]: Select an option
  - [Choice]: Can we talk about assignments?
    - **Player:** I need another assignment.
    - (Condition: Without meeting the requirements:)
      - **Laniakea:** Sorry, but you're not a good enough slayer to be taught by me. Your best trainer would be [slayer master] in [location].
      - You need to be at least level 120 in Combat and level 90 in Slayer to train under this Slayer Master.
    - (Condition: If already on a normal assignment:)
      - **Laniakea:** You're still hunting [monster]; come back when you've finished your task.
    - (Condition: If already on Laniakea's special assignment:)
      - **Laniakea:** You still need to complete my challenge before I can give you another assignment.
      - **Player:** What did you want me to do again?
      - **Laniakea:** I've run out of vials of poison from the Vile blooms around the island. Could you collect a drop of poison from the Lampenflora, Liverworts, Luminous snagglers and Devil's snare? I will reward you handsomely.
    - (Condition: If not on an assignment:)
      - {{anchor|regular}} (Condition: Getting a normal assignment:)
        - (Condition: Slayer master cape perk is activated:)
          - [Laniakea notices your cape, and beckons for you to select your own task.]
          - (opens=Select your slayer task)
          - (continue|regular-assignment-amount)
        - (Condition: With a Slayer VIP ticket only:)
          - [Menu]: Change your assigned Slayer task?
            - [Choice]: [Amount] [monsters] (default)
              - (continue)
            - [Choice]: [Amount] [monsters] (costs 1 Slayer token)
              - (continue)
        - (Condition: Only the Slayer mask perk is available:)
          - [Menu]: Change your assigned Slayer task?
            - [Choice]: [Amount] [monsters] (default)
              - (continue)
            - [Choice]: [Amount] [monsters] (Slayer Mask - Once per day)
              - (continue)
        - (Condition: With a Slayer VIP ticket and available Slayer mask perk:)
          - [Menu]: Change your assigned Slayer task?
            - [Choice]: [Amount] [monsters] (default)
              - (continue)
            - [Choice]: [Amount] [monsters] (costs 1 Slayer token)
              - (continue)
            - [Choice]: [Amount] [monsters] (Slayer Mask - Once per day)
              - (continue)
        - {{anchor|regular-assignment-amount}} **Laniakea:** You're doing okay, I suppose. Your new task is to kill [amount] [monsters].
        - [Menu]: Select an option
          - [Choice]: Got any tips for me?
            - **Player:** Got any tips for me?
            - **Laniakea:** [Standard tip for the assigned monster]
            - [Second line of the standard tip]
          - [Choice]: Okay, great!
            - **Laniakea:** Good luck! Don't forget to come back when you require a new assignment.
          - [Choice]: No thanks. (Clear task, costs 30 Slayer points)
            - {{Transcript missing}}
      - (Condition: Getting the special assignment:)
        - **Laniakea:** How would you like a special challenge this time, instead of a regular assignment?
        - [Menu]: Select an option
          - [Choice]: Very well, I accept your challenge.
            - {{Transcript missing}}
          - [Choice]: No thanks, I'd prefer a regular assignment instead.
            - **Player:** No thanks, I'd prefer a regular assignment instead.
            - (continuea|regular)
          - [Choice]: What do you mean?
            - **Laniakea:** I've run out of vials of poison from the Vile blooms around the island. Could you collect a drop of poison from the Lampenflora, Liverworts, Luminous snagglers and Devil's snare? I will reward you handsomely.
            - [Menu]: Select an option
              - [Choice]: Very well, I accept your challenge.
                - **Laniakea:** Very good.
              - [Choice]: No thanks, I'd prefer a regular assignment instead.
                - {{Transcript missing}}
          - [Choice]: No and please don't ask me again.
            - {{Transcript missing}}
  - [Choice]: The doorway at the top of the ruins.
    - (above)
  - [Choice]: cond=After Desperate Times|Kerapac.
    - **Player:** Have you seen any sign of Kerapac?
    - **Laniakea:** I have not. Though there are a fair few ruins around here that appear to have been disturbed so there is a good chance he is still here or did something here. The ones which are open lead deep into an underground network, but cave collapses have caused the passageways to block up. It would take some serious power to shift through the rubble to get through to them.
    - **Player:** Or magic?
    - **Laniakea:** Or magic, but unless you know of an entire army of mages that are on hand to help us, we're out of luck. Our best bet is to hope that some of the sealed up ruins around the island give us passage to whatever is below.
    - (Condition: If the player is at the base camp:)
      - (end)
    - (Condition: If the player is in the south-eastern ruins:)
      - **Laniakea:** For now, I am interested in the doorway at the top of the ruins. It's sealed with an ancient dragonkin spell.
      - **Player:** You know how to read the language?
      - **Laniakea:** I would not say I am fluent, but I have studied scrolls that I discovered and learnt a bit of the language.
      - **Player:** What do the ruins say then?
      - **Laniakea:** Most of the runes above the door are worn, but there are few I am able to make out.
      - **Laniakea:** Even with the few, I can't seem to piece together what they mean.
      - **Laniakea:** Here, this word. This means 'Locked'.
      - **Laniakea:** And another few here. 'Sacrifice', 'Loss' and 'Unity'.
      - **Laniakea:** What could be so dangerous that it was entombed in layers upon layers of rock and then locked behing ancient seals?
      - **Player:** You don't plan on finding out right?
      - **Laniakea:** Aren't you the slighest bit curious, Player?
      - **Player:** You know what they say: curiosity killed the cat...
      - **Laniakea:** ...But satisfaction brought it back.
      - **Laniakea:** I must know.
      - **Laniakea:** From what I know of the dragonkin and their curse, it's no wonder that Kerapac has gone to the lengths he has for his people.
      - **Laniakea:** In a sense it's admirable.
      - **Player:** But what about the treachery he has caused? All the hurt, pain and death.
      - **Laniakea:** You're looking at it from your perspective. What would you give up and sacrifice in order to save your own kind?
      - **Laniakea:** Would you stand by and let the curse consume us? We can't even begin to imagine what they have gone through.
      - **Player:** Are you siding with Kerapac?
      - **Laniakea:** I do not take sides and I pity tose that do. There are two sides to any story or conflict and each side always believe they are right. Yes, the dragonkin have inflicted countless terrors but they have only done what they have to protect and survive.
      - **Laniakea:** That is the nature of all creatures.
      - **Laniakea:** Survival.
  - [Choice]: Let's talk about you. {{anchor|about-you}}
    - [Menu]: Select an option
      - [Choice]: Tell me more about your background.
        - **Laniakea:** I was born and raised in a village far to the east, a treacherous place. Full of death and danger.
        - **Laniakea:** To survive you could not just sit idly by and expect family to provide for you.
        - **Laniakea:** No. It was kill or be killed and my people were raised as fighters.
        - **Laniakea:** But at great cost. The things I have done and seen I must live with.
        - **Laniakea:** We do what we must to survive.
        - **Laniakea:** Eventually it was too much and I decided it would be best for me to leave that place.
        - **Laniakea:** I ventured out, but still remaining aware of what was around me and who was a threat.
        - **Laniakea:** It's safe to say I do not have many friends or those I trust and I will always follow my own agenda.
        - **Player:** Good to know...
        - **Laniakea:** Fear not. I have heard about your triumphs. You're a good soul.
        - **Player:** Have you ever returned home?
        - **Laniakea:** Never. Though I have heard stories about a hidden treasure there; something I considered just a story to scare the children from the village.
        - **Player:** What is it?
        - **Laniakea:** That is not knowledge I feel the need to share with you. What you can know is it's very powerful and if harnessed... well, who knows what can be achieved with it.
        - **Player:** Where was it you said you grew up again?
        - **Laniakea:** Nice try.
        - (previous)
      - [Choice]: How did you become a slayer master?
        - {{anchor|background}} **Laniakea:** Funny that you ask, it was never my intention to become one of the Order.
        - **Laniakea:** I happened across a meeting of the Order whilst they were tracking a beast that I was also pursuing so it became somewhat of a competition. At least I turned it into that. I wanted to see if I could be the one to take it down.
        - **Laniakea:** I ended up slaying the beast before their very eyes.
        - **Laniakea:** They were hesitant of accepting me at first, but so was I. I didn't want to be part of the Order. I didn't really have the time for it but I could not refuse all the valuable lessons they've taught me over the years.
        - **Laniakea:** Part of me also wanted a sense of belonging. As someone who grew up without family, the Order quickly became everything I wanted and never had.
        - **Laniakea:** I learnt the most from Morvran and Kuradal. Kuradal and I shared a lot of similarities so we trained together more frequently; but Morvran liked to train alone like I.
        - **Laniakea:** There was another...
        - **Laniakea:** I would not say I loved him but...
        - **Laniakea:** Something connected with him deeper down than I could have imagined and that made me...
        - **Laniakea:** ...That made me feel vulnerable. The feeling of desire, lust and longing. I had not yet felt anything like it before and they were alien to me.
        - **Laniakea:** I had to leave; craft my own path.
        - **Player:** Who was it and why did you leave that behind?
        - **Laniakea:** I'd rather not talk about this. I have told you too much already.
        - (previous)
      - [Choice]: What is this temple?
        - **Laniakea:** This site appears to be more grand than all the other areas around the island, with the exception of the ruins to the south-east.
        - (previous)
      - {{anchor|poison}} [Choice]: Tell me about your poisons.
        - **Laniakea:** Poison... Where to begin? How such a tiny drop of liquid may kill a man in either the most peaceful manner or cause them the most painful death you can imagine.
        - **Laniakea:** As you can see, as someone from the Order of Slayer Masters, I remain unmarked and lack the scars you see in my companions.
        - **Laniakea:** I tend to fight a little cleaner you could say. Whilst I can handle myself in the thick of combat, I prefer to inflict poisons upon my enemy and let that do the fighting.
        - **Player:** That sounds like fighting dirty to me.
        - **Laniakea:** It only takes a cut. Once the wound is inflicted I can vanish into the shadows and let the poison do its work.
        - **Player:** How have you not accidentally cut yourself?
        - **Laniakea:** Over my years of studying different poisons, I saw fit to drink doses of each daily to build up an immunity. Now I could drink a vial of the most deadly poisons and not feel a thing.
        - **Player:** Could you teach me how to make these poisons?
        - **Laniakea:** I will not.
          - (Condition: If the player has not completed Helping Laniakea:)
            - (see|Helping Laniakea (miniquest))
          - (Condition: If the player has completed Helping Laniakea:)
            - (previous)
      - {{anchor|doll}} [Choice]: Tell me about the doll on your belt.
        - **Player:** What is the doll you have attached to your belt?
        - **Laniakea:** A strange type of magic... This doll can be bound to a soul and any damage I deal to the doll will also be inflicted upon the bearer of its mark. If I were to twist the arm in a manner that is unnatural then the soul it links too will feel that pain.
        - **Laniakea:** It is dark magic though. So dark that even I dare not meddle with it too often.
        - **Player:** Why do you carry it around then?
        - **Laniakea:** Always be prepared for situations. Better to have it and not need it, than to need it and not have it.
        - **Player:** You have a fair enough point.
        - **Player:** How can I make one?
        - **Laniakea:** I'm not aware you can. This is an artefact from a witch coven that once thrived. They're gone now and with them, their knowledge.
        - (previous)
  - [Choice]: cond=If the special challenge is toggled off|Can I receive special slayer assignments again?
    - **Laniakea:** Sure, I will now start giving you special slayer assignments again.
  - [Choice]: Er...nothing...
    - **Player:** Er...nothing...

#### Using savage spear parts on her

- **Player:** Do you know anything about these spear pieces I found?
- ((With all parts in backpack:))
  - [You show Laniakea the spear tip.]
  - **Laniakea:** This is quite a beautiful piece, it's eerily similar to my own.
  - [You show Laniakea the spear shaft.]
  - **Laniakea:** Interesting, it's very weighty, I would imagine it's hard to use accurately.
  - [You show Laniakea the spear cap.]
  - **Laniakea:** This appears to be the partner of the spear tip you showed me. They are clearly weighted to work together.
  - [You show Laniakea the plume.]
  - **Laniakea:** This design is exquisite, it would make quite the adornment to a weapon.
  - **Laniakea:** It seems you've acquired a full spear. Will you allow me to look at it in greater detail?
  - **Player:** Of course.
  - [You hand the spear parts to Laniakea]
  - Laniakea examines each of the pieces for a short moment.
  - **Laniakea:** Very interesting. I think I could fashion this into a weapon similar to my own. If you wish?
  - [Menu]: Assemble Laniakea's Spear?
    - [Choice]: Yes.
      - (removes=the savage spear tip, shaft, cap, and plume) (receives=Laniakea's spear)
      - [Laniakea hands you back an assembled spear.]
      - **Player:** Wow! Thanks.
    - [Choice]: No.
      - **Laniakea:** Very well. You know where I am if you change your mind.
- ((Without all parts in backpack:))
  - ((With the spear tip in backpack:))
    - [You show Laniakea the spear tip.]
    - **Laniakea:** This is quite a beautiful piece, it's eerily similar to my own.
    - (continue)
  - ((With the spear shaft in backpack:))
    - [You show Laniakea the spear shaft.]
    - **Laniakea:** Interesting, it's very weighty, I would imagine it's hard to use accurately.
    - (continue)
  - ((With the spear cap in backpack:))
    - [You show Laniakea the spear cap.]
    - (Condition: Without a spear tip in backpack:)
      - **Laniakea:** Strange. This is of the same origin as mine. I do not understand how such an item could come to exist on this island.
      - (continue)
    - (Condition: With a spear tip in backpack:)
      - **Laniakea:** This appears to be the partner of the spear tip you showed me. They are clearly weighted to work together.
      - (continue)
  - ((With the plume in backpack:))
    - [You show Laniakea the plume.]
    - **Laniakea:** This design is exquisite, it would make quite the adornment to a weapon.
    - **Laniakea:** I believe it may have once been bound to a spear, much like my own.
    - (continue)
  - ((With the spear tip and spear cap in backpack:))
    - You show Laniakea the spear tip.
    - **Laniakea:** This is quite a beautiful piece, it's eerily similar to my own.
    - You show Laniakea the spear cap.
    - **Laniakea:** This appears to be the partner of the spear tip you showed me. They are clearly weighted to work together.
    - (continue)
  - **Laniakea:** If you recover the rest of the spear, bring it to me. I would very much like to see it.

### At the southeastern ruins

- [Menu]: Select an option
  - [Choice]: Can we talk about assignments?
    - (above)
  - [Choice]: The doorway at the top of the ruins.
    - (Condition: If the player has not completed Raksha, the Shadow Colossus:)
      - (see|Raksha, the Shadow Colossus (quest))
    - (Condition: If the player has completed Raksha, the Shadow Colossus:)
      - **Laniakea:** I cannot enter that place. It hurts.
      - **Laniakea:** You must go alone Player.
  - [Choice]: Let's talk about you.
    - [Menu]: Select an option
      - [Choice]: Tell me more about your background.
        - (above|background)
      - [Choice]: How did you become a slayer master?
        - (above|slayer)
      - [Choice]: What is this temple?
        - **Laniakea:** This temple, of whatever its original architectural purpose was built for, stands atop something of great importance I think.
        - **Laniakea:** There are signs of sacrificial offerings and signs of attempted openings upon the doors.
        - **Player:** Have you explored any of the other temples around the island?
        - **Laniakea:** I've visited a few, but none of them spoke to me as much as this one has. Whilst I'm sure there are secrets across the others I'm keen on exploring, there is something about this that I can't quite put my finger on.
        - (previous)
      - [Choice]: Tell me about your poisons.
        - (above|poison)
      - [Choice]: Tell me about the doll on your belt.
        - (above|doll)
  - [Choice]: cond=If the special challenge is toggled off|Can I receive special slayer assignments again?
    - (above)
  - [Choice]: Er...nothing...
    - **Player:** Er...nothing...

### Activating the Enchanted gem

- {{Transcript missing}}

### Casting NPC contact

- (see|NPC Contact#Laniakea)

### Assignment advice


#### Abyssal demons

- **Laniakea:** The last Abyssal demon I killed I found slashing attacks took them down effectively.
- [Abyssal demons are nasty creatures to deal with. They aren't really part of this realm and are able to move very quickly to trap their prey. They can be found in Canifis Slayer Tower and in the Senntisten Asylum.]

#### Acheron mammoths

- **Laniakea:** Acheron Mammoths are honourable yet powerful beasts from the frozen north. When they charge you, get out of the way! They can be found on an iceberg that is accessible from a dock near Rellekka.

#### Adamant dragons

- **Laniakea:** The last Adamant dragon I killed I found air spells took them down effectively.
- [Adamant dragons are even more dangerous than mithril dragons. Look for them in Brimhaven dungeon, beneath a staircase north-west of the iron and steel dragons.]

#### Airut

- **Laniakea:** The airut are aggressive creatures from another world. They have powerful arms and attack with great vigour. Certain abilities can counter and stun them, however.

#### Aquanites

- **Laniakea:** Aquanites are amphibious creatures that attract prey using the glowing lures on their heads. They attack stronger opponents from a distance with water magic, and dislike those who pray against it. They dwell in the Fremennik Slayer Dungeon, in a chamber past the kurasks.

#### Armoured phantoms

- **Laniakea:** The last Armoured phantom I killed I found crushing attacks took them down effectively.
- [You can find armoured phantoms swarming inside the crypts north of Fort Forinthry. Their hateful spirit seeks only violence. You'll find crush weapons effective at breaking down their ability to move.]

#### Aviansie

- **Laniakea:** The last Aviansie I killed I found a crossbow with bolts took them down effectively.
- Aviansie can be found in the God Wars Dungeon north of Trollheim. As they are flying, you'll find melee attacks are not going to cut it.

#### Black demons

- **Laniakea:** Black demons are weak to ranged attacks. They're still the strongest demon and very dangerous, however. Seek them out in the Edgeville or Brimhaven dungeons.

#### Black dragons

- **Laniakea:** Black dragons are among the strongest dragons and are very fierce. Watch out for their fiery breath. I am sure you will have seen them in your travels and have honed your techniques on lesser dragons.

#### Camel warriors

- **Laniakea:** Camel warriors can use ancient magics to attack you. They also have the blessings of Akthanakos and can create powerful, disorientating mirages.  They can be found in the deep desert.

#### Celestial dragons

- **Laniakea:** Celestial dragons are one of the strangest dragons I assign. They use melee but also have a powerful dragonfire attack, as well as a fascinating ability to momentarily stop time. You can find them in the depths of Dragontooth Island.

#### Chaos giants

- **Laniakea:** You can find Chaos giants out in the Barendir tunnels, beyond Keldagrim. Be careful, as they can launch their Dragon throwing axe at range or take a swipe at you if you get close. Perhaps you could recover some.

#### Corrupted creatures

- **Laniakea:** You can find corrupted creatures in the Sophanem Slayer Dungeon.

#### Creatures of Daemonheim

- **Laniakea:** The last Kal'gerion demon I killed I found many different combat styles took them down effectively.
- You can find various creatures from the depths of Daemonheim lurking in sinkholes across Gielinor.

#### Creatures of the lost grove

- **Laniakea:** You can find the creatures of the lost grove within the lost grove, south of the poison waste.

#### Cres's automatons

- **Laniakea:** Without their master, Cres's automatons roam Guthix's chambers attacking any who enter. They are programmed to use magic, melee or ranged and can perform a violent area-of-effect attack. Guthix's chambers may be reached via his shrine, or the excavation west of the Legends' Guild.

#### Crystal shapeshifters

- **Laniakea:** The last Crystal Shapeshifter I killed I found fire spells took them down effectively.
- Crystal shapeshifters are deranged remnants of the elves on Tarddiad. They are quite mad and, according to Angof, beyond redemption. Show them mercy by ending their suffering.

#### Dagannoth

- **Laniakea:** The last Dagannoth I killed I found slashing attacks took them down effectively.
- Dagannoth are large, sea-dwelling creatures that are very aggressive. You'll often find them in caves near sea water. There is no joy so great as to cleanse these from the face of Gielinor.

#### Dark beasts

- **Laniakea:** Dark beasts are large, dog-like predators with massively muscled bodies that protect them from crushing weapons. We found some while mining the Mourner tunnels, in search of the Temple of Light.

#### Demons

- **Laniakea:** You can find many types of demons around Gielinor.

#### Dinosaurs

- **Laniakea:** The last Feral Dinosaur I killed I found many different combat styles took them down effectively.
- [You can find a variety of dinosaurs on Anachronia.]

#### Dragons

- **Laniakea:** You can find any type of Dragon around Gielinor.

#### Edimmu

- **Laniakea:** The last Edimmu I killed I found slashing attacks took them down effectively.
- [Edimmu are ghosts which failed to escape their body. They're ghosts and zombies, yet somehow different altogether. They use ranged attacks and are highly aggressive. You can find them in a resource dungeon, which the Meilyr clan in Prifddinas has access to.]

#### Elves

- **Laniakea:** Elves are skilled fighters across all disciplines from whom you could learn a lot. I recommend challenging only one type of elf combatant at a time.

#### Ganodermic creatures

- **Laniakea:** The last Ganodermic beast I killed I found fire spells took them down effectively.
- Ganodermic beasts and runts live in the depths of a cave north-east of the Mage Training Arena. The creatures of that dungeon are coated in toxic fungus, so you should fight them from a distance. The fungus helps them repair physical damage, so you might prefer using magical attacks.

#### Gargoyles

- **Laniakea:** Gargoyles are winged creatures of stone. You'll need to fight them until they are close to death before breaking them apart with a rock hammer. They can be found in Canifis Slayer Tower.

#### Gemstone dragons

- **Laniakea:** You can find gemstone dragons beneath the gem mine in Shilo Village.

#### Glacors

- **Laniakea:** Glacors were brought to this world by Lucien. They use magic, ranged and melee attacks. You can find them in an underground cavern on the Frozen Plateau.

#### Greater demons

- **Laniakea:** Greater demons are weak to ranged attacks. Though not the strongest of demons, they are still dangerous. There are some in Brimhaven Dungeon.

#### Ice strykewyrms

- **Laniakea:** The coldest of their kind, they are found beneath the Fremennik mountains. As they are beings of ice, I've found that fire spells inflict far more damage against them.

#### Iron dragons

- **Laniakea:** Iron dragons are some of the weaker metallic dragons, with iron scales that are far thicker than normal iron armour. Their fiery breath and sharp claws can be negated by a number of means. Look for them in Brimhaven Dungeon.

#### Kal'gerion demons

- **Laniakea:** Kal'gerion demons are powerful creatures that use both magic and melee. They reside in a resource dungeon near Daemonheim. I would recommend you take cover when they smash the ground, or when they use magic to pull you towards them.

#### Kalphites

- **Laniakea:** Kalphites are large insects that live in hives under the desert sands. I am sure that, by now, you have seen them to the south-west of Shantay Pass.

#### Lava strykewyrms

- **Laniakea:** The last Lava strykewyrm I killed I found many different combat styles took them down effectively.
- [Lava strykewyrms are the most powerful of their kind. They attack with all combat styles and are weak to nothing. They can be found deep within the Wilderness so I would watch your back while slaying them.]

#### Living wyverns

- **Laniakea:** Living wyverns breathe a poison that will kill you rapidly unless you are freezing. But watch out; the colder you are the harder their regular attacks will hit you.  They can be found in the Asgarnia Ice dungeon.

#### Mithril dragons

- **Laniakea:** Mithril dragons are very dangerous opponents. There's some in the Ancient Cavern, north of where you'll find Kuradal. You are a battle master - test your skills.

#### Muspah

- **Laniakea:** Muspah are creatures born of nightmares. Ancient magic is the most effective thing to use against them. You can find them by travelling to Freneskae. They'll be aggressive unless you wear your shard of Zaros.

#### Mutated jadinkos

- **Laniakea:** These warped jade vine creatures will not hesitate to use their environment to help them in combat if they cannot retaliate otherwise. The baby jadinkos are easiest to kill, but the males offer the greatest rewards. Ranged weapons made from vines are best against them.

#### Nightmare creatures

- **Laniakea:** You can find nightmare creatures on Freneskae, which can be accessed through the world gate.

#### Nihil

- **Laniakea:** The surviving subjects of Zaros's experiments. They have powerful charge attacks and fight in packs of four. You can find them by travelling to Freneskae. They'll be aggressive unless you wear your shard of Zaros.

#### Nodon dragonkin

- **Laniakea:** Nodon dragonkin are deeply intelligent creatures, armed with advanced siege weaponry. However, they are weak to dragonbane weapons. You can find them fighting for Jas in Senntisten.

#### Order of ascension members

- **Laniakea:** The Order of Ascension are magic users. It is strongly suggested you use ranged attacks. Their tactics can make them tough one-on-one, so bringing a friend along would be beneficial.

#### Ripper demons

- **Laniakea:** Ripper Demons are driven crazy by the scent of blood. They will hit you harder the worse your injuries are. And watch out; they can sometimes drop on you from above, which is lethal.  They can be found in a fissure near Al Kharid.

#### Rune dragons

- **Laniakea:** The last Rune dragon I killed I found many different combat styles took them down effectively.
- Rune dragons are even more dangerous than adamant dragons. I highly recommend you bring dragonbane ammunition to pierce their armour. To find them, you must travel to Kethsi via the World Gate in Arandar.

#### Shadow creatures

- **Laniakea:** Shadows are light creatures that have been corrupted by the Dark Lord. The Amlodd summon them to their section of the city in order to defeat them and then cleanse their cores.

#### Soul devourers

- **Laniakea:** The last Crocodile akh I killed I found water spells took them down effectively.
- You can find soul devourers in the Sophanem Slayer Dungeon.

#### Stalker creatures

- **Laniakea:** You can find stalker creatures within Zamorak's hideout.

#### Steel dragons

- **Laniakea:** Steel dragons are dangerous and metallic, with steel scales that are far thicker than normal steel armour. Look for them in Brimhaven Dungeon.

#### Strykewyrms

- **Laniakea:** You can find jungle strykewyrms in jungles, ice strykewyrms in icy environments and lava strykewyrms in hot environments.

#### Tormented demons

- **Laniakea:** Tormented demons are powerful creatures that use magic, ranged and melee attacks. They also have the ability to shield themselves. You can find them below the Tears of Guthix cave.

#### Undead

- **Laniakea:** The last Bound skeleton I killed I found earth spells took them down effectively.
- You can find many types of undead around Gielinor, notably those festering inside the crypts north of Fort Forinthry.

#### Vile blooms

- **Laniakea:** The last Lampenflora I killed I found fire spells took them down effectively.
- You can find a variety of vile blooms on Anachronia.

#### Vyrewatch

- **Laniakea:** These foul creatures can be found throughout Meiyerditch and Darkmeyer in Morytania. They have a telepathic ability which enables them to dodge incoming attacks, so you'll need a weapon specially created to harm them.

#### Armoured phantoms

- **Laniakea:** You can find armoured phantoms swarming inside the crypts north of Fort Forinthry. Their hateful spirits seek only violence. You'll find crush weapons effective at breaking down their ability to move.

#### Risen ghosts

- **Laniakea:** These tortured spirits have been risen from the dead by Zemouregal and are bound to his will. You can find risen ghosts inhabiting the depths within the crypts north of Fort Forinthry, waiting for Zemouregal's command. You'll find bows effective against this target.
