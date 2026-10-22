# Jaraah

- **Original Wiki Page**: [Transcript:Jaraah](https://runescape.wiki/w/Transcript%3AJaraah)
- **Letter**: `J`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Player:** ¡Hola!
- **Jaraah:** ¿Qué? ¿No ves que estoy ocupado?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Puedes curarme?
    - ((Before the destruction of Duel Arena:))
      - **Jaraah:** Está bien. Esto te hará más daño a ti que a mí.
      - (continue)
    - ((After the destruction of Duel Arena:))
      - **Player:** ¿Puedes curarme?
      - **Jaraah:** Estas instalaciones no son ideales para un hospital, pero puedo hacer que funcionen.
      - **Jaraah:** Está bien. Esto te dolerá más a ti que a mí.
      - (continue)
    - *Si está en plena salud:*
      - **Jaraah:** ¡Me pareces saludable!
      - (previous)
    - *Si no está en plena salud:*
      - Te sientes un poco mejor.
      - (previous)
  - [Choice]: cond=Historical, before the destruction of Duel Arena|Debes ver algunas cosas espantosas.
    - **Jaraah:** Es un negocio espantoso y, con las herramientas que me dan, se vuelve más espantoso antes de mejorar.
  - [Choice]: cond=After the destruction of Duel Arena|Debes haber visto algunas cosas espantosas.
    - **Player:** Debes haber visto algunas cosas espantosas.
    - **Jaraah:** ¿En mi tiempo en Duel Arena? Ciertamente, fue un asunto espantoso.
    - **Jaraah:** Pero ahora que la arena se ha hundido nuevamente en el desierto, las cosas están un poco mejor.
  - [Choice]: ¿Por qué te llaman 'El Carnicero'?
    - ((Before the destruction of Duel Arena:))
      - **Jaraah:** ¿'El Carnicero'?
      - **Jaraah:** ¡Ja!
      - **Jaraah:** ¿Quieres que te lo demuestre?
      - **Player:** Er... Lo dejaré pasar, gracias.
    - ((After the destruction of Duel Arena:))
      - **Player:** ¿Por qué te llaman 'El Carnicero'?
      - **Jaraah:** ¿'El Carnicero'?
      - **Jaraah:** ¡Ja!
      - **Jaraah:** ¿Quieres que te lo demuestre?
      - **Player:** Er... Lo dejaré pasar, gracias.

### Heal

- (above|heal)

### Treasure Trails

- **Jaraah:** ¡Aquí! ¡Ahora tengo trabajo que hacer!
- (removes=the old clue scroll (medium))
- ((If the trail continues:))
  - (receives=a new clue scroll (medium))
  - [¡Jaraah te ha dado otro pergamino de pistas!]
- ((If the trail ends:))
  - (receives=reward casket (medium))
  - [¡Has encontrado un ataúd!]
