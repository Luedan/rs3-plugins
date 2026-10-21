# Strange Old Man

- **Original Wiki Page**: [Transcript:Strange Old Man](https://runescape.wiki/w/Transcript%3AStrange%20Old%20Man)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre el sistema de tareas.
    - (abajo2|Sistema de tareas)
  - [Choice]: Habla de otra cosa.
    - (abajo2|Diálogo estándar)

### Standard dialogue


#### Sin pala en backpack

- **Strange Old Man:** ¡Cavar, cavar, CAVAR! ¿Quieres cavar? ¡Necesitas una pala!
- **Player:** Sí, tienes razón, probablemente sí. ¿Dónde puedo conseguir uno?
- **Strange Old Man:** Ohh... Las espadas me han costado muchos problemas: ¡siempre me molestan por ellas! Terminé cediendo y simplemente poniendo uno en cada montículo para que lo usen ustedes, aventureros olvidadizos.

#### Con una pala en backpack

*Nota: Todas estas conversaciones también pueden comenzar con el Strange Old Man diciendo "Excavar, excavar, excavar". primero.*

##### Conversación 1

- **Strange Old Man:{{anchor|argh}}** AAAAAAAAARRRRRRGGGGGHHHHHHHH!
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué pasa?
    - **Player:** ¿Qué pasa?
    - (continuea|argh)
  - [Choice]: Te dejo con eso entonces...
    - **Player:** Entonces te dejo con eso...

##### Conversación 2

- **Strange Old Man:** Pst, ¿quieres escuchar un secreto?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Claro!
    - **Player:** ¡Claro!
    - **Strange Old Man:** ¡No son normales!
  - [Choice]: No gracias.
    - **Player:** No, gracias.

##### Conversación 3

- **Strange Old Man:** Toc, toc.
- **Player:** ¿Quién está ahí?
- **Strange Old Man:** ¡Un gran monstruo aterrador, JAJAJAJAJAJAJAJAJAJAJAJA!
- **Player:** Está bien...

##### Conversación 4

- **Strange Old Man:** ¿Qué? ¡No pedí un libro!
- (receives=Crumbling tome)

### With Jennica's ring equipped

- **Strange Old Man:** El... anillo...Jennica...
- **Player:** ¿Cómo sabes sobre Jennica?
- **Strange Old Man:** Jennica... Cava, cava, cava... Cava...
- **Player:** ¿Excavar?
- (continuea|Standard dialogue)

### During The Temple at Senntisten

(ver|El Temple at Senntisten#Hablando con el Strange Old Man)

### Task System

- ((Si el player ha completado los logros difíciles de Morytania y no se han reclamado las recompensas:))
  - **Player:** He completado todas las tareas difíciles del conjunto Morytania.
  - **Strange Old Man:** Así que sí. Tengo unos leggings especiales reservados para ti.
  - [El Strange Old Man te entrega un par de mallas y una lámpara.]
  - **Strange Old Man:** Ahí lo tienes. Pueden ser un poco extraños, pero deberían ayudarte a deshacerte de las molestas gafas de sol de una vez por todas.
  - **Player:** ¡Gracias! ¿Qué más hacen?
  - **Strange Old Man:** Bueno, los fantasmas te entenderán y hablé con Hiylik, por lo que obtendrás mejores recompensas por ayudar a los desafortunados a llegar al templo. Ahh... también protegen un poco de la mala influencia de los Túmulos, y parecen estar relacionados con esas... tabletas que usas para llegar al Altar de Sangre.
  - (continue)
- (Condition: Si el player ha perdido sus patas Morytania 3:)
  - **Strange Old Man:** ¡Ah, el que usa calzas! ¿Cómo los estás encontrando?
  - **Player:** Los perdí.
  - **Strange Old Man:** ¡Oh, no!
  - **Strange Old Man:** No importa, tengo otro par. Aquí...
  - (receives=Morytania legs 3)
  - [El Strange Old Man te entrega un par de leggings.]
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: Háblame del Sistema de Logros.
    - **Strange Old Man:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
    - **Strange Old Man:**Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
    - **Strange Old Man:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
    - [Menu]: Elige una opción:
      - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
        - **Player:** Cuéntame sobre la recompensa establecida para esta área.
        - **Strange Old Man:** Para completar el conjunto Morytania, se te presentan unos leggings.
        - **Strange Old Man:** Estos leggings serán cada vez más útiles a medida que completes conjuntos de tareas de mayor dificultad.
        - **Strange Old Man:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
        - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
        - (previous2)
      - [Choice]: ¿Cómo reclamo estas recompensas?
        - **Player:** ¿Cómo reclamo las recompensas?
        - **Strange Old Man:** Debes completar todas las tareas dentro de un conjunto de dificultad particular y luego podrás reclamar tu recompensa.
        - **Strange Old Man:** Algunas de las tareas del conjunto Morytania son simples, algunas requieren cierto skill levels y otras requieren que se inicien o completen misiones.
        - **Strange Old Man:** Para reclamar las recompensas del conjunto Morytania, habla con Hiylik Myna justo al este de Paterdomus, Robin en Port Phasmatys, Old Man Ral en Meiyerditch o conmigo mismo.
        - (previous2)
      - [Choice]: Lo siento, me estaba yendo.
        - (end)
  - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
    - [Menu]: Elige una opción:
      - [Choice]: Morytania piernas 1
        - **Strange Old Man:** Morytania piernas 1? Sí, pero me temo que te costaría 1.500 coins.
        - [Menu]: ¿Comprar otro por 1.500 coins?
          - [Choice]: si
            - [Te entregan otras piernas Morytania 1.]
            - (receives=Morytania legs 1) (removes= 1,500 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Morytania piernas 2
        - **Strange Old Man:** Morytania piernas 2? Sí, pero me temo que te costaría 2500 coins.
        - [Menu]: ¿Comprar otro por 2500 coins?
          - [Choice]: si
            - [Te entregan otras piernas Morytania 2.]
            - (receives=Morytania legs 2) (removes= 2,500 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Morytania piernas 3
        - **Strange Old Man:** Morytania piernas 3? Sí, pero me temo que te costaría 7.500 coins.
        - [Menu]: ¿Comprar otro por 7.500 coins?
          - [Choice]: si
            - [Te entregan otras piernas Morytania 3.]
            - (receives=Morytania legs 3) (removes= 7,500 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Morytania piernas 4
        - **Strange Old Man:** Morytania patas 4? Sí, pero me temo que te costaría 15.000 coins.
        - [Menu]: ¿Comprar otro por 15.000 coins?
          - [Choice]: si
            - [Te entregan otras patas Morytania 4.]
            - (receives=Morytania legs 4) (removes= 15,000 coins)
          - [Choice]: No
            - **Player:** No, gracias.
  - [Choice]: Lo siento, me estaba yendo.
    - (end)

### Farming Guild


#### Ayuda


##### Antes de completar la solicitud

- **¿QUÉ TE GUSTARÍA HACER?**
  - Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Strange Old Man:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Strange Old Man:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - (Condition: Con 2 razas de animales aceptadas:)
      - **Strange Old Man:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
      - (continue)
    - (Condition: Con 3 razas de animales aceptadas:)
      - **Strange Old Man:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
      - (continue)
    - **Strange Old Man:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - **Strange Old Man:** Si completas esto, te daré: Un objeto de Barrows x 1. ¡Estoy seguro de que también ganarás reputación en el gremio de agricultores!
    - **Strange Old Man:** ¡Tendrás que ser rápido!, solo estoy aquí por [número] días, [número] horas y [número] minutos. Para ser exactos.
  - Dales los artículos y animales que soliciten.
    - ((Sin los artículos solicitados:))
      - **Strange Old Man:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Strange Old Man:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - (Condition: Con 2 razas de animales aceptadas:)
        - **Strange Old Man:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
        - (continue)
      - (Condition: Con 3 razas de animales aceptadas:)
        - **Strange Old Man:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
        - (continue)
      - **Strange Old Man:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - ((Con los artículos solicitados:))
      - (removes=the requested items) (receives=the reward)
      - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
      - ((Repetido en una ventana emergente:))
        - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
        - (continue)
      - Has recibido: [Reward] x [número]<br>Y 13,750 reputación agrícola.

##### Después de completar la solicitud

- **Strange Old Man:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [número] días, [número] horas y [número] minutos.

#### Entregar solicitud dura


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Strange Old Man:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Strange Old Man:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- (Condition: Con 2 razas de animales aceptadas:)
  - **Strange Old Man:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
  - (continue)
- (Condition: Con 3 razas de animales aceptadas:)
  - **Strange Old Man:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
  - (continue)
- **Strange Old Man:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]

##### Con artículos solicitados

- (removes=the requested items) (receives=the reward)
- Por completar esta solicitud, recibió 3 imprimadores para Brassica.
- ((Repetido en una ventana emergente:))
  - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
  - (continue)
- Has recibido: [Reward] x [número]<br>Y 13,750 reputación agrícola.

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud semanal en [número] días, [número] horas y [número] minutos.
