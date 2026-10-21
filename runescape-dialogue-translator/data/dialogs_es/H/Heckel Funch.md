# Heckel Funch

- **Original Wiki Page**: [Transcript:Heckel Funch](https://runescape.wiki/w/Transcript%3AHeckel%20Funch)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Hola.
- **Heckel Funch:** Buenos días para ti, amigo mío, y además muy bonito. ¿Quieres algo de comida? Tengo de todo tipo. Alcohol también, si eres partidario de beber.
- [Menu]: Selecciona una opción
  - [Choice]: No, gracias.
    - **Player:** No, gracias.
    - **Heckel Funch:** Ahh bueno, todo lo mejor para ti.
  - [Choice]: Echaré un vistazo.
    - **Player:** Echaré un vistazo.
    - **Heckel Funch:** Hay un buen ser humano.
    - (opens=Funch's Fine Groceries)

### Treasure Trails


#### Recibiendo la caja del rompecabezas

- **Heckel Funch:** ¡Por favor, haz rompecabezas para mí, humano!
- (receives=puzzle box)
- [¡Heckel Funch te ha regalado una caja de rompecabezas!]

#### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- **Heckel Funch:** No, me temo que eso está mal.

#### Cuando se le habla con el rompecabezas resuelto

- (Condition: Si el rastro continúa:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [¡Heckel Funch te ha dado otro pergamino de pistas!]
  - (continue)
- (Condition: Si el sendero termina:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Heckel Funch:** ¡Bien hecho, humano!
