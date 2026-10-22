# Wizard Finix

- **Original Wiki Page**: [Transcript:Wizard Finix](https://runescape.wiki/w/Transcript%3AWizard%20Finix)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At the [[Wizards' Tower]]


#### Hablando con Wizard Finix

- **Wizard Finix:** Espero que me dejen entrar pronto al Runecrafting Guild. ¡Hace frío aquí en el tejado!
- [Menu]: Seleccione una opción:{{anchor|init-tower}}
  - [Choice]: ¿Qué haces en el Wizards' Tower?
    - **Wizard Finix:** Soy estudiante de Wizards' Tower. Estoy aquí para ver a Wizard Elriss en Runecrafting Guild sobre la tesis que escribí en Runecrafting.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿De qué se trató la tesis?
        - **Wizard Finix:** Bueno, eso explica mi teoría de que los altares de creación de runas no son eternos. Son grandes reservas de energía rúnica, ¡pero algún día se acabarán!
        - **Wizard Finix:** Creo que es por eso que Wizard Elriss quiere verme. ¡Los magos de Runecrafting Guild no pueden refutar mis teorías y creo que eso les preocupa!
        - **Wizard Finix:** Afortunadamente, creo que encontré un método alternativo para crear runas: ¡energía rúnica en Runespan!
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Extracción de energía rúnica?{{anchor|siphoning}}
            - **Wizard Finix:** ¡Sí! Es una manera de tomar la energía del mundo que nos rodea y colocarla en la esencia rúnica, que a su vez produce runas.
            - **Wizard Finix:** Sigue siendo una teoría, y la mayoría de los magos de Runecrafting Guild piensan que nunca se podrá hacer, pero Wizard Elriss cree que Runespan podría ayudarme en mis estudios.
            - **Wizard Finix:** Veremos qué dice Wizard Elriss, supongo.
            - [Menu]: Selecciona una opción
              - [Choice]: ¿El Runespan?
                - (below|runespan)
              - [Choice]: Otras preguntas...
                - (initial|init-tower)
          - [Choice]: ¿La Runespan?{{anchor|runespan}}
            - **Wizard Finix:** El Runespan es el avión en el que se construyó el Runecrafting Guild. Es un lugar caótico con energía rúnica volando sin ataduras a nada.
            - **Wizard Finix:** Puedes visitar Runespan a través de este portal junto a mí. Los magos lo han estado observando desde el Runecrafting Guild durante años, pero sólo recientemente han estado explorándolo.
            - **Wizard Finix:** Viejos magos tontos. Pasan demasiado tiempo discutiendo y no suficiente tiempo saliendo e investigando todas las teorías que se les ocurren.
            - [Choice]: Seleccione una opción
              - [Choice]: ¿Extracción de energía rúnica?
                - (above|siphoning)
              - [Choice]: Otras preguntas...
                - (initial|init-tower)
          - [Choice]: Otras preguntas...
            - (initial|init-tower)
      - [Choice]: Otras preguntas...
        - (initial|init-tower)
  - [Choice]: ¿Qué vendes?
    - **Wizard Finix:** Puedes comprarme túnicas malvadas. La capucha te dará runas y esencia rúnica e incluso te teletransportará a los altares de creación de runas. El resto de batas mejorarán la capucha y te harán más ligera.
    - **Wizard Finix:** También puedo volver a colorear estas túnicas para ti y proporcionarte un ícono de estima para que muestres cuánto has entrenado para extraer energía.
    - **Wizard Finix:** También puedo proporcionarte bastones hechos de esencia rúnica. Son ineficaces como armas cuerpo a cuerpo, pero pueden almacenar las cargas de hechizos que sólo cuestan runas y son buenos para defenderse de ataques mágicos.
    - **Wizard Finix:** Por último, puedo venderte una bolsa de esencia rúnica que es mucho más grande que cualquiera que puedas encontrar en otros lugares. Esta bolsa no se degradará tan rápido como otras bolsas, pero una vez que se haya degradado se convertirá en polvo.
    - (initial|init-tower)
  - [Choice]: ¿Puedo ver tu tienda?
    - (opens=Wizard Finix's Runecrafting Shop)
  - [Choice]: Adiós.
    - (end)

#### Compras con Wizard Finix

- (opens=Wizard Finix's Runecrafting Shop)
  - (Condition: If something is purchased:)
    - **Wizard Finix:** ¡Disfruta!
    - (opens=Wizard Finix's Runecrafting Shop)
  - (Condition: If esteem is purchased:)
    - **Wizard Finix:** ¡Felicitaciones! En reconocimiento a tu trabajo extrayendo energía rúnica, has alcanzado el rango [número] Estima.
    - (opens=Wizard Finix's Runecrafting Shop)

### At the [[Runespan]]


#### Hablando con Wizard Finix

- **Wizard Finix:** Hola. ¿Le puedo ayudar en algo?
  - Hola. ¿Quién eres?
    - **Wizard Finix:** Soy Wizard Finix. Soy un estudiante de creación de runas.
    - **Player:** Ah, encantado de conocerte, Wizard Finix. Soy Player. ¿Qué estás haciendo aquí?
    - **Wizard Finix:** Estoy creando runas extrayendo energía del Runespan.
    - **Player:** ¿Crear runas extrayendo?
    - **Wizard Finix:** Sí, es una nueva forma de crear runas. ¡Lo descubrí, de hecho!
    - Seleccione una opción
      - ¿Por qué no usas simplemente los altares?{{anchor|runespan-altars}}
        - **Wizard Finix:** ¡Ese es otro de mis descubrimientos! Los altares de Runecrafting no durarán para siempre. ¡Un día se acabarán los altares!
        - **Player:** ¿Se te acabó?
        - **Wizard Finix:** Sí, por supuesto, todavía es sólo una teoría. Los magos de Runecrafting Guild todavía se muestran escépticos, pero no pueden demostrar que estoy equivocado.
        - **Player:** ¿Cómo realizarán la magia los humanos si no pueden crear runas?
        - **Wizard Finix:** Exactamente. Por eso es importante aprender a desviar energía del mundo que nos rodea.
        - **Player:** ¿Quieres decir que podría crear runas extrayendo energía del propio Gielinor?
        - **Wizard Finix:** En teoría, sí, pero todavía no existe ningún creador de runas lo suficientemente capacitado para hacer esto. En teoría, la creación de runas y la magia deberían ser un ciclo autosostenible.
        - **Player:** Entonces, ¿cómo puedo aprender a desviar energía si es tan difícil?
        - **Wizard Finix:** Por eso estamos en esta área. En Runespan, la energía todavía está en un estado muy crudo y no está estrechamente ligada a la materia, como ocurre en Gielinor. Los magos de Runecrafting Guild han estado usando su torre para estudiar la energía rúnica en Runespan durante años.
        - **Player:** Entonces eso significa...
        - **Wizard Finix:** ...estamos fuera del Runecrafting Guild - ¡sí!
        - Seleccione una opción
          - Entonces, ¿cómo se hacen runas mediante sifón?
            - (continue|finix-warning)
          - ¿Puedes teletransportarme de regreso al Wizards' Tower?
            - (below|teleport-to-tower)
      - ¿Cómo se hacen runas mediante sifón?
        - (continue|finix-warning)
      - ¿Puedes teletransportarme de regreso al Wizards' Tower?
        - (below|teleport-to-tower)
  - ¿Qué puedo hacer aquí?
    - **Wizard Finix:** Puedo mostrarte el lugar o simplemente explicártelo. ¿Cuál preferirías?
    - Seleccione una opción
      - Muéstrame
        - *(Comienza el tutorial de Runespan)*
      - Dime
        - **Wizard Finix:** Este es Runespan. Puedes entrenar la creación de runas extrayendo energía de aquí a la esencia de las runas.
        - **Player:** ¿Cómo se crean runas mediante extracción?
        - **Wizard Finix:{{anchor|finix-warning}}** Bueno, en primer lugar, tengo que advertirte que cualquier runa que hagas aquí será tomada por Runecrafting Guild cuando te vayas. Descubrieron el portal a este plano y lo reclamaron como propio. Pero no te preocupes demasiado por eso. Cualquier runa que hagas te otorgará puntos para gastar en mi tienda en Wizards' Tower. Aquí también aprenderás a convertirte en un mejor creador de runas más rápido.
        - Seleccione una opción{{anchor|runespan-opts-3}}
          - ¿Cómo obtengo esencia rúnica?
            - **Wizard Finix:** En primer lugar, aquí solo puedes entrenar la creación de runas con la esencia de runas que se encuentra en este plano.
            - **Player:** Entonces, ¿cómo obtengo esencia rúnica?
            - **Wizard Finix:** Hay dos formas de obtener esencia rúnica. Si no tienes esencia rúnica, puedes usar la esencia flotante para recolectar una pequeña cantidad. Si tienes algo de esencia, la mejor manera de obtener más es extraerla de las criaturas que caminan por ahí.
            - **Player:** ¿Sifón de las criaturas?
            - **Wizard Finix:** Sí. Las criaturas que puedes encontrar aquí están hechas de esencia rúnica unida a energía rúnica. Si quitas toda esa energía, solo te quedará la esencia rúnica. Si tienes prisa y no quieres desviar el contenido de las criaturas, puedes quitarles parte de su esencia rúnica usando tus runas. Sin embargo, desaconsejaría hacérselo a la misma criatura dos veces.
            - (previous|runespan-opts-3)
          - ¿Cómo hago runas?
            - **Wizard Finix:** Una vez que tengas esencia rúnica de este plano, podrás extraer energía de las criaturas y bolsas de energía que aparecen aleatoriamente en las islas de esta área. La energía de las criaturas no es tan densa como lo es en las bolsas de energía, por lo que te darán una pequeña cantidad de runas y no mucha experiencia. Las bolsas de energía son la mejor forma de entrenar. Estos se pueden detectar fácilmente porque, cuando aparece uno, los magos creadores de runas marcarán el piso a su alrededor para mostrar cuándo se puede extraer energía de él. Las bolsas de energía aparecen en lugares aleatorios y puedes encontrarte en una isla donde no las hay. La mejor manera de entrenar es encontrar el tipo de energía más complejo que puedas extraer y extraerlo de ahí.
            - (previous|runespan-opts-3)
          - ¿Cómo me muevo?
            - **Wizard Finix:** Moverse por este avión puede ser complicado ya que está formado por islas flotantes. Afortunadamente, los asistentes de Runecrafting Guild han instalado puntos de cruce. Por el coste de unas cuantas runas, puedes activar estos puntos que te encantarán y te llevarán a otra isla. Sin embargo, dado que están hechos por magos, no es tan simple como saltar de isla en isla. El tipo de runas requeridas se muestra en el punto de cruce. A medida que se acerque a un punto de cruce, el otro lado se iluminará para mostrar hacia dónde se dirige. Si tienes las runas para usar el punto de cruce, el lado cercano también brillará. No todos los puntos de cruce te cobrarán. Si intentas ir de una isla pequeña a una isla grande, el punto de cruce es gratuito. Esto es para evitar que usted quede varado.
            - (previous|runespan-opts-3)
          - ¿Hay algo más que hacer aquí?
            - **Wizard Finix:** Sí, hay un par de cosas que puedes hacer aquí también. Los magos tienen tendencia a quedarse atrapados en islas y, de vez en cuando, escucharás a uno de ellos llamándote. Si encuentras y ayudas al mago, él compartirá contigo algunos de sus conocimientos sobre creación de runas. También existe una rara posibilidad de que se forme una esfera rúnica. Esta es una bola compleja de esencia rúnica de múltiples capas. Cada capa de la esfera rúnica está alineada con un tipo rúnico específico y debes desviar todas las capas de la esfera rúnica. Esto le dará polvo de runas y le impartirá más conocimientos sobre elaboración de runas. La esfera rúnica sólo aparece por un tiempo antes de desaparecer. Si puedes desviar todas sus capas antes de que desaparezca, entonces puedes entregar el polvo de runas que reuniste al desviar las capas al pure energy del interior. Esto te otorgará aún más conocimientos sobre creación de runas.
            - (previous|runespan-opts-3)
          - ¿Por qué no usas simplemente los altares?
            - (above|runespan-altars)
  - ¿Puedo tener algunas runas?
    - (continue|Buying runes from Wizard Finix)
  - ¿Puedes ayudarme a encontrar algo?
    - **Wizard Finix:** Claro, ¿qué te gustaría que te ayudara a encontrar?
    - Seleccione una opción
      - ¿Puedes ayudarme a encontrar un mago con túnica amarilla?
        - **Wizard Finix:** Claro, lo he visto. Te indicaré la dirección correcta por un tiempo.
      - ¿Puedes ayudarme a encontrar la runesfera?
        - *Si la runesfera no está activa actualmente:*
          - **Wizard Finix:** No siento la influencia de la esfera rúnica en este momento.
        - *Si la runesfera está activa:*
          - *Si la esfera rúnica está en un piso superior:*
            - **Wizard Finix:** Siento la influencia de la esfera rúnica sobre mí.
          - *Si la runesfera está en el piso actual:*
            - **Wizard Finix:** Siento la influencia de la esfera rúnica hacia mi <cardinal direction>.
  - ¿Puedes teletransportarme de regreso al Wizards' Tower?{{anchor|teleport-to-tower}}
    - **Wizard Finix:** Claro.
    - (continue|Teleporting with Wizard Finix)

#### Teletransportarse con Wizard Finix

- Todas tus runas se convertirán en puntos cuando te vayas.
- ¿Teletransportarse al Wizards' Tower?
  - si
    - (Action: Wizard Finix teletransporta a el player a la cima del Wizards' Tower.)
  - No
  - (end)

#### Comprando runas de Wizard Finix

- *Si el player aún no ha comprado runas:*
  - **Wizard Finix:** Puedo darte 10 de cada runa que puedes extraer por un costo de puntos de recompensa <number>.
  - ¿Quieres comprar algunas runas?
    - si
      - (receives=10 of each rune that the player can siphon)
    - No
      - (end)
- *Si el player ya ha comprado runas:*
  - **Wizard Finix:** Ya compraste un paquete de inicio. Solo puedes comprar uno por viaje a Runespan.
