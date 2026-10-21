# Gatekeeper

- **Original Wiki Page**: [Transcript:Gatekeeper](https://runescape.wiki/w/Transcript%3AGatekeeper)
- **Letter**: `G`

---

## Dialogue Transcript


### At the entrance to Zanaris Market area


#### Before A Fairy Tale III - Battle at Ork's Rift


##### Talk to

- **Player:** What happened to the old man who used to be the doorman?
- **Gatekeeper:** You mean my father? He went into retirement. I've taken over the family business.
- **Player:** Your father? But you don't look anything like him!
- **Gatekeeper:** No. Fortunately for me, I inherited my good looks from my mother.

##### Interacting with the gate

- (Condition: If the player has any kind of sacks:)
  - **Gatekeeper:** Sorry, we cannot allow you to bring those sacks into the market for security reasons.<!--Always plural "sacks".-->
- (Condition: Without any kind of sacks:)
  - **Gatekeeper:** You may not pass through this door without paying the trading tax.
  - **Player:** So how much is the tax?
  - **Gatekeeper:** The cost is one diamond.
  - [Menu]: Select an Option
    - [Choice]: Okay...
      - **Player:** Okay...
      - (Condition: Without a diamond:)
        - **Player:** ...but...
        - **Player:** I haven't brought my diamonds with me.
        - **Gatekeeper:** No tax, no entry.
      - (Condition: With a diamond:)
        - (removes=diamond)
        - You give the doorman a diamond.
        - {{Qact|The player enters through the magic door.}}
    - [Choice]: A diamond? Are you crazy?
      - **Player:** A diamond? Are you crazy?
      - **Gatekeeper:** Not at all. Those are the rules.
    - [Choice]: I haven't brought my diamonds with me.
      - **Player:** I haven't brought my diamonds with me.
      - **Gatekeeper:** No tax, no entry.
    - [Choice]: What do you do with all the diamonds you get?
      - **Player:** What do you do with all the diamonds you get?
      - **Gatekeeper:** Ever heard of fairylights? Well how do you think we make 'em? First we collect a pile of gems and then we get a spider to spin 'em into a long web, we light the jewels by imbuing each one with a little bit of magic.
      - **Player:** So you're telling me fairylights are made out of gems?
      - **Gatekeeper:** That's right, how else could we make 'em twinkle so beautifully?

#### After A Fairy Tale III - Battle at Ork's Rift


##### Talk to

- **Gatekeeper:** Many thanks for saving Zanaris from the Fairy Godfather and his orks.
- **Gatekeeper:** Please feel free to enter and leave the market as you please; we could not possibly charge you a diamond after all you have done for us.
- [Menu]: Select an Option
  - [Choice]: Why, thank you.
    - **Player:** Why, thank you.
    - **Gatekeeper:** No, thank you.
  - [Choice]: What happened to the old man that used to be the doorkeeper?
    - (above|inherited)

##### Interacting with the gate

- (Condition: If the player has any kind of sacks:)
  - **Gatekeeper:** Sorry, we cannot allow you to bring those sacks into the market for security reason.<!--Always plural "sacks".-->

##### Using Nuff's certificate on them

- (Condition: Before studying the certificate:)
  - [You show the certificate to the gatekeeeper.]
  - **Player:** Do you know what these strange marks mean?
  - **Gatekeeper:** That you've been doodling? If you don't mind, I have a job to do. Please stop distracting me.
- (Condition: After studying the certificate:)
  - [You show the certificate to the gatekeeeper.]
  - **Player:** Do you know what these strange marks mean?
  - **Gatekeeper:** No, I don't, and I'm trying to work here. Please stop distracting me.

### Near the entrance to the Tanglefoot's lair


#### Talk to


##### During A Fairy Tale I - Growing Pains

- **Player:** What are you doing all the way over here? Shouldn't you be at the market door?
- **Gatekeeper:** Yes, that's my usual spot, but the Godfather said I should be here, so here I am.

##### After A Fairy Tale I - Growing Pains

- **Gatekeeper:** Hello, did you just come from the market gates? Are my brothers doing their job well? I do worry that they'll start letting people into the market for free without me being there to supervise them!

#### Entering the grove


##### Before obtaining magic secateurs during A Fairy Tale I - Growing Pains

- **Gate Keeper:** I'm afraid nobody is allowed in there, orders from the boss.

##### After obtaining magic secateurs during A Fairy Tale I - Growing Pains

- **Gate Keeper:** I've received orders to let you through if you want. Good luck.

##### After defeating Tanglefoot

- **Gate Keeper:** Be careful in there, there are still some of those baby Tanglefootii around.
- {{Qact|The player appears in the grove.}}
- (Condition: During A Fairy Tale I, if the Queen's secateurs have been lost:)
  - (receives=Queen's secateurs)
  - [You find the Fairy Queen's secateurs!]
