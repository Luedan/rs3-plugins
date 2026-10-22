# Yrsa

- **Original Wiki Page**: [Transcript:Yrsa](https://runescape.wiki/w/Transcript%3AYrsa)
- **Letter**: `Y`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|Missing dialogue to reclaim Fremennik sea boots 2 if lost}}

### Before The Fremennik Trials


#### Hablando con ella

- **Player:** ¡Hola!
- **Yrsa:** Lo siento, outsider, no puedo venderte ropa. Nuestras costumbres lo prohíben.
- [Menu]: Elige una opción:
  - [Choice]: Háblame del Sistema de Logros.
    - (abajo)
  - [Choice]: Lo siento, me estaba yendo.
    - (end)

#### Opción comercial

- Sólo los Fremenniks pueden comprar ropa aquí.

#### Opción de cambio de zapatos

- **Yrsa:** Lo siento, outsider, no puedo ayudarte. Nuestras costumbres lo prohíben.

### After The Fremennik Trials

- **Yrsa:** Bienvenido a mi tienda de ropa. Puedo cambiarte los zapatos o tengo una excelente selección de ropa a la venta.
- [Menu]: Elige una opción:
  - [Choice]: Me gustaría comprar algo de ropa.
    - (opens=Yrsa's Accoutrements)
  - [Choice]: Me gustaría cambiarme de zapatos.
    - **Player:** Me gustaría cambiarme de zapatos.
      - *(Si el player está empuñando un arma:)*
        - **Yrsa:** No me siento cómodo ayudándote a probarte zapatos cuando estás empuñando algo. Primero retire lo que tiene en sus manos.
      - *(Si el player no empuña un arma pero lleva algo en la ranura de los pies o tiene una anulación de pies activa:)*
        - **Yrsa:** Primero tendrás que quitarte lo que llevas puesto.
        - Deberá quitarse todo lo que lleve puesto en los pies y también desactivar las anulaciones de los pies antes de poder cambiarse los zapatos.
      - *(Si el player no empuña nada y no lleva nada en la ranura para los pies y no tiene una anulación de pies activa:)*
        - (opens=Yrsa's Shoe Store)
  - [Choice]: Acerca del sistema de tareas...
    - (below|Task System)
  - [Choice]: Nada, gracias.
    - **Player:** Nada, gracias.
    - **Yrsa:** Como desees.

### Task System

- ((If the player has completed the medium Fremennik achievements and the rewards have not been claimed:))
  - **Player:** He completado todas las tareas medianas del conjunto Fremennik.
  - **Yrsa:** Así es. Tengo unas botas especiales que he guardado para ti.
  - (Condition: If the player does not have sufficient space in backpack:)
    - **Yrsa:** Aunque tendrás que regresar cuando tengas espacio para tomarlos.
  - (Condition: If the player does have sufficient space in backpack:)
    - (receives=Fremennik sea boots 2 and Antique lamp (Medium Fremennik Tasks))
    - **Yrsa:** Ahí lo tienes. Son cosas poderosas a su manera, así que tenga cuidado de estudiarlas y encontrar todas las formas en que pueden ayudarle.
    - **Player:** ¡Gracias!
    - (continue)
- (Condition: If the player has lost their Fremennik sea boots 2:)
  - {{transcript missing}}
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: Háblame del Sistema de Logros.
    - **Yrsa:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
    - **Yrsa:**Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
    - **Yrsa:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
    - [Menu]: Elige una opción:
      - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
        - **Player:** Cuéntame sobre la recompensa establecida para esta área.
        - **Yrsa:** Por completar el conjunto Fremennik Province, se te presenta un par de botas de mar.
        - **Yrsa:** Estas botas serán cada vez más útiles con cada nivel de dificultad del conjunto que completes.
        - **Yrsa:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
        - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
        - (previous2)
      - [Choice]: ¿Cómo reclamo estas recompensas?
        - **Player:** ¿Cómo reclamo las recompensas?
        - **Yrsa:** Debes completar todas las tareas en un conjunto de una dificultad particular, luego podrás reclamar tu recompensa.
        - **Yrsa:** Algunas de las tareas del conjunto Fremennik son simples, algunas requerirán cierto skill levels y otras pueden requerir que se inicien o completen misiones.
        - **Yrsa:** Para reclamar las recompensas del conjunto Fremennik, habla con council workman en el puente al sur de Rellekka, Advisor Ghrim en Miscellania o conmigo mismo.
        - (previous2)
      - [Choice]: Lo siento, me estaba yendo.
        - (end)
  - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
    - [Menu]: Elige una opción:
      - [Choice]: Fremennik sea boots 1
        - **Yrsa:** Fremennik sea boots 1? Sí, pero me temo que te costaría 1.500 coins.
        - [Menu]: ¿Comprar otro por 1.500 coins?
          - [Choice]: si
            - [Te entregan otro Fremennik sea boots 1.]
            - (receives=Fremennik sea boots 1) (removes= 1,500 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Fremennik sea boots 2
        - **Yrsa:** Fremennik sea boots 2? Sí, pero me temo que te costaría 2500 coins.
        - [Menu]: ¿Comprar otro por 2500 coins?
          - [Choice]: si
            - [Te entregan otro Fremennik sea boots 2.]
            - (receives=Fremennik sea boots 2) (removes= 2,500 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Fremennik sea boots 3
        - **Yrsa:** Fremennik sea boots 3? Sí, pero me temo que te costaría 7.500 coins.
        - [Menu]: ¿Comprar otro por 7.500 coins?
          - [Choice]: si
            - [Te entregan otro Fremennik sea boots 3.]
            - (receives=Fremennik sea boots 3) (removes= 7,500 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Fremennik sea boots 4
        - **Yrsa:** Fremennik sea boots 4? Sí, pero me temo que te costaría 15.000 coins.
        - [Menu]: ¿Comprar otro por 15.000 coins?
          - [Choice]: si
            - [Te entregan otro Fremennik sea boots 4.]
            - (receives=Fremennik sea boots 4) (removes= 15,000 coins)
          - [Choice]: No
            - **Player:** No, gracias.
  - [Choice]: Lo siento, me estaba yendo.
    - (end)
