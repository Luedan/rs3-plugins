# Party Pete

- **Original Wiki Page**: [Transcript:Party Pete](https://runescape.wiki/w/Transcript%3AParty%20Pete)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Falador Party Room


#### Diálogo estándar

- **Player:** ¡Hola!
- **Party Pete:** ¡Hola! Soy Party Pete. ¡Bienvenidos al Salón de Fiestas!
- *Si no se ha completado el logro 'Seguir con el 'Fro':*
  - color = blanco
- Seleccione una opción
  - Entonces, ¿para qué es esta habitación?
    - **Player:** Entonces, ¿para qué sirve esta habitación?
    - **Party Pete:** ¡Esta habitación es para salir de fiesta toda la noche!
    - **Player:** ¿Cómo se hace una fiesta?
    - **Party Pete:** ¡Reúne algunos amigos, prepara las cervezas y diviértete! Algunos jugadores organizan fiestas, ¡así que mantente atento!
    - **Player:** ¡Vaya! Gracias Pete!
  - ¿Para qué sirve esa gran palanca de ahí?
    - **Player:** ¿Para qué sirve la gran palanca de ahí?
    - **Party Pete:** Sencillo. Con la palanca puedes hacer cosas divertidas.
    - **Player:** ¿Qué tipo de cosas?
    - **Party Pete:** La caída de un globo cuesta 1000 de oro. Para esto, se lanzan 200 globos por toda la sala de fiestas. ¡Luego podrás divertirte haciendo estallar los globos! Cualquier artículo en el Party Drop Chest se colocará en globos tan pronto como jales la palanca. Cuando se suelten los globos, ¡puedes reventarlos para alcanzar los objetos! Por 500 de oro, puedes convocar a los Party Room Knights, que bailarán para tu deleite. ¡Sin embargo, su canto no es una delicia!
  - ¿Para qué es el cofre de oro?
    - **Player:** ¿Para qué es el cofre dorado?
    - **Party Pete:** Cualquier objeto en el cofre caerá dentro de los globos cuando jales la palanca.
    - **Player:** ¡Genial! Suena como una forma divertida de hacer una fiesta de presentación.
    - **Party Pete:** ¡Exactamente! Sin embargo, una palabra de advertencia. Cualquier elemento que coloques en el cofre no se puede volver a sacar y cuesta 1000 piezas de oro por cada grupo de entrega.
  - ¡Quiero fiesta!
    - **Player:** ¡Quiero festejar!
    - **Party Pete:** ¡He ganado el Trofeo de Danza en el Kandarin Ball durante tres años seguidos!
    - **Player:** ¡Muéstrame tus movimientos, Pete!
  - Más.
    - ¡Me encanta tu cabello!
      - **Player:** ¡Me encanta tu cabello!
      - **Party Pete:** ¿No es genial? Me gustó tanto que hice extras para los asistentes a mi fiesta. ¿Quieres comprar uno?
      - Seleccione una opción:
        - Sí.
          - (opens=Party Pete's Emporium)
        - No.
          - (end)
    - ¿Por qué hay un camaleón aquí?
      - **Player:** ¿Por qué hay un camaleón aquí?
      - **Party Pete:** Karma es mi mascota. Lo compré para Navidad un año. Mantiene el salón de fiestas libre de moscas y le encanta verme bailar. Karma karma karma cha...
      - {{anchor|karmaoptions}}Seleccione una opción:
        - ¿Puedes hablar con él?
          - **Player:** ¿Puedes hablar con él?
          - **Party Pete:** Claro, hablo con el pequeño todo el tiempo. Mi nivel de Summoning no es lo suficientemente alto como para entender lo que me responde, pero sigue siendo una gran compañía.
          - (previous|karmaoptions)
        - Se acabó la Navidad.
          - **Player:** Se acabó la Navidad. ¿Por qué todavía lo tienes dando vueltas?
          - **Party Pete:** ¡No podía echar al pequeño chappy! ¡Una mascota es para toda la vida!
          - (previous|karmaoptions)
        - Ay, eso es lindo.
          - **Player:** Oh, eso es bueno.
        - ¿Tienes pastel?
          - **Player:** ¿Tienes algún pastel que pueda comer?
          - **Party Pete:** ¡Tenemos todo tipo de delicias geniales para la fiesta!
          - **Player:** ¿Pero tienes pastel? Del tipo que nunca termina.
          - (Condition: With an anniversary celebration active:)
            - (Condition: Without free backpack space:)
              - **Party Pete:** Ah. No tienes suficiente espacio para llevar este pastel.
            - (Condition: With free backpack space:)
              - (Condition: With 25th Anniversary cake already owned:)
                - **Party Pete:** No seas codicioso, hombre, ¡ya tienes algunos! Necesitamos que todos los ciudadanos de Gielinor disfruten de este fantástico pastel.
              - (Condition: With 25th Anniversary cake lost:)
                - (receives=25th Anniversary cake)
                - **Party Pete:** ¡Aquí tienes un pastel del 25 aniversario! ¡Feliz aniversario, hombre!
          - (Condition: Without an anniversary celebration active:)
            - **Party Pete:** Lamentablemente no hay pastel en este momento, intenta regresar el 1 de enero... ¡Pero la fiesta nunca termina!
    - Atrás.
      - *(Vuelve a las opciones anteriores.)*

#### Senderos del tesoro

- **Party Pete:** ¡Has venido al lugar correcto!
- (removes=the old clue scroll (medium))
- ((If the trail continues:))
  - (receives=a new clue scroll (medium))
  - [¡Party Pete te ha dado otro pergamino de pistas!]
- ((If the trail ends:))
  - (receives=reward casket (medium))
  - [¡Has encontrado un ataúd!]

#### Durante el evento de Resoluciones de Año Nuevo

- **Player:** ¡Hola!
- **Party Pete:** ¡Hola! Soy Party Pete. ¡Bienvenidos al Salón de Fiestas!
- Pregunta sobre...
  - Resoluciones de año nuevo
    - **Player:** ¿Qué es todo eso de los propósitos de Año Nuevo?
    - **Party Pete:** Oh, gracias a Dios, después de todas esas lámparas de celebración para el Año Nuevo, ¡estoy de fiesta!
    - **Party Pete:** Así que pensé que este año haría una lista de propósitos de Año Nuevo.
    - Pregunta sobre...
      - ¿Cómo puedo ayudar?
        - **Player:** ¿Cómo puedo ayudar?
        - *(Si no se ha reclamado una lista de resoluciones:)*
          - {{Transcript missing}}
        - *(Si se ha reclamado una lista de resoluciones:)*
          - **Party Pete:** Veo que ya tienes una copia de mi lista de resoluciones, échale un vistazo a la lista y buena suerte amigo, ¡la necesitaremos!
          - **Player:** ¿Qué es todo eso de los propósitos de Año Nuevo?
          - **Party Pete:** Oh, gracias a Dios, después de todas esas lámparas de celebración del Año Nuevo, ¡estoy de fiesta!
          - **Party Pete:** Así que pensé que este año haría una lista de propósitos de Año Nuevo.
          - *(Vuelve a las opciones anteriores.)*
      - Resoluciones de Año Nuevo
        - **Player:** ¿Resoluciones de Año Nuevo?
        - **Party Pete:** Sí, es una tradición. Al comienzo de cada año eliges algunas cosas que hacer.
        - **Party Pete:** ¡Ahora podría ser ponerse en forma, dejar los malos hábitos o probar algo nuevo!
        - **Player:** Genial, gracias, lo investigaré.
        - **Player:** ¿Qué es todo eso de los propósitos de Año Nuevo?
        - **Party Pete:** Oh, gracias a Dios, después de todas esas lámparas de celebración del Año Nuevo, ¡estoy de fiesta!
        - **Party Pete:** Así que pensé que este año haría una lista de propósitos de Año Nuevo.
        - *(Vuelve a las opciones anteriores.)*
      - ¿Bebida desintoxicante?
        - **Player:** ¿Bebida desintoxicante?
        - **Party Pete:** Sí, es mi receta súper secreta.
        - **Party Pete:** Aunque me vendría bien una mano con algunos de los ingredientes.
        - **Player:** ¿Qué necesitas?
        - **Party Pete:** Tengo una lista aquí, échale un vistazo...
        - *(Se abre el libro de ingredientes de la bebida detox.)*
      - Lista de ingredientes
        - **Player:** ¿Puedo ver la lista nuevamente?
        - *(Se abre el libro de ingredientes de la bebida detox.)*
      - tengo algunos ingredientes
        - *(Si hay una poción de reabastecimiento en el inventario y aún se necesita:)*
          - **Player:** Te he traído una poción de reabastecimiento.
          - **Party Pete:** ¡Salud amigo, eso hará que mi bebida desintoxicante sea un poco más refrescante!
          - *(Continúa a continuación.)*
        - *(Si hay un simulacro divino II en el inventario y aún se necesita:)*
          - **Player:** Les he traído un Simulacro Divino II.
          - **Party Pete:** ¡Salud amigo, eso le dará un poco de energía a la bebida desintoxicante!
          - *(Continúa a continuación.)*
        - *(Si hay una geoda de cristal en el inventario y aún se necesita:)*
          - **Player:** Te traje una geoda de cristal.
          - **Party Pete:** ¡Salud amigo, eso le dará un poco de brillo a la bebida desintoxicante!
          - *(Continúa a continuación.)*
        - *(Si hay polvo de 120 armónicos en el inventario y aún se necesita:)*
          - **Player:** Te he traído 120 polvo armónico.
          - **Party Pete:** ¡Salud amigo, eso le dará buenas vibraciones a la bebida desintoxicante!
          - *(Continúa a continuación.)*
        - *(Si hay una pluma de Silverhawk en el inventario y aún se necesita:)*
          - **Player:** Te he traído una pluma Silverhawk.
          - **Party Pete:** ¡Salud amigo, eso le dará un toque especial a la bebida desintoxicante!
          - *(Continúa a continuación.)*
        - *(Si hay una canasta de tomates en el inventario y aún se necesita:)*
          - **Player:** Te he traído una cesta llena de tomates.
          - **Party Pete:** ¡Salud amigo, eso le dará un poco de sabor a la bebida desintoxicante!
          - *(Continúa a continuación.)*
        - *(Si aún faltan ingredientes:)*
          - **Party Pete:** Parece que todavía nos faltan algunos ingredientes, amigo. Corre y ve si puedes conseguirlos.
        - *(Si la tarea ha sido completada:)*
          - **Party Pete:** No necesito más ingredientes ahora amigo.
  - algo mas
    - *(Diálogo sin evento.)*

#### Durante la tarea de celebraciones del 25 Aniversario

- **Party Pete:** ¡Oye, hombre! Ha pasado un tiempo desde que salimos de fiesta. Déjame preparar los globos...
- **Player:** No es necesario, esta es solo una visita rápida para tachar algo de mi lista de tareas.
- **Party Pete:** ¿Seguro que no quieres donar algo al cofre de la fiesta para la próxima Bonanza de Globos?
- {{RSFontAchievement|Party Pete|Talk to Party Pete in the Falador Party Room.}}
- ((Shown in a task completion pop-up:))
  - {{Colour|#F0BE79| TAREA DEL 25 ANIVERSARIO |#181513}}
  - Party Pete
  - Habla con Party Pete en la sala de fiestas Falador.
  - (continue)
- **Party Pete:** No te preocupes si no, amigo. Es todo genial.
- (Condition: If all the tasks have been completed:)
  - **Player:** Parece que he completado todo. ¡Será mejor que vaya a ver a Hans sobre esa recompensa!

### 15th year anniversary party garden

- **Player:** ¡Oye!
- **Party Pete:** ¡Hola! Soy Party Pete. ¡Bienvenidos al jardín del 15º Aniversario!
- Entonces, ¿qué está pasando aquí?
  - **Party Pete:** ¡Es una fiesta! ¡RuneScape ha llegado a los 15 grandes, así que le organizaré una fiesta de cumpleaños que nadie olvidará!
  - **Player:** ¿Incluso si se dejan llevar demasiado por el espíritu de fiesta?
  - **Party Pete:** Incluso entonces. ¡Esta es una fiesta para todas las edades!
- ¿Para qué sirven los zócalos?
  - *Si el player no ha recogido ninguna de las estatuas*
    - **Party Pete:** Están listos para sostener estatuas que celebran cada uno de los quince años de RuneScape. El jardín lucirá increíble cuando los tengas todos. Se pueden encontrar en los lanzamientos de globos o buscando portales especiales en todo el mundo. ¡Cuando encuentres un portal, echa un vistazo y es posible que tengas una estatua! Se entregará directamente en el pedestal correcto, así que cuando encuentres uno, ¡asegúrate de volver aquí y comprobarlo!
  - *Si el player ha recogido todas las estatuas*
    - **Party Pete:** ¡Se ven geniales con todas tus estatuas encima! Tómate un tiempo para echarles un vistazo y apreciar realmente su esplendor.
- Cuéntame más sobre el beneficio.
  - **Party Pete:** El espíritu de fiesta es contagioso. Simplemente come algo de comida de las mesas o come un poco del pastel, ¡y eso también te dará el espíritu de fiesta! Es un beneficio del 5% para todas las habilidades que hagas en el área del grupo durante las siguientes 24 horas. ¡Simplemente haz clic nuevamente después de que transcurran las 24 horas para reactivar el bono!
  - **Player:** ¡Ciertamente parece haber funcionado contigo!
  - **Party Pete:** Sí. Genial, ¿no?
- ¿Hay alguna recompensa?
  - **Party Pete:** ¡Hay muchas recompensas fantásticas para acompañar las celebraciones! ¡Explota 15 globos para obtener un toque elegante y 50 globos para un regalo que irá con fuerza! Obtén el beneficio del espíritu de fiesta al comer en las mesas de la fiesta y desbloquea otro regalo, ¡esta vez uno sabroso!
  - **Player:** ¡Todo eso suena bien! ¿Algo más?
  - **Party Pete:** Coleccionar estatuas también te otorga recompensas especiales cuando hayas recolectado 4, 8, 12 y 15. ¡Esté atento a los mensajes de desbloqueo especiales! Además, puedes obtener cosas interesantes de los globos, como fragmentos de sombreros de fiesta, estrellas, lámparas y oro, ¡y la posibilidad de desbloquear una estatua!
- ¿Cuánto dura esta fiesta?
  - **Party Pete:** No todo el mundo tiene la misma energía para la fiesta que yo, pero estaremos de fiesta hasta finales de enero. Sin embargo, los portales de las estatuas se pueden encontrar hasta fin de año, ¡así que sigue buscando!
- ¿Cómo funcionan las caídas de globos?
  - **Party Pete:** ¡Hice todo lo posible con los globos para esto! Son cada media hora y están en todos los lodestone excepto Prifddinas. ¡Solo busca los anuncios y el confeti, y luego acércate y sal! Puedes hacer estallar 50 globos al día y hay cosas maravillosas que encontrar dentro de ellos, como fragmentos de sombreros de fiesta, estrellas y lámparas. Además, si obtienes 50, ¡obtendrás una recompensa especial!
- Adiós.
  - **Party Pete:** ¡Nos vemos luego, caimán!

### RuneFest Treasure Island


#### Conversación 1

- **Player:** Me alegro de verte por aquí Pete, ¿cómo van las cosas?
- **Party Pete:** He visto a mucha gente lucir un peinado nuevo y genial.
- **Party Pete:** Lo intentaría yo mismo, ¡pero no podía soportar perder el afro!

#### Conversación 2

- **Player:** Me alegro de verte por aquí Pete, ¿cómo van las cosas?
- **Party Pete:** Nada mal, nada mal. Me estoy poniendo manos a la obra para celebrar RuneFest y, como estoy seguro de que ya sabes, ¡la fiesta es una de mis especialidades!
- **Player:** Supongo que no sabes lo que puedo hacer aquí.
- **Party Pete:** Bueno, RuneFest no se lleva a cabo todo el año, ¡pero siempre es genial relajarse con algunos de los tipos geniales con los que compartiste la experiencia allí!

#### Conversación 3

- **Player:** Me alegro de verte por aquí Pete, ¿cómo van las cosas?
- **Party Pete:** ¡Un tipo bastante radical! Aunque, de vez en cuando este dragón viene detrás de mí, ahora tengo el control de la situación. ¡Cada vez que me ataca termino domando a the beast y festejando como ningún hombre lo ha hecho antes! Así que si no estoy aquí de fiesta ya sabes dónde estoy.
