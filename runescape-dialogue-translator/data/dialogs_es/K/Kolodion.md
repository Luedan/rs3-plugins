# Kolodion

- **Original Wiki Page**: [Transcript:Kolodion](https://runescape.wiki/w/Transcript%3AKolodion)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- [Menu]: Selecciona una opción
  - [Choice]: Sistema de tareas
    - [Menu]: Elige una opción:
      - [Choice]: Cuéntame sobre el sistema de tareas.
        - **Kolodion:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
        - **Kolodion:** Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
        - **Kolodion:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
        - [Menu]: Elige una opción:
          - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
            - **Kolodion:** Por completar el conjunto Wilderness, se te presenta la espada Wilderness.
            - **Kolodion:** Esta espada será cada vez más útil con cada nivel de dificultad del conjunto que completes.
            - **Kolodion:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
            - También puede seleccionar una tarea determinada (indicada en la interfaz principal del sistema de tareas mediante un pequeño icono de escudo) y elegir 'Recompensas' para ver qué recompensas proporciona un elemento determinado.
            - (previous2)
          - [Choice]: ¿Cómo reclamo estas recompensas?
            - **Kolodion:** Debes completar todas las tareas del conjunto de una dificultad particular y luego podrás reclamar tu recompensa. La mayoría de las tareas del conjunto Wilderness son sencillas, aunque es posible que algunas requieran misiones.
            - **Kolodion:** iniciado, si no terminado.
            - **Kolodion:** Para reclamar la recompensa del conjunto Wilderness, habla con Mr Ex, Mandrith, Quercus o conmigo mismo.
            - (previous2)
          - [Choice]: Lo siento, me estaba yendo.
            - (end)
      - [Choice]: ¿Puedo reclamar alguna recompensa de usted?
        - (Condition: Si el player no tiene ninguna recompensa para reclamar:)
          - **Kolodion:** ¡Ya no tienes más recompensas para reclamar!
        - (Condition: Si el player no ha reclamado las recompensas del conjunto de tareas de élite Wilderness:)
          - (Condition: Sin tres espacios backpack libres:)
            - **Kolodion:** Me temo que no tienes suficiente espacio en el inventario para reclamar todas tus recompensas. Hablame de nuevo cuando tengas 3 espacios.
          - (Condition: Sin tres espacios backpack libres:)
            - **Player:** He completado todas las tareas del conjunto de tareas de élite Wilderness.
            - **Kolodion:** Bien hecho Player, he reservado algunas recompensas para ti.
            - Espada (receives=two Antique lamp (Elite Wilderness Tasks) y Wilderness 1)
            - [¡Recibirás algunas recompensas por completar el conjunto de tareas de élite Wilderness!]
            - **Kolodion:** Ahí lo tienes, parece que eso es todo.
        - (Condition: Si el player ha perdido su espada Wilderness 4:)
          - **Player:** Perdí la espada Wilderness 4 que me diste...
          - **Kolodion:** Por suerte para ti, tengo uno de repuesto... Aunque me temo que te va a costar 100.000 coins.
          - [Menu]: ¿Reclamar 100.000 coins?
            - [Choice]: Sí.
              - (Condition: Si el player no tiene suficiente dinero:)
                - No puedes permitirte eso.
                - **Kolodion:** Pero no parece que tengas suficiente dinero para eso. Vuelve conmigo cuando lo hagas.
              - (Condition: Si el player tiene suficiente dinero:)
                - (removes=100,000 coins) (receives=Wilderness sword 4)
                - [Te entregan otra espada Wilderness 4.]
            - [Choice]: No.
              - **Player:** No, gracias.
      - [Choice]: cond=If the player has claimed at least one of the Wilderness task set rewards:|¿Puedo comprar un repuesto de la recompensa?
        - [Menu]: Elige una opción:
          - [Choice]: Wilderness espada 1
            - **Kolodion:** Wilderness espada 1? Sí, pero me temo que te costaría 50.000 coins.
            - [Menu]: ¿Comprar otro por 50.000 coins?
              - [Choice]: si
                - (removes=50,000 coins) (receives=Wilderness sword 1)
                - [Te entregan otra espada Wilderness 1.]
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: Wilderness espada 2
            - **Kolodion:** Wilderness espada 2? Sí, pero me temo que te costaría 65.000 coins.
            - [Menu]: ¿Comprar otro por 65.000 coins?
              - [Choice]: si
                - (removes=65,000 coins) (receives=Wilderness sword 2)
                - [Te entregan otra espada Wilderness 2.]
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: Wilderness espada 3
            - **Kolodion:** Wilderness espada 3? Sí, pero me temo que te costaría 80.000 coins.
            - [Menu]: ¿Comprar otro por 80.000 coins?
              - [Choice]: si
                - (removes=80,000 coins) (receives=Wilderness sword 3)
                - [Te entregan otra espada Wilderness 3.]
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: Wilderness espada 4
            - **Kolodion:** Wilderness espada 4? Sí, pero me temo que te costaría 100.000 coins.
            - [Menu]: ¿Comprar otro por 100.000 coins?
              - [Choice]: si
                - (removes=100,000 coins) (receives=Wilderness sword 4)
                - [Te entregan otra espada Wilderness 4.]
              - [Choice]: No
                - **Player:** No, gracias.
      - [Choice]: Lo siento, me estaba yendo.
        - (end)
  - [Choice]: algo mas
    - (abajo)

#### Jugadores con magia inferior al nivel 60

- [Menu]: Selecciona una opción
  - [Choice]: Sistema de tareas
    - (above|tasks)
  - [Choice]: algo mas
    - **Player:** Hola. ¿Qué es este lugar?
    - **Kolodion:** No me hagas perder el tiempo con preguntas triviales. Soy el Gran Kolodion, maestro de la magia de batalla. Tengo una arena para correr.
    - **Player:** ¿Puedo participar?
    - **Kolodion:** ¡Ja! ¿Un mago de tu nivel? No seas absurdo.

#### Jugadores con magia superior al nivel 60

- [Menu]: Selecciona una opción
  - [Choice]: Sistema de tareas
    - (above|tasks)
  - [Choice]: algo mas
    - **Player:** Hola. ¿Qué es este lugar?
    - **Kolodion:** Soy el gran Kolodion, maestro de la magia de batalla, y este es mi campo de batalla. Los mejores magos viajan desde todo Gielinor para luchar aquí.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Puedo pelear aquí?
        - **Player:** ¿Puedo pelear aquí?
        - **Kolodion:** Mi campo está abierto a cualquier mago de alto nivel, pero esto no es un juego. Muchos magos caen en esta arena y nunca más vuelven a levantarse. Los magos más fuertes han sido destruidos.
        - **Kolodion:** ¿Estás seguro de que quieres participar?
        - (continue|join)
      - [Choice]: ¿Cuál es el punto de eso?
        - **Player:** ¿Cuál es el punto de eso?
        - **Player:** Aprendemos cómo usar nuestra magia al máximo y cómo canalizar las fuerzas del cosmos en nuestro mundo...
        - **Player:** Pero principalmente, me gusta convertir a la gente en polvo.
        - (otro)
      - [Choice]: ¡Eso es bárbaro!
        - **Player:** ¡Eso es bárbaro!
        - **Kolodion:** No, es mágico. Pero sé lo que quieres decir. ¿Quieres unirte a nosotros?
        - (continue|join)
    - {{anchor|join}}[Menú]: Seleccione una opción
      - [Choice]: Sí, de hecho.
        - **Player:** Sí, de hecho.
        - **Kolodion:** Bien, bien. Tienes un sano sentido de competencia.
        - **Kolodion:** Recuerda, viajero: en mi arena, el combate cuerpo a cuerpo es inútil. Tu fuerza disminuirá a medida que entres a la arena, pero los hechizos que puedes aprender se encuentran entre los más poderosos de todo Gielinor.
        - **Kolodion:** Antes de que pueda aceptarte, debemos batirnos en duelo.
        - [Menu]: Selecciona una opción
          - [Choice]: Está bien, peleemos.
            - **Player:{{anchor|lets-fight}}** Está bien, peleemos.
            - **Kolodion:** Primero debo comprobar que estás a la altura.
            - **Player:** No necesitas preocuparte por eso.
            - **Kolodion:** No cualquier mago puede entrar, solo los más poderosos y temidos. Antes de que puedas usar el poder de esta arena, debes probar tu valía contra mí.
            - (Action: Kolodion se teletransporta a sí mismo y a el player al Mage Arena.)
            - (continue|Battling him at the Mage Arena)
          - [Choice]: No gracias.
            - **Player:** No, gracias.
      - [Choice]: No, no lo hago.
        - **Player:** No, no lo sé.
        - **Kolodion:** Tú te lo pierdes.

### If the player fled a fight

- [Menu]: Selecciona una opción
  - [Choice]: Sistema de tareas
    - (above|tasks)
  - [Choice]: algo mas
    - (continuea|lets-fight)

### Battling him at the Mage Arena


#### Primera forma

- **Kolodion:** {{RSChat|You must prove yourself... now!}}

#### Segunda forma

- (Action: Kolodion se transforma en un ogro.)
- **Kolodion:** {{RSChat|This is only the beginning; you can't beat me!}}

#### Tercera forma

- (Action: Kolodion se transforma en un troll.)
- **Kolodion:** {{RSChat|Foolish mortal; I am unstoppable.}}

#### Cuarto curso

- (Action: Kolodion se transforma en una bestia oscura.)
- **Kolodion:** {{RSChat|Now you feel it... The dark energy}}

#### Forma final

- (Action: Kolodion se transforma en un demonio negro.)
- **Kolodion:** {{RSChat|Aaaaaaaarrgghhhh! The power!}}

#### Derrotándolo

- (Action: Kolodion se transforma nuevamente en humano y se teletransporta a sí mismo y a el player al banco Mage Arena.)
- **Kolodion:** Bien hecho, joven aventurero; Realmente eres un digno mago de batalla.
- **Player:** ¿Y ahora qué?
- **Kolodion:{{anchor|step-into-pool}}** Entra en la piscina mágica. Te llevará a una cámara. Allí deberás decidir a qué dios representarás en la arena.
- **Player:** Gracias, Kolodion.
- **Kolodion:** Para eso estoy aquí.

### Talking to him after defeating him and without having chosen a god to represent

- [Menu]: Selecciona una opción
  - [Choice]: Sistema de tareas
    - (above|tasks)
  - [Choice]: algo mas
    - **Player:** Hola, Kolodion.
    - **Kolodion:** Hola, joven mago. Eres una persona dura.
    - **Player:** ¿Y ahora qué?
    - (continuea|step-into-pool)

### Talking to him after having chosen a god to represent

- [Menu]: Selecciona una opción
  - [Choice]: Sistema de tareas
    - (above|tasks)
  - [Choice]: algo mas
    - **Player:** Hola, Kolodion.
    - **Kolodion:** Hola, ¿cómo estás? ¿Estás disfrutando del derramamiento de sangre?
    - **Player:** Creo que ya he tenido suficiente por ahora.
    - **Kolodion:**Una pena. Eres un buen mago de batalla. Espero verte pronto.
