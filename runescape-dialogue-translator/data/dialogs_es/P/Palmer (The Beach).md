# Palmer (The Beach)

- **Original Wiki Page**: [Transcript:Palmer (The Beach)](https://runescape.wiki/w/Transcript%3APalmer%20%28The%20Beach%29)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Normally

- [Menu]: Selecciona una opción
  - [Choice]: cond=Only before asking anything else:|¿Qué está pasando aquí?
    - **Palmer:** Estos cocoteros tienen productos fantásticos que vale la pena cultivar.
    - [La cosecha de los cocoteros te brinda experiencia agrícola. Puedes ganar experiencia adicional entregando los cocos al cocotero.]
    - (previous)
  - [Choice]: ¿Cómo van las cosas?
    - (Condition: Only if not answered like this the last time:)
      - **Palmer:** Mi adorable manojo de cocos me mantiene feliz, aunque preferiría que esa gran criatura no siguiera saliendo del cráter y asustándome.
      - **Palmer:** Pensé que mudándonos aquí nos alejaríamos de esto. ¡Pero resulta que aquí es donde vive!
      - (previous)
    - (Condition: Only if answered like above this the last time:)
      - **Palmer:** Estos cocoteros tienen productos fantásticos que vale la pena cultivar.
      - [La cosecha de los cocoteros te brinda experiencia agrícola. Puedes ganar experiencia adicional entregando los cocos al cocotero.]
      - (previous)
  - [Choice]: cond=Only after asking something else:|Adiós.
    - **Palmer:** Disfruta tu tiempo en la playa.

### Before 2026


#### Normalmente

- [Menu]: Selecciona una opción
  - [Choice]: cond=Only before asking anything else:|¿Qué está pasando aquí?
    - **Palmer:** Estos cocoteros tienen productos fantásticos que vale la pena cultivar.
    - [La cosecha de los cocoteros te brinda experiencia agrícola. Puedes ganar experiencia adicional entregando los cocos al cocotero.]
    - (previous)
    - (Condition: Only if not answered like this the last time:)
      - **Palmer:** Mi adorable manojo de cocos me mantiene feliz, aunque preferiría que esa gran criatura no siguiera saliendo del cráter y asustándome.
      - **Palmer:** ¿Qué es esa cosa? Reyna dijo que tiene algo que ver con la energía del área y que está ligado a aquí, pero no estoy seguro de que eso me haga sentir mejor.
      - (previous)
    - (Condition: Only if answered like above this the last time:)
      - **Palmer:** Estos cocoteros tienen productos fantásticos que vale la pena cultivar.
      - [La cosecha de los cocoteros te brinda experiencia agrícola. Puedes ganar experiencia adicional entregando los cocos al cocotero.]
      - (previous)
  - [Choice]: cond=Only after asking something else:|Adiós.
    - **Palmer:** Disfruta tu tiempo en la playa.

#### Con el pergamino de pistas Sandy

- **Palmer:** ¡Oh, un extraño te dejó esto!
- (Condition: Receiving a scroll box:)
  - (receives=Sandy Scroll box)
  - [scrollbox].}}
- (Condition: Receiving caskets:)
  - (Condition: Without free space in backpack:)
    - Necesitas 1 espacio libre en tu backpack para recibir tus cofres de pistas.
  - (Condition: With free space in backpack:)
    - (removes=Sandy Clue Scroll)
    - (receives=Sandy Casket and its red version)
    - [¡Te entregan un ataúd!]
