# Simon Templeton

- **Original Wiki Page**: [Transcript:Simon Templeton](https://runescape.wiki/w/Transcript%3ASimon%20Templeton)
- **Letter**: `S`

---

## Dialogue Transcript

{{Incomplete|missing dialogue pre-dealing with scabaras, asking about his contract post-quest, and unknown conditional for "Fair Dinkum mate" vs "Fair dinkum, mate" when selling artefacts through talk-to option}}

### Talk-to


#### Normally


##### Before Dealing with Scabaras


##### First-time dialogue

- **Player:** Hello.
- **Simon Templeton:** G'day, mate. I'm Simon. Simon Templeton. Who are you?
- **Player:** I'm Player. What are you doing all the way out here?
- **Simon Templeton:** I've been contracted to retrieve artefacts from the top of this magnificient pyramid.
- **Player:** So, why are you down here and not up there?
- **Simon Templeton:** Well, it's me back...an old injury I picked up in Sophanem has come back to haunt me. I was working for Varrock Museum, but the gold they gave me wasn't even enough to pay for the carpet rides, let alone any decent equipment.
- **Simon Templeton:** But that was a long time ago... I can't even lift a chisel right now. There's no way I can climb all the way up there.
- **Simon Templeton:** Hang on a second... You look like you're pretty agile and up for a challenge. How about you retrieve them for me?
- **Simon Templeton:** I'll tell you what. I'll give you 1,000 coins for every artefact you get for me.
- **Player:** I'll see what I can do.
- **Simon Templeton:** Good on ya, mate!

##### Subsequent dialogue

- **Player:** Hello, Simon.
- **Simon Templeton:** G'day, Player.
- **Player:** How's it going?
- (Condition: If the player has not asked Simon Templeton about his contract to retrieve Agility Pyramid artefacts:)
  - **Player:** Hello, Simon.
  - **Simon Templeton:** G'day, Player.
  - **Player:** How's it going?
  - **Simon Templeton:** I've been contracted to retrieve artefacts from the top of this magnificent pyramid.
  - **Player:** So, why are you down here and not up there?
  - **Simon Templeton:** Well, it's me back...an old injury I picked up in Sophanem has come back to haunt me. I was working for Varrock Museum, but the gold they gave me wasn't even enough to pay for the carpet rides, let alone any decent equipment.
  - **Simon Templeton:** But that was a long time ago... I can't even lift a chisel right now. There's no way I can climb all the way up there.
  - **Simon Templeton:** Hang on a second... You look like you're pretty agile and up for a challenge. How about you retrieve them for me?
  - **Simon Templeton:** I'll tell you what. I'll give you 1,000 coins for every artefact you get for me.
  - **Player:** I'll see what I can do.
  - **Simon Templeton:** Good on ya, mate!
- (Condition: If the player has already asked Simon Templeton about his contract to retrieve Agility Pyramid artefacts:)
  - **Simon Templeton:** Got any Agility Pyramid artefacts for me?
  - (Condition: With pyramid tops in backpack:)
    - [Menu]: Select an option
      - [Choice]: Sell it.
        - **Player:** I have one here I'll sell you.
        - [Simon hands you a total of 1,000 coins for the sale.]
        - **Simon Templeton:** Ripper! Thanks a bundle, mate. Thanks to you, I can fulfill me contract. You're a true blue. The boss will be pleased.
        - **Player:** Glad I was able to help...but who is your boss? I thought you worked for Varrock Museum?
        - **Simon Templeton:** Mind your own bizzo, mate. But if you get any more, you know where I am.
      - [Choice]: Keep it.
        - **Player:** I have one, but I want to keep it for now.
        - **Simon Templeton:** Careful, mate. People might come looking for a thing like that.
        - **Player:** Thanks for the advice, but I'll hang onto it for now.
        - **Simon Templeton:** Bye, cobber.
  - (Condition: Without any pyramid tops in backpack:)
    - **Player:** No, I haven't.
    - **Simon Templeton:** Try harder, mate! It won't be long till some other critter turns up and stanches them out from under your eyes.
    - **Player:** I will. Goodbye, Simon.
    - **Simon Templeton:** Bye, cobber.

##### After Dealing with Scabaras

- **Player:** I'd like to talk a bit.
- **Simon Templeton:** Shoot away, sport.
- [Menu]: Select an Option
  - [Choice]: About that little job you mentioned...
    - **Player:** About that little job you mentioned...
    - (Condition: If the player has not talked to the guardian mummy about Pyramid Plunder artefacts:)
      - **Simon Templeton:** I can't remember whether I asked you to do this yet – mind like a sieve, I have – but have you ever talked to the Pyramid Plunder mummy in Sophanem about me?
      - **Player:** No, I haven't.
      - **Simon Templeton:** Well, that's what you can do for me. Ask him if he'll let me have a quick shufty at some of his relics. I think I may be able to cut him a deal.
    - (Condition: If the player has talked to the guardian mummy about Pyramid Plunder artefacts:)
      - [Menu]: Select an Option
        - [Choice]: I talked to the mummy in Sophanem.
          - **Player:** I talked to the mummy in Sophanem.
          - **Simon Templeton:** I take it she was no use. You look as dismal as a croc with toothache.
          - **Player:** No good news, for sure. Wait. What? She? I always assumed it was a man under those bandages.
          - **Simon Templeton:** Was your mummy a man? He, he, he.
          - **Player:** That joke stinks worse than those bronze 'antiques' I delivered to you.
          - **Simon Templeton:** Jokes aside, you've been a good sport. As a favour, from now on, I'm willing to take bank certificates of any objects you get from that miserable mummy's Pyramid Plunder. Well, any but the gold ones, that is - you might be tempted to fake stuff if there's a profit involved, as we both know.
          - **Player:** And the mummy has more loot plundered and ends up even more miserable. I see your cunning plan. It also makes me wonder, would your client for those artefacts be anything to do with a bank, by any chance?
          - **Simon Templeton:** Curiosity... Cats... Need I say more?
          - **Player:** I have some more questions.
          - **Simon Templeton:** Shoot away, sport.
          - (initial|initial-options)
        - [Choice]: Actually, I'd like to discuss business matters.
          - (Condition: If the player has not asked Simon Templeton about his contract to retrieve Agility Pyramid artefacts:)
            - (above|Subsequent_dialogue)
          - (Condition: If the player has already asked Simon Templeton about his contract to retrieve Agility Pyramid artefacts:)
            - (below|business-matters)
  - [Choice]: What do you know of other archaeologists in this area?
    - **Player:** What do you know of other archaeologists in this area?
    - **Simon Templeton:** They're all a bit dodgy, if ya gets me drift.
    - **Player:** Dodgy?
    - **Simon Templeton:** Them blokes in Varrock just put out the call for researchers, half trained 'em then ran out of cash. Left a load of folks about as angry as a barrel o' crocs. Young, angry and poor makes a fella dodgy.
    - **Player:** Why would Varrock stop the money?
    - **Simon Templeton:** They made all them fancy doodahs in the museum, for one. Bet they didn't come cheap. Then there's some island expedition they were planning – reckon that sucked up a load of cash, too.
    - **Simon Templeton:** Anyways, it does mean more folks willing to sell – so, silver linings, eh?
    - **Player:** Quite.
    - **Player:** I have some more questions.
    - **Simon Templeton:** Shoot away, sport.
    - (initial|initial-options)
  - [Choice]: Who are you selling all these items on to?
    - **Player:** Who are you selling all these items on to?
    - **Simon Templeton:** Well, it's not that Osman – I can tell ya that much. Don't be having dealings with him; he's a slippery customer.
    - **Player:** Slippery?
    - **Simon Templeton:** He was always after documents – new, old, fake, authentic. Claimed it didn't matter to him. Was obvious that royal history was what got him all excited, though. Now, what's a man like him wanting with that sort of information? He's not some fancy librarian, just some sort of lackey. He musta guessed I was onto something, so he cut me out cold.
    - **Player:** So, who do you sell to now?
    - **Simon Templeton:** Are you daft or what? I'm a middleman, a fixer – if I tell you that I'll be cutting me own throat. We'll talk about other stuff.
    - **Player:** I have some more questions.
    - **Simon Templeton:** Shoot away, sport.
    - (initial|initial-options)
  - [Choice]: What do you know of underground areas to the east?
    - **Player:** What do you know of underground areas to the east?
    - **Simon Templeton:** A bit of this, a bit of that. Those ruins are older than Sophanem and Menaphos, for sure. Pulled some documents out before them creepy crawlies took over.
    - **Player:** So the Scabarites are new arrivals there?
    - **Simon Templeton:** Seems so, but don't ask me why. All that research stuff is ancient history to me, now...if ya pardom me pun. I'm just gathering cash and that's it.
    - **Player:** Cash for what? There's nothing to spend it on out here in the middle of nowhere?
    - **Simon Templeton:** C'mon, sport. You know me better than to stick your snout where it might end up sliced off. Ask no questions, hear no lies.
    - **Player:** I have some more questions.
    - **Simon Templeton:** Shoot away, sport.
    - (initial|initial-options)
  - [Choice]: cond=Before using any other dialogue option:|Actually, I'd like to talk about business matters.
    - **Player:** Actually, I'd like to change the subject back to business matters.
    - (Condition: If the player has at least one Pyramid Plunder artefact or a pharaoh's sceptre in their backpack:)
      - **Player:** I have some interesting artefacts I'd like you to look at.
      - **Simon Templeton:** Bonza! Let's have a butcher's, mate.
      - **Simon Templeton:** Do you want to flog the lot of 'em?
      - [Menu]: Do you want to sell all your artefacts?
        - [Choice]: Yes, show me the money.
          - **Player:** Yes, show me the money.
          - (Condition: If the player has a pharaoh's sceptre in their backpack:)
            - **Simon Templeton:** You sellin' me this gold coloured stick thing? Looks fake to me. I'll give you 100 gold for it.
            - **Player:** What! This is a genuine pharaoh's sceptre - made out of solid gold and finely jewelled with precious gems by the finest craftsmen in the area.
            - **Simon Templeton:** Strewth! I can tell a pile of croc when I hear it! You've got the patter mate, but I'm no mug. That's a fake.
            - **Player:** It has magical powers!
            - **Simon Templeton:** Oh, magical powers ... yeah, yeah, yeah. Heard it all before mate. I'll give you a 100{{Sic}} gold, or some 'magic beans'. Take it or leave it.
            - **Player:** I don't think so! I'll find someone who'll give me what it's worth.
            - **Simon Templeton:** Suit yerself..{{Sic}} You wanna sell the other artefacts you have?
            - [Menu]: Sell other artefacts?
              - [Choice]: Yes, as long as I get a decent price for them.
                - **Player:** Yes, as long as I get a decent price for them.
                - (continue|sell-artefacts)
              - [Choice]: Nah, I've changed my mind.
                - **Player:** Nah, I've changed my mind.
          - (Condition: If the player does not have a pharaoh's sceptre in their backpack:)
            - (removes=all artefacts) (receives=coins)
            - (Condition: {{Transcript missing|(unknown conditional)):}}
              - **Simon Templeton:** Fair Dinkum mate, Bonzer doing business with you mate.
            - (Condition: {{Transcript missing|(unknown conditional)):}}
              - **Simon Templeton:** Fair dinkum, mate. Bonzer doing business with you.
        - [Choice]: No, let me think about it.
          - **Player:** No, let me think about it.
          - **Simon Templeton:** No probs mate. Just give me the items you want to sell and we can do them one by one.
    - (Condition: If the player does not have any Pyramid Plunder artefacts nor a pharaoh's sceptre in their backpack:)
      - (Condition: If the player has not sold Simon Templeton a pyramid top after asking about his contract to retrieve Agility Pyramid artefacts:)
        - **Simon Templeton:** Got any Agility Pyramid artefacts for me?
        - (continue|has-pyramid-top)
      - (Condition: If the player has sold Simon Templeton at least one pyramid top after asking about his contract to retrieve Agility Pyramid artefacts:)
        - **Simon Templeton:** Got any more Agility Pyramid artefacts for me?
        - (continue|has-pyramid-top)
      - (Condition: If the player has at least one pyramid top in their backpack:)
        - [Menu]: Select an Option
          - [Choice]: Sell [it/them].
            - **Player:**  I have [one/some] here I'll sell you.
            - (removes=all pyramid tops) (receives=[1,000/10,000 * N] coins)
            - [Simon hands you a total of [1,000/10,000 * N] coins for the sale.]
            - **Simon Templeton:** Ripper! Thanks a bundle, mate. Thanks to you, I can fulfill me contract. You're a true blue. The boss will be pleased.
            - **Player:** Glad I was able to help...but who is your boss? I thought you worked for Varrock Museum?
            - **Simon Templeton:** Mind your own bizzo, mate. But if you get any more, you know where I am.
          - [Choice]: Keep [it/them].
            - **Player:** I have [one/some], but I want to keep [it/them] for now.
            - **Simon Templeton:** Careful, mate. People might come looking for a thing like that.
            - **Player:** Thanks for the advice, but I'll hang onto it for now.
            - **Simon Templeton:** Bye, cobber.
      - (Condition: If the player does not have any pyramid tops in their backpack:)
        - **Player:** No, I haven't.
        - (Condition: If the player has not sold Simon Templeton a pyramid top after asking about his contract to retrieve Agility Pyramid artefacts:)
          - **Simon Templeton:** Try harder, mate! It won't be long till some other critter turns up and stanches them out from under your eyes.
          - **Player:** I will. Goodbye, Simon.
          - **Simon Templeton:** Bye, cobber.
        - (Condition: If the player has sold Simon Templeton at least one pyramid top after asking about his contract to retrieve Agility Pyramid artefacts:)
          - **Simon Templeton:** Well, keep my offer in mind if you do find one.
          - **Player:** I will. Goodbye, Simon.
          - **Simon Templeton:** Bye, mate.
  - [Choice]: cond=After using any other dialogue option:|Actually, I'd like to discuss business matters.
    - (above|change-subject-business-matters)

#### During the Gielinor Egg Hunt

- (see|Gielinor Egg Hunt (2024)#Talking to Simon Templeton)

### Trade


#### With Pyramid Plunder artefacts or a pyramid top in backpack

- [Menu]: Select an Option
  - [Choice]: Sell all your artefacts.
    - (removes=all artefacts) (receives=coins)
    - **Simon Templeton:** Fair Dinkum mate, Bonzer doing business with you mate.
  - [Choice]: Don't sell.
    - (end)

#### Without Pyramid Plunder artefacts nor a pyramid top in backpack

- **Simon Templeton:** Sorry, mate, I don't see anything I want.

### Using a Pyramid Plunder artefact on Simon Templeton


#### Unnoted items

- **Simon Templeton:** You wanna sell that mate?
- [Menu]: Do you want to sell your [artefact]?
  - [Choice]: Yes, show me the money.
    - **Player:** Yes, show me the money.
    - (removes=artefact) (receives=coins)
    - **Simon Templeton:** Cheers mate!
  - [Choice]: No, I think I'll keep it.
    - **Player:** No, I think I'll keep it.

#### Noted items


##### Before having unlocked the ability to sell noted items

- Simon wants nothing to do with this.
- ((Repeated in a pop-up:))
  - Simon wants nothing to do with this.

##### After having unlocked the ability to sell noted items

- **Simon Templeton:** You wanna sell that, mate?
- (Condition: Golden scarabs or gold seals:)
  - [Menu]: Do you want to sell your null{{Sic?}}
    - [Choice]: Yes, show me the money.
      - (above|yes-show-me-the-money)
    - [Choice]: No, I think I'll keep it.
      - (above|no-i-think-ill-keep-it)
- (Condition: Any other artefact:)
  - [Menu]: Do you want to sell your certed [artefact]?
    - [Choice]: Yes, show me the money.
      - (above|yes-show-me-the-money)
    - [Choice]: No, I think I'll keep it.
      - (above|no-i-think-ill-keep-it)

### Using a pyramid top on Simon Templeton

- **Simon Templeton:** Got any Agility Pyramid artefacts? I'll give you cash for any you have.
- [Menu]: Select an Option
  - [Choice]: Sell [it/them].
    - **Player:** I'll sell [it/them] to you.
    - (continuea|sell-tops)
  - [Choice]: Keep [it/them].
    - (above|keep-tops)

### Using a pharaoh's sceptre on Simon Templeton

- **Simon Templeton:** You sellin' me this gold coloured stick thing.{{Sic}} Looks fake to me. I'll give you 100 gold for it.
- **Player:** What! This is a genuine pharaoh's sceptre - made out of solid gold and finely jewelled with precious gems by the finest craftsmen in the area.
- **Simon Templeton:** Strewth! I can tell a pile of croc when I hear it! You've got the patter mate, but I'm no mug. That's a fake.
- **Player:** It has magical powers!
- **Simon Templeton:** Oh, magical powers ... yeah, yeah, yeah. Heard it all before mate. I'll give you a 100{{Sic}} gold, or some 'magic beans'. Take it or leave it.
- **Player:** I don't think so! I'll find someone who'll give me what it's worth.
- **Simon Templeton:** Suit yerself..{{Sic}}

### Using any other item on Simon Templeton


#### Before having unlocked the ability to sell noted items

- (above|simon-wants-nothing)

#### After having unlocked the ability to sell noted items

- Simon wants nothing to do with this.
