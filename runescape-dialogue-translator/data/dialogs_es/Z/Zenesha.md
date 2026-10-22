# Zenesha

- **Original Wiki Page**: [Transcript:Zenesha](https://runescape.wiki/w/Transcript%3AZenesha)
- **Letter**: `Z`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In East Ardougne

- **Zenesha:** ¡Hola! Vendo armaduras de placas. ¿Estás interesado?
- [Menu]: Elige una opción:
  - [Choice]: Lo siento, no estoy interesado.
    - (end)
  - [Choice]: Puede que me interese.
    - (opens=Zenesha's Platebody Shop)

### Treasure Trails


#### Recibiendo la caja del rompecabezas

- **Zenesha:** ¡Tengo un rompecabezas para ti!
- (receives=puzzle box)
- [¡Zenesha te ha regalado una caja de rompecabezas!]

#### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- **Zenesha:** No, ese rompecabezas está arruinado. ¡Intentar otra vez!

#### Cuando se le habla con el rompecabezas resuelto

- (Condition: If the trail continues:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [¡Zenesha te ha dado otro pergamino de pistas!]
  - (continue)
- (Condition: If the trail ends:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Zenesha:** ¡Genial, eso es justo lo que quería!
