# Redbeard Frank

- **Original Wiki Page**: [Transcript:Redbeard Frank](https://runescape.wiki/w/Transcript%3ARedbeard%20Frank)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Redbeard Frank:** ¡Arriba, amigo!
- **Seleccione una opción**
  - [Choice]: cond=Before Pirate's Treasure|Estoy en busca de un tesoro.
    - (ver|El tesoro de Pirate)
  - [Choice]: ¡Arriba!
    - **Player:** ¡Arriba!
    - **Redbeard Frank:** ¡Arr!
    - (initial)
  - [Choice]: ¿Tienes algo para intercambiar?
    - **Player:** ¿Tienes algo para intercambiar?
    - **Redbeard Frank:** Nada por el momento, pero claro, los agentes de aduanas están en pie de guerra en este momento.
  - [Choice]: cond=After Pieces of Hate|Habla de Piezas de Odio
    - **Redbeard Frank:** ¿De verdad me dejaste fuera de todo eso?
    - **Redbeard Frank:** ¿No estabas pensando que me hubiera gustado poner mi cuchillo en la garganta de Rabid Jack?
    - **Elige una opción:**
      - [Choice]: Lo siento, lo olvidé.
        - **Redbeard Frank:** Sí, me han olvidado de muchas cosas estos días.
        - (continue|grudge)
      - [Choice]: Ya teníamos suficiente gente.
        - **Redbeard Frank:** Bah, la primera regla para ser un pirata es llevar siempre más de lo que necesitas.
        - (continue|grudge)
      - [Choice]: ¡No fue mi culpa!
        - **Redbeard Frank:** Sí, pero no dijiste nada al respecto, ¿verdad?
        - **Player:** Quiero decir, literalmente no tuve otra opción.
        - **Redbeard Frank:** ¡Bah!
        - (continue|grudge)
      - [Choice]: Culpar al cuervo
        - **Redbeard Frank:** ¿Qué crees que soy? ¿Un idiota? ¡Si lo culpo, me pondrá en su lista!
        - **Player:** ¡Oh dioses!
        - **Redbeard Frank:** ¡Soy demasiado pelirrojo para morir!
        - {{anchor|grudge}}**Redbeard Frank:** Arrr, pero no tiene sentido guardar rencor por esto.
        - **Redbeard Frank:** ¿Fue al menos una batalla gloriosa?
        - **Player:** Fue muy extraño, había 'ron' involucrado y gatitos por todos lados.
        - **Redbeard Frank:** ¿Gatitos?
        - **Player:** Sí, tampoco estoy seguro de entenderlo.
        - **Redbeard Frank:** Cuentos realmente extraños.
        - **Redbeard Frank:** Continúa, vete. Tengo que dedicarme a la piratería.
        - **Player:** Nos vemos cerca, capitán.
  - [Choice]: Acerca del sistema de tareas...
    - (below|Task System)

### Task System

- (Condition: Si se completaron los logros de Easy Falador y no se reclamaron las recompensas:)
  - **Player:** He venido por mi recompensa.
  - **Redbeard Frank:** Entonces, ya terminaste, ¡bien hecho! Creo que las felicitaciones son necesarias.
  - **Player:** Creo que las recompensas están en orden.
  - **Redbeard Frank:** Tienes razón.
  - (receives=Falador shield 1 and Antique lamp (Easy Falador Tasks))
  - **Redbeard Frank:** Esta es la primera etapa del escudo Falador: un escudo. Te otorga acceso a la capacidad de restauración de Prayer y a un emote.
  - **Redbeard Frank:**Cada una de estas funciones se puede activar mientras se empuña el escudo. La restauración de Prayer también se puede activar desde su inventario.
  - **Redbeard Frank:** La capacidad de restauración de Prayer solo se puede usar una vez al día y te devuelve una cuarta parte de tus puntos Prayer.
  - **Redbeard Frank:** Además de todas estas características, el escudo es bastante útil en combate y te brinda un pequeño impulso de Prayer.
  - **Redbeard Frank:** Incluso agregué un poco del botín que encontré en mis viajes.
  - **Player:** ¡Vaya, gracias!
  - **Redbeard Frank:** Si pierdes tu escudo, regresa y busca otro.
  - (continue)
- (Condition: Si el player ha perdido su escudo Falador 1:)
  - **Player:** He perdido mi escudo.
  - **Redbeard Frank:** ¿Qué? ¡Ese era un equipo valioso!
  - **Redbeard Frank:** Por suerte, tengo uno de repuesto. Cuídalo mejor esta vez.
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: Háblame del Sistema de Logros.
    - **Redbeard Frank:** ¡Arr! El Sistema de Logros será una gran cantidad de desafíos que enfrentar mientras viajas por el mundo.
    - **Redbeard Frank:** Puedes ganar botín al completar ciertos logros, ya sea botín o piezas de ocho, que puedes obtener de Explorer Jack en Lumbridge.
    - **Redbeard Frank:** La mayoría de ellos, si haces lo suficiente en un área, obtienes un objeto poderoso que puedes reclamar de alguien en el área, como yo.
    - [Menu]: Elige una opción:
      - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
        - **Player:** Cuéntame sobre la recompensa establecida para esta área.
        - **Redbeard Frank:** Tu recompensa aquí en Falador será un escudo, un compañero y uno mejor cada vez que termines un nivel de dificultad.
        - **Redbeard Frank:** Te informaremos qué hace cuando te lo entreguemos.
        - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
        - (previous)
      - [Choice]: ¿Cómo reclamo estas recompensas?
        - **Player:** ¿Cómo reclamo las recompensas?
        - **Redbeard Frank:** Debes completar todas las tareas en un conjunto de una dificultad particular, luego podrás reclamar tu recompensa.
        - **Redbeard Frank:** Algunas de las tareas del conjunto Falador son simples, algunas requerirán cierto skill levels y otras pueden requerir que se inicien o completen misiones.
        - **Redbeard Frank:** Para reclamar las recompensas del conjunto Falador, charlar con el químico de Rimmington, el escudero de Sir Vyvin en el Castillo de los Caballeros Blancos o conmigo mismo.
        - (previous)
      - [Choice]: Lo siento, me estaba yendo.
        - (end)
  - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
    - [Menu]: Elige una opción:
      - [Choice]: Escudo Falador 1
        - **Redbeard Frank:** ¿Escudo Falador 1? Sí, pero me temo que te costaría 1.500 coins.
        - [Menu]: ¿Comprar otro por 1.500 coins?
          - [Choice]: si
            - (receives=Falador shield 1) (removes=1,500 coins)
            - [Te entregan otro escudo Falador 1.]
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Escudo Falador 2
        - **Redbeard Frank:** ¿Escudo Falador 2? Sí, pero me temo que te costaría 2500 coins.
        - [Menu]: ¿Comprar otro por 2500 coins?
          - [Choice]: si
            - (receives=Falador shield 2) (removes=2,500 coins)
            - [Te entregan otro escudo Falador 2.]
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Escudo Falador 3
        - **Redbeard Frank:** ¿Escudo Falador 3? Sí, pero me temo que te costaría 7.500 coins.
        - [Menu]: ¿Comprar otro por 7.500 coins?
          - [Choice]: si
            - (receives=Falador shield 3) (removes=7,500 coins)
            - [Te entregan otro escudo Falador 3.]
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Escudo Falador 4
        - **Redbeard Frank:** ¿Escudo Falador 4? Sí, pero me temo que te costaría 15.000 coins.
        - [Menu]: ¿Comprar otro por 15.000 coins?
          - [Choice]: si
            - (receives=Falador shield 4) (removes=15,000 coins)
            - [Te entregan otro escudo Falador 4.]
          - [Choice]: No
            - **Player:** No, gracias.
  - [Choice]: Lo siento, me estaba yendo.
    - (end)

### During the first Frank's Free Chest event


#### Usando llaves en el cofre

- (ver|Cofre libre de Frank (paisaje)#Con llaves)

#### Habla con

- **Redbeard Frank:** ¡Arriba, amigo!
- ((Sólo la primera vez durante el evento:))
  - **Player:** ¡Arréglate! Di Frank, ¿qué pasa con ese cofre de ahí?
  - **Redbeard Frank:** Ese será un cofre del tesoro de Héctor el Tuerto, mi viejo capitán.
  - **Redbeard Frank:** Recientemente se lavó y considerando todas las celebraciones y regalos de los últimos tiempos, pensé en entregar sus riquezas a la gente de Gielinor.
  - **Redbeard Frank:** Ya sabes, para corregir algunos errores del pasado y cosas así.
  - **Player:** ¡Eso es genial! ¿Puedo tener algunos?
  - **Redbeard Frank:** Arr, bueno, ya sabes...
  - **Redbeard Frank:** ...Puede que no tenga la clave.
  - **Redbeard Frank:** ¡Pero ahí es donde entras tú! Por cada 4 llaves de pirata que me traigas, te daré un tesoro una vez que esté abierto el cofre.
  - **Redbeard Frank:** Hasta el 31 de enero, podrás encontrar las llaves todos los días cuando llegues a Gielinor y cada hora mientras estés fuera de casa.
  - **Redbeard Frank:** Sin embargo, creo que no encontrarás más de 12 llaves por semana.
  - **Redbeard Frank:** La semana de un pirata siempre comienza el miércoles, así que es cuando seguramente aparecerán más llaves de piratas.
  - **Player:** ¡Suena como un trato! ¿Pero qué pasa si la llave de montaje se está oxidando en el fondo del mar?
  - **Redbeard Frank:** Arr, eso es bastante probable. Esperaba evitar arrastrar la memoria de Héctor de esta manera, pero...
  - **Redbeard Frank:** ...si todavía está cerrado el 1 de febrero, lo abriré de golpe.
  - **Player:** Muy bien.
  - **Redbeard Frank:** De cualquier manera, si vienes a verme una vez que el cofre esté abierto, esperaré otras cuatro semanas para que reclames tu parte, hasta el 28 de febrero.
  - (continue)
- **Seleccione una opción**
  - Estoy en busca de un tesoro.
    - (arriba)
  - ¡Arriba!
    - (arriba)
  - ¿Tienes algo para intercambiar?
    - (arriba)
  - Habla de Piezas de Odio
    - (arriba)
  - Habla sobre el cofre gratuito de Frank
    - **Redbeard Frank:** Ese será un cofre del tesoro de Héctor el Tuerto, mi viejo capitán.
    - ((Con el cofre cerrado:))
      - **Redbeard Frank:** Por cada 4 llaves de pirata que me traigas, te daré un tesoro una vez que el cofre esté abierto.
      - **Redbeard Frank:** Podrás encontrar las llaves todos los días cuando llegues a Gielinor y cada hora mientras estés fuera de casa.
      - **Redbeard Frank:** Sin embargo, creo que no encontrarás más de 12 llaves por semana.
      - **Redbeard Frank:** La semana de un pirata siempre comienza el miércoles, así que ahí es cuando podrás encontrar más llaves.
      - **Redbeard Frank:** Podéis traerme las llaves hasta el 31 de enero.
      - **Redbeard Frank:** Después de eso, esperaré hasta el 28 de febrero para que reclames tu parte.
    - ((Con el cofre abierto:))
      - **Redbeard Frank:** Actualmente estoy repartiendo sus riquezas a la gente de Gielinor.
      - **Redbeard Frank:** ¡Continúa y toma tu parte!
  - Acerca del sistema de tareas...
    - (above|Task System)

### During the second Frank's Free Chest event


#### Habla con

- **Redbeard Frank:** ¡Arriba, amigo!
- ((Sólo la primera vez durante el evento:))
  - **Player:** ¡Llega ahí! ¿Veo que has sacado otro cofre de las profundidades del mar?
  - **Redbeard Frank:** ¡Sí! El húmedo tesoro de Héctor está resultando bastante lucrativo.
  - ((Sólo hasta que se abra el cofre:))
    - **Player:** ¡Es genial escucharlo! ¿Alguna posibilidad de volver a conseguir algo de botín a cambio de llaves?
    - **Player:** Espero que no haya sapos ahí esta vez...
    - **Redbeard Frank:** ¡De hecho, encontré la clave de este yo mismo!
    - **Redbeard Frank:** Le eché un vistazo antes. ¡Muchos atuendos piratas y mascotas, objetos poderosos y ni un solo sapo!
    - **Player:** ¿Pero cómo puedo ganar algo de botín si no necesitas que te traiga las llaves?
    - **Redbeard Frank:** ¡Puedes pagarme por ello, en trozos de ocho!
    - **Redbeard Frank:** Hasta finales del 2 de mayo, podrás encontrarlos todos los días cuando llegues a Gielinor, y cada hora mientras estés fuera.
    - **Redbeard Frank:** Habrá un límite de 16 por semana, que se reinicia todos los miércoles.
    - **Redbeard Frank:** Por cada 4 bits de ocho que me traigas, te reservaré un tesoro.
    - **Redbeard Frank:** Cada 8 bits de ocho, esa pieza será de un grupo especial.
    - **Redbeard Frank:** ¡Eso significa que aproximadamente la mitad de tu botín será botín pirata y objetos poderosos!
    - **Redbeard Frank:** Además de eso, le he ordenado a mi tripulación que les entregue un botín pirata adicional por cada 16 bits de ocho que encuentren.
    - **Redbeard Frank:** Cada botín pirata tiene un botín de este cofre, así como un título y algo de ropa digna de un pirata.
    - **Redbeard Frank:** Puedes venir a reclamar el botín ganado desde el 3 de mayo hasta el final del 31 de mayo.
  - ((Sólo después de abrir el cofre:))
    - **Redbeard Frank:** {{Transcript missing|}} piezas de a ocho.
  - (continue)
- **Seleccione una opción**
  - Estoy en busca de un tesoro.
    - (arriba)
  - ¡Arriba!
    - (arriba)
  - ¿Tienes algo para intercambiar?
    - (arriba)
  - Habla de Piezas de Odio
    - (arriba)
  - Acerca del cofre gratuito de Frank
    - ((Con el cofre cerrado:))
      - **SELECCIONA UNA OPCIÓN**
        - Acerca de Bits de ocho
          - **Redbeard Frank:** Dado que mis reservas de ron se están agotando rápidamente, esta vez repartiré botín a cambio de trozos de ocho.
          - **Redbeard Frank:** Hasta finales del 2 de mayo, podrás encontrarlos todos los días cuando llegues a Gielinor, y cada hora mientras estés fuera.
          - **Redbeard Frank:** Habrá un límite de 16 por semana, que se reinicia todos los miércoles.
          - (previous)
        - Acerca del botín del cofre
          - **Redbeard Frank:** Por cada 4 bits de ocho que me traigas, te reservaré un tesoro.
          - **Redbeard Frank:** Cada 8 bits de ocho, esa pieza será de un grupo especial.
          - **Redbeard Frank:** ¡Eso significa que aproximadamente la mitad de tu botín será botín pirata y objetos poderosos!
          - **Redbeard Frank:** Puedes venir a reclamar el botín ganado desde el 3 de mayo hasta el final del 31 de mayo.
          - (previous)
        - Acerca del saqueo de Pirate
          - **Redbeard Frank:** Le he ordenado a mi tripulación que les entregue un botín pirata adicional por cada 16 bits de ocho que encuentren.
          - **Redbeard Frank:** Cada botín pirata tiene un botín de este cofre, así como un título y algo de ropa digna de un pirata.
          - (previous)
    - ((Con el cofre abierto:))
      - **Redbeard Frank:** Si tienes suficientes piezas de ocho, ahora puedes reclamar una parte del botín.
      - **Redbeard Frank:** Será un tesoro por cada 4 bits de ocho. ¡Aproximadamente la mitad del tesoro son vestimentas piratas, mascotas o objetos poderosos!
  - Acerca del sistema de tareas...
    - (above|Task System)
