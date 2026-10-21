# Mind-controlled monkey butler

- **Original Wiki Page**: [Transcript:Mind-controlled monkey butler](https://runescape.wiki/w/Transcript%3AMind-controlled%20monkey%20butler)
- **Letter**: `M`

---

## Dialogue Transcript

{{Incomplete|Missing dialogue from Invention Guild before hiring and firing dialogue from POH}}

### In the Invention Guild

{{Cleanup|The dialogue title may be inaccurate, the "yes" branch may be missing dialogue, and the "no" branch is missing}}
- Would you like to hire the mind-controlled monkey butler?
  - Yes.
    - **Mind-controlled monkey butler:** Happy! Steve has a new Master.
    - {{Qact|The butler vanishes}}
  - No.
    - {{Transcript missing}}

### In a player-owned house


#### Calling the butler

- {{Qact|The butler teleports next to the player}}
- **Mind-controlled monkey butler:** Happy. Master need Steve?
- (continue|butler-options)

#### Talking to the butler

- **Mind-controlled monkey butler:** Happy. Master need help?
- Select an Option
  - Go to the bank/sawmill...
    - Select an Option
      - Take something to the bank
        - **Player:** Can you take something to the bank for me?
        - **Mind-controlled monkey butler:** Happy! Give to Steve. Steve take to bank.
      - Bring something from the bank
        - What would you like from the bank?
          - *Option set 1*
            - *(If the player has previously used the butler to retrieve something from the bank:)*
              - Fetch another [quantity] [item].
            - Wooden planks.
            - Oak planks.
            - Teak planks.
          - *Option set 2*
            - Mahogany planks.
            - Soft clay.
            - Limestone brick.
            - Steel bar.
          - *Option set 3*
            - Cloth.
            - Gold leaf.
            - Marble block.
            - Magic housing stone.
          - More...
            - ((Cycles through the above sets of options.))
        - (Interface with prompt "Enter amount:" opens.)
        - {{Qact|The butler disappears}}
        - The servant goes to the bank.
        - {{Qact|The butler reappears next to the player}}
        - (receives=some or all of the item(s) requested, depending upon free space in the backpack)
        - *(If the player requested planks and has a plank box with space to hold them:)*
          - **Mind-controlled monkey butler:** Happy! Steve put Master's stuff in Master's plank box.
        - *(If the player did not have enough space in the backpack to hold two or more items:)*
          - **Mind-controlled monkey butler:** Happy! Steve hold Master's stuff until Master need them.
          - Select an Option
            - Take it back to the bank
              - **Player:** Take it back to the bank please.
              - **Mind-controlled monkey butler:** Happy. Steve return items.
              - {{Qact|The butler disappears and later reappears next to the player}}
            - Thanks
              - **Player:** Thanks.
        - *(If the player did not have enough space in the backpack to hold one item:)*
          - **Mind-controlled monkey butler:** Happy! Steve hold Master's thing until Master need it.
          - (above|butler-item-overflow)
        - *(Otherwise:)*
          - **Mind-controlled monkey butler:** Happy! Steve return with Master's stuff.
      - Take something to the sawmill
        - **Mind-controlled monkey butler:** Happy! Steve go to sawmill.
  - Misc...
    - Select an Option
      - Make tea
        - **Mind-controlled monkey butler:** Happy! Steve make tea.
        - {{Qact|The butler appears in the kitchen and makes tea, returning to the player once finished}}
        - **Mind-controlled monkey butler:** Happy. Master want milk?
        - Select an Option
          - Yes please
            - **Player:** Yes please.
            - (receives=a milky cup of tea)
          - No thanks
            - **Player:** No thanks.
            - (receives=a cup of tea)
          - Actually I don't want any
            - **Player:** Actually I don't want any.
      - Serve dinner
        - **Mind-controlled monkey butler:** Happy! Serving.
        - ''(If the player does not have anything built in the dining room's table space:)
          - **Mind-controlled monkey butler:** Confused. Table? Table missing.
        - *(If the player does not have a larder, stove, sink, and shelves built in the kitchen:)*
          - **Mind-controlled monkey butler:** Confused. No kitchen. Steve need kitchen.
          - Your kitchen must contain:<br>A larder<br>A stove<br>A sink<br>Kitchen shelves
        - *(Otherwise:)*
          - {{Qact|The butler appears in the kitchen and prepares dinner, placing it on the dining room table once finished}}
      - Serve drinks
        - **Player:** Serve drinks please.
        - **Mind-controlled monkey butler:** Happy. Steve make drinks!
        - *(If the player does not have anything built in the kitchen's barrel space:)*
          - **Mind-controlled monkey butler:** Confused. Master have no big drink to make small drinks.
        - *(Otherwise:)*
          - {{Qact|The butler appears in the kitchen and prepares drinks, returning to the player once finished}}
          - **Mind-controlled monkey butler:** Happy! Master accept drink?
          - Select an Option
            - Yes please
              - **Player:** Yes please!
              - (receives=the drink corresponding to whichever beer barrel is built in the barrel space)
              - **Mind-controlled monkey butler:** Happy. Steve hope Master like.
            - No thanks
              - **Player:** No thanks.
            - Something else
              - (initial|butler-options)
      - Greet guests
        - **Player:** Stay at the entrance and greet guests.
        - **Mind-controlled monkey butler:** Happy! Steve greet Master's friends.
        - {{Qact|The butler appears next to the portal}}
  - Stop following me
    - (The butler now wanders throughout the area.)
  - You're fired
    - Do you really want to fire your servant?
      - Yes.
        - {{Transcript missing}}
      - No.
        - (end)

#### Talking to the butler while he is holding items fetched from the bank

- (above2|butler-holding-items)

#### Using an item on the butler

- Take this item to the bank?
  - Bank
    - (Interface with prompt "Enter amount:" opens.)
    - {{Qact|The butler disappears, removing the items from the backpack and depositing them in the bank}}
    - The servant goes to the bank.
  - Cancel
    - (end)
