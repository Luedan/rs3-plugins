# Steven (salamander commander)

- **Original Wiki Page**: [Transcript:Steven (salamander commander)](https://runescape.wiki/w/Transcript%3ASteven%20%28salamander%20commander%29)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Sell Animals

- **Steven (comandante salamandra):** Tengo un pedido especial para [breed]. ¡Especialmente si tiene el rasgo [Trait]!
- **Steven (comandante de salamandras):** También busco algunas salamandras; de hecho, compraré hasta [número] más mientras esté aquí.
- ((Repetido para cada salamandra en backpack:))
  - {{Transcript missing}}

### Quick-sell animals

- **Steven (comandante de salamandras):** ¿Estás seguro de que quieres que me lleve todas las Salamandras que tienes? No aceptaré ninguno de tus favoritos.
- **¿VENDER TODAS TUS SALAMANDRAS?**
  - si
    - ((Con salamandras en backpack:))
      - ((Si el player tiene un millón de beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Steven (comandante de salamandra):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - No tienes animales para vender. ¡Cero animales, cero frijoles!
      - ((Si la transacción le tomara a el player más de un millón de beans:))
        - {{Transcript missing}}
      - ((De lo contrario:))
        - (Action: Los animales se venden.)
        - ((Se repite para cada animal vendido y luego continúa a continuación:))
          - Frijoles [número] agregados a su bolsa de divisas.
        - ((Si se vendieron varios animales:))
          - Has vendido animales [número] por un total de frijoles [número].
    - ((Sin salamandras en backpack:))
      - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - No
    - (end)
