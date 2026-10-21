# Elen Anterth

- **Original Wiki Page**: [Transcript:Elen Anterth](https://runescape.wiki/w/Transcript%3AElen%20Anterth)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### First time entering the Max Guild garden

- **Elen:** ¡Oye, bienvenido al jardín del gremio Max!

### Talk to

- **Elen:** ¡Oh, hola!
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Cuál es tu nombre?
    - **Elen:** ¡Soy Elen! ¡Es un placer conocerte! ¡Bienvenido al gremio Max!
    - (Condition: Si el player está en el gremio Max:)
      - **Elen:** Enhorabuena por haber entrado aquí. ¡Es bien merecido!
      - (continue)
    - **Player:** ¿Elen? ¿No deberías llamarte Maxine o algo así?
    - **Elen:** ¿Maxine? ¡Qué nombre más extraño sería ese para un elfo! Jaja, me gusta!
    - **Elen:** Pero no, es Elen - Elen Anterth. Mi familia está bajo los auspicios del Clan Cadarn.
    - **Player:** ¿Cómo eres tan hábil si la ciudad acaba de volver a crecer?
    - **Elen:** ¡Oh, he estado por todas partes! Mi familia viajó hacia el este con el camino de regreso de Cadarn.
    - **Elen:** Yo era muy joven, pero vi mucho y aprendí mucho. Te sorprendería lo que se te queda grabado.
    - (initial)
  - [Choice]: Bonita capa la que tienes ahí...
    - **Elen:** ¡Gracias! Me tomó mucho tiempo lograrlo, pero al final lo logré: soy completamente competente en todas las habilidades.
    - (Condición: si el player no ha maximizado todas las habilidades:){{anchor|notmaxed}}
      - Para hacer esto necesitas en el siguiente skill levels:<br>99 [Skill]
      - **Player:** Vaya, eso es bastante impresionante.
      - **Elen:** Gracias. Tengo fe en ti, Player. Tómate tu tiempo y tú también llegarás allí, ¡lo sé!
      - **Player:** Sí, tal vez...
      - **Elen:** Sólo recuerda: no te apresures. ¡Es el viaje, no el destino!
    - (Condición: si el player ha maximizado todas las habilidades:){{anchor|maxed}}
      - **Player:** ¡He maximizado todas las habilidades!
      - **Elen:** ¿En serio? ¡Bien por usted! ¿Quieres una capa para mostrar tu logro? Son 2.871.000 coins: ¡99.000 por cada habilidad!
      - [Menu]: ¿Pagar 2.871.000 por una capa máxima?
        - [Choice]: ¡Me llevaré uno!
          - **Player:** ¡Claro!
          - ((Sin dos espacios libres en backpack:))
            - No tienes suficiente espacio en el inventario para retirar tantos.
            - **Elen:** Ah, pero necesitarás espacio en tu inventario para una capa y una capucha.
          - ((Con dos espacios libres en backpack:))
            - ((Sin suficiente coins:))
              - No puedes permitirte eso.
              - ((Repetido en una ventana emergente:))
                - No puedes permitirte eso.
                - (continue)
              - **Elen:** Lo siento, cariño, pero no tienes suficiente coins contigo.
            - ((Con suficiente coins:))
              - (removes=2,871,000 coins) (receives=a max cape and max hood)
              - **Elen:** Gracias. ¡Disfrutar!
              - (initial)
        - [Choice]: No, gracias.
          - **Player:** No, gracias.
          - (initial)
  - [Choice]: cond=Historical, only occurs when a skill is recently released|¿Qué pasó con tu capa Max?
    - **Elen:** ¡Oh, estoy entrenando a [Recently released skill]! Sin prisas, tomándome mi tiempo. ¡Probablemente me ganarás al máximo!
    - ((Si no has conseguido que [Recently released skill] llegue a 99:))
      - (above|notmaxed)
    - ((Si has conseguido [Recently released skill] a 99:))
      - (above|maxed)
  - [Choice]: ¿Conoces a alguien llamado Max?
    - **Elen:** No te refieres a ese humano optimista de Varrock, ¿verdad?
    - **Player:** ¿Alcista? Bueno, supongo que siempre está corriendo de un lugar a otro.
    - **Elen:** Urgh, odio a ese tipo.
    - **Player:** ¿Cuándo lo conociste?
    - **Elen:** Desde que la ciudad volvió a crecer, él aparece aquí a veces. Nunca se detiene por mucho tiempo.
    - **Elen:** Simplemente corre por el lugar entrenando, no se toma el tiempo para simplemente relajarse y disfrutar las cosas.
    - **Player:** Eso suena como Max.
    - **Elen:** Intenté hablar con él las primeras veces que lo vi, pero siempre decía que estaba "haciendo sus diarios" y que no tenía tiempo.
    - **Elen:** En nuestra hermosa ciudad hay más que "diarios".
    - **Player:** ¿Entra aquí?
    - **Elen:** Aquí no hay ningún beneficio para él, dice. Sería un desperdicio, dice.
    - **Elen:** Entonces no eres bienvenido aquí, dije.
    - (initial)
  - [Choice]: cond=Only in the Max Guild|¿Puedo alternar mi teletransporte del Max Guild?
    - **Elen:** ¡Por supuesto! Actualmente estás listo para llegar al [garden/tower]. ¿Quieres llegar al [tower/garden]?
    - [Menu]: ¿Cambiar el teletransporte del gremio Max?
      - [Choice]: Sí.
        - (initial)
      - [Choice]: No.
        - (initial)
  - [Choice]: Más...
    - [Menu]: Selecciona una opción
      - [Choice]: Acerca del sistema de tareas...
        - ((Si el player ha completado los logros de élite de Tirannwn y no se han reclamado las recompensas:))
          - **Player:** He completado todas las tareas Elite del conjunto Tirannwn.
          - **Elen Anterth:** Bien hecho Player. Tengo un carcaj especial reservado para ti.
          - [Elen te entrega un carcaj, algunas lámparas y muchos recursos.]
          - **Elen Anterth:** Llévate esta merecida recompensa: nos has impresionado a todos. El carcaj te permitirá teletransportarte a la mazmorra de recursos, luchar contra bestias oscuras más fácilmente y usar la imagen de nuestros Señores y Damas cuando estés en el fotomatón.
          - **Player:** ¡Gracias! ¿Qué más hace?
          - **Elen Anterth:** Debido a que completaste el conjunto de tareas Elite, podrás persuadir a Coeden para que te dé algo de logs, usar menos cargas al usar las cartas Most Wanted y tu arco y guardián de cristal sintonizados.
          - (continue)
        - (Condition: Si el player ha perdido su carcaj Tirannwn 4:)
          - **Elen Anterth:** ¡Ah, portador de la aljaba! ¿Cómo está yendo?
          - **Player:** Lo perdí.
          - **Elen Anterth:** ¡Oh, no!
          - **Elen Anterth:** No importa, tengo otro. Aquí...
          - [Elen te entrega un carcaj.]
          - (continue)
        - [Menu]: Elige una opción:
          - [Choice]: Háblame del Sistema de Logros.
            - **Elen Anterth:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
            - **Elen Anterth:** Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
            - **Elen Anterth:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
            - [Menu]: Elige una opción:
              - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
                - **Player:** Cuéntame sobre la recompensa establecida para esta área.
                - **Elen Anterth:** Por completar el conjunto Tirannwn, se te presenta un carcaj.
                - **Elen Anterth:** Este carcaj será cada vez más útil a medida que completes conjuntos de tareas de mayor dificultad.
                - **Elen Anterth:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
                - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
                - (previous2)
              - [Choice]: ¿Cómo reclamo estas recompensas?
                - **Player:** ¿Cómo reclamo las recompensas?
                - **Elen Anterth:** Debes completar todas las tareas de un conjunto de una dificultad particular y luego podrás reclamar tu recompensa.
                - **Elen Anterth:** Algunas de las tareas del conjunto Tirannwn son simples, algunas requerirán skill levels y otras requieren que se inicien o completen misiones.
                - **Elen Anterth:** Para reclamar las recompensas del conjunto Tirannwn, habla con Elven Tracker cerca de Lodestone, Gwir en Lletya, Elen en la ciudad o conmigo mismo.
                - (previous2)
              - [Choice]: Lo siento, me estaba yendo.
                - (end)
          - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
            - [Menu]: Elige una opción:
              - [Choice]: Tirannwn carcaj 1
              - **Elen Anterth:** Tirannwn carcaj 1? Sí, pero me temo que te costaría 5.000 coins.
                - [Menu]: ¿Comprar otro por 5.000 coins?
                  - [Choice]: si
                    - [Te entregan otro carcaj Tirannwn 1.]
                    - (receives=Tirannwn quiver 1) (removes= 5,000 coins)
                  - [Choice]: No
                    - **Player:** No, gracias.
              - [Choice]: Tirannwn carcaj 2
                - **Elen Anterth:** ¿Tirannwn carcaj 2? Sí, pero me temo que te costaría 10.000 coins.
                - [Menu]: ¿Comprar otro por 10.000 coins?
                  - [Choice]: si
                    - [Te entregan otro carcaj Tirannwn 2.]
                    - (receives=Tirannwn quiver 2) (removes= 10,000 coins)
                  - [Choice]: No
                    - **Player:** No, gracias.
              - [Choice]: Tirannwn carcaj 3
                - **Elen Anterth:** Tirannwn carcaj 3? Sí, pero me temo que te costaría 25.000 coins.
                - [Menu]: ¿Comprar otro por 25.000 coins?
                  - [Choice]: si
                    - [Te entregan otro carcaj Tirannwn 3.]
                    - (receives=Tirannwn quiver 3) (removes= 25,000 coins)
                  - [Choice]: No
                    - **Player:** No, gracias.
              - [Choice]: Tirannwn carcaj 4
                - **Elen Anterth:** Tirannwn carcaj 4? Sí, pero me temo que te costaría 50.000 coins.
                - [Menu]: ¿Comprar otro por 50.000 coins?
                  - [Choice]: si
                    - [Te entregan otro carcaj Tirannwn 4.]
                    - (receives=Tirannwn quiver 4) (removes= 50,000 coins)
                  - [Choice]: No
                    - **Player:** No, gracias.
          - [Choice]: Lo siento, me estaba yendo.
            - (end)
      - [Choice]: Adiós.
        - **Player:** Adiós.

### Trade


#### Fuera del edificio del gremio Max

- **Elen:** Lo siento, cariño, solo vendo capas de habilidad en la torre.
- **Elen:** Oh, pero podría decirte quién SÍ vende capas de habilidades. ¿Quieres que te diga dónde están todos los maestros de habilidades?
- [Menu]: ¿Preguntar sobre los maestros de habilidades?
  - [Choice]: Sí.
    - **Elen:** ¡Te lo desglosaré o seguiré hablando durante mucho tiempo!
    - [Menu]: ¿Preguntar sobre qué categoría de capa?
      - [Choice]: Combate.
        - **Elen:** Hay un par que puedes obtener de Warriors' Guild en Burthorpe: el attack cape de Ajjat y la capa de fuerza de Yadech Strongarm.
        - **Elen:** La capa mágica la vende robe store owner en el Wizards' Guild de Yanille, y la capa a distancia la vende armour salesman en Ranging Guild en Hemenster.
        - **Elen:** Si buscas la capa Defence, habla con Harlan en Lumbridge Combat Academy. Para Constitution, habla con Surgeon General Tafani en su casa cerca de la entrada norte de Al Kharid.
        - **Elen:** Para la capa de Necromancy, querrás buscar en City of Um un fantasma llamado the Spirit of Accomplishment.
        - **Elen:** Ah, y son más bien habilidades de apoyo, pero la capa de oración se puede comprar en Brother Jered en Edgeville Monstary, y Pikkupstix en Taverley vende la capa de invocación.
        - (continue|hearmore)
      - [Choice]: Reunión.
        - **Elen:** Hice una nueva amiga en Orla Fairweather: ella vende la capa para adivinación. Es una habilidad cercana a mi corazón.
        - **Elen:** El master fisher del Gremio Fishing al norte de Ardougne vende esa capa. No me gusta el pescado, ¡qué asco!
        - **Elen:** Si buscas una capa minera, habla con el enano que dirige el gremio Mining en Falador.
        - **Elen:** ¡Si quieres una capa de leñador, dirígete al bosque al norte de Falador y encuentra Wilfred!
        - **Elen:** Ah, y si eres fanático del pasado, puedes conseguir la capa de arqueología de Reiniger en el Gremio Archaeology.
        - (continue|hearmore)
      - [Choice]: Artisan.
        - **Elen:** No mantengo mi casa en buen estado desde que me instalé aquí, pero tengo mi capa de construcción, la compré de un estate agent.
        - **Elen:** Y el master crafter en el Gremio Crafting al norte de Rimmington me resolvió con esa capa.
        - **Elen:** Ignatius Vulcan es extraño, pero se ganó con creces su capa de hacer fuego: está en los bosques al sur de Seers' Village.
        - **Elen:** No muy lejos de él, en Catherby, encontrarás a Hickton; él vende la capa con plumas.
        - **Elen:** ¿Y quién puede olvidar a Thurgo en su cabaña en Mudskipper Point? Vende la capa de herrería... ¡y come pasteles de frutos rojos!
        - **Elen:** Ah, y en cuanto a Invention... ¡probablemente podrías inventar tu PROPIO skillcape! O ve a ver Doc en el Invention Guild.
        - (continue|hearmore)
      - [Choice]: Naturalista.
        - **Elen:** head chef del gremio de cocineros Varrock te repartirá una capa de cocina.
        - **Elen:** Dirígete al mercado Draynor Village y habla con Martin the master gardener si buscas una capa agrícola.
        - **Elen:** Si quieres una capa herblore, habla con Kaqemeex en el círculo de piedras en Taverley.
        - **Elen:** ¡Ah, y Larriar en el Runecrafting Guild encima del Wizards' Tower te venderá esa capa!
        - (continue|hearmore)
      - [Choice]: Superviviente.
        - **Elen:** Cap'n Izzy No-Beard en Brimhaven Agility Arena vende la capa de agilidad.
        - **Elen:** No es un gran maestro, pero Thok Thokson vende la capa de mazmorra en Daemonheim. Es un poco murmurador, eso no siempre tiene sentido.
        - **Elen:** Localiza el hunting expert en Feldip Hills si buscas una capa de cazador.
        - **Elen:** Estoy seguro de que Morvran del Clan Iorwerth discutiría esto, pero Kuradal en la Caverna Antigua es un maestro asesino.
        - **Elen:** Y, por último, puedes robar la capa de ladrón de Martin Thwait; se encuentra en Rogues' Den, debajo del pub Pick and {{Sic|Loot}} en Taverley.
        - (continue|hearmore)
    - {{anchor|hearmore}}**Elen:** ¿Quieres saber más o ya has oído suficiente?
    - [Menu]: ¿Escuchaste más?
      - [Choice]: Sí, ¡cuéntame más!
        - (previous2)
      - [Choice]: No, ¡ya he oído suficiente!
        - (end)
  - [Choice]: No.
    - **Elen:** Está bien, ¡nos vemos!

#### En el edificio del gremio Max


##### Con un inverted cape desbloqueado

- (Condition: Con un inverted cape desbloqueado:)
  - [Menu]: Elige una opción:
    - [Choice]: Ver capas regulares
      - (opens=The Max Cape Marketplace)
    - [Choice]: Ver inverted capes
      - (opens=The Inverted Max Cape Marketplace)

##### Sin un inverted cape desbloqueado

- (opens=The Max Cape Marketplace)
