# The Spirit of Mastery

- **Original Wiki Page**: [Transcript:The Spirit of Mastery](https://runescape.wiki/w/Transcript%3AThe%20Spirit%20of%20Mastery)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Trade


#### Sin 120 Necromancy

- **Player:** Aún no domino la nigromancia, así que no puedo comprar un master cape...

#### Con 120 Necromancy

- (Condition: With an inverted skillcape token:)
  - [El espíritu toma tu ficha de inversión de capa.]
  - (removes=inverted master skillcape token)
  - (continue)
- (Condition: Having unlocked the inverted skillcape:)
  - [Menu]: Selecciona una opción
    - [Choice]: Me gustaría un master cape normal.
      - (continue)
    - [Choice]: Me gustaría un master cape invertido.
      - (continue)
- [Menu]: ¿Comprar Necromancy master cape por 120.000 coins?
  - [Choice]: Sí.
    - (Condition: Without free space in backpack:)
      - **Player:** No tengo suficiente espacio en mi backpack. Debería volver cuando tenga más.
    - (Condition: With free space in backpack:)
      - (Condition: Without 120,000 coins:)
        - No tienes suficiente dinero para comprar esta capa.
        - (pop-up)
          - {{Popup|You do not have enough money to purchase this<br>cape.|warning=yes}}
      - (Condition: Without 120,000 coins:)
        - (Action: Se escucha un tintineo.)
        - (removes=120,000 coins) (receives=Necromancy master cape or Inverted Necromancy master cape)
  - [Choice]: No.
    - (end)
