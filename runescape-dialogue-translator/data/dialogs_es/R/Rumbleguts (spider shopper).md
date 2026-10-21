# Rumbleguts (spider shopper)

- **Original Wiki Page**: [Transcript:Rumbleguts (spider shopper)](https://runescape.wiki/w/Transcript%3ARumbleguts%20%28spider%20shopper%29)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Sell Animals

- **Rumbleguts (comprador de arañas):** Tengo una solicitud especial para [breed]. ¡Especialmente si tiene el rasgo [Trait]!
- **Rumbleguts (comprador de arañas):** También busco algunas arañas; de hecho, compraré hasta [número] más mientras esté aquí.
- ((Repetido para cada araña en backpack:))
  - ¿Le gustaría vender [name] por frijoles [número]?
  - [Menu]: ¿Vender [name] por frijoles [número]?
    - [Choice]: Sí.
      - ((Si el player tiene un millón de beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Rumbleguts (comprador de arañas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - (continue)
      - ((Si la transacción le tomara a el player más de un millón de beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - [Menu]: ¿Completar la transacción de todos modos?
          - [Choice]: Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - [Choice]: No.
            - **Rumbleguts (comprador de arañas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((De lo contrario:))
        - (Action: El animal está vendido.)
        - Frijoles [número] agregados a su bolsa de divisas.
        - (continue)
    - [Choice]: No.
      - (end)
- ((Si no se vendieran animales:))
  - **Player:** Déjame comprobar qué animales tengo que coincidan con tu solicitud.
- ((Si se vendieran animales:))
  - ((Si Rumbleguts aún puede comprar más:))
    - (end)
  - ((Si Rumbleguts no puede comprar más:))
    - **Rumbleguts (comprador de arañas):** He comprado todos los animales que necesito por ahora, ¡nos vemos más tarde!
    - (Action: Rumbleguts se teletransporta.)

### Quick-sell animals

- **Rumbleguts (comprador de arañas):** ¿Estás seguro de que quieres que me lleve todas las arañas que tienes? No aceptaré ninguno de tus favoritos.
- [Menu]: ¿Vender todas tus arañas?
  - [Choice]: si
    - ((Con arañas en backpack:))
      - ((Si el player tiene un millón de beans:))
        - ((Se repite para cada animal restante y luego continúa a continuación:))
          - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - **Rumbleguts (comprador de arañas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
                - **Rumbleguts (comprador de arañas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - ((Si se vendieron varios animales:))
                - Has vendido animales [número] por un total de frijoles [número].
            - [Choice]: No.
              - **Rumbleguts (comprador de arañas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
    - ((Sin arañas en backpack:))
      - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - [Choice]: No
    - (end)
