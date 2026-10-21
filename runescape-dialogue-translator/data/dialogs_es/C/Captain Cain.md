# Captain Cain

- **Original Wiki Page**: [Transcript:Captain Cain](https://runescape.wiki/w/Transcript%3ACaptain%20Cain)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|Missing wave resetting if you're not at wave 1.}}

### Barbarian Assault


#### Antes de aceptar registrarse


##### Hablando con él

- **Player:** Hola. ¿Qué es este lugar?
- **Captain Cain:** ¡Por qué desgraciado hijo de un duende maloliente y verrugoso de nariz grande! ¿Cómo te atreves a hablarle así a un oficial al mando?
- **Player:** Yo...err... ¿Qué?
- **Captain Cain:** ¡Manténgase derecho! ¡Pecho hacia afuera, hombros hacia atrás!
- **Player:** Está bien, está bien.
- **Captain Cain:** ¡Te dirigirás a mí como capitán!
- **Player:** Sí... ¡sí, capitán!
- **Captain Cain:** Mejor. Ahora bien, ¿cuál es una excusa patética y de mala vida para que un ser humano husmee en mi estadio?
- **Player:** Explorando, capitán. ¡Parecía una oportunidad de combate, señor!
- **Captain Cain:** ¿Y crees que tienes lo necesario para asumir la Penitencia? No hay posibilidad.
- **Player:** Con todo respeto capitán, no entiendo qué es este lugar.
- **Captain Cain:** Realmente eres un inútil, ¿no? ¡Muy bien, aprovecha esto porque no soporto idiotas fácilmente! Esta es la arena de Barbarian Assault. ¿Quieres registrarte con nosotros?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Señor, sí señor!
    - **Player:** ¡Señor, sí señor!
    - **Captain Cain:** Entonces escucha atentamente.
    - (opens=Barbarian Assault tutorial)
  - [Choice]: No, suena aburrido.
    - (below|boring)

##### Opción de tutorial

- ¡Será mejor que te presentes primero!

#### Después de aceptar registrarse


##### Hablando con él

- **Player:** Hola... Quiero decir, ¡Player informando, señor!
- **Captain Cain:** ¡Endereza eso cuando me hables! ¿Quieres mi ayuda?
  - [Menu]: Seleccione una opción|anclaje=init
    - [Choice]: ¡Señor! ¿Podemos hacer algo de entrenamiento?
      - **Player:** ¡Señor! ¿Podemos hacer algo de entrenamiento?
      - **Captain Cain:** ¿Otra vez? Muy bien. ¡Escuche atentamente esta vez!
      - (opens=Barbarian Assault tutorial)
    - [Choice]: ¡Señor! ¿Puedo cambiar mi ola actual?
      - **Player:** ¡Señor! ¿Puedo cambiar mi ola actual?
        - (Condition: Si el player se encuentra actualmente en la Onda 1:)
          - **Captain Cain:** ¡Solo puedes cambiarlo a la onda 1 y ya estás en la onda 1!
          - **Player:** Ah, ya veo. Gracias de todos modos.
          - (previous)
        - (Condition: Si el player no está en la Onda 1:)
          - {{transcript missing}}
        - (Condition: Si el player no ha terminado el tutorial:)
          - **Captain Cain:** ¿Qué? ¡Primero termina tu entrenamiento, soldado!
          - (initial|init)
    - [Choice]: No, suena aburrido.{{anchor|boring}}
      - **Player:** No, suena aburrido.
      - **Captain Cain:** ¿Aburrido? ¡No llegarás a ninguna parte con ese tipo de actitud! ¡Déjame caer y dame diez!
      - [Menu]: Selecciona una opción
        - [Choice]: Quizás la próxima vez. Necesito ir a lavarme el pelo.
          - **Player:** Quizás la próxima vez tenga que ir a lavarme el pelo.
          - **Captain Cain:** ¡Harás lo que te diga!
          - **Player:** Arrrghhh. ¡Está bien, está bien!
          - (Action: el player realiza cinco flexiones.)
        - [Choice]: ¡Señor, sí señor!
          - **Player:** ¡Señor, sí señor!
          - **Captain Cain:** Es bueno ver que has aprendido algo de respeto. Que sean cinco.
          - (Action: el player realiza cinco flexiones.)
          - **Player:** ¡Sí señor!
        - [Choice]: Pero ya lo hice...
          - **Player:** ¡Pero ya lo hice!
          - **Captain Cain:** ¿Lo hiciste?
          - **Player:** ¡Señor, sí señor!
          - **Captain Cain:** No confío en ti en lo más mínimo. ¡Haz lo que te digo!
          - (Action: el player realiza cinco flexiones.)

##### Opción de tutorial

- (opens=Barbarian Assault tutorial)

### NPC Contact

- (ver|NPC Contact#Captain Cain)
