# Ignatius Vulcan

- **Original Wiki Page**: [Transcript:Ignatius Vulcan](https://runescape.wiki/w/Transcript%3AIgnatius%20Vulcan)
- **Letter**: `I`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Without level 99 Firemaking

- **Ignatius Vulcan:** ¿Puedo ayudarte en algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Ignatius Vulcan:** Mi nombre es Ignatius Vulcan. Una vez fui, como tú, un aventurero, ¡pero eso fue antes de que me diera cuenta de la belleza y el poder de las llamas! Solo mira esto...
    - (Action: Ignacio enciende un fuego debajo de el player.)
    - **Player:** {{RSChat|Yeeouch!}}
    - **Ignatius Vulcan:** ¡Mira fijamente la llama y sé testigo de la pureza y el poder del fuego! A medida que mi atracción por las llamas crecía, también crecían mis habilidades para encender fuegos. Empecé a descuidar mis habilidades de combate, mis habilidades Mining y mis misiones. ¿Quién necesita habilidades tan mundanas?
    - **Ignatius Vulcan:** ¿Cuándo se puede aprovechar el poder del fuego? ¡Después de años de práctica, ahora soy el Maestro de la Llama reconocido! ¡Todo debe ser purificado por el fuego!
    - **Player:** ¡Está bien! Err, me voy ahora. Umm, mejora pronto.
  - [Choice]: ¿Tienes algo para intercambiar?
    - **Player:** ¿Tienes algo para intercambiar?
    - (opens=Ignatius's Hot Deals)
  - [Choice]: ¿Qué es esa capa que llevas?
    - **Player:** ¿Qué es esa capa que llevas puesta?
    - **Ignatius Vulcan:** Este es un Skillcape de Firemaking. ¡Me lo dieron en reconocimiento a mi habilidad como el mejor fabricante de fuego del país! ¡YO SOY el Maestro de la Llama!
    - **Player:** Hmm, ya me voy. ¡Esté atento a esos hombres con sus chaquetas blancas!
  - [Choice]: No, gracias.
    - **Player:** No, gracias.
    - **Ignatius Vulcan:** Está bien, mantén el fuego encendido.

### With level 99 Firemaking

- **Ignatius Vulcan:** ¿Puedo ayudarte en algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - (arriba)
  - [Choice]: ¿Tienes algo para intercambiar?
    - (arriba)
  - [Choice]: ¿Puedo comprar un Skillcape de Firemaking?
    - (Condition: If the player has a ring of charos (a) equipped:)
      - **Ignatius Vulcan:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins por este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
      - [Menu]: Elige una opción:
        - [Choice]: ¿92.000 coins? Eso es demasiado caro.
          - **Player:** Sé dónde encontrarte si cambio de opinión.
        - [Choice]: De hecho, creo que tengo el dinero aquí.
          - (Condition: If the player has no backpack space:)
            - **Ignatius Vulcan:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar algo de espacio en backpack antes de que pueda venderte uno.
          - (Condition: If the player does not have enough money:)
            - **Player:** Pero desafortunadamente me equivoqué.
            - **Ignatius Vulcan:** Bueno, vuelve a verme cuando lo hagas.
          - (Condition: If the player has enough money:)
            - (receives=firemaking cape and firemaking hood) (removes=92,000 coins)
            - **Ignatius Vulcan:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
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
            - (receives=firemaking cape and firemaking hood) (removes=99,000 coins)
            - **Ignatius Vulcan:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
        - [Choice]: cond=With virtual level 120 Firemaking:|He dominado esta habilidad. ¿Hay algo más?
          - **Ignatius Vulcan:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
          - **Ignatius Vulcan:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
          - **Ignatius Vulcan:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo.
          - **Ignatius Vulcan:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle un Firemaking master cape.
          - [Menu]: ¿Comprar Firemaking master cape por 120.000 coins?
            - [Choice]: Sí.
              - (Condition: Without free backpack space:)
                - **Ignatius Vulcan:** No tienes suficiente espacio en tu backpack. Por favor regresa cuando tengas más.
              - (Condition: With free backpack space:)
                - (Condition: Without 120,000 coins:)
                  - No tienes suficiente dinero para comprar esta capa.
                  - (pop-up)
                    - (Pop-up: You do not have enough money to purchase this cape.|warning=yes)
                - (Condition: With 120,000 coins:)
                  - (removes=120,000 coins) (receives=Firemaking master cape)
                  - (Action: Suena música Master cape.)
            - [Choice]: No.
              - (end)
  - [Choice]: He notado que hay un par de versiones de cada skillcape.
    - **Ignatius Vulcan:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
    - (Condition: If you use the old model:)
      - **Ignatius Vulcan:** Parece que actualmente estás usando el modelo anterior para tu Firemaking skillcape. ¿Quieres cambiar a uno más nuevo?
      - (continue)
    - (Condition: If you use the new model:)
      - **Ignatius Vulcan:** Aún puedes elegir usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, me gustaría usar la versión [new/old] del skillcape.
        - **Ignatius Vulcan:** ¿Te gustaría usar el modelo [old/newer] solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
        - [Menu]: Selecciona una opción
          - [Choice]: Solo me gustaría cambiar el Firemaking skillcape.
            - **Ignatius Vulcan:** No hay problema, ahora utilizarás el modelo [older/newer] para tu Firemaking skillcape.
          - [Choice]: Me gustaría cambiar todos mis skillcapes.
            - **Ignatius Vulcan:** ¡No hay problema, ahora usarás el modelo [older/newer] para todos tus skillcapes!
          - [Choice]: ¡He cambiado de opinión!
            - (end)
      - [Choice]: No, gracias.
        - **Ignatius Vulcan:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión [old/new]!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Ignatius Vulcan:** Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas.
          - [Menu]: Selecciona una opción
            - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
              - **Ignatius Vulcan:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
            - [Choice]: No, gracias.
              - (end)
  - [Choice]: No, gracias.
    - **Player:** No, gracias.
    - **Ignatius Vulcan:** Está bien, mantén el fuego encendido.
