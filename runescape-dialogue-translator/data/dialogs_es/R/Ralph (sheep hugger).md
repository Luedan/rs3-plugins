# Ralph (sheep hugger)

- **Original Wiki Page**: [Transcript:Ralph (sheep hugger)](https://runescape.wiki/w/Transcript%3ARalph%20%28sheep%20hugger%29)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Sell Animals

- **Ralph (abraza-ovejas):** Tengo un pedido especial para [breed]. ¡Especialmente si tiene el rasgo [Trait]!
- **Ralph (abraza-ovejas):** También busco Sheep, de hecho compraré hasta [número] más mientras esté aquí.
- ((Repeated for each sheep in backpack:))
  - ¿Le gustaría vender [name] por frijoles [número]?
  - [Menu]: ¿Vender [name] por frijoles [número]?
    - [Choice]: Sí.
      - ((If the player has a million beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Ralph (abraza-ovejas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - (continue)
      - ((If transaction would take the player over a million beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - [Menu]: ¿Completar la transacción de todos modos?
          - [Choice]: Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - [Choice]: No.
            - **Ralph (abraza-ovejas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((Otherwise:))
        - (Action: El animal está vendido.)
        - Frijoles [número] agregados a su bolsa de divisas.
        - (continue)
    - [Choice]: No.
      - (end)
- ((If animals were not sold:))
  - **Player:** Déjame comprobar qué animales tengo que coincidan con tu solicitud.
- ((If animals were sold:))
  - ((If Ralph can still buy more:))
    - (end)
  - ((If Ralph can't buy more:))
    - **Ralph (abraza-ovejas):** He comprado todos los animales que necesito por ahora, ¡nos vemos más tarde!
    - (Action: Ralph se teletransporta.)

### Quick-sell animals

- **Ralph (abraza-ovejas):** ¿Estás seguro de que quieres que tome todo el Sheep que tienes en la mano? No aceptaré ninguno de tus favoritos.
- [Menu]: ¿Vender todas tus ovejas?
  - [Choice]: si
    - ((With sheep in backpack:))
      - ((If the player has a million beans:))
        - ((Repeated for each remaining animal, then continues below:))
          - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - **Ralph (abraza-ovejas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
                - **Ralph (abraza-ovejas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - ((If multiple animals were sold:))
                - Has vendido animales [número] por un total de frijoles [número].
            - [Choice]: No.
              - **Ralph (abraza-ovejas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
    - ((Without sheep in backpack:))
      - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - [Choice]: No
    - (end)
