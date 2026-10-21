# Kazgar

- **Original Wiki Page**: [Transcript:Kazgar](https://runescape.wiki/w/Transcript%3AKazgar)
- **Letter**: `K`

---

## Dialogue Transcript


### In the tunnel near Lumbridge Castle cellar


#### Talking to him

- **Kazgar:** Hello, surface-dweller.
- [Menu]: Select an Option
  - [Choice]: Who are you?
    - **Player:** Who are you?
    - **Kazgar:** Mistag posted me here when surface-dwellers started visiting the mine. If you have business in the Dorgeshuun mines I will guide you through the tunnels.
    - [Menu]: Select an Option
      - [Choice]: Can you show me the way to the mine?
        - **Player:** Can you show me the way to the mine?
        - (Condition: Before Death to the Dorgeshuun:)
          - **Kazgar:** All right. Follow me.
          - (continue)
        - (Condition: After Death to the Dorgeshuun:)
          - **Kazgar:** Of course! You're always welcome in our mines!
          - (continue)
        - Kazgar shows you the way through the tunnels.
      - [Choice]: cond=After Death to the Dorgeshuun|Can you show me the way to the water mill cellar?
        - **Player:** Can you show me the way to the water mill cellar?
        - **Kazgar:** Of course!
        - Kazgar shows you the way through the tunnels.
      - [Choice]: Maybe some other time.
        - **Player:** Maybe some other time.
  - [Choice]: Can you show me the way to the mine?
    - (above)
  - [Choice]: cond=After Death to the Dorgeshuun|Can you show me the way to the water mill cellar?
    - (above)

#### Follow option


##### Before Death to the Dorgeshuun

- Kazgar shows you the way through the tunnels.

##### After Death to the Dorgeshuun

- [Menu]: Where do you want to go?
  - [Choice]: Dorgeshuun Mines
    - Kazgar shows you the way through the tunnels.
  - [Choice]: Water mill cellar
    - Kazgar shows you the way through the tunnels.
  - [Choice]: Nowhere
    - (end)
