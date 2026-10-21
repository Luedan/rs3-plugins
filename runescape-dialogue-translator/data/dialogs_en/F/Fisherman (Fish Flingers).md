# Fisherman (Fish Flingers)

- **Original Wiki Page**: [Transcript:Fisherman (Fish Flingers)](https://runescape.wiki/w/Transcript%3AFisherman%20%28Fish%20Flingers%29)
- **Letter**: `F`

---

## Dialogue Transcript


### Talk to


#### Outside the waiting area

- (Condition: If you are on a free world:)
  - **Fisherman:** Sorry, you'll have to switch to a members' world in order to play Fish Flingers.
  - (continue)
- (Condition: If Fish Flingers hasn't started yet, but you can teleport to the waiting area:)
  - **Fisherman:** Fish Flingers starts in [number] [minute/minutes].
  - (continue)
- (Condition: If you just missed Fish Flingers:)
  - **Fisherman:** You've just missed the start of a Fish Flingers competition, I'm afraid. The waiting area for the next Fish Flingers competition opens in 15 minutes. If you speak to me again then, I'll teleport you to the competition.
  - (continue)
- (Condition: (If Fish Flingers won't start for several more minutes:)
  - **Fisherman:** The waiting area for the next Fish Flingers competition opens in [number] [minute/minutes]. If you speak to me again then, I'll teleport you to the competition.
  - (continue)
- [Menu]: What would you like to say?{{anchor|initial-select}}
  - [Choice]: cond=Only if a competition is about to start:|Teleport me to Fish Flingers.
    - (Condition: Before the Dailyscape Overhaul update:)
    - **Fisherman:** When Fish Flingers starts you will use one of your entry tickets, leaving you with [number] more tickets. Okay?
    - [Menu]: What would you like to say?
      - [Choice]: Yes, I'll use a ticket to compete.
        - (Condition: If the competition has already started:)
          - **Fisherman:** Oh no! The Fish Flingers competition has started I'm afraid, so I can't teleport you. The next competition starts in [number] minutes. If you speak to me again then, I'll teleport you to the competition.
        - (Condition: If the competition hasn't started:)
          - {{Qact|The player is teleported to the waiting area.}}
      - [Choice]: No, I've changed my mind.
        - (end)
  - [Choice]: cond=Only if a competition is about to start:|Give me a hint for the next competition.
    - ((As below, then shows the initial options.))
  - [Choice]: cond=Only if there is no competition about to start soon:|Can I enter the competition now?
    - (Condition: If you are on a free world:)
      - **Fisherman:** Sorry, you'll have to switch to a members' world in order to play Fish Flingers.
      - (initial)
    - (Condition: If you are on a member's world:)
      - **Fisherman:** The waiting area for the next Fish Flingers competition opens in [number] minutes. If you speak to me again then, I'll teleport you to the competition.
      - (initial)
  - [Choice]: About Fish Flingers...
    - **Fisherman:** What would you like me to tell you?
    - [Menu]: What would you like to say?
      - [Choice]: What is the competition about?
        - **Fisherman:** It's a chance for you to show how well you can catch fish by choosing the best tackle and habitat.
        - **Fisherman:** Us old-timers know of a special place, Isla Anglerine, where huge schools of unusual fish seem to gather.
        - **Fisherman:** I'm not sure what the fish find so appealing there, but it's a fisherman's paradise!
        - **Fisherman:** I can teleport you to the island if you want to take part. Just say the word.
        - (previous)
      - [Choice]: How do I catch fish?
        - **Fisherman:** Once I've teleported you, wait in the starting area for the competition to begin. Then, walk to the waterfront where you would like to fish.
        - **Fisherman:** Next, select a hook and bait that you think the fish will like, add some weights to get the cast distance you need, and you're ready to cast your line.
        - **Fisherman:** As you catch fish you'll be shown how effective your tackle is, and you'll be able to make improvements as you learn what each fish likes.
        - **Fisherman:** Remember, different species are different sizes. You'll need to try fishing in different areas to find the heaviest species.
        - **Fisherman:** It's also worth remembering that fish are adaptable creatures, so tackle that works well in one competition might not work so well in the next.
        - (previous)
      - [Choice]: How often can I compete?
        - (Condition: Before the Dailyscape Overhaul update:)
        - **Fisherman:** Everyone is allowed 2 entry tickets every day. We hang on to the tickets for you, so there's no need to carry them about or store them in your bank.
        - **Fisherman:** If you want to know how many you have left, or you want to claim more tickets, just let me know.
        - [Menu]: What would you like to say?
          - [Choice]: How many entry tickets do I have left?
            - **Fisherman:** You've got [number] tickets left at the moment.
            - (previous)
          - [Choice]: When can I next claim entry tickets?
            - (Condition: If enough time has passed:)
            - **Fisherman:** Enough time has passed since you last claimed entry tickets, so you can claim more as soon as you've used up the ones you have left.
            - (previous)
          - [Choice]: Is there another way of getting entry tickets?
            - **Fisherman:** Funny you should ask that. We had a fierce storm recently. The gale picked up a whole load of entry tickets and scattered them all across Gielinor.
            - **Fisherman:** We picked up any we could find, but most of them ended up in the water.
            - **Fisherman:** So, you never know. You might find an entry ticket whenever you catch fish.
            - (previous)
          - [Choice]: Let's talk about something else...
            - (initial)
        - (Condition: After the Dailyscape Overhaul update:)
        - **Fisherman:** As often as you like!
      - [Choice]: About the competition score...
        - [Menu]: What would you like to say?
          - [Choice]: Give me a copy of my competition history.
            - ((Without Fish Flingers scorecard in backpack:))
              - (Condition: Without one free backpack space:)
                - **Fisherman:** You don't have room to carry it. No problem, just ask me again when you have a free inventory space.
                - (previous)
              - (Condition: With one free backpack space:)
                - (receives=Fish Flingers scorecard)
                - [The fisherman hands you a Fish Flingers scorecard.]
                - (previous)
            - (Condition: With Fish Flingers scorecard in backpack:)
              - **Fisherman:** You already seem to have one in your inventory.
              - (previous)
          - [Choice]: How is my score calculated?
            - **Fisherman:** We take into account the number of fish caught, the total weight caught, and the heaviest fish caught.
            - **Fisherman:** We also include how many big fish you caught and how often you helped other contestants to catch their big fish.
            - **Fisherman:** Finding the perfect tackle for each species is an important part of fishing. You'll get bonus points for each species you find the perfect tackle for.
            - **Fisherman:** You'll know you've found the perfect tackle when your rating for catching that fish reaches 100%.
            - **Fisherman:** After the competition you'll be shown your results, so you'll be able to see what had an impact on your score.
            - (previous)
          - [Choice]: Tell me about big fish.
            - **Fisherman:** Maintain a 100% rating, and you'll eventually hook a valuable big fish. Big fish are so heavy that you'll need assistance from other contestants to heave it out of the water.
            - **Fisherman:** Catching big fish significantly improves your score, but helping others to catch their big fish earns you the greatest reward of all.
            - (previous)
          - [Choice]: Tell me about medals.
            - **Fisherman:** If you perform well enough you'll receive up to four medals, which give you a bonus to your score. The noticeboard in the waiting area describes the conditions to win medals.
            - (previous)
          - [Choice]: Let's talk about something else...
            - (initial)
      - [Choice]: Let's talk about something else...
        - (initial)
    - [Choice]: Show me the rewards shop.
      - ((Fish Flingers Reward Shop interface opens.))
  - [Choice]: About rewards...{{anchor|about-rewards}}
    - [Menu]: What would you like to say?
      - [Choice]: Tell me about the Fishing experience reward.
        - **Fisherman:** You'll find that the extra skill involved in competitive fishing can earn you more experience than your everyday fishing.
        - **Fisherman:** At the end of each competition you'll receive all the experience you've earned, so there's no need to speak to me to collect it.
        - **Fisherman:** It might take you a few tries to get used to the competition tackle, but once you've learned the best way to find and catch the biggest fish species you should notice a great improvement in the experience you get.
        - **Fisherman:** The amount of experience you earn depends on your skill at Fishing. Having a higher Fishing level means you earn more experience.
        - (previous)
      - [Choice]: I'd like to know more about the raw fish reward.
        - **Fisherman:** We'll give you noted raw fish, which is much easier to carry to the bank.
        - **Fisherman:** When you claim your noted fish you'll be given a selection of fish appropriate to your Fishing level. For example, if you'd normally be fishing swordfish, you'll be given a mix of swordfish and lobsters.
        - (previous)
      - [Choice]: Tell me about the tackle box reward.
        - **Fisherman:** The tackle box holds fishing equipment and raw fish, saving you inventory and bank space. They also hold a copy of your competition history, so you can review your performance.
        - **Fisherman:** Admittedly, when you first get your tackle box it won't hold much, but over time you can upgrade it so it will hold much more.
        - (previous)
      - [Choice]: Tell me about the fishing outfit reward.
        - **Fisherman:** The fishing outfit increases the amount of Fishing experience you get. When you're fishing or playing Fish Flingers, it's a good idea to wear as many pieces of the fishing outfit as possible.
        - (previous)
      - [Choice]: Let's talk about something else.
        - (initial)

#### In the waiting area

- (Condition: If there is more than a minute to the start:)
  - **Fisherman:** It won't be long now. The competition starts in [number] [minute/minutes].
  - (continue)
- (Condition: If there is less than a minute to the start:)
  - **Fisherman:** The competition is about to start. Have fun!
  - (continue)
- [Menu]: What would you like to say?
  - (Condition: Only if a competition is about to start:)
    - [Choice]: Give me a hint for the next competition.
      - ((As below, then shows the initial options.))
  - [Choice]: About Fish Flingers...
    - **Fisherman:** What would you like me to tell you?
    - [Menu]: What would you like to say?
      - [Choice]: What is the competition about?
        - **Fisherman:** It's a chance for you to show how well you can catch fish by choosing the best tackle and habitat.
        - **Fisherman:** Here on Isla Anglerine, huge schools of unusual fish seem to gather. I'm not sure what the fish find so appealing here, but it's a fisherman's paradise!
        - (previous)
      - [Choice]: How do I catch fish?
        - **Fisherman:** When the gates open, hurry to the any shoreline where you would like to fish.
        - **Fisherman:** You can fish at either of the docks to the east and west, the lake to the north, the river east of the lake, and the beach to the far north-east.
        - **Fisherman:** Next, select a hook and bait that you think the fish will like, add some weights to get the cast distance you need, and you're ready to cast your line.
        - **Fisherman:** As you catch fish you'll be shown how effective your tackle is, and you'll be able to make improvements as you learn what each fish likes.
        - **Fisherman:** Remember, different species are different sizes. You'll need to try fishing in different areas to find the heaviest species.
        - **Fisherman:** It's also worth remembering that fish are adaptable creatures, so tackle that works well in one competition might not work so well in the next.
        - (previous)
      - [Choice]: How often can I compete?
        - **Fisherman:** Everyone is allowed 2 entry tickets every day. We hang on to the tickets for you, so there's no need to carry them about or store them in your bank.
        - **Fisherman:** If you want to know how many you have left, or you want to claim more tickets, just let me know.
        - [Menu]: What would you like to say?
          - [Choice]: How many entry tickets do I have left?
            - **Fisherman:** You've got [number] tickets left at the moment.
            - (previous)
          - [Choice]: When can I next claim entry tickets?
            - **Fisherman:** Enough time has passed since you last claimed entry tickets, so you can claim more as soon as you've used up the ones you have left.
            - (previous)
          - [Choice]: Is there another way of getting entry tickets?
            - **Fisherman:** Funny you should ask that. We had a fierce storm recently. The gale picked up a whole load of entry tickets and scattered them all across Gielinor.
            - **Fisherman:** We picked up any we could find, but most of them ended up in the water.
            - **Fisherman:** So, you never know. You might find an entry ticket whenever you catch fish.
            - (previous)
          - [Choice]: Let's talk about something else...
            - (initial)
      - [Choice]: About the competition score...
        - [Menu]: What would you like to say?
          - [Choice]: Give me a copy of my competition history.
            - (Condition: Without Fish Flingers scorecard in backpack:)
              - ((Without space in backpack:))
                - **Fisherman:** You don't have room to carry it. No problem, just ask me again when you have a free inventory space.
                - (previous)
              - ((With space in backpack:))
                - (receives=Fish Flingers scorecard)
                - [The fisherman hands you a Fish Flingers scorecard.]
                - (previous)
            - ((With Fish Flingers scorecard in backpack:))
              - **Fisherman:** You already seem to have one in your inventory.
              - (previous)
          - [Choice]: How is my score calculated?
            - **Fisherman:** We take into account the number of fish caught, the total weight caught, and the heaviest fish caught.
            - **Fisherman:** We also include how many big fish you caught and how often you helped other contestants to catch their big fish.
            - **Fisherman:** Finding the perfect tackle for each species is an important part of fishing. You'll get bonus points for each species you find the perfect tackle for.
            - **Fisherman:** You'll know you've found the perfect tackle when your rating for catching that fish reaches 100%.
            - **Fisherman:** After the competition you'll be shown your results, so you'll be able to see what had an impact on your score.
            - (previous)
          - [Choice]: Tell me about big fish.
            - **Fisherman:** Maintain a 100% rating, and you'll eventually hook a valuable big fish. Big fish are so heavy that you'll need assistance from other contestants to heave it out of the water.
            - **Fisherman:** Catching big fish significantly improves your score, but helping others to catch their big fish earns you the greatest reward of all.
            - (previous)
          - [Choice]: Tell me about medals.
            - **Fisherman:** If you perform well enough you'll receive up to four medals, which give you a bonus to your score. The noticeboard in the waiting area describes the conditions to win medals.
            - (previous)
          - [Choice]: Let's talk about something else...
            - (initial)
      - [Choice]: Let's talk about something else...
        - (initial)
    - [Choice]: Show me the rewards shop.
      - ((Fish Flingers Reward Shop interface opens.))
  - [Choice]: About rewards...
    - [Menu]: What would you like to say?
      - [Choice]: Tell me about the Fishing experience reward.
        - **Fisherman:** You'll find that the extra skill involved in competitive fishing can earn you more experience than your everyday fishing.
        - **Fisherman:** At the end of each competition you'll receive all the experience you've earned, so there's no need to speak to me to collect it.
        - **Fisherman:** It might take you a few tries to get used to the competition tackle, but once you've learned the best way to find and catch the biggest fish species you should notice a great improvement in the experience you get.
        - **Fisherman:** The amount of experience you earn depends on your skill at Fishing. Having a higher Fishing level means you earn more experience.
        - (previous)
      - [Choice]: I'd like to know more about the raw fish reward.
        - **Fisherman:** We'll give you noted raw fish, which is much easier to carry to the bank.
        - **Fisherman:** When you claim your noted fish you'll be given a selection of fish appropriate to your Fishing level. For example, if you'd normally be fishing swordfish, you'll be given a mix of swordfish and lobsters.
        - (previous)
      - [Choice]: Tell me about the tackle box reward.
        - **Fisherman:** The tackle box holds fishing equipment and raw fish, saving you inventory and bank space. They also hold a copy of your competition history, so you can review your performance.
        - **Fisherman:** Admittedly, when you first get your tackle box it won't hold much, but over time you can upgrade it so it will hold much more.
        - (previous)
      - [Choice]: Tell me about the fishing outfit reward.
        - **Fisherman:** The fishing outfit increases the amount of Fishing experience you get. When you're fishing or playing Fish Flingers, it's a good idea to wear as many pieces of the fishing outfit as possible.
        - (previous)
      - [Choice]: Let's talk about something else.
        - (initial)

### Teleport


#### If Fish Flingers hasn't started yet, but you can teleport to the waiting area

- **Fisherman:** Fish Flingers starts in [number] minutes.
- {{Qact|The player is teleported to the waiting area.}}

#### If Fish Flingers won't start for several more minutes

- **Fisherman:** The waiting area for the next Fish Flingers competition opens in [number] minutes. If you speak to me again then, I'll teleport you to the competition.

### Claim reward

- ((Fish Flingers Reward Shop interface opens.))

#### First time dialogue

- **Fisherman:** Everyone likes to be rewarded for their efforts, of course. You can be awarded Fishing experience, raw fish, a fishing outfit and - if you get good enough - a tackle box to hold your fishing supplies.
- [Menu]: What would you like to say?
  - [Choice]: Tell me more about the rewards.
    - (continuea|about-rewards)
  - [Choice]: Show me the reward shop.
    - ((Fish Flingers Reward Shop interface opens.))
  - [Choice]: Let's talk about something else.
    - (Condition: Before the Dailyscape Overhaul update:)
      - **Fisherman:** Good news! You're eligible to claim entry tickets. You now have [number] Fish Flingers entry tickets. Come back tomorrow to claim more.
      - (continuea|initial-select)

#### Upgrading a tackle box

- (Condition: With the previous tackle box in the bank:)
  - **Fisherman:** You'll need to get your tackle box from the bank before I can upgrade it.
- (Condition: With the previous tackle box in the inventory:)
  - (removes=previous tackle box) (receives=upgraded tackle box)
  - [The tackle box in your inventory has been upgraded and can now hold more items.]
  - (Condition: Upgrading to the Champion's tackle box:)
    - {{RSFontAchievement|Master Angler|Purchase the champion's tackle box from the Fish Flingers fisherman.}}
- (Condition: With the tackle box already fully upgraded:)
  - You already own the best tackle box available.

### Get hint from


#### If the competition hasn't yet started


##### If the waiting area just opened

- **Fisherman:** We're still tidying up from the last competition. Give me a minute and I'll have that hint for you.

##### If the waiting area has been open for a while

- ((One of the following is shown:))
  - **Fisherman:** You'll find bowline salmon at the beach. They've been sighted far from the shore, so attach lots of weights to your line to reach them.
  - **Fisherman:** You'll find cove bass at the beach. They're clever and can spot metal a mile off. You'd better think carefully about what type of hook you use.
  - **Fisherman:** You'll find darter cod at the river. They're known to like shellfish, particularly grey ones.
  - **Fisherman:** You'll find darter cod at the river. They've been spotted close to the shore, so you won't need much weight on your line to reach them.
  - **Fisherman:** You'll find drift herring at the docks. They've been seen a fair distance from the shore, but not too far. You'll need to attach a few weights to reach them.
  - **Fisherman:** You'll find shallow bass at the lake. They've been spotted close to the shore, so you won't need much weight on your line to reach them.
  - **Fisherman:** You'll find spotted pike at the lake. They're known to like wriggling creatures, particularly red ones.
  - **Fisherman:** You'll find thunder trout at the river. They're clever and can spot metal a mile off. You'd better think carefully about what type of hook you use.
  - **Fisherman:** You'll find yearning trout at the docks. They're known to like fluttering creatures, particularly green ones.
  - {{Transcript missing|More clues}}

#### If the competition already started or just ended

- **Fisherman:** You're keen, aren't you?<br>You'll have to wait for the countdown to the next competition to start before I can give you a hint.

### Overhead

- **Fisherman:** {{RSChat|Fish Flingers starts in [number] minutes.}}
