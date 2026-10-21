# Pikkenmix

- **Original Wiki Page**: [Transcript:Pikkenmix](https://runescape.wiki/w/Transcript%3APikkenmix)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### While obelisk is active, first conversation

- **Player:** Hola.
- **Pikkenmix:** ¿Dónde ESTÁN? No han regresado todavía.
- **Player:** ¿Quién?
- **Pikkenmix:** Los otros druidas; Pikkupstix estará muy molesto.
- **Pikkenmix:** Fueron a recolectar fragmentos en bruto del plano espiritual, pero o no regresarán en absoluto o regresarán con las manos vacías.
- **Pikkenmix:** Aparentemente, ahora hay muchos fragmentos esparcidos por ahí para ser recogidos, pero los familiares en el reino no están contentos con la situación y están tratando de detener a cualquiera que intente recuperarlos.
- [Menu]: Elige una opción:
  - [Choice]: No veo ningún druida por aquí.
    - **Player:** No veo ningún druida por aquí.
    - **Pikkenmix:** Bueno, no lo harías, ¿verdad? No están aquí. Entraron al plano espiritual para recolectar fragmentos en bruto. Pikkupstix irá de sobra; esto sigue pasando!
    - **Player:** Umm... cierto.
    - (previous)
  - [Choice]: ¿Por qué brilla ese obelisco?
    - **Player:** ¿Por qué brilla ese obelisco?
    - **Pikkenmix:** Está activo. Cuando está activo de esta manera, los druidas podemos ingresar al plano espiritual para recolectar fragmentos espirituales en bruto.
    - (continue|sparklingquestion)
  - [Choice]: ¿Puedo ayudar?
    - **Player:** ¿Puedo ayudar?
    - **Pikkenmix:** ¿Quieres ayudarnos a conseguir fragmentos?
    - (continue|helpshards)

### While obelisk is active, subsequent conversations

- **Pikkenmix:** Entonces, ¿nos ayudarás a reunir más fragmentos sin procesar?
- [Menu]: Selecciona una opción
  - [Choice]: Claro, lo intentaré.
    - **Player** Claro, lo intentaré.
    - (Condition: Si la familiarización no se ha completado esa semana:)
      - (Action: el player mete la mano en el obelisco y es teletransportado al plano espiritual.)
    - (Condition: Si la familiarización ya se completó esa semana:)
      - **Pikkenmix:** Ya me has ayudado esta semana.
      - Ya has ayudado a Pikkenmix esta semana. Vuelve el miércoles.
    - (Condition: Si el obelisco ha dejado de brillar antes de terminar el diálogo:)
      - **Pikkenmix:** Ya me has ayudado esta semana.
      - El obelisco ya no está activo.
    - (Condition: Si hay un seguidor fuera:)
      - **Pikkenmix:** Me temo que no puedes entrar ahí con esa mascota siguiéndote. Podría distraerte con consecuencias desastrosas.
  - [Choice]: ¿Cuáles son los riesgos?
    - **Player:** ¿Cuáles son los riesgos?
    - **Pikkenmix:** Bueno, no hay riesgo para tu forma física ni para tus objetos en este reino. Tu cuerpo permanece aquí, por lo que realmente no puedes morir.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Cuáles son los límites de este enfoque mental del que hablas?
        - **Player:** ¿Cuáles son los límites de este enfoque mental del que hablas?
        - **Pikkenmix:** Bueno, Pikkupstix dice que es bastante agotador mentalmente mantener la concentración en permanecer en el plano espiritual, por lo que solo puedes hacerlo por un tiempo limitado y solo una vez por semana.
        - **Player:** Hmm, está bien, entonces tendré que trabajar rápido.
        - **Pikkenmix:** Descubrirás que solo puedes tener un máximo de sesenta fragmentos sin procesar a la vez. Pikkupstix dice que es porque tienen un efecto drenante en tu concentración mental.
        - (otro)
      - [Choice]: ¿Algún otro efecto dentro del plano espiritual?
        - **Player:** ¿Algún otro efecto dentro del plano espiritual?
        - **Pikkenmix:** Bueno, no podrás andar corriendo por ahí dentro. Tómate tu tiempo y conserva tu energía al correr. Al menos eso es lo que enseña Pikkupstix.
        - **Player:** ¿Pero eso no me afectará cuando salga?
        - **Pikkenmix:** No, en absoluto.
        - (otro)
      - [Choice]: ¿Alguna limitación sobre lo que puedo llevar conmigo?
        - **Player:** ¿Alguna limitación sobre lo que puedo llevar conmigo?
        - **Pikkenmix:** En realidad no, pero las mejoras físicas no te beneficiarán en absoluto en el plano espiritual, por lo que en realidad no se necesita nada. Se trata del enfoque mental que tengas.
        - (otro)
      - [Choice]: Pregunta por otra cosa.
        - (below|sparklingquestion)
  - [Choice]: Pregunta por otra cosa.
    - [Menu]: Elige una opción:
      - [Choice]: ¿Entrar como si simplemente entrara?
        - **Player:** ¿Entrar como si simplemente entrara?
        - **Pikkenmix:** ¡No, no, no! Usamos nuestra fortaleza mental y nuestro enfoque para penetrar el reino espiritual. Nuestros cuerpos físicos permanecen aquí en este mundo. Lo llamamos "familiarización".
        - **Player:** ¿Es difícil?
        - **Pikkenmix:** No, pero puede ser mentalmente agotador. Por supuesto, no tiene ningún efecto sobre nada en este mundo.
        - [Menu]: Elige una opción:
          - [Choice]: ¿Cuáles son los riesgos?
            - (above|risk)
          - [Choice]: ¿Por qué entras en el plano espiritual?
            - (below|enter)
          - [Choice]: ¿Cómo entraría al plano espiritual?
            - (abajo)
      - [Choice]: ¿Por qué entras en el plano espiritual?
        - **Player:** ¿Por qué ingresas al plano espiritual?
        - **Pikkenmix:** Ah, yo también me lo preguntaba... hasta que Pikkupstix me lo dijo. ¿Sabes, por supuesto, que los fragmentos espirituales están hechos de fragmentos de obeliscos de invocación?
        - [Menu]: Selecciona una opción
          - [Choice]: Sí, ¿qué pasa con eso?
            - **Player:** Sí, ¿qué pasa?
            - **Pikkenmix:** ¿Alguna vez has visto algún obelisco en la tierra que haya sido desconchado?
            - **Player:** Ahora que lo mencionas, no.
            - **Pikkenmix:** ¡Exactamente! Sin embargo, descubrimos que los fragmentos de este reino no funcionan correctamente para unir un espíritu entre reinos, por lo que tenemos que usar los fragmentos del plano espiritual.
            - **Player:** Oh.
            - [Menu]: Selecciona una opción
              - [Choice]: ¿De dónde vienen todos los fragmentos espirituales que utilizamos?
                - **Pikkenmix:** Un gran obelisco en el plano espiritual. Ahora que los druidas no han regresado, debería haber muchos fragmentos en bruto esparcidos por allí.
                - **Player:** Vaya, entonces simplemente están tirados por ahí...
                - (otro)
              - [Choice]: ¿No puedes hacerlos de otra manera?
              - **Pikkenmix:** Hemos intentado todo lo que se nos ha ocurrido, pero parece que, a menos que provengan del plano espiritual en su forma original, no están en sintonía con él, por lo que no pueden actuar como un vínculo entre reinos a través del cual invocar a un familiar.
              - (otro)
              - [Choice]: ¿Quién los colecciona?
                - **Player:** ¿Quién los colecciona?
                - **Pikkenmix:** Algunos de los druidas más valientes usan todas sus habilidades mentales para ingresar al plano espiritual y recolectar fragmentos en bruto del obelisco que se encuentra allí. Luego sintonizamos esos fragmentos en bruto con este reino para crear un lin. No es fácil y requiere una gran concentración mental.
                - (otro)
              - [Choice]: Entonces, ¿cuál es el problema?
                - **Player:** Entonces, ¿cuál es el problema?
                - **Pikkenmix:** Bueno, recientemente, hemos estado apareciendo espíritus rebeldes en RuneScape...
                - **Pikkenmix:** Ha habido un número cada vez mayor de estas incursiones, y ahora no todos nuestros druidas regresan del plano espiritual con fragmentos.
                - **Player:** ¿Quieres decir que se los están comiendo?
                - **Pikkenmix:** ¡No! Oh, no. Su forma corpórea permanece aquí; sólo su esencia viaja al plano espiritual. Parece que los familiares allí les impiden tomar fragmentos en bruto.
                - **Player:** Interesante... Así que hay montones de estos fragmentos en bruto vagando por ahí sin reclamar...
                - (previous2|sparklingquestion)
              - [Choice]: pregunta sobre otra cosa
                - (above|sparklingquestion)
          - [Choice]: No, nunca he examinado un fragmento espiritual.
            - **Player:** No, nunca he examinado un fragmento espiritual.
            - **Pikkenmix:** Bueno, de ahí son - obeliscos de invocación desconchados - pero, como decía...
            - **Pikkenmix:** ¿Alguna vez has visto algún obelisco en la tierra que haya sido desconchado?
            - (continuea|whatofit)
      - [Choice]: ¿Cómo entraría al plano espiritual?
        - **Player:** ¿Cómo entraría al plano espiritual?
        - **Pikkenmix:** Debería ser bastante fácil para ti, ya que Pikkupstix me ha estado enseñando a ayudar a otros en la técnica. Lo llamamos "familiarización". Los fenómenos del obelisco también ocurren razonablemente regularmente: cada dos horas... más o menos.
        - [Menu]: Elige una opción:
          - [Choice]: ¿Cuáles son los riesgos?
            - (above|risk)
          - [Choice]: ¿Entrar como si simplemente entrara?
            - (above|stroll)
          - [Choice]: ¿Por qué entras en el plano espiritual?
            - (above|enter)
  - [Choice]: No, gracias.
    - **Player:** No, gracias.

### At an inactive obelisk

- **Player:** Hola.
- **Pikkenmix:** Ah. Hola.
- **Player:** ¿Qué pasa?
- **Pikkenmix:** Estoy estudiando este obelisco; estuvo activo recientemente.
- [Menu]: Selecciona una opción
  - [Choice]: ¿A qué te refieres con activo?
    - **Player:** ¿Qué quieres decir con activo?
    - **Pikkenmix:** Brillan, y cuando lo hacen podemos entrar en el plano espiritual.
    - (above|sparklingquestion)
  - [Choice]: ¿Puedo ayudar?
    - **Player:** ¿Puedo ayudar?
    - **Pikkenmix:** No hasta que encuentre otro obelisco activo. Pero si quieres, puedo contarte un poco sobre lo que sucede cuando los obeliscos están activos. Brillan, y cuando lo hacen, podemos entrar en el plano espiritual.
    - (continuea|sparklingquestion)
  - [Choice]: Eso es lindo. Adiós.
    - **Player:** Eso es bueno. Adiós.

### Claiming a reward

- (Condition: Si es la primera vez que es elegible para una recompensa:)
  - **Pikkenmix:** Hola de nuevo, gracias por ayudarnos. Si lo deseas, puedo darte una recompensa a cambio de los fragmentos en bruto que hayas recolectado. ¡Pikkupstix dice que puedo!
  - (continue|rewards)
- (Condition: Momentos posteriores elegibles para una recompensa:)
  - **Pikkenmix:** Gracias por conseguir los fragmentos.
  - **Pikkenmix:** Si quieres, puedo darte una recompensa a cambio de los fragmentos sin procesar que hayas recolectado.
  - (continue|rewards)
- [Menu]: Selecciona una opción
  - [Choice]: Sí, por favor.
    - **Player:** Sí, por favor.
    - **Pikkenmix:** ¡Excelente, excelente! Has recolectado x montones de fragmentos en bruto. ¿Te gustarían gotas de triple encanto para un rato o algunos ingredientes de Summoning?
    - [Menu]: Selecciona una opción
      - [Choice]: Gotas de amuleto triple.
        - **Player** Gotas de amuleto triple.
        - ((Si el player ya tiene un potenciador de caída de amuletos de una recompensa anterior:))
          - **Pikkenmix:** Me temo que ya tienes nuestra recompensa. Elige otra cosa.
          - **Pikkenmix:** Si quieres, puedo contarte un poco sobre estos obeliscos y cómo entrar al plano espiritual cuando están activos.
          - (continuea|sparklingquestion)
        - (Condition: De lo contrario:)
          - Pikkenmix hace un movimiento oscuro con sus manos que no se puede ver del todo.
          - (receives=charm drop enhancer)
          - **Pikkenmix:** Ahí lo tienes; Creo que eso es correcto. Al menos, eso es lo que Pikkupstix me dijo que hiciera. Solo durará 40 minutos desde que rompas el boleto, ¡así que comienza a recolectar amuletos! Vuelve en <number> días, cuando te hayas recuperado y puedas volver a ayudarnos.
          - (continue|While obelisk is active, subsequent conversations)
      - [Choice]: Ingredientes Summoning.
        - ((Si el player ya tiene una caja de ingredientes de invocación de una recompensa anterior:))
          - **Pikkenmix:** Ya tienes una caja de esos. Cuando lo hayas abierto te puedo dar otro.
        - (Condition: De lo contrario:)
          - **Player:** Ingredientes Summoning.
          - (receives=a box of summoning ingredients)
          - [Pikkenmix te entrega una caja.]
          - **Pikkenmix:** Ahí lo tienes.
          - **Pikkenmix:** Si quieres, puedo contarte un poco sobre estos obeliscos y cómo entrar al plano espiritual cuando están activos.
          - (continuea|sparklingquestion)
  - [Choice]: No, gracias.
    - **Player:** No, gracias.
    - **Pikkenmix:** Está bien. Vuelve si cambias de opinión.
    - **Pikkenmix:** Si quieres, puedo contarte un poco sobre estos obeliscos y cómo entrar al plano espiritual cuando están activos.
    - (continuea|sparklingquestion)

#### Si la familiarización se completó sin reunir ningún fragmento

- **Pikkenmix:** Hola.
- **Player:** Hola.
- **Pikkenmix:** ¿No estuviste recientemente en el plano espiritual? No regresaste con ningún fragmento si no recuerdo mal. ¿Por qué fue eso?
- [Menu]: Selecciona una opción
  - [Choice]: No pude encontrar ningún fragmento para recoger.
    - **Pikkenmix:** Oh, lamento escuchar eso. Espero que lo intentes de nuevo; Estoy seguro de que puedes hacerlo un poco mejor.
    - **Pikkenmix:** Intenta dirigirte en una dirección y mirar a tu alrededor. Estarán dispersos donde los druidas los hayan dejado para escapar.
    - **Pikkenmix:** Si quieres, puedo contarte un poco sobre estos obeliscos y cómo entrar al plano espiritual cuando están activos.
    - (continuea|sparklingquestion)
  - [Choice]: No pude resolver lo que se suponía que debía hacer.
    - **Pikkenmix:** Oh, lamento escuchar eso. Espero que lo intentes de nuevo; Estoy seguro de que puedes hacerlo un poco mejor.
    - **Pikkenmix:** Dentro del plano espiritual, hay fragmentos por ahí. Debes recoger tantos de estos como sea posible, evitando al mismo tiempo a los familiares que te estén persiguiendo.
    - **Pikkenmix:** Si quieres, puedo contarte un poco sobre estos obeliscos y cómo entrar al plano espiritual cuando están activos.
    - (continuea|sparklingquestion)
  - [Choice]: Fui atacado por demasiados familiares.
    - **Pikkenmix:** Oh, lamento escuchar eso. Espero que lo intentes de nuevo; Estoy seguro de que puedes hacerlo un poco mejor.
    - **Pikkenmix:** A veces, puedes evitar a los familiares mirando su hábitat. Los familiares amantes del agua, como los sapos ladradores y los señores supremos karamthulu, no se alejan mucho del agua.
    - **Pikkenmix:** Si quieres, puedo contarte un poco sobre estos obeliscos y cómo entrar al plano espiritual cuando están activos.
    - (continuea|sparklingquestion)
  - [Choice]: No quería.
    - **Pikkenmix:** Oh, lamento escuchar eso. Espero que lo intentes de nuevo; Estoy seguro de que puedes hacerlo un poco mejor.
    - **Pikkenmix:** Si recolectas fragmentos para nosotros, podemos ofrecerte una recompensa. Inténtalo la próxima vez, ¡puede que lo disfrutes!
    - **Pikkenmix:** Si quieres, puedo contarte un poco sobre estos obeliscos y cómo entrar al plano espiritual cuando están activos.
    - (continuea|sparklingquestion)
  - [Choice]: Alguna otra razón.
    - **Pikkenmix:** Oh, lamento escuchar eso. Espero que lo intentes de nuevo; Estoy seguro de que puedes hacerlo un poco mejor.
    - **Pikkenmix:** Si quieres, puedo contarte un poco sobre estos obeliscos y cómo entrar al plano espiritual cuando están activos.
    - (continuea|sparklingquestion)

### After claiming a reward

- **Pikkenmix:** Hola de nuevo.
- **Player:** Hola.
- **Pikkenmix:** Espero que hayas disfrutado de tu recompensa por ayudarnos a recolectar fragmentos en bruto del plano espiritual.
- **Pikkenmix:** Si quieres, puedo contarte un poco sobre estos obeliscos y cómo entrar al plano espiritual cuando están activos.
- (continuea|sparklingquestion)
