# Henrietta (chicken chaser)

- **Original Wiki Page**: [Transcript:Henrietta (chicken chaser)](https://runescape.wiki/w/Transcript%3AHenrietta%20%28chicken%20chaser%29)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Sell Animals

- **Henrietta (cazapollos):** Tengo un pedido especial para [breed]. ¡Especialmente si tiene el rasgo [Trait]!
- **Henrietta (cazadora de pollos):** Compraré hasta [número] pollos más.
- ((Repetido para cada pollo en backpack:))
  - ¿Le gustaría vender [name] por frijoles [número]?
  - [Menu]: ¿Vender [name] por frijoles [número]?
    - [Choice]: Sí.
      - ((Si el player tiene un millón de beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Henrietta (caza gallinas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - (continue)
      - ((Si la transacción le tomara a el player más de un millón de beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - [Menu]: ¿Completar la transacción de todos modos?
          - [Choice]: Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - [Choice]: No.
            - **Henrietta (caza gallinas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((De lo contrario:))
        - (Action: El animal está vendido.)
        - Frijoles [número] agregados a su bolsa de divisas.
        - (continue)
    - [Choice]: No.
      - (end)
- ((Si no se vendieran animales:))
  - **Player:** Déjame comprobar qué animales tengo que coincidan con tu solicitud.
- ((Si se vendieran animales:))
  - ((Si Henrietta aún puede comprar más:))
    - (end)
  - ((Si Henrietta no puede comprar más:))
    - **Henrietta (caza gallinas):** ¡He comprado suficientes animales para hoy!
    - (Action: Henrietta se teletransporta.)

### Quick-sell animals

- **Henrietta (caza gallinas):** ¿Estás segura de que quieres que me lleve todas las gallinas que tienes? No aceptaré ninguno de tus favoritos.
- [Menu]: ¿Vender todas tus gallinas?
  - [Choice]: si
    - ((Con gallinas en backpack:))
      - ((Si el player tiene un millón de beans:))
        - ((Se repite para cada animal restante y luego continúa a continuación:))
          - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - **Henrietta (caza gallinas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
                - **Henrietta (caza gallinas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - ((Si se vendieron varios animales:))
                - Has vendido animales [número] por un total de frijoles [número].
            - [Choice]: No.
              - **Henrietta (caza gallinas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
    - ((Sin gallinas en backpack:))
      - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - [Choice]: No
    - (end)
