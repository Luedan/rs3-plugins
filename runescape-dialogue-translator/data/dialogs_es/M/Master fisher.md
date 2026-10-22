# Master fisher

- **Original Wiki Page**: [Transcript:Master fisher](https://runescape.wiki/w/Transcript%3AMaster%20fisher)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Fishing Guild


#### Hablando con él

- **Master fisher:** Hola, bienvenido al gremio Fishing. No dude en hacer uso de cualquiera de nuestras instalaciones.
- [Menu]: ¿Sobre qué te gustaría preguntar?
  - [Choice]: ¿Puedes hablarme sobre el Fishing skillcape?
    - (Condition: If the player is below level 99 Fishing:)
      - **Master fisher:** Estoy feliz de hacerlo, amigo mío. Esta hermosa capa me fue entregada en reconocimiento a mis habilidades y experiencia como pescador y al mismo tiempo me pidieron ser el líder de este gremio. Como el mejor pescador del gremio, es mi deber controlar quién tiene acceso al gremio y decir quién puede comprar skillcapes similares.
    - (Condition: If the player is at least level 99 Fishing)
      - (Condition: If the player has a ring of charos (a) equipped:)
        - **Master fisher:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins por este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
        - [Menu]: Elige una opción:
          - [Choice]: ¿92.000 coins? Eso es demasiado caro.
            - **Player:** Sé dónde encontrarte si cambio de opinión.
          - [Choice]: De hecho, creo que tengo el dinero aquí.
            - (Condition: If the player has no backpack space:)
              - **Master fisher:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar algo de espacio en backpack antes de que pueda venderte uno.
            - (Condition: If the player does not have enough money:)
              - **Player:** Pero desafortunadamente me equivoqué.
              - **Master fisher:** Bueno, vuelve a verme cuando lo hagas.
            - (Condition: If the player has enough money:)
              - (receives=fishing cape and fishing hood) (removes=92,000 coins)
              - **Master fisher:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
      - (Condition: If the player does not have a ring of charos (a) equipped:)
        - [Menu]: Elige una opción:
          - [Choice]: ¿99.000 coins? Eso es demasiado caro.
            - **Player:** Sé dónde encontrarte si cambio de opinión.
          - [Choice]: De hecho, creo que tengo el dinero aquí.
            - (Condition: If the player has no backpack space:)
              - (arriba)
            - (Condition: If the player does not have enough money:)
              - (arriba)
            - (Condition: If the player has enough money:)
              - (receives=fishing cape and fishing hood) (removes=99,000 coins)
              - **Master fisher:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
          - [Choice]: cond=With 120 virtual Fishing:|He dominado esta habilidad. ¿Hay algo más?
            - **Master fisher:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
            - **Master fisher:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
            - **Master fisher:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo...
            - **Master fisher:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle un Fishing master cape.
            - [Menu]: ¿Comprar Fishing master cape por 120.000 coins?
              - [Choice]: Sí.
                - (Condition: Without free backpack space:)
                  - **Master fisher:** No tienes suficiente espacio en tu backpack. Por favor regresa cuando tengas más.
                - (Condition: With free backpack space:)
                  - (Condition: Without 120,000 coins:)
                    - No tienes suficiente dinero para comprar esta capa.
                    - (pop-up)
                      - (Pop-up: You do not have enough money to purchase this cape.|warning=yes)
                  - (Condition: With 120,000 coins:)
                    - (removes=120,000 coins) (receives=Fishing master cape)
                    - (Action: Suena música Master cape.)
              - [Choice]: No.
                - (end)
  - [Choice]: ¿Puedes ayudarme con los trajes de tiburón?
    - **Player:** ¿Puedes ayudarme con los trajes de tiburón?
    - ((If the player can't receive shark fragments and hasn't unlocked the blueprint required to make the outfit pieces:))
      - **Master fisher:** En el nivel 70 puedes comenzar a recolectar fragmentos para crear trajes de habilidades de élite. Cuando llegues a ese nivel, automáticamente comenzarás a recolectar fragmentos. Luego puedes usarlos con un plano para hacerte las piezas restantes del atuendo de élite para esta habilidad.
    - ((If the player can receive shark fragments but hasn't unlocked the blueprint required to make the outfit pieces:))
      - **Master fisher:** Estás configurado para recibir fragmentos. Cuando llegues al nivel 80 podrás crear prendas de vestir.
    - ((If the player can receive shark fragments and has unlocked the blueprint required to make the outfit pieces:))
      - **Master fisher:** Estás configurado para recibir fragmentos. Cuando tengas 3600 fragmentos, podrás usarlos para crear una pieza de atuendo de élite. Simplemente acude a un banco de trabajo Invention para crear las piezas.
    - ((If the player owns the full fury shark outfit, or all of the outfit pieces required to craft it:))
      - **Master fisher:** Ya has creado todas las prendas posibles. Me aseguraré de que no reciba más fragmentos. Recuerda que puedes combinar las piezas del conjunto básico para hacer las versiones de nivel alto y obtener beneficios adicionales.
  - [Choice]: He notado que hay un par de versiones de cada skillcape.
    - **Master fisher:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
    - (Condition: If you use the old model:)
      - **Master fisher:** Parece que actualmente estás usando el modelo anterior para tu Fishing skillcape. ¿Quieres cambiar a uno más nuevo?
      - (continue)
    - (Condition: If you use the new model:)
      - **Master fisher:** Aún puedes elegir usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, me gustaría usar la versión [new/old] del skillcape.
        - **Master fisher:** ¿Te gustaría usar el modelo [old/newer] solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
        - [Menu]: Selecciona una opción
          - [Choice]: Sólo me gustaría cambiar la pesca skillcape.
            - **Master fisher:** No hay problema, ahora utilizarás el modelo [older/newer] para tu skillcape de pesca.
          - [Choice]: Me gustaría cambiar todos mis skillcapes.
            - **Master fisher:** ¡No hay problema, ahora usarás el modelo [older/newer] para todos tus skillcapes!
          - [Choice]: ¡He cambiado de opinión!
            - (end)
      - [Choice]: No, gracias.
        - **Master fisher:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión [old/new]!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Master fisher:** Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas.
          - [Menu]: Selecciona una opción
            - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
              - **Master fisher:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
            - [Choice]: No, gracias.
              - (end)
  - [Choice]: Nada.
    - (end)

#### Opción de carterista

- (Antes y después de Deadliest Catch:)
- No tienes motivos para robarle.
