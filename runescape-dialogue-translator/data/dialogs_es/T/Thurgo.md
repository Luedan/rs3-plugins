# Thurgo

- **Original Wiki Page**: [Transcript:Thurgo](https://runescape.wiki/w/Transcript%3AThurgo)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At Mudskipper Point


#### Durante La espada del caballero

- (ver|La espada del caballero#Hablando con Thurgo)

#### Después de la espada del caballero

- [Menu]: ¿Sobre qué te gustaría preguntar? {{anchor|standard}}
  - [Choice]: Skillcape de Smithing
    - (Condition: If the player is below 99 Smithing:)
      - **Player:** Esa capa que llevas es inusual, ¿qué es?
      - **Thurgo:** Es un Skillcape de Smithing. Demuestra que soy un maestro herrero, pero, por supuesto, eso es de esperarse. Después de todo, soy un enano Imcando y todo el mundo sabe que somos los mejores herreros.
    - (Condition: If the player has 99 Smithing and has a ring of charos (a) equipped:)
      - **Thurgo:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins para este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
      - [Menu]: Elige una opción:
        - [Choice]: ¿92.000 coins? Eso es demasiado caro.
          - **Player:** Sé dónde encontrarte si cambio de opinión.
        - [Choice]: De hecho, creo que tengo el dinero aquí.
          - (Condition: If the player has no backpack space:)
            - **Thurgo:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar espacio en backpack antes de que pueda venderte uno.
          - (Condition: If the player does not have enough money:)
            - **Player:** Pero desafortunadamente me equivoqué.
            - **Thurgo:** Bueno, vuelve a verme cuando lo hagas.
          - (Condition: If the player has enough money:)
            - (receives=Smithing cape and Smithing hood) (removes=92,000 coins)
            - **Thurgo:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
        - [Choice]: cond=If the player has 120 Smithing|He dominado esta habilidad. ¿Hay algo más?
          - **Thurgo:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
          - **Thurgo:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
          - **Thurgo:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo.
          - **Thurgo:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle un Smithing master cape.
          - [Menu]: ¿Comprar Smithing master cape por 120.000 coins?
            - [Choice]: Sí.
              - (Condition: If the player has no backpack space:)
                - **Thurgo:** No tienes suficiente espacio en tu backpack. Por favor regresa cuando tengas más.
              - (Condition: If the player does not have enough money:)
                - No tienes suficiente dinero para comprar esta capa.
              - (Condition: If the player has enough money:)
                - (receives=Smithing master cape) (removes=120,000 coins)
                - (Action: Suena música Master cape.)
            - [Choice]: No.
              - (end)
    - (Condition: If the player has 99 Smithing but does not have a ring of charos (a) equipped:)
      - [Menu]: Elige una opción:
        - [Choice]: ¿99.000 coins? Eso es demasiado caro.
          - **Player:** Sé dónde encontrarte si cambio de opinión.
        - [Choice]: De hecho, creo que tengo el dinero aquí.
          - (Condition: If the player has no backpack space:)
            - (arriba)
          - (Condition: If the player does not have enough money:)
            - (arriba)
          - (Condition: If the player has enough money:)
            - (receives=Smithing cape and Smithing hood) (removes=99,000 coins)
            - **Thurgo:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
        - [Choice]: cond=If the player has 120 Smithing|He dominado esta habilidad. ¿Hay algo más?
          - (arriba)
  - [Choice]: cond=If the player has 99 Smithing|He notado que hay un par de versiones de cada skillcape.
    - **Thurgo:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
    - (Condition: If the player is using the old model:)
      - **Thurgo:** Parece que actualmente estás usando el modelo anterior para tu Smithing skillcape. ¿Quieres cambiar a uno más nuevo?
      - (continue)
    - (Condition: If the player is using the new model:)
      - **Thurgo:** Aún puedes optar por usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, me gustaría usar la versión [new/old] del skillcape.
        - **Thurgo:** ¿Te gustaría usar el modelo [old/newer] solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
        - [Menu]: Selecciona una opción
          - [Choice]: Solo me gustaría cambiar el Smithing skillcape.
            - **Thurgo:** No hay problema, ahora utilizarás el modelo [older/newer] para tu Smithing skillcape.
          - [Choice]: Me gustaría cambiar todos mis skillcapes.
            - **Thurgo:** ¡No hay problema, ahora usarás el modelo [older/newer] para todos tus skillcapes!
          - [Choice]: ¡He cambiado de opinión!
            - (end)
      - [Choice]: No, gracias.
        - **Thurgo:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión [old/new]!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Thurgo:** Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas.
          - [Menu]: Selecciona una opción
            - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
              - **Thurgo:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
            - [Choice]: No, gracias.
              - (end)
  - [Choice]: Algo más.
    - **Player:** Sobre esa espada...
    - **Player:** ¡Gracias por toda tu ayuda para conseguirlo!
    - **Thurgo:** No te preocupes, amigo.

#### Después de Birthright of the Dwarves mientras tienes piezas de pico Imcando en el inventario

- **Thurgo:** ¡Un cosquilleo en mis huesos de Imcando! ¿Puede realmente ser...?
- **Thurgo:** ¡Sí! ¡Has encontrado parte de un antiguo pico Imcando! ¿Podría verlo?
- [Menu]: Selecciona una opción
  - [Choice]: Por favor hazlo.
    - *(Si tienes de uno a tres fragmentos de pico Imcando en tu inventario:)*
      - **Thurgo:** ¡Sí! ¡Tienes un trozo del antiguo pico Imcando! Si me traes las cuatro piezas, puedo recrear el pico para ti.
      - (continue|MakePickaxe)
    - *(Si tienes los cuatro fragmentos del pico Imcando en tu inventario:)*
      - **Thurgo:** ¡Tienes las cuatro piezas! ¡Con esto puedo recrear un antiguo pico Imcando para ti!
      - (continue|MakePickaxe)
    - **Thurgo:** Aunque no será fácil. Además de las piezas, necesitaré un pico de dragón dorado y un millón de coins para comprar otros materiales.
    - **Thurgo:** Y un pastel de frutos rojos, por supuesto. ¡Smithing me da hambre!
    - [Menu]: Selecciona una opción
      - [Choice]: Si el player tiene todos los elementos necesarios en backpack|tengo esas cosas conmigo ahora.
        - **Player:** Ahora tengo esas cosas conmigo.
        - **Thurgo:** ¡Excelente! Déjame ponerme a trabajar.
        - (Action: La pantalla se desvanece y luego aparece.)
        - (removes=1,000,000 coins, the four Imcando pickaxe fragments and the redberry pie)
        - (receives=the Imcando pickaxe)
        - [Thurgo crea un pico mágico para ti.]
      - [Choice]: ¿Un pico Imcando?
        - **Player:** ¿Un pico Imcando?
        - [El pico Imcando es equivalente a un pico bane +4 y, de manera similar, requiere 80 Mining para su uso. A diferencia de un pico Bane, el pico Imcando se puede aumentar con la habilidad Invention.]
      - [Choice]: Gracias, adiós.
        - (end)
  - [Choice]: Pregunta por otra cosa.
    - (above|standard)

#### Mientras tenga piezas de azadón Imcando en el inventario

- **Thurgo:** ¡Un hormigueo en los dedos de mis pies Imcando! ¿Es eso realmente lo que creo que es?
- **Thurgo:** ¡Sí! Te has encontrado con algo muy raro. Algo de metal Imcando sin forjar. ¿Te importa si le echo un vistazo?
- [Menu]: Selecciona una opción
  - [Choice]: Por favor hazlo.
    - ((If the player doesn't have all four Imcando pieces:))
      - **Thurgo:** ¡Sí! ¡Tienes un trozo del antiguo metal Imcando! Dado que Archaeology es la gran moda en este momento, si me traes las cuatro piezas, puedo enseñarte cómo hacer tu propio azadón Imcando.
      - (continue|MakeMattock)
    - ((If the player has all four Imcando pieces:))
      - [Menu]: Selecciona una opción
        - [Choice]: ¿Puedes ayudarme a hacer un azadón?
          - **Thurgo:** ¡Tienes suficientes piezas! Con estos, en lugar de hacerlo yo mismo, puedo enseñarte cómo trabajar los metales Imcando y hacer el azadón tú mismo.
          - (continue|MakeMattock)
        - [Choice]: ¿Puedes ayudarme a hacer un pico?
          - **Thurgo:** Lamentablemente no, para una herramienta tan grande como un pico Imcando necesitaría piezas mucho más grandes, siendo Archaeology la gran moda en este momento, esto es suficiente para un azadón.
          - (previous)
    - **Thurgo:** Aunque no será fácil. Además de las piezas, necesitaré un azadón de dragón y un millón de coins por el momento.
    - **Thurgo:** Y un pastel de frutos rojos, por supuesto.
    - [Menu]: Selecciona una opción
      - [Choice]: cond=If the player has all of the required items|Tengo esas cosas conmigo ahora.
        - **Thurgo:** Pongámonos a trabajar.
        - (Action: La pantalla se vuelve negra y luego vuelve a aparecer.)
        - (removes=redberry pie and 1,000,000 coins)
        - Has aprendido cómo crear un azadón Imcando, lleva el metal Imcando a un yunque en la forja.
        - **Thurgo:** ...y luego, una vez que unes estas dos piezas con un poco de fundente para evitar que el metal se oxide. Te has convertido en una herramienta que los enanos estarían orgullosos de usar {{Sic}}.
        - **Player:** Gracias, Thurgo.
      - [Choice]: cond=If the player does not have all four Imcando pieces|Un azadón Imcando
        - (below|AskAboutMattock)
      - [Choice]: cond=If the player has all four Imcando pieces|¿Un azadón Imcando?
        - **Thurgo:** Con todos los sitios antiguos que se han descubierto últimamente, parece correcto equipar a los mejores arqueólogos con las herramientas y los medios para descubrir los secretos de nuestros antepasados.
        - **Thurgo:** Si puedes encontrar suficientes de estos raros metales Imcando, puedo enseñarte cómo crear una herramienta de este tipo por ti mismo.
      - [Choice]: Gracias, adiós.
        - (end)
  - [Choice]: Pregunta por otra cosa.
    - (above|standard)

#### Después de Canción desde las profundidades mientras tienes una ballesta de coral en el inventario

- **Thurgo:** ¡Tú! ¿Puedo echarle un vistazo a esa ballesta de coral?
- [Menu]: Selecciona una opción
  - [Choice]: Por favor hazlo.
    - **Thurgo:** ¡Esta es una ingeniería increíble! Tu ballesta podría volverse extremadamente poderosa si le agregamos los componentes adecuados.
    - **Thurgo:** Desafortunadamente, a juzgar por los materiales, las llamas que necesitarás para forjar estos componentes deberán estar extremadamente calientes; mucho más allá de lo que cualquier forja convencional podría producir. Probablemente necesitarías un antiguo
    - **Thurgo:** ¡un dragón de las leyendas que produce una llama lo suficientemente caliente!
    - **Thurgo:** Mientras tanto, puedo realizar un ensamblaje básico de estos componentes si lo deseas; Sin embargo, no se podrá utilizar como arma hasta que lo expongas a un calor extremo.
    - [Menu]: ¿Montar la ballesta real no forjada?
      - [Choice]: Sí.
        - *(Si faltan piezas de la ballesta real:)*
          - Le faltan los siguientes componentes: <br>a perno estabilizador <br>a marco <br>a mira <br>a resorte
        - *(Si todas las piezas de la ballesta real están presentes:)*
          - (removes=royal torsion spring, royal stabiliser, royal sight and royal frame) (receives=Royal crossbow (unforged))
          - Thurgo comienza a montar la ballesta. Thurgo te entrega la ballesta sin forjar.
          - **Thurgo:** Debes exponerlo a calor extremo para finalizar el proceso. Probablemente podré realizar cualquier mantenimiento necesario una vez que esté hecho, si me lo permite.
      - [Choice]: No ahora mismo.
        - (above|standard)
  - [Choice]: Pregunta por otra cosa.
    - (above|standard)

#### Mientras tengas piezas de hacha de Imcando en el inventario

- **Thurgo:** ¡Un hormigueo en mis dedos Imcando! ¿Es eso...?
- **Thurgo:** ¡Sí! ¡Has encontrado parte de un antiguo hacha de Imcando! ¿Podría verlo?
- [Menu]: Selecciona una opción
  - [Choice]: Por favor hazlo.
    - (Condition: If the player doesn't have all four Imcando hatchet fragments:)
      - **Thurgo:** ¡Sí! ¡Tienes un trozo del antiguo hacha Imcando! Si me traes las cuatro piezas, puedo recrear el hacha para ti.
    - (Condition: If the player has all four Imcando hatchet fragments:)
      - **Thurgo:** ¡Tienes las cuatro piezas! ¡Con esto puedo recrear un antiguo hacha Imcando para ti!
    - **Thurgo:** Aunque no será fácil. Además de las piezas, necesitaré un hacha de dragón y un millón de coins para comprar otros materiales.
    - (Condition: If the player doesn't have all four Imcando hatchet fragments:)
      - **Thurgo:** Y un pastel de frutos rojos, por supuesto. ¡Smithing me da hambre!
    - (Condition: If the player has all four Imcando hatchet fragments:)
      - **Thurgo:** Y como estoy seguro de que ya sabrás, ¡mi pastel de frutos rojos es de suma importancia!
    - [Menu]: Selecciona una opción
      - [Choice]: cond=Only with all the required items:|Tengo esas cosas conmigo ahora.
        - **Thurgo:** ¡Excelente! Déjame ponerme a trabajar.
        - (Action: La pantalla se desvanece y vuelve a aparecer.)
        - (removes=the Imcando hatchet fragments, dragon hatchet, redberry pie, and a million coins) (receives=an Imcando hatchet)
        - (Condition: If receiving an Imcando hatchet for the first time:)
          - ¡Felicitaciones! Has completado: 'Imcando at a tree' - Obtén un hacha de Imcando.
          - (continue)
        - [Thurgo crea un hacha mágica para ti.]
      - [Choice]: ¿Un hacha Imcando?
        - **Thurgo:** Es un antiguo artefacto enano, ¿no es suficientemente emocionante?
        - **Thurgo:** Un hacha será mucho mejor para cortar árboles que un hacha de dragón, eso es seguro.
        - (Condition: If the player has a crystal hatchet on their toolbelt:)
          - **Player:** Oh, ya tengo un hacha de cristal en mi cinturón de herramientas. ¡Es un hacha de dragón mejorada!
          - **Thurgo:** ¿Esta cosa endeble? ¡Bah! ¡Un hacha Imcando lo atravesará!
      - [Choice]: Gracias, adiós.
        - (end)
  - [Choice]: Pregunta por otra cosa.
    - (above|standard)

### At Thalmund's forge

- ((One of the following sequences is seen.))

#### Dándole un pastel de frutos rojos

- **Thurgo:** {{RSChat|Thanks, pal!}}

#### Secuencia 1

- (Thurgo aparece en las puertas del norte).
- (Thurgo camina hacia los escombros en el sur).
- **Thurgo:** {{RSChat|Needs a clean.}}
- (Thurgo camina hacia la palanca.)
- **Thurgo:** {{RSChat|Smells like pie and slag.}}
- (Thurgo camina hacia la habitación con el yunque imcando y lo investiga.)
- (Thurgo camina hacia el horno.)
- **Thurgo:** {{RSChat|Impressive.}}
- (Thurgo camina hacia el estante de armas de los duendes, lo investiga y se teletransporta.)

#### Secuencia 2

- (Thurgo aparece en las puertas del norte).
- (Thurgo camina hacia los escombros en el sur).
- **Thurgo:** {{RSChat|What a mess!}}
- (Thurgo camina hacia la palanca.)
- **Thurgo:** {{RSChat|Hmmm...}}
- (Thurgo camina hacia la habitación con el yunque imcando y lo investiga.)
- (Thurgo camina hacia el horno.)
- **Thurgo:** {{RSChat|Not bad.}}
- (Thurgo camina hacia el estante de armas de los duendes, lo investiga y se teletransporta.)
