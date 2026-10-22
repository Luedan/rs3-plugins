# Zoe (zygomite trader)

- **Original Wiki Page**: [Transcript:Zoe (zygomite trader)](https://runescape.wiki/w/Transcript%3AZoe%20%28zygomite%20trader%29)
- **Letter**: `Z`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Sell Animals

- **Zoe (comerciante de zigomitas):** Tengo una solicitud especial para [breed]. ¡Especialmente si tiene el rasgo [Trait]!
- **Zoe (comerciante de zygomitas):** También busco algunos zygomitas; de hecho, compraré hasta [número] más mientras esté aquí.
- ((Repeated for each zygomite in backpack:))
  - ¿Le gustaría vender [name] por frijoles [número]?
  - [Menu]: ¿Vender [name] por frijoles [número]?
    - [Choice]: Sí.
      - ((If the player has a million beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Zoe (comerciante de zigomitas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - (continue)
      - ((If transaction would take the player over a million beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - [Menu]: ¿Completar la transacción de todos modos?
          - [Choice]: Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - [Choice]: No.
            - **Zoe (comerciante de zigomitas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((Otherwise:))
        - (Action: El animal está vendido.)
        - Frijoles [número] agregados a su bolsa de divisas.
        - (continue)
    - [Choice]: No.
      - (end)
- ((If animals were not sold:))
  - **Player:** Déjame comprobar qué animales tengo que coincidan con tu solicitud.
- ((If animals were sold:))
  - ((If Zoe can still buy more:))
    - (end)
  - ((If Zoe can't buy more:))
    - **Zoe (comerciante de zigomitas):** He comprado todos los animales que necesito por ahora, ¡nos vemos más tarde!
    - (Action: Zoe se teletransporta.)

### Quick-sell animals

- **Zoe (comerciante de zygomites):** ¿Estás seguro de que quieres que me lleve todos los zygomites que tienes? No aceptaré ninguno de tus favoritos.
- [Menu]: ¿Vender todos tus cigomitas?
  - [Choice]: si
    - ((With zygomites in backpack:))
      - ((If the player has a million beans:))
        - ((Repeated for each remaining animal, then continues below:))
          - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - **Zoe (comerciante de zigomitas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
                - **Zoe (comerciante de zigomitas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - ((If multiple animals were sold:))
                - Has vendido animales [número] por un total de frijoles [número].
            - [Choice]: No.
              - **Zoe (comerciante de zigomitas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
    - ((Without zygomites in backpack:))
      - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - [Choice]: No
    - (end)
