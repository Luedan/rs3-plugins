# Tool leprechaun

- **Original Wiki Page**: [Transcript:Tool leprechaun](https://runescape.wiki/w/Transcript%3ATool%20leprechaun)
- **Letter**: `T`

---

## Dialogue Transcript


### At all Farming patches


#### Exchange

- ((Farming Store interface opens.))

#### Talk to

- **Tool leprechaun:** Ah, 'tis a fine day! Can I help ye with tool storage, or a trip to Winkin's Farm, or what?
- **Choose...**
  - Tool storage.
    - **What would you like to say?**
      - What tools can you store?
        - **Player:** What can you store?
        - **Tool leprechaun:** We'll hold onto yer rake, seed dibber, spade, secateurs, waterin' can and trowel - but mind it's not one of them fancy trowels only archaeologists use.
        - **Tool leprechaun:** We'll take a few buckets an' scarecrows off yer hands too, and even yer compost, supercompost and ultracompost. There's room in our shed for plenty of compost, so bring it on.
        - **Tool leprechaun:** Also, if ye hands us yer Farming produce, we might be able to change it into banknotes.
        - **Tool leprechaun:** So, do ye want to be using the store?
        - **What would you like to say?**
          - Yes, please.
            - **Player:** Yes, please.
            - ((Farming Store interface opens.))
          - What do you do with the tools you're storing?
            - **Player:** What do you do with the tools you're storing? They can't all possibly fit in your pockets!
            - **Tool leprechaun:** We leprechauns have a shed where we keep 'em. It's a magic shed, so ye can get yer items back from any of us leprechauns whenever ye want. Saves ye havin' to carry loads of stuff around the country!
            - **Tool leprechaun:** So... do ye want to be using the store?
            - **What would you like to say?**
              - {{Sic|Yes please.}}
                - **Player:** Yes, please.
                - ((Farming Store interface opens.))
              - What can you store?
                - (above)
              - No thanks, I'll keep hold of my stuff.
                - (below)
          - No thanks, I'll keep hold of my stuff.
            - **Player:** No thanks, I'll keep hold of my stuff.
            - **Tool leprechaun:** Ye must be dafter than ye look if ye likes luggin' yer tools everywhere ye goes.
      - Open your tool store, please.
        - ((Farming Store interface opens.))
      - Actually, I'm fine.
        - **Player:** Actually, I'm fine.
  - Winkin's Farm.
    - **What would you like to say?**
      - Can you take me to Winkin's Farm?
        - **Player:** Can you take me to Winkin's Farm?
        - **Tool leprechaun:**{{RSChat|Avach nimporto!}}
        - {{Qact|Tool leprechaun teleports you to Winkin's Farm.}}
      - Actually, I'm fine.
        - (above)
  - Composting.
    - **What would you like to say?**
      - Can you compost patches for me?
        - **Player:** Can you compost patches for me?
        - **Tool leprechaun:** Sure, we'll do it at every one o' yer patches using the compost you give us, but not fer free.
        - **Tool leprechaun:** 500 gold for regular compost, 1,500 gold for supercompost or 2,500 gold for ultracompost. Pay for up to 60,000 upfront, but no refunds.
        - ((With composting left to buy:))
          - **What do you want to top up?**
            - ((With normal composting left to buy:))
              - Normal compost.
                - ((A number input with prompt "Pay for how many (max 60,000)?" opens.))
                - ((After entering a positive number:))
                  - **Pay [number] coins?**
                    - Yes.
                      - ((If you do not have sufficient money with you:))
                        - **Tool leprechaun:** Looks like ye can't pay up. Come back when ye can.
                      - ((If you have sufficient money with you:))
                        - (removes=coins)
                        - **Tool leprechaun:** Don't ye worry 'bout compost no more, just keep yer storage topped up!
                    - No.
                      - **Tool leprechaun:** Looks like ye can't pay up. Come back when ye can.
                - ((After entering 0:))
                  - **Tool leprechaun:** Suit yourself.
            - ((With supercomposting left to buy:))
              - Supercompost.
                - ((A number input with prompt "Pay for how many (max 60,000)?" opens.))
                - ((After entering a positive number:))
                  - **Pay [number] coins?**
                    - Yes.
                      - ((If you do not have sufficient money with you:))
                        - **Tool leprechaun:** Looks like ye can't pay up. Come back when ye can.
                      - ((If you have sufficient money with you:))
                        - (removes=coins)
                        - **Tool leprechaun:** Don't ye worry 'bout compost no more, just keep yer storage topped up!
                    - No.
                      - **Tool leprechaun:** Looks like ye can't pay up. Come back when ye can.
                - ((After entering 0:))
                  - **Tool leprechaun:** Suit yourself.
            - ((With ultracomposting left to buy:))
              - Ultracompost.
                - ((A number input with prompt "Pay for how many (max 60,000)?" opens.))
                - ((After entering a positive number:))
                  - **Pay [number] coins?**
                    - Yes.
                      - ((If you do not have sufficient money with you:))
                        - **Tool leprechaun:** Looks like ye can't pay up. Come back when ye can.
                      - ((If you have sufficient money with you:))
                        - (removes=coins)
                        - **Tool leprechaun:** Don't ye worry 'bout compost no more, just keep yer storage topped up!
                    - No.
                      - **Tool leprechaun:** Looks like ye can't pay up. Come back when ye can.
                - ((After entering 0:))
                  - **Tool leprechaun:** Suit yourself.
            - Nothing
              - (continue|refund)
        - ((Without composting left to buy:))
          - **Tool leprechaun:** Looks like yer all paid up.
      - Can you stop composting patches for me?
        - **Player:** Can you stop composting patches for me?
          - ((If you have not paid for composting:))
            - **Tool leprechaun:** Ye've not paid fer anyway, weren't happening anyway.
          - ((If you have paid for composting:))
            - (continue|refund)
      - How much have I paid for?
        - **Player:** How much compost will you use?
        - **Tool leprechaun:** We'll use [number] regular, [number] supercompost and [number] ultracompost. Want to top up?
        - **Select an Option**
          - Yes.
            - (above|top-up)
          - No.
            - **Tool leprechaun:** Don't suppose ye're lookin' for a refund then? I can give ye back all the money ye originally gave me.
            - **Select an Option**
              - Yes.
                - ((Without anything to refund:))
                  - **Tool leprechaun:** Looks like yer all refunded anyway! Phew...
                - ((With something to refund:))
                  - **What do you want to refund?**
                    - ((Only with normal compost to refund:))
                      - Normal compost.
                        - ((A number input opens with prompt "Refund how many (max [number])?"))
                        - ((After entering a positive number:))
                          - (receives=coins)
                          - **Tool leprechaun:** There you go!
                        - ((After entering 0:))
                          - **Tool leprechaun:** Suit yourself.
                    - ((Only with supercompost to refund:))
                      - Supercompost.
                        - ((A number input opens with prompt "Refund how many (max [number])?"))
                        - ((After entering a positive number:))
                          - (receives=coins)
                          - **Tool leprechaun:** There you go!
                        - ((After entering 0:))
                          - **Tool leprechaun:** Suit yourself.
                    - ((Only with ultracompost to refund:))
                      - Ultracompost.
                        - ((A number input opens with prompt "Refund how many (max [number])?"))
                        - ((After entering a positive number:))
                          - (receives=coins)
                          - **Tool leprechaun:** There you go!
                        - ((After entering 0:))
                          - **Tool leprechaun:** Suit yourself.
                    - Nothing.
                      - (end)
              - No.
                - (end)
      - Can I change which patches you compost?
        - ((If there are patches that the tool leprechauns are composting:))
          - ((In the following only the patches that the leprechauns are composting are listed:))
            - **Tool leprechaun:** We'll currently use yer compost on:<br>Tree patches<br>Allotment patches<br>Hops patches<br>Bush patches<br>Herb patches<br>Flower patches<br>Special patches
            - (continue)
        - ((If there are patches that the tool leprechauns are not composting))
          - ((In the following only the patches that the leprechauns are not composting are listed:))
            - **Tool leprechaun:** We'll not use yer compost on<br>Tree patches<br>Allotment patches<br>Hops patches<br>Bush patches<br>Herb patches<br>Flower patches<br>Special patches
            - (continue)
        - **Select an Option**
          - Toggle tree patches
            - **Tool leprechaun:** Do ye want ta change some more?
            - **Select an Option**
              - Yes.
                - (previous)
              - No.
                - (end)
          - Toggle allotment patches
            - **Tool leprechaun:** Do ye want ta change some more?
            - **Select an Option**
              - Yes.
                - (previous)
              - No.
                - (end)
          - Toggle hops patches
            - **Tool leprechaun:** Do ye want ta change some more?
            - **Select an Option**
              - Yes.
                - (previous)
              - No.
                - (end)
          - Toggle bush patches
            - **Tool leprechaun:** Do ye want ta change some more?
            - **Select an Option**
              - Yes.
                - (previous)
              - No.
                - (end)
          - [More Options]
            - **Select an Option**
              - Toggle herb patches
                - **Tool leprechaun:** Do ye want ta change some more?
                - **Select an Option**
                  - Yes.
                    - (previous2)
                  - No.
                    - (end)
              - Toggle flower patches
                - **Tool leprechaun:** Do ye want ta change some more?
                - **Select an Option**
                  - Yes.
                    - (previous2)
                  - No.
                    - (end)
              - Toggle miscellaneous patches
                - **Tool leprechaun:** Do ye want ta change some more?
                - **Select an Option**
                  - Yes.
                    - (previous2)
                  - No.
                    - (end)
              - [Previous Options]
                - (previous)
      - Actually, I'm fine.
        - (above)
  - ((If you have any rewards to collect from the Evil Tree:))
    - Other topics.
      - Can I collect my rewards from the Evil Tree?
        - **Player:** Can I collect my rewards from the Evil Tree?
          - **Tool leprechaun:** To be sure, to be sure.
          - The leprechan hands you your rewards [rewards list]. You also found some [type of seed] seeds!
          - The leprechaun snaps its fingers, and you are granted a magical log-banking ability for the next X minutes.
          - **Tool leprechaun:** Thanks for ya help, [lad/lass]! For the next X minutes, if ya got a full inventory, any regular oak, willow, maple, yes, magic, or elder logs ya get I'll teleport straight to ya bank.
          - **Tool leprechaun:** I'll also sort some magic out, makin' ya less likely to fell regular, oak, willow, maple, yew, or magic trees, but this'll only work on some trees ya find on ya wanderin', not ones ya've grown yaself.
          - **Player:** Thanks!
      - Actually, I'm fine.
        - (above)

#### Note produce


##### Without produce to note

- **Tool leprechaun:** There's nothing for me to exchange.

##### With produce to note

- (All of the produce in the player's backpack is noted.)
- **Tool leprechaun:** Here's some banknotes for ye.

#### Compost

- (above|top-up)

#### Using items


##### If the item can't be noted by tool leprechauns

- **Tool leprechaun:** Nay, I've got no banknotes to exchange for that item.

##### If the item can be noted by tool leprechauns

- (All of the item in the player's backpack is noted.)
- The leprechaun exchanges your [item/items] for: [number] x [banknote/banknotes].
- (pop-up)
  - {{Pop-up|The leprechaun exchanges your [item/items] for: [number] x [banknote/banknotes].|color=#00FF00}}

### At the allotment patch south of Falador


#### Attempting to exchange cabbage(s) for banknotes

- **Tool leprechaun:** A cabbage? Don't ye go showing me yer cabbage; this whole farm stinks of the things! Take it away and get it exchanged somewhere else.

### At the Herblore Habitat


#### Asking "What tools can you store?"

- **Tool leprechaun:** Ah, 'tis a foine day, to be sure! Can I help ye with tool storage, or a trip to Winkin's Farm, or what?
  - Tool storage.
    - What tools can you store?
      - **Player:** What can you store?
      - **Tool leprechaun:** We'll hold onto yer rake, seed dibber, spade, secateurs, waterin' can and trowel - but mind it's not one of them fancy trowels only archaeologists use.
      - **Tool leprechaun:** We'll take a few buckets an' scarecrows off yer hands too, and even yer compost and supercompost. There's room in our shed for plenty of compost, so bring it on.
      - **Tool leprechaun:** Also, if ye hands us yer Farming produce, we might be able to change it into banknotes.
      - **Tool leprechaun:** We can also store some of the potions that help keep this 'ere habitat running smoothly. Only 3-dose potions, mind: we're not going to look after your empties.
      - **Tool leprechaun:** So, do ye want to be using the store?
        - Yes, please.
          - **Player: **Yes, please.
          - **Tool leprechaun:** What would you like to store?
            - Farming tools.
              - *(Farming Store opens)*
            - Vine potions.
              - *(Potion Store opens)*
            - Cancel
        - What do you do with the tools you're storing?
          - *(Same as above)*
        - No thanks, I'll keep hold of my stuff.
          - *(Same as above)*

#### Selected "Exchange" option

- What would you like to exchange?
  - Farming tools.
    - *(Farming Store opens)*
  - Vine potions.
    - *(Potion Store opens)*
  - Cancel

### At Zolarea

- **Tool leprechaun:** Gosh, it's a nice day! Now - can I help you with tool storage, or a trip to Winkin's farm, or something else?
- **CHOOSE...**
  - Tool storage.
    - **WHAT WOULD YOU LIKE TO SAY?**
      - What tools can you store?
        - **Player:** What can you store?
          - **Tool leprechaun:** I can hold onto your rake, seed dibber, spade, secateurs, watering can and trowel - but not those trowels used for archaeology.
          - **Tool leprechaun:** I can also store a few buckets and scarecrows for you, and even compost, supercompost and ultracompost. Of course, compost is essential for good farming, so I can store lots of that for you.
          - **Tool leprechaun:** Also, if you hands me your farming produce, I might be able to change it into banknotes.
          - **Tool leprechaun:** So, would you like me to look after your farming tools?
          - **WHAT WOULD YOU LIKE TO SAY?**
            - Yes, please.
              - **Player:** Yes, please.
              - ((Farming Store interface opens.))
            - What do you do with the tools you're storing?
              - **Player:** What do you do with the tools you're storing? They can't all possibly fit in your pockets!
              - **Tool leprechaun:** Of course not. I have a toolshed. It is rather a curious shed, though. Sometimes, items just seem to appear in there.
              - **Tool leprechaun:** So, would you like me to look after your farming tools?
              - **WHAT WOULD YOU LIKE TO SAY?**
                - {{Sic|Yes please.}}
                  - **Player:** Yes, please.
                  - ((Farming Store interface opens.))
                - What can you store?
                  - (above)
                - No thanks, I'll keep hold of my stuff.
                  - (below)
            - No thanks, I'll keep hold of my stuff.
              - **Player:** No thanks, I'll keep hold of my stuff.
              - **Tool leprechaun:** Well, I shall be here if you ever decide that I may be of service.
      - Open your tool store, please.
        - ((Farming Store interface opens.))
      - Actually, I'm fine.
        - **Player:** Actually, I'm fine.
  - Winkin's Farm.
    - (above)
  - Composting.
    - (above)
  - Other topics.
    - Tell me about yourself.
      - **Player:** What are you doing all the way out here on Zolarea?
      - **Tool leprechaun:** Oh, I love an adventure, me.
      - **Tool leprechaun:** I over'eard some of the wizards in the Wizards' Tower nattering on about this newly-discovered planet and managed to nab a trip 'ere to see it meself.
      - **Tool leprechaun:** And boy, am I glad I did! This place is overgrowing with beautiful starblooms - I tell ya, the soil 'ere is perfect fer cultivating them.
      - **Tool leprechaun:** But enough about me, do ye want me to look after yer farming tools?
        - **WHAT WOULD YOU LIKE TO SAY?**
          - Yes, please.
            - (above)
          - What can you store?
            - (above)
          - No thanks, I'll keep hold of my stuff.
            - (above)
    - Actually, I'm fine.
      - **Player:** Actually, I'm fine.

### Applying compost to a patch

- The tool leprechaun automatically uses [compost/supercompost/ultracompost] on your patch for you.  <!-- filtered -->
