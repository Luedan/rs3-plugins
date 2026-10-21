# Markus

- **Original Wiki Page**: [Transcript:Markus](https://runescape.wiki/w/Transcript%3AMarkus)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talking to Markus


#### Con un contrato completo en el inventario.

- (Si el player tiene un contrato de cazador especial:)
  - **Markus:** Veo que has completado ese contrato. Trabajo bueno. ¿Quieres XP de combate o dinero en efectivo?
- (Si el player tiene un contrato de asesino:)
  - **Markus:** Veo que has completado ese contrato especial. Trabajo bueno. ¿Quieres XP de combate o dinero en efectivo?
- Elige tu recompensa:
  - XP de combate: [#] XP
    - (receives=a combat training book)
    - Recibes un libro sobre combate.
  - Efectivo: [#] coins
    - (receives=coins added directly to their money pouch)
    - Recibirás [#] coins.

#### Con un contrato incompleto en el inventario

- (Si el player tiene un contrato de cazador especial:)
  - **Markus:** Muéstrame tu contrato especial cuando lo hayas terminado.
- (Si el player tiene un contrato de asesino:)
  - **Markus:** Muéstrame tu contrato cuando lo hayas terminado.

#### Sin una tarea Slayer para un monstruo de la Torre Slayer

- **Markus:** ¿Puedo interesarte en un trabajo? Te pagaré por tu trabajo.
- ¿Qué te gustaría decir?
  - Háblame de ti.
    - **Markus:** Mi nombre es Markus. Solía ​​dirigir una empresa comercial en Falador, pero ahora soy un guerrero que lucha contra los males de Morytania. En realidad, descubrí que pelear no es lo mío, así que estoy contratando gente para que haga todo eso por mí. Si estás interesado en luchar tú mismo, estaré encantado de darte un trabajo. Puedo pagarte.
    - ¿Qué te gustaría decir?
      - ¿Qué tipo de trabajo ofreces?
        - (continue|type)
      - Eso es muy noble de tu parte.
        - **Markus:** Gracias. Creo que mi experiencia empresarial y mi riqueza realmente están marcando una diferencia en la lucha contra el mal aquí. ¿Te gustaría un trabajo ahora?
        - (initial)
      - ¿Eres incapaz de hacer tu propio trabajo?
        - **Markus:** Cualquier idiota puede golpear a un monstruo. Con mi experiencia empresarial y mi riqueza, puedo dirigir un ejército para lograr cosas mucho mayores. Sólo necesito encontrar suficientes personas dispuestas a trabajar bajo mis órdenes. Entonces, ¿te gustaría trabajar ahora?
        - (initial)
      - Está bien, me gustaría un trabajo.
        - (continue|job)
      - No, gracias.
        - (continue|no)
  - ¿Qué tipo de trabajo ofreces?
    - **Markus:** Estoy contratando gente para matar a los monstruos de esta torre. Lo haría yo mismo, pero descubrí que pelear no es lo mío. En cambio, uso mi riqueza para contratar personas que maten a los monstruos por mí. ¡Efectivamente, estoy luchando contra los males de Morytania a través de los negocios! Puedo ofrecer pagos en efectivo. Alternativamente, me compré algunos libros sobre combate, pero son demasiado técnicos para mí, así que podrías tener uno como pago. Por cierto, si ya tienes una tarea de otro lugar para matar criaturas que se pueden encontrar dentro de la torre, ven a verme. Cumple tu tarea dentro de la torre y te daré un contrato especial que funcionará en conjunto con él y te daré una recompensa adicional además. Entonces, ¿te gustaría un trabajo ahora?
    - (continuea|extraQs)
  - Está bien, me gustaría un trabajo.
    - **Markus:** Excelente. Echa un vistazo a mi contracts y mira cuál te gustaría hacer.
    - (opens=Slayer contracts)
    - (Si el player acepta un contrato de asesino:)
      - (receives=a slayer contract)
      - El pergamino sólo puede seguir tu progreso si lo llevas mientras matas. Tráelo de vuelta cuando hayas terminado.
  - No gracias.
    - **Markus:** Está bien, pero vuelve si cambias de opinión. Puedo pagarte por tu trabajo.

#### Con una tarea Slayer para un monstruo Torre Slayer

- **Markus:** Veo que tienes una tarea de Slayer. Te pagaré más si aceptas un contrato para realizar tu tarea en esta torre.
- ¿Qué te gustaría decir?
  - ¿Qué estás ofreciendo?
    - **Markus:** Obtendrás una bonificación del 20 % en la XP Slayer obtenida al matar monstruos, además de la opción de XP de combate [#] o [#] coins.
    - (anterior)
  - Está bien, lo aceptaré.
    - (receives=a special slayer contract)
    - El pergamino sólo puede seguir tu progreso si lo llevas mientras matas. Tráelo de vuelta cuando hayas terminado.
  - ¿Puedo tener un contrato diferente en su lugar?
    - (Si el player ya tiene contrato de cazadora:)
      - **Markus:** No, ya tienes uno.
      - (end)
    - (opens=Slayer contracts)
    - (Si el player acepta un contrato de asesino:)
    - (receives=a slayer contract)
    - El pergamino sólo puede seguir tu progreso si lo llevas mientras matas. Tráelo de vuelta cuando hayas terminado.
  - No gracias.
    - **Markus:** Está bien, pero vuelve si cambias de opinión. Puedo pagarte por tu trabajo.

### Using the Contract interact option on Markus

- (Si el player tiene una asignación Slayer para un monstruo Torre Slayer :)
  - (continuea|With a Slayer assignment for a Slayer Tower monster)
- (opens=Slayer Contracts)
- (Si el player acepta un contrato de asesino:)
  - (receives=a slayer contract)
  - El pergamino sólo puede seguir tu progreso si lo llevas mientras matas. Tráelo de vuelta cuando hayas terminado.
