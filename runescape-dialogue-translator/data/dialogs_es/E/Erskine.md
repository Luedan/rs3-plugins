# Erskine

- **Original Wiki Page**: [Transcript:Erskine](https://runescape.wiki/w/Transcript%3AErskine)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- {{anchor|standard}}**Erskine:** ¿Puedo interesarte en un trabajo? <br>Te pagaré por tu trabajo.
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: Háblame de ti.
    - **Erskine:** Mi nombre es Erskine. Soy un poderoso guerrero de Edgeville destinado a erradicar los horrores de Wilderness.
    - **Erskine:** Aunque descubrí que entrar allí no es lo mío en este momento, así que estoy contratando gente para que haga todo eso por mí bajo mi estandarte.
    - **Erskine:** Si estás interesado en participar en combate tú mismo, estaré encantado de darte un trabajo. Puedo pagarte.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Qué tipo de trabajo ofreces?
        - (below|what-job)
      - [Choice]: ¿Tienes miedo de hacerlo tú mismo?{{anchor|scared}}
        - **Erskine:** Por supuesto que no, hay... a veces tormentas de polvo y tengo alergia. . Ejem... tos, tos.
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: Está bien, me gustaría un trabajo.
            - (below|accept-job)
          - [Choice]: ¿Qué tipo de trabajo ofreces?
            - (below|what-job)
          - [Choice]: Háblame de ti.
            - (above|about-erskine)
          - [Choice]: ¿Entonces eres incapaz de hacer tu propio trabajo?
            - (below|incapable)
          - [Choice]: No gracias.
            - (below|decline-job)
      - [Choice]: ¿Eres incapaz de hacer tu propio trabajo?{{anchor|incapable}}
        - **Erskine:** ¿Qué intentas decir? ¿Que tengo demasiado miedo para entrar al Wilderness por si muero y pierdo mis cosas?
    - **Erskine:** Solo quiero erradicar a los monstruos, así que necesito quedarme aquí y contratar suficiente gente para acelerar el proceso.
    - **Erskine:** Entonces, ¿te gustaría conseguir un trabajo ahora?
        - [Choice]: ¿Qué te gustaría decir?
          - Está bien, me gustaría un trabajo.
            - (below|accept-job)
          - [Choice]: ¿Qué tipo de trabajo ofreces?
            - (below|what-job)
          - [Choice]: Háblame de ti.
            - (above|about-erskine)
          - [Choice]: No gracias.
            - (below|decline-job)
      - [Choice]: Está bien, me gustaría un trabajo.
        - (below|accept-job)
      - [Choice]: No gracias.
        - (below|decline-job)
  - [Choice]: ¿Qué tipo de trabajo ofreces?{{anchor|what-job}}
    - **Erskine:** Estoy contratando gente para matar a los monstruos del norte.
    - **Erskine:** Lo haría yo mismo, pero descubrí que la ceniza y el polvo no son buenos para mí. Ejem, tos, tos.
    - **Erskine:** En lugar de eso, le pago a gente como tú para que mate a los monstruos por mí.
    - **Erskine:** ¡Efectivamente, estoy eliminando cosas peligrosas del Wilderness diciéndoles a todos que se deshagan de ellas una y otra vez!
    - **Erskine:** Puedo ofrecer pagos en efectivo. Alternativamente, me compré algunos libros sobre combate, pero no tenía ganas de aventurarme más allá de la introducción después de leer las advertencias sobre los peligros, así que podrías tener uno como pago.
    - **Erskine:** Por cierto, si ya tienes una tarea de otro lugar para matar criaturas que puedes encontrar en la naturaleza, ven a verme. Complete su tarea y le daré un contrato especial que funcionará en conjunto con ella y le daré una recompensa adicional además.
    - **Erskine:** Entonces, ¿te gustaría conseguir un trabajo ahora?
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Tienes miedo de hacerlo tú mismo?
        - (above|scared)
      - [Choice]: ¿Por qué no lo haces tú mismo?
        - (above|incapable)
      - [Choice]: Está bien, me gustaría un trabajo.
        - (below|accept-job)
      - [Choice]: Háblame de ti.
        - (above|about-erskine)
      - [Choice]: No gracias.
        - (below|decline-job)
  - [Choice]: Vale, me gustaría un trabajo.{{anchor|accept-job}}
    - **Erskine:** Excelente. Echa un vistazo a mi contracts y mira cuál te gustaría hacer.
    - (opens=Slayer Contracts){{anchor|slayer-contracts}}
      - (Condition: Al seleccionar una tarea:)
        - (receives=Slayer contract (Wilderness))
        - [El pergamino sólo puede seguir tu progreso si lo llevas mientras matas. Tráelo de vuelta cuando hayas terminado.]
  - [Choice]: No, gracias.{{anchor|decline-job}}
    - **Erskine:** Está bien, pero vuelve si cambias de opinión. Puedo pagarte por tu trabajo.

### Talk to him when assigned relevant Slayer assignment

- **Erskine:** Veo que tienes una tarea de Slayer. Te pagaré extra si aceptas un contrato para realizar tu tarea en Wilderness.
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Qué estás ofreciendo?
    - **Erskine:** También obtendrás una bonificación del 20 % en la XP Slayer obtenida al matar monstruos, un 20 % adicional de XP Slayer cuando uses la calavera demoníaca o en tu inventario dentro de Wilderness.
    - **Erskine:** Además, puedes elegir entre XP de combate [número] o [número] coins.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Está bien, lo aceptaré.
        - (below|special-slayer-contracts)
      - [Choice]: ¿Puedo tener un contrato diferente en su lugar?
        - (above|slayer-contracts)
      - [Choice]: No gracias.
        - (above|decline-job)
  - [Choice]: Está bien, lo aceptaré.
    - {{anchor|special-slayer-contracts}}(receives=Special slayer contract (Wilderness))
    - [El pergamino sólo puede seguir tu progreso si lo llevas mientras matas. Tráelo de vuelta cuando hayas terminado.]
  - [Choice]: ¿Puedo tener un contrato diferente en su lugar?
    - (above|slayer-contracts)
  - [Choice]: ¿Puedo preguntar algo más?
    - (above|standard)
  - [Choice]: No gracias.
    - (above|decline-job)

### Talk to him when having a contract in the backpack

- (Condition: Si el contrato no se completa:)
  - (Condition: Si el contrato es un contrato especial de asesino:)
    - {{anchor|show-special-contract}} **Erskine:** Muéstrame tu contrato especial cuando lo hayas terminado.
  - (Condition: Si el contrato es un contrato de asesino normal:)
    - {{anchor|show-regular-contract}} **Erskine:** Muéstrame tu contrato cuando lo hayas terminado.
- (Condition: Si el contrato se completa:)
  - **Erskine:** Veo que has completado ese contrato. Trabajo bueno. ¿Quieres XP de combate o dinero en efectivo?
  - {{anchor|choose}} [Menú]: Elige tu recompensa:
    - [Choice]: XP de combate: [número] XP
      - (removes=Slayer contract (Wilderness)) (receives=combat training book)
      - [Recibes un libro sobre combate.]
    - [Choice]: Efectivo: [número] coins
      - (removes=Slayer contract (Wilderness)) (receives=coins)
      - [Recibirás [número] coins.]

### Talk to him when having a contract in the bank

- **Erskine:** Tienes un contrato en tu banco.<br>¿Te lo busco?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: Sí. Por favor tráelo.
    - (Condition: Si el contrato es un contrato especial de asesino:)
      - [Su contrato ha sido recuperado de su banco.]
      - (Condition: Si el contrato no se completa:)
        - (above|show-special-contract)
      - (Condition: Si el contrato se completa:)
        - (above|choose)
    - (Condition: Si el contrato es un contrato de asesino normal:)
      - [Su contrato ha sido recuperado de su banco.]
      - (above|show-regular-contract)
  - [Choice]: No gracias. Déjalo en paz.
    - **Erskine:** Muy bien, pero necesitarás tenerlo en tu inventario si quieres progresar en él.
    - (Condition: Si el contrato es un contrato especial de asesino:)
      - (above|show-special-contract)
    - (Condition: Si el contrato es un contrato de asesino normal:)
      - (above|show-regular-contract)
