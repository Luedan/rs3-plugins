# Advisor Ghrim

- **Original Wiki Page**: [Transcript:Advisor Ghrim](https://runescape.wiki/w/Transcript%3AAdvisor%20Ghrim)
- **Letter**: `A`

---

## Dialogue Transcript

{{transcript npc|Advisor Ghrim}}

### Before Throne of Miscellania

- **Advisor Ghrim:** Greetings, [Sir/Madam].
- {{tact|If the player has previously killed anyone in Miscellania:}}
  - **Advisor Ghrim:** I can tell you right away that killing someone will not make you popular with anyone.
  - {{tact|continue}}
- **Advisor Ghrim:**  The King needs someone to take over the rule of the kingdom. If I were you, I should consider the position.
- {{tselect|Choose an option:}}
  - {{topt|Tell me about the Achievement System.}}
    - {{tact|below}}
  - {{topt|Could I buy a spare of the reward?}}
    - {{tact|below}}
  - {{topt|Sorry, I was just leaving.}}
    - (end)

### After Throne of Miscellania


#### Talking to Advisor Ghrim

- **Advisor Ghrim:** Greetings, Your Royal Highness.
- {{tact|If the player has previously killed anyone in Miscellania:}}
  - **Advisor Ghrim:** Your Royal Highness, I should tell you right away that killing the people of this kingdom will not make you popular with anyone.
  - {{tact|continue}}
- {{tselect|Choose an option:}}
  - {{topt|How is the kingdom faring?}}
    - **Player:** How is the Kingdom faring?
      - {{tcond|If the player's approval rating is sufficiently high:}}
        - **Advisor Ghrim:** Your subjects are content, Your Highness.
        - {{tact|continue}}
    - **Advisor Ghrim:** Your approval rating is [number]%. Would you like to collect the resources gathered by your subjects?
    - {{tselect|Select an Option}}
      - {{topt|Yes, please.}}
        - **Player:** Yes, please.
        - **Advisor Ghrim:** Here is a list of what your subjects have collected.
        - *(Kingdom Resources interface opens.)*
        - {{tcond|After collecting the resources:}}
          - **Advisor Ghrim:** I shall tell your subjects to deliver your resources to your bank right away, Your Royal Highness.
          - **Advisor Ghrim:** This is how your subjects are distributing their effort.
          - *(Kingdom of Miscellania interface opens.)*
      - {{topt|No, thank you.}}
        - **Player:** No, thank you.
        - **Advisor Ghrim:** Very well, Your Royal Highness.
        - **Advisor Ghrim:** This is how your subjects are distributing their effort.
        - *(Kingdom of Miscellania interface opens.)*
  - {{topt|cond=Between Glorious Memories and Blood Runs Deep|What happened to King Vargas?}}
    - **Player:** What happened to King Vargas?
    - **Advisor Ghrim:** His Majesty has just set out on his latest great adventure. I do not know when he will return, your{{Sic}} Royal Highness.
  - {{topt|cond=After Blood Runs Deep|It's good to have King Vargas back.}}
    - **Player:** It's good to have King Vargas back.
    - **Advisor Ghrim:** It certainly is, and I understand he has you to thank, your Majesty.
    - **Advisor Ghrim:** Perhaps, now that Queen Sigrid has moved in, he will not be tempted to go on any more 'adventures'.
  - {{topt|How do I manage the kingdom?}}
    - **Player:** How do I manage the kingdom?
    - **Advisor Ghrim:** Your loyal subjects work hard to collect resources for you. Every day they bring what they have collected to the castle. The resources which they collect are coal from the rocks to the north, maple logs from the trees to the east, herbs from the garden just outside the castle, and tuna and swordfish fished at the port to the south.
    - {{tcond|Before Royal Trouble:}}
      - **Advisor Ghrim:** They are paid from the money in the coffers; each day, one-tenth of the money in the coffers is distributed to them. A maximum of 75k is paid to your subjects, and the coffers can store up to 7.5 million gp.
      - {{tact|continue}}
    - {{tcond|After Royal Trouble:}}
      - **Advisor Ghrim:** Etceteria has also pledged you teak and mahogany logs from their trees to the north, and seeds from their farm to the south. They are paid from the money in the coffers; each day, one-tenth of the money in the coffers is distributed to them. A maximum of 75k is paid to your subjects and the Etceterians, and the coffers can store up to 7.5 million gp.
      - {{tact|continue}}
    - **Advisor Ghrim:** Another thing which affects the amounts of resources collected is your approval rating. The more your subjects love you, the more they will be motivated to work hard. King Vargas would often go and help out his subjects in their daily tasks, when he was still able to do so, and they loved him dearly for it. Finally, you can choose how much of their efforts your subjects devote to each resource; of course, the harder they work at collecting one, the less time they have to spend collecting the others.
    - {{tcond|If the player doesn't have a copy of Ghrim's book:}}
      - **Advisor Ghrim:** Have you got a copy of my book? It explains everything in more detail.
      - **Player:** No, I don't...
      - **Advisor Ghrim:** Here, you can have this one, I have plenty spare.
      - **Player:** Thanks!
      - {{tact|receives=Ghrim's book}}
  - {{topt|What am I meant to be doing again?}}
    - **Player:** What am I meant to be doing again?
    - **Advisor Ghrim:** Ruling the kingdom, Your Royal Highness.
    - **Advisor Ghrim:** And making sure that the king doesn't cause any more trouble.
  - {{topt|About the Task System...}}
    - {{tact|below2|Task System}}

### Collect

- **Advisor Ghrim:**  Here is a list of what your subjects have collected.
- *(Kingdom Resources interface opens.)*
- **Advisor Ghrim:**  I shall tell your subjects to deliver your resources to your bank right away, Your Royal Highness.
- **Advisor Ghrim:** This is how your subjects are distributing their effort.
- *(Kingdom of Miscellania interface opens.)*

##### If there are no resources to collect

- **Advisor Ghrim:** I'm afraid your subjects have not collected anything.

### Manage

- **Advisor Ghrim:**  This is how your subjects are distributing their effort.
- *(Kingdom of Miscellania interface opens.)*

### Task System

- ((If the player has completed the hard Fremennik achievements and the rewards have not been claimed:))
  - **Player:**  I've completed all of the Hard Tasks in the Fremennik set.
  - **Advisor Ghrim:** Yes, Your Highness, I see that. I have some old boots here I discovered in the treasury which you should perhaps take.
  - {{tact|receives=Fremennik sea boots 3 and Antique lamp (Hard Fremennik Tasks)}}
    - {{tcond|If the player does not have sufficient space in backpack:}}
      - **Advisor Ghrim:** Unfortunately, you can't carry them at the moment.
    - {{tcond|If the player does have sufficient space in backpack:}}
      - **Advisor Ghrim:** There you are. You should look carefully to see what they can do.
      - **Advisor Ghrim:** For example, if you have spare flat-packed furniture I could buy it from you and put the gold in the coffers. We're expanding the settlements in the dungeons and spare furniture could be very useful.
      - **Player:** Thanks!
      - {{tact|continue}}
- ((If the player has completed the elite Fremennik achievements and the rewards have not been claimed:))
  - **Player:**  I've completed all of the Elite Tasks in the Fremennik set.
  - **Advisor Ghrim:** Yes, Your Highness, I see that. I have some old boots here I discovered in the treasury which you should perhaps take.
  - {{tact|receives=Fremennik sea boots 4, four Antique lamps (Elite Fremennik Tasks, 30k) and Antique lamp (Elite Fremennik Tasks, 40k)}}
  - **Advisor Ghrim:** There you are. You should look carefully to see what they can do.
  - **Advisor Ghrim:** For example, that barbarian lyre could take you more places; talk to Rimae Sirsalis to trade suqah hide and teeth for run essence; use the NPC contact spell to change your spell book from Lunar back to the standard spellbook and use the seal Seal of Passage to teleport to Lunar Isle once per day.
  - **Player:** Thanks!
  - {{tact|continue}}
- {{tcond|If the player has lost their Fremennik sea boots 3:}}
  - **Advisor Ghrim:** Your Highness, how are the boots?
  - **Player:** I lost them.
  - **Advisor Ghrim:** Really? Here, I found some more in the treasury.
  - {{tact|receives=Fremennik sea boots 3}}
  - {{tbox|pic=Fremennik sea boots 3 detail.png|Advisor Ghrim hands you another pair of boots.}}
  - {{tact|continue}}
- {{tcond|If the player has lost their Fremennik sea boots 4:}}
  - **Advisor Ghrim:** How are the boots, Your Highness?
  - **Player:** I lost them.
  - **Advisor Ghrim:** Really? Here, I found some more in the treasury.
  - {{tact|receives=Fremennik sea boots 4}}
  - {{tbox|pic=Fremennik sea boots 4 detail.png|Advisor Ghrim hands you another pair of boots.}}
  - {{tact|continue}}
- {{tselect|Choose an option:}}
  - {{topt|Tell me about the Achievement System.}}
    - **Advisor Ghrim:** Very well: the Achievement System is a collection of deeds you may wish to complete while adventuring around the world.
    - **Advisor Ghrim:**You can earn special rewards for completing certain achievements; at the very least, each is worth a cash bounty from Explorer Jack in Lumbridge.
    - **Advisor Ghrim:** Some also give items that will help complete other achievements, and many count as progress towards the set for the area they're in.
    - {{tselect|Choose an option:}}
      - {{topt|Tell me about the set reward for this locality.}}
        - **Player:** Tell me about the set reward for this area.
        - **Advisor Ghrim:** Your Highness, the Fremennik set reward is a pair of sea boots.
        - **Advisor Ghrim:** These boots will become increasingly useful with each difficulty level of the set that you complete.
        - **Advisor Ghrim:** When you are presented with your rewards, you will be told of their uses.
        - You may also see what rewards a set item provides by hovering over the Rewards icon for its Exploration Achievement set in the Achievements interface.
        - {{tact|previous2}}
      - {{topt|How do I claim these rewards?}}
        - **Player:** How do I claim the rewards?
        - **Advisor Ghrim:** You need to complete all of the tasks in a set of a particular difficulty, then you can claim your reward.
        - **Advisor Ghrim:** Some of the Fremennik set's Tasks are simple, some will require certain skill levels, and some might require quests to be started or completed.
        - **Advisor Ghrim:**  To claim your Fremennik set rewards, speak to the council workman on the bridge south of Rellekka, Yrsa in Rellekka, or myself.
        - {{tact|previous2}}
      - {{topt|Sorry, I was just leaving.}}
        - {{tact|end}}
  - {{topt|Could I buy a spare of the reward?}}
    - {{tselect|Choose an option:}}
      - {{topt|Fremennik sea boots 1}}
        - **Advisor Ghrim:** Fremennik sea boots 1? Yes, but I'm afraid it would cost you 1,500 coins.
        - {{tselect|Purchase another for 1,500 coins?}}
          - {{topt|Yes}}
            - {{tbox|pic=Fremennik sea boots 1 detail.png|You're handed another Fremennik sea boots 1.}}
            - {{tact|receives=Fremennik sea boots 1}} {{tact|removes= 1,500 coins}}
          - {{topt|No}}
            - **Player:** No thanks.
      - {{topt|Fremennik sea boots 2}}
        - **Advisor Ghrim:** Fremennik sea boots 2? Yes, but I'm afraid it would cost you 2,500 coins.
        - {{tselect|Purchase another for 2,500 coins?}}
          - {{topt|Yes}}
            - {{tbox|pic=Fremennik sea boots 2 detail.png|You're handed another Fremennik sea boots 2.}}
            - {{tact|receives=Fremennik sea boots 2}} {{tact|removes= 2,500 coins}}
          - {{topt|No}}
            - **Player:** No thanks.
      - {{topt|Fremennik sea boots 3}}
        - **Advisor Ghrim:** Fremennik sea boots 3? Yes, but I'm afraid it would cost you 7,500 coins.
        - {{tselect|Purchase another for 7,500 coins?}}
          - {{topt|Yes}}
            - {{tbox|pic=Fremennik sea boots 3 detail.png|You're handed another Fremennik sea boots 3.}}
            - {{tact|receives=Fremennik sea boots 3}} {{tact|removes= 7,500 coins}}
          - {{topt|No}}
            - **Player:** No thanks.
      - {{topt|Fremennik sea boots 4}}
        - **Advisor Ghrim:** Fremennik sea boots 4? Yes, but I'm afraid it would cost you 15,000 coins.
        - {{tselect|Purchase another for 15,000 coins?}}
          - {{topt|Yes}}
            - {{tbox|pic=Fremennik sea boots 4 detail.png|You're handed another Fremennik sea boots 4.}}
            - {{tact|receives=Fremennik sea boots 4}} {{tact|removes= 15,000 coins}}
          - {{topt|No}}
            - **Player:** No thanks.
  - {{topt|Sorry, I was just leaving.}}
    - (end)

#### Using flatpacks on Ghrim (requires the hard Fremennik achievements)

- **Advisor Ghrim:** Ah, just what we need! We can always use new furniture. I'll put them in the coffers now, if you'd like.
- {{tselect|How many would you like to donate?}}
  - {{topt|Donate-1.}}
    - **Advisor Ghrim:** For 1 of those, I'll put [number] coins into the coffers. Is that acceptable?
    - {{anchor|flatpack}} {{tselect|Select an Option}}
      - {{topt|Yes.}}
        - {{tact|removes=flatpack(s)}}
      - {{topt|No.}}
        - {{tact|end}}
  - {{topt|Donate-5.}}
    - **Advisor Ghrim:** For 5 of those, I'll put [number] coins into the coffers. Is that acceptable?
    - {{tact|continuea|flatpack}}
  - {{topt|Donate-all.}}
    - **Advisor Ghrim:** For [number] of those, I'll put [number] coins into the coffers. Is that acceptable?
    - {{tact|continuea|flatpack}}
  - {{topt|Donate-X.}}
    - {{tinput|Enter amount:}}
    - {{tact|(After entering a positive amount:)}}
      - **Advisor Ghrim:** For [number] of those, I'll put [number] coins into the coffers. Is that acceptable?
      - {{tact|continuea|flatpack}}
    - {{tcond|If zero is entered:}}
      - **Advisor Ghrim:** For 0 of those, I'll put 0 coins into the coffers. Is that acceptable?
      - {{tact|continuea|flatpack}}
