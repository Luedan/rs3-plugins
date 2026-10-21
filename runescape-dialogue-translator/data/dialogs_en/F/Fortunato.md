# Fortunato

- **Original Wiki Page**: [Transcript:Fortunato](https://runescape.wiki/w/Transcript%3AFortunato)
- **Letter**: `F`

---

## Dialogue Transcript


### In Draynor Village

- **Fortunato:** Can I help you at all?
- [Menu]: Choose an option:
  - [Choice]: Yes, what are you selling?
    - **Player:** Yes, what are you selling?{{anchor|shop}}
    - (opens=Fortunato's Fine Wine)
  - [Choice]: cond=After Rag and Bone Man:|Talk about Rag and Bone Man.
    - **Fortunato:** Oh, you've come back.
    - **Fortunato:** Please, I haven't got any more vinegar. Give me some time, I beg you.
    - **Player:** I wasn't after vinegar today.
    - **Fortunato:** Oh, wonderful.
    - **Fortunato:** I will have some in soon if 'he' needs it.
    - **Fortunato:** In the meantime, can I interest you in anything else?
    - [Menu]: Select an Option
      - [Choice]: Yes.
        - (above|shop)
      - [Choice]: No.
        - **Player:** No.
        - **Fortunato:** Well, I'll put something special to one side for you.
        - **Player:** Thanks.
  - [Choice]: cond=On free-to-play worlds, or before Rag and Bone Man:|Wine merchant, huh?
    - **Fortunato:** Yes, indeed. The finest wines in Misthalin.
    - **Fortunato:** Care to take a look at my wares?
    - [Menu]: Select an Option
      - [Choice]: Yes.
        - (above|shop)
      - [Choice]: Not at the moment.
        - (below|ragamuffin)
  - [Choice]: cond=Before Vampyre Slayer:|Can you tell me about Draynor Village?
    - **Fortunato:** The village is quite old, but the market is a rather recent addition. We were doing quite good business up until recently.
    - **Player:** What happened?
    - **Fortunato:** Mysterious attacks began happening to villagers. Some say it's a vampyre, but I'm not convinced.
    - (initial)
  - [Choice]: cond=After Vampyre Slayer:|Talk about Vampyre Slayer.
    - **Fortunato:** Well done killing that vampyre. Business has certainly improved since the attacks have stopped.
    - **Player:** Happy to help.
    - (initial)
  - [Choice]: Not at the moment.
    - **Player:** Not at the moment.{{anchor|ragamuffin}}
    - **Fortunato:** Then move along, you filthy ragamuffin, I have customers to serve!

#### Using empty wine bottles on Fortunato

- **Fortunato:** Ah! I buy wine bottles back if you want to hand them all over.
- (removes=all empty wine bottles) (receives=2 coins per bottle)

#### Getting caught while attempting to steal from his stall

- **Fortunato:** {{RSChat|Hey! Get your hands off there!}}

#### Trading or speaking to him after stealing from his stall

- **Fortunato:**{{RSChat|shadow=yes|colour=yellow|You're the thief who stole from me!}}
- **Fortunato:**{{RSChat|shadow=yes|colour=yellow|Guards, guards!}}

#### Historical dialogue

- **Fortunato:** Can I help you at all?
- [Menu]: Choose an option:
  - [Choice]: Yes, what are you selling?
    - (above|shop)
  - [Choice]: cond=After Rag and Bone Man:|Talk about Rag and Bone Man.
    - (above)
  - [Choice]: cond=On free-to-play worlds, or before Rag and Bone Man:|Wine merchant, huh?
    - (above)
  - [Choice]: Can you tell me about Draynor Village?
    - **Fortunato:** The village is quite old, but the market is a rather recent addition. We were doing quite good business up until recently.
    - **Player:** What happened?
    - (Condition: During the Battle of Lumbridge:)
      - **Fortunato:** Saradomin and Zamorak have decided to have a huge fight just nearby! It's terrible for business!
      - (continue|zxc)
    - (Condition: After the Battle of Lumbridge:)
      - **Fortunato:** Well, not long ago there was a battle right outside Draynor, between Saradomin and Zamorak! You can still see the battlefield.
      - (continue|zxc)
    - (Condition: Before Vampyre Slayer:)
      - **Fortunato:** Besides that, mysterious attacks began happening to villagers. Some say it's a vampyre, but I'm not convinced.
      - (continue|cxz)
    - (Condition: After Vampyre Slayer:)
      - **Fortunato:** You add that to the vampyre you killed, and it doesn't make for happy sales figures!
      - (continue|cxz)
    - **Fortunato:** Perhaps I can interest you in some wine?
    - [Menu]: Select an Option
      - [Choice]: Yes.
        - (above|shop)
      - [Choice]: Not at the moment.
        - (above|ragamuffin)
