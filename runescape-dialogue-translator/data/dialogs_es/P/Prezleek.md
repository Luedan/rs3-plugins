# Prezleek

- **Original Wiki Page**: [Transcript:Prezleek](https://runescape.wiki/w/Transcript%3APrezleek)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Spring Fayre

- **Prezleek:** ¡Bienvenido al Bucking Baroo!
  - [Choice]: ¿Qué está pasando aquí?
    - *(Solo en 2017 :)*
      - **Prezleek:** Este es el Bucking Baroo: ¡paga 10 fichas y luego espera por tu vida!
      - (continue)
    - *(Solo en 2018 :)*
      - **Prezleek:** Este es el Bucking Baroo: ¡súbete y luego agárrate para salvar tu vida!
      - (continue)
    - **Player:** ¿Es seguro?
    - **Prezleek:** ¿En serio? ¿Te preguntarás si esto, de todas las cosas que has hecho en Gielinor, es seguro?
    - **Player:** ...¿verdad?
    - **Prezleek:** ...
    - **Prezleek:** Probablemente no.
    - (otro)
  - [Choice]: ¿No te reconozco?
    - **Prezleek:** ¡Qué astuto! Probablemente hayas visto una buena cantidad de mis fantásticas obras de arte aquí y allá.
    - **Player:** Oh, ahora lo recuerdo. ¡Tú haces los cómics divertidos!
    - **Prezleek:** Prefiero las 'obras maestras únicas'.
    - **Player:** ¡Son muy divertidos!
    - **Prezleek:** ...gracias.
    - (otro)
  - [Choice]: ¿En qué tarea de cazador estás actualmente?
    - **Prezleek:** Es aburrido. Quiero Nex.
    - **Player:** Pero ¿qué ab...?
    - **Prezleek:** Nex.
    - **Player:** ¿No es un li...
    - **Prezleek:** Nex.
    - **Player:** ¿Pero cómo...?
    - **Prezleek:** GIMMIE NEX.
    - **Player:** Uf, olvida que pregunté.
    - (otro)
  - [Choice]: Adiós
    - **Prezleek:** ¡Diviértete!

### Manor Farm


#### Durante el tutorial

{{Main|Transcript:Player-owned farm Tutorial}}

#### Después del tutorial


##### Vender animales

- **Prezleek (comerciante de yaks):** Tengo una solicitud especial para [breed]. ¡Especialmente si tiene el rasgo [Trait]!
- **Prezleek (comerciante de yaks):** También busco algunos yaks; de hecho, compraré hasta [número] más mientras esté aquí.
- ((Repetido para cada yak en backpack:))
  - ¿Le gustaría vender [name] por frijoles [número]?
  - [Menu]: ¿Vender [name] por frijoles [número]?
    - [Choice]: Sí.
      - ((Si el player tiene un millón de beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Prezleek (comerciante de yaks):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - (continue)
      - ((Si la transacción le tomara a el player más de un millón de beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - [Menu]: ¿Completar la transacción de todos modos?
          - [Choice]: Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - [Choice]: No.
            - **Prezleek (comerciante de yaks):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((De lo contrario:))
        - (Action: El animal está vendido.)
        - Frijoles [número] agregados a su bolsa de divisas.
        - (continue)
    - [Choice]: No.
      - (end)
- ((Si no se vendieran animales:))
  - **Player:** Déjame comprobar qué animales tengo que coincidan con tu solicitud.
- ((Si se vendieran animales:))
  - ((Si Prezleek aún puede comprar más:))
    - (end)
  - ((Si Prezleek no puede comprar más:))
    - **Prezleek (comerciante de yaks):** He comprado todos los animales que necesito por ahora, ¡nos vemos más tarde!
    - (Action: Prezleek se teletransporta.)

##### Animales de venta rápida

- **Prezleek (comerciante de yaks):** ¿Estás seguro de que quieres que me quede con todos los yaks que tienes? No aceptaré ninguno de tus favoritos.
- [Menu]: ¿Vender todos tus yaks?
  - [Choice]: si
    - ((Con yaks en backpack:))
      - ((Si el player tiene un millón de beans:))
        - ((Se repite para cada animal restante y luego continúa a continuación:))
          - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - **Prezleek (comerciante de yaks):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
                - **Prezleek (comerciante de yaks):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - ((Si se vendieron varios animales:))
                - Has vendido animales [número] por un total de frijoles [número].
            - [Choice]: No.
              - **Prezleek (comerciante de yaks):** No puedes aguantar más frijoles, no puedo comprarte este animal.
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
    - ((Sin yaks en backpack:))
      - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - [Choice]: No
    - (end)
