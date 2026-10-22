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
- ((Repeated for each malletops in backpack:))
  - ((If the animal isn't favourited:))
    - ¿Le gustaría vender [name] por frijoles [número]?
    - (continue)
  - ((If the animal is favourited:))
    - ¿Le gustaría vender [name] por frijoles [número]? {{Colour|#AE0000|¡Tienes a Etta marcada como favorita!}}
    - (continue)
  - '''¿VENDER [NAME] POR FRIJOLES [número]?
    - Sí.
      - ((If the player has a million beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Moia (maestro de mazas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((If transaction would take the player over a million beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - **¿COMPLETAR LA TRANSACCIÓN DE TODOS MODOS?**
          - Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - No.
            - **Moia (maestro de mazas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
            - (continue)
      - ((Otherwise:))
        - {{Transcript missing}}
    - No.
      - (continue)

#### Animales de venta rápida

- **Moia (maestro de malletops):** ¿Estás seguro de que quieres que me lleve todos los Malletops que tienes? No aceptaré ninguno de tus favoritos.
- **¿VENDER TODAS TUS MALLETTOPS?**
  - si
    - ((With non-favourited malletops in backpack:))
      - ((If the player has a million beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Moia (maestro de mazas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - ((Without favourited malletops in backpack:))
          - No tienes animales para vender. ¡Cero animales, cero frijoles!
          - ((Repeated in a pop-up:))
            - No tienes animales para vender. ¡Cero animales, cero frijoles!
        - ((With favourited malletops in backpack:))
          - No tienes animales para vender. Los compradores no comprarán animales favoritos.
          - ((Repeated in a pop-up:))
            - No tienes animales para vender. Los compradores no comprarán animales favoritos.
      - ((If transaction would take the player over a million beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - **¿COMPLETAR LA TRANSACCIÓN DE TODOS MODOS?**
          - Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - No.
            - **Moia (maestro de mazas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
            - ((With favourited malletops in backpack:))
              - No tienes animales para vender. Los compradores no comprarán animales favoritos.
              - ((Repeated in a pop-up:))
                - No tienes animales para vender. Los compradores no comprarán animales favoritos
            - ((Without favourited malletops in backpack:))
              - No tienes animales para vender. ¡Cero animales, cero frijoles!
              - ((Repeated in a pop-up:))
                - No tienes animales para vender. ¡Cero animales, cero frijoles!
      - ((Otherwise:))
        - {{Transcript missing}}
    - ((Without non-favourited malletops in backpack:))
      - ((With favourited malletops in backpack:))
        - No tienes animales para vender. Los compradores no comprarán animales favoritos.
        - ((Repeated in a pop-up:))
          - No tienes animales para vender. Los compradores no comprarán animales favoritos
      - ((Without favourited malletops in backpack:))
        - No tienes animales para vender. ¡Cero animales, cero frijoles!
        - ((Repeated in a pop-up:))
          - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - No
    - (end)
