# Farmer Fromund

- **Original Wiki Page**: [Transcript:Farmer Fromund](https://runescape.wiki/w/Transcript%3AFarmer%20Fromund)
- **Letter**: `F`

---

## Dialogue Transcript


### On Etceteria, before Royal Trouble

- **Farmer Fromund:** Hey! This is the Queen's farm. You'll need her approval to make use of it.

### Standard dialogue after Royal Trouble

- [Menu]: What would you like to talk about?
  - [Choice]: Farmer Fromund.
    - **Player:** Good day. What are you doing?
    - **Farmer Fromund:** I'm tending to these farming patches. They need a little more work before I can plant anything.
    - [Menu]: Select an option
      - [Choice]: Good luck with that.
        - **Player:** Good luck with that.
        - **Farmer Fromund:** Thank you, [Fremennik name].
      - [Choice]: What's wrong with the patches?
        - **Player:** What's wrong with the patches?
        - **Farmer Fromund:** The centre patch is full of weeds, and as soon as I clear them they grow back. The south patch is always far too dry. And the soil in the north patch is terrible; it needs a good dose of compost.
  - [Choice]: Your approval rating.
    - **Player:** What do people think of me around here?
    - (Condition: If your approval rating is between 25% and 49%:)
      - **Farmer Fromund:** Your people are growing dissatisfied with the regime, Your Royal Highness. At the last poll, only [approval rating]% of the population supported you.
    - (Condition: If your approval rating is between 50% and 74%:)
      - **Farmer Fromund:** You are well regarded, Your Royal Highness. At the last poll, [approval rating]% of the population supported you.
    - (Condition: If your approval rating is at 75% or higher:)
      - **Farmer Fromund:** You are universally adored, Your Royal Highness. At the last poll, [approval rating]% of the population supported you.

### Working on the island

*When player rakes the weedy patch, or waters the dry patch nearby*
- (Condition: Below 100% approval rating:)
  - **Farmer Fromund:** {{RSChat|Thanks!}}
- (Condition: At 100% approval rating:)
  - (Condition: Before Royal Trouble:)
    - **Farmer Fromund:** Don't trouble yourself further, [Sir/Madam], you've already done so much!
  - (Condition: After Royal Trouble:)
    - **Farmer Fromund:** Don't trouble yourself further, Your Highness, you've already done so much!

### Manor Farm


#### Help


##### Before completing the request

- **What would you like to do?**
  - [Choice]: Ask about their request.
    - **Player:** What're you requesting today?
    - **Farmer Fromund:** I've been working on my own farm recently and need a few items to bolster my productivity!
    - **Farmer Fromund:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
    - **Farmer Fromund:** I'm also looking for a new animal, I'm currently after A [animal]
    - **Farmer Fromund:** If you complete this, I'll give you : Farming reputation boon (small) x 1. I'm sure you'll gain some reputation with the farming guild too!
    - **Farmer Fromund:** You'll have to be quick though!, I'm only here for [number] hours and [number] minutes. To be exact.
  - [Choice]: Give them the items & animals for their request
    - ((Without the requested items:))
      - **Farmer Fromund:** You don't have enough items to fulfil my request. I won't take favourited animals.
      - **Farmer Fromund:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
      - **Farmer Fromund:** I'm also looking for a new animal, I'm currently after A [animal]
    - ((With the requested items:))
      - (removes=the requested items) (receives=the reward)
      - ((If a Brassica primer was rewarded:))
        - For completing this request you've received Brassica primer x 1.
        - ((Repeated in a pop-up:))
          - For completing this request you've received Brassica primer x 1.
          - (continue)
      - You've received : Farming reputation boon (small) x 1<br>And 2,750 farming reputation.

##### After completing the request

- **Farmer Fromund:** Thank you for your help!
- [A new request will be available in [time].]

#### Hand in easy request


##### Before completing the request


##### Without requested items

- **Farmer Fromund:** You don't have enough items to fulfil my request. I won't take favourited animals.
- **Farmer Fromund:** I'm trying to get some extra crops going, so I'll need : [Seed] x [number]
- **Farmer Fromund:** I'm also looking for a new animal, I'm currently after A [animal]

##### With requested items

- (removes=the requested items) (receives=the reward)
- ((If a Brassica primer was rewarded:))
  - For completing this request you've received Brassica primer x 1.
  - ((Repeated in a pop-up:))
    - For completing this request you've received Brassica primer x 1.
    - (continue)
- You've received : Farming reputation boon (small) x 1 <br>And 2,750 farming reputation.

##### After completing the request

- You've already completed this request, there will be a new daily request in [time]..
