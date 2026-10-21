# Karim

- **Original Wiki Page**: [Transcript:Karim](https://runescape.wiki/w/Transcript%3AKarim)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Al Kharid


#### Hablando con él

- **Karim:** ¿Te gustaría comprar un buen kebab? Sólo un oro.
- [Menu]: Selecciona una opción
  - [Choice]: Creo que lo dejaré pasar.
    - **Player:** Creo que lo dejaré pasar.
  - [Choice]: Sí por favor.
    - **Player:** Sí, por favor.
    - (Condition: Si el player no tiene al menos un espacio backpack libre:)
      - **Player:** No tengo suficiente espacio, lo siento.
    - (Condition: Si el player tiene al menos un espacio backpack libre:)
      - (Condition: Si el player tiene al menos una moneda:)
        - (removes=1 coin) (receives=kebab)
        - Compras un kebab.
      - (Condition: Si el player no tiene coins:)
        - **Player:** Vaya, olvidé traer dinero conmigo.
        - **Karim:** Vuelve cuando tengas algo.
        - No puedes permitirte eso.
  - [Choice]: ¿Qué opinas de Ali Morrisane?
    - **Player:** ¿Qué opinas de Ali Morrisane?
    - **Karim:** No me gusta. Hace todas esas afirmaciones de ser el mejor vendedor del mundo, e incluso tiene algunos matones que contrató para amenazarnos.
    - **Karim:** ¡Uno de ellos vino por aquí y amenazó con cortarme la cabeza si no cooperaba con ellos!
    - **Karim:** También escuché algunos rumores sobre ellos de mi amigo Isma'il en Pollnivneach...
    - **Player:** ¿Qué tipo de rumores?
    - **Karim:** Aparentemente también tiene hombres allí, que también han estado amenazando a la gente.
    - **Karim:** ¡Y se dice que incluso tienen la intención de robarle al mismísimo gobernante de Al Kharid!
    - **Player:** ¿En serio?
    - **Karim:** Eso es lo que he oído. De todos modos, ¿estás seguro de que no te apetece un kebab?
    - [Menu]: Selecciona una opción
      - [Choice]: Creo que lo dejaré pasar.
        - (above|give-it-a-miss)
      - [Choice]: Sí por favor.
        - (above|yes-please)

#### Senderos del tesoro

- (Condition: Sólo la primera vez:)
  - **Karim:** Tengo un pequeño problema que debes resolver.
- (receives=challenge scroll (medium))
- [¡El vendedor te ha dado un pergamino de desafío!]

##### Cuando hablé de nuevo

- **Karim:** Ingresa la respuesta al acertijo.
- Ingrese la cantidad:<br>[Input field]
- (Condition: Cuando se le da la respuesta incorrecta:)
  - **Karim:** No, eso no está bien, piénsalo de nuevo.
- (Condition: Cuando se le da la respuesta correcta:)
  - (removes=the clue scroll (medium) y desplazamiento de desafío (medio))
  - (Condition: Si el rastro continúa:)
    - (receives=a new clue scroll (medium))
    - [¡El vendedor te ha dado otro pergamino de pistas!]
    - (continue)
  - (Condition: Si el sendero termina:)
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
    - (continue)
  - **Karim:** ¡Correcto!
