# Nhitpyx

- **Original Wiki Page**: [Transcript:Nhitpyx](https://runescape.wiki/w/Transcript%3ANhitpyx)
- **Letter**: `N`

---

## Dialogue Transcript


### Exchange

- ((Farming Store interface opens.))

### Talk to

- **Nhitpyx:** What do you want then?
- **CHOOSE...**
  - Tool storage.
    - **WHAT WOULD YOU LIKE TO SAY?**
      - What tools can you store?
        - (continue|What can you store)
      - Open your tool store, please.
        - ((Farming Store interface opens.))
      - Actually, I'm fine.
        - **Player:** Actually, I'm fine.
  - Winkin's Farm.
    - **WHAT WOULD YOU LIKE TO SAY?**
      - Can you take me to Winkin's Farm?
        - **Player:** Can you take me to Winkin's Farm?
        - **Nhitpyx:** {{RSChat|Avach nimporto!}}
        - {{Qact|The player is teleported to Winkin's Farm.}}
      - Actually, I'm fine.
        - **Player:** Actually, I'm fine.
  - Composting.
    - **WHAT WOULD YOU LIKE TO SAY?**
      - Can you compost patches for me?
        - **Player:** Can you compost patches for me?
        - **Nhitpyx:** Wow, someone's lazy... I'll do it, but it'll cost you.
        - **Nhitpyx:** 500 gold for regular compost, 1,500 gold for supercompost or 2,500 gold for ultracompost. Pay for up to 60,000 upfront, but no refunds.
        - (continue|Compost)
      - Can you stop composting patches for me?
        - **Player:** Can you stop composting patches for me?
        - ((With refund available:))
          - (continue|Do you want a refund then)
        - ((Without refund available:))
          - **Nhitpyx:** You hadn't paid me, so I wasn't doing it anyway.
      - How much have I paid for?
        - **Player:** How much compost will you use?
        - **Nhitpyx:** We'll use [number] regular, [number] supercompost and [number] ultracompost. Want to top up?
        - **SELECT AN OPTION**
          - Yes.
            - (continue|Compost)
          - No.
            - (continue|Do you want a refund then)
      - Can I change which patches you compost?
        - ((Only with composting toggled on for some patches, and only the patches toggled on are listed:))
          - **Nhitpyx:** We'll use your compost on:<br>Tree patches<br>Allotment patches<br>Hops patches<br>Bush patches<br>Herb patches<br>Flower patches<br>Special patches<br>
          - (continue)
        - ((Only with composting toggled off for some patches, and only the patches toggled off are listed:))
          - **Nhitpyx:** We'll not use your compost on:<br>Tree patches<br>Allotment patches<br>Hops patches<br>Bush patches<br>Herb patches<br>Flower patches<br>Special patches<br>
          - (continue)
        - **SELECT AN OPTION**
          - Toggle tree patches.
            - (continue|After toggling a patch)
          - Toggle allotment patches.
            - (continue|After toggling a patch)
          - Toggle hops patches.
            - (continue|After toggling a patch)
          - Toggle bush patches.
            - (continue|After toggling a patch)
          - [More options]
            - **SELECT AN OPTION**
              - Toggle herb patches.
                - (continue|After toggling a patch)
              - Toggle flower patches.
                - (continue|After toggling a patch)
              - Toggle miscellaneous patches.
                - (continue|After toggling a patch)
              - [Previous options]
                - (previous2)
      - Actually, I'm fine.
        - **Player:** Actually, I'm fine.
  - Other topics.
    - **WHAT WOULD YOU LIKE TO SAY?**
      - Aren't you bit tall for a leprechaun?
        - **Player:** Aren't you bit tall for a leprechaun?
        - **Nhitpyx:** What?<br>Aren't you a bit old for such stupid questions?
        - **Player:** Well, you're looking after tools like leprechauns do.
        - **Nhitpyx:** I swear to Guthix I'm getting too old for this. Now, do you want me to look after your farming tools?
        - **WHAT WOULD YOU LIKE TO SAY?**
          - Yes, please.
            - **Player:** Yes, please.
            - ((Farming Store interface opens.))
          - ((Only if not asked last:))
            - What can you store?
              - **Player:** {{AnchorText|What can you store}}?
              - **Nhitpyx:** I didn't think this was complicated... I can hold onto a rake, seed dibber, spade, secateurs, watering can and trowel - but not those dodgy archaeology ones.
              - **Nhitpyx:** I can also store some buckets and scarecrows, as well as compost, supercompost and ultracompost.
              - **Nhitpyx:** I've also been told that if you give me your farming produce, I should swap it for these banknotes.
              - **Nhitpyx:** So, do you want me to look after your farming tools?
              - (previous)
          - ((Only after asking "What can you store?":))
            - What do you do with the tools you're storing?
              - **Player:** What do you do with the tools you're storing?<br>They can't possibly all fit in your pockets!
              - **Nhitpyx:** What...Well obviously I don't keep them in my pockets, look, I tend to just throw them behind the old compost bin there with the other adventurer's tools.
              - **Nhitpyx:** Now, do you want me to look after your tools or not?
          - No thanks, I'll keep hold of my stuff.
            - **Player:** No thanks, I'll keep hold of my stuff.
            - **Nhitpyx:** Alright? Your loss.
      - Actually, I'm fine.
        - **Player:** Actually, I'm fine.

#### After toggling a patch

- **Nhitpyx:** Do you want to change some more?
- **SELECT AN OPTION**
  - Yes.
    - (above|patches)
  - No.
    - (end)

### Note produce


#### With items to note

- {{Qact|The items are noted.}}
- **Nhitpyx:** Here's your banknotes.

#### Without items to note

- **Nhitpyx:** There's nothing for me to exchange.

### Compost

- **WHAT DO YOU WANT TO TOP UP?**
  - Normal compost.
    - (continue|Buying compost)
  - Supercompost.
    - (continue|Buying compost)
  - Ultracompost.
    - (continue|Buying compost)
  - Nothing.
    - **Nhitpyx:** {{AnchorText|Do you want a refund then}}?
    - **SELECT AN OPTION**
      - Yes.
        - ((With refund available:))
          - **WHAT DO YOU WANT TO REFUND?**
            - ((Only with normal compost to refund:))
              - Normal compost.
                - (continue|Refunding compost)
            - ((Only with supercompost to refund:))
              - Supercompost.
                - (continue|Refunding compost)
            - ((Only with ultracompost to refund:))
              - Ultracompost.
                - (continue|Refunding compost)
            - Nothing.
              - (end)
        - ((Without refund available:))
          - **Nhitpyx:** Looks like you're not actually owed a refund anyway.
      - No.
        - (end)

#### Buying compost

- ((The prompt "Pay for how many (max [number])?" is shown.))
- ((After entering a number:))
  - **PAY [NUMBER] COINS? YOU WILL NOT BE ABLE TO RECLAIM THEM.**
    - Yes.
      - ((If a number greater than zero was entered and you have enough coins:))
        - (removes=coins)
        - **Nhitpyx:** Very well, I'll keep your patches composted. Just keep your storage topped up.
      - ((If zero was entered or you don't have enough coins:))
        - **Nhitpyx:** You've not got enough gold, I'm not doing it for free!
    - No.
      - **Nhitpyx:** You've not got enough gold, I'm not doing it for free!

#### Refunding compost

- ((The prompt "Refund how many (max [number])?" is shown.))
- ((After entering a number:))
  - (receives=coins)
  - **Nhitpyx:** There you go!
