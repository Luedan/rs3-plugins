# Kaleb Paramaya

- **Original Wiki Page**: [Transcript:Kaleb Paramaya](https://runescape.wiki/w/Transcript%3AKaleb%20Paramaya)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Shilo Village


#### Antes de completar la misión Shilo Village

- **Kaleb Paramaya:** Me voy de aquí Bwana, el lugar está infestado de zombies.

#### Después de completar la misión Shilo Village

- **Player:** Hola.
- **Kaleb Paramaya:** Hola Bwana, ¿Qué puedo hacer {{Sic}} por ti hoy?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Puedes contarme un poco sobre este lugar?
    - **Player:** ¿Puedes contarme un poco sobre este lugar?
    - **Kaleb Paramaya:** ¡Por supuesto Bwana, pareces un viajero!
    - **Player:** ¡Sí, de hecho lo soy!
    - **Kaleb Paramaya:** Bueno, yo también soy un viajero y he creado este albergue para aventureros y viajeros que están cansados del viaje.
    - **Kaleb Paramaya:** Hay un dormitorio arriba si estás cansado, cuesta 35 piezas de oro que cubren el costo de lavandería y limpieza.
  - [Choice]: Compra algo.
    - [Menu]: Selecciona una opción
      - [Choice]: Compra vino: 1 Gold.{{Sic}}
        - **Kaleb Paramaya:** ¡Muy bien [sir/madam]!
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Kaleb Paramaya:** Lo siento Bwana, no tienes suficiente dinero.
          - No puedes permitirte eso.
        - (Condition: Si el player tiene suficiente dinero:)
          - (receives=jug of wine) (removes=one coin)
          - Compras una jarra de vino.
      - [Choice]: Compra cerveza: 2 de oro.{{Sic}}
        - **Kaleb Paramaya:** ¡Muy bien [sir/madam]!
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Kaleb Paramaya:** Lo siento Bwana, no tienes suficiente dinero.
          - No puedes permitirte eso.
        - (Condition: Si el player tiene suficiente dinero:)
          - (receives=beer) (removes=two coins)
          - Compras un vaso de cerveza espumosa.
      - [Choice]: Comprar una noche de descanso: 35 Gold{{Sic}}
        - **Kaleb Paramaya:** ¡Muy bien [sir/madam]!
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Kaleb Paramaya:** Lo siento Bwana, no tienes suficiente dinero.
          - No puedes permitirte eso.
        - (Condition: Si el player tiene suficiente dinero:)
          - (receives=Paramaya ticket) (removes=35 coins)
          - Compras un boleto para acceder al dormitorio.
      - [Choice]: Compra un paquete de 5 entradas para dormitorios: 175 Gold{{Sic}}
        - **Kaleb Paramaya:** ¡Muy bien [sir/madam]!
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Kaleb Paramaya:** Lo siento Bwana, no tienes suficiente dinero.
          - No puedes permitirte eso.
        - (Condition: Si el player tiene suficiente dinero:)
          - (receives=five Paramaya tickets) (removes=175 coins)
          - Compras 5 entradas para acceder al dormitorio.
  - [Choice]: Acerca del sistema de tareas...
    - (Condition: Si el player ha completado los logros medios de Karamja, pero aún no ha reclamado las recompensas:)
      - **Player:** He realizado todas las tareas medianas del conjunto Karamja.
      - **Kaleb Paramaya:** ¡Ahh, sí, lo has hecho! ¡Felicidades!
      - (Condition: Si el player no tiene guantes Karamja 1 en backpack:)
        - **Kaleb Paramaya:** ¿Cómo puedo encantar tus guantes Karamja si no los tienes contigo? Tráeme los guantes Karamja que obtuviste al completar las tareas fáciles.
        - (continue|task-system)
      - (Condition: Si el player tiene guantes Karamja 1 en backpack:)
        - Kaleb toma los guantes Karamja y murmura algo sobre ellos. Parecen brillar. Él se los devuelve.
        - (receives=Karamja gloves 2 and an antique lamp)
        - **Kaleb Paramaya:** El encantamiento que he colocado en estos guantes es un símbolo de tu futura exploración de la isla. Además de los beneficios de los anteriores, también podrás ganar más recompensas en Agility Arena. Oh, también hay un pequeño extra por todo tu arduo trabajo.
        - **Player:** ¡Vaya, gracias!
        - **Kaleb Paramaya:** Si los pierdes, vuelve conmigo para reclamarlos.
        - (continue|task-system)
    - (Condition: Si el player ha perdido sus guantes Karamja 2:)
      - **Kaleb Paramaya:** Oh... espera un minuto, te recuerdo de la última vez. ¿No bendije tus guantes Karamja?
      - **Player:** Sí, pero los perdí.
      - **Kaleb Paramaya:** Lo mismo pensé. Toma, toma otro par.
      - (receives=Karamja gloves 2)
      - (continue|task-system)
    - [Menu]: Elige una opción:
      - [Choice]: Cuéntame sobre el sistema de logros.{{anchor|achievements}}
        - **Kaleb Paramaya:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
        - **Kaleb Paramaya:** Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
        - **Kaleb Paramaya:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
        - [Menu]: Elige una opción:
          - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
            - **Player:** Cuéntame sobre la recompensa establecida para esta área.
            - **Kaleb Paramaya:** Para completar las tareas del conjunto Karamja, se te entregará un par de guantes.
            - **Kaleb Paramaya:** Completar cada nivel de dificultad del conjunto permitirá mejorar tus guantes.
            - **Kaleb Paramaya:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
            - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
            - (previous)
          - [Choice]: ¿Cómo reclamo estas recompensas?
            - **Player:** ¿Cómo reclamo las recompensas?
            - **Kaleb Paramaya:** Debes completar todas las tareas del conjunto de una dificultad particular y luego podrás reclamar tu recompensa.
            - **Kaleb Paramaya:** Algunas de las tareas del conjunto Karamja son simples, algunas requerirán cierto skill levels y otras pueden requerir que se inicien o completen misiones.
            - **Kaleb Paramaya:** Puedes reclamar tu recompensa del conjunto Karamja a Jackie the Fruit en el Brimhaven Agility Arena, a mí o a uno de los guardabosques de la jungla del sur.
            - (previous)
          - [Choice]: Lo siento, me estaba yendo.
            - (end)
      - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
        - [Menu]: Elige una opción:
          - [Choice]: guantes Karamja 1
            - **Kaleb Paramaya:** ¿Guantes Karamja 1? Sí, pero me temo que te costaría 1.500 coins.
            - [Menu]: ¿Comprar otro por 1.500 coins?
              - [Choice]: si
                - (receives=Karamja gloves 1) (removes=1,500 coins)
                - [Te entregan otros guantes Karamja 1.]
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: guantes Karamja 2
            - **Kaleb Paramaya:** ¿Guantes Karamja 2? Sí, pero me temo que te costaría 2500 coins.
            - [Menu]: ¿Comprar otro por 2500 coins?
              - [Choice]: si
                - (receives=Karamja gloves 2) (removes=2,500 coins)
                - [Te entregan otros guantes Karamja 2.]
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: Guantes Karamja 3
            - **Kaleb Paramaya:** ¿Guantes Karamja 3? Sí, pero me temo que te costaría 7.500 coins.
            - [Menu]: ¿Comprar otro por 7.500 coins?
              - [Choice]: si
                - (receives=Karamja gloves 3) (removes=7,500 coins)
                - [Te entregan otros guantes Karamja 3.]
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: Guantes Karamja 4
            - **Kaleb Paramaya:** ¿Guantes Karamja 4? Sí, pero me temo que te costaría 15.000 coins.
            - [Menu]: ¿Comprar otro por 15.000 coins?
              - [Choice]: si
                - (receives=Karamja gloves 4) (removes=15,000 coins)
                - [Te entregan otros guantes Karamja 4.]
              - [Choice]: No
                - **Player:** No, gracias.
      - [Choice]: Lo siento, me estaba yendo.
        - (end)

##### Intentando entrar al dormitorio


##### Con un boleto

- (removes=Paramaya ticket)
- El barman toma tu billete y te permite subir al dormitorio.

##### Sin billete

- **Kaleb Paramaya:** Puedes comprarme un boleto para el dormitorio. Y que tengas un agradable descanso nocturno.
