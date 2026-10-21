# General Bentnoze

- **Original Wiki Page**: [Transcript:General Bentnoze](https://runescape.wiki/w/Transcript%3AGeneral%20Bentnoze)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Goblin Village


#### Diálogo estándar

{{Transcript|Goblin generals}}

#### Senderos del tesoro


##### Recibiendo la caja del rompecabezas

- **General Bentnoze:** ¡Humano, haz rompecabezas por mí!
- (receives=puzzle box)
- [¡Bentnoze te ha regalado una caja de rompecabezas!]

##### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- **General Bentnoze:** ¡Eso no está bien!

##### Cuando se volvió a hablar con él después de resolver el rompecabezas

- (Condition: Si el rastro continúa:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [¡Bentnoze te ha dado otro pergamino de pistas!]
  - (continue)
- (Condition: Si el sendero termina:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **General Bentnoze:** ¡Gracias, humano!
