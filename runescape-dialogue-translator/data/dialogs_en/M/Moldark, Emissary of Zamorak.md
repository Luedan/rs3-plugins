# Moldark, Emissary of Zamorak

- **Original Wiki Page**: [Transcript:Moldark, Emissary of Zamorak](https://runescape.wiki/w/Transcript%3AMoldark%2C%20Emissary%20of%20Zamorak)
- **Letter**: `M`

---

## Dialogue Transcript

{{Template:Incomplete|missing dialogue from after completing all tasks}}

### Standard dialogue

- {{anchor|initial}}**Moldark, Emissary of Zamorak:** I, my friend, am Moldark: foremost follower of Zamorak. I am his emissary.
- **Moldark, Emissary of Zamorak:** I am here to teach you of the ways of chaos - the way of power!
- **Moldark, Emissary of Zamorak:** Join with me and with Zamorak! If you do, I may have some work for you.
- [Menu]: Choose an option:
  - [Choice]: Who are you?|cond=If continue from the previous options:
    - (continuea|initial)
  - [Choice]: Can you tell me about Zamorak?
    - **Moldark, Emissary of Zamorak:** What do you want to know about Zamorak?
    - [Menu]: Choose an option:
      - [Choice]: Who is Zamorak?
        - {{anchor|whoiszamorak}}**Moldark, Emissary of Zamorak:** Zamorak was once a mortal, like you and I. But he knew the value of chaos, and he sought power through it.
        - **Moldark, Emissary of Zamorak:** When the opportunity of godhood presented itself before him, Zamorak took it gladly.
        - **Moldark, Emissary of Zamorak:** Now, he is a powerful god, the god of chaos and destruction.
          - (other)
      - [Choice]: Why should I follow Zamorak?
        - **Moldark, Emissary of Zamorak:** Great creation can only follow great destruction. We all progress more quickly when chaos reigns.
        - **Moldark, Emissary of Zamorak:** But following Zamorak is about personal gain also. Like Zamorak, we should all be ready to take power when offered.
        - (other)
      - [Choice]: What does Zamorak want?
        - **Moldark, Emissary of Zamorak:** Zamorak sees the stagnation underneath the peace preached by the other gods. They want passive sheep to grind underfoot.
        - **Moldark, Emissary of Zamorak:** Zamorak sees the true way to greatness. It is through chaos and conflict that mortals make their biggest steps.
        - (other)
      - [Choice]: Talk about something else.
        - (previous)
  - [Choice]: I want to declare my support for Zamorak!
  - **Moldark, Emissary of Zamorak:** That's wonderful! On behalf of Zamorak's followers, I welcome you.
  - (receives=Banner of Zamorak)
  - **Moldark, Emissary of Zamorak:** Please, take this banner to show your support.
  - **Moldark, Emissary of Zamorak:** I have a gift for you: a book of stories regarding the gods and their followers. Please, read it.
  - **Moldark, Emissary of Zamorak:** Perhaps it will shed some light on the delusions of order and contingency held by the others.
  - **Moldark, Emissary of Zamorak:** The book is not yet complete, however. When you complete some jobs I will give you more pages.
  - (receives=Book of the Gods)
  - [The emissary gives you the Book of the Gods.]
  - (Condition: If in free-to-play worlds:)
    - [The book is currently incomplete. You can earn more pages by doing jobs for the emissary, which are only available on member's worlds.]
    - (previous)

### Dialogue with the players supporting Zamorak

- [Menu]: Choose an option:
  - [Choice]: Who are you?
    - (continuea|initial)
  - [Choice]: Can you tell me about Zamorak?
    - (continuea|whoiszamorak)
  - [Choice]: Do you have any jobs for me?
    - (Condition: If in free-to-play worlds:)
      - [God emissary jobs can only be performed on a member's worlds!]
      - (previous)
    - (see|God Emissaries)
  - [Choice]: Talk about rewards.
    - (see|God Emissaries#Rewards)

### Treasure Trails

- (Condition: Only the first time:)
  - **Moldark, Emissary of Zamorak:** What do you want with me?
  - **Player:** Can you help me with this treasure trail?
  - **Moldark, Emissary of Zamorak:** Only if you prove yourself by answering this question!
- (receives=challenge scroll (medium))
- [Moldark has given you a challenge scroll!]

##### When talked to again

- **Moldark, Emissary of Zamorak:** Please enter the answer to the question.
- Enter amount:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Moldark, Emissary of Zamorak:** Wrong!
- (Condition: When given the correct answer:)
  - (removes=the clue scroll (medium) and challenge scroll (medium))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [Moldark has given you another clue scroll!]
    - (continue)
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [You've found a casket!]
    - (continue)
  - (Condition: If the correct answer was 7 before Ritual of the Mahjarrat:)
    - **Moldark, Emissary of Zamorak:** Correct!
  - (Condition: If the correct answer was 7 after Ritual of the Mahjarrat:)
    - **Moldark, Emissary of Zamorak:** That was right, before the burning. You know what? I'll count that as a pass.
  - (Condition: If the correct answer was 3 after Ritual of the Mahjarrat:)
    - **Moldark, Emissary of Zamorak:** Correct. That's all that is left now. So much death...
Category:God Emissaries
