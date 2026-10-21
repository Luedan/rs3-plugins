# Party pack (non-player character)

- **Original Wiki Page**: [Transcript:Party pack (non-player character)](https://runescape.wiki/w/Transcript%3AParty%20pack%20%28non-player%20character%29)
- **Letter**: `P`

---

## Dialogue Transcript


### Retrieve item

- ((The Party Pack interface opens.))
- (Condition: When taking an item:)
  - (Condition: Without backpack space for the item:)
    - ((The following is shown in a pop-up interface:))
      - You must free up inventory space in order to take this item.
        - [Choice]: OK
          - ((The interface closes.))
  - (Condition: With backpack space for the item:)
    - (receives=item)
