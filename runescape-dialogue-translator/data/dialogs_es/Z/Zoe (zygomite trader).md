# Zoe (zygomite trader)

- **Original Wiki Page**: [Transcript:Zoe (zygomite trader)](https://runescape.wiki/w/Transcript%3AZoe%20%28zygomite%20trader%29)
- **Letter**: `Z`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Sell Animals

- **Zoe (comerciante de zigomitas):** Tengo una solicitud especial para [breed]. ¡Especialmente si tiene el rasgo [Trait]!
- **Zoe (comerciante de zygomitas):** También busco algunos zygomitas; de hecho, compraré hasta [número] más mientras esté aquí.
- ((Repetido para cada cigomita en backpack:))
  - ¿Le gustaría vender [name] por frijoles [número]?
  - [Menu]: ¿Vender [name] por frijoles [número]?
    - [Choice]: Sí.
      - ((Si el player tiene un millón de beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Zoe (comerciante de zigomitas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - (continue)
      - ((Si la transacción le tomara a el player más de un millón de beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - [Menu]: ¿Completar la transacción de todos modos?
          - [Choice]: Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - [Choice]: No.
            - **Zoe (comerciante de zigomitas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((De lo contrario:))
        - (Action: El animal está vendido.)
        - Frijoles [número] agregados a su bolsa de divisas.
        - (continue)
    - [Choice]: No.
      - (end)
- ((Si no se vendieran animales:))
  - **Player:** Déjame comprobar qué animales tengo que coincidan con tu solicitud.
- ((Si se vendieran animales:))
  - ((Si Zoe aún puede comprar más:))
    - (end)
  - ((Si Zoe no puede comprar más:))
    - **Zoe (comerciante de zigomitas):** He comprado todos los animales que necesito por ahora, ¡nos vemos más tarde!
    - (Action: Zoe se teletransporta.)

### Quick-sell animals

- **Zoe (comerciante de zygomites):** ¿Estás seguro de que quieres que me lleve todos los zygomites que tienes? No aceptaré ninguno de tus favoritos.
- [Menu]: ¿Vender todos tus cigomitas?
  - [Choice]: si
    - ((Con cigomitas en backpack:))
      - ((Si el player tiene un millón de beans:))
        - ((Se repite para cada animal restante y luego continúa a continuación:))
          - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - **Zoe (comerciante de zigomitas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
                - **Zoe (comerciante de zigomitas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - ((Si se vendieron varios animales:))
                - Has vendido animales [número] por un total de frijoles [número].
            - [Choice]: No.
              - **Zoe (comerciante de zigomitas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
    - ((Sin cigomitas en backpack:))
      - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - [Choice]: No
    - (end)
