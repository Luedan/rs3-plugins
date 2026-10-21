# Wahisietel

- **Original Wiki Page**: [Transcript:Wahisietel](https://runescape.wiki/w/Transcript%3AWahisietel)
- **Letter**: `W`

---

## Dialogue Transcript

{{cleanup}}

### First time informing about Jhallan


#### After The Temple at Senntisten

- **Player:** You told me how to thaw out the Muspah. I thought I should keep my part of the bargain.
- **Ali the Wise:** Oh! So you have some information for me? I must record this!
- **Player:** To start with, the Muspah wasn't what it appeared to be.
- **Player:** It turned out to be alive all along, and once I'd freed it, it... changed. It told me it was a Mahjarrat.
- **Player:** It was quite a shock to suddenly see its head was a skull.
- **Ali the Wise:** The Muspah creature was a Mahjarrat in disguise?
- **Player:** Yes, he's called Jhallan. He was incredibly weak and wanted to hibernate under the Mahjarrat ritual site.
- **Player:** I found him somewhere peaceful and put him back to sleep. Apparently the ritual will rejuvenate any Mahjarrat nearby.
- **Ali the Wise:** Well, we know where to find him again, should we ever need to.
- (continue)

#### Unknown conditional

- **Player:** So this is your place?
- **Ali the Wise:** Humble but homely, I think. It suits me well. How good to see you again!
- **Player:** You told me how to thaw out the Muspah. I thought I should keep my part of the bargain.
- **Ali the Wise:** Oh! So you have some information for me? I must record this!
- **Player:** To start with, the Muspah wasn't what it appeared to be.
- **Player:** It turned out to be alive all along, and once I'd freed it, it... changed.
- **Player:** It told me it was a Mahjarrat. It was quite a shock to suddenly see its head was a skull.
- **Ali the Wise:** The Muspah creature was a Mahjarrat in disguise?
- **Player:** Yes, he's called Jhallan. He was incredibly weak and wanted to hibernate under the Mahjarrat ritual site.
- **Player:** I found him somewhere peaceful and put him back to sleep. Apparently the ritual will rejuvenate any Mahjarrat nearby.
- **Ali the Wise:** We know where to find him again, should we ever need to.
- **Ali the Wise:** Well, that creature in the ice has given me much to think about.
- **Ali the Wise:** I've started to research these Mahjarrat; I'm worried they may be a threat to us humans. We need to collaborate to gather as much information as possible.
- (continue)

### After The Temple at Senntisten


#### Before telling Ali the Wise about Dr Nabanik

- [Menu]: What would you like to say?
  - [Choice]: How goes the research?
    - **Player:** How goes the research?
    - **Ali the Wise:** Nothing new. Have you spoken to Dr Nabanik yet?
    - [Menu]: What would you like to say?
      - [Choice]: Yes, and I've finished helping him.
        - **Player:** Yes, and I've finished helping him.
        - **Ali the Wise:** Splendid, I knew I could rely on you. I trust you were appropriately rewarded?
        - **Player:** Indeed, I now have the ability to use curses in place of prayers.
        - **Ali the Wise:** Really? I've heard of these curses in ancient texts, but had presumed them to be myths. Be sure to use your newfound power wisely.
        - **Player:** As you may know, Dr Nabanik is actually a Mahjarrat named Azzanadra.
        - **Ali the Wise:** I must admit I had my suspicions, Player. He seemed to know a lot about history, but the way he talked about it...
        - **Ali the Wise:** Well, like it was an eyewitness account.
      - [Choice]: No, I never went to see him.
        - **Player:** No, I never went to see him.
        - **Ali the Wise:** It astounds me, Player, that after all the help we have been to each other, you insist on lying to me.
        - **Ali the Wise:** You know that I receive information from across the world. Do you really think I would not have heard of your struggles at that frozen fortress, or your sticky fingered antics at the Barrows?
        - [Menu]: What would you like to say?
          - [Choice]: I'm sorry, I shouldn't keep information from you.
            - **Player:** I'm sorry, I shouldn't keep information from you.
            - **Ali the Wise:** Splendid, let's try again.
            - **Ali the Wise:** Nothing new. Have you spoken to Dr Nabanik yet?
            - (continuea)
          - [Choice]: I'm not comfortable sharing information with you anymore.
            - **Player:** I'm not comfortable sharing information with you anymore.
            - **Ali the Wise:** So be it. Speak to me again when you've got over your little paranoid episode.
      - [Choice]: Never mind.
        - **Player:** Never mind.
  - [Choice]: About the Mahjarrat...
    - **Player:** About the Mahjarrat...
    - [Menu]: Select an Option
      - [Choice]: I may have more interesting information.
        - **Player:** I have more interesting information about the Mahjarrat.
        - **Ali the Wise:** Good, good, I'm always happy to compile more information on these creatures. They are of great interest to me.
        - (Condition: If the player has new information:)
          - (continue|I have more information about the Mahjarrat)
        - (Condition: If the player does not have new information:)
          - **Player:** Nothing else particularly interesting springs to mind.
      - [Choice]: So, what do we know so far?
        - **Player:** So what information do we have compiled so far?
        - **Ali the Wise:**  The Mahjarrat are powerful creatures with a strong aptitude for magic including the ability to change their form and look like other creatures. There are a number of Mahjarrat active in the world.
        - **Ali the Wise:**  Jhallan, who you helped hibernate in the north, seems much weaker than I'd expect the Mahjarrat to be. You spoke of a Rejuvenation Ritual, perhaps he was not present at the last ritual.
      - [Choice]: I've got to go now.
        - **Player:** I've got to go now.
        - **Ali the Wise:** Good luck. Come back if you find more interesting Mahjarrat information.

#### After telling Ali the Wise about Dr Nabanik

- **Player:** How goes the research?
- **Ali the Wise:** Well, I'm finding out all sorts of interesting things. Nothing particularly relevant, mind you. I'm sure I'll make a proper breakthrough and find something more relevant in time, though.
- [Menu]: Select an Option
  - [Choice]: I may have more interesting information.
  - [Choice]: So, what do we know so far?
  - [Choice]: I've got to go now.

### After Ritual of the Mahjarrat (?)

- [Menu]: Choose an option:
  - [Choice]: I'd like to talk about the Ritual
    - **Player:** Ali. Or should I call you Wahisietel now?
    - **Ali the Wise:** Either will suffice.
    - [Menu]: Choose an option:
      - [Choice]: cond=After Missing, Presumed Death|I'd like to ask about what happened at the Empyrean Citadel.
        - (Condition: If the player declared support for Zaros:)
          - **Ali the Wise:** I was happy to learn you supported the Empty Lord while debating with the gods. I'm sure he is aware of your deeds.
          - **Ali the Wise:** Sliske may be acting recklessly, but at least you remained calm and dedicated to Zaros.
          - (continue)
        - (Condition: If the player declared support for another faction:)
          - **Ali the Wise:** Mmm. I was most displeased to learn you did not support Zaros, Player. I expected more of you.
          - (continue)
        - [Menu]: Select an Option
          - [Choice]: Do you still see Sliske as a Zarosian?
            - **Ali the Wise:** I do not. That snake has betrayed us for the last time. After murdering Guthix I was disappointed in him, but now I have lost all hope.
            - **Ali the Wise:** It has always been his way to act alone; spending his days in isolation, always plotting and scheming. But now I fear he has lost his mind.
            - **Ali the Wise:** His actions do seem to indirectly benefit Zaros, but if he really is loyal he will have some serious explaining to do.
            - (other)
          - [Choice]: Are you in contact with Zaros?
            - **Ali the Wise:** Unfortunately my lord has not seen fit to contact me, no. He keeps his communication to an absolute minimum, choosing only to liaise with Azzanadra.
            - **Ali the Wise:** I do not take it personally, though. He must keep his communication routes hidden, and his plans even more so.
            - **Ali the Wise:** I can feel him watching, adventurer.
            - (Condition: If the player has not yet completed Fate of the Gods:)
              - **Ali the Wise:**It will not be long before he makes his return.
              - (continue)
            - (other)
          - [Choice]: Will you try and obtain the Stone of Jas?
            - **Ali the Wise:** I have no interest in the power the Stone of Jas provides. I leave the hunger for ascension to the Zamorakians. So blinded by their own selfish needs...
            - **Ali the Wise:** If Zaros expresses a need for the stone, I will of course commit my focus to obtaining it. Perhaps it will factor into my plans.
            - (Condition: If the player has not yet completed Fate of the Gods:)
              - **Ali the Wise:** For now though I prepare for the Empty Lord's return. He still has many followers who will rally to his side.
              - (continue)
            - (other)
      - [Choice]: Why did you deceive me?
        - **Player:** I'm not sure what to make of you. You deceived me, pretended to know nothing of Mahjarrat and had me gathering 'research' for you, but...at the ritual...
        - **Player:** I... I don't think I'd still be here if not for your assistance.
        - **Ali the Wise:** And I apologise for my earlier deception. Us Mahjarrat are in a weakened state as the ritual approaches, and I did not initially know where your allegiances were.
        - (Condition: If the player sided with the cultists in Hazeel Cult:)
          - **Ali the Wise:** You helped to revive Hazeel in time for the ritual, which gave me cause for concern.
          - (continue)
        - **Ali the Wise:** But then I heard how you bloodied Khazard's nose, which tickled me some.
        - **Ali the Wise:** Then, if not for your actions, neither Azzanadra or Akthanakos would have been at the ritual.
        - **Ali the Wise:** And from your working with Azzanadra, it soon became clear that I too could trust you. I only kept up my ruse for the benefit of your comrades.
        - **Player:** What of Jhallan? It was because of me that he was hidden beneath the ritual site, that he was such easy pickings.
        - **Ali the Wise:** No, Jhallan's vulnerability was his own doing, and his alone. He always avoided conflict where he could.
        - **Ali the Wise:** His power was wasted and is better shared among those of us who persist.
        - **Ali the Wise:** And besides, the loss of Lucien is a huge blow to the lapdogs of Zamorak. They'll be reeling from that one for centuries!
        - **Player:** That's if we're not all wiped out by the Dragonkin first.
        - **Ali the Wise:** Yes, that was a worrying turn of events...but do not forget your own history, Player. This is not the first time a Mahjarrat has misused the Stone of Jas; the Dragonkin have been here before.
        - **Ali the Wise:** And yet life goes on...
        - (previous)
      - [Choice]: About the strange power...
        - **Player:** About the strange power...
        - **Ali the Wise:** You mean the wave of power you felt when Jhallan was sacrificed, and when Lucien too met his end?
        - **Ali the Wise:** When one of our kind dies, all that they were dissipates from their body. During planetary alignment, that energy is channeled through our ritual marker into any Mahjarrat who are nearby.
        - **Player:** But I've felt that power before, and it happened across all of Gielinor!
        - **Ali the Wise:** Ah, you speak of the Daemonheim event.
        - **Ali the Wise:** A case of the wrong Mahjarrat being in the wrong place at the wrong time...
        - **Ali the Wise:** Such a waste of power.
        - (previous)
      - [Choice]: So, what do we know about the Mahjarrat?
        - **Ali the Wise:** Well of course you now I am myself a Mahjarrat, but I'm happy to remind you of what you know of us.
        - **Ali the Wise:** We are powerful with a strong aptitude for magic including the ability to change our form and look like other creatures. There are a number of Mahjarrat active in the world.
        - **Ali the Wise:** Jhallan, who you helped to hibernate in the north, was weaker then most Mahjarrat. He was sacrificed at the last ritual.
        - (Condition: If Hazeel was revived:)
          - **Ali the Wise:** Hazeel is faithful to Zamorak. The cult in Ardougne have revived him, though he's rather weak. He attended the Rejuvenation Ritual.
          - (continue)
        - (Condition: If Hazeel wasn't revived:)
          - **Ali the Wise:** Hazeel, who has a following in Ardougne. The cult are trying to revive him, and are faithful to Zamorak.
          - (continue)
        - **Ali the Wise:** There is Zemouregal, who controls many zombies, Zemouregal seems to have a penchant for attacking Varrock. He controlled the great hero Arrav, but we put a stop to that.
        - **Ali the Wise:** He was also present at the death of Guthix in an unsuccessful effort to kill Guthix in the name of Zamorak.
        - **Ali the Wise:** Enakhra is a female Mahjarrat and a follower of Zamorak. She is a rival of Akthanakos, who is a follower of Zaros.
        - **Ali the Wise:** Enakhra also tried to kill Guthix in order to gain favour with Zamorak, but she did not succeed in her plan.
        - **Ali the Wise:** There is General Khazard, who owns territory around Port Khazard and the Fight Arena.
        - **Ali the Wise:** There is Azzanadra, who you freed from a pyramid he was trapped in and who then taught you how to use a lot of useful magic.
        - **Ali the Wise:** Later in your travels, you met Azzanadra again. He was disguised so that he could restore the Zarosian temple under the Digsite without arousing too much suspicion.
        - **Ali the Wise:** Once the temple was complete it formed a communication link between Azzanadra and Zaros.
        - **Ali the Wise:** So, although Zaros has not physically returned, he is able to command those loyal to him once again. It seems the stage is set for a rather dramatic act, no?
        - **Ali the Wise:** You also met Azzanadra at the death of Guthix. He was proposing to wake Guthix, with the other Zarosians.
        - **Ali the Wise:** There was Lucien, who was looking particularly dangerous and powerful, even for a Mahjarrat. First, he gained control of the Staff of Armadyl and then he found the Stone of Jas, which could be the most powerful artefact
        - **Ali the Wise:** known to Gielinor. He had aspirations to become a god, but perished at the claws of the Dragonkin.
        - **Ali the Wise:** There is Sliske, a cunning Mahjarrat who controls a group of wights named the barrows brothers.
        - **Ali the Wise:** He made your friend, Akrisae, one of his wights.
        - **Ali the Wise:** More importantly, you witnessed Sliske killing Guthix. It is possible he gained power from this, but we do not know for sure.
        - **Ali the Wise:** Many Mahjarrat follow the evil god Zamorak. The wiser among us follow Zaros.
      - [Choice]: Never mind.
        - **Player:** Never mind.
  - [Choice]: I'd like to talk about Guthix's death.
    - (Condition: If the player sided with the Guthixians or Saradominists:)
      - **Ali the Wise:** The day the edicts were broken. It is a shame we had to clash; I can only hope in the future you come around to the Zarosian way. You have proved to be a wonderful ally in the past.
      - (continue)
    - (Condition: If the player sided with the Zarosians:)
      - **Ali the Wise:** The breaking of the edicts! How can we forget! And of course you played your part excellently. Until Sliske came along, anyway...
      - (continue)
    - [Menu]: Select an Option
      - [Choice]: What happened with Sliske?
        - **Ali the Wise:** Well, he has always been...different.
        - **Ali the Wise:** He is slippery; always lurking in the shadows. You can never quite be sure what he is intending, but you can always guarantee his actions will either benefit himself or Zaros.
        - **Ali the Wise:** While he betrayed us, he was still working for Zaros. Just in the way he thought best.
        - **Ali the Wise:**  And of course, in the way he felt was the most entertaining. In any case, it is still a good outcome. If not what we had planned.
        - (other)
      - [Choice]: What do you envisage for the future?
        - (Condition: Before Fate of the Gods:)
          - **Ali the Wise:** Zaros' return, of course! With the edicts gone, we can set so much in motion!
          - **Player:** So what's stopping Zaros coming back straight away?
          - **Ali the Wise:** Zaros is intelligent. It is wise to first devise a plan, observe any enemies, calculate the risks...
          - (continue)
        - (Condition: After Fate of the Gods:)
          - **Ali the Wise:** I have to say that I do not know. Perhaps it is time that I checked in with Azzanadra again.
          - (continue)
        - (other)
      - [Choice]: What do you think of Saradomin's return?
        - **Ali the Wise:** What a display that was. Typical Saradomin; always trying to make an impression, show everyone what he can do.
        - **Ali the Wise:** He flaunts his power and leaves himself open.
        - **Ali the Wise:** Wiser gods keep their cards close to their chest; a hidden strength can take an opponent by surprise.
        - **Ali the Wise:** That is why Zaros will have the upper hand.
        - (other)
  - [Choice]: I'd like to talk about Zaros returning.
    - [Menu]: Tell Wahisietel that Zaros is back?
      - [Choice]: Yes
        - **Player:** So...I have some news for you. Which do you want first: good or bad?
        - **Ali the Wise:** Good. Always good.
        - **Player:** Okay, so, I guess you'd think it was good news that...Zaros has returned.
        - **Ali the Wise:** What? Could it really be true, after all this time?
        - **Player:** It is; I was there. In fact, if not for my aid, he'd not have been able to.
        - **Ali the Wise:** Hmm, thanks to your new status as World Guardian, no doubt...
        - **Ali the Wise:** This is very good news indeed. I thank you for the bringing of it.
        - **Ali the Wise:** And the bad news?
        - **Player:** Sliske has been excommunicated - he's no longer a loyal supporter of Zaros.
        - **Ali the Wise:** That's hardly news, let alone bad news!
        - **Ali the Wise:** How was Zaros?
        - (Condition: If the player helped Zaros:)
          - **Player:** He's strong - returned to his former glory. I made sure of that.
          - (continue)
        - (Condition: If the player sabotaged Zaros:)
          - **Player:** He's weak. I'm sure you'd think that's bad news...
          - **Wahisietel:** Well, at least he is returned.
          - (continue)
        - **Ali the Wise:** I do wonder why it is that I am finding this out from you, however.
        - **Player:** Azzanadra didn't tell you the plan?
        - **Ali the Wise:** He did not... I must contact him about this.
        - **Ali the Wise:** I'm sure he has his reasons
        - (Condition: If the player is telling Wahisietel for the first time:)
          - **Ali the Wise:** I give you knowledge, in exchange for the knowledge you gave me...
          - (receives=Large prismatic lamp (Fate of the Gods))
          - Wahisietel hands you a reward lamp.
      - [Choice]: No
        - **Player:** Actually, never mind.

### I have more information about the Mahjarrat


#### Enakhra's Lament

- **Player:** I encountered a pair of Mahjarrat called Enakhra and Akthanakos. Enakhra had imprisoned Akthanakos in the form of a creature called a "boneguard". The imprisonment spell seemed to require her constant supervision, though. I ended up breaking the deadlock and now they say they're headed to the north to continue their fight there.
- **Ali the Wise:** Why would they be heading to the north before resuming their fight, I wonder? I guess it's something to do with the ritual. It seems unusual that they were embroiled in such a fight outside the Ritual, anyway.
- **Player:** Apparently they've always been rivals, but it seems they also had religious differences. Enakhra is a follower of Zamorak and Akthanakos follows a god called Zaros.
- **Ali the Wise:** A Mahjarrat following Zaros? Interesting.
- **Player:** So, you've heard of Zaros?
- **Ali the Wise:** Yes, there are some reference to him in ancient texts that I have run across. From what I gather, he once had followers who were fiercely loyal to him; what has become of him now, I don't know.

#### Defender of Varrock

- **Player:** A Mahjarrat called Zemouregal tried to invade Varrock with an army of zombies!
- **Ali the Wise:** Ooh, can you tell me more? That's big enough news that rumours of it have already been circulating down here.
- **Player:** Yes, his army was led by an ancient hero Arrav, who Zemouregal had managed to enslave. A man named Dimintheis managed to defeat the zombie army with an artefact called the Shield of Arrav. Oh, and I helped quite a lot, if I do say so myself.

#### Temple of Ikov


##### Aiding the Guardians

- **Player:** I met a strange person called Lucien - I believe he was a Mahjarrat. He certainly looked similar to Jhallan. He was trying to steal a powerful artefact called the 'Staff of Armadyl'. He wasn't actually all that strong, I managed to just about defeat him in combat, but he escaped before I could finish him off.
- **Ali the Wise:** Hmm, this is quite interesting. From what I've heard of Mahjarrat, I wouldn't have expected him to be such a weak foe. I guess the fact it's not long until the Ritual means they are weakening a bit.
- **Player:** It doesn't seem to have stopped him getting up to some mischief, though.
- **Ali the Wise:** The Staff of Armadyl, you say? I've heard of Armadyl; an obscure deity from around the Third Age. Very interesting that a Mahjarrat would be after an artefact attributed to him. Sounds like it might be powerful.
- (Condition: If the player obtained the Armadyl communiqué:)
  - **Player:** Unfortunately, I've heard that Lucien has managed to capture the Staff of Armadyl despite my efforts. A message I received indicates a mage called Movario obtained it for him.
  - **Ali the Wise:** I'm not sure of all the implications of this. That could be a powerful artefact. We're going to need to keep an eye out for this Lucien fellow now.

##### Aiding Lucien

- **Player:** I met a strange person called Lucien - I believe he was a Mahjarrat. I helped him steal an artefact called 'the staff of Armadyl".
- **Ali the Wise:** You did what! Are you sure that's the sort of thing that's sensible to go around doing?
- **Player:** I'm an adventurer. I do quests. He was prepared to give me a quest. I did the quest.
- **Ali the Wise:** I've heard of Armadyl, an obscure deity from around the Third Age. If a Mahjarrat was after an artefact attributed to Armadyl, we can be sure it's powerful. I'm not sure what all the implications of what you've done are, but we're going to keep a eye out for this Lucien fellow now.

#### The Curse of Zaros

- **Player:** I've managed to find out more about the Staff of Armadyl. I'm told Zamorak used it to defeat Zaros and become a god himself.
- **Ali the Wise:** It's really that powerful? Does it mean that Lucien is trying to follow in Zamorak's footsteps and become a god? Who knows what chaos would come to pass if that were to happen.

#### The General's Shadow

- **Player:** I've run into General Khazard in the Shadow Realm. I think he's a Mahjarrat.
- **Ali the Wise:** You were in the Shadow Realm? Goodness me, how did you manage to get there?
- **Player:** I guess I've picked up a lot of useful bits and pieces on my adventures.
- **Ali the Wise:** Did you find out anything of interest from him?
- **Player:** Yes, he was sending this message to his followers: "The planets are nearing alignment; we will meet in the place of half light and ice soon. Beware of the others, for though they are weak and few, they are cunning." Mean anything to you?
- **Ali the Wise:** Hmmm...I'm not sure exactly. I guess the place of half light and ice could be the Ritual area. The bit about the planets aligning is interesting.

#### Desert Treasure

- **Player:** I inadvertently freed a being called Azzanadra from a pyramid to the west of here.
- (Condition: If the player has not completed The Curse of Arrav:)
  - **Ali the Wise:** That name sounds familiar. Is he a Mahjarrat?
  - **Player:** I think he might be.
  - (continue)
- (Condition: If the player has completed The Curse of Arrav:)
  - **Ali the Wise:** That name was on the list of Mahjarrat in Zemouregal’s notes. Have you let another Mahjarrat loose on the world?
  - **Player:** Yes, I think I might have.
  - (continue)
- **Ali the Wise:** So, what was he like? Was he another conniving and evil follower of Zamorak?
- **Player:** Well, now you come to mention it, he wasn't a follower of Zamorak and he was actually rather helpful. He taught me a bunch of new spells. I'm still not convinced he's entirely trustworthy, but he didn't seem all that bad either.
- **Ali the Wise:** It's all very interesting. You know it does increasingly seem that not all these Mahjarrat are completely evil. Not to the extent some people would have you believe, anyway. There does seem to be a bit of a mix of personality types, like with many other races.

#### Hazeel Cult

- **Player:** I've found out about a slain Mahjarrat named Hazeel. There's a whole cult dedicated to reviving him in Ardougne.
- **Ali the Wise:** So this cult is helping the Mahjarrat?
- **Player:** Yes, they said they're faithful to Lord Zamorak, and seem to be in awe of the Mahjarrats' power.
- **Ali the Wise:** It's fascinating how people of a particular nature flock to power.
- (Condition: If the player aided the cult:)
  - **Player:** I actually managed to infiltrate the cult. I saw Hazeel in the flesh!
  - **Ali the Wise:** But...you said he'd been slain!
  - **Player:** It turns out he wasn't dead, just in a state very near death.
  - **Player:** The cult was successful in reviving him, though he seemed very weak.
  - **Ali the Wise:** This Hazeel, is he still in Ardougne?
  - **Player:** No, he said he was heading north where he'd regain his strength.
  - **Ali the Wise:** North, up to the ritual site, I dare say. So, Jhallan isn't the only Mahjarrat in dire need of rejuvination{{Sic}}.

#### While Guthix Sleeps

- **Player:** Lucien has managed to get hold of another artefact. From what I can tell, it's quite a bit more powerful than the Staff of Armadyl - it's called 'The Stone of Jas'
- **Ali the Wise:** The Stone of Jas? That sounds highly unlikely.
- **Player:** You've heard of it?
- **Ali the Wise:** Yes, I've seen passing references to it in some old texts I've read. I doubt it's real though.
- **Player:** I can assure you it's very real. I touched it with my own hand before the Mahjarrat ran off with it.
- **Ali the Wise:** Well, this is very frightening news. Who knows what havoc the Mahjarrat will be able to wreak. I shall have to ponder on this.

#### The Curse of Arrav


##### Stone Tablets

- **Player:** I've found some interesting stone tablets in those tunnels written by a Mahjarrat named Lamistard.
- **Ali the Wise:** Let's see them, then.
- **Ali the Wise:** Now these look interesting. Hmmm, let's see...
- **Ali the Wise:** Yes, this is interesting. It seems that Jhallan wasn't the only one trying to get near the Ritual area by other methods. It does really seem attending the Ritual is critical to their power. It looks like this guy might have come to a sticky end.

##### Zemouregal's Notes

- **Player:** I've found these notes about many different Mahjarrat, made by Zemouregal.
- Ali starts to read the notes.
- **Ali the Wise:** These really do look interesting - there's so much information here! There are more Mahjarrat in the world than most people think. All sorts of Mahjarrat I've never heard of mentioned. Bilrach, Kharshai - look, there are even details of Mahjarrat who have recently perished. Remarkable. It looks like there's a clear split between those who follow Zamorak and those who follow Zaros.

#### The Temple at Senntisten

- **Player:** Dr Nabanik, who you met at the Varrock Dig Site, was actually Azzanadra in disguise. I helped him restore a ruined Zarosian temple under the the site.
- **Ali the Wise:** Varrock Dig Site... That's where the Zarosian city of Senntisten once stood.
- **Player:** When Zaros was banished long ago, Azzanadra used the temple to communicate with him. With the temple in ruins, the link was broken.
- **Ali the Wise:** That explains why Azzanadra's Nabanik persona seemed to be obsessed with Varrock Dig Site. But you say the temple is now restored?
- **Player:** Yes, and with the temple restored, Azzanadra and Zaros can communicate once more.
- **Ali the Wise:** How intriguing! I take it Zaros is still banished, but I wonder how long he will remain so.

#### The World Wakes

- **Player:** At the death of Guthix, I met many Mahjarrat.
- **Player:** Azzanadra, Akthanakos and Wahisietel were there, representing Zaros.
- **Player:** Zemouregal and Enakhra were both there, fighting for Zamorak.
- **Player:** Throughout this, Sliske was lurking in the shadows. He approached me when I entered Guthix's chambers and said he wanted to just wake Guthix, but he deceived everyone and killed Guthix himself.
- **Ali the Wise:** Fascinating. The death of Guthix will have implications for the future; perhaps these Mahjarrat will see their gods return.
- **Ali the Wise:** And I cannot help but wonder what will happen to Sliske. It is rumoured that someone who kills a god can gain great power, but it is not fully understood.

### What do we know so far?

- **Player:** So what information do we have compiled so far?
- **Ali the Wise:** The Mahjarrat are powerful creatures with a strong aptitude for magic including the ability to change their form and look like other creatures. There are a number of Mahjarrat active in the world.
- **Ali the Wise:** Jhallan, who you helped hibernate in the north, seems much weaker than I'd expect the Mahjarrat to be. You spoke of a Rejuvenation Ritual, perhaps he was not present at the last ritual.
- (Condition: If Hazeel was revived:)
  - **Ali the Wise:** You told me of Hazeel, who is faithful to Lord Zamorak. The cult in Ardougne have revived Hazeel, though he's rather weak, and he's headed north. Presumably for the Rejuvenation Ritual.
  - (continue)
- (Condition: If Hazeel wasn't revived:)
  - **Ali the Wise:** You told me of Hazeel, who has a following in Ardougne. The cult are trying to revive him, and are faithful to Lord Zamorak
  - (continue)
- **Ali the Wise:** There is Zemouregal, who controls many zombies, including the once great hero Arrav. Zemouregal seems to have a penchant for attacking Varrock.
- **Ali the Wise:** Enakhra is a female Mahjarrat and follower of Zamorak. She is a rival of Akthanakos, who is a follower of Zaros.
- **Ali the Wise:** There's General Khazard, who is currently wandering the Shadow Realm.
- **Ali the Wise:** There is Azzanadra, who you freed from a pyramid he was trapped in and who then taught you how to use a lot of useful magic. Later in your travels, you met Azzanadra again. He was disguised so that he could restore the Zarosian temple under the Digsite without arousing too much suspicion. Once the temple was complete it formed a communication link between Azzanadra and Zaros. So, although Zaros has not physically returned, he is able to command those loyal to him once again. It seems that the stage is set for a rather dramatic act, no?
- **Ali the Wise:** There is Lucien, who is now looking particularly dangerous and powerful, even for a Mahjarrat. First, he gained control of the Staff of Armadyl and now he has the Stone of Jas, which could be the most powerful artefact known to Gielinor. It's possible he even has aspirations to become a god.
- **Ali the Wise:** There are many more Mahjarrat with names like Bilrach, Kharshai, Sliske and Wahisietel. Some more powerful than others. Many seem to follow the evil god Zamorak. Others seem to follow another, more obscure god of debatable alignment called Zaros.
- **Ali the Wise:** They all seem to be preparing for a forthcoming Ritual, where one of them will be killed.

#### With Ritual of the Mahjarrat started and The World Wakes completed

- **Player:** So, what do we know of the Mahjarrat?
- **Ali the Wise:** Well of course now you know I am myself a Mahjarrat, but I'm happy to remind you of what you know of us.
- **Ali the Wise:** We are powerful with a strong aptitude for magic including the ability to change our form and look like other creatures. There are a number of Mahjarrat active in the world.
- **Ali the Wise:** Jhallan, who you helped to hibernate in the north, was weaker than most Mahjarrat. He was not present at the last ritual.
- (Condition: If Hazeel was revived:)
  - **Ali the Wise:** Hazeel is faithful to Lord Zamorak. The cult in Ardougne have revived Hazeel, though he's rather weak, and he's headed north, presumably for the Rejuvenation Ritual.
  - (continue)
- (Condition: If Hazeel wasn't revived:)
  - **Ali the Wise:** You told me of Hazeel, who is faithful to Lord Zamorak. The cult are trying to revive him, and are faithful to Lord Zamorak
  - (continue)
- **Ali the Wise:** There is Zemouregal, who controls many zombies, including the once great hero Arrav. Zemouregal seems to have a penchant for attacking Varrock. He was also present at the death of Guthix in an unsuccessful effort to kill Guthix in the name of Zamorak.
- **Ali the Wise:** Enakhra is a female Mahjarrat and follower of Zamorak. She is a rival of Akthanakos, who is a follower of Zaros. Enakhra also tried to kill Guthix in order to gain favour with Zamorak, but she did not succeed in her plan.
- **Ali the Wise:** There is General Khazard, who owns territory around Port Khazard and the Fight Arena.
- **Ali the Wise:** There is Azzanadra, who you freed from a pyramid he was trapped in and who then taught ou how to use lot a of useful magic. Later in your travels, you met Azzanadra again. He was disguised so that he could restore the Zarosian temple under the digsite without arousing too much suspicion. Once the temple was complete it formed a communication link between Azzanadra and Zaros. So, although Zaros has not physically returned, he is able to command those loyal to him once again. It seems that the stage is set for a rather dramatic act, no? You also met Azzanadra at the death of Guthix. He was proposing to wake Guthix, with the other Zarosians.
- **Ali the Wise:** There is Lucien, who is looking particularly dangerous and powerful, even for a Mahjarrat. First, he gained control of the Staff of Armadyl and now he has the Stone of Jas, which could be the most powerful artefact known to Gielinor. It's possible he even has aspirations to become a god.
- **Ali the Wise:** There is also Sliske. A mysterious Mahjarrat who killed Guthix. It is possible he may have gained power from this, but we do not know for sure.
- **Ali the Wise:** Many Mahjarrat follow the evil god Zamorak. The wiser among us follow Zaros.
<!---==After Ritual of the Mahjarrat==
- **Player:** Ali. Or should I call you Wahisietel now?
- **Ali the Wise:** Either will suffice.
  - **Player:** Why did you deceive me?
    - **Player:** I'm not sure what to make of you. You deceived me, pretended to know nothing of Mahjarrat and had me gathering 'research' for you, but...at the ritual... I... I don't think I'd still be here if not for your assistance.
    - **Ali the Wise:** And I apologise for my earlier deception. Us Mahjarrat are in a weakened state as the ritual approaches, and I did not initially know where your allegiances were. You helped to revive Hazeel in time for the ritual, which gave me cause for concern *(cultist side*). But then I heard how you bloodied Khazard's nose, which tickled me some. Then, if not for your actions, neither Azzanadra or Akthanakos would have been at the ritual. And from your working with Azzanadra, it soon became clear that I too could trust you. I only kept up my ruse for the benefit of your comrades.
    - **Player:** What of Jhallan? It was because of me that he was hidden beneath the ritual site, that he was such easy pickings.
    - **Ali the Wise:** No, Jhallan's vulnerability was his own doing, and his alone. He always avoided conflict where he could. His power was wasted and is better shared among those of us who persist. And besides, the loss of Lucien is a huge blow to the lapdogs of Zamorak. They'll be reeling from that one for centuries!
    - **Player:** That's if we're not all wiped out by the Dragonkin first.
    - **Ali the Wise:** Yes, that was a worrying turn of events...but do not forget your own history, Player. This is not the first time a Mahjarrat has misused the Stone of Jas; the Dragonkin have been here before. And yet life goes on...
  - **Player:** About the strange power...
    - **Ali the Wise:** You mean the wave of power you felt when Jhallan was sacrificed, and when Lucien too met his end? When one of our kind dies, all that they were dissipates from their body. During planetary alignment, that energy is channeled through our ritual marker into any Mahjarrat who are nearby.
    - **Player:** But I've felt that power before, and it happened across all of Gielinor!
    - **Ali the Wise:** Ah, you speak of the Daemonheim event. A case of the wrong Mahjarrat being in the wrong place at the wrong time... Such a waste of power.
  - **Player:** So, what do we know of the Mahjarrat?
    - **Ali the Wise:** Well of course you now I am myself a Mahjarrat, but I'm happy to remind you of what you know of us.
    - **Ali the Wise:** We are powerful with a strong aptitude for magic including the ability to change our form and look like other creatures. There are a number of Mahjarrat active in the world.
    - **Ali the Wise:** Jhallan, who you helped to hibernate in the north, was weaker then most Mahjarrat. He was sacrificed at the last ritual.
    - (Condition: If Hazeel was revived:)
      - **Ali the Wise:** Hazeel is faithful to Zamorak. The cult in Ardougne have revived him, though he's rather weak. He attended the Rejuvenation Ritual.
      - (continue)
    - (Condition: If Hazeel wasn't revived:)
      - **Ali the Wise:** Hazeel, who has a following in Ardougne. The cult are trying to revive him, and are faithful to Zamorak.
      - (continue)
    - **Ali the Wise:** There is Zemouregal, who controls many zombies, Zemouregal seems to have a penchant for attacking Varrock. He controlled the great hero Arrav, but we put a stop to that. He was also present at the death of Guthix in an unsuccessful effort to kill Guthix in the name of Zamorak.
    - **Ali the Wise:** Enakhra is a female Mahjarrat and a follower of Zamorak. She is a rival of Akthanakos, who is a follower of Zaros. Enakhra also tried to kill Guthix in order to gain favour with Zamorak, but she did not succeed in her plan.
    - **Ali the Wise:** There is General Khazard, who owns territory around Port Khazard and the Fight Arena.
    - **Ali the Wise:** There is Azzanadra, who you freed from a pyramid he was trapped in and who then taught you how to use a lot of useful magic. Later in your travels, you met Azzanadra again. He was disguised so that he could restore the Zarosian temple under the Digsite without arousing too much suspicion. Once the temple was complete it formed a communication link between Azzanadra and Zaros. So, although Zaros has not physically returned, he is able to command those loyal to him once again. It seems the stage is set for a rather dramatic act, no? You also met Azzanadra at the death of Guthix. He was proposing to wake Guthix, with the other Zarosians.
    - **Ali the Wise:** There was Lucien, who was looking particularly dangerous and powerful, even for a Mahjarrat. First, he gained control of the Staff of Armadyl and then he found the Stone of Jas, which could be the most powerful artefact known to Gielinor. He had aspirations to become a god, but perished at the claws of the Dragonkin.
    - **Ali the Wise:** There is Sliske, a cunning Mahjarrat who controls a group of wights named the barrows brothers. He made your friend, Akrisae one of his wights. More importantly, you witnessed Sliske killing Guthix. It is possible he gained power from this, but we do not know for sure.
    - **Ali the Wise:** Many Mahjarrat follow the evil god Zamorak. The wiser among us follow Zaros.

### After The World Wakes

- **Player:** I'd like to talk about Guthix's death.
  - (Condition: If the player sided with the Guthixians or to kill Guthix:)
    - **Ali the Wise:** The day the edicts were broken. It is a shame we had to clash; I can only hope in the future you come around to the Zarosian way. You have proved to be a wonderful ally in the past.
  - (Condition: If the player sided with the Zarosians:)
    - **Ali the Wise:** The breaking of the edicts! How can we forget! And of course you played your part excellently. Until Sliske came along, anyway...
  - **Player:** What happened with Sliske?
    - **Ali the Wise:** Well, he has always been...different. He is slippery; always lurking in the shadows. You can never quite be sure what he is intending, but you can always guarantee his actions will either benefit himself or Zaros. While he betrayed us, he was still working for Zaros. Just in the way he thought best. And of course, in the way he felt was the most entertaining. In any case, it is still a good outcome. If not what we had planned.
  - **Player:** What do you envisage for the future?
    - **Ali the Wise:** Zaros' return, of course! With the edicts gone, we can set so much in motion!
    - **Player:** So what's stopping Zaros coming back straight away?
    - **Ali the Wise:** Zaros is intelligent. It is wise to first devise a plan, observe any enemies, calculate the risks...
  - **Player:** What do you think of Saradomin's return?
    - **Ali the Wise:** What a display that was. Typically Saradomin; always trying to make an impression, show everyone what he can do. He flaunts his power and leaves himself open. Wiser gods keep their cards close to their chest; a hidden strength can take an opponent by surprise. That is why Zaros will have the upper hand.

### After Missing, Presumed Death

- **Player:** I'd like to ask about what happened at the Empyrean Citadel.
  - (Condition: If the player declared support for Zaros:)
    - **Ali the Wise:** I was happy to learn you supported the Empty Lord while debating with the gods. I'm sure he is aware of your deeds.
    - **Ali the Wise:** Sliske may be acting recklessly, but at least you remained calm and dedicated to Zaros
  - (Condition: If the player declared support for another faction:)
    - **Ali the Wise:** Mmm. I was most displeased to learn you did not support Zaros, (player name). I expected more of you.
  - **Player:** Do you still see Sliske as a Zarosian?
    - **Ali the Wise:** I do not. That snake has betrayed us for the last time. After murdering Guthix I was disappointed in him, but now I have lost all hope.
    - **Ali the Wise:** It has always been his way to act alone; spending his days in isolation, always plotting and scheming. But now I fear he has lost his mind.
    - **Ali the Wise:** His actions do seem to indirectly benefit Zaros, but if he really is loyal he will have some serious explaining to do.
  - **Player:** Are you in contact with Zaros?
    - **Ali the Wise:** Unfortunately my lord has not seen fit to contact me, no. He keeps his communication to an absolute minimum, choosing only to liaise with Azzanadra.
    - **Ali the Wise:** I do not take it personally though. He must keep his communication routes hidden, and his plans even more so.
    - **Ali the Wise:** I can feel him watching, adventurer. It will not be long before he makes his return.
  - **Player:** Will you try and obtain the Stone of Jas?
    - **Ali the Wise:** I have no interest in the power the Stone of Jas provides. I leave the hunger for ascension to the Zamorakians. So blinded by their own selfish needs...
    - **Ali the Wise:** If Zaros expresses a need for the stone, I will of course commit my focus to obtaining it. Perhaps it will factor into my plans.
    - **Ali the Wise:** For now though I prepare for the Empty Lord's return. He still has many followers who will rally to his side.

### After Fate of the Gods

- **Player:** I'd like to talk about Zaros returning
  - [Menu]: Tell Wahisietel that Zaros is back?
    - [Choice]: Yes
      - **Player:** So...I have some news for you. Which do you want first: good or bad?
      - **Ali the Wise:** Good. Always good.
      - **Player:** Okay, so, I guess you'd think it was good news that...Zaros has returned.
      - **Ali the Wise:** What? Could it really be true, after all this time?
      - **Player:** It is; I was there. In fact, if not for my aid, he'd not have been able to.
      - **Ali the Wise:** Hmm, thanks to your new status as World Guardian, no doubt...
      - **Ali the Wise:** This is very good news indeed. I thank you for the bringing of it.
      - **Ali the Wise:** And the bad news?
      - **Player:** Sliske has been excommunicated - he's no longer a loyal supporter of Zaros.
      - **Ali the Wise:** That's hardly news, let alone bad news!
      - **Ali the Wise:** How was Zaros?
        - (Condition: If the player helped Zaros:)
          - **Player:** He's strong - returned to his former glory. I made sure of that.
        - (Condition: If the player sabotaged Zaros:)
          - **Player:** He's weak. I'm sure you'd think that's bad news...
          - **Wahisietel:** Well, at least he is returned.
      - **Ali the Wise:** I do wonder why it is that I am finding this out from you, however.
      - **Player:** Azzanadra didn't tell you the plan?
      - **Ali the Wise:** He did not... I must contact him about this.
      - **Ali the Wise:** I'm sure he has his reasons
      - **Ali the Wise:** I give you knowledge, in exchange for the knowledge you gave me...
      - (receives=large prismatic lamp)
      - Wahisietel hands you a reward lamp.
    - [Choice]: No
      - **Player:** Actually, never mind.

#### Guthix's death

*(Only one line of dialogue is changed.)*
- **Player:** What do you envisage for the future?
  - **Ali the Wise:** I have to say that I do not know. Perhaps it is time I checked in with Azzanadra again.--->

### Treasure Trails

- **Ali the Wise:** I see you're on the right track!
- (Condition: If the trail continues:)
  - (removes=the old clue scroll (master)) (receives= the new clue scroll (master))
  - [You've found another clue!]
- (Condition: If the trail ends:)
  - (removes=the old clue scroll (master)) (receives=reward casket (master))
  - [You've found a casket!]
Category:Mahjarrat
