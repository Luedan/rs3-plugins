# Horacio

- **Original Wiki Page**: [Transcript:Horacio](https://runescape.wiki/w/Transcript%3AHoracio)
- **Letter**: `H`

---

## Dialogue Transcript


### Pay


#### Before Back to my Roots

- {{Qact|Nothing happens.}}

#### After Back to my Roots


##### With the jade vine patch empty

- **Horacio:** Err... you haven't planted a vine yet!

##### With the jade vine growing

- **Horacio:** I'll want 10 wildblood hops so that I can brew myself some tasty beer.
- (Condition: If the player does not have enough wildblood hops in backpack:)
  - **Player:** I don't have enough of those. I guess I'll come back later.
- (Condition: If the player has ten wildblood hops in backpack:)
  - [Menu]: Pay 10 wildblood hops?
    - [Choice]: Okay, it's a deal.
      - **Player:** Okay, it's a deal.
      - (removes=ten wildblood hops)
      - **Horacio:** That'll do nicely. Never fear, Horacio is here, your vine shall grow safely in my hands.
    - [Choice]: No, that's too much.
      - **Player:** No, that's too much.
      - **Horacio:** Well, I'm not risking my life for free.

##### Having already paid for protection

- **Horacio:** I'm already looking after your vine! You have ears like corn!

##### With the jade vine fully grown

- **Horacio:** The vine is already fully grown! I don't know what you want me to do with it!

##### With a wild jade vine

- **Horacio:** I'm not protecting that vile thing! You must be mad!

### Talk-to


#### Before Tribal Totem

- **Horacio:** It's a fine day to be out in the garden, isn't it?
- [Menu]: Select an Option
  - [Choice]: Yes, it's very nice.
    - **Player:** Yes, it's very nice.
    - **Horacio:** Days like these make me glad to be alive!
  - [Choice]: So... who are you?
    - **Player:** So... who are you?
    - **Horacio:** My name is Horacio Dobson. I'm the gardener to Lord Handelmort. Take a look around this beautiful garden, all of this is my handiwork.

#### After Tribal Totem

- **Horacio:** It's a fine day to be out in the garden, isn't it?
- [Menu]: Select an Option
  - [Choice]: Yes, it's very nice.
    - **Player:** Yes, it's very nice.
    - **Horacio:** Days like these make me glad to be alive!
  - [Choice]: So... who are you?
    - **Player:** So... who are you?
    - **Horacio:** My name is Horacio Dobson. I'm the gardener to Lord Handelmort. Take a look around this beautiful garden, all of this is my handiwork.
    - [Menu]: Select an Option
      - [Choice]: So... do you garden round the back, too?
        - **Player:** So... do you garden round the back, too?
        - **Horacio:** That I do!
        - **Player:** Doesn't all of the security around the house get in your way then?
        - **Horacio:** Ah, I'm used to all that. I have my keys, the guard dogs know me, and I know the combination to the door lock. It's rather easy, it's his middle name.
        - **Player:** Whose middle name?
        - **Horacio:** Hum. I probably shouldn't have said that. Forget I mentioned it.
      - [Choice]: Do you need any help?
        - **Player:** Do you need any help?
        - (Condition: If the player does not meet the requirements for Back to my Roots:)
          - **Horacio:** Actually, now you mention it, yes... but you're not experienced enough to help me just yet.
          - Check your quest journal for the requirements to start the Back to my Roots quest.
        - (Condition: If the player meets the requirements for Back to my Roots:)
          - **Horacio:** Actually, now you mention it, yes... I'm going to improve the garden around the house. Would you be willing to help me?
          - (see|Back to my Roots)
        - (Condition: If the player has completed Back to my Roots:)
          - **Horacio:** You've done more than enough to help. Hope you're enjoying your vine patch!
  - [Choice]: cond=After Back to my Roots|Talk about the vine.
    - (Condition: If the player does not have a jade vine seed:)
      - ((Horacio says one of the following at random:))
      - ((Dialogue 1:))
        - **Horacio:** Gardeners who plant trees be-leaf in their own abilities, but gardeners who plant the vine are simply divine. So, would you like your lost seed back?
        - (continue|lost)
      - ((Dialogue 2:))
        - **Horacio:** Despite making a complete mulch of things with your first attempt at growing the vine, you did save my life... Would you like another seed to replace your lost one?
        - (continue|lost)
      - ((Dialogue 3:))
        - **Horacio:** Glad to see you're still alive and growing. Would you like another seed to replace your lost one?
        - (continue|lost)
      - ((Dialogue 4:))
        - **Horacio:** I see you didn't get to the root of the problem before losing your vine. Would you like another seed?
        - (continue|lost)
      - [Menu]: Select an Option
        - [Choice]: Yes, please.
          - **Player:** Yes, please.
          - (receives=jade vine seed)
          - **Horacio:** Here you go then.
        - [Choice]: Not at the moment, thanks.
          - (end)
    - (Condition: If the player has a jade vine seed but has not planted it:)
      - **Horacio:** Hope you're having fun growing your vine, mine is looking particularly fine.
      - **Player:** How are you?
      - **Horacio:** Oh, I'm vine. I say, it's a fine day to be out in the garden, isn't it?
      - [Menu]: Select an Option
        - [Choice]: Yes, it's very nice.
          - (above)
        - [Choice]: So... who are you?
          - (above)
    - (Condition: If the player has a jade vine seed and has planted it:)
      - **Horacio:** Hope you're having fun growing your vine, mine is looking particularly fine.{{anchor|having-fun}}
      - (Condition: If there is no wild jade vine:)
        - [Menu]: Select an Option
          - [Choice]: Could you look after my vine for me?
            - (Condition: If the jade vine is growing:)
              - **Horacio:** Yes, of course, but it will cost you. My thyme is valuable.
              - **Player:** How much?
              - **Horacio:** I'll want 10 wildblood hops so that I can brew myself some tasty beer.
              - (Condition: If the player does not have ten wildblood hops in backpack:)
                - **Player:** I don't have enough of those. I guess I'll come back later.
              - (Condition: If the player has ten wildblood hops in backpack:)
                - [Menu]: Pay 10 wildblood hops?
                  - [Choice]: Okay, it's a deal.
                    - **Player:** Okay, it's a deal.
                    - (removes=ten wildblood hops)
                    - **Horacio:** That'll do nicely. Never fear, Horacio is here, your vine shall grow safely in my hands.
                  - [Choice]: No, that's too much.
                    - **Player:** No, that's too much.
                    - **Horacio:** Well, I'm not risking my life for free.
            - (Condition: If the player has already paid for protection:)
              - **Horacio:** I'm already looking after your vine! You have ears like corn!
            - (Condition: If the jade vine is fully grown:)
              - **Horacio:** The vine is already fully grown! I don't know what you want me to do with it!
          - [Choice]: Could you clear my vine patch, please?
            - **Horacio:** You've got a fine young vine growing there. Probably best not to disturb it. Wait till it's grown.
            - **Player:** Okay. I'll wait then.
          - [Choice]: Could you tell me more about the jade vine?
            - **Horacio:** Of course. What would you like to know?
            - [Menu]: Select an Option
              - [Choice]: Tell me about propagation.
                - **Player:** Tell me about propagation.
                - **Horacio:** These plants have gender, the same as you or I, and need one of each gender to propagate the species by seed, which is why we didn't get seeds until you successfully grew another vine in my patch. They are usually pollinated by nocturnal bats which can fly vast distances.
                - **Player:** So, the one on Karamja would never have given seed until we had another of a different gender growing?
                - **Horacio:** Maybe, maybe not, but it would never have grown, even if it had given seed. Needs the other gender to be fertile.
                - **Player:** Interesting, thanks.
              - [Choice]: Can you tell me anything about its history?
                - **Player:** Can you tell me anything about its history?
                - **Horacio:** The jade vine, or 'strongylodon macrobotrys' was once thought hunted to extinction by the Slayer Masters when they thought them the best thing to train on without needing an assignment. As we have found out, there
                - **Horacio:** seems to have been one that slipped through the net and grew on its own, undisturbed on Karamja. It can be a formidable opponent when fully wild - I don't think I'd have liked killing it for fun!
                - **Player:** It wasn't that hard.
          - [Choice]: Can you sell me something?
            - **Player:** Can you sell me something?
            - **Horacio:** That depends on what I have to sell. What is it that you're looking for?
            - (opens=Farmer's Supplies)
      - (Condition: If there is a wild jade vine:)
        - **Player:** Actually mine has gotten a bit out of hand again.
        - **Horacio:** ARG! Not again!
        - **Horacio:** Would you like me to remove it for you?
        - [Menu]: Select an Option
          - [Choice]: Yes, please!
            - **Horacio:** Okay, but I'm not doing it for nothing. Five coconuts and five watermelons to do that.
            - (Condition: Without five watermelons and five coconuts in backpack:)
              - **Player:** I don't have that - I guess I'll come back, or deal with it by myself.
            - (Condition: With five watermelons and five coconuts in backpack:)
              - [Menu]: Select an Option
                - [Choice]: Okay, it's a deal.
                  - **Player:** Okay, it's a deal.
                  - (removes=five watermelons and five coconuts)
                  - {{Qact|The wild jade vine disappears, leaving an empty patch behind.}}
                  - **Horacio:** There, all done for you.
                  - **Player:** Thanks!
                - [Choice]: No, that's too much.
                  - **Player:** No, that's too much.
                  - **Horacio:** Well, I'm not risking my life for free.
          - [Choice]: No, thanks - I can handle it.
            - (end)

### Retrieve seed


#### Before Back to my Roots

- {{Qact|Nothing happens.}}

#### If the player already has the seed planted

- **Horacio:** I don't have any seeds to give you?
- **Horacio:** Hope you're having fun growing your vine, mine is looking particularly fine.
- (continuea|having-fun)

#### If the player already has the seed but it is not planted

- **Horacio:** I have already  you a seed. Maybe you have stored it somewhere?

#### If the player does not have a seed

- **Horacio:** Here you go.
- (receives=jade vine seed)
