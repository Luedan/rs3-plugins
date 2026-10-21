# Civilian

- **Original Wiki Page**: [Transcript:Civilian](https://runescape.wiki/w/Transcript%3ACivilian)
- **Letter**: `C`

---

## Dialogue Transcript


### After Plague City, before Plague's End


#### While not wearing full Mourner gear


##### Civilian #1 (long hair with green pants)

- **Player:** Hi there.
- **Civilian:** Good day to you, traveller.
- **Player:** What are you up to?
- **Civilian:** Chasing mice as usual! It's all I seem to do nowadays.
- **Player:** You must waste a lot of time?
- **Civilian:** Yes, but what can you do? It's not like there's many cats around here!
- (Condition: With the Witch's cat in backpack:)
  - **Player:** I have a cat...look!
  - **Civilian:** Hmmm...doesn't look like it's seen daylight in years. That's not going to catch any mice!
- (Condition: With a kitten or cat follower, or in backpack:)
  - (continue|Cat sale dialogue)
- (Condition: Otherwise:)
  - **Player:** No, you're right, you don't see many around.

##### Civilian #2 (bald with green top)

- **Player:** Hello there.
- **Civilian:** I'm a bit busy to talk right now, sorry.
- **Player:** Why? What are you doing?
- **Civilian:** Trying to kill these mice! What I really need is a cat!
- (Condition: With the Witch's cat in backpack:)
  - (above|daylight)
- (Condition: With a kitten or cat follower, or in backpack:)
  - (continue|Cat sale dialogue)
- (Condition: Otherwise:)
  - (above|notmany)

##### Civilian #3 (blond hair with red pants)

- **Player:** Hello there.
- **Civilian:** Oh, hello. I'm sorry, I'm a bit worn out.
- **Player:** Busy day?
- **Civilian:** Oh, it's those mice! They're everywhere! What I really need is a cat, but they're hard to come by nowadays.
- (Condition: With the Witch's cat in backpack:)
  - (above|daylight)
- (Condition: With a kitten or cat follower, or in backpack:)
  - (continue|Cat sale dialogue)
- (Condition: Otherwise:)
  - (above|notmany)

#### While wearing full Mourner gear

- **Player:** Hello.
- **Civilian:** If you Mourners really wanna help, why don't you do something about these mice?!

### After Plague's End


#### While not wearing full Mourner gear


##### Civilian #1 (long hair with green pants)

- **Player:** Hi there.
- **Civilian:** Good day to you, [hero/heroine] of Ardougne.
- (continuea)

##### Civilian #2 (bald with green top)

- (above)

##### Civilian #3 (blond hair with red pants)

- (above)

#### While wearing full Mourner gear

- **Player:** Hello.
- **Civilian:** Ugh, a Mourner. I'm glad Player finally ratted you out.

### Cat sale dialogue

- [Menu]: Select an Option
  - [Choice]: cond=With a kitten follower, or in backpack|I have a kitten that I could sell.
    - **Player:** I have a kitten that I could sell.
    - **Civilian:** Really, let's have a look.
    - You present the kitten.
    - **Civilian:** Hah!  little thing won't catch any mice. I need a fully grown cat.
  - [Choice]: cond=With a cat follower, or in backpack|I have a cat that I could sell.
    - **Player:** I have a cat that I could sell.
    - **Civilian:** You don't say. Is that it?
    - **Player:** Say hello to a real mouse-killer!
    - **Civilian:** Hmmm, not bad, not bad at all. Looks like it's a lively one.
    - **Player:** Erm...kind of...
    - **Civilian:** I don't have much in the way of money, but I do have these!
    - [The peasant shows you a sack of death runes.]
    - (Condition: Without the easy Ardougne achievements:)
      - **Civilian:** The dwarves bring them from the mine for us. Tell you what, I'll give you 100 death runes for the cat.
      - (continue)
    - (Condition: With the easy Ardougne achievements:)
      - **Civilian:** The dwarves bring them from the mine for us. Tell you what, as you've been doing a lot of exploring around Ardougne I'll give you 200 death runes for the cat.
      - (continue)
    - [Menu]: Select an Option
      - [Choice]: Nope, I'm not parting for that.
        - **Player:** Nope, I'm not parting for that.
        - **Civilian:** Well, I'm not giving you any more!
      - [Choice]: Okay, then, you've got a deal.
        - **Player:** Okay, then, you've got a deal.
        - **Civilian:** Great! Hand over the cat and I'll give you the runes.
  - [Choice]: Nope, they're not easy to get hold of.
    - **Player:** Nope, they're not easy to get hold of.

#### Using a cat on the civilian

- (removes=cat) (receives=100 or 200 death runes)
- [You hand over the cat. You are given [100/200] death runes.]
- **Civilian:** Great, thanks for that!
- **Player:** That's okay. Take care.

#### Using a kitten on the civilian

- **Civilian:** That kitten isn't big enough; come back when it's bigger.
