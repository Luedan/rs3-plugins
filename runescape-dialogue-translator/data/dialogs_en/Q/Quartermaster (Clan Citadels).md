# Quartermaster (Clan Citadels)

- **Original Wiki Page**: [Transcript:Quartermaster (Clan Citadels)](https://runescape.wiki/w/Transcript%3AQuartermaster%20%28Clan%20Citadels%29)
- **Letter**: `Q`

---

## Dialogue Transcript

{{Incomplete|Needs dialogue for updating the job list and changing the build tick}}

### In the Clan Citadel


#### Talking to him

- **Quartermaster:** Good day to you! How may I assist?
- [Menu]: Choose an option:
  - [Choice]: What do you do here?
    - **Quartermaster:** I'm the quartermaster for your clan. I keep track of the jobs you or your clanmates have marked to be undertaken within the citadel; the resources it will take; and whether you can meet that requirement.
    - **Quartermaster:** I am also capable of altering the day on which your buildings are altered and the resources used up, and I can award bonus experience.
    - [Menu]: Select an Option
      - [Choice]: Tell me more about the job list.
        - **Quartermaster:** On the job list you will see all downgrades, upkeep dues, and upgrade requests pending for your clan's citadel. Upkeep jobs will remain as long as you have a building in your citadel requiring upkeep; the others are removed when they are carried out.
        - **Quartermaster:** You may click on jobs in the list to view more information regarding their costs, and the resources available to perform those jobs, and any warnings related to jobs which currently have shortfall or unmet requirements.
        - **Quartermaster:** If you have the requisite access permissions from your clan's officers, you may alter the list by dragging jobs to reorder them, or to cancel downgrade or upgrade jobs.
        - **Quartermaster:** You may also jump from upgrade jobs to the build interface to make alterations if need be, but that's more the artisan's area than mine, quite frankly.
        - [Menu]: Would you like to open the list now?
          - [Choice]: Yes
            - *(Job list interface opens)*
          - [Choice]: No
            - (end)
      - [Choice]: Tell me about moving the build tick.
        - The owner, deputy or overseer of a clan may move the build tick to a day of the week and time of day more suitable for your clan's activity. Just talk to me about it and I will set your build tick to be due precisely one week from that moment.
        - **Quartermaster:** I must warn you, though, that it will cost you a week's upkeep up front to do so. You will be allowed to do it only once per week and you may not move the tick to the same day on which it already falls.
        - **Quartermaster:** Moving the build tick will also not carry out any upgrade or downgrade jobs you have listed.
        - [Menu]: Do you wish to move the build tick?
          - [Choice]: Yes
            - (Condition: If clan rank is high enough:)
              - {{Transcript missing}}
            - (Condition: If clan rank is not high enough:)
              - Your rank is not high enough to move your clan's build/upkeep day.
          - [Choice]: No
            - (end)
      - [Choice]: About experience boosts...
        - (Condition: If the player has been in the clan for less than 1 week, and received bonus experience within 1 week:)
          - **Quartermaster:** I'm afraid I've given you experience rather recently, and as you're new to the clan I can't give you more for at least another day.
        - (Condition: If the player has already received bonus experience for the current build cycle:)
          - **Quartermaster:** I've already given you some experience; I won't be able to give you more until after the next build cycle.
        - (Condition: If the player has not yet received bonus experience for the current build cycle:)
          - [Menu]: Select an Option
            - [Choice]: Can you give me some experience?
              - **Quartermaster:** As you work for your clan, gathering resources we need for building and maintaining the Stronghold, you will make progress towards earning an experience boost. You will be able to use up the bonus experience both here in the citadel and out in the rest of the world.
              - **Quartermaster:** I must warn you that I can only provide one bonus per week.
              - **Quartermaster:** Now, let's see...
              - (Condition: If the player has not yet gathered enough resources for the current build cycle:)
                - **Quartermaster:** Our records show that you have done no work for us this week.
              - (Condition: If the player has not yet gathered enough resources for the current build cycle:)
                - **Quartermaster:** Yes; you've done enough work to earn experience. Which skill would you like it in?
                - ((Skill selection interface opens.))
            - [Choice]: How can I earn bonus experience?
              - **Quartermaster:** Earning the boost is simply a matter of working in any of our resource-gathering buildings, from the Woodcutting tree up to the Summoning grove. Once you've gathered enough, spread however you wish between the plots available to the clan, I can grant you the bonus.
              - (previous)
            - [Choice]: I'm here for an experience boost
              - (Condition: If the player has not yet gathered enough resources for the current build cycle:)
                - **Quartermaster:** I'm terribly sorry. You'll need to do more work before I can give you experience.
              - (Condition: If the player has not yet gathered enough resources for the current build cycle:)
                - **Quartermaster:** Yes; you've done enough work to earn experience. Which skill would you like it in?
                - ((Skill selection interface opens.))
  - [Choice]: I'd like to check the Job list.
    - *(Job list interface opens)*
  - [Choice]: I'd like to move the Clan's build tick.
    - (Condition: If clan rank is high enough:)
      - {{Transcript missing}}
    - (Condition: If clan rank is high enough:)
      - Your rank is not high enough to move your clan's build/upkeep day.
  - [Choice]: About bonus experience...
    - (above|bxp)
  - [Choice]: Can you sell me some Clan Citadel Boosters?
    - **Quartermaster:** Of course! How many do you want?
    - [Menu]: How many would you like to buy?
      - [Choice]: One.
        - (Purchase interface opens up for Clan Citadel Booster (x1) for 100 RuneCoins)
      - [Choice]: Three.
        - (Purchase interface opens up for Clan Citadel Booster (x3) for 250 RuneCoins)
      - [Choice]: Six.
        - (Purchase interface opens up for Clan Citadel Booster (x6) for 450 RuneCoins)
      - [Choice]: None, I changed my mind.
        - (end)

#### Move tick option

- (above|move)

#### Claim XP option

- (above|claim)
