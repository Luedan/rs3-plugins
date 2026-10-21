# Head chef

- **Original Wiki Page**: [Transcript:Head chef](https://runescape.wiki/w/Transcript%3AHead%20chef)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Outside the Cooks' Guild


#### Intentando entrar sin 32 Cooking

- Necesitas un nivel 32 de Cooking para ingresar al gremio de the Chef.
- ((Repetido en una ventana emergente:))
  - Necesitas un nivel 32 de Cooking para ingresar al gremio de the Chef.
- **Head chef:** Lo siento. Aquí sólo se permiten los mejores chefs. Consigue tu nivel Cooking hasta 32 y vuelve con un gorro de chef.

#### Intentando entrar con el nivel 32 Cooking pero sin gorro de chef

- **Head chef:** No puedes entrar aquí a menos que lleves un gorro de chef o algo así.

#### Entrando con los logros duros de Varrock completos

- **Head chef:** ¡Un maestro explorador de Varrock! ¡Eres más que bienvenido aquí, amigo mío!

### Inside the Cooks' Guild


#### Hablando con el head chef


##### Sin nivel 99 Cooking

- **Head chef:** Hola, bienvenido al gremio Cooking. Aquí solo se permiten chefs y cocineros consumados. No dude en utilizar cualquiera de nuestras instalaciones.
- [Menu]: Selecciona una opción
  - [Choice]: Habla sobre el 'Asistente del Chef'. {{anchor|cheesecake}}
    - (Condition: Antes del asistente del chef:)
      - (ver|Asistente del chef#Comenzando la misión)
    - (Condition: Después del asistente del chef:)
      - (ver|Asistente del chef#Diálogo posterior a la misión)
  - [Choice]: cond=If the player is below 99 Cooking|¡Bonita capa la que llevas!
    - **Player:** ¡Bonita capa la que llevas puesta!
    - **Head Chef:** ¡Gracias! Es mi posesión más preciada, es un Skillcape de Cooking; ¡Demuestra que he alcanzado el nivel 99 Cooking y soy uno de los mejores chefs del mundo!
  - [Choice]: Gracias, adiós.
    - **Player:** Gracias, adiós.

##### Con nivel 99 Cooking

- **Head chef:** Hola, bienvenido al gremio Cooking. Siempre es fantástico que nos visite un chef tan consumado. Dime, ¿estarías interesado en un Skillcape de Cooking? Sólo están disponibles para maestros chefs.
- [Menu]: Selecciona una opción
  - [Choice]: Habla sobre el 'Asistente del Chef'.
    - (above|cheesecake)
  - [Choice]: No gracias.
    - **Player:** No, gracias.
    - **Head chef:** Está bien, vuelve conmigo si cambias de opinión.
  - [Choice]: Sí por favor.
    - (Condition: Si el player está en un mundo gratuito:)
      - **Head Chef:** Lo siento, no puedo venderte uno aquí. Intenta hablar conmigo en un mundo de miembros.
    - (Condition: Si el player está en un mundo de miembros:)
      - (Condition: Si el player tiene un ring of charos (a) equipado:)
        - **Head chef:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins por este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
        - [Menu]: Elige una opción:
          - [Choice]: ¿92.000 coins? Eso es demasiado caro.
            - **Player:** Sé dónde encontrarte si cambio de opinión.
          - [Choice]: De hecho, creo que tengo el dinero aquí.
            - (Condition: Si el player no tiene espacio backpack:)
              - **Head chef:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar algo de espacio en backpack antes de que pueda venderte uno.
            - (Condition: Si el player no tiene suficiente dinero:)
              - **Player:** Pero desafortunadamente me equivoqué.
              - **Head chef:** Bueno, vuelve a verme cuando lo hagas.
            - (Condition: Si el player tiene suficiente dinero:)
              - (receives=cooking cape and cooking hood) (removes=92,000 coins)
              - **Head chef:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
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
              - (receives=cooking cape and cooking hood) (removes=99,000 coins)
              - **Head chef:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
  - [Choice]: He notado que hay un par de versiones de cada skillcape.
    - **Head chef:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
    - (Condition: Si usas el modelo antiguo:)
      - **Head chef:** Parece que actualmente estás usando el modelo anterior para tu Prayer skillcape. ¿Quieres cambiar a uno más nuevo?
      - (continue)
    - (Condition: Si utiliza el nuevo modelo:)
      - **Head chef:** Aún puedes elegir usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, me gustaría usar la versión [new/old] del skillcape.
        - **Head chef:** ¿Te gustaría usar el modelo [old/newer] solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
        - [Menu]: Selecciona una opción
          - [Choice]: Solo me gustaría cambiar el Prayer skillcape.
            - **Head chef:** No hay problema, ahora utilizarás el modelo [older/newer] para tu Prayer skillcape.
          - [Choice]: Me gustaría cambiar todos mis skillcapes.
            - **Head chef:** ¡No hay problema, ahora usarás el modelo [older/newer] para todos tus skillcapes!
          - [Choice]: ¡He cambiado de opinión!
            - (end)
      - [Choice]: No, gracias.
        - **Head chef:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión [old/new]!
        - (Condition: Si el player usa el nuevo modelo para cualquier otro skillcape:)
          - **Head chef:** Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas.
          - [Menu]: Selecciona una opción
            - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
              - **Head chef:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
            - [Choice]: No, gracias.
              - (end)

#### Intentando entrar a la sala del banco sin los duros logros de Varrock

- **Head chef:** Oye, no puedes entrar ahí.
- **Player:** Oh, ¿por qué no?
- **Head chef:** Me temo que eso es sólo para los mejores exploradores de Varrock.
- **Player:** Ah, ya veo. ¿Cómo puedo convertirme en un explorador así?
- **Head chef:** Hmm, bueno, por lo que he oído, se otorga a personas que han demostrado ser un beneficio para la ciudad al completar todas las tareas fáciles, intermedias y difíciles en Varrock.
- (Condition: Si el player ha adquirido la armadura Varrock:)
  - **Player:** Aunque tengo la armadura Varrock.
  - **Head chef:** Sí, pero parece que tienes algunas tareas más que realizar antes de que podamos confiar en ti en este banco. Vuelve cuando hayas completado todas las tareas difíciles y puedas demostrarlo.
- (Condition: Si el player lleva la armadura Varrock:)
  - **Player:** Aunque llevo la armadura Varrock.
  - **Head chef:** Sí, pero parece que tienes algunas tareas más que realizar antes de que podamos confiar en ti en este banco. Vuelve cuando hayas completado todas las tareas difíciles y puedas demostrarlo.
