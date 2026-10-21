# Spirit tree (Incomitatus)

- **Original Wiki Page**: [Transcript:Spirit tree (Incomitatus)](https://runescape.wiki/w/Transcript%3ASpirit%20tree%20%28Incomitatus%29)
- **Letter**: `S`

---

## Dialogue Transcript


### At the mountains east of the Poison Waste


#### First time dialogue after The Path of Glouphrie

- **Spirit tree:** Thank you, tree whisperer. My brethren tell me that, in the past, you have had to travel back to our paternal tree before choosing your destination; however, your deeds have enhanced your attunement to the anima mundi and
- **Spirit tree:** there is no more need for this. You may now travel freely between all of my brethren.
- (continue|Standard dialogue)

#### Standard dialogue


##### If there is no Evil Tree

- **Spirit tree:** If you are a friend of the gnome people, you are a friend of mine. Do you wish to travel, or are you here to ask about the evil tree?
- [Menu]: What would you like to ask about?
  - [Choice]: Travel.
    - **Spirit tree:** You can travel to the trees related to me. Where do you wish to travel, whisperer?
    - (opens=Spirit tree)
      - *(Upon selecting a valid spirit tree:)*
        - You feel at one with the spirit tree.
        - {{Qact|The player is teleported to the selected spirit tree.}}
  - [Choice]: Evil tree.
    - (Condition: If there is currently an active Evil Tree which was recently killed:)
      - **Spirit tree:** The taint of the evil tree is not currently on the land. There won't be an evil tree for a long time.
      - (continue)
    - (Condition: Otherwise:)
      - **Spirit tree:** The taint of the evil tree is not currently on the land. There will be an evil tree in approximately [number] hour [number] minutes.
      - (continue)
    - **Spirit tree:** I can help you find the where it will spawn, but my knowledge outside of the anima mundi is limited.
    - **Spirit tree:** It can be found close to a [location] *(See Evil Tree#Locations with hints for list of locations)*.
    - [Menu]: Select an option
      - [Choice]: What is this 'evil tree'?
        - **Spirit tree:** It is an abomination of nature that must be destroyed as quickly as possible. We do not know where it will appear, but, when it does, you should go to it immediately and help out!
      - [Choice]: Goodbye.
        - **Spirit tree:** Goodbye.
  - [Choice]: Nothing.
    - **Player:** Nothing, thanks.

#### If there is a strange sapling

- **Spirit tree:** If you are a friend of the gnome people, you are a friend of mine. Do you wish to travel, or are you interested in the strange sapling?
- [Menu]: What would you like to ask about?
  - [Choice]: Travel.
    - **Spirit tree:** You can travel to the trees related to me. Where do you wish to travel, whisperer?
    - (opens=Spirit tree)
      - *(Upon selecting a valid spirit tree:)*
        - You feel at one with the spirit tree.
        - {{Qact|The player is teleported to the selected spirit tree.}}
  - [Choice]: Strange sapling.
    - **Spirit tree:** I can help you to find the strange sapling, but my knowledge outside of the anima mundi is limited.
    - **Spirit tree:** It can be found at [location] *(See Evil Tree#Locations with hints for list of locations)*.
  - [Choice]: Nothing.
    - **Player:** Nothing, thanks.

##### If there is an active Evil Tree

- **Spirit tree:** If you are a friend of the gnome people, you are a friend of mine. Do you wish to travel, or are you here to help dispatch the evil tree?
- [Menu]: What would you like to ask about?
  - [Choice]: Travel.
    - **Spirit tree:** You can travel to the trees related to me. Where do you wish to travel, whisperer?
    - (opens=Spirit tree)
      - *(Upon selecting a valid spirit tree:)*
        - You feel at one with the spirit tree.
        - {{Qact|The player is teleported to the selected spirit tree.}}
  - [Choice]: Evil tree.
    - **Spirit tree:{{anchor|evil-tree-teleport}}** Would you like me to teleport you directly there?
    - [Menu]: Select an option
      - [Choice]: Yes, please.
        - {{qact|The player is teleported to the location of the Evil Tree.}}
      - [Choice]: What is this 'evil tree'?
        - **Spirit tree:** It is an abomination of nature, which has appeared at [location]*(See Evil Tree#Locations with hints for list of locations)*. You should go there immediately to help out!
        - (continuea|evil-tree-teleport)
      - [Choice]: I've changed my mind, I want to stay here.
        - **Spirit tree:** Suit yourself.
  - [Choice]: Nothing.
    - **Player:** Nothing, thanks.
