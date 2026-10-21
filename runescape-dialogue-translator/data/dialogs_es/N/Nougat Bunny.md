# Nougat Bunny

- **Original Wiki Page**: [Transcript:Nougat Bunny](https://runescape.wiki/w/Transcript%3ANougat%20Bunny)
- **Letter**: `N`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Normalmente


##### Sin recompensas para reclamar


##### Sin la primera búsqueda de huevos de madriguera floreciente en progreso

- **Nougat Bunny:** ¡Hola, Player! ¿Sabías que estás hablando con el nuevo supervisor de búsqueda de huevos del tío para este año?
- (Condition: Sin haber participado en Blooming Burrow Egg Hunts antes de este año:)
  - **Player:** ¿Búsqueda de huevos? ¿¡Hay una búsqueda de huevos este año!?
  - **Nougat Bunny:** ¡Esta no es una búsqueda de huevos cualquiera, es la búsqueda de los huevos de oro! He organizado tres búsquedas de huevos diferentes para que los aventureros las realicen este año.
  - **Nougat Bunny:** Pero no estoy seguro de que estés listo para abordar los tres todavía.
  - **Nougat Bunny:** ¡Tendrás que demostrar tu destreza en la búsqueda de huevos completando primero una búsqueda de huevos en Blooming Burrow!
  - **Player:** Esto suena interesante, ¿podrías hablarme entonces de la búsqueda de huevos de Blooming Burrow?
  - (continue|The Blooming Burrow egg hunt)
- (Condition: Por primera vez en el año habiendo participado en Blooming Burrow Egg Hunts durante años anteriores:)
  - **Player:** ¿¡La búsqueda de huevos ha vuelto este año!?
  - **Nougat Bunny:** ¡Seguro que lo son! Tendrás que demostrar que tus habilidades para buscar huevos aún son buenas completando primero la búsqueda de huevos de Blooming Burrow, pero luego estarás listo para afrontar las otras cacerías de este año.
  - **Player:** ¿Entonces podrías recordarme sobre la búsqueda de huevos de Blooming Burrow?
  - (continue|The Blooming Burrow egg hunt)
- [Menu]: Elige una opción:
  - [Choice]: Habla sobre la búsqueda de huevos de Blooming Burrow.
    - **Nougat Bunny:** La búsqueda de huevos de Blooming Burrow se lleva a cabo aquí mismo, donde esconderé un lote de huevos dorados alrededor de la madriguera para que los encuentres.
    - **Nougat Bunny:** Cada día, si puedes encontrar los 12 huevos escondidos y traérmelos...
    - **Nougat Bunny:** ¡Entonces te daré un premio especial aprobado por buscadores de huevos!
    - (Condition: Sin haber participado en Blooming Burrow Egg Hunts este año:)
      - **Nougat Bunny:** Acabo de terminar de ocultar el lote de hoy, así que echa un vistazo a tu alrededor y trata de encontrarlos todos.
    - (Condition: Habiendo participado en Blooming Burrow Egg Hunts:)
      - (Condition: Sin haber participado hoy en una Búsqueda de Huevos de Madriguera Floreciente:)
        - **Nougat Bunny:** He escondido otro juego de huevos para que los encuentres hoy en la madriguera, ¡buena suerte!
        - (Condition: Si preguntas sobre la búsqueda de huevos de Blooming Burrow:)
          - (previous)
      - (Condition: Con la búsqueda de huevos de Blooming Burrow de hoy iniciada pero sin haber encontrado todos los huevos de oro:)
        - **Nougat Bunny:** Parece que ya estás en medio de una búsqueda de huevos en una madriguera. ¡Buena suerte para encontrar el resto de los huevos!
        - Huevos encontrados: [número]/12
        - (previous)
      - (Condition: Habiendo encontrado todos los huevos de oro para la búsqueda de huevos de Blooming Burrow de hoy:)
        - (continue|With rewards to claim)
      - (Condition: Habiendo reclamado recompensas por la búsqueda de huevos de Blooming Burrow de hoy:)
        - **Nougat Bunny:** Ya has completado la búsqueda de hoy. Vuelve mañana y habré escondido un nuevo lote de huevos para que los encuentres.
  - [Choice]: Hable sobre la búsqueda de huevos de Gielinor.
    - **Nougat Bunny:** Para mantenerte ocupado durante las celebraciones de Pascua, ¡he escondido un montón de huevos de oro por todo Gielinor!
    - **Nougat Bunny:** Para ayudarte a orientarte en su dirección, he elaborado un libro de pistas.
    - **Nougat Bunny:** Ganarás fichas de primavera por cualquiera de estos huevos de oro que podrás encontrar en Gielinor.
    - (Condition: Sin haber completado una Búsqueda de Huevos de Madriguera Floreciente:)
      - **Nougat Bunny:** Pero no le daré libros de pistas a cualquiera. ¡Tendrás que demostrar tu destreza en la búsqueda de huevos completando primero una búsqueda de huevos en Blooming Burrow!
      - (continue)
    - (Condition: Habiendo completado una búsqueda de huevos de Blooming Burrow con la segunda búsqueda de huevos Gielinor bloqueada después del inicio del segundo lunes del evento:)
      - Agrega las pistas adicionales a su libro de pistas de búsqueda de huevos.
      - (ventana emergente)
        - (Ventana emergente: agregas las pistas adicionales a tu libro de pistas de búsqueda de huevos.|color=#00FF00)
        - (continue)
      - **Nougat Bunny:** La segunda semana de huevos para la búsqueda de huevos de Gielinor ya están listos para encontrarlos, aquí están sus pistas. ¡Toda la suerte!
      - (continue)
    - (Condition: Habiendo completado una búsqueda de huevos en Blooming Burrow con la tercera búsqueda de huevos Gielinor bloqueada después del inicio del tercer lunes del evento:)
      - Agrega las pistas adicionales a su libro de pistas de búsqueda de huevos.
      - (ventana emergente)
        - (Ventana emergente: agregas las pistas adicionales a tu libro de pistas de búsqueda de huevos.|color=#00FF00)
        - (continue)
      - **Nougat Bunny:** La tercera semana de huevos para la búsqueda de huevos de Gielinor ya están listos para encontrarlos, aquí están tus pistas. ¡Toda la suerte!
      - (continue)
    - (previous)
  - [Choice]: cond=Having lost the egg hunt clue book:|Recupera el libro de pistas de Egg Hunt.
    - **Player:** Nougat, lamentablemente perdí mi libro de pistas para la búsqueda de huevos. ¿Tienes alguno de repuesto?
    - **Nougat Bunny:** No hay necesidad de preocuparse, con tanta actividad en la madriguera este año, hice mucho para todos.
    - (Condition: Sin espacio libre en backpack:)
      - **Nougat Bunny:** Oh, me temo que necesitas al menos 1 espacio backpack libre para tu libro de pistas. Ven y habla conmigo nuevamente cuando tengas espacio.
    - (Condition: Con espacio libre en backpack:)
      - (receives=egg hunt clue book)
      - [Nougat Bunny te entrega un nuevo libro de pistas para la búsqueda de huevos.]
      - **Player:** Gracias, intentaré realizar un seguimiento de este.
      - (previous)
  - [Choice]: Adiós.
    - **Player:** Cuídate, Turrón.
    - **Nougat Bunny:** ¡Tú también! ¡Recuerda estar atento a cualquiera de esos huevos de oro!

##### Con la primera búsqueda de huevos de madrigueras florecientes en progreso

- **Nougat Bunny:** Bienvenido de nuevo, Player. Parece que todavía te quedan algunos huevos por encontrar en la madriguera.
- Huevos encontrados: [número]/12
- **Nougat Bunny:** ¡Ven a hablar conmigo nuevamente una vez que los hayas encontrado todos y compartiré los detalles de las otras búsquedas de huevos!

##### Con recompensas para reclamar

- **Nougat Bunny:** Felicitaciones por encontrar los 12 huevos. Reciba esta recompensa por su esfuerzo con vista de águila.
- (Condition: Cuándo en la primera búsqueda de huevos de Blooming Burrow:)
  - (Condition: Sin dos espacios libres en backpack:)
    - **Nougat Bunny:** Oh, me temo que necesitas al menos 2 espacios backpack para tu libro de recompensas y pistas. Ven y habla conmigo nuevamente cuando tengas espacio.
  - (Condition: Con dos slots libres en backpack:)
    - (Condition: Como jugador gratuito:)
      - (receives=egg hunt clue book and holiday reward casket (free))
      - [Nougat Bunny te entrega un libro de pistas para la búsqueda de huevos y un cofre de recompensa navideña (gratis).]
      - (continue)
    - (Condition: Como miembro:)
      - (receives=egg hunt clue book and holiday reward casket)
      - [Nougat Bunny te entrega un libro de pistas para la búsqueda de huevos y un cofre de recompensa navideña.]
      - (continue)
    - **Nougat Bunny:** Ese es tu propio libro de pistas para la búsqueda de huevos. Ahora que has demostrado ser un experto cazador de huevos, estás listo para emprender la búsqueda de huevos Gielinor.
    - **Nougat Bunny:** La primera semana de huevos está listo para encontrar. No olvides que puedes leer las pistas en tu libro de pistas de búsqueda de huevos. ¡Toda la suerte!
- (Condition: Cuando no estés en la primera búsqueda de huevos de Blooming Burrow:)
  - (Condition: Sin espacio libre en backpack:)
    - **Nougat Bunny:** Oh, me temo que necesitas al menos 1 espacio backpack para tu recompensa. Ven y habla conmigo nuevamente cuando tengas espacio.
    - (above|Choose an option)
  - (Condition: Con un slot libre en backpack:)
    - (Condition: Como jugador gratuito:)
      - (receives=holiday reward casket (free))
      - [Nougat Bunny te entrega un cofre de recompensa navideña (gratis).]
      - (above|Choose an option)
    - (Condition: Como miembro:)
      - (receives=holiday reward casket)
      - [Nougat Bunny te entrega un cofre de recompensa navideña.]
      - Se ha agregado lo siguiente a su bolsa de divisas: 5 x Puntos Treasure Trail.
      - (Condition: Con al menos 30.000 fichas de primavera:)
        - Ha alcanzado el límite flexible del token Spring de 30 000. Debes gastar algunas fichas en la tienda de Gummy antes de poder ganar más.
        - (ventana emergente)
          - (Ventana emergente: has alcanzado el límite flexible de tokens de primavera de 30 000. Debes gastar algunos tokens en la tienda de Gummy antes de poder ganar más.|advertencia=yes)
          - (continue)
      - (Condition: Si estás en la primera búsqueda de huevos de madrigueras florecientes del año:)
        - (receives=egg hunt clue book)
        - **Nougat Bunny:** Ahora que has demostrado que sigues siendo un experto cazador de huevos, estás listo para emprender esta búsqueda de huevos {{Sic|years}} Gielinor. Echa un vistazo a las pistas de este libro y trata de descubrir dónde se escondieron los huevos este año.
        - **Nougat Bunny:** La primera semana de huevos está listo para encontrar. No olvides que puedes preparar las pistas en tu libro de pistas de búsqueda de huevos. ¡Toda la suerte!
        - (continue)
      - (above|Choose an option)

#### Con el título de "el Huevo" antes de haber desbloqueado su variante "Yema"

- **Nougat Bunny:** ¡Ese título te queda bien! ¿Vas a esconderte con los otros huevos?
- ¡Has desbloqueado el color 'Yema' para el título 'El Huevo'!
- ((Repetido en una ventana emergente:))
  - ¡Has desbloqueado el color 'Yema' para el título 'El Huevo'!
  - (continue)
- **Nougat Bunny:** ¡Solo asegúrate de tener cuidado o terminarás revuelto!

### Daily egg hunt


#### Antes de haber reclamado las recompensas de Blooming Burrow Egg Hunt hoy


##### Sin una búsqueda de huevos de madriguera floreciente en curso

- (above|The Blooming Burrow egg hunt quick)

##### Con una búsqueda de huevos de madrigueras florecientes en progreso


##### Antes de haber encontrado todos los huevos de oro

- **Nougat Bunny:** Parece que ya estás en medio de una búsqueda de huevos en una madriguera. ¡Buena suerte para encontrar el resto de los huevos!
- Huevos encontrados: [número]/12

##### Después de haber encontrado todos los huevos de oro

- **Nougat Bunny:** Felicitaciones por encontrar los 12 huevos. Reciba esta recompensa por su esfuerzo con vista de águila.
- (Condition: Cuándo en la primera búsqueda de huevos de Blooming Burrow del año:)
  - (Condition: Sin dos espacios libres en backpack:)
    - **Nougat Bunny:** Oh, me temo que necesitas al menos 2 espacios backpack para tu libro de recompensas y pistas. Ven y habla conmigo nuevamente cuando tengas espacio.
  - (Condition: Con dos slots libres en backpack:)
    - Se ha agregado lo siguiente a su bolsa de divisas: 5 x Puntos Treasure Trail.
    - (receives=egg hunt clue book and holiday reward casket)
    - [Nougat Bunny te entrega un libro de pistas para la búsqueda de huevos y un cofre de recompensa navideña.]
    - **Nougat Bunny:** Ahora que has demostrado que sigues siendo un experto cazador de huevos, estás listo para emprender esta búsqueda de huevos {{Sic|years}} Gielinor. Echa un vistazo a las pistas de este libro y trata de descubrir dónde se escondieron los huevos este año.
    - **Nougat Bunny:** La primera semana de huevos está listo para encontrar. No olvides que puedes leer las pistas en tu libro de pistas de búsqueda de huevos. ¡Toda la suerte!
- (Condition: Cuando no estés en la primera búsqueda de huevos de Blooming Burrow del año:)
  - (Condition: Sin espacio libre en backpack:)
    - **Nougat Bunny:** Oh, me temo que necesitas al menos 1 espacio backpack para tu recompensa. Ven y habla conmigo nuevamente cuando tengas espacio.
  - (Condition: Con un slot libre en backpack:)
    - Se ha agregado lo siguiente a su bolsa de divisas: 5 x Puntos Treasure Trail.
    - (receives=holiday reward casket)
    - [Nougat Bunny te entrega un cofre de recompensa navideña.]

#### Después de haber reclamado las recompensas de Blooming Burrow Egg Hunt hoy

- **Nougat Bunny:** Ya has completado la búsqueda de hoy. Vuelve mañana y habré escondido un nuevo lote de huevos para que los encuentres.

### Overheads (historical)


#### Cada 5 minutos cuando faltan 30 minutos o menos para que comience una búsqueda de huevos comunitaria

- ((Lo siguiente también se muestra como un mensaje general habitual:))
  - {{Colour: {{Colour|#99FF99|The community egg hunt will be starting in [number] minutes!}}}}

#### Comienza la primera búsqueda comunitaria de huevos

- ((Lo siguiente también se muestra como un mensaje general habitual:))
  - {{Colour: {{Colour|#99FF99|The first community egg hunt has now begun. Hop to it everyone!}}}}

#### Comienza la segunda búsqueda de huevos comunitaria

- ((Lo siguiente también se muestra como un mensaje general habitual:))
  - {{Colour: {{Colour|#99FF99|The second community egg hunt is starting now. Good luck everyone!}}}}

### Trade (historical)

- (opens=Egg Hunter's Hoard)
