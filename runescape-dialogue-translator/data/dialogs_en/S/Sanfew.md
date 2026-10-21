# Sanfew

- **Original Wiki Page**: [Transcript:Sanfew](https://runescape.wiki/w/Transcript%3ASanfew)
- **Letter**: `S`

---

## Dialogue Transcript


### In Taverley


#### Before Druidic Ritual

- **Sanfew:** What can I do for you young 'un?
- **Player:** So... I've heard you druids might be able to teach me Herblore...
- **Sanfew:** Herblore eh? You're probably best off talking to Kaqemeex about that; he's the best herblore teacher we currently have. I believe at the moment he's at our stone circle just north of here.
- **Sanfew:** 'Course he's just the best teacher. You don't need him to show you how it works. Not like in my day. Back then you had to go running all over the place before you so much as learned how to wipe muck off a leaf.
- **Sanfew:** Still, that's what the kids are all like these days. No time to stop and listen to a teacher. With their 'rune armour', and their 'chilly-chompers' and their loud music...
- **Player:** Uh... thanks?

#### After Druidic Ritual

- **Sanfew:** What can I do for you young 'un?
- [Menu]: Select an Option
  - [Choice]: Have you any more work for me?
    - (Condition: Having not yet completed Troll Stronghold:)
      - **Sanfew:** Not just yet, young 'un.
    - (Condition: Having completed Troll Stronghold, but below level 31 Herblore:)
      - **Sanfew:** I'm afraid you are not yet learned enough in the art of Herblore to be able to help me, adventurer...
    - (Condition: Having completed Troll Stronghold and with level 31 Herblore:)
      - (see|Eadgar's Ruse)
  - [Choice]: Actually, I don't need to speak to you.
    - **Sanfew:** Well, we all make mistakes sometimes.
    - Sanfew grunts.

#### After Eadgar's Ruse

- **Sanfew:** What can I do for you young 'un?
- [Menu]: Select an Option
  - [Choice]: cond=Without goutweed in backpack|Did you say you needed more goutweed?
    - **Player:** Did you say you needed more goutweed?
    - **Sanfew:** I don't need any more goutweed for the ritual, but it's still quite difficult for me to get. If you ever come across some, bring it to me; I'll exchange it for some other herbs.
  - [Choice]: cond=With goutweed in backpack|I have some more goutweed for you.
    - (removes=goutweed) (receives=random herbs)
    - **Player:** I have some more goutweed for you.
    - **Sanfew:** Ah, good. Here are some herbs in exchange.
  - [Choice]: ave you any more work for me, to help reclaim the circle?
    - **Player:** Have you any more work for me to help reclaim the stone circle?
    - **Sanfew:** Well, not right now I don't think young 'un. In fact, I need to make some preparations myself for the ritual. Rest assured, if I need any more help I will ask you again.
  - [Choice]: Actually, I don't need to speak to you.
    - (above)

#### With partial completion of Zogre Flesh Eaters

- **Sanfew:** What can I do for you young 'un?
- [Menu]: Select an Option
  - [Choice]: Ask about Sanfew Serum.
    - **Player:** Hey there, can you tell me something about this Sanfew Serum, like how do I make it, and what does it do?
    - **Sanfew:** Certainly. It was after all, my creation, and mine alone. If anyone should know how to make it, it should be me!
    - **Player:** Can't fault that logic!
    - **Sanfew:** Ok, essentially this potion is a mixture of a cure poison and restore stats all rolled into one! Very hand for the adventurers with an eye on conserving inventory space.
    - **Player:** Ok, I'm sold... How do you make it?
    - **Sanfew:** Well, it's very easy really. You take a standard super stat restore potion. Add some ground unicorn horn. Then, add some snake weed from the island of Karamja. Finally, add some nail beast nails. You can only get these from the
    - **Sanfew:** area of Morytania, specifically, if you go deep in the Mort Myre swamp.
    - **Player:** How do you mean, deep into the Mort Myre swamp?
    - **Sanfew:** Well, most adventurers avoid the deep Mort Myre swamp, whereas the Paterdomus trek and the Burgh de Rott trek take you through the most interesting areas. These areas often allow the quickest, but potentially more dangerous
    - **Sanfew:** routes, through Mort Myre. This is where you're likely to encounter a nail beast.
    - **Player:** Are they very dangerous?
    - **Sanfew:** They can be pretty dangerous. They'll defend for a long time, then attack suddenly and seemingly without warning, landing three vicious attacks at once. This can be pretty lethal. However, the nail beasts can be damaged by
    - **Sanfew:** the Sanfew Serum itself... it's very bizarre that a potion made from their claws should have such a pronounced effect on them.
    - **Player:** Ok, that’s very helpful. Many thanks for your assistance.
  - [Choice]: Ask general questions.
    - (Condition: Before Druidic Ritual:)
      - (above2|Before Druidic Ritual)
    - (Condition: After Druidic Ritual:)
      - (above2|After Druidic Ritual)
    - (Condition: After Eadgar's Ruse:)
      - (above2|After Eadgar's Ruse)
