# Eliza

- **Original Wiki Page**: [Transcript:Eliza](https://runescape.wiki/w/Transcript%3AEliza)
- **Letter**: `E`

---

## Dialogue Transcript


### Before finding a totem piece

- [Menu]: Choose an option:
  - [Choice]: What do you think about the island? {{anchor|island}}
    - **Eliza:** We're finally here! Can you believe it? We're finally here!
    - **Player:** Have you been waiting long?
    - **Eliza:** Years! I remember when we first started building the boat; I thought 'this is it Eliza, by summer you'll be on the island'.
    - **Eliza:** Summer came and went, then wintumber, then summer again... I had given up hope in all honesty.
    - **Eliza:** But we're here now. Really here!
    - (initial)
  - [Choice]: I should go.
    - **Eliza:** Happy exploring!

### After finding a totem piece


#### Upon entering base camp

- **Eliza:** Hmm... What's that... The readings have gone off the chart!
- **Alpheus:** Is it magical interference? I've been seeing spikes occasionally.
- **Eliza:** Could be. It seems to be location based... Wait...
- **Eliza:** Player? What do you have there? Come talk to us quickly.

#### Initially

- (Condition: If the player doesn't have the totem piece in backpack:)
  - **Eliza:** What is that energy reading? Have you been in contact some magical artefact recently?
  - **Player:** I found a piece of a totem on the island? Could that be it?
  - (continue|discovery)
- (Condition: If the player has the totem piece in backpack:)
  - **Eliza:** What do you have in your backpack, Player? It's sending our energy readings off the chart.
  - **Player:** Do you mean this?
  - You show the archaeologists the totem piece you discovered.
  - (continue|discovery)
- {{anchor|discovery}} **Alpheus:** What a discovery! Whatever it is, it seems to contain a vast amount of energy within.
- **Eliza:** Look! It's only one piece of something larger. Perhaps if you could find all the pieces they could be combined...
- **Alpheus:** Are you seriously telling Player to reassemble an ancient artefact of huge energy without considering safety precautions first?
- **Player:** It's okay actually. I tend to rush into things and most of the time everything works out fine.
- **Alpheus:** Goodness! Can you believe this?
- **Eliza:** HOW DO YOU DO IT? My whole life I've been told what to be afraid of! I wish I could have your courage.
- **Player:** Uh... well... I just feel... compelled to do things, you know? Like there's an external force guiding my actions.
- **Eliza:** Oh that sounds amazing! You sound like the perfect person to conduct this line of research then!
- **Alpheus:** I concur. Just think of all the paperwork we'll avoid!
- **Alpheus:** If you find all the pieces of that totem, put them together and see what happens next.

#### Subsequent dialogue

- [Menu]: Choose an option:
  - [Choice]: What do you think about the island?
    - (above|island)
  - [Choice]: What can you tell me about totem pieces?
    - **Eliza:** Those totems appear to hold a huge amount of magical energy, but they seem to have broken into pieces.
    - **Eliza:** If you could find all the pieces of a totem and repair it, then it will likely create an item of immense power.
    - (initial)
  - [Choice]: Do you have anything I can store totem pieces in?
    - ''(Without a totem bag:)
      - [You receive a reinforced bag that looks like it will be strong enough to carry totem pieces.]
      - (receives=totem bag)
      - **Eliza:** I hope that helps.
      - (initial)
    - *(With a totem bag in backpack:)*
      - **Eliza:** You already have one in your backpack. Are you okay or is the heat getting to you?
      - (initial)
    - *(With a totem bag in bank:)*
      - **Eliza:** You already have one. Tell you what though, I will have someone fetch it for you.
      - {{qact|Screen fades out and in.}}
      - [You receive a reinforced bag that looks like it will be strong enough to carry totem pieces.]
      - **Eliza:** I hope that helps.
      - (initial)
  - [Choice]: I should go.
    - **Eliza:** Happy exploring!

### Block of Stone

- {{Main|Transcript:Helping Laniakea (miniquest)#Block of Stone}}

### Archaeology assistants


#### Showing them an assembled totem

- **Eliza:** You've rebuilt a totem? And you're still alive! What luck!
- **Alpheus:** And just as we've completed some compelling research that may lead to the next step.
- **Eliza:** Oh yes! This is very exciting! As part of our research we've discovered the island has what we're calling 'magical ley lines'.
- **Alpheus:** Yes. There seems to be a flow of magic on and around the island which seems to form concentrations in certain areas. I'm sure the totem has a connection to them.
- **Eliza:** If you explore the island you may find where these totems belong. Placing them should create the connection between the island and the power within the totem.
- **Alpheus:** And who knows what that will do.
- **Eliza:** Maybe an explosion? It will be thrilling regardless I'm sure.
- **Player:** Sure, I'll see what I can find...

#### Talking to them after completing a totem ritual and with the Associate rank in Archaeology

- **Alpheus:** Hey, so, word has got around that you're now an associate of the Archaeology Guild, and that you've set up a research team...
- **Eliza:** Alpheus and I were wondering if you could make use of us two as research assistants...
- Alpheus and Eliza have joined your research team!
- **Player:** Hey, sure thing! The more the merrier. I could do with some assistants as it happens.
- **Eliza:** That's awesome, thank you! We'll do you proud!
- **Alpheus:** Yeah, Eliza and I will work hard. You won't regret this! Thank you.
- (continuea|NormalDialogue)
