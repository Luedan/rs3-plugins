# Valerio

- **Original Wiki Page**: [Transcript:Valerio](https://runescape.wiki/w/Transcript%3AValerio)
- **Letter**: `V`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before One Piercing Note

- **Valerio:** ¡Saludos viajero!
- [Menu]: Selecciona una opción
  - [Choice]: ¿Sobre qué cantabas?
    - **Player:** ¿Sobre qué cantabas?
    - **Valerio:** Ah... es una canción sobre alguien que conocí hace mucho tiempo.
    - (otro)
  - [Choice]: ¿Qué estás haciendo en la abadía?
    - **Player:** ¿Qué haces en la abadía?
    - **Valerio:** Una de las hermanas aquí, la hermana Anna, falleció recientemente. La conocí antes de que se uniera a la abadía, así que he venido a presentarle mis respetos.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Cómo se enteró de la muerte de la hermana Anna?
        - **Player:** ¿Cómo se enteró de la muerte de la hermana Anna?
        - **Valerio:** Tengo el oído pegado al suelo. Ni siquiera una orden religiosa está completamente aislada del mundo.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Sobre qué cantabas?
            - (arriba)
          - [Choice]: Adiós.
            - (abajo)
      - [Choice]: Adiós.
        - (abajo)
  - [Choice]: Adiós.
    - **Player:** Adiós.

### After One Piercing Note

- **Valerio:** Hola de nuevo, aventurero.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Cómo estás?
    - **Player:** ¿Cómo estás?
    - *(Si el player mintió sobre The Killer:)*
      - **Valerio:** Todavía no puedo creer que un demonio haya matado a Anna. Sabía que todavía había demonios en el Wilderness, pero la idea de que uno atacara en un lugar como este...
    - *(Si el player dijera la verdad :)*
      - **Valerio:** Todavía no puedo creer que Anna pudiera hacer esas cosas. Crees que conoces a alguien... pero supongo que la gente puede cambiar mucho con el tiempo.
    - (otro)
  - [Choice]: ¿Hay algo en lo que pueda ayudarte?
    - **Player:** ¿Hay algo en lo que pueda ayudarte?
    - **Valerio:** Gracias, aventurero, pero no. Ya has hecho suficiente.
    - (otro)
  - [Choice]: Adiós.
    - **Player:** Adiós.

### Treasure Trails


#### Recibiendo el pergamino de desafío

- (Condition: Only the first time:)
  - **Valerio:** ¿Estás aquí por el rastro del tesoro?
  - **Player:** ¡Sí, lo soy!
  - **Valerio:** Aquí está tu desafío. ¡Buena suerte!
- (receives=challenge gem (medium))
- [¡Valerio te ha dado un pergamino de desafío!]

#### Cuando hablé de nuevo

- **Valerio:** Ingrese la respuesta a la pregunta.
- Ingrese la cantidad:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Valerio:** ¡No del todo! Ve a mirar de nuevo.
- (Condition: When given the correct answer:)
  - (removes=the clue scroll (medium) y gema de desafío (mediano))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [¡Valerio te ha dado otro pergamino de pistas!]
    - (continue)
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
    - (continue)
  - **Valerio:** ¡Correcto!
