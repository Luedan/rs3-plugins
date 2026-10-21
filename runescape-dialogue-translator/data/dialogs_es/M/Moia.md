# Moia

- **Original Wiki Page**: [Transcript:Moia](https://runescape.wiki/w/Transcript%3AMoia)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Battle of Lumbridge

- (ver|Batalla de Lumbridge)

### [[Tuska Comes]]

- (ver|Tuska viene)

### Anachronia Dinosaur Farm


#### Vender animales

- **Moia (maestro de malletops):** Tengo una solicitud especial para [Breed]. ¡Especialmente si tienen el rasgo [Trait]!
- **Moia (maestro de malletops):** También busco algunos Malletops, de hecho compraré hasta [número] más mientras esté aquí.
- ((Repetido para cada mazo en backpack:))
  - ((Si el animal no es favorito:))
    - ¿Le gustaría vender [name] por frijoles [número]?
    - (continue)
  - ((Si el animal es favorito:))
    - ¿Le gustaría vender [name] por frijoles [número]? {{Colour|#AE0000|¡Tienes a Etta marcada como favorita!}}
    - (continue)
  - '''¿VENDER [NAME] POR FRIJOLES [número]?
    - Sí.
      - ((Si el player tiene un millón de beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Moia (maestro de mazas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((Si la transacción le tomara a el player más de un millón de beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - **¿COMPLETAR LA TRANSACCIÓN DE TODOS MODOS?**
          - Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - No.
            - **Moia (maestro de mazas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
            - (continue)
      - ((De lo contrario:))
        - {{Transcript missing}}
    - No.
      - (continue)

#### Animales de venta rápida

- **Moia (maestro de malletops):** ¿Estás seguro de que quieres que me lleve todos los Malletops que tienes? No aceptaré ninguno de tus favoritos.
- **¿VENDER TODAS TUS MALLETTOPS?**
  - si
    - ((Con mazos no favoritos en backpack:))
      - ((Si el player tiene un millón de beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Moia (maestro de mazas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - ((Sin tapas de mazo favoritas en backpack:))
          - No tienes animales para vender. ¡Cero animales, cero frijoles!
          - ((Repetido en una ventana emergente:))
            - No tienes animales para vender. ¡Cero animales, cero frijoles!
        - ((Con mazos favoritos en backpack:))
          - No tienes animales para vender. Los compradores no comprarán animales favoritos.
          - ((Repetido en una ventana emergente:))
            - No tienes animales para vender. Los compradores no comprarán animales favoritos.
      - ((Si la transacción le tomara a el player más de un millón de beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - **¿COMPLETAR LA TRANSACCIÓN DE TODOS MODOS?**
          - Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - No.
            - **Moia (maestro de mazas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
            - ((Con mazos favoritos en backpack:))
              - No tienes animales para vender. Los compradores no comprarán animales favoritos.
              - ((Repetido en una ventana emergente:))
                - No tienes animales para vender. Los compradores no comprarán animales favoritos
            - ((Sin tapas de mazo favoritas en backpack:))
              - No tienes animales para vender. ¡Cero animales, cero frijoles!
              - ((Repetido en una ventana emergente:))
                - No tienes animales para vender. ¡Cero animales, cero frijoles!
      - ((De lo contrario:))
        - {{Transcript missing}}
    - ((Sin mazos no favoritos en backpack:))
      - ((Con mazos favoritos en backpack:))
        - No tienes animales para vender. Los compradores no comprarán animales favoritos.
        - ((Repetido en una ventana emergente:))
          - No tienes animales para vender. Los compradores no comprarán animales favoritos
      - ((Sin tapas de mazo favoritas en backpack:))
        - No tienes animales para vender. ¡Cero animales, cero frijoles!
        - ((Repetido en una ventana emergente:))
          - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - No
    - (end)
