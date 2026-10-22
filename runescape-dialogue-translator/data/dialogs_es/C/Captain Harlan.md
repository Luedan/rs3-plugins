# Captain Harlan

- **Original Wiki Page**: [Transcript:Captain Harlan](https://runescape.wiki/w/Transcript%3ACaptain%20Harlan)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Lumbridge Market

- [Menu]: ¿De qué te gustaría hablar?
  - [Choice]: ¿Quién eres?
    - **Harlan:** ¡Mi nombre es Harlan, un maestro de la defensa!
    - (otro)
  - [Choice]: cond=If the player has 99 Defence|¿Qué es esa capa que llevas?
    - **Harlan:** Ah, este es un Skillcape de Defence. He dominado el arte de la defensa y lo uso con orgullo para mostrárselo a los demás.
    - **Player:** Mmmm, interesante.
    - **Harlan:** Ah, pero veo que ya eres un maestro en el fino arte de la defensa. ¿Quizás has venido a mí para comprar un Skillcape o un Defence y así unirte a la élite que domina esta exigente habilidad?
    - [Menu]: Elige una opción:
      - [Choice]: Sí, por favor véndeme un Skillcape de Defence.
        - (Condition: If the player has a ring of charos (a) equipped:)
          - **Harlan:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins para este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
          - [Menu]: Elige una opción:
            - [Choice]: ¿92.000 coins? Eso es demasiado caro.
              - **Player:** Sé dónde encontrarte si cambio de opinión.
            - [Choice]: De hecho, creo que tengo el dinero aquí.
              - (Condition: If the player has no backpack space:)
                - **Harlan:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar espacio en backpack antes de que pueda venderte uno.
              - (Condition: If the player does not have enough money:)
                - **Player:** Pero desafortunadamente me equivoqué.
                - **Harlan:** Bueno, vuelve a verme cuando lo hagas.
              - (Condition: If the player has enough money:)
                - (receives=Defence cape and Defence hood) (removes=92,000 coins)
                - **Harlan:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
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
                - (receives=Defence cape and Defence hood) (removes=99,000 coins)
                - **Harlan:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
      - [Choice]: No, gracias.
        - (end)
      - [Choice]: He notado que hay un par de versiones de cada skillcape.
        - **Harlan:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
        - (Condition: If you use the old model:)
          - **Harlan:** Parece que actualmente estás usando el modelo antiguo para tu Defence skillcape. ¿Quieres cambiar a uno más nuevo?
          - (continue)
        - (Condition: If you use the new model:)
          - **Harlan:** Aún puedes elegir usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
          - (continue)
        - [Menu]: Selecciona una opción
          - [Choice]: Sí, me gustaría usar la versión [new/old] del skillcape.
            - **Harlan:** ¿Te gustaría usar el modelo [old/newer] solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
            - [Menu]: Selecciona una opción
              - [Choice]: Solo me gustaría cambiar el Defence skillcape.
                - **Harlan:** No hay problema, ahora usarás el modelo [older/newer] para tu Defence skillcape.
              - [Choice]: Me gustaría cambiar todos mis skillcapes.
                - **Harlan:** ¡No hay problema, ahora usarás el modelo [older/newer] para todos tus skillcapes!
              - [Choice]: ¡He cambiado de opinión!
                - (end)
          - [Choice]: No, gracias.
            - **Harlan:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión [old/new]!
            - (Condition: If the player uses the new model for any other skillcape:)
              - **Harlan:** Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tienes.
              - [Menu]: Selecciona una opción
                - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
                  - **Harlan:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
                - [Choice]: No, gracias.
                  - (end)
  - [Choice]: Habla sobre la asistencia del jefe.
    - (Condition: If on a free-to-play world:)
      - Debes estar en el mundo de un miembro para utilizar esta función.
    - (Condition: If on a members' world:)
      - **Harlan:** La asistencia del jefe es un incentivo para ayudar a tus compañeros aventureros a enfrentarse a los enemigos más grandes del mundo.
      - **Player:** Entonces, ¿cómo funciona?
      - **Harlan:** Bastante simple en realidad. Cuando un jefe muere, si has luchado con aventureros que lograron herir al jefe pero aun así tienes menos de diez muertes, recibirás un punto por cada persona.
      - **Player:** ¿Entonces obtengo un punto para todos los que tienen menos de diez muertes y lograron involucrarse en la pelea?
      - **Harlan:** Eso es correcto, sí. Los puntos que ganes pueden ayudarte a desbloquear algunas recompensas. ¿Te gustaría verlas?
      - [Menu]: ¿Qué te gustaría decir?
        - [Choice]: Claro, muéstrame mi progreso hacia las recompensas.
          - (Se abre la interfaz de Asistencia del jefe).
        - [Choice]: Eso es todo por ahora.
          - **Harlan:** No hay problema. No olvides que te enseñé todo lo que sabes, Player.

#### Diálogo histórico

- [Menu]: ¿De qué te gustaría hablar?
  - [Choice]: ¿Quién eres?
    - (arriba)
  - [Choice]: cond=If the player has 99 Defence|¿Qué es esa capa que llevas?
    - (arriba)
  - [Choice]: ¿Qué está pasando en Lumbridge?
    - (Condition: After the Lumbridge Rebuildathon:)
      - **Harlan:** No hace mucho, hubo una gran batalla cerca de aquí, entre Saradomin y Zamorak. ¡Duró meses!
      - **Harlan:** Aún puedes ver la devastación que hay a tu alrededor. Incluso con el esfuerzo de reconstrucción, Lumbridge tardará años en recuperarse por completo.
    - (Condition: After the Battle of Lumbridge but before the Lumbridge Rebuildathon:)
      - **Harlan:** Todavía se puede ver la devastación que hay a nuestro alrededor: Lumbridge tardará años en recuperarse.
      - **Harlan:** No hace mucho, hubo una gran batalla aquí, entre Saradomin y Zamorak. ¡Duró meses!
      - **Harlan:** Ya se acabó. ¡Espero que este tipo de peleas nunca vuelvan a Lumbridge!
    - (Condition: During the Battle of Lumbridge:)
      - **Harlan:** Mira a tu alrededor: puedes ver la devastación, todo debido a los combates en el campo de batalla al oeste.
      - **Harlan:** No mucho después de la muerte de Guthix, Saradomin y Zamorak regresaron a Gielinor y comenzaron a pelear aquí mismo en Lumbridge.
      - **Harlan:** Aún así, Lady Deathknell y yo intentamos entrenar a las personas para que puedan aprender a defenderse durante estos tiempos difíciles.
  - [Choice]: Habla sobre la asistencia del jefe.
    - (arriba)
