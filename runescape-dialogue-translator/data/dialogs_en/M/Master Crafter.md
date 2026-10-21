# Master Crafter

- **Original Wiki Page**: [Transcript:Master Crafter](https://runescape.wiki/w/Transcript%3AMaster%20Crafter)
- **Letter**: `M`

---

## Dialogue Transcript


### Attempting to enter the Crafting Guild with under 40 Crafting

- **Master Crafter:** Sorry, only experienced crafters are allowed in here. You must be level 40 or above to enter.

### Entering the Crafting Guild with 40 Crafting

- **Master Crafter:** Welcome to the Guild of Master Craftsmen.

### Standard dialogue

- **Master Crafter:**  Hello, and welcome to the Crafting Guild. Accomplished crafters from all over the land come here to use our top notch workshops.
- [Menu]: What would you like to ask?
  - [Choice]: What can I do here?
    - **Master Crafter:** The upper landing of the crafting guild has everything you need to tailor armour.
    - **Master Crafter:** In brief, you spin plant fibres into thread at a spinning wheel, then weave the thread into cloth at the loom.
    - **Master Crafter:** Next, choose a design for your cloth at the pattern table, draft your project at the drafting table, and finish it at a tailor's dummy.
    - **Master Crafter:** When you've fully upgraded your armour, you can adorn a full set on the tailor's display. It's an admirable experience.
    - **Master Crafter:** But first, you'll need seeds to plant in flower patches to get the flowers you'll spin into thread.
    - **Master Crafter:** I don't know much about starblooms. You might be able to find out more at the Wizards' Tower's big telescope.
    - **Player:** Alright, I'll ask Wizard Rosalina. It might have something to do with shooting stars.
    - **Master Crafter:** Another thing you might like to try is crafting and enchanting platinum jewellery.
    - [You can mine platinum ore north of Uzer and south of Piscatoris.]
    - **Master Crafter:** If you're really good at crafting, you could also have a crack at masterwork magic armour. You can find the recipe on the pattern table beside me.
    - **Master Crafter:** Remember, cloth on a loom. Thread on a spinning wheel. As for stones of binding, maybe try the Wizards' Guild in Yanille.
    - **Master Crafter:** And you'll need tectonic and praesulic essence to start crafting pearlescent plates. Platinum normally wouldn't be suitable for armour, but imbuing negates that.
    - (initial)
  - [Choice]: Trading Summoning focus parts.
    - (below|Trade Summoning Focus Parts)
  - [Choice]: Custom-fitting masterwork armour.
    - **Master Crafter:** If you've got a fully equipped set of trimmed melee masterwork, masterwork ranged or masterwork magic, I can custom fit it for you. If it's augmented it'll remain augmented and you'll repair it the same way you repair trimmed masterwork.
    - **Player:** What does custom-fitting do?
    - **Master Crafter:** It will become untradeable.
    - **Master Crafter:** It will degrade 50% slower so it'll last longer.
    - **Master Crafter:** It will also never degrade when damaged by your current Slayer/Reaper target.
    - **Master Crafter:** But the process is irreversable. Once custom fitted, your masterwork will always be custom fitted.
    - (Condition: While not wearing a full masterwork melee, ranged or magic set:)
      - [You must be wearing a full set of trimmed melee masterwork, masterwork ranged or masterwork magic to custom-fit it.]
    - (Condition: While wearing a full masterwork magic set:)
      - [Are you sure you want to custom-fit your masterwork armour? This process will make them permanently un-tradeable, make them degrade 50% slower and never degrade when damaged by your current Slayer/Reaper target.]
      - [Menu]: Custom-fit your masterwork armour?
        - [Choice]: Yes
          - ((all worn masterpiece armour is custom-fit))
      - [Choice]: No
          - (end)
    - (Condition: While wearing a full masterwork ranged set:)
      - [Are you sure you want to custom-fit your masterwork armour? This process will make them permanently un-tradeable, make them degrade 50% slower and never degrade when damaged by your current Slayer/Reaper target.]
      - [Menu]: Custom-fit your masterwork armour?
        - [Choice]: Yes
          - ((all worn masterpiece armour is custom-fit))
      - [Choice]: No
          - (end)
  - [Choice]: Skillcapes.
    - [Menu]: What about skillcapes?
      - [Choice]: Skillcape of Crafting.
        - (Condition: If the player does not have 99 Crafting:)
          - **Player:** Hey, what is that cape you're wearing? I don't recognise it.
          - **Master Crafter:** This? This is a Skillcape of Crafting. It is a symbol of my ability and standing here in the Crafting Guild. If you should ever achieve 99 Crafting come and talk to me and we'll see if we can sort you out with one.
        - (Condition: If the player has 99 Crafting and has a ring of charos (a) equipped:)
          - **Master Crafter:** I don't do this for anyone, but I've got a special offer today! Normally I require 99,000 coins for this prestigious item, but for you it's half price. Only 92,000 coins!
          - [Menu]: Choose an option:
            - [Choice]: 92,000 coins? That's much too expensive.
              - **Player:** I know where to find you if I change my mind.
            - [Choice]: I think I have the money right here, actually.
              - (Condition: If the player has no backpack space:)
                - **Master Crafter:** Unfortunately all skillcapes are only available with a free hood, it's part of a skill promotion deal; buy one get one free, you know. So, you'll need to free up some backpack space before I can sell you one.
              - (Condition: If the player does not have enough money:)
                - **Player:** But unfortunately, I was mistaken.
                - **Master Crafter:** Well, come back and see me when you do.
              - (Condition: If the player has enough money:)
                - (receives=Crafting cape and Crafting hood) (removes=92,000 coins)
                - **Master Crafter:** Excellent! Wear that cape with pride my friend.
            - [Choice]: cond=If the player has 120 Crafting|I've mastered this skill. Is there anything else?
              - **Master Crafter:** There is something...though I have kept it a secret for a very long time. It is something that can only be worn by a true master.
              - **Master Crafter:** Not even I can wear it - that's how hard it is to achieve.
              - **Master Crafter:** You say you're a master. Stand straight, let me take a look at you…
              - **Master Crafter:** You...really have mastered it. What an honour! It would be my pleasure to sell you a Crafting master cape.
              - [Menu]: Buy Crafting master cape for 120,000 coins?
                - [Choice]: Yes.
                  - (Condition: If the player has no backpack space:)
                    - **Master Crafter:** You do not have enough room in your backpack. Please come back when you have some more.
                  - (Condition: If the player does not have enough money:)
                    - You do not have enough money to purchase this cape.
                  - (Condition: If the player has enough money:)
                    - (receives=Crafting master cape) (removes=120,000 coins)
                    - {{qact|Master cape music plays.}}
                - [Choice]: No.
                  - (end)
        - (Condition: If the player has 99 Crafting but does not have a ring of charos (a) equipped:)
          - [Menu]: Choose an option:
            - [Choice]: 99,000 coins? That's much too expensive.
              - **Player:** I know where to find you if I change my mind.
            - [Choice]: I think I have the money right here, actually.
              - (Condition: If the player has no backpack space:)
                - (above)
              - (Condition: If the player does not have enough money:)
                - (above)
              - (Condition: If the player has enough money:)
                - (receives=Crafting cape and Crafting hood) (removes=99,000 coins)
                - **Master Crafter:** Excellent! Wear that cape with pride my friend.
            - [Choice]: cond=If the player has 120 Crafting|I've mastered this skill. Is there anything else?
              - (above)
      - [Choice]: cond=If the player has 99 Crafting|I've noticed there are a couple of versions of each skillcape.
        - **Master Crafter:** Yes! We, the skill masters, have crafted new versions of all skillcapes! We felt like it was time for a change.
        - (Condition: If the player is using the old model:)
          - **Master Crafter:** It looks like you're currently using the old model for your Crafting skillcape. Would you like to change to the newer one?
          - (continue)
        - (Condition: If the player is using the new model:)
          - **Master Crafter:** You can still choose to wear the old model skillcape if you want. Would you like to change which model you are currently using?
          - (continue)
        - [Menu]: Select an Option
          - [Choice]: Yes, I would like to wear the [new/old] version of the skillcape.
            - **Master Crafter:** Would you like to wear the [old/newer] model for just this cape, or for the Quest Cape and all of the skillcapes you own?
            - [Menu]: Select an Option
              - [Choice]: I would just like to change the Crafting skillcape.
                - **Master Crafter:** No problem, you will now use the [older/newer] model for your Crafting skillcape.
              - [Choice]: I would like to change all my skillcapes.
                - **Master Crafter:** No problem, you will now use the [older/newer] model for all of your skillcapes!
              - [Choice]: I've changed my mind!
                - (end)
          - [Choice]: No, thank you.
            - **Master Crafter:** Great! I'm glad you're still enjoying the [old/new] version!
            - (Condition: If the player uses the new model for any other skillcape:)
              - **Master Crafter:** If you want, I can make it so you use the old model for all of the skillcapes you own.
              - [Menu]: Select an Option
                - [Choice]: Ok, I'd like to wear the old version for all my skillcapes.
                  - **Master Crafter:** Great, you will now use the old model for all of your skillcapes!
                - [Choice]: No, thanks.
                  - (end)

### Trade Summoning Focus Parts


#### Without focus parts, or on a free-to-play world

- **Master Crafter:** You don't have any Summoning focus parts on you. You can obtain them by using a Crafting Catalyst. If you get any parts I can exchange them for you.

#### With focus parts

- **Player:** I'd like to exchange some parts of the Summoning focus, please.
- {{anchor|exchange}} **Master Crafter:** Which part would you like to exchange?
- [Menu]: Select part
  - [Choice]: Leather case
    - **Master Crafter:** Okay, and which would you like to swap it for?
    - [Menu]: Select part
      - [Choice]: Leather case
        - **Master Crafter:** That's the same as the one you've already got.
        - (continuea|exchange)
      - [Choice]: Gem focus
        - **Master Crafter:**  How many would you like to swap?
        - {{tinput|Enter amount:}}
          - (Condition: If zero is entered:)
            - (end)
          - ((After entering a positive amount:))
            - ((Player receives one gem focus for each leather case handed in.))
            - **Master Crafter:** There you go, would you like to swap anything else?
            - {{anchor|anything-else}} [Menu]: Select an Option
              - [Choice]: Yes please.
                - (continuea|exchange)
              - [Choice]: No thanks.
                - (end)
      - [Choice]: Metal setting
        - **Master Crafter:**  How many would you like to swap?
        - {{tinput|Enter amount:}}
          - (Condition: If zero is entered:)
            - (end)
          - ((After entering a positive amount:))
            - ((Player receives one metal setting for each leather case handed in.))
            - **Master Crafter:** There you go, would you like to swap anything else?
            - (continuea|anything-else)
  - [Choice]: Gem focus
    - **Master Crafter:** Okay, and which would you like to swap it for?
    - [Menu]: Select part
      - [Choice]: Leather case
        - **Master Crafter:**  How many would you like to swap?
        - {{tinput|Enter amount:}}
          - (Condition: If zero is entered:)
            - (end)
          - ((After entering a positive amount:))
            - ((Player receives one leather case for each gem focus handed in.))
            - **Master Crafter:** There you go, would you like to swap anything else?
            - (continuea|anything-else)
      - [Choice]: Gem focus
        - **Master Crafter:** That's the same as the one you've already got.
        - (continuea|exchange)
      - [Choice]: Metal setting
        - **Master Crafter:**  How many would you like to swap?
        - {{tinput|Enter amount:}}
          - (Condition: If zero is entered:)
            - (end)
          - ((After entering a positive amount:))
            - ((Player receives one metal setting for each gem focus handed in.))
            - **Master Crafter:** There you go, would you like to swap anything else?
            - (continuea|anything-else)
  - [Choice]: Metal setting
    - **Master Crafter:** Okay, and which would you like to swap it for?
    - [Menu]: Select part
      - [Choice]: Leather case
        - **Master Crafter:**  How many would you like to swap?
        - {{tinput|Enter amount:}}
          - (Condition: If zero is entered:)
            - (end)
          - ((After entering a positive amount:))
            - ((Player receives one leather case for each metal setting handed in.))
            - **Master Crafter:** There you go, would you like to swap anything else?
            - (continuea|anything-else)
      - [Choice]: Gem focus
        - **Master Crafter:**  How many would you like to swap?
        - {{tinput|Enter amount:}}
          - (Condition: If zero is entered:)
            - (end)
          - ((After entering a positive amount:))
            - ((Player receives one gem focus for each metal setting handed in.))
            - **Master Crafter:** There you go, would you like to swap anything else?
            - (continuea|anything-else)
      - [Choice]: Metal setting
        - **Master Crafter:** That's the same as the one you've already got.
        - (continuea|exchange)
  - [Choice]: Cancel
    - (end)

### Custom-fit Trimmed Masterwork

- (above|custom-fit-dialogue)

### During the Master Crafting event


#### Entering the Crafting Guild

- **Master Crafter:** Welcome to the Guild of Master Craftsmen.
- **Master Crafter:** We're currently running a master crafting event! Come and speak to me for more information.

#### Getting a Crafting level

- **Master Crafter:** {{RSChat|Congratulations for advancing a crafting level, Player!}}

#### Attempting to use the Temporary Bank chest before unlocking it

- **Master Crafter:** Sorry you can't use that bank chest until you've unlocked it as part of the Master Crafting event. If you hand in at least 800 Master Crafting patches to me I'll unlock it for you.

#### Talk to

- **Master Crafter:** Hello, and welcome to the Crafting Guild. We're running a master crafting event currently, we're inviting crafters from all over the land to come here and use our top notch workshops!
- [Menu]: What would you like to ask about?
  - [Choice]: The master crafting event!
    - **Master Crafter:** Yes, welcome to the crafting guild and our master crafting event!
    - **Master Crafter:** What can I help you with?
    - [Menu]: What would you like to ask?
      - [Choice]: How does this event work?
        - **Player:** How does this work?{{anchor|how}}
        - **Master Crafter:** Well, I've opened the crafting guild doors to all adventurers, so everyone can take part.
        - **Master Crafter:** Throughout the world you may find crafting patches whilst doing any skilling, combat activities or daily challenges.
        - **Master Crafter:** If you bring these patches to me I can grant you some awesome rewards and benefits!
        - [Menu]: What would you like to ask?
          - [Choice]: What awesome rewards?
            - **Master Crafter:** Rewards, ah yes!{{anchor|rewards}}
            - **Master Crafter:** I have a whole selection of cosmetics to give away!
            - **Master Crafter:** Like these amazing boots I'm wearing!
            - **Master Crafter:** And these exceptional gloves!
            - **Player:** Your whole outfit?
            - **Master Crafter:** Yes.
            - You can unlock the master crafter outfit containing : Goggles, Chestpiece, Trousers, Gloves & Boots
            - **Player:** Can I get anything else?
            - **Master Crafter:** Of course! I've got an assortment of tools you can use for all your monster-killing needs!
            - **Master Crafter:** A screwdriver, which could be used like a dagger.
            - **Master Crafter:** A hammer, which could be used like a mace.
            - **Master Crafter:** A saw, which could be used like a scimitar!
            - **Master Crafter:** And a hatchet, which you know could be used for hatcheting.
            - You can unlock various master crafting weapon overrides : A saw, A hatchet, A screwdriver & A hammer'
            - [Menu]: What would you like to ask?
              - [Choice]: How does this event work?
                - (above|how)
              - [Choice]: Are there any other benefits?
                - **Player:** Are there any other benefits I can get from this event?{{anchor|benefits}}
                - **Master Crafter:** Of course! I've managed to sort out all sorts of crafting guild benefits that will run for the duration of the event!
                - **Master Crafter:** If you're inside the guild, I've managed to sort out an experience buff for all skills of +5% XP, for the entire event!
                - **Master Crafter:** I've also managed to sort out a +10% XP buff to crafting, and they stack together!
                - **Master Crafter:** If you've donated at least 800 currency you can use this helpful bank chest I've hauled to the guild.
                - **Master Crafter:** I will be removing it after the event though, it's on loan and I can't afford to keep it here!
                - **Master Crafter:** If you've donated at least 5,000 currency you'll receive a jewellery crafting buff!
                - Jewellery crafting buff (within the crafting guild) :
                - +250% XP when smelting Gold & Silver Bars
                - +50% faster Gold & Silver smelting
                - +33% faster Gold & Silver casting.
                - **Master Crafter:** If you've donated at least 10,000 currency you'll receive a mining buff!
                - Mining buff (within the crafting guild) :
                - +50% XP when mining Gold & Silver rocks
                - Mining Clay now gives soft clay instead.
                - **Master Crafter:** If you've donated at least 20,000 currency you'll receive an urn crafting buff!
                - Urn crafting buff (within the crafting guild) :
                - +50% faster Pottery wheel crafting
                - +80% faster pottery oven crafting
                - +100% XP when crafting urns
                - **Master Crafter:** I really hope you'll enjoy these benefits, however they'll dissappear after the event is over, I've only managed to secure them for a short time.
                - **Master Crafter:** Is there anything else I can help you with?
                - [Menu]: What would you like to ask?
                  - [Choice]: How does this event work?
                    - (above|how)
                  - [Choice]: What rewards can I get?
                    - (above|rewards)
          - [Choice]: What awesome benefits?
            - (above|benefits)
          - [Choice]: I'd like to hand in currency!
            - (below|Hand in)
          - [Choice]: Wait, how do I get those patches?
            - **Master Crafter:** You get the patches from combat, skilling or daily challenges.
            - [Menu]: What would you like to ask?
              - [Choice]: What rewards can I get?
                - (above|rewards)
              - [Choice]: re there any other benefits?
                - (above|benefits)
              - [Choice]: I'd like to hand in currency!
                - (below|Hand in)
              - [Choice]: But how?
                - **Player:** But how?
                - *(Only on first time:)*
                  - **Player:** How do monsters have these patches?, How do they appear while I'm crafting?
                  - (continue)
                - *(One of the following is shown, and then returns to the previous options:)*
                  - **Master Crafter:** Because I have a really, really, really, good friendshiop with the world guardian.
                  - **Master Crafter:** Because I said so.
                  - **Master Crafter:** Because I spent a long time giving to every monster ever.
                  - **Master Crafter:** Because I've had nothing better to do for the last 11 years.
                  - **Master Crafter:** Because someone is following you around, subtley throwing patches into your backpack.
                  - **Master Crafter:** Because the creators said so.
                  - **Master Crafter:** Because you'll accidently create them?
                  - **Master Crafter:** Because you'll find them.
                  - **Master Crafter:** Magic.
                  - **Master Crafter:** Please don't ask me how again.
                  - **Master Crafter:** Reasons.
                  - **Master Crafter:** You know how you buy a shirt sometimes, and it just comes with extra sweets? It's like that but with patches.
      - [Choice]: What rewards can I get?
        - (above|rewards)
      - [Choice]: Are there any other benefits?
        - (above|benefits)
      - [Choice]: I'd like to hand in currency!
        - (below|Hand in)
  - [Choice]: Skillcape of Crafting.
    - *(Non-event dialogue.)*
  - [Choice]: I've noticed there are a couple of versions of each skillcape.
    - *(Non-event dialogue.)*
  - [Choice]: A Summoning focus.
    - *(Non-event dialogue.)*

#### Hand in


##### During the event


##### Without master crafting patches

- You do not have anything to hand in.

##### With master crafting patches


##### With rewards left to unlock

- Redeem currency
- Handing in event currency will increase your progress for this event unlocking unique rewards. This will remove currency up to the amount that is required to complete the event.
- [Menu]: Do you wish to continue?
  - [Choice]: No
    - (end)
  - [Choice]: Yes
    - You hand in [number] Master crafting patches. You need to hand in [numberK or number] more to complete the event.
    - ((If rewards weren't unlocked, and no rewards have been unlocked previously:))
      - **Master Crafter:** You need to bring me more crafting patches if you want to claim more rewards.
    - ((If rewards were unlocked:))
      - ((If the bank chest is unlocked:))
        - Congratulations, you've unlocked the ability to use the bank chest within the crafting guild for the events duration.
        - (continue)
      - ((If the master crafter goggles are unlocked:))
        - Congratulations, you have unlocked the Master Crafter goggles override. You can find this in the customisations interface.
        - (continue)
      - ((If the master crafter saw is unlocked:))
        - Congratulations, you have unlocked the Master Crafter saw override. You can find this in the customisations interface.
        - (continue)
      - ((If the jewellery benefits are unlocked:))
        - You have the following jewellery casting benefits within the crafting guild for the events duration.
        - +250% XP when smelting Gold and Silver bars.
        - +50% faster Gold and Silver smelting.
        - +33% faster Gold and Silver casting.
        - (continue)
      - ((If the master crafter gloves are unlocked:))
        - Congratulations, you have unlocked the Master Crafter gloves override. You can find them in the customisations interface.
        - (continue)
      - ((If the master crafter boots are unlocked:))
        - Congratulations, you have unlocked the Master Crafter boots override. You can find them in the customisations interface.
        - (continue)
      - ((If the mining benefits are unlocked:))
        - You have the following jewellery casting benefits within the crafting guild for the events duration.
        - +50% XP when mining Gold and Silver rocks.
        - Mining Clay now gives soft clay instead.
        - (continue)
      - ((If the master crafter trousers are unlocked:))
        - Congratulations, you have unlocked the Master Crafter trouser override. You can find them in the customisations interface.
        - (continue)
      - ((If the master crafter chestpiece is unlocked:))
        - Congratulations, you have unlocked the Master Crafter chestpiece override. You can find them in the customisations interface.
        - (continue)
      - ((If the master crafter hammer is unlocked:))
        - Congratulations, you have unlocked the Master Crafter hammer override. You can find this in the customisations interface.
        - (continue)
      - ((If the master crafter screwdriver is unlocked:))
        - Congratulations, you have unlocked the Master Crafter screwdriver override. You can find this in the customisations interface.
        - (continue)
      - ((If the master crafter hatchet is unlocked:))
        - Congratulations, you have unlocked the Master Crafter hatchet override. You can find this in the customisations interface.
        - (continue)
      - ((If the urn benefits are unlocked:))
        - You have completed the event!
        - You have the following urn crafting benefits within the crafting guild for the events duration.
        - +50% faster crafting using the pottery wheel.
        - +80% faster crafting using the pottery oven.
        - +100% XP when crafting urns.
        - (continue)
      - (continue)
    - ((If some of the rewards have been unlocked:))
      - You have unlocked [number]/13 of the rewards for the Master Crafter event.
      - ((If there are still rewards to unlock, and either no reward or the bank chest was just unlocked:))
        - **Master Crafter:** We have more rewards to offer, should you bring me more skill tokens.
      - ((If a reward other than the bank chest was just unlocked:))
        - **Master Crafter:** There you are!

##### With all rewards unlocked

- You have handed in as much currency as you can this event. You can convert any remaining currency into consumable rewards.

##### After the event

- The master crafter event has finished, however you can still convert your left over tokens to mystery boxes.
- ((Continues with normal dialogue.))

#### Open event


##### During the event

- (opens=Master Crafting{{!)Event}}

##### After the event

- The master crafter event has finished, however you can still convert your left over tokens to mystery boxes.
- ((Continues with normal dialogue.))
