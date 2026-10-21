# Spirit Tree (Prifddinas)

- **Original Wiki Page**: [Transcript:Spirit Tree (Prifddinas)](https://runescape.wiki/w/Transcript%3ASpirit%20Tree%20%28Prifddinas%29)
- **Letter**: `S`

---

## Dialogue Transcript


### In Prifddinas, after Plague's End


#### Talking to the Spirit Tree

- **Spirit Tree:** Hello, tree whisperer. I have been alone so long, but it is good to be part of the Anima Mundi once again.
  - (Condition: If the player has yet to reconnect the Spirit Tree to all of her brethren:)
    - **Spirit Tree:** I can hear my brethren clearly...but not all of them. I wonder, might you help reconnect me to them all?
      - (Condition: If the player has yet to aid Incomitatus:)
        - **Spirit Tree:** The tree to the south in the Poison Wastes sounds troubled.
        - (continue)
      - (Condition: If the player has yet to plant a Spirit tree in Port Sarim:)
        - **Spirit Tree:** I cannot sense my brethren in Port Sarim.
        - (continue)
      - (Condition: If the player has yet to plant a Spirit tree in Etceteria:)
        - **Spirit Tree:** I cannot sense my brethren in Etceteria.
        - (continue)
      - (Condition: If the player has yet to plant a Spirit tree in Brimhaven:)
        - **Spirit Tree:** I cannot sense my brethren in Brimhaven.
        - (continue)
      - (Condition: If the player has yet to plant a Spirit tree at Manor Farm:)
        - **Spirit Tree:** I cannot sense my brethren on Manor Farm.
        - (continue)
      - (Condition: If the player has a Spirit tree being grown:)
        - **Spirit Tree:** I feel my brethren in [location] is returning.
      - (Condition: If the player has a Spirit tree that is fully grown but not yet checked its health:)
        - **Spirit Tree:** My brethren in [location] is close. Perhaps you should go see them.
        - (continue)
    - **Spirit Tree:** If you could find a way to return these brethren to me, I would be most grateful. I've left a little reward with our gnome friend here should you manage this.
    - (continue|standard)
  - (Condition: If it is the first time speaking after all Spirit Trees have been regrown:)
    - **Spirit Tree:** No...wait...I can hear them all again! Thank you, tree whisperer, thank you! I've asked our gnome friend here to reward you for your efforts.
    - (continue|standard)

#### After all spirit trees have been connected


##### If there is no Evil Tree

- **Spirit tree:{{anchor|standard}}** If you are a friend of the gnome people, you are a friend of mine. Do you wish to travel, or are you here to ask about the evil tree?
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

##### If there is a strange sapling

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
