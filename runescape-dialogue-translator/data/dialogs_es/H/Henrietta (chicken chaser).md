# Henrietta (chicken chaser)

- **Original Wiki Page**: [Transcript:Henrietta (chicken chaser)](https://runescape.wiki/w/Transcript%3AHenrietta%20%28chicken%20chaser%29)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Sell Animals

- **Henrietta (cazapollos):** Tengo un pedido especial para [breed]. ¡Especialmente si tiene el rasgo [Trait]!
- **Henrietta (cazadora de pollos):** Compraré hasta [número] pollos más.
- ((Repeated for each chicken in backpack:))
  - ¿Le gustaría vender [name] por frijoles [número]?
  - [Menu]: ¿Vender [name] por frijoles [número]?
    - [Choice]: Sí.
      - ((If the player has a million beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Henrietta (caza gallinas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - (continue)
      - ((If transaction would take the player over a million beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - [Menu]: ¿Completar la transacción de todos modos?
          - [Choice]: Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - [Choice]: No.
            - **Henrietta (caza gallinas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((Otherwise:))
        - (Action: El animal está vendido.)
        - Frijoles [número] agregados a su bolsa de divisas.
        - (continue)
    - [Choice]: No.
      - (end)
- ((If animals were not sold:))
  - **Player:** Déjame comprobar qué animales tengo que coincidan con tu solicitud.
- ((If animals were sold:))
  - ((If Henrietta can still buy more:))
    - (end)
  - ((If Henrietta can't buy more:))
    - **Henrietta (caza gallinas):** ¡He comprado suficientes animales para hoy!
    - (Action: Henrietta se teletransporta.)

### Quick-sell animals

- **Henrietta (caza gallinas):** ¿Estás segura de que quieres que me lleve todas las gallinas que tienes? No aceptaré ninguno de tus favoritos.
- [Menu]: ¿Vender todas tus gallinas?
  - [Choice]: si
    - ((With chickens in backpack:))
      - ((If the player has a million beans:))
        - ((Repeated for each remaining animal, then continues below:))
          - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - **Henrietta (caza gallinas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - No tienes animales para vender. ¡Cero animales, cero frijoles!
      - ((If transaction would take the player over a million beans:))
        - ((Repeated for each animal not surpassing the cap, then continues below:))
          - (Action: El animal está vendido.)
          - Frijoles [número] agregados a su bolsa de divisas.
        - ((Repeated for each animal left to sell, then continues below:))
          - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
          - [Menu]: ¿Completar la transacción de todos modos?
            - [Choice]: Sí.
              - (Action: El animal está vendido.)
              - Frijoles [número] agregados a su bolsa de divisas.
              - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
              - ((Repeated for each remaining animal, then continues below:))
                - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
                - **Henrietta (caza gallinas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - ((If multiple animals were sold:))
                - Has vendido animales [número] por un total de frijoles [número].
            - [Choice]: No.
              - **Henrietta (caza gallinas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - (continue)
        - ((If no animals were sold:))
          - No tienes animales para vender. ¡Cero animales, cero frijoles!
        - ((If multiple animals were sold:))
          - Has vendido animales [número] por un total de frijoles [número].
      - ((Otherwise:))
        - ((Repeated for each animal not surpassing the cap, then continues below:))
          - (Action: El animal está vendido.)
          - Frijoles [número] agregados a su bolsa de divisas.
        - ((If multiple animals were sold:))
          - Has vendido animales [número] por un total de frijoles [número].
    - ((Without chickens in backpack:))
      - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - [Choice]: No
    - (end)
