# Sarah (The Beach)

- **Original Wiki Page**: [Transcript:Sarah (The Beach)](https://runescape.wiki/w/Transcript%3ASarah%20%28The%20Beach%29)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- [Menu]: Selecciona una opción
  - [Choice]: cond=Only if not asked last:|¿Qué está pasando aquí?
    - **Sarah:** Hemos creado un divertido juego de cocos tímidos. Simplemente recoge algunas bolas e intenta quitar los cocos.
    - **Player:** Parece que algunos cocos están atascados. No sabrías nada sobre eso, ¿verdad?
    - **Sarah:** ¿Qué estás diciendo, cariño? ¿Que no confías en mi pequeño? ¿Cómo te atreves a acusarme de esas cosas?
    - (previous)
  - [Choice]: cond=Only if not asked last:|¿Cómo funciona el coco tímido?
    - **Sarah:** Simplemente recoge algunas bolas e intenta quitar los cocos. Obtienes bolas {{Sic|10}} a la vez para lanzar.
    - (previous)
  - [Choice]: cond=Only if neither "What's going on here?" or this question was asked last:|¿Cómo funciona el anzuelo de un pato?
    - **Sarah:** Simplemente toma una caña e intenta atrapar a los patos. Obtienes {{Sic|10}} a la vez.
    - (previous)
  - [Choice]: ¿Cómo van las cosas?
    - **Sarah:** Lo estoy pasando genial. Se puede saber mucho sobre una persona por los tipos de pelotas que lanza, y eso me parece muy interesante.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué significan las bolas normales?
        - **Sarah:** Ah, la elección del equilibrado. Para aquellos que están felices de fluir con el viento y ser uno con el mundo.
        - (continue)
      - [Choice]: ¿Qué significan las coles?
        - **Sarah:** Coles. Estas personas son tenaces y espontáneas, leales hasta el final y siempre luchan por lo que creen.
        - (continue)
      - [Choice]: ¿Qué significan chinchompas?
        - **Sarah:** Chinchompas, la elección del alma creativa, del artista. Almas bondadosas que a menudo son incomprendidas.
        - (continue)
    - **Sarah:** Aunque no es una ciencia exacta. Todavía estoy solucionando los problemas.
    - (previous)

### Talk to with the Sandy Clue Scroll (historical)

- **Sarah:** ¡Oh, un extraño te dejó esto!
- (Condition: Receiving a scroll box:)
  - (removes=Sandy Clue Scroll) (receives=Sandy Scroll box)
  - [scrollbox].}}
- (Condition: Receiving caskets:)
  - (Condition: Without free backpack space:)
    - Necesitas 1 espacio libre en tu backpack para recibir tus cofres de pistas.
  - (Condition: With free backpack space:)
    - (removes=Sandy Clue Scroll) (receives=Sandy Casket and its red version)
    - [¡Te entregan un ataúd!]
