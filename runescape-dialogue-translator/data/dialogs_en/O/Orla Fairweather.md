# Orla Fairweather

- **Original Wiki Page**: [Transcript:Orla Fairweather](https://runescape.wiki/w/Transcript%3AOrla%20Fairweather)
- **Letter**: `O`

---

## Dialogue Transcript


### At the Divination camp


#### Talk to


##### Introduction to Divination


##### First time

- **Player:** What's going on here?
- **Orla Fairweather:** So glad you asked! I'm Orla Fairweather, and these are my colleagues. We're pioneers, researching the art of divination!
- **Player:** Divination? You mean like reading tea leaves, casting bones, that sort of thing?
- **Orla Fairweather:** Oh no, this is much larger! Here, we are dealing with the energy of the world! The fate of Gielinor may be determined by our actions!
- **Player:** Wow - that does sound interesting.
- **Orla Fairweather:** Oh yes. It's early days, but we've had exciting results already.
- (Condition: Before collecting a memory:)
  - **Player:** Can I start training divination myself?
  - (continue)
- (Condition: After collecting a memory:)
  - **Player:** Can you help me improve my skill in divination?
  - (continue)
- **Orla Fairweather:** Of course! We could use all the help we can get!
- (Condition: Before collecting a memory:)
  - (continue|before-collecting-a-memory)
- (Condition: After collecting a memory:)
  - (continue|after-collecting-a-memory)
- (Condition: After converting a memory into experience:)
  - (continue|after-convert-memory-into-experience)
- (Condition: After converting a memory into energy:)
  - (continue|after-convert-memory-into-energy)
- (Condition: After converting a memory and energy into experience:)
  - (continue|after-convert-memory-and-energy)

##### Talking to Orla again before collecting a memory

- **Orla Fairweather:** Are you ready to get started?
- [Menu]: Select an Option
  - [Choice]: Yes, show me how to train divination.
    - {{anchor|before-collecting-a-memory}}**Orla Fairweather:**  The first step is to gather a memory. The wisps to the south will do - see how you get on and come back to me if you need help.
  - [Choice]: Not at the moment, thanks.
    - (end)

##### Talking to Orla after collecting a memory

- **Orla Fairweather:** I think you're ready for the next step! Do you want to continue learning the ways of divination?
- [Menu]: Select an Option
  - [Choice]: Yes!
    - {{anchor|after-collecting-a-memory}}**Orla Fairweather:** You've got some memories, but they're no use to you like that! You need to feed them back to the earth. Give it a go!
  - [Choice]: Not at the moment, thanks.
    - (end)

##### Talking to Orla after converting a memory into experience

- **Orla Fairweather:** At this rate, you'll surpass my knowledge in no time! Are you ready to continue learning?
- [Menu]: Select an Option
  - [Choice]: Yes, please.
    - {{anchor|after-convert-memory-into-experience}}**Orla Fairweather:** As you've seen, memories can be converted into experience, but that's not all they can be used for. If you focus your mind, you can also receive divine energy - a useful material. Why don't you try it?
  - [Choice]: Not at the moment, thanks.
    - (end)

##### Talking to Orla after converting a memory into memory

- **Orla Fairweather:** No time to waste! Are you ready to continue?
- [Menu]: Select an Option
  - [Choice]: Yes!
    - {{anchor|after-convert-memory-into-energy}}**Orla Fairweather:** If you've spare divine energy you can use it to your advantage. Just focus your mind on enhanced experience and you'll get more return from your memories.
  - [Choice]: Not at the moment, thanks.
    - (end)

##### After the introduction to Divination

- {{anchor|after-convert-memory-and-energy}}**Orla Fairweather:** You seem to be up to date with my discoveries. However, Faizan is making breakthroughs with divine energy - you should speak to him.
- [Menu]: Select an Option
  - [Choice]: Okay, I'll speak to Faizan.
    - (end)
  - [Choice]: How can I collect memories? {{anchor|how-to-collect-memories}}
    - (Condition: If the player is below level 10 Divination:)
      - **Orla Fairweather:** First, you need to locate a wisp. The ideal wisps for you are right here, just south of the camp. As you become more skilled in divination, you should move on to more complex wisps.
      - (continue|how-to-collect-memories-2)
    - (Condition: If the player is level 10 Divination or higher:)
      - **Orla Fairweather:** First, you need to locate a wisp. You already have some skill in divination, so it'd be best for you to find a more complex colony than the one we have here.
      - (continue|how-to-collect-memories-2)
    - **Orla Fairweather:{{anchor|how-to-collect-memories-2}}** You can use the map next to me to find out where the most suitable wisps for you are located.
    - **Orla Fairweather:** Interact with a wisp to transform it into a spring and harvest memories from it!
    - **Orla Fairweather:** You'll also get a small amount of divine energy. Hang on to that - it can be used later!
    - [Menu]: Select an Option
      - [Choice]: How can I convert memories?
        - (below|how-to-convert-memories)
      - {{anchor|enriched-memories}}What are enriched memories?
        - **Orla Fairweather:** Enriched memories are particularly strong memories, charged with power.
        - **Orla Fairweather:** If you convert an enriched memory at a crater, you will receive additional experience or energy compared to a normal memory.
        - **Player:** Sounds great! Where can I get them?
        - **Orla Fairweather:** You may receive enriched memories just from harvesting normal wisps, if you're lucky!
        - **Orla Fairweather:** Alternatively, if you keep an eye out, you may spot an enriched wisp floating around a colony. These always give enriched memories when harvested.
        - **Orla Fairweather:** They are unstable, however. If you want one to stick around you'll need to feed it a memory you've harvested previously. Get your friends to do it too - the more people who feed it, the longer it will stay around!
        - **Orla Fairweather:** Finally, bear in mind you'll need to visit the wisps further away from camp. We've never seen any enriched memories from the wisps to the south, or any enriched wisps floating around down there.
        - [Menu]: Select an Option
          - [Choice]: How can I collect memories?
            - (above|how-to-collect-memories)
          - [Choice]: How can I convert memories?
            - (below|how-to-convert-memories)
          - [Choice]: That's all, thanks.
            - (end)
      - [Choice]: That's all I needed to know, thanks.
        - (end)
  - {{anchor|how-to-convert-memories}}How can I convert memories?
    - (Condition: If the player doesn't have a memory in the inventory:)
      - **Orla Fairweather:** Well, you'll need some memories! You remember how to get those, don't you?
      - [Menu]: Select an Option
        - [Choice]: No, please go over that again.
          - (above2|how-to-collect-memories)
        - [Choice]: Yes, I remember.
          - (continue|how-to-convert-memories-2)
    - (Condition: If the player has a memory in the inventory:)
      - **Orla Fairweather:** Well, you've got some memories with you, which is the first step!
      - (continue|how-to-convert-memories-2)
    - **Orla Fairweather:{{anchor|how-to-convert-memories-2}}** You need to take one or more memories to a crater. These can be found near any of the wisp colonies.
    - **Orla Fairweather:** Deposit memories into the crater to receive either additional divination knowledge, or divine energy - something that can be used to create items later on!
    - **Orla Fairweather:** Alternatively, if you have any spare divine energy you can combine that with the memories for additional divination knowledge. We call this 'enhanced' experience.
    - **Orla Fairweather:** To do this, you'll need to throw both a memory and some divine energy into the crater.
    - **Orla Fairweather:** For normal memories, you'll need 5 energy of the same tier as your memory and for enriched memories you'll need 10 lots of energy for the same tier.
      - [Menu]: Select an Option
        - [Choice]: How can I collect memories?
          - (above|how-to-collect-memories)
        - [Choice]: What are enriched memories?
          - (above|enriched-memories)
        - [Choice]: That's all I needed to know, thanks.
          - (end)
  - [Choice]: That's all, thanks.
    - (end)

##### After Faizan Augour's lessons on Divination

- **Orla Fairweather:** A new discovery has been made! Would you like me to show you?
- [Menu]: Select an Option
  - [Choice]: Yes!
    - **Orla Fairweather:** My latest discovery is rather exciting, although unfortunately we haven't been able to observe it in the wisps here.
    - **Orla Fairweather:** In the other colonies, you will occasionally see an enriched wisp, or be particularly successful when harvesting a normal wisp, resulting in you gathering an enriched memory.
    - **Orla Fairweather:** Why don't you see if you can find one!
  - [Choice]: Not at the moment, thanks.
    - (end)

##### After gathering an enriched memory

- **Orla Fairweather:** You've covered everything I know. Faizan has discovered something new, though. You should catch up with him.

##### After completing the 10 introductory Divination achievements

- **Orla Fairweather:** First, I'd like to give you a reward for learning the basics of divination. You've shown real dedication!
- You receive 500 pieces of flickering energy!
- (receives=500 flickering energy)
- **Orla Fairweather:** Use them wisely.
- (initial|initial-options-camp)

##### After claiming the Divination achievements reward

- **Orla Fairweather:** What can I aid you with today?
- [Menu]: Select an Option {{anchor|initial-options-camp}}
  - [Choice]: I'd like to ask about divination.
    - [Menu]: Select an Option {{anchor|about-divination}}
      - [Choice]: How can I collect memories?
        - (above2|how-to-collect-memories)
      - [Choice]: How can I convert memories?
        - (above2|how-to-convert-memories)
      - [Choice]: What are enriched memories?
        - (above2|enriched-memories)
      - [Choice]: That's all, thanks.
        - (end)
  - [Choice]: Can you tell me about that cape?
    - **Orla Fairweather:** Beautiful, isn't it? We're reserving it for true masters of divination, who may wear it as a sign of their accomplishment.
    - (previous)
  - [Choice]: Can you help me with the divination outfits? {{anchor|fragments}}
    - (Condition: If the player can't receive divination fragments and hasn't unlocked the blueprint required to make the outfit pieces:)
      - **Orla Fairweather:** At level 70 you can start to collect fragments to make elite skilling outfits. When you get to that level you will automatically start collecting fragments. Then you can use them with a blueprint to make yourself any remaining elite outfit pieces for this skill.
    - (Condition: If the player can receive divination fragments but hasn't unlocked the blueprint required to make the outfit pieces:)
      - **Orla Fairweather:** You are set up to receive fragments. When you get to level 80 you will be able to create outfit pieces.
    - (Condition: If the player can receive divination fragments and has unlocked the blueprint required to make the outfit pieces:)
      - **Orla Fairweather:** You are set up to receive fragments. When you have 3600 fragments you can use them to create an elite outfit piece. Simply go to an Invention workbench to create the pieces.
    - (Condition: If the player owns the full elder divination outfit, or all of the outfit pieces required to craft it:)
      - **Orla Fairweather:** You have already created all of the possible outfit pieces. I will make sure you do not receive any further fragments.
      - **Orla Fairweather:** Remember you can combine the base outfit pieces to make the high tier versions, to get the additional benefits.

##### If the player has 99 Divination

- [Menu]: Choose an option:
  - [Choice]: Can you sell me a Divination skillcape?{{anchor|skillcape}}
    - (Condition: If the player has a ring of charos (a) equipped:)
      - **Orla Fairweather:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
      - [Menu]: Choose an option:
        - [Choice]: 92,000 coins? That's much too expensive.
          - **Player:** I know where to find you if I change my mind.
        - [Choice]: I think I have the money right here, actually.
          - (Condition: If the player has no backpack space:)
            - **Orla Fairweather:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some backpack space before I can sell you one.
          - (Condition: If the player does not have enough money:)
            - **Player:** But unfortunately, I was mistaken.
            - **Orla Fairweather:** Well, come back and see me when you do.
          - (Condition: If the player has enough money:)
            - (receives=Divination cape and Divination hood) (removes=92,000 coins)
            - **Orla Fairweather:** Excellent! Wear that cape with pride my friend.
        - [Choice]: cond=If the player has 120 Divination:|I've mastered this skill. Is there anything else?
          - **Orla Fairweather:** There is something...though I have kept it a secret for a very long time. It is something that can only be worn by a true master.
          - **Orla Fairweather:** Not even I can wear it - that's how hard it is to achieve.
          - **Orla Fairweather:** You say you're a master. Stand straight, let me take a look at you...
          - **Orla Fairweather:** You...really have mastered it. What an honour! It would be my pleasure to sell you a Divination master cape.
          - [Menu]: Buy Divination master cape for 120,000 coins?
            - [Choice]: Yes.
              - (Condition: Without free backpack space:)
                - **Orla Fairweather:** You do not have enough room in your backpack. Please come back when you have some more.
              - (Condition: With free backpack space:)
                - (Condition: Without 120,000 coins:)
                  - You do not have enough money to purchase this cape.
                  - (pop-up)
                    - {{Pop-up|You do not have enough money to purchase this cape.|warning=yes}}
                - (Condition: With 120,000 coins:)
                  - (removes=120,000 coins) (receives=Divination master cape)
                  - {{qact|Master cape music plays.}}
            - [Choice]: No.
              - (end)
    - (Condition: If the player does not have a ring of charos (a) equipped:)
      - **Orla Fairweather:** Of course. It is a very prestigious item, however, so it does come with a hefty price tag. The skillcape costs 99,000 gold.
      - [Menu]: Choose an option:
        - [Choice]: 99,000 coins? That's much too expensive.
          - **Player:** I know where to find you if I change my mind.
        - [Choice]: I think I have the money right here, actually.
          - (Condition: If the player has no backpack space:)
            - (above)
          - (Condition: If the player does not have enough money:)
            - (above)
          - (Condition: If the player has enough money:)
            - (receives=Divination cape and Divination hood) (removes=99,000 coins)
            - **Orla Fairweather:** Excellent! Wear that cape with pride my friend.
        - [Choice]: cond=If the player has 120 Divination:|I've mastered this skill. Is there anything else?
          - (above)
  - [Choice]: I've noticed there are a couple of versions of each skillcape. {{anchor|skillcape-version}}
    - **Orla Fairweather:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
    - (Condition: If the player uses the old model:)
      - **Orla Fairweather:** It looks like you're currently using the old model for your Divination skillcape. Would you like to change to the newer one?
      - (continue)
    - (Condition: If the player uses the new model:)
      - **Orla Fairweather:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
      - (continue)
    - [Menu]: Select an Option
      - [Choice]: Yes, I would like to wear the [new/old] version of the skillcape.
        - **Orla Fairweather:** Would you like to wear the [old/newer] model for just this cape, or for the Quest Cape and all of the skillcapes you own?
        - [Menu]: Select an Option
          - [Choice]: I would just like to change the Divination skillcape.
            - **Orla Fairweather:** No problem, you will now use the [older/newer] model for your Divination skillcape.
          - [Choice]: I would like to change all my skillcapes.
            - **Orla Fairweather:** No problem, you will now use the [older/newer] model for all of your skillcapes!
          - [Choice]: I've changed my mind!
            - (end)
      - [Choice]: No, thank you.
        - **Orla Fairweather:** Great! I'm glad you're still enjoying the [old/new] version!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Orla Fairweather:** If you want, I can make it so you use the old model for all of the skillcapes you own.
          - [Menu]: Select an Option
            - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
              - **Orla Fairweather:** Great, you will now use the old model for all of your skillcapes!
            - [Choice]: No, thanks.
              - (end)
  - [Choice]: I'd like to talk about something else.
    - **Orla Fairweather:** What can I aid you with today?
    - [Menu]: Select an Option
      - [Choice]: I'd like to ask about divination.
        - (above|about-divination)
      - [Choice]: Can you sell me a Divination skillcape?
        - (above|skillcape)
      - [Choice]: I've noticed there are a couple of versions of each skillcape.
        - (above|skillcape-version)
      - [Choice]: Can you help me with the divination outfits?
        - (above|fragments)
  - [Choice]: Can you help me with the divination outfits?
    - (above|fragments)

#### Using a chronicle fragment on her

- **Orla Fairweather:** This is a fragment of a chronicle. You should speak to May about these.

#### Using energy on her

- **Orla Fairweather:** This is divine energy. It can be used to produce useful objects and effects.

#### Using a memory on her


##### Normally

- **Orla Fairweather:** Ah, that's a memory. You should take it to a crater and convert it into either experience or energy.

##### During the 25th Anniversary celebrations task

- **Orla Fairweather:** Ah, the memories...
- **Player:** And the energies, chronicles and wisps...
- **Orla Fairweather:** Very droll.
- **Orla Fairweather:** But you are right, we should not dwell on the past so much.
- **Orla Fairweather:** Perhaps you are here for me to divine your future...
- **Player:** Well, seeing as I'm here.
- **Orla Fairweather:** Hmm, let me see... You will stand tall and fight back against powerful gods, yet end up triumphant!
- **Player:** Um, all of that is in the past.
- **Orla Fairweather:** Hmm, let me see... You will complete a series of seemingly random, nostalgic tasks in exchange for a shiny reward!
- **Player:** Sorry, no, that's the present.
- **Orla Fairweather:** Hmm, let me see... You will get an elbow in the ribs from an irate diviner.
- {{RSFontAchievement|By Guthix, to Orla!|Show Orla Fairweather a Divination memory.}}
- ((Shown in a task completion pop-up:))
  - {{Colour|#F0BE79|&nbsp;25TH ANNIVERSARY TASK&nbsp;|#181513}}
  - By Guthix, to Orla!
  - Show Orla Fairweather a Divination memory.
  - (continue)
- **Player:** Ah, no! Please, spare me from my terrible fate!
- (Condition: If all the tasks have been completed:)
  - **Player:** Looks like I've completed everything. I'd better go and see Hans about that reward!

### In Burthorpe

- **Orla Fairweather:** Can you remember now too? I had forgotten. We had all forgotten. Now I know we have to go! The Memorial to Guthix has been waiting for us to remember. Shall we go together?
- [Menu]: Teleport to the Memorial to Guthix?
  - [Choice]: Yes.
    - {{Qact|The player is teleported to the Memorial to Guthix.}}
  - [Choice]: No.
    - (end)

### At Memorial to Guthix


#### First time

- **Player:** What is this place?
- **Orla Fairweather:** It's been here for years, my dear. I knew of it, I've read of it, but we could never see it. It was kept hidden from view for reasons I know not.
- **Orla Fairweather:** Ever since Guthix left this world, I've been gaining an ever-increasing sense of this place's existence.
- **Orla Fairweather:** Tiny strands of Guthixian memories have started appearing near Divination craters.
- **Orla Fairweather:** It seems like they were hidden from view until now.
- **Orla Fairweather:** I'll try to explain what I've been researching since I've been here. It's all coming back to me slowly.
- **Orla Fairweather:** It all starts with engrams. Engrams are permanent markers left on the timeline.
- **Orla Fairweather:** They're caused by the significant activities of living things and can only be spotted by those who have an adept understanding of Divination.
- **Orla Fairweather:** It is possible to charge these engrams by infusing them with divine energy and memory strands.
- **Player:** What does that do to them?
- **Orla Fairweather:** Oh, it's a theatre of light and magic, my dear. The engrams hold an echo of history.
- **Player:** These 'echoes' all belong to Guthix, right? Engrams, memory strands, divine energy...they're all part of Guthix's residual life-force.
- **Orla Fairweather:** How very astute. I suppose I should expect nothing less from you.
- **Orla Fairweather:** I have only ever charged a couple of weak engrams, but they were both from the viewpoints of Guthix himself. We can assume that the rest are almost certainly related to Guthix as well.
- **Player:** There could be so much valuable information stored in these engrams. How do we find them?
- **Orla Fairweather:** In the centre of this concourse behind me, you'll see a pool brimming with energy. You'll probably sense it before you see it. It gives off such a glorious aura.
- **Orla Fairweather:** All of the plinths inside the building are somehow connected to this pool.
- **Orla Fairweather:** Once charged, I could display the echoes found inside the engrams there, just like statues of raw life; animated echoes of reality.
- **Orla Fairweather:** If you tinker with the plinths, you may be able to discover a vague idea of locations of other engrams. I can't promise that they will be easy to detect, though.
- **Player:** So once I've found an engram, I can charge it by filling it with divine energy and these memory strands?
- **Orla Fairweather:** Yes, and then bring it to me. I can get the pool of energy to absorb any charged engrams that you bring here. After that, you should be free to interact with the echoes as you see fit.
- **Player:** This seems simple enough, but let me quickly recap.
- **Player:** I need to use the plinths to get hints about where to find the engrams, then charge these engrams with memory strands and divine energy, and then give them to you to add to the pool here?
- **Orla Fairweather:** Yep, it seems that you've got it.
- **Orla Fairweather:** Oh, one more thing!
- **Player:** Hmm?
- **Orla Fairweather:** The pool of energy. Once I had charged some engrams, I noticed that I felt a stronger connection to this place.
- **Orla Fairweather:** Perhaps we can focus the energy in this place to help you with your Divination skill? Just a hunch, of course.
- **Player:** Sounds interesting. I'll investigate.
- **Orla Fairweather:** Fantastic. Please take one of the engrams that I found, to get yourself started and to gain a feel for them.
- Tutorial stage 1/6 complete.
- (pop-up)
  - {{Pop-up|Tutorial stage 1/6 complete.}}
- (Condition: Without space in backpack:)
  - **Orla Fairweather:** It appears you are too burdened to carry the engram and memory strands. Come back when you have more space.
- (Condition: With space in backpack:)
  - (receives=Naragi engram and 80 memory strands)
  - **Orla Fairweather:** Try not to lose it!

#### Afterwards

- **Orla Fairweather:** See if you can attune the engram that I gave you. It needs to be jump started with some divine energy.

#### Giving memory strands

- [Orla can only do that for you once you have prestiged at least once.]

#### Retrieving the naragi engram

- **Orla Fairweather:** Oh dear, have you lost touch with the engram I gave you?
- **Orla Fairweather:** Here, let's try again. Take this engram.
- (Condition: Without space in backpack:)
  - **Orla Fairweather:** It appears you are too burdened to carry the engram and memory strands. Come back when you have more space.
- (Condition: With space in backpack:)
  - (receives=Naragi engram)
  - **Orla Fairweather:** Try not to lose it!

#### Attempting to enter the pool without 70 Divination

- **Orla Fairweather:** There's a strange energy emanating from that pool. I've tried to enter the pool but nothing happens for myself.
- You need Divination level 70 to enter the Hall of Memories.

#### Returning with the charged Naragi engram

- **Player:** I've charged this engram with divine energy and some memory strands. Could you please take a look at it?
- **Orla Fairweather:** This is perfect!<br> I can feel the energies of the past radiating from this engram.
- (removes=Naragi engram (charged))
- Tutorial stage 2/6 complete.
- (pop-up)
  - {{Pop-up|Tutorial stage 2/6 complete.}}
- **Orla Fairweather:** I will add the echo to the pool and harness its power for you. For free, of course, though I wouldn't mind a pat on the back every now and then.

#### Talking to her again

- **Orla Fairweather:** I've added the charged engram you gave me to the pool of energy. You should assign that echo to one of the plinths surrounding the pool.

#### Adding the Naragi echo

- Tutorial stage 3/6 complete.
- (pop-up)
  - {{Pop-up|Tutorial stage 3/6 complete.}}

#### Talking to her after adding the Naragi echo

- **Orla Fairweather:** That echo, my dear: is that a naragi?
- **Orla Fairweather:** I've only read descriptions, but it makes sense. I wonder what we can learn from it?

#### Checking the naragi

- [Menu]: What would you like to do?
  - [Choice]: Talk to the echo.
    - **Guthix:** The nature of things is a perfect cycle, from one state to another, and a return to prior existence.
    - **Guthix:** Things that once existed, yet now are lost, may yet return and in improved form.
    - **Guthix:** That which is no more shall return again, renewed with more vigour and power than before.
    - **Guthix:** Those who remember the past will see the truth in my words.
    - **Guthix:** Of future events, I see most clear, yet things that must be, must be.
    - **Guthix:** I could change them if I so desired, but I do not, for all things must happen as they run their course.
    - Tutorial stage 4/6 complete.
- (pop-up)
  - {{Pop-up|Tutorial stage 4/6 complete.}}
  - [Choice]: Recolour this echo.
    - ((Non-related dialogue))
  - [Choice]: Clear this plinth.
    - {{Qact|The echo plinth is cleared.}}

#### Returning to Orla

- **Orla Fairweather:** Knowledge is power. That metaphor has an almost tangible weight in times like these. We exist merrily beside beings capable of smiting us with an utterance.
- **Orla Fairweather:** Some days I stand and bask in the serenity of this world, yet on others I feel like a helpless observer in a world where tyrannical children run amok.
- **Orla Fairweather:** The chance for even a miniscule rebalance is not to be scoffed at, should the opportunity present itself, my dear. Let us tinker with the powers here and see what arises.
- **Player:** What is it that you're asking me to do?
- **Orla Fairweather:** Sorry, I sometimes go off on a tangent.
- **Orla Fairweather:** The butterfly statue at the edge of the energy pool controls the flow of energy here. You should be able to power up your Divination skill by tinkering with it. Let me know if it works.

#### Directing the fountain of energy

- Tutorial stage 5/6 complete.
- (pop-up)
  - {{Pop-up|Tutorial stage 5/6 complete.}}

#### Finishing the tutorial

- **Orla Fairweather:** Did you manage to power up your Divination abilities in any way?
- **Player:** I picked an effect and locked the energy to it. It seems like there are more options for me there, but I couldn't quite access them.
- **Orla Fairweather:** Oh, I knew you could do it! I couldn't manage it myself, but I knew there was something to that statue as soon as I found this place.
- **Orla Fairweather:** For allowing me to learn from you, I will allow you to learn from me in return!
- **Orla Fairweather:** There's now almost no limit to the number of chronicles you can carry, and they should also be a bit easier to find.
- Tutorial stage 6/6 complete.
- (pop-up)
  - {{Pop-up|Tutorial stage 6/6 complete.}}
- **Player:** That's very kind of you. Thanks!

#### After the tutorial


##### Without charged engrams

- [Menu]: Talk to Orla
  - [Choice]: Have you got anything else for me?
    - *(With not enough engrams:)*
      - **Orla Fairweather:** You haven't attuned enough engrams for your reward!
    - *(With enough engrams:)*
      - *(Without having claimed the strands:)*
        - **Orla Fairweather:** Take my collection of memory strands. You succeeded, my dear, while I couldn't quite crack it, so it makes sense.
        - Orla has given you [amount] memory strands.
        - **Orla Fairweather:** When I added that charged engram to the pool of energy, everything felt... finished? Is that the right word? I get the sense that there are a set of echoes and we seem to have collected them all.
      - *(Having claimed the strands:)*
        - **Orla Fairweather:** Nothing right now - you can get a feel for the locations of engrams by interacting with the plinths.
  - [Choice]: Can you tell me about these butterflies?
    - **Orla Fairweather:** They seem to be made of dispersed magical energy - from Guthix himself.
    - **Orla Fairweather:** It seems safe to collect them. In keeping with Guthix's teachings of balance, it will be in one of the areas of knowledge or skill where you are most inexperienced.
    - **Player:** What if I don't want to receive experience for catching butterflies?
    - **Orla Fairweather:** Well, I... I suppose I could help you. Do you really want to stop gaining experience for catching butterflies?
    - [Menu]: Select an Option
      - [Choice]: Block XP from butterflies
        - **Orla Fairweather:** You will no longer gain any more experience from catching Guthixian butterflies. Ask me about butterflies again if you change your mind!
      - [Choice]: Gain XP from butterflies
        - **Orla Fairweather:** You will now get experience from catching Guthixian butterflies. Ask me about butterflies again if you change your mind!
  - [Choice]: Nevermind.
    - **Orla Fairweather:** You can get a feel for the locations of engrams by interacting with the plinths.

##### With charged engrams

- **Player:** I've charged this engram with divine energy and some memory strands. Could you please take a look at it?
- **Orla Fairweather:** This is perfect!<br> I can feel the energies of the past radiating from this engram.
- **Orla Fairweather:** I will add the echo to the pool and harness its power for you. For free, of course, though I wouldn't mind a pat on the back every now and then.
- (Condition: If the player still has charged engrams:)
  - **Player:** That wasn't the only charged engram I have.
  - **Orla Fairweather:** Oh? Someone has been busy. Your reputation for getting things done is clearly not unfounded.<br> I'll take any more you have and add them to the pool.
