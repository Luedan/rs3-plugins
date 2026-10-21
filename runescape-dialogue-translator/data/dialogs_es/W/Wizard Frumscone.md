# Wizard Frumscone

- **Original Wiki Page**: [Transcript:Wizard Frumscone](https://runescape.wiki/w/Transcript%3AWizard%20Frumscone)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Wizard Frumscone:** ¿Te gustan mis Zombies mágicos? Siéntete libre de matarlos, ¡hay muchos más de donde vinieron!
- *Si el player ha completado Swan Song:*
  - **Player:** Hablé con el nigromante como sugeriste...
  - **Wizard Frumscone:** Por favor, no hablemos de eso. Distentor y Zavistic se enfadarían mucho si descubrieran que te he enviado con un nigromante.
  - **Player:** Ok, es justo.

### Attempting to open the gate

- **Wizard Frumscone:** No puedes atacar a los Zombies en la habitación, mis Zombies son solo para practicar magia y deben ser atacados desde el otro lado de la cerca.

### Treasure Trails


#### Recibiendo la caja del rompecabezas

- **Wizard Frumscone:** Oh, estarás aquí para esto, ¿verdad?
- (receives=puzzle box)
- [¡Wizard Frumscone te ha regalado una caja de rompecabezas!]

#### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- **Wizard Frumscone:** Esa no es la respuesta que estaba buscando. Por favor, resuelve el rompecabezas primero.

#### Cuando se le habla con el rompecabezas resuelto

- (Condition: Si el rastro continúa:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [¡Wizard Frumscone te ha dado otro pergamino de pistas!]
  - (continue)
- (Condition: Si el sendero termina:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Wizard Frumscone:** ¡Maravilloso! ¡Ahí tienes!
