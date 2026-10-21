# Sloane

- **Original Wiki Page**: [Transcript:Sloane](https://runescape.wiki/w/Transcript%3ASloane)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Sloane:** Ahhh, hola, Player.
- (Condition: Si el player tiene 99 Strength:)
  - **Sloane:** ¡Ah, pero puedo ver que ya eres lo más fuerte posible! ¿Quizás has venido a mí para comprar un Skillcape o un Strength y así unirte a la élite que domina esta exigente habilidad?
  - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: cond=If the player is below 99 Strength:|¿Puedes contarme un poco sobre skillcapes?
    - **Player:** ¿Puedes contarme un poco sobre skillcapes?
    - **Sloane:** Claro. Puedes comprar un skillcape cuando alcances el nivel 99 en una habilidad. Además de mejorar tus estadísticas en esa habilidad, ¡también pueden usarse para realizar algunos gestos increíbles! ¿Hay algo más que te gustaría saber?
    - (initial)
  - [Choice]: |cond=Si el player tiene 99 Strength:|¿Puedo comprar un Skillcape de Strength, por favor?
    - (Condition: Si el player tiene un ring of charos (a) equipado:)
      - **Sloane:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins para este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
      - [Menu]: Elige una opción:
        - [Choice]: ¿92.000 coins? Eso es demasiado caro.
          - **Player:** Sé dónde encontrarte si cambio de opinión.
        - [Choice]: De hecho, creo que tengo el dinero aquí.
          - (Condition: Si el player no tiene espacio backpack:)
            - **Sloane:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar espacio en backpack antes de que pueda venderte uno.
          - (Condition: Si el player no tiene suficiente dinero:)
            - **Player:** Pero desafortunadamente me equivoqué.
            - **Sloane:** Bueno, vuelve a verme cuando lo hagas.
          - (Condition: Si el player tiene suficiente dinero:)
            - (receives=Strength cape and Strength hood) (removes=92,000 coins)
            - **Sloane:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
    - (Condition: Si el player no tiene un ring of charos(a) equipado:)
      - [Menu]: Elige una opción:
        - [Choice]: ¿99.000 coins? Eso es demasiado caro.
          - **Player:** Sé dónde encontrarte si cambio de opinión.
        - [Choice]: De hecho, creo que tengo el dinero aquí.
          - (Condition: Si el player no tiene espacio backpack:)
            - (arriba)
          - (Condition: Si el player no tiene suficiente dinero:)
            - (arriba)
          - (Condition: Si el player tiene suficiente dinero:)
            - (receives=Strength cape and Strength hood) (removes=99,000 coins)
            - **Sloane:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
  - [Choice]: He notado que hay un par de versiones de cada skillcape.
    - **Sloane:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
    - (Condition: Si usas el modelo antiguo:)
      - **Sloane:** Parece que actualmente estás usando el modelo anterior para tu Strength skillcape. ¿Quieres cambiar a uno más nuevo?
      - (continue)
    - (Condition: Si utiliza el nuevo modelo:)
      - **Sloane:** Aún puedes optar por usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, me gustaría usar la versión [new/old] del skillcape.
        - **Sloane:** ¿Te gustaría usar el modelo [old/newer] solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
        - [Menu]: Selecciona una opción
          - [Choice]: Solo me gustaría cambiar el Strength skillcape.
            - **Sloane:** No hay problema, ahora utilizarás el modelo [older/newer] para tu Strength skillcape.
          - [Choice]: Me gustaría cambiar todos mis skillcapes.
            - **Sloane:** ¡No hay problema, ahora usarás el modelo [older/newer] para todos tus skillcapes!
          - [Choice]: ¡He cambiado de opinión!
            - (end)
      - [Choice]: No, gracias.
        - **Sloane:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión [old/new]!
        - (Condition: Si el player usa el nuevo modelo para cualquier otro skillcape:)
          - **Sloane:** Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas.
          - [Menu]: Selecciona una opción
            - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
              - **Sloane:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
            - [Choice]: No, gracias.
              - (end)
  - [Choice]: ¿Qué puedo hacer aquí?
    - **Player:** ¿Qué puedo hacer aquí?
    - **Sloane:** Ahh, el lanzamiento de peso es una gran prueba de fuerza y puede ser bastante gratificante. Eso sí, asegúrate de hacerlo correctamente; es posible que primero quieras espolvorearte las manos con alguna sustancia en polvo. Le dará un mejor agarre.
    - **Player:** Lo recordaré. ¿Qué debo usar?
    - **Sloane:**Personalmente prefiero las cenizas molidas, produce un polvo fino y agradable y proporciona un agarre realmente bueno.
    - **Player:** Vale, ¿qué más?
    - **Sloane:** Básicamente tendrás que entrar allí, asegurarte de no tener nada en tus manos, tomar un tiro y lanzarlo. Dependiendo de tu técnica, puedes realizar lanzamientos bastante largos.
    - **Player:** ¿Cuál fue tu mejor?
    - **Sloane:** Ahh, eso sería revelador.
    - (initial)
  - [Choice]: ¡Esa es un hacha grande!
    - **Player:** ¡Esa es un hacha grande!
    - **Sloane:** Sí, efectivamente lo es. Tienes que ser muy fuerte para manejarlo también.
    - **Player:** ¡Pero no te ves tan fuerte!
    - **Sloane:** Tal vez, tal vez no, pero aún así tuve que vencer a un Bárbaro para conseguirlo. Eso sí, normalmente no se separan de ellos. Esta fue una circunstancia inusual.
    - **Player:** ¿Ah?
    - **Sloane:** Le apuesto que no podría atrapar una ardilla mientras todavía sostiene su hacha, pero que yo sí podría... y que si ganaba, conseguiría su hacha.
    - **Player:** ¿Qué pasó?
    - **Sloane:** Salió corriendo detrás de la ardilla... casi la atrapa también... se subió a un árbol y él trató de trepar, solo se enredó un poco con su hacha porque no podía agarrarse a ella al mismo tiempo y... se cayó del árbol.
    - **Sloane:** Luego fue mi turno....
    - **Sloane:** Simplemente fui y corté el árbol con esta gran hacha vieja, todavía sosteniéndola. La ardilla estaba tan petrificada que simplemente saltó del árbol hacia mí. ¡Gané el hacha y dejé ir a la pobre criatura!
    - **Player:** Siento una moraleja en alguna parte.
    - **Sloane:** Sí, claro. Músculo no es todo lo que necesitas para empuñar un hacha grande, ¡también se requiere cerebro!
    - (initial)
  - [Choice]: ¡Adiós!
    - **Player:** ¡Adiós!
    - (Action: Sloane hace el gesto Bow.)
    - **Sloane:** Que estés bien, guerrero Player.

### In City of Um


#### Saludando a Sloane

- (Action: el player saluda a Sloane y él le devuelve el saludo.)
- **Player:** Yadech continúa con su legado.
