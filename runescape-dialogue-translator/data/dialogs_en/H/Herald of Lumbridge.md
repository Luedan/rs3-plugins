# Herald of Lumbridge

- **Original Wiki Page**: [Transcript:Herald of Lumbridge](https://runescape.wiki/w/Transcript%3AHerald%20of%20Lumbridge)
- **Letter**: `H`

---

## Dialogue Transcript


### In Lumbridge


#### Before claiming a herald cape

- **Herald of Lumbridge:** Hello there, dearie! How can I make your Lumbridge day even more wonderful?
- **Player:** Hello to you too!<br>What do you do here?
- **Herald of Lumbridge:** I'm the Lumbridge herald, my dear! It's my job to make Lumbridge a lovely place to be.
- **Herald of Lumbridge:** You need a parade? I'll arrange it! You need a fancy banner? I can do that too! You need a herald cape...
- **Player:** Herald cape? What's that?
- **Herald of Lumbridge:** Why, it's the latest and greatest thing in Lumbridge attire. We provide you with a lovely Lumbridge cape to wear around, for nothing!
- **Herald of Lumbridge:** And if you've been particularly handy around the area, we'll show you how to customise it into something more fabulous!
- **Herald of Lumbridge:** In fact, I hear that other cities, like Varrock and Falador, are also offering herald capes with their own special designs!
- **Herald of Lumbridge:** Naturally, our Lumbridge capes are much nicer.
- **Herald of Lumbridge:** Can I interest you in taking a cape?
- [Menu]: Accept this Lumbridge herald cape?
  - [Choice]: Yes
    - (receives=herald cape) <!-- worn ones will be swapped, not sure about poh -->
    - **Player:** Sure, I'll take it!
    - **Herald of Lumbridge:** Wonderful! Let's take a look at the customisations we can do...
    - (continue|Customise)
  - [Choice]: No
    - **Player:** No, thanks.
    - **Herald of Lumbridge:** Oh, gosh. Well, drop by again if you change your mind, sweetheart.

#### After claiming a herald cape

- **Herald of Lumbridge:** Hello there, dearie! How can I make your Lumbridge day even more wonderful?
- [Menu]: Choose an option:
  - [Choice]: Hello back at you! What do you do here?
    - **Herald of Lumbridge:** I'm the Lumbridge herald, my dear! It's my job to make Lumbridge a lovely place to be.
    - **Herald of Lumbridge:** You need a parade? I'll arrange it! You need a fancy banner? I can do that too! You need a herald cape...
    - (Condition: If another city's herald cape is owned:)
      - **Player:** I already have a herald cape from another city, though.
      - **Herald of Lumbridge:** *tsk* Yes, I noticed - I don't think it suits you, though. The Lumbridge cape is MUCH nicer!
      - **Herald of Lumbridge:** If you want, I can take that herald cape off your hands and instead give you a wonderful Lumbridge herald cape.
      - [Menu]: Change your herald cape To Lumbridge?
        - [Choice]: Yes
          - (continuea|accept)
        - [Choice]: No
          - **Player:** No thanks, I'll keep the cape I have.
          - **Herald of Lumbridge:** That silly thing? Well if you must. Drop by again if you change your mind, sweetheart.
    - (Condition: If the Lumbridge herald cape is owned:)
      - **Player:** Oh, I already have one of those.
      - **Herald of Lumbridge:** Yes, I noticed! It looks very dashing on you. Would you like to customise it some more, perhaps?
      - [Menu]: Customise your Lumbridge herald cape?
        - [Choice]: Yes
          - (continue|Customise)
        - [Choice]: No
          - (end)
  - [Choice]: Could you be a little less...noisy?|cond=Default, and after telling her it's too quiet:
    - **Herald of Lumbridge:** Well, I AM a herald, dearie. Proudly proclaiming the civic value of Lumbridge is my whole thing.
    - **Player:** Could you perhaps do you thing with a bit less...enthusiasm?
    - **Herald of Lumbridge:** On a scale of 'one' to 'me', how much enthusiasm would you prefer?
    - **Player:** As little 'you' as possible, please.<br>That would be splendid.
    - **Herald of Lumbridge:** Righto. I'll quit my jibber-jabber, 'til you say otherwise.
    - **Player:** Marvellous.<br>So, remind me what do you do here?
    - (continuea|what-do-you-do)
  - [Choice]: It's quiet. Almost too quiet.|cond=After asking her to be less noisy before:
    - **Herald of Lumbridge:** I could go back to yelling about Lumbridge, if you like?
    - **Player:** Your yelling about Lumbridge has to be unbearably effervescent, I presume?
    - **Herald of Lumbridge:** That's the only way I know how.
    - **Player:** Go on, then. Proclaim your sweet nonsense.
    - **Herald of Lumbridge:** YIPPEE!
    - **Player:** Now, I suppose you want to introduce yourself, again, despite our prior conversations?
    - **Herald of Lumbridge:** You know me too well.
    - **Player:** Very well. Tell me what you do here.
    - (continuea|what-do-you-do)

#### Customise

- **Herald of Lumbridge:** Looks like you have some extra crests to unlock, dearie. How exciting!
- ((Lumbridge Herald Cape customisation interface opens.))

#### Overhead dialogue

- **Herald of Lumbridge:** {{RSChat|"Give me an L!"}}
- **Herald of Lumbridge:** {{RSChat|"Give me a U!"}}
- **Herald of Lumbridge:** {{RSChat|"Give me a Lumbridge herald cape!"}}
- **Herald of Lumbridge:** {{RSChat|"Lumbridge; the friendliest place to be"}}
- **Herald of Lumbridge:** {{RSChat|"Wear a Lumbridge herald cape with pride!"}}
- **Herald of Lumbridge:** {{RSChat|"It's Lumbridge!"}}
- **Herald of Lumbridge:** {{RSChat|"The eye of the fun hurricane"}}
- **Herald of Lumbridge:** {{RSChat|"Whoo! This is tiring work."}}
- **Herald of Lumbridge:** {{RSChat|"Have yourself a snazzy Lumbridge day!"}}

#### Historical dialogue

- **Herald of Lumbridge:** Hello there, dearie! How can I make your Lumbridge day even more wonderful?
- [Menu]: Choose an option:
  - [Choice]: Hello back at you! What do you do here?
    - (continuea|what-do-you-do)
  - [Choice]: Could you be a little less...noisy?|cond=Default, and after telling her it's too quiet:
    - (above|noisy)
  - [Choice]: It's quiet. Almost too quiet.|cond=After asking her to be less noisy before:
    - (above|quiet)
  - [Choice]: This city looks like it's seen better days!
    - (Condition: During the Lumbridge Rebuildathon:)
      - **Herald of Lumbridge:** It was the battle of Lumbridge, where Saradomin and Zamorak fought for supremecy after the death of Guthix. It makes me sad to think about it, though. Look at my once-fair city! Shops and houses ruined! But I'm trying to improve everyone's mood!
      - **Player:** Why is that? What do you do here?
      - (continuea|what-do-you-do)
    - (Condition: During the Battle of Lumbridge:)
      - **Player:** Wonderful? We're practically in the middle of a battle!
      - **Herald of Lumbridge:** I know, but you don't need to remind me. The battle has been bad for everyone! Look at my once-fair city! It's practically a war camp! But I'm trying to improve everyone's mood!
      - **Player:** Why is that? What do you do here?
      - (continuea|what-do-you-do)
