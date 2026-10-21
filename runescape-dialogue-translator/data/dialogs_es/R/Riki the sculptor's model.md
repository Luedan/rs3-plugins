# Riki the sculptor's model

- **Original Wiki Page**: [Transcript:Riki the sculptor's model](https://runescape.wiki/w/Transcript%3ARiki%20the%20sculptor%27s%20model)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before The Giant Dwarf

- **Player:** Hola, ¿qué haces aquí?
- **Riki the sculptor's model:** Yo... soy el asociado del escultor.
- **Player:** ¿Su socio? ¿Qué significa eso?
- **Riki the sculptor's model:** Yo... soy el asociado del escultor.
- **Player:** ¿Vas a decir algo significativo?
- **Riki the sculptor's model:** I...-
- **Player:** No, aparentemente no.

### After The Giant Dwarf

- **Player:** ¡Me alegro de no tener que hablar más contigo!
- **Riki the sculptor's model:** Hrm.

### Treasure Trails


#### Recibiendo la caja del rompecabezas

- **Riki the sculptor's model:** Oh, tengo un rompecabezas que debes resolver.
- (receives=puzzle box)
- [¡Riki te ha regalado una caja de rompecabezas!]

#### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- **Riki the sculptor's model:** Eso no está bien, sigue intentándolo.

#### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- (Condition: Si el rastro continúa:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [¡Riki te ha dado otro pergamino de pistas!]
  - (continue)
- (Condition: Si el sendero termina:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Riki the sculptor's model:** Oh, lo lograste. Eso es una sorpresa.
