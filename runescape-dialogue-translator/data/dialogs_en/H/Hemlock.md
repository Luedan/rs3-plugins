# Hemlock

- **Original Wiki Page**: [Transcript:Hemlock](https://runescape.wiki/w/Transcript%3AHemlock)
- **Letter**: `H`

---

## Dialogue Transcript


### Exchange

- ((Farming Store interface opens.))

### Talk to

- **Hemlock:** It's a rather nice day here in Um! Can I help you with tool storage, or a trip to Winkin's farm, or something else?
- [Menu]: Choose...
  - [Choice]: Tool storage.
    - [Menu]: What would you like to say?
      - [Choice]: What tools can you store?
        - **Player:** What can you store?
        - **Hemlock:** I can hold onto your rake, seed dibber, spade, secateurs, watering can and trowel - but not those trowels used for archaeology.
        - **Hemlock:** I can also store a few buckets and scarecrows for you, and even compost, supercompost and ultracompost. Of course, compost is essential for good farming, so I can store lots of that for you.
        - **Hemlock:** Also, if you hand me your farming produce, I might be able to change it into banknotes.
        - **Hemlock:** So, would you like me to look after your farming tools?
        - [Menu]: What would you like to say?
          - [Choice]: Yes, please.
            - **Player:** Yes, please.
            - ((Farming Store interface opens.))
          - [Choice]: What do you do with the tools you're storing?
            - **Player:** What do you do with the tools you're storing? They can't all possibly fit in your pockets!
            - **Hemlock:** Of course not. I have a toolshed. It is rather curious shed, though. Sometimes, items just seem to appear in there.
            - **Hemlock:** So, would you like me to look after your tools?
            - [Menu]: What would you like to say?
              - [Choice]: Yes please.
                - **Player:** Yes, please.
                - ((Farming Store interface opens.))
              - [Choice]: What can you store?
                - (above)
              - [Choice]: No thanks, I'll keep hold of my stuff.
                - (below)
          - [Choice]: No thanks, I'll keep hold of my stuff.
            - **Player:** No thanks, I'll keep hold of my stuff.
            - **Hemlock:** Well, I shall be here if you ever decide that I may be of service.
      - [Choice]: Open your tool store, please.
        - ((Farming Store interface opens.))
      - [Choice]: Actually, I'm fine.
        - **Player:** Actually, I'm fine.
  - [Choice]: Winkin's Farm.
    - [Menu]: What would you like to say?
      - [Choice]: Can you take me to Winkin's Farm?
        - **Player:** Can you take me to Winkin's Farm?
        - **Hemlock:**{{RSChat|Avach nimporto!}}
        - {{Qact|Hemlock teleports you to Winkin's Farm.}}
      - [Choice]: Actually, I'm fine.
        - (above)
  - [Choice]: Composting.
    - [Menu]: What would you like to say
      - [Choice]: Can you compost patches for me?
        - **Player:** Can you compost patches for me?
        - **Hemlock:** Sure, I can do it at all of your patches using the compost you give me, if you're willing to pay for the convenience.
        - **Hemlock:** 500 gold for regular compost, 1,500 gold for supercompost or 2,500 gold for ultracompost. Pay for up to 60,000 upfront, but no refunds.
        - ((With composting left to buy:))
          - [Menu]: What do you want to top up?
            - (Condition: With normal composting left to buy:)
              - [Choice]: Normal compost
                - {{Tinput|Pay for how many (max [number])?}}
                - ((After entering a positive number:))
                  - [Menu]: Pay [number] coins?
                    - [Choice]: Yes.
                      - (Condition: If you do not have sufficient money with you:)
                        - **Hemlock:** You've not got enough coins, come back when you do
                      - (Condition: If you have sufficient money with you:)
                        - (removes=coins)
                        - **Hemlock:** Very well, I'll keep your patches composted. Just keep your storage topped up.
                    - [Choice]: No.
                      - **Hemlock:** You've not got enough coins, come back when you do
                - ((After entering 0:))
                  - **Hemlock:** Suit yourself.
            - (Condition: With supercomposting left to buy:)
              - [Choice]: Supercompost
                - {{Tinput|Pay for how many (max [number])?}}
                - ((After entering a positive number:))
                  - [Menu]: Pay [number] coins?
                    - [Choice]: Yes.
                      - (Condition: If you do not have sufficient money with you:)
                        - **Hemlock:** You've not got enough coins, come back when you do
                      - (Condition: If you have sufficient money with you:)
                        - (removes=coins)
                        - **Hemlock:** Very well, I'll keep your patches composted. Just keep your storage topped up.
                    - [Choice]: No.
                      - **Hemlock:** You've not got enough coins, come back when you do
                - ((After entering 0:))
                  - **Hemlock:** Suit yourself.
            - (Condition: With ultracomposting left to buy:)
              - [Choice]: Ultracompost.
                - {{Tinput|Pay for how many (max [number])?}}
                - ((After entering a positive number:))
                  - [Menu]: Pay [number] coins?
                    - [Choice]: Yes.
                      - (Condition: If you do not have sufficient money with you:)
                        - **Hemlock:** You've not got enough coins, come back when you do
                      - (Condition: If you have sufficient money with you:)
                        - (removes=coins)
                        - **Hemlock:** Very well, I'll keep your patches composted. Just keep your storage topped up.
                    - [Choice]: No.
                      - **Hemlock:** You've not got enough coins, come back when you do
                - ((After entering 0:))
                  - **Hemlock:** Suit yourself.
            - [Choice]: Nothing
              - (continue|refund)
        - (Condition: Without composting left to buy:)
          - **Hemlock:** Looks like yer all paid up.
      - [Choice]: Can you stop composting patches for me?
        - **Player:** Can you stop composting patches for me?
          - ((If you have not paid for composting:))
            - **Hemlock:** You hadn't paid me, so I wasn't doing it anyway.
          - ((If you have paid for composting:))
            - (continue|refund)
      - [Choice]: How much have I paid for?
        - **Player:** How much compost will you use?
        - **Hemlock:** We'll use [number] regular, [number] super compost and [number] ultracompost. Want to top up?
        - [Menu]: Select an Option
          - [Choice]: Yes.
            - (above|top-up)
          - [Choice]: No.
            - **Hemlock:** Do you want a refund then?
            - [Menu]: Select an Option
              - [Choice]: Yes.
                - (Condition: Without anything to refund:)
                  - **Hemlock:** Looks like you're not actually owed a refund anyway.
                - (Condition: With something to refund:)
                  - [Menu]: What do you want to refund?
                    - (Condition: Only with normal compost to refund:)
                      - [Choice]: Normal compost.
                        - {{Tinput|Refund how many (max [number])?}}
                        - ((After entering a positive number:))
                          - (receives=coins)
                          - **Hemlock:** There you go!
                        - ((After entering 0:))
                          - **Hemlock:** Suit yourself.
                    - (Condition: Only with supercompost to refund:)
                      - [Choice]: Supercompost.
                        - {{Tinput|Refund how many (max [number])?}}
                        - ((After entering a positive number:))
                          - (receives=coins)
                          - **Hemlock:** There you go!
                        - ((After entering 0:))
                          - **Hemlock:** Suit yourself.
                    - (Condition: Only with ultracompost to refund:)
                      - [Choice]: Ultracompost.
                        - {{Tinput|Refund how many (max [number])?}}
                        - ((After entering a positive number:))
                          - (receives=coins)
                          - **Hemlock:** There you go!
                        - ((After entering 0:))
                          - **Hemlock:** Suit yourself.
                    - Nothing.
                      - (end)
              - [Choice]: No.
                - (end)
      - [Choice]: Can I change which patches you compost?
        - (Condition: If there are patches that are being composted:)
          - ((In the following only the patches that are being composted are listed:))
            - **Hemlock:** We'll currently use your compost on:<br>Tree patches<br>Allotment patches<br>Hops patches<br>Bush patches<br>Herb patches<br>Flower patches<br>Special patches
            - (continue)
        - (Condition: If there are patches that aren't being composted:)
          - ((In the following only the patches that aren't being composted are listed:))
            - **Hemlock:** We'll not use your compost on:<br>Tree patches<br>Allotment patches<br>Hops patches<br>Bush patches<br>Herb patches<br>Flower patches<br>Special patches
            - (continue)
        - [Menu]: Select an Option
          - [Choice]: Toggle tree patches.
            - **Hemlock:** Do you want to change some more?
            - [Menu]: Select an Option
              - [Choice]: Yes.
                - (previous)
              - [Choice]: No.
                - (end)
          - [Choice]: Toggle allotment patches.
            - **Hemlock:** Do you want to change some more?
            - [Menu]: Select an Option
              - [Choice]: Yes.
                - (previous)
              - [Choice]: No.
                - (end)
          - [Choice]: Toggle hops patches.
            - **Hemlock:** Do you want to change some more?
            - [Menu]: Select an Option
              - [Choice]: Yes.
                - (previous)
              - [Choice]: No.
                - (end)
          - [Choice]: Toggle bush patches.
            - **Hemlock:** Do you want to change some more?
            - [Menu]: Select an Option
              - [Choice]: Yes.
                - (previous)
              - [Choice]: No.
                - (end)
          - [Choice]: [More Options]
            - [Menu]: Select an Option
              - [Choice]: Toggle herb patches.
                - **Hemlock:** Do you want to change some more?
                - [Menu]: Select an Option
                  - [Choice]: Yes.
                    - (previous2)
                  - [Choice]: No.
                    - (end)
              - [Choice]: Toggle flower patches.
                - **Hemlock:** Do you want to change some more?
                - [Menu]: Select an Option
                  - [Choice]: Yes.
                    - (previous2)
                  - [Choice]: No.
                    - (end)
              - [Choice]: Toggle miscellaneous patches.
                - **Hemlock:** Do you want to change some more?
                - [Menu]: Select an Option
                  - [Choice]: Yes.
                    - (previous2)
                  - [Choice]: No.
                    - (end)
              - [Choice]: [Previous Options]
                - (previous)
      - [Choice]: Other topics.
        - [Menu]: What would you like to say?
          - [Choice]: Tell me about yourself.
            - **Player:** How did you come to be a gardener in Um? A lot of people would probably want to stop working after they died.
            - **Hemlock:** Well, you see, all my life I'd wanted to be a gardener.
            - **Hemlock:** The smell of the soil, the joy you feel when you harvest a cared-for crop...
            - **Hemlock:** But, I was afraid of what people would think of me...
            - **Hemlock:** All of the gardeners were leprechauns at the time, and I looked nothing like a leprechaun!
            - **Player:** You still don't look anything like a leprechaun.
            - **Hemlock:** Exactly! So, I never did become a gardener.
            - **Hemlock:** After death though, I created this little garden in Um.
            - **Hemlock:** When my leprechaun friend over there arrived, I was prepared for the worst...
            - **Hemlock:** 'There's only room for one gardener in this town', I was expecting him to say. Or something along those lines.
            - **Hemlock:** But he's been noting but accepting! As it turned out, he was more than happy to retire after dying.
            - **Player:** How lovely.
            - **Hemlock:** Anyway, do you want me to look after your farming tools?
            - (above|farming-tools)
          - [Choice]: Actually, I'm fine.
            - (above)

### Note produce


#### Without produce to note

- **Hemlock:** There's nothing for me to exchange.

#### With produce to note

- (All of the produce in the player's backpack is noted.)
- **Hemlock:** Here's your banknotes.

### Compost

- (above|top-up)

### Using items


#### If the item can't be noted by Hemlock or stored in the Farming Store

- **Hemlock:** Sorry, I don't have any banknotes to exchange for that item.

#### If the item can be noted by Hemlock

- (All of the item in the player's backpack is noted.)
- The skeleton exchanges your [item/items] for: [number] x [banknote/banknotes].
- ((Repeated in a pop-up:)
  - The skeleton exchanges your [item/items] for: [number] x [banknote/banknotes].

#### If the item can be stored in the Farming Store


##### Without space for the item

- You can't store any more of those.

##### With space for the item

- (removes=item)
- You add [number] x [Item] to the store.
