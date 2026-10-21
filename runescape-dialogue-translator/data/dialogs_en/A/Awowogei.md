# Awowogei

- **Original Wiki Page**: [Transcript:Awowogei](https://runescape.wiki/w/Transcript%3AAwowogei)
- **Letter**: `A`

---

## Dialogue Transcript

{{Transcript npc|Awowogei}}

### After Monkey Madness


#### As a karamjan monkey

- **King Awowogei:**  We are still pondering your proposition...We will let you know when we have an answer...

#### As any other monkey

- **King Awowogei:** Hello stranger, what can I do for you?
- **Player:** I'm just exploring.
- **King Awowogei:** Well stranger, feel free to explore my kingdom for as long as you like.

### After Recipe for Disaster

- **King Awowogei:** Hello again,  I do anything for you?
- **Player:** Not really, just popping in to say hi.
- **King Awowogei:** Well, enjoy the .

### Chimp ice dialogue (After Do No Evil)


#### If the player does not have a chimp ice in inventory

- **King Awowogei:** Got any more chimp ices?
- **Player:** Not on me.
- **King Awowogei:** Well bring me some more, you've only brought me [number], after all.

#### If the player has a chimp ice in inventory

- **King Awowogei:** *Sniff sniff* Is that a chimp ice?
- **Player:** Yes, Your Majesty.
- **King Awowogei:** Bring me more and you shall see your colony prosper.
- Awowogei gobbles it up.
- (removes=chimp ice)
- {{tcond|If it's the 5th, 10th, or 15th delivery:}}
  - **King Awowogei:** Your colony has served me well. I'll have a statue built in the colony to celebrate your success!
- {{tcond|If it's the 25th delivery:}}
  - **King Awowogei:** Your colony has proven to be a valuable asset and will need safeguarding. I'll send my elite to protect you.
  - Congratulations! You have completed: 'Ice Ice Chimpy' - Complete 25 chimp ice deliveries. (25/25)
- (Condition: Otherwise:)
  - (Condition: If the reward is death runes:)
    - (receives=30 to 50 death runes)
    - **King Awowogei:** Take these death runes for your trouble.
  - (Condition: If the reward is blood runes:)
    - (receives=30 to 50 blood runes)
    - **King Awowogei:** Take these blood runes for your trouble.
  - (Condition: If the reward is a banana:)
    - (receives=banana)
    - **King Awowogei:** Take this banana for your trouble.
  - {{tcond|If the reward is a dragon scimitar:}}
    - (receives=dragon scimitar)
    - **King Awowogei:** Take this scimitar for your trouble.

### Sandy Clue Scroll (historical)

- ((Without space in backpack for a casket:))
  - You need more inventory space to receive your clue casket.
- ((With space in backpack:))
  - (removes=Sandy Clue Scroll and banana)
  - (Condition: If the trail continues:)
    - (receives=Sandy Scroll box)
    - {{tbox|pic=Sandy Scroll box detail.png|You hand Awowogei a banana and he hands you a {{Sic|scrollbox}}... silently.}}
  - (Condition: If the trail ends:)
    - (receives=Sandy Casket and Sandy Casket (red))
    - {{tbox|pic=Sandy Casket detail.png|pic2=Sandy Casket (red) detail.png|You hand Awowogei a banana and he hands you a casket... silently.}}
