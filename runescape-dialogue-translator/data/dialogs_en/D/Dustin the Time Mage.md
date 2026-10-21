# Dustin the Time Mage

- **Original Wiki Page**: [Transcript:Dustin the Time Mage](https://runescape.wiki/w/Transcript%3ADustin%20the%20Time%20Mage)
- **Letter**: `D`

---

## Dialogue Transcript


### Talk to


#### During the event

- (Condition: Only on the first time:)
  - {{#vardefineecho:Dustin|**Dustin {{Colour|#d1be88|the Time Mage}}:**}} Hello there. Good to meet you!
  - {{#var:Dustin}} I don't suppose I could ask a favour? You see, I may have created a crack in time itself...
  - **Player:** You've done what?
  - {{#var:Dustin}} Let me explain. Have you heard the time altar has been discovered?
  - {{#var:Dustin}} Of course I was excited at the concept of a new rune, and with it the new spells we can cast!
  - {{#var:Dustin}} But I thought to myself: what if there was even more we could accomplish with this new magic? So I started to experiment...
  - {{#var:Dustin}} However, things got out of hand and... well... I may have created a tear in the time altar's realm. Nothing too serious. Just a small hole.
  - {{#var:Dustin}} Through that hole, however, the Sands of Time appear to be escaping! I could do with a helping hand to get it all back while I plug the hole.
  - {{#var:Dustin}} As long as we work together I'm sure nothing terrible will happen in the mean time, like the end of the universe.
  - **Player:** Let me recap. You want me to find and gather the Sands of Time and return them to you while you repair the 'hole' to stop the potential end of the universe?
  - {{#var:Dustin}} Exactly that! Glad you're following! Now get going! Or do you have any more questions?
  - (continue|1)
- (Condition: Afterwards:)
  - {{#var:Dustin}} Good to see you again, Player.
  - (continue|1)
- [Menu]: Choose an option:
  - [Choice]: What is going on?
    - (continuea|Let-me-explain)
  - [Choice]: How do I gather Sands of Time?
    - {{#var:Dustin}} It's very simple. The Sands of Time seem to be attracted to hard work - if you're doing any of that skilling and killing you adventurers seem fond of, the sands will find their way to you.
    - {{#var:Dustin}} It seems especially fond of those training Runecrafting so you'll find the sand in larger quantities there. I imagine it senses home.
    - {{#var:Dustin}} It appears to be less fond of those of you who stand around banks all day. Makes sense really. If I was a magical sand, I'd more likely sail in the opposite direction too.
    - {{#var:Dustin}} Bring the sand back here and I'll happily reward you for it.
    - (previous|1)
  - [Choice]: What rewards can I get?
    - {{#var:Dustin}} Rewards? Rewards! Of course, couldn't possibly do something for nothing. Hm... let me see... Oh, I know. I can give you a recommendation for a tailor. That outfit is doing nothing for you.
    - **Player:** What kind of reward is that?
    - {{#var:Dustin}} Not good enough? Hm... okay, how about this very outfit? I have a spare you can have.
    - {{#var:Dustin}} And... I have some mystery boxes laying around I never got around to opening. Don't ask what they contain because I don't know; that's what makes it a mystery, but I'm sure they're worth your while.
    - **Player:** I guess that will do.
    - (previous|1)
  - [Choice]: I'd like to hand in some Sands of Time.
    - (below|Hand-in for rewards)
  - [Choice]: Goodbye.
    - {{#var:Dustin}} Until next time.

#### After the event

- {{#var:Dustin}} The Sands of Time are back where they belong! Thanks for your help.
- [Menu]: Choose an option:
  - [Choice]: I'd like to hand in some Sands of Time.
    - (below|Hand-in for rewards)
  - [Choice]: Goodbye.
    - {{#var:Dustin}} Until next time.

### Hand-in for rewards


#### Without Sands of Time

- You do not have anything to hand in.
- (pop-up)
  - {{Pop-up|You do not have anything to hand in.|warning=yes}}

#### With Sands of Time


##### With rewards left to unlock

- ((The following is shown in an interface titled "Redeem Currency":))
  - Handing in event currency will increase your progress for this event unlocking unique rewards. This will remove currency up to the amount that is required to complete the event.
  - Do you wish to continue?
    - [Choice]: No
      - ((The interface closes.))
    - [Choice]: Yes
      - ((The interface closes and the dialogue continues below.))
- (removes=smaller number of all and as many Sands of Time as are missing from handing in 20,000)
- (Condition: If the player hasn't handed in 10,000 Sands of Time:)
  - You hand in [number] Sands of Time. You need to hand in [number]K more to complete the event.
  - (pop-up)
    - {{Pop-up|You hand in [number] Sands of Time. You need to hand in [number]K more to complete the event.}}
    - (continue)
- (Condition: If the player has handed in between 10,000 and 19,999 Sands of Time:)
  - You hand in [number] Sands of Time. You need to hand in [number] more to complete the event.
  - (pop-up)
    - {{Pop-up|You hand in [number] Sands of Time. You need to hand in [number] more to complete the event.}}
    - (continue)
- (Condition: If the player has handed in 20,000 Sands of Time:)
  - You have completed the event!
  - (continue)
- (Condition: Depending on how many sand the player has handed in, some of these are shown, and then continues below:)
  - Congratulations! You've unlocked: Time Mage Boots. Your new item(s) can be found in the Customisations Interface.
  - (pop-up)
    - {{Pop-up|Congratulations! You've unlocked: Time Mage Boots. Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}
    - (continue)
  - Congratulations! You've unlocked: Time Mage Gloves. Your new item(s) can be found in the Customisations Interface.
  - (pop-up)
    - {{Pop-up|Congratulations! You've unlocked: Time Mage Boots. Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}
    - (continue)
  - (Condition: Without backpack space for an event mystery box:)
    - You do not have enough backpack space for some of the rewards. Please make some space and try again.
    - (pop-up)
      - {{Pop-up|You do not have enough backpack space for some of the rewards. Please make some space and try again.|warning=yes}}
      - (continue)
  - (Condition: With backpack space for an event mystery box:)
    - (receives=event mystery box)
    - Congratulations, you have been awarded: 1 x Event mystery box.
    - (continue)
  - Congratulations! You've unlocked: Time Mage Robe Bottom. Your new item(s) can be found in the Customisations Interface.
  - (pop-up)
    - {{Pop-up|Congratulations! You've unlocked: Time Mage Robe Bottom. Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}
    - (continue)
  - Congratulations! You've unlocked: Time Mage Robe Top. Your new item(s) can be found in the Customisations Interface.
  - (pop-up)
    - {{Pop-up|Congratulations! You've unlocked: Time Mage Robe Top. Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}
    - (continue)
  - Congratulations! You've unlocked: Time Mage Hood. Your new item(s) can be found in the Customisations Interface.
  - (pop-up)
    - {{Pop-up|Congratulations! You've unlocked: Time Mage Robe Top. Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}
    - (continue)
  - (Condition: Without backpack space for an event mystery box:)
    - You do not have enough backpack space for some of the rewards. Please make some space and try again.
    - (pop-up)
      - {{Pop-up|You do not have enough backpack space for some of the rewards. Please make some space and try again.|warning=yes}}
      - (continue)
  - (Condition: With backpack space for an event mystery box:)
    - (receives=event mystery box)
    - Congratulations, you have been awarded: 1 x Event mystery box.
    - (continue)
  - You have unlocked the title: 'Player {{Colour{{Colour|#FFFFFF|'}}|colour=#00FF00}}
  - You can activate this via the 'Titles' tab in the 'Customisations' interface.
  - (Condition: Without backpack space for two big event mystery boxes:)
    - You do not have enough backpack space for some of the rewards. Please make some space and try again.
    - (pop-up)
      - {{Pop-up|You do not have enough backpack space for some of the rewards. Please make some space and try again.|warning=yes}}
      - (continue)
  - (Condition: With backpack space for two big event mystery boxes:)
    - (receives=two big event mystery boxes)
    - Congratulations, you have been awarded: 2 x Big event mystery box.
    - (continue)
  - Congratulations! You've unlocked: Shifting Time Mage Outfit. Your new item(s) can be found in the Customisations Interface.
  - (pop-up)
    - {{Pop-up|Congratulations! You've unlocked: Shifting Time Mage Outfit. Your new item(s) can be found in the Customisations Interface.|colour=#00FF00}}
    - (continue)
- (Condition: Without having any rewards unlocked:)
  - {{#var:Dustin}} You'll need to help me some more before I can offer you any rewards.
- (Condition: With some of the rewards unlocked:)
  - You have unlocked [number claimed]/10 of the rewards for the Shifting Sands event.
  - (Condition: If some new rewards were just claimed:)
    - {{#var:Dustin}} Thanks for your help. Time feels a little more stable already.
  - (Condition: If no new rewards were just claimed:)
    - {{#var:Dustin}} I have additional rewards to offer if you can find more Sands of Time.

##### Without rewards left to unlock

- You have handed in as much currency as you can this event. You can convert any remaining currency into consumable rewards.
- (pop-up)
  - {{Pop-up|You have handed in as much currency as you can this event. You can convert any remaining currency into consumable rewards.|colour=#FFC800}}

### Claim rewards


#### With rewards left to unlock

- (above|claim)

#### Without rewards left to unlock

- {{#var:Dustin}} You've already claimed all of the rewards I have to offer. However, you can convert any extra Sands of Time you find into mystery boxes.
- You have unlocked all of the rewards available for this event. You can convert any remaining Sands of Time into mystery boxes.

### Open event


#### During the event

- (opens=Shifting Sands)

#### After the event

- (opens=Interface#Community{{!)Community}}
