# Pikkenmix

- **Original Wiki Page**: [Transcript:Pikkenmix](https://runescape.wiki/w/Transcript%3APikkenmix)
- **Letter**: `P`

---

## Dialogue Transcript


### While obelisk is active, first conversation

- **Player:** Hello.
- **Pikkenmix:** Where ARE they? They haven't come back yet.
- **Player:** Who?
- **Pikkenmix:** The other druids; Pikkupstix will be most upset.
- **Pikkenmix:** They went to gather raw shards from the spirit plane, but they're either not coming back at all, or coming back empty-handed.
- **Pikkenmix:** Apparently, there's lots of shards now scattered around to be picked up, but the familiars in the realm aren't happy about the situation, and are trying to stop anyone who tries to get them.
- [Menu]: Choose an option:
  - [Choice]: I don't see any druids around here.
    - **Player:** I don't see any druids around here.
    - **Pikkenmix:** Well, you wouldn't, would you? They're not here. They went into the spirit plane to gather raw shards. Pikkupstix will go spare; this keeps happening!
    - **Player:** Umm...right.
    - (previous)
  - [Choice]: Why is that obelisk sparkling?
    - **Player:** Why is that obelisk sparkling?
    - **Pikkenmix:** It's active. When it's active like this, we druids are able to enter the spirit plane to collect raw spirit shards.
    - (continue|sparklingquestion)
  - [Choice]: Can I help?
    - **Player:** Can I help?
    - **Pikkenmix:** You want to help us get shards?
    - (continue|helpshards)

### While obelisk is active, subsequent conversations

- **Pikkenmix:** So, will you help us gather more raw shards?
- [Menu]: Select an Option
  - [Choice]: Sure, I'll have a go.
    - **Player** Sure, I'll have a go.
    - (Condition: If Familiarisation hasn't been completed that week:)
      - {{qact|The player puts their hand into the obelisk, and is teleported to the spirit plane.}}
    - (Condition: If Familiarisation has already been completed that week:)
      - **Pikkenmix:** You've already helped me this week.
      - You have already helped Pikkenmix this week. Come back on Wednesday.
    - (Condition: If the obelisk has stopped sparkling before dialogue was finished:)
      - **Pikkenmix:** You've already helped me this week.
      - The obelisk is no longer active.
    - (Condition: If there is a follower out:)
      - **Pikkenmix:** I'm afraid you can't go in there with that pet following you. It might distract you with disasterous consequences.
  - [Choice]: What are the risks?
    - **Player:** What are the risks?
    - **Pikkenmix:** Well, there's no risk to your physical form or items in this realm. Your body stays here, so you can't really die.
    - [Menu]: Select an Option
      - [Choice]: What are the limits on this mental focus you speak of?
        - **Player:** What are the limits on this mental focus you speak of?
        - **Pikkenmix:** Well, Pikkupstix says it is quite mentally exhausting to maintain your focus on staying in the spirit plane, so you can only do so for a limited time and only once per week.
        - **Player:** Hmm, okay, so I'll need to work quickly.
        - **Pikkenmix:** You'll find that you can only have a maximum of sixty raw shards on you at a time. Pikkupstix says it's because they have a draining effect on your mental focus.
        - (other)
      - [Choice]: Any other effects inside the spirit plane?
        - **Player:** Any other effects inside the spirit plane?
        - **Pikkenmix:** Well, you won't be able ot go running around willy-nully in there. Take your time and conserve your run energy. At least, that's what Pikkupstix teaches.
        - **Player:** But that won't affect me when I get out?
        - **Pikkenmix:**  No, not at all.
        - (other)
      - [Choice]: Any limitations on what I can take with me?
        - **Player:** Any limitations on what I can take with me?
        - **Pikkenmix:** Not really, but physical enhancements will not benefit you in the spirit plane at all, so nothing is actually needed. It's all about the mental focus you have.
        - (other)
      - [Choice]: Ask about something else.
        - (below|sparklingquestion)
  - [Choice]: Ask about something else.
    - [Menu]: Choose an option:
      - [Choice]: Enter as in just stroll in?
        - **Player:** Enter as in just stroll in?
        - **Pikkenmix:** No, no, no! We use our mental fortitude and focus to penetrate the spirit realm. Our physical bodies stay here in this world. We call it 'familiarisation'.
        - **Player:** Is it difficult?
        - **Pikkenmix:** No, but it can be mentally exhausting. Of course, it has no effect on anything in this world, though.
        - [Menu]: Choose an option:
          - [Choice]: What are the risks?
            - (above|risk)
          - [Choice]: Why do you enter the spirit plane?
            - (below|enter)
          - [Choice]: How would I enter the spirit plane?
            - (below)
      - [Choice]: Why do you enter the spirit plane?
        - **Player:** Why do you enter the spirit plane?
        - **Pikkenmix:** Ah, I wondered that too... until Pikkupstix told me. You know of course, that spirit shards are made from chips of summoning obelisks?
        - [Menu]: Select an Option
          - [Choice]: Yes, what of it?
            - **Player:** Yes, what of it?
            - **Pikkenmix:** Have you ever seen any obelisk in the land that has been chipped?
            - **Player:** Now you come to mention it, no.
            - **Pikkenmix:** Exactly! However, we found that shards from this realm don't work properly to bind a spirit between realms, so we have to use the shards from the spirit plane.
            - **Player:** Oh.
            - [Menu]: Select an Option
              - [Choice]: Where do all the spirit shards we use come from?
                - **Pikkenmix:** A large obelisk in the spirit plane. Now that the druids haven't been returning, there should be a lot of raw shards just scattered around there.
                - **Player:** Wow, so they're just laying around...
                - (other)
              - [Choice]: Can't you make them another way?
              - **Pikkenmix:** We've tried everything we can think of, but it seems unless they come from the spirit plane in their raw form, they're not attuned to it, so they can't act as a link between realms through which to summon a familiar.
              - (other)
              - [Choice]: Who collects them?
                - **Player:** Who collects them?
                - **Pikkenmix:** Some of the braver druids use all their mental skills to enter the spirit plane and collect raw shards from the obelisk there. Then we attune those raw shards to this realm to create a lin. It's not easy, and requires great mental focus.
                - (other)
              - [Choice]: So what's the problem?
                - **Player:** So what's the problem?
                - **Pikkenmix:** Well, just recently, we've been having rogue spirits appearing on RuneScape...
                - **Pikkenmix:** There have been an increasing number of these incursions, and now our druids aren't all returning from the spirit plane with shards.
                - **Player:** You mean they're being eaten?
                - **Pikkenmix:** No! Oh, no. Their corporeal form stays here; only their essence travels to the spirit plane. It seems that the familiars there are stopping them from taking any raw shards.
                - **Player:** Interesting... So there's bunches of these raw shards just hanging around unclaimed...
                - (previous2|sparklingquestion)
              - [Choice]: Ask about something else
                - (above|sparklingquestion)
          - [Choice]: No, I've never examined a spirit shard.
            - **Player:** No, I've never examined a spirit shard.
            - **Pikkenmix:** Well, that's where they're from - chipped off summoning obelisks - but, as I was saying...
            - **Pikkenmix:** Have you ever seen any obelisk in the land that has been chipped?
            - (continuea|whatofit)
      - [Choice]: How would I enter the spirit plane?
        - **Player:** How would I enter the spirit plane?
        - **Pikkenmix:** It should be fairly easy for you, as Pikkupstix has been teaching me to assist others in the technique. We call it 'familiarisation'. The obelisk phenomena are reasonably regular in their occurence too - every couple of hours... ish.
        - [Menu]: Choose an option:
          - [Choice]: What are the risks?
            - (above|risk)
          - [Choice]: Enter as in just stroll in?
            - (above|stroll)
          - [Choice]: Why do you enter the spirit plane?
            - (above|enter)
  - [Choice]: No, thanks.
    - **Player:** No, thanks.

### At an inactive obelisk

- **Player:** Hello there.
- **Pikkenmix:** Oh. Hello.
- **Player:** What's up?
- **Pikkenmix:** I'm studying this obelisk; it was recently active.
- [Menu]: Select an Option
  - [Choice]: What do you mean by active?
    - **Player:** What do you mean by active?
    - **Pikkenmix:** They sparkle, and when they do that we can enter the spirit plane.
    - (above|sparklingquestion)
  - [Choice]: Can I help?
    - **Player:** Can I help?
    - **Pikkenmix:** Not until I find another active obelisk. But I can tell you a bit about what goes on when obelisks are active if you want. They sparkle, and when they do that, we can enter the spirit plane.
    - (continuea|sparklingquestion)
  - [Choice]: That's nice. Bye.
    - **Player:** That's nice. Bye.

### Claiming a reward

- (Condition: If this is the first time eligible for a reward:)
  - **Pikkenmix:** Hello again, thanks for helping us out. If you'd like, I can give you a reward in return for the raw shards you've collected. Pikkupstix says I can!
  - (continue|rewards)
- (Condition: Subsequent times eligible for a reward:)
  - **Pikkenmix:** Thanks for getting the shards.
  - **Pikkenmix:** If you'd like, I can give you a reward in return for the raw shards you've collected.
  - (continue|rewards)
- [Menu]: Select an Option
  - [Choice]: Yes, please.
    - **Player:** Yes, please.
    - **Pikkenmix:** Excellent, excellent! You have collected x piles of raw shards. Would you like triple charm drops for a while or some Summoning ingredients?
    - [Menu]: Select an Option
      - [Choice]: Triple charm drops.
        - **Player** Triple charm drops.
        - ((If the player already has a charm drop enhancer from a previous reward:))
          - **Pikkenmix:** I'm afraid you already have our reward. Choose something else.
          - **Pikkenmix:** If you'd like, I can tell you a bit about these obelisks, and how to enter the spirit plane when they're active.
          - (continuea|sparklingquestion)
        - (Condition: Otherwise:)
          - Pikkenmix makes an obscure motion with his hands you can't quite see.
          - (receives=charm drop enhancer)
          - **Pikkenmix:** There you go; I think that's right. At least, that's what Pikkupstix told me to do. It will only last 40 minutes from when you tear the ticket, so get collecting charms! Come back in <number> days, when you've recovered and you can help us again.
          - (continue|While obelisk is active, subsequent conversations)
      - [Choice]: Summoning ingredients.
        - ((If the player already has a box of summoning ingredients from a previous reward:))
          - **Pikkenmix:** You already have a box of those. When you've opened it up I can give you another.
        - (Condition: Otherwise:)
          - **Player:** Summoning ingredients.
          - (receives=a box of summoning ingredients)
          - [Pikkenmix hands you a box.]
          - **Pikkenmix:** There you go.
          - **Pikkenmix:** If you'd like, I can tell you a bit about these obelisks, and how to enter the spirit plane when they're active.
          - (continuea|sparklingquestion)
  - [Choice]: No, thanks.
    - **Player:** No, thanks.
    - **Pikkenmix:** Okay. Come back if you change your mind.
    - **Pikkenmix:** If you'd like, I can tell you a bit about these obelisks, and how to enter the spirit plane when they're active.
    - (continuea|sparklingquestion)

#### If Familiarisation was completed without gathering any shards

- **Pikkenmix:** Hello there.
- **Player:** Hello.
- **Pikkenmix:** Weren't you recently in the spirit plane? You didn't come back with any shards if I remember correctly. Why was that?
- [Menu]: Select an Option
  - [Choice]: I couldn't find any shards to pick up.
    - **Pikkenmix:** Oh, sorry to hear that. I do hope you'll try again; I'm sure you can do a little better.
    - **Pikkenmix:** Try heading off in one direction and looking about. They'll be scattered wherever the druids have dropped them in order to get away.
    - **Pikkenmix:** If you'd like, I can tell you a bit about these obelisks, and how to enter the spirit plane when they're active.
    - (continuea|sparklingquestion)
  - [Choice]: I couldn't work out what I was supposed to do.
    - **Pikkenmix:** Oh, sorry to hear that. I do hope you'll try again; I'm sure you can do a little better.
    - **Pikkenmix:** Within the spirit plane, there are shards just laying around. You should pick up as many of these as possible, while avoiding any familiars that are hunting you.
    - **Pikkenmix:** If you'd like, I can tell you a bit about these obelisks, and how to enter the spirit plane when they're active.
    - (continuea|sparklingquestion)
  - [Choice]: I got attacked by too many familiars.
    - **Pikkenmix:** Oh, sorry to hear that. I do hope you'll try again; I'm sure you can do a little better.
    - **Pikkenmix:** Sometimes, you can avoid familiars by looking at their habitat. Water-loving familiars such as barker toads and karamthulu overlords don’t stray far from water.
    - **Pikkenmix:** If you'd like, I can tell you a bit about these obelisks, and how to enter the spirit plane when they're active.
    - (continuea|sparklingquestion)
  - [Choice]: I didn't want to.
    - **Pikkenmix:** Oh, sorry to hear that. I do hope you'll try again; I'm sure you can do a little better.
    - **Pikkenmix:** If you collect shards for us, we can offer you a reward. Do try next time, you might enjoy it!
    - **Pikkenmix:** If you'd like, I can tell you a bit about these obelisks, and how to enter the spirit plane when they're active.
    - (continuea|sparklingquestion)
  - [Choice]: Some other reason.
    - **Pikkenmix:** Oh, sorry to hear that. I do hope you'll try again; I'm sure you can do a little better.
    - **Pikkenmix:** If you'd like, I can tell you a bit about these obelisks, and how to enter the spirit plane when they're active.
    - (continuea|sparklingquestion)

### After claiming a reward

- **Pikkenmix:** Hello again.
- **Player:** Hello there.
- **Pikkenmix:** I hope you enjoyed your reward for helping us collect raw shards from the spirit plane.
- **Pikkenmix:** If you'd like, I can tell you a bit about these obelisks, and how to enter the spirit plane when they're active.
- (continuea|sparklingquestion)
