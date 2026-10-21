# Not-So-Secret-Santa

- **Original Wiki Page**: [Transcript:Not-So-Secret-Santa](https://runescape.wiki/w/Transcript%3ANot-So-Secret-Santa)
- **Letter**: `N`

---

## Dialogue Transcript

{{Incomplete|Verify Ironman dialogue for gift donation, claiming another gift with various time remaining, and daily reward progress}}

### Talk to

- [Menu]: Select an Option
  - [Choice]: Who are you?
    - **Not-So-Secret-Santa:** I'm Santa, but Ssshhhh! It's a secret!
    - **Player:** How is it a secret if you're dressed like him?
    - **Not-So-Secret-Santa:** That's the idea! If I dress like him, nobody should suspect that I AM him.
    - **Player:** Right.
    - **Player:** What are you doing here?
    - **Not-So-Secret-Santa:** I'm hosting a big game of Secret Santa this year!
    - (initial)
  - [Choice]: Can you tell me about the Secret Santa?
    - **Not-So-Secret-Santa:** There are two phases to Secret Santa.
    - **Not-So-Secret-Santa:** Phase one: Donate. Individuals can donate their hard-earned items into my bag. I will distribute them in phase two.
    - **Not-So-Secret-Santa:** We don't want any tat, so there is a minimum donation value. Whatever you give must be worth at least 50,000 coins on the Grand Exchange.
    - **Not-So-Secret-Santa:** I've got special rewards too - for anyone going above and beyond. Each day I can give you a medium prismatic lamp for donations totalling 100,000 coins in value.
    - **Not-So-Secret-Santa:** If you do this 15 times, I can give you the title of Secret Santa!
    - **Not-So-Secret-Santa:** There is a special title for those that donate 200,000,000 coins in one go: the Top Secret Santa!
    - **Not-So-Secret-Santa:** Phase two: Gift. Anyone can ask me for a present, and I will randomly select an item from my stores to give them.
    - **Not-So-Secret-Santa:** Don't get greedy though, eh? I'll only let you take a gift once every 3 hours.
    - (initial)
  - [Choice]: I'd like to donate to the Secret Santa.
    - (below|Donate gift)
  - [Choice]: I'd like to claim a gift from the Secret Santa.
    - (below|Claim gift)
  - [Choice]: Can you tell me about my daily reward progress?
    - ((Having donated 50,000–99,000 value today:))
      - **Not-So-Secret-Santa:** You need to donate items totalling at least a value of [number] coins to receive a daily reward.
      - (continue)
    - ((Not having donated today or having reached the daily 100,000 value:))
      - **Not-So-Secret-Santa:** You have donated enough wealth to receive your daily reward today. If you haven't collected it from me you can claim it like you would claim a standard Secret Santa gift.
      - (continue)
    - ((Without Secret Santa unlocked:))
      - **Not-So-Secret-Santa:** You need to donate enough to claim a daily reward on [number] more days to receive the Secret Santa title.
      - (initial)
    - ((With Secret Santa unlocked:))
      - **Not-So-Secret-Santa:** You have donated items of high enough value on enough days to receive the Secret Santa title already.
      - (initial)

### Donate gift


#### Outside Ironman Mode


##### With items stored

- [You have rewards you must claim or abandon before you can donate any more items.]

##### Without items stored

- ((Gift Donation interface opens.))
- (Condition: Attempting to donate items worth less than 50,000 coins:)
  - You cannot donate items that are worth less than 50,000 coins.
  - (pop-up)
    - {{Pop-up|You cannot donate items that are worth less than 50,000 coins.|warning=yes}}
- ((After donating a gift with a value over 100,000 coins for the first time of the day:))
  - ((Gift Claim interface opens with a medium prismatic lamp.))
  - For donating 100,000 coins worth of items today, you have been awarded a medium prismatic lamp.
  - (pop-up)
    - {{Pop-up|For donating 100,000 coins worth of items today, you have been awarded a medium prismatic lamp.|colour=#00FF00}}
    - (continue)
  - ((Taking the lamp to backpack directly:))
    - (receives=medium prismatic lamp)
    - ((The interface closes.))
    - The chest is now empty.
  - ((Attempting to bank the lamp directly:))
    - The item could not be added to your bank.
  - ((Discarding the lamp directly:))
    - ((The following is shown in an interface titled "ABANDON ITEM":))
      - Are you sure you want to discard this item?
        - [Choice]: NO
          - ((The interface closes.))
        - [Choice]: YES
          - ((The whole Gift Claim interface closes.))
  - [Choice]: BANK ALL
    - ((Shown in a pop-up:))
      - {{Pop-up|The items could not be added to your bank.|warning=yes}}
  - [Choice]: TAKE ALL
    - (receives=medium prismatic lamp)
    - ((The interface closes.))
    - All the items were moved to your inventory.
    - (pop-up)
      - {{Pop-up|All the items were moved to your inventory.|colour=#00FF00}}
      - (continue)
    - The chest is now empty.
  - [Choice]: ABANDON ALL
    - ((The following is shown in an interface titled "ABANDON ITEM":))
      - Abandon all remaining items in the chest?
        - [Choice]: NO
          - ((The interface closes.))
        - [Choice]: YES
          - ((Both interfaces close.))

#### In Ironman Mode

- As an Ironman you cannot partake in the greatest joy of all - gift giving. All donations from Ironmen will be destroyed in a controlled explosion in accordance with standard Ironman rules of engagement. Any remaining residue will be destroyed in a second, larger, explosion. Your wealth will not be transferred to other players, but you will be able to receive cosmetic titles for your donations, and progress for related yak track tasks.
- Would you still like to donate items?
  - Yes.
    - ((Gift Donation interface opens.))
  - Yes and don't ask me again.
    - ((Gift Donation interface opens.))
  - No.
    - (end)

### Claim gift


#### Without having claimed a gift in the last 3 hours

- ((Gift Claim interface opens.))
- ((If the player walks away or otherwise closes the gift claim interface without taking or banking the gifts:))
  - {{Colour|#003366|WARNING:}} If you log out, items in the reward chest will be moved to your inventory or bank. If both of those places are full you will lose the items.
- ((Taking the gift to backpack directly:))
  - ((The interface closes.))
  - (receives=gift)
  - The chest is now empty.
- ((Banking the gift directly:))
  - ((The interface closes.))
  - ((The player banks the gift, or has coins added to money pouch if it's coins.))
  - The chest is now empty.
- ((Discarding the gift directly:))
  - ((The following is shown in an interface titled "ABANDON ITEM":))
    - Are you sure you want to discard this item?
      - [Choice]: NO
        - ((The interface closes.))
      - [Choice]: YES
        - ((The whole Gift Claim interface closes.))
- [Choice]: BANK ALL
  - ((The interface closes.))
  - All of the items were moved to your bank.
  - (pop-up))
    - {{Pop-up|All of the items were moved to your bank.|colour=#00FF00}}
    - (continue)
  - The chest is now empty.
- [Choice]: TAKE ALL
  - (Condition: Without sufficient backpack space:)
    - (pop-up))
      - {{Pop-up|The items could not be added to your inventory.|warning=yes}}
  - (Condition: With sufficient backpack space:)
    - ((The interface closes.))
    - (receives=gift)
    - All the items were moved to your inventory.
    - (pop-up)
      - {{Pop-up|All the items were moved to your inventory.|colour=#00FF00}}
      - (continue)
    - The chest is now empty.
- [Choice]: ABANDON ALL
  - ((The following is shown in an interface titled "ABANDON ITEM":))
    - Abandon all remaining items in the chest?
      - [Choice]: NO
        - ((The interface closes.))
      - [Choice]: YES
        - ((Both interfaces close.))

#### Having claimed a gift in the last 3 hours

- You can collect another gift in [time].
- (pop-up)
  - {{Pop-up|You can collect another gift in [time].|warning=yes}}
