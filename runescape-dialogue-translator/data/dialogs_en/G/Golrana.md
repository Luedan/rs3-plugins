# Golrana

- **Original Wiki Page**: [Transcript:Golrana](https://runescape.wiki/w/Transcript%3AGolrana)
- **Letter**: `G`

---

## Dialogue Transcript


### In the Tree Gnome Village, after The Prisoner of Glouphrie


#### First time dialogue

- **Golrana:** Thanks again for aiding me in my father's rescue, Player. While he gets back to full health, I've decided to stay in the Tree Gnome Village and care for him.
- **Golrana:** I thought I'd use the time to train up as a tree whisperer. If you have any spirit tree seeds, then I can keep them for you. I study them as part of my training, and you can get them back whenever you need them!
- **Golrana:** Uncle Bolren also allowed Belmondo to establish a gilder route to the village. Belmondo won him over with stories of his landing in the Galarpos Mountains and they've become fast friends since.
- **Golrana:** Bolren's no longer worried about having a flightpath so close to the village - as long as Belmondo's operating the line, of course!
- **Golrana:** I get all the men of my life close to me: my dad, my husband, my son and even my uncle!
- **Golrana:** Lucky lady, right?

#### Subsequent dialogue


##### Without any spirit seeds stored with Golrana, or in backpack

- **Golrana:** Hey, Player! Have you come to bring me some spirit tree seeds? I'll keep them for you.
- **Player:** No, I just came to see how things were.
- **Golrana:** How very unlike an adventurer! It's appreciated, of course. Dad's well; he's upstairs, recovering from his ordeal in Arposandra, and he's already planning the next step of his revenge, bless him. We visit mum's grave every weekend, too.
- **Golrana:** Golrie's back in the cave, and I'm holding back his allowance until he's organised it all.
- **Golrana:** My training's going well; the spirit trees quite like me, although they tell me that you are a great whisperer yourself. I'm starting to think that perhaps - but only perhaps - you may be as good an adventurer as me. And that's about it!
- **Player:** Glad to know it's all going okay. I'll see you later.

##### With any spirit seeds stored with Golrana, or with spirit seeds in backpack

- (Condition: Without any spirit seeds stored:)
  - **Golrana:** Hey, Player! Have you come to bring me some spirit tree seeds? I'll keep them for you.
  - (continue)
- (Condition: With exactly one spirit seed stored:)
  - **Golrana:** Hey, Player! Have you come to get back some of your spirit tree seeds? I'm storing one so far for you.
  - (continue)
- (Condition: With two or more spirit seeds stored:)
  - **Golrana:** Hey, Player! Have you come to get back some of your spirit tree seeds? I'm storing [number] so far for you.
  - (continue)
- [Menu]: Choose an option:
  - [Choice]: cond=With spirit seeds in backpack:|Give her all your seeds.
    - (removes=all spirit seeds in backpack)
    - [You store the seeds with Golrana.]
    - **Golrana:** Thank you! I'll watch over them preciously.
  - [Choice]: cond=With spirit seeds in backpack:|Give her some of your seeds.
    - {{Tinput|Enter amount:}}
      - (above|store)
  - [Choice]: cond=With spirit seeds stored with Golrana:|Withdraw all your seeds
    - (Condition: Without space in backpack:)
      - **Golrana:** Sorry, but you don't have enough space in your inventory for the seeds. Make some room and talk to me again.
    - (Condition: With space in backpack:)
      - (receives=spirit seeds)
      - [You reclaim all your seeds from Golrana.]
      - **Golrana:** There you go.
    - [Choice]: cond=With spirit seeds stored with Golrana:|Withdraw some of your seeds.
    - {{Tinput|Enter amount:}}
      - (Condition: Without space in backpack:)
        - (above|sorry)
      - (Condition: With space in backpack:)
        - (Condition: If withdrawing all seeds:)
          - (above|withdrawal)
        - (Condition: If withdrawing only some seeds:)
          - [You reclaim the seeds from Golrana.]
          - **Golrana:** There you go.
  - [Choice]: Talk about something else.
    - (above|other)
