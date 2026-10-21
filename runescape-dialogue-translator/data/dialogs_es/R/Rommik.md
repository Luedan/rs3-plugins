# Rommik

- **Original Wiki Page**: [Transcript:Rommik](https://runescape.wiki/w/Transcript%3ARommik)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Rimmington


#### Hablando con él

- **Rommik:** ¿Te gustaría comprar algún equipo Crafting?
- [Menu]: Selecciona una opción
  - [Choice]: Veamos qué tienes entonces.
    - (opens=Rommik's Crafty Supplies)
  - [Choice]: No gracias, tengo todo el equipo de artesanía que necesito.
    - **Player:** No, gracias. Tengo todo el equipo de artesanía que necesito.
    - **Rommik:** Está bien. Que te vaya bien en tus viajes.

#### Senderos del tesoro

- (Condition: Sólo la primera vez:)
  - **Player:** He venido por este sendero del tesoro.
  - **Rommik:** Bastante bien. Responde mi pregunta y podrás continuar.
- (receives=challenge scroll (medium))
- [¡Rommik te ha dado un pergamino de desafío!]

##### Cuando hablé de nuevo

- **Rommik:** Ingrese la respuesta a la pregunta.
- Ingrese la cantidad:<br>[Input field]
- (Condition: Cuando se le da la respuesta incorrecta:)
  - **Rommik:** ¿Estás seguro de eso?
- (Condition: Cuando se le da la respuesta correcta:)
  - (removes=the clue scroll (medium) y desplazamiento de desafío (medio))}
  - ((Si el rastro continúa:))
    - (receives=a new clue scroll (medium))
    - [¡Rommik te ha dado otro pergamino de pistas!]
  - ((Si el sendero termina:))
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
  - **Rommik:** ¡Adelante!
