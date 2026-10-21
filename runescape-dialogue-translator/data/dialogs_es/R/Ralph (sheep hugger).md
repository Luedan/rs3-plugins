# Ralph (sheep hugger)

- **Original Wiki Page**: [Transcript:Ralph (sheep hugger)](https://runescape.wiki/w/Transcript%3ARalph%20%28sheep%20hugger%29)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Sell Animals

- **Ralph (abraza-ovejas):** Tengo un pedido especial para [breed]. ¡Especialmente si tiene el rasgo [Trait]!
- **Ralph (abraza-ovejas):** También busco Sheep, de hecho compraré hasta [número] más mientras esté aquí.
- ((Repetido para cada oveja en backpack:))
  - ¿Le gustaría vender [name] por frijoles [número]?
  - [Menu]: ¿Vender [name] por frijoles [número]?
    - [Choice]: Sí.
      - ((Si el player tiene un millón de beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Ralph (abraza-ovejas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - (continue)
      - ((Si la transacción le tomara a el player más de un millón de beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - [Menu]: ¿Completar la transacción de todos modos?
          - [Choice]: Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - [Choice]: No.
            - **Ralph (abraza-ovejas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((De lo contrario:))
        - (Action: El animal está vendido.)
        - Frijoles [número] agregados a su bolsa de divisas.
        - (continue)
    - [Choice]: No.
      - (end)
- ((Si no se vendieran animales:))
  - **Player:** Déjame comprobar qué animales tengo que coincidan con tu solicitud.
- ((Si se vendieran animales:))
  - ((Si Ralph aún puede comprar más:))
    - (end)
  - ((Si Ralph no puede comprar más:))
    - **Ralph (abraza-ovejas):** He comprado todos los animales que necesito por ahora, ¡nos vemos más tarde!
    - (Action: Ralph se teletransporta.)

### Quick-sell animals

- **Ralph (abraza-ovejas):** ¿Estás seguro de que quieres que tome todo el Sheep que tienes en la mano? No aceptaré ninguno de tus favoritos.
- [Menu]: ¿Vender todas tus ovejas?
  - [Choice]: si
    - ((Con ovejas en backpack:))
      - ((Si el player tiene un millón de beans:))
        - ((Se repite para cada animal restante y luego continúa a continuación:))
          - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - **Ralph (abraza-ovejas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - No tienes animales para vender. ¡Cero animales, cero frijoles!
      - ((Si la transacción le tomara a el player más de un millón de beans:))
        - ((Se repite para cada animal que no supere el límite, luego continúa a continuación:))
          - (Action: El animal está vendido.)
          - Frijoles [número] agregados a su bolsa de divisas.
        - ((Se repite para cada animal que queda por vender y luego continúa a continuación:))
          - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
          - [Menu]: ¿Completar la transacción de todos modos?
            - [Choice]: Sí.
              - (Action: El animal está vendido.)
              - Frijoles [número] agregados a su bolsa de divisas.
              - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
              - ((Se repite para cada animal restante y luego continúa a continuación:))
                - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
                - **Ralph (abraza-ovejas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - ((Si se vendieron varios animales:))
                - Has vendido animales [número] por un total de frijoles [número].
            - [Choice]: No.
              - **Ralph (abraza-ovejas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - (continue)
        - ((Si no se vendieron animales:))
          - No tienes animales para vender. ¡Cero animales, cero frijoles!
        - ((Si se vendieron varios animales:))
          - Has vendido animales [número] por un total de frijoles [número].
      - ((De lo contrario:))
        - ((Se repite para cada animal que no supere el límite, luego continúa a continuación:))
          - (Action: El animal está vendido.)
          - Frijoles [número] agregados a su bolsa de divisas.
        - ((Si se vendieron varios animales:))
          - Has vendido animales [número] por un total de frijoles [número].
    - ((Sin ovejas en backpack:))
      - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - [Choice]: No
    - (end)
