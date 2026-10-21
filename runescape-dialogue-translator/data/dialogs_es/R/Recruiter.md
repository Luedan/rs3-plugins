# Recruiter

- **Original Wiki Page**: [Transcript:Recruiter](https://runescape.wiki/w/Transcript%3ARecruiter)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Plague's End

- **Recruiter:** ¡Ciudadanos de West Ardougne! ¿Quién se unirá al Ejército Real de Ardougne? Es una causa muy noble. ¡Lucha junto al rey Tyras en una cruzada en las tierras oscuras del oeste!
- **Hombre (#1):** ¡Portador de plaga!
- **Hombre (#2):** ¡El rey Tyras es escoria!
- **Recruiter:** ¡Tyras será informado de estas palabras de traición!
- (continue|tomatoes)

### After Plague's End

- **Recruiter:** ¡Ciudadanos de West Ardougne! ¿Quién se unirá al Ejército Real de Ardougne? Es una causa muy noble. ¡Ponte junto al Rey Thoros, listo para defender nuestra tierra de nuevas amenazas!
- **Hombre (#1):** ¡Mentiroso!
- **Hombre (#2):** ¡Thoros es igual de malo!
- **Recruiter:** ¡El rey Thoros será informado de estas palabras de traición!
- {{anchor|tomatoes}}(Acción: Dos hombres cercanos le arrojan tomates al reclutador).
- sombra=si
- *(Si el logro Revolución Roja no se ha completado:)*
  - sombra=si

### Treasure Trails

- (Condition: Sólo la primera vez:)
  - **Recruiter:** ¡Luce animado! Veamos si tienes lo necesario para responder esta pregunta.
  - **Player:** ¿Qué pregunta?
  - **Recruiter:** El de este pergamino.
- (receives=challenge scroll (medium))
- [¡El reclutador te ha dado un pergamino de desafío!]

##### Cuando hablé de nuevo

- **Recruiter:** Ingrese la respuesta a la pregunta.
- Ingrese la cantidad:<br>[Input field]
- (Condition: Cuando se le da la respuesta incorrecta:)
  - **Recruiter:** ¡Ni siquiera cerca!
- (Condition: Cuando se le da la respuesta correcta:)
  - (removes=the clue scroll (medium) y desplazamiento de desafío (medio))
  - (Condition: Si el rastro continúa:)
    - (receives=a new clue scroll (medium))
    - [¡El reclutador te ha dado otro pergamino de pistas!]
  - (Condition: Si el sendero termina:)
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
  - **Recruiter:** ¡Acertado!
