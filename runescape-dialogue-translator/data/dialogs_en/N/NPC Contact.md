# NPC Contact

- **Original Wiki Page**: [Transcript:NPC Contact](https://runescape.wiki/w/Transcript%3ANPC%20Contact)
- **Letter**: `N`

---

## Dialogue Transcript


### Tooltip

{{Spell tooltip|
<poem>
Telepathically speak with a selection of useful NPCs.
</poem>
}}

### Non-random NPC dialogue


#### Honest Jimmy

- **Player:** Hello?
- **Honest Jimmy:** Huh, who's there?
- **Player:** It's Player. I'm using my magick to communicate to you. Don't worry.
- (Condition: If you are nearby:)
  - **Honest Jimmy:** I figured, seeing as I can see you over there! I don't make deals like this.
- (Condition: If you are not nearby:)
  - **Honest Jimmy:** The sooner you get out of my head the better. So, you here for the...information?
  - **Player:** The information?
  - **Honest Jimmy:** Look pal, you interrupted me for a reason, you must be after something.
  - [Menu]: Select an option.
    - [Choice]: How much time till the next game of Trouble Brewing starts?
      - **Player:** How much time till the next game of Trouble Brewing starts?
      - **Honest Jimmy:** Ah, that's information I can help yer with.
      - **Honest Jimmy:** A game is ready to start just as soon as there are enough people.
      - **Player:** And how many people are there?
      - **Honest Jimmy:** There are X people on Dan's team, and Y on San's. There needs to be three on each in order for a game to start.
      - **Player:** Oh, okay. Thanks.
      - **Honest Jimmy:** Anything else?
      - (initial)
    - [Choice]: How many people are waiting for a game to start?
      - **Player:** How many people are waiting for a game to start?
      - (Condition: If no one is waiting:)
        - **Honest Jimmy:** No one's waiting at the moment. Perhaps you can get some people interested.
        - **Player:** Hmmm...maybe.
        - (initial)
      - (Condition: If there are players waiting:)
        - {{Transcript missing}}
    - [Choice]: I have no idea what you're talking about.
      - **Player:** I have no idea what you are talking about.
      - **Honest Jimmy:** Then sling yer 'ook!

#### Bert

- **Player:** Hi there, Bert.
- **Bert:** Huh? What tha' doin' in marn 'ed?
- **Player:** This is the voice of your conscience. Hand all your money to Player! Wooo wooo!
- **Bert:** Be away wit' ya!
- **Player:** Just kidding, I'm using magic to talk to you. I'm totally 'armless.
- (Condition: If you are nearby (in the Dragon Inn):)
  - **Bert:** Oh ar. Hey, then why ya standon' so close? Speak in person please!
- **Bert:** Oh ar. So wha' do thee want?
- **Player:** Could you hand some sand into my bank?
- (Condition: If you have not collected sand for the day:)
  - **Bert:** Ah, keep yer 'air on, I'll leg I' to tha bank wit' some sand fer ya.
  - **Player:** Thanks!
- (Condition: If you have already collected sand for the day:)
  - **Bert:** I be a wee bi' busy to 'elp wit' yon sand, come back tomorra.
  - **Player:** Okay, Bert, I'll come back for my sand a bit later on.

#### Advisor Ghrim

- **Player:** Good day, Ghrim!
- **Advisor Ghrim:** What? Who is this?
- **Player:** Aha, you've gone crazy, Ghrim. I am your alternate personality...Ghrom!
- (Condition: If you are nearby:)
  - **Advisor Ghrim:** Very amusing, your Royal Highness. I can see you talking.
  - **Player:** Oops.
- (Condition: If you are not nearby:)
  - **Advisor Ghrim:** Is that you, your Royal Highness?
  - **Player:** Er...yes, it is. I'm using magic to communicate with you.
  - **Advisor Ghrim:** Very amusing, your Royal Highness. How may I help you?
  - [Menu]: Select an option
    - [Choice]: How is the kingdom faring?
      - (see|Advisor Ghrim)
    - [Choice]: How do I manage the kingdom?
      - (see|Advisor Ghrim)
    - [Choice]: About the task System:...
      - (see|Advisor Ghrim)
    - [Choice]: That's all, thanks.
      - **Player:** That's all, thanks.
      - **Advisor Ghrim:** Very well, your Royal Highness. If you have any further problems, pleas talk to me in person.

#### Turael/Spria


##### Turael (before & during While Guthix Sleeps)

- **Player:** Hello?
- **Turael:** 'Ello, who's that?
- **Player:** I'm Player. I'm using magic to communicate with you.
- **Turael:** Bizarre. Go on then, what do you want?
- [Menu]: Choose an option:
- (Condition: During While Guthix Sleeps before recruiting Turael:)
  - [Choice]: I need to talk to you about Lucien.
    - **Player:** I need to talk to you about Lucien!
    - **Turael:** Oh, yes, and what about Lucien? I haven't heard that name in a while.
    - **Player:** He's growing in power and we need to apprehend him. Would you be interested in joining a small party tasked with doing so?
    - **Turael:** I've spent the last few years telling amateurs to kill goblins. Excitement and danger sounds like just the ticket before I quit the job forever.
    - **Player:** Great news Turael, many thanks!
  - [Choice]: Ask about something else
    - [Choice]: I need another assignment.
      - **Player:** I need another assignment.
      - (Condition: If player already has a Slayer assignment:)
        - **Turael:** You're still hunting [assigned creature]; come back when you've finished your task.
  - [Choice]: Er... Nothing...
    - **Player:** Er... Nothing...
- (Condition: After recruiting Turael (While Guthix Sleeps))
  - **Player:** I need to talk to you about Lucien!
  - **Turael:** You seem very forgetful, really. You have already recruited me, there's no point trying again.
  - (end)
(Condition: If Player is in close proximity with Turael)
- **Player:** Hello?
- **Turael:** 'Ello, who's that?
- **Player:** I'm Player. I'm using magic to communicate with you.
- **Turael:** Well, please don't. If you want to talk to me, do it face to face. I can see you, you know.
- (end)

##### Spria (after While Guthix Sleeps)

- **Player:** Hello?
- **Spria:** 'Ello, who's that?
- **Player:** I'm Player. I'm using my magic to communicate with you.
- (Condition: If you are nearby:)
  - **Spria:** Well, please don't. If you want to talk to me, do it face to face. I can see you, you know.
- (Condition: If you are not nearby:)
  - **Spria:** Bizarre. Go on then, what do you want?
  - [Menu]: Select an option
    - [Choice]: I need another assignment.
      - (see|Spria#Get task)
    - [Choice]: Er...nothing.
      - (end)

#### Lanthus

- **Player:** Hello, Lanthus
- **Lanthus:** Huh?
- **Player:** Be not afraid! I am the all mighty god of all! Bow down before your creator!
- (Condition: If you are nearby:)
  - **Lanthus:** No you're not. You're standing over there. Leave me alone!
- (Condition: If you are not nearby:)
  - **Lanthus:** Okay, Okay; I'm bowing, I'm bowing. Just don't h-h-hurt me!
  - **Player:** Are you listening to me, Lanthus?
  - **Lanthus:** I...I am. How may I h-h-help you?
  - [Menu]: Select an option
    - [Choice]: How long until another game starts?
      - **Player:** How long until another game starts?
      - **Lanthus:** The n-next game starts in X minute[s]. Sir.
      - **Player:** Very well.
      - **Lanthus:** But why do you want to know that?
      - **Player:** Silence!
      - (initial)
    - [Choice]: How many people are waiting in each room?
      - **Player:** How many people are waiting in each room?
      - (Condition: If the Zamorak room is empty:)
        - **Lanthus:** There's no one in the Zamorak room,
      - (Condition: If the Zamorak room is not empty:)
        - {{Transcript missing}}
      - (Condition: If the Saradomin room is empty:)
        - **Lanthus:** and there's no one in the Saradomin room.
      - (Condition: If the Saradomin room is not empty:)
        - {{Transcript missing}}
      - (initial)
    - [Choice]: That is all. Now keep out of trouble.
      - **Player:** That is all. Now keep out of trouble.
      - **Lanthus:** Y-yes.
      - **Player:** I'm watching you, Lanthus.

#### Sumona

- **Player:** Hello?
- (Condition: If you are nearby:)
  - **Sumona:** 'Ello, who's that?
  - **Player:** I'm Player. I'm using my magic to communicate with you.
  - **Sumona:** Well, please don't. If you want to talk to me, do it face to face. I can see you, you know.
- (Condition: If you are not nearby:)
  - **Sumona:** 'Ello, Player.
  - **Player:** I'm using magic to communicate with you.
  - [Menu]: Select an option
    - [Choice]: I need another assignment.
      - (see|Sumona#After_Smoking_Kills)
    - [Choice]: Er...nothing.
      - (end)

#### Mazchna/Achtryn


##### Mazchna (before/after While Guthix Sleeps)

- **Player:** Hello?
- **Mazchna:** 'Ello, who's that?
- **Player:** I'm Player. I'm using magic to communicate with you.
- (Condition: If you are nearby:)
  - **Mazchna:** Well, please don't. If you want to talk to me, do it face to face. I can see you, you know.
- (Condition: If you are not nearby:)
  - **Mazchna:** Bizarre. Go on then, what do you want?
  - [Menu]: Select an option
    - [Choice]: I need another assignment.
      - (see|Mazchna)
    - [Choice]: Er..Nothing.
      - (end)

##### Achtryn (during While Guthix Sleeps)

- {{Transcript missing}}

#### Duradel/Lapalok


##### Duradel (before While Guthix Sleeps)

- {{Transcript missing}}

##### Lapalok (after While Guthix Sleeps)

- **Player:** Hello?
- **Lapalok:** 'Ello, who's that?
- **Player:** I'm Player. I'm using magic to communicate with you.
- (Condition: If you are nearby:)
  - **Lapalok:** Well, please don't. If you want to talk to me, do it face to face. I can see you, you know.
- (Condition: If you are not nearby:)
  - **Lapalok:** Bizarre. Go on then, what do you want?
  - [Menu]: Select an option
    - [Choice]: I need another assignment.
      - (see|Lapalok)
    - [Choice]: Er..Nothing.
      - (end)

#### Vannaka

- **Player:** Hello?
- **Vannaka:** 'Ello, who's that?
- **Player:** I'm Player. I'm using my magic to communicate with you.
- (Condition: If you are nearby:)
  - **Vannaka:** Well, please don't. If you want to talk to me, do it face to face. I can see you, you know.
- (Condition: If you are not nearby:)
  - **Vannaka:** Bizarre. Go on then, what do you want?
  - [Menu]: Select an option
    - [Choice]: I need another assignment.
      - (see|Vannaka)
    - [Choice]: Er...nothing.
      - (end)

#### Murphy

- **Player:** Hello there
- **Murphy:** What the...?
- **Player:** Don't worry, Murphy. My name's Player and I'm using magic to contact you!
- (Condition: If you are nearby:)
  - **Murphy:** That's so rude when you may as well just speak to me in person!
- (Condition: If you are not nearby:)
  - **Murphy:** Well I never! Technology these days. It's beyond me. So how might I help you?
  - **Player:** I was just wondering if there was anyone down there helping you out on the trawler?
  - (Condition: If the boat has left:)
    - **Murphy:** The boat has just left, actually! Perhaps, when it comes back, you can join them on another run?
    - **Player:** Sounds like a plan.
  - (Condition: If the boat has not left:)
    - **Murphy:** The boat is just sitting there, waiting for someone to join. How about it?
    - **Player:** Maybe I'll come have a look. I'll catch you later.
    - **Murphy:** Okay, mate. Bye!

#### Chaeldar

- **Player:** Hello?
- **Chaeldar:** 'Ello, who's that?
- **Player:** I'm Player. I'm using my magic to communicate with you.
- (Condition: If you are nearby:)
  - **Chaeldar:** Well, please don't. If you want to talk to me, do it face to face. I can see you, you know.
- (Condition: If you are not nearby:)
  - **Chaeldar:** Bizarre. Go on then, what do you want?
  - [Menu]: Select an option
    - [Choice]: I need another assignment.
      - (see|Chaeldar)
    - [Choice]: Er..Nothing.
      - (end)

#### Cyrisus

- {{Trandom}}
  - ''Conversation 1:
    - **Player:** Hello mate. What are you up to now?
    - **Cyrisus:** Erm, I'm a bit busy at the moment.
    - **Player:** Oooh, I bet you're travelling the seas. Or maybe you're visiting world leaders?
    - **Cyrisus:** Well, I'm trying to fight TzTok-Jad at the moment.
    - **Player:** He must be really tough!
    - **Cyrisus:** Yes, he's got a combat level of 702.
    - **Player:** Enjoy!
    - **Cyrisus:** Thanks. Arghhhh, death to you, foul beast!
  - ''Conversation 2:
    - **Player:** Hello!
    - **Cyrisus:** Oh, hi.
    - **Player:** What adventure are you now on?
    - **Cyrisus:** Well, I just dispatched TzTok-Jad. Pretty tough! I'm now on my way to the desert. I'm going to see if I can hunt down this Kalphite Queen everyone's been telling me about.
    - **Player:** I should warn you, you'll need a team to take that beast on.
    - **Cyrisus:** I've already thought of that. I've arranged for a couple of the slayer masters to join me.
    - **Player:** Wow! I wish I could witness that!
  - ''Conversation 3:
    - **Player:** Hello again!
    - **Cyrisus:** That's funny, I was just talking about you.
    - **Player:** You were?
    - **Cyrisus:** Yes, I've been arranging various leaders of Runescape to discuss some political issues. It seems you've certainly been around a bit!
    - **Player:** I suppose I have. What issues are you suppose to discuss in this meeting? Who will be there?
    - **Cyrisus:** Sorry, that's top secret information.
    - **Player:** That's fine, I understand.
  - ''Conversation 4:
    - **Player:** Hi there, where are you now?
    - **Cyrisus:** I am in the Clan Wars free-for-all arena: the one with the pretty red portal. I'm meeting lots of interesting people.
    - **Player:** Oh? That's a funny place to meet people.
    - **Cyrisus:** Well, I thought that too, but this guy told me to bring all my most valuable items and follow him in there to meet his friends.
    - **Player:** Um, Cyrisus, aren't you afraid that they might kill you so that you lose all your stuff?
    - **Cyrisus:** Oh yes, they did try that. So I killed all of them instead. But it was very nice to meet them anyway.
    - **Player:** I guess you're fine.
  - ''Conversation 5:
    - **Player:** Hey. How's it going?
    - **Cyrisus:** Summoning, summoning and more summoning!
    - **Player:** Really? Nice one. So what's your choice of a pet at the moment?
    - **Cyrisus:** Dragon!
    - **Player:** No way! I'm so jealous.
    - **Cyrisus:** It's certainly taken a lot of hard work, but it's very much worthwhile!
    - **Player:** I'll bet!

#### Eluned

- (Condition: If you have an uncharged Crystal teleport seed in your inventory:)
  - (opens=Crystal teleport seed#Charges)
- (Condition: If you do not have an uncharged Crystal teleport seed in your inventory (or it is partially charged):)
  - **Eluned:** Player? Do you wish me to re-enchant crystal teleport seeds for you?
  - **Player:** I haven't got any of those.
  - **Eluned:** Perhaps another time.

#### Larry/Chuck


##### Larry (before Hunt for Red Raktuber)

- {{Transcript missing}}

##### Chuck (after Hunt for Red Raktuber)

- **Player:** Hello there.
- **Chuck:** Greetings, voice in my head.
- **Player:** I wanted to talk to you about the penguin spies all over the world.
- **Chuck:** What about them?
- [Menu]: Select an option
  - [Choice]: I've found more penguins.
    - **Player:** I've found more penguins.
    - **Chuck:** More? Hmm, interesting. How many have you found?
    - **Player:** I've found X penguin[s] this week.
      - (Condition: If you haven't found all the penguins this week:)
        - [Menu]: Select an option
          - [Choice]: I'm having trouble finding the penguins. Can I have a hint?
            - '' (One of the following is shown, depending on the location of the penguins:)
              - **Chuck:** I've heard there's a penguin located around a village between a great tower and a vampyre's manor.
              - **Chuck:** I've heard there's a penguin located around Ardougne
              - **Chuck:** I've heard there's a penguin located around Feldip Hills, near Gu'Tanoth
              - **Chuck:** I've heard there's a penguin located around the Al Kharid region, north of Shantay Pass
              - **Chuck:** I've heard there's a penguin located around the Ice Mountain region
              - **Chuck:** I've heard there's a penguin located between the Fremenniks and the Barbarians
              - **Chuck:** I've heard there's a penguin located deep in the jungle
              - **Chuck:** I've heard there's a penguin located east of the Mage Training Arena
              - **Chuck:** I've heard there's a penguin located in a city of plagues within the desert
              - **Chuck:** I've heard there's a penguin located in a town of druids
              - **Chuck:** I've heard there's a penguin located in or around Falador
              - **Chuck:** I've heard there's a penguin located in the east of the kingdom of Kandarin
              - **Chuck:** I've heard there's a penguin located in the fairy realm
              - **Chuck:** I've heard there's a penguin located in the frozen wastes
              - **Chuck:** I've heard there's a penguin located in the north of the Kharidian desert
              - **Chuck:** I've heard there's a penguin located in the north of the kingdom of Misthalin
              - **Chuck:** I've heard there's a penguin located in the south of the Kharidian desert
              - **Chuck:** I've heard there's a penguin located in the south of the kingdom of Misthalin
              - **Chuck:** I've heard there's a penguin located in the west of the kingdom of Kandarin
              - **Chuck:** I've heard there's a penguin located in the wilderness
              - **Chuck:** I've heard there's a penguin located near a big tree surrounded by short people
              - **Chuck:** I've heard there's a penguin located near a mountain of wolves
              - **Chuck:** I've heard there's a penguin located near a tainted swamp
              - **Chuck:** I've heard there's a penguin located near a town of werewolves
              - **Chuck:** I've heard there's a penguin located near Port Sarim
              - **Chuck:** I've heard there's a penguin located near some ogres in South Feldip Hills
              - **Chuck:** I've heard there's a penguin located near the Barbarian Outpost
              - **Chuck:** I've heard there's a penguin located near the bees and flax
              - **Chuck:** I've heard there's a penguin located near the Castle of Arthur
              - **Chuck:** I've heard there's a penguin located near the city of ghosts
              - **Chuck:** I've heard there's a penguin located near the coast, east of Ardougne
              - **Chuck:** I've heard there's a penguin located near the island of Dragontooth
              - **Chuck:** I've heard there's a penguin located near the mudskippers
              - **Chuck:** I've heard there's a penguin located near the pointy-eared ones
              - **Chuck:** I've heard there's a penguin located north of Ardougne
              - **Chuck:** I've heard there's a penguin located on a large crescent island
              - **Chuck:** I've heard there's a penguin located on an island, etc
              - **Chuck:** I've heard there's a penguin located on islands where brothers quarrel
              - **Chuck:** I've heard there's a penguin located somewhere beyond detection
              - **Chuck:** I've heard there's a penguin located somewhere in Gielinor
              - **Chuck:** I've heard there's a penguin located south of Ardougne
              - **Chuck:** I've heard there's a penguin located west of Ardougne, in the hills
              - **Chuck:** I've heard there's a penguin located west of Varrock
              - **Chuck:** I've heard there's a penguin located where banana smugglers dwell
              - **Chuck:** I've heard there's a penguin located where bloodsuckers rule
              - **Chuck:** I've heard there's a penguin located where eagles fly
              - **Chuck:** I've heard there's a penguin located where fishers colonise
              - **Chuck:** I've heard there's a penguin located where monkeys rule
              - **Chuck:** I've heard there's a penguin located where no weapons may go
              - **Chuck:** I've heard there's a penguin located where pirates feel mostly harmless
              - **Chuck:** I've heard there's a penguin located where the big-eyed goblins dwell
              - **Chuck:** I've heard there's a penguin located where the dwarves dig deep
              - **Chuck:** I've heard there's a penguin located where the Fremennik 'heim' and seek
              - **Chuck:** I've heard there's a penguin located where the Imperial Guard train
              - **Chuck:** I've heard there's a penguin located where wizards study
  - [Choice]: I'm having trouble find the penguins. Can I have a hint?
    - (above)
  - [Choice]: Never mind.
    - **Player:** Never mind.

#### Kuradal

{{Incomplete|Requires dialogue for if you interrupt her during a bad time, such as while a monster tries to escape the dungeon}}
- **Player:** Hello?
- **Kuradal:** 'Ello, who's this?
- **Player:** It's Player. I'm using my magic to communicate with you.
- (Condition: If you are nearby:)
  - **Kuradal:** What a waste of runes. I can see you, you know. Let's talk face to face.
- (Condition: If you are not nearby:)
  - **Kuradal:** A useful application of magical talent. How can I help?
  - [Menu]: Select an option
    - [Choice]: I need another assignment.
      - (see|Kuradal)
    - [Choice]: Er..Nothing.
      - (end)

#### Dark Mage

- **Player:** Hello?
- **Dark Mage:** What is this?! You must not break my concentration!
- **Player:** It's Player. I'm using my magic to communicate with you.
- (Condition: If you are nearby:)
  - **Dark Mage:** What a waste of runes! - I can see you, lets talk face to face.
- (Condition: If you are not nearby:)
  - **Dark Mage:** Are you trying to collapse the Abyss? What do you want? Speak quickly!
  - (Condition: If the Abyssal book is in your inventory or bank:)
    - **Player:** Actually, I can't think of anything right now...
    - **Dark Mage:** THEN STOP DISTRACTING ME!
    - **Dark Mage:** Honestly, you have no idea of the pressure I am under attempting to keep this portal open!
  - (Condition: If the Abyssal book is not in your inventory or bank:)
    - **Player:** Sorry to disturb you. I just needed your help with something quickly.
    - **Dark Mage:** What? Oh... Very well. what did you want?
    - [Menu]: Chose an option:
      - [Choice]: Can I have another Abyssal book?
        - **Player:** Can I have another Abyssal book? I seem to have misplaced the one I was given.
        - **Dark Mage:** Here, take it, it is important to pool our research. Now leave me be, I must concentrate!
        - (receives=Abyssal book)
      - [Choice]: Actually, I can't think of anything right now...
        - **Player:** Actually, I can't think of anything right now...
        - **Dark Mage:** THEN STOP DISTRACTING ME!
        - **Dark Mage:** Honestly, you have no idea of the pressure I am under attempting to keep this portal open!

#### Pikkupstix

- **Player:** Hello?
- **Pikkupstix:** Ahh, a familiar voice in my head!
- [Menu]: Select an option
  - [Choice]: So, where's Pikkenmix?
    - (see|Pikkupstix)
  - [Choice]: What's it all about?
    - (see|Pikkupstix)

#### Pauline Polaris

- **Player:** Hi Pauline!
- **Pauline Polaris:** Bah! You made me jump! I suppose you want to claim some reward wishes?
- **Player:** Yes please.
- (opens=Livid_Farm#Rewards)

#### Oneiromancer

- **Player:** Oneiromancer!
- **Oneiromancer:** What? Ah, very bright of you contacting me this way.
- **Player:** Yeah, thought I'd make use of the new spell to ask a question.
- [Menu]: Select an option
  - [Choice]: Can you change my spell book back to the standard one?
    - (Condition: If you have not completed the elite achievement diary tasks:)
      - **Oneiromancer:** Hmmm, no I think you need to prove yourself a bit more first.
      - If you complete the elite achievement diary tasks the Oneiromancer will help you.
    - (Condition: If you have completed the elite achievement diary tasks:)
      - **Oneiromancer:** Certainly...
      - **Oneiromancer:** There!
  - [Choice]: Can I tell you a joke?
    - **Oneiromancer:** Oh, I do like jokes, go ahead.
    - **Player:** What do you call a crazy moon?
    - **Oneiromancer:** A crazy moon... Hmm, I don't know. What?
    - **Player:** A luna-tic!
    - **Oneiromancer:** Ahahahaha!
    - **Oneiromancer:** Hahaa!
    - **Oneiromancer:** Hahahaha!
    - **Player:** Okay, okay. It wasn't THAT funny.

#### Islwyn

- (Condition: If you have an uncharged Crystal teleport seed in your inventory:)
  - (opens=Crystal teleport seed#Charges)
- (Condition: If you do not have an uncharged Crystal teleport seed in your inventory (or it is partially charged):)
  - **Islwyn:** Player? Do you wish me to re-enchant crystal teleport seeds for you?
  - **Player:** I haven't got any of those.
  - **Islwyn:** Perhaps another time.

#### Mieliki Tapio

- **Mieliki Tapio:** Mieliki sent Nyriki to a swamp, south-east of Canifis.
- [Menu]: What would you like to say?
  - [Choice]: Who are you?
    - **Mieliki Tapio:** Mieliki is an alchemist. Mieliki's stupid husband Nyriki hunts for giant chinchompas to get chemicals for Mieliki.
    - **Mieliki Tapio:** Nyriki needs human help because he is stupid. Use Mieliki portal, in this shop, to go to him now.
    - (initial)
  - [Choice]: Can you teleport me?
    - (Condition: If you are nearby:)
      - **Mieliki Tapio:** Mieliki is working! Use the portal.
    - (Condition: If you are not nearby:)
      - **Mieliki Tapio:** Mieliki is working! Come to Mieliki's shop in the Gnome Stronghold and use the portal.
    - (initial)
  - [Choice]: Thanks.
    - **Mieliki Tapio:** Very well, human. Work hard.

#### Morvran

- **Player:** Hello?
- (Condition: If you are nearby:)
  - **Morvran:** If you're going to bother me with your prattle, you could at least have the decency to do it to my face. Get over here.
- (Condition: If you are not nearby:)
  - **Morvran:** You have no business in my head. My secrets are not for your eyes. Get out.
  - **Player:** It's Player. I'm using my magic to communicate with you.
  - **Morvran:** Too scared to seek me out in person, hmm? Well, what is it?
  - [Menu]: Select an option
    - [Choice]: I need another assignment.
      - (see|Morvran)
    - [Choice]: Er..Nothing.
      - (end)

#### Urluk

- (see|Urluk)

#### Laniakea

- **Player:** Laniakea?
- (Condition: If you are nearby:)
  - **Laniakea:** Why would you waste the runes to contact me when you're standing so close?
- (Condition: If you are not nearby:)
  - **Laniakea:** You have no business in my head. My thoughts are my own.
  - **Plyer:** It's Player. I'm using my magic to communicate with you.
  - **Laniakea:** That's a shame. It'd have been nice to see you. Well, what is it?
  - [Menu]: Select an option
    - [Choice]: I need another assignment.
      - (see|Laniakea)
    - [Choice]: Er..Nothing.
      - (end)

#### Polletix


##### Before speaking to her at Garden of Kharid

- **Player:** Hello?
- **Polletix:** Ugh, another one.
- **Player:** What?
- **Polletix:** Oh nothing. What can I help with?
- **Player:** Oh, well, someone said something about some druids in the desert, and rather than go there I figured I'd see what was going on first.
- **Polletix:** Look, if you want to help, maybe come and have a chat rather than pushing your way into my head.
- **Player:** Well I did-
- **Polletix:** Good day!
- **Player:** Hello?
- **Player:** Helloooo?
- There is no one there but the cold, dark void of your own mind.

##### After speaking to her at Garden of Kharid and asked to farm herbs

- **Player:** Hello, Polletix?
- (Condition: If you are nearby:)
  - **Polletix:** What are you doing?
  - **Player:** Well I was jus-
  - **Polletix:** I can see you. You're right here.
  - **Player:** Oh, I-
  - **Polletix:** Now, if you want to talk I suggest you come and do so in person, rather than this misuse of magic.
- (Condition: If you are not nearby:)
  - **Polletix:** Hello adventurer. This is a nifty little trick. How can I help?
  - **Player:** I was just wondering what herb you wanted planted today?
  - **Polletix:** Oh, today I'd like you to plant and harvest: [Herb type] seed.
  - **Player:** Great, thanks!

#### The Raptor

- **Player:** Hello? is this the Raptor?
- **The Raptor** You have no business in my head. My thoughts are my own.
- **Player:** It's Player. I'm using my magic to communicate with you.
- **The Raptor** Explain yourself.
  - [Menu]: Select an option
    - [Choice]: I need another assignment.
      - (see|The Raptor)
    - [Choice]: Er..Nothing.
      - (end)

### Random NPC dialogue


#### Lumbridge Sheep

- **Player:** Hello?
- **Lumbridge Sheep:** Baaaa.
- **Player:** Huh? Okay.
- **Player:** Baa, baaaa, BAA!
- **Lumbridge Sheep:** Baaa?

#### Lumbridge Sage

- **Player:** Hello!
- **Lumbridge Sage:** What? Who's that?
- **Player:** Hehe...ahem...
- **Player:** This is the voice of your conscience! You've been a very naughty boy, haven't you?
- **Lumbridge Sage:** What? No I haven't!
- **Player:** You know what I'm talking about! Don't lie!
- **Lumbridge Sage:** Okay, okay! I'm sorry, I'll never do it again.
- **Player:** If you do it again, you'll be in deep trouble.

#### Wise Old Man

- **Player:** Hello.
- (The player is hit by a Fire Wave spell, but takes no damage.)
- **Player:** Ow!
- **Wise Old Man:** Keep your foreign magicks out of my head!

#### My Arm


##### Before completing My Arm's Big Adventure

- **Player:** Hi there.
- **My Arm:** Voice in my head?
- **Player:** Huh?
- **My Arm:** Go away voice, leave My Arm.
- **Player:** Now that's the most weird conversation I've had in a long time.

##### After completing My Arm's Big Adventure

- **Player:** Hi there.
- **My Arm:** Is dat you, Player? My Arm can hear you but you not here.
- **Player:** I'm using magic to talk to you. How's the goutweed?
- **My Arm:** Sorry, Player, but My Arm not know magic, so My Arm no can reply.

#### Hans

- **Player:** Hiya.
- **Hans of Lumbridge:** Oooh! Who are you?
- **Player:** I'm a brave knight! I am coming to kill anyone in the vicinity of Lumbridge Castle!
- **Hans of Lumbridge:** Aaaaargh! Run away, run away!
- **Player:** Hehe. Fool!

#### Evil Dave

- **Player:** Hallo!
- **Evil Dave:** Whoa! A voice in my head! What do you want?
- **Player:** I am your evil master!
- **Evil Dave:** You're using dark magic to contact me! That is SO evil! What is thy bidding, O Master?
- **Player:** Build me an army worthy of Zamorak!
- **Evil Dave:** Yes, O master! As soon as I get this summoning thing to work, my army of evil UNDEAD CHAOS ZOMBIE DEMON ASSASSINS OF DARKNESS will overrun the world! Mwuhahahahaaa!

#### Clay Golem

- **Player:** Hello!
- **Clay Golem:** Error! Perception mismatch (auditory/visual).
- **Player:** Don't worry, Golem! It's Player!
- **Clay Golem:** I am sorry. I can hear you but not see you. I will have to examine my eyes.
- **Player:** No, you can't see me because I'm not there. I'm contacting you by magic!
- **Clay Golem:** If you are not here then I cannot be hearing you. I will have to examine my ears.
- **Player:** Don't worry about it, Golem.

#### General Wartface

- **Player:** Hello!
- **General Wartface:** What you want, Bentnoze?
- **General Wartface:** ...
- **General Wartface:** Then who did say something? Who that?
- **Player:** It's Player! I'm talking to you by magic!
- **General Wartface:** Hello, Player!
- **General Wartface:** Bentnoze, [he/she] is here! I hear [him/her] in head!
- **General Wartface:** ...
- **General Wartface:** Me not crazy, Bentnoze! [He/She] talk to me by magic!
- **General Wartface:** ...
- **General Wartface:** You shut up Bentnoze! You stupid! You just jealous Player talk to me not you!
- **General Wartface:** ...
- **General Wartface:** Shut up Bentnoze! You stupid!
- **General Wartface:** ...
- **General Wartface:** SHUT UP!

#### Drunken Dwarf

- **Player:** Howdy.
- **Drunken Dwarf:** Waaahaaay! It's Player! *hic* Maate!
- **Player:** How's things?
- **Drunken Dwarf:** I fink oiv drunk a bit toooo much.
- **Player:** So, same as always.
- **Drunken Dwarf:** Wont a kebab?
- **Player:** Uh, no, I'm good, thanks.
- **Drunken Dwarf:** Well, oym goona pass owt now. Have one on me!
- **Player:** Oh, okay.
- **Player:** ...
- **Player:** Erm, bye.

#### Al Kharid Camel

- **Player:** Hi there!
- **Al Kharid Camel:** Why, helloooo!
- **Player:** A camel?
- **Al Kharid Camel:** Well this is grand, darling. How nice it is to make your acquaintance!
- **Player:** Thank you. Nice to meet you too.
- **Player:** Wait a minute. How am I talking to you without a camulet?
- **Al Kharid Camel:** My dear, I'm a camel; how should I know?
- **Player:** Hmmm. I suppose this spell must tap directly into your mind, so there's no need for language to get in the way.
- **Al Kharid Camel:** I think I am somewhat confused.
- **Al Kharid Camel:** May one ask how you contacted me?
- **Player:** I'm just using one of the Lunar spells.
- **Al Kharid Camel:** Oh my, oh my. These youngsters today and their new-fangled gadgets!

#### Sandwich Lady

- **Player:** Hello?
- **Sandwich Lady:** What do ya want for tea? And it better not be a baguette!
- **Player:** ...
- **Player:** ... ...
- **Sandwich Lady:** Don't ignore me, Player!
- **Player:** ...
- **Sandwich Lady:** Why won't people talk to me?
- **Player:** ...
- **Sandwich Lady:** I'll beat you up!
- **Player:** Uhh, urr, a sandwich please?
- **Sandwich Lady:** Okay, then, my dear! Toodle-oo!

#### 1337mage43

- **Player:** Hello?
- **1337mage43:** Hello?
- **Player:** Hey, I started the conversation!
- **1337mage43:** No you didn't. Get out of my spell!
- **Player:** No! Get out of my spell!
- **1337mage43:** Cry-baby.
- **Player:** What! I'm no cry-baby, you cry-baby!
- **1337mage43:** I'm reporting you!
- **Player:** Oh, how scary!
- **Player:** Idiot.

#### Osman

- **Player:** Hello?
- **Osman:** Reveal yourself!
- **Player:** Ha, call yourself a spymaster! You can't see me!
- **Osman:** Ahh, I'm hallucinating! Must cut back on sq'irks!

#### Helpline Assistant

- **Player:** Hello?
- **Helpline Assistant:** You have reached the Lunar Communication Helpline. I'm sorry we can't answer your telekinetic question right now. Our opening times are carefully organised to coincide with you being busy. If you are having an emergency, you have
- **Helpline Assistant:** our most profound apologies. Have a nice day. Goodbye.
- **Player:** Typical.

#### Father Urhney

- **Player:** Hello?
- **Father Urhney:** At last! The voice of Saradomin! My years of meditation have paid off!
- **Player:** Um...
- **Father Urhney:** O mighty Saradomin! What is your message to me?
- **Player:** Stop sitting around in a house in a swamp and go and do something useful!
- **Father Urhney:** Oh, thank you Saradomin! I will meditate on what this message means!

#### Romeo (historical)

- **Player:** Hello?
- **Romeo:** Oh, hello. You sound lovely.
- **Player:** Sorry?
- **Romeo:** You sound lovely. You have a beautiful...twang to your voice.
- **Player:** Twang? It's Romeo, isn't it?
- **Romeo:** May I compare thee to some pineapple chunks?
- **Player:** No, Romeo. Goodbye.

#### Blurberry

- **Player:** Hello?
- **Blurberry:** Blurberry here! Can I help?
- **Player:** Hehe. Yes you can. I'm looking for a Gnome. Gnome Mates.
- **Blurberry:** Okay, I'll ask. Everybody shush! Is there a Gnome Mates here? Did anyone come in with Gnome Mates?
- You hear laughter in the background.
- **Blurberry:** Ooooh, who is this? I'll get you!
- **Player:** Hahaha.

#### Aris

- **Player:** Hello.
- **Aris:** Because I can tell the future.
- **Player:** Um?
- **Aris:** That is the answer to your next question.
- **Player:** But how did you know what I would ask?
- **Aris:** Because I can tell the future.
- **Player:** Ah, that's very clever.
- **Aris:** Thanks. Oh - and be careful in the Wilderness. Tonight is not your night.
- **Player:** Cheers!

#### Hakeem the Sandsweeper

- **Player:** Hello there! Who is this?
- **Hakeem:**  Hakeem.
- **Player:** Hakeem who?
- **Hakeem:** I'm Hakeem the Sandsweeper.
- **Player:** You sweep sand?
- **Hakeem:** Certainly do! I'm the best darn sandsweeper this side of the Lum.
- **Player:** There's more of you?
- **Hakeem:** We have a union, mate! There's always sand to sweep.
- **Player:** Indeed. Um, I have to go.

#### Man

- **Player:** Hello.
- **Man:** Excuse me!
- **Player:** Oh sorry, what did I do?
- **Man:** Can't you see I'm on the toilet?
- **Player:** Wait a minute...a toilet?
- **Man:** Yeah. A toilet.
- **Player:** Riiiight. Oh, man, you didn't wipe your hands?
- **Man:** Get over it.
- (Condition: If contacting the man on the toilet for the first time:)
  - {{RSFontAchievement|Is This a Bad Time?}}

#### Party Pete

- **Player:** Hello?
- **Party Pete:** Yo! Party, party, party!
- **Player:** Um, Party Pete?
- **Party Pete:** Yeah! Party's the name, and partying is the game! Actually it's a full-time profession. You can't stop the party.
- **Player:** Party Pete. Do you ever want to just relax?
- **Party Pete:** Relax, don't do it! Yeah! Party mania! Yeah!
- **Player:** Bye, Party.
- **Party Pete:** You may leave the party, but the party never leaves you! Party!

#### Bob

- **Player:** Hello?
- **Bob:** Hello.
- **Player:** Ah, Bob! I've been meaning to ask you some questions
- **Bob:** Okay, but be quick.
- **Player:** Well, where did you come from? Why do you wander around Gielinor? I've heard lots of rumours about your past!
- **Bob:** It's simple really...
- **Bob:** *cough* *cough*.
- **Player:** Are you okay?
- **Bob:** *cough* I'm *cough* just...
- **Player:** Bob?
- **Player:** Bob! Don't die! Noooooo!
- **Player:** ...
- **Bob:** Sorry, I had a hairball.
- **Player:** Euw! That's nasty.
- **Bob:** Hey, it's normal. I'm off now!
- **Player:** Bob?
- **Player:** Oh no, Bob, please don't go.
- **Bob:** Goodbye.

#### Captain Cain

- **Player:** Who's that?
- **Captain Cain:** What? Such insolence! How dare you speak like that, you poor excuse for goblin-dribble!
- **Player:** What?
- **Captain Cain:** Drop and give me twenty!
- **Player:** Okay, okay. I'm doing them now.
- **Player:** ...
- **Captain Cain:** Liar!
- **Player:** Wait a minute, I don't have to put up with this. You do twenty!
- **Captain Cain:** Why I oughtta!
- **Player:** Erm, yeah. Bye!

#### Homunculus

- **Player:** Hello?
- **Homunculus:** It's Player. How are you?
- **Player:** Fine, thanks. How about you?
- **Homunculus:** Alchemists return the other day. Me turn them into animals.
- **Player:** No! Really?
- **Homunculus:** Yeah, me made a uniman and a chickalchemist!
- **Player:** Nice work!

#### KGP Agent #1

- **Player:** Anyone there?
- **KGP Agent:** INTRUDER! Red alert! Batten down the hatches! DIVE, DIVE, DIVE!
- **Player:** Err, maybe I'll call back later.

#### KGP Agent #2

- **Player:** Hello.
- **KGP Agent:** The fish cannot ride the gravy train.
- **Player:** Sorry?
- **KGP Agent:** The cyclops cannot see his inner walrus?
- **Player:** Is this code?
- **KGP Agent:** Waddle into a sunset of flaking mackerel?
- **Player:** I'm going now.
- **KGP Agent:** The sardine is leaving the tin?

#### Lumbridge Cow

- **Player:** Hello?
- **Lumbridge Cow:** Moooooo.
- **Player:** Hey, I know you can talk!
- **Lumbridge Cow:** Moooo.
- **Player:** Stop ignoring me!
- **Lumbridge Cow:** Look, mate. Leave me alone!
- **Player:** You talked! You talked!
- **Lumbridge Cow:** Moooo.
- **Player:** I think I'll have some beef tonight.

#### Zanik (before The Mighty Fall)

- {{Trandom}}
  - ''Conversation 1:
    - **Player:** Hello?
    - **Zanik:** Player?
    - **Player:** I'm contacting you by magic!
    - **Zanik:** Hey Player, do you know someone named Evil Dave? He's telling me about his plan for world domination, but I'm not sure if he's being serious.
    - [Menu]: Select an option
      - [Choice]: He's an evil wizard! You've got to stop him!
        - **Player:** He's an evil wizard! You've got to stop him!
        - **Zanik:** Okay, I've got this.
        - **Zanik:** Stop right now, Evil Dave! If you want to conquer the world you'll have to get past me first!
        - **Zanik:** He's casting a spell, Player! He's made a magic circle and he's going to summon something! I have to disrupt the magic somehow!
        - [Menu]: Select an option
          - [Choice]: Make him get the words wrong!
            - {{Transcript missing}}
          - [Choice]: Disrupt the magic circle!
            - **Player:** Disrupt the magic circle!
            - **Zanik:** There! The circle's broken! Something is still happening, though...
            - **Zanik:** Evil Dave has turned into a fish! He's flopping around and-
            - **Zanik:** Oh, he's turned back.
            - **Zanik:** He says he's going to go and have a lie down. I think his evil plans are foiled for the time being.
          - [Choice]: Just let him cast the spell
            - {{Transcript missing}}
      - [Choice]: I think he's harmless.
        - **Player:** I think he's harmless.
        - **Zanik:** Really? He's asking me to join his evil scheme. He says I could be his 'Evil Death-Bringer Assassin of Darkness'.
        - [Menu]: Select an option
          - [Choice]: You'd make a great assassin of darkness.
            - **Player:** You'd make a great assassin of darkness.
            - **Zanik:** Ha! I bet I would. I'd stand on a rooftop, wrapped in a black cloak, a crossbow bolt glinting in the moonlight as my target moved unsuspecting below...
            - **Zanik:** Um, if I were evil, of course.
            - **Zanik:** Which I'm not.
            - **Zanik:** I think I've hung around with Evil Dave for long enough. I'll talk to you some other time, Player.
          - [Choice]: You're not going to join him, are you?
            - **Player:** You're not going to join him, are you?
            - **Zanik:** Of course not. You won't catch me being part of any evil scheme!
            - **Zanik:** Well, except that one time, of course. But I don't want to talk about that.
            - **Zanik:** Anyway, I think I should leave Evil Dave to his schemes. I'll see you around, Player.
  - ''Conversation 2:
    - **Player:** Hello?
    - **Zanik:** Player? Oldak, something's happening. I've got Player in my head.
    - **Player:** I'm contacting you by magic.
    - **Zanik:** Um, okay. Hey Player, do you know what an 'abyssal doom vortex' is?
    - **Zanik:** Because that's what Oldak says he's created in his lab.
    - **Zanik:** It's kind of getting larger, I think it's going to explode.
    - [Menu]: Select an option
      - [Choice]: Run away!
        - **Player:** Run away!
        - **Zanik:** Okay! Oldak! Grubfoot! Let's get out of here!
        - **Zanik:** Grubfoot!
        - **Zanik:** Grubfoot's stuck under a thing. I'm going back for him.
        - **Zanik:** Oh no!
        - ...
        - **Zanik:** I've ended up somewhere else. The walls are red...I think this is the abyss.
        - **Zanik:** I can see a portal out, but there are some monsters between it and me.
        - [Menu]: Select an option
          - [Choice]: You should fight them.
            - **Player:** You should fight them.
            - **Zanik:** Okay, I haven't got my crossbow, but I'm got a dagger. Here goes...
            - **Zanik:** There! They weren't as tough as they looked. I've reached the portal.
            - **Zanik:** I'm home! And Grubfoot is fine. That's a relief.
            - **Zanik:** Okay, I'm going to help Oldak clean up the mess. I'll see you around, Player.
          - [Choice]: You should sneak past them.
            - {{Transcript missing}}
      - [Choice]: You need to shut it down!
        - **Player:** You need to shut it down!
        - **Zanik:** Yeah, that's what I was thinking.
        - **Zanik:** Hey, Oldak, Player thinks you should shut it down!
        - **Zanik:** Oh no! Oldak!
        - **Zanik:** Oldak's paralysed!
        - **Zanik:** I can't remember how to shut it down! What did Oldak say? It was either de-align the rune injector, or reverse to polarity on the polarity reverser.
        - [Menu]: Select an option
          - [Choice]: De-align the injector!
            - **Player:** De-align the injector!
            - **Zanik:** Okay! Here goes...
            - **Zanik:** It worked! It's shut off! But it's left this red gunk all over the floor.
            - **Zanik:** Oldak is scraping some of it into a sample jar. A very interesting result, he says.
            - **Zanik:** Anyway, that looks like the end of that abyssal doom vortex. I'll see you around Player.
          - [Choice]: Reverse the polarity!
            - **Player:** Reverse the polarity!
            - **Zanik:** Okay, I'm turning this part the other way round...
            - **Zanik:** Wow...
            - **Zanik:** That's the most amazing...it's...indescribable...
            - **Player:** What was it? What happened?
            - **Zanik:** I can't describe it! It's literally indescribable!
            - **Zanik:** Anyway, it's gone now.
            - **Zanik:** I think I should leave Oldak and Grubfoot to work. I'll see you around, Player.
  - ''Conversation 3:
    - **Player:** Hello?
    - **Zanik:** Player? Where are you? I can't see you in the swamp.
    - **Player:** I'm contacting you by magic!
    - **Zanik:** Oh! I'm exploring Morytania and...
    - **Zanik:** Whoah! I'm slipping! Wo-o-oah!
    - **Player:** Zanik? Are you alright?
    - **Zanik:** I've fallen in the swamp! What should I do Player?
    - [Menu]: Select an option
      - [Choice]: Grapple out with your crossbow!
        - **Player:** Grapple out with your crossbow!
        - **Zanik:** Okay, I'll try that...
        - **Zanik:** There, the grapple's caught on a tree. I'm climbing out...
        - **Zanik:** I've landed in a bush, and... hey, there's someone else here! Hey! Lumberjack! Over here!
        - **Zanik:** He's turning this way, and... oh. Uh-oh. I think he's a zombie.
        - [Menu]: Select an option
          - [Choice]: Run for it!
            - {{Transcript missing}}
          - [Choice]: You can take it! Fight!
            - **Player:** You can take it! Fight!
            - **Zanik:** It's not so tough!
            - **Zanik:** Its arm's come off, but it's still coming at me!
            - **Zanik:** Now I've cut off both its arms, but it's still trying to bite me!
            - **Zanik:** What? It's hopping at me with just one leg! Why doesn't it die already?
            - **Zanik:** There. I've cut off all its limbs and kicked it in the swamp. No zombie is safe from Zanik of the Dorgeshuun!
            - **Zanik:** I don't think I'll have trouble with anything else in this swamp. Thanks for the help, Player! See you around!
      - [Choice]: Try to swim to the bank!
        - **Player:** Try to swim to the bank!
        - **Zanik:** I think I can do that! The bank is just...
        - **Zanik:** Hey, what's that? There's a head poking out of the water...
        - **Zanik:** Eek! Tentacles! It's got me!
        - [Menu]: Select an option
          - [Choice]: Attack the tentacle!
            - {{Transcript missing}}
          - [Choice]: Attack the head!!
            - **Player:** Attack the head!
            - **Zanik:** I hope that my crossbow's still dry enough...
            - **Zanik:** Haha! Got it! Crossbow bolt in the eye!
            - **Zanik:** It didn't seem to hurt it too much, but it's let me go. I've got back to the bank. I think I can see a way out of the swamp from here.
            - **Zanik:** Thanks for your help, Player! I'll talk to you some other time.

### Redial '[NPC]'

- (Condition: If the player has not dialed an NPC yet:)
  - Last contact not found. Please call again.
  - (popup)
    - {{popup|Last contact not found. <br>Please call again.|warning=yes}}
- (Condition: If the player has dialed an NPC before:)
  - Redialing '[NPC]'...
  - (Condition: Without enough runes:)
    - You do not have enough [rune type] runes to cast this spell.
    - (popup)
      - {{popup|You do not have enough [rune type]<br>runes to cast this spell.|warning=yes}}
  - (Condition: With enough runes:)
    - (removes=runes)
    - (continuea)
