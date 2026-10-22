# Roberta

- **Original Wiki Page**: [Transcript:Roberta](https://runescape.wiki/w/Transcript%3ARoberta)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- (Condition: Before obtaining On the Origin of Centaurs:)
  - **Roberta:** Oye, ¿puedes ayudarme? Excavé la cueva hacia el sur mientras buscaba artefactos. Contiene un tipo de arcilla raro y precioso, pero carezco de la experiencia y el equipo para extraer la porcelana yo mismo.
  - (continue)
- (Condition: After obtaining On the Origin of Centaurs:)
  - Muchas gracias por ayudarme, ¡eres el mejor! Espero que te lo pases genial leyendo el libro.
  - (continue)
- [Menu]: Elija una opción:|anchor=Roberta-options
  - [Choice]: What will you give me in exchange?|cond=Antes de obtener Sobre el origen de los centauros:
    - **Roberta:** Encontré un libro en la cueva cuando lo descubrí por primera vez. Lo cambio por 100 de porcelana, blanda o seca.
    - [pic=Sobre el origen de los centauros detail.png]
    - (initial|Roberta-options)
  - [Choice]: Háblame de esta cueva.
    - **Roberta:** Dos corrientes de agua fluyen a través de la cueva, que es rica en depósitos de arcilla porcelánica. La arcilla más cercana al agua es más blanda.
    - **Roberta:** El agua de Everlight tiene propiedades minerales especiales que con el tiempo han hecho que la arcilla sea más fuerte, tanto para extraer como para trabajar.
    - **Roberta:** La porcelana puede producir cerámica fuerte y hermosa, pero requiere una mano experta y un pico fuerte para extraerla.
    - (initial|Roberta-options)
  - [Choice]: Look at all this porcelain clay I've mined!|cond=Con arcilla porcelánica en backpack:
    - (Condition: With less than 100 porcelain clay in backpack before obtaining On the Origin of Centaurs:)
      - **Roberta:** ¡Guau! ¡[número] es impresionante! ¿Puedes traerme 100 de arcilla porcelana? Te daré mi libro a cambio.
      - (initial|Roberta-options)
    - (Condition: With at least 100 porcelain clay in backpack before obtaining On the Origin of Centaurs:)
      - **Roberta:** ¡Guau! ¡[número] es impresionante!
      - **Roberta:** Puedes quedarte con el libro que encontré a cambio de 100 arcilla de porcelana.
      - (Condition: Without one free backpack space:)
        - **Roberta:** Sin embargo, necesitas un espacio libre en tu backpack para poder darte el libro.
      - (Condition: With one free backpack space:)
        - (removes=100 porcelain clay) (receives=On the Origin of Centaurs)
        - [pic=Sobre el origen de los centauros detail.png]
        - (initial|Roberta-options)
    - (Condition: After obtaining On the Origin of Centaurs:)
      - **Roberta:** ¡La arcilla para porcelana [número] es impresionante! Aunque no tengo nada más que darte a cambio.
      - (initial|Roberta-options)
  - [Choice]: Adiós.
    - (end)

### Attempting to enter the Everlight porcelain clay mine without level 102 Mining

- **Roberta:** Tendrás que ser un minero particularmente competente para recolectar arcilla de porcelana en esa cueva.
