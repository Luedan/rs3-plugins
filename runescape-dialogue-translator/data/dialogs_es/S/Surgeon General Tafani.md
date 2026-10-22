# Surgeon General Tafani

- **Original Wiki Page**: [Transcript:Surgeon General Tafani](https://runescape.wiki/w/Transcript%3ASurgeon%20General%20Tafani)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Normalmente

- **Player:** ¡Hola!
- **Surgeon General Tafani:** Hola. ¿Cómo puedo ayudar?
- Seleccione una opción
  - ¿Puedes curarme?
    - **Player:** ¿Puedes curarme?
    - **Surgeon General Tafani:** ¡Por supuesto!
    - (Action: Surgeon General Tafani intenta curar a el player.)
    - *(Si el player tiene salud completa:)*
      - **Surgeon General Tafani:** ¡Me pareces saludable!
      - (continue)
    - *(Si el player no tiene salud completa:)*
      - (Action: el player se cura por algunos puntos de vida.)
      - Te sientes un poco mejor.
      - (continue)
  - ¿Ves muchos combatientes heridos?
    - **Player:** ¿Ves muchos peleadores heridos?
    - ((Before the destruction of Duel Arena:))
      - **Surgeon General Tafani:** Sí, lo hago. Afortunadamente, podemos hacer frente a casi cualquier cosa. Jaraah realmente es un cirujano maravilloso; sus métodos son un poco poco ortodoxos pero hace el trabajo. No debería decirte esto, pero su apodo es 'El Carnicero'.
      - **Player:** Eso es tranquilizador.
    - ((After the destruction of Duel Arena:))
      - **Surgeon General Tafani:** No tanto estos días, pero cuando el Duel Arena todavía existía, vi una buena cantidad de lesiones.
      - **Surgeon General Tafani:** Afortunadamente, pudimos hacer frente a casi cualquier cosa. Jaraah realmente es un cirujano maravilloso. Sus métodos eran un poco poco ortodoxos, pero hizo el trabajo.
      - **Surgeon General Tafani:** No debería decirte esto, pero su apodo es 'El Carnicero'.
      - **Player:** Eso es tranquilizador.
      - (previous)
  - ¿Vienes aquí a menudo?
    - **Player:** ¿Vienes aquí a menudo?
    - ((Before the destruction of Duel Arena:))
      - **Surgeon General Tafani:** Trabajo aquí, así que sí. ¡Eres tonto!
    - ((After the destruction of Duel Arena:))
      - **Surgeon General Tafani:** Bueno, aquí es donde trabajo ahora, así que sí. Éste es un lugar tan bueno como cualquier otro para montar un hospital.
      - (previous)
  - ((Only if not returning from another question:))
    - ¿Puedo comprarles un Skillcape o un Constitution?
      - *(Si el player tiene alguna de las variantes de Ring of Charos equipada:)*
        - **Surgeon General Tafani:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins por este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
        - Elige una opción:
          - ¿92.000 coins? Eso es demasiado caro.
            - (below|expensive)
          - De hecho, creo que tengo el dinero aquí.
            - (below|buy-cape)
      - *(Si el player no tiene ninguna de las variantes de Ring of Charos equipadas:)*
        - **Surgeon General Tafani:** Vaya, ciertamente amigo mío. Sin embargo, poseer un artículo de este tipo te convierte en parte de un grupo de élite y ese privilegio te costará 99 000 coins.
        - Elige una opción:
          - ¿99.000 coins? Eso es demasiado caro.
            - **Surgeon General Tafani:{{anchor|expensive}}** En absoluto; ¡Hay muchos otros aventureros a quienes les encantaría tener la oportunidad de comprar un artículo tan prestigioso! Puedes encontrarme aquí si cambias de opinión.
          - De hecho, creo que tengo el dinero aquí.{{anchor|buy-cape}}
            - *(Si el player tiene la cantidad requerida de coins:)*
              - Capa (removes=the required coins) (receives=Constitution cape (if the player only has level 99 in Constitution) o Constitution (t) (si el player tiene nivel 99 en múltiples habilidades) y capucha Constitution)
              - **Surgeon General Tafani:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
            - *(Si el player no tiene la cantidad requerida de coins:)*
              - **Player:** Pero, lamentablemente, me equivoqué.
              - **Surgeon General Tafani:** Bueno, vuelve a verme cuando lo hagas.
          - [Choice]: cond=Only with true skill mastery in Constitution:|He dominado esta habilidad. ¿Hay algo más?
            - **Surgeon General Tafani:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
            - **Surgeon General Tafani:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
            - **Surgeon General Tafani:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo...
            - **Surgeon General Tafani:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle un Constitution master cape.
            - [Menu]: ¿Comprar Constitution master cape por 120.000 coins?
              - (Sí).
                - (Condition: Without free backpack space:)
                  - **Surgeon General Tafani:** No tienes suficiente espacio en tu backpack. Por favor regresa cuando tengas más.
                - (Condition: With free backpack space:)
                  - (Condition: Without 120,000 coins:)
                    - No tienes suficiente dinero para comprar esta capa.
                    - ((Repeated in a pop-up:))
                      - No tienes suficiente dinero para comprar esta capa.
                  - (Condition: With 120,000 coins:)
                    - (removes=120,000 coins) (receives=Constitution master cape)
                    - (Action: Suena música Master cape.)
              - [Choice]: No.
                - (end)
  - ((Only if not returning from another question:))
    - He notado que hay un par de versiones de cada skillcape.
      - **Surgeon General Tafani:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
      - *(Si el player ha elegido los nuevos modelos skillcape :)*
        - **Surgeon General Tafani:** Aún puedes elegir usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
        - Seleccione una opción
          - Sí, me gustaría usar la versión antigua del skillcape.
            - **Surgeon General Tafani:** ¿Te gustaría usar el modelo antiguo solo para esta capa, o para la capa de puntos Quest y todos los skillcapes que tienes?
            - Seleccione una opción
              - Solo me gustaría cambiar el Constitution skillcape.
                - **Surgeon General Tafani:** No hay problema, ahora utilizarás el modelo anterior para tu Constitution skillcape.
                - Me gustaría cambiar todos mis skillcapes.
                - **Surgeon General Tafani:** No hay problema, ¡ahora usarás el modelo anterior para todos tus skillcapes!
              - ¡He cambiado de opinión!
                - (end)
          - No, gracias.
            - **Surgeon General Tafani:** ¡Genial! ¡Me alegra que estés disfrutando de nuestra nueva versión!
            - *(Si el player está usando los modelos skillcape antiguos excepto la capa Constitution :)*
              - **Surgeon General Tafani:** ¡Si quieres, puedo hacerlo para que uses el modelo más nuevo para todos los skillcapes que tienes!
              - Seleccione una opción
                - Ok, me gustaría usar la versión más nueva para todos mis skillcapes.
                  - **Surgeon General Tafani:** ¡Genial, ahora usarás el modelo más nuevo para todos tus skillcapes!
                - No, gracias.
                  - (end)
      - *(Si el player ha elegido los modelos antiguos skillcape :)*
        - **Surgeon General Tafani:** Parece que actualmente estás usando el modelo anterior para tu Constitution skillcape. ¿Quieres cambiar a uno más nuevo?
        - Seleccione una opción
          - Sí, me gustaría usar la nueva versión del skillcape.
            - **Surgeon General Tafani:** ¿Te gustaría usar el modelo más nuevo solo para esta capa o para todos los skillcapes que tienes?
            - Seleccione una opción
              - Solo me gustaría cambiar el Constitution skillcape.
                - **Surgeon General Tafani:** No hay problema, ahora utilizarás el modelo más nuevo para tu Constitution skillcape.
              - Me gustaría cambiar todos mis skillcapes.
                - **Surgeon General Tafani:** No hay problema, ¡ahora usarás el modelo más nuevo para todos tus skillcapes!
              - ¡He cambiado de opinión!
                - (end)
          - No, gracias.
            - **Surgeon General Tafani:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión anterior!
            - *(Si el player está usando los nuevos modelos skillcape excepto la capa Constitution :)*
              - **Surgeon General Tafani:** ¡Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas!
              - Seleccione una opción
                - Ok, me gustaría usar la versión antigua para todos mis skillcapes.
                  - **Surgeon General Tafani:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
                - No, gracias.
                  - (end)
  - ((Only if returning from another question:))
    - Adiós
      - (end)

#### Durante la tarea "verificar con el médico" en el evento Oasis Restoration

- **Player:** ¡Hola!
- **Surgeon General Tafani:** Hola. ¿Cómo puedo ayudar?
- **Player:** ¿Están todos bien después de que, ya saben, el Duel Arena colapsara?
- **Surgeon General Tafani:** Oh, bastante. Todos hemos pasado por cosas mucho peores.
- **Player:** ¿En serio? ¿Cómo qué?
- **Surgeon General Tafani:** Bueno... hubo... el incidente de la piña.
- **Player:** ¿Qué pasó allí?
- **Surgeon General Tafani:** No hablamos de eso. ¡ALGUNA VEZ! Todavía escucho los gritos cuando sueño.
- Has completado: 'Consulta con el médico' y has progresado hacia el evento Restauración del Oasis.
- **Surgeon General Tafani:** ¡El horror! ¡El dulce y pegajoso horror!
- (above|options)

### Heal

- (above|heal)
