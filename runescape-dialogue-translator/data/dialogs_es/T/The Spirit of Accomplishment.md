# The Spirit of Accomplishment

- **Original Wiki Page**: [Transcript:The Spirit of Accomplishment](https://runescape.wiki/w/Transcript%3AThe%20Spirit%20of%20Accomplishment)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Trade


#### Con menos de 99 Necromancy

- **Player:** Todavía no he logrado lo suficiente como nigromante para comprar un skillcape...

#### Con 99 o superior Necromancy

- [Menu]: ¿Comprar Necromancy skillcape?
  - [Choice]: Sí.
    - (Condition: With an inverted skillcape token:)
      - [El espíritu toma tu ficha de inversión de capa.]
      - (removes=inverted skillcape token)
      - (continue)
    - [Menu]: Elige una opción:
      - [Choice]: cond=While wearing an activated or imbued ring of charos:|¿92.000 coins? Eso es demasiado caro.
        - **Player:** Sé dónde encontrarte si cambio de opinión.
      - [Choice]: cond=Without an activated or imbued ring of charos:|¿99.000 coins? Eso es demasiado caro.
        - **Player:** Sé dónde encontrarte si cambio de opinión.
      - [Choice]: De hecho, creo que tengo el dinero aquí.
        - (Condition: Without enough coins:)
          - **Player:** Oh, no tengo suficiente coins para comprar esto.
        - (Condition: Without two free spaces in backpack:)
          - **Player:** Ah, necesito espacio tanto para la capa como para la capucha.
        - (Condition: With enough coins and two free spaces in backpack:)
          - (removes= 92,000 or 99,000 coins) (receives=a Necromancy cape (or trimmed variant) y capó)
          - **Player:** ¡Excelente! Usaré esta capa con orgullo.
      - [Choice]: cond=Having unlocked the inverted skillcape:|Me gustaría un skillcape con los colores invertidos.
        - (Condition: Without enough coins:)
          - **Player:** Oh, no tengo suficiente coins para comprar esto.
        - (Condition: Without two free spaces in backpack:)
          - **Player:** Ah, necesito espacio tanto para la capa como para la capucha.
        - (Condition: With enough coins and two free spaces in backpack:)
          - (removes= 92,000 or 99,000 coins) (receives=a Inverted hooded Necromancy cape)
          - **Player:** ¡Excelente! Usaré esta capa con orgullo.
  - [Choice]: No.
    - (end)
