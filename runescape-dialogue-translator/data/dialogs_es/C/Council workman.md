# Council workman

- **Original Wiki Page**: [Transcript:Council workman](https://runescape.wiki/w/Transcript%3ACouncil%20workman)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At the bridge south of Rellekka

- **Player:** Hola.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Así que arreglaste el puente?
    - **Player:** ¿Entonces arreglaste el puente?
    - **Council workman:** Sí, eso hice. También era un trabajo que daba mucha sed. Si tan solo algún extraño amable nos invitara un poco de cerveza para cenar, ¿eh?
    - **Council workman:** ¿Qué pasa con esa posada de Seers' Village tan cerca y todo eso, eh?
    - El trabajador te guiña un ojo.
    - **Council workman:** ¡Solo asegúrate de no darme nada de esa basura sin alcohol de ese tipo poison salesman en la taberna!
  - [Choice]: Acerca del sistema de tareas...
    - ((Si el player ha completado los logros fáciles de Fremennik y no se han reclamado las recompensas:))
      - **Player:** He completado todas las tareas fáciles del conjunto Fremennik.
      - **Council workman:** Ah, es bueno escucharlo. Puedes usar Fremennik sea boots ahora; tengo un par para ti.
      - (Condition: Si el player no tiene suficiente espacio en backpack:)
        - **Council workman:** Aunque tendrás que regresar cuando tengas espacio para tomarlos.
      - (Condition: Si el player tiene suficiente espacio en backpack:)
        - (receives=Fremennik sea boots 1 and Antique lamp (Easy Fremennik Tasks))
        - **Council workman:** Son raras esas botas. Supongo que impresionarán a los Fremennik y sus extraños espíritus. Mírelos con atención, vea si no puede descubrir lo que hacen.
        - **Player:** ¡Gracias!
        - (continue)
    - (Condition: Si el player ha perdido su Fremennik sea boots 1:)
      - **Council workman:** ¿Tú otra vez? ¿Cómo te fue con esas botas?
      - **Player:** Los perdí.
      - **Council workman:** ¿Los perdiste? Bueno, da la casualidad de que encontré otro par. Cuídalos mejor esta vez.
      - (receives=Fremennik sea boots 1)
      - (continue)
    - [Menu]: Elige una opción:
      - [Choice]: Háblame del Sistema de Logros.
        - **Council workman:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
        - **Council workman:**Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
        - **Council workman:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
        - [Menu]: Elige una opción:
          - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
            - **Player:** Cuéntame sobre la recompensa establecida para esta área.
            - **Council workman:** Por completar las tareas del conjunto Fremennik Province, obtienes un par de botas.
            - **Council workman:** Cuantos más niveles de dificultad del conjunto completes, mejores serán las botas; te diremos qué hacen cuando te las entreguemos.
            - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
            - (previous2)
          - [Choice]: ¿Cómo reclamo estas recompensas?
            - **Player:** ¿Cómo reclamo las recompensas?
            - **Council workman:** Debes completar todas las tareas en un conjunto de una dificultad particular, luego podrás reclamar tu recompensa.
            - **Council workman:** Algunas de las tareas del conjunto Fremennik son simples, algunas requerirán cierto skill levels y otras pueden requerir que se inicien o completen misiones.
            - **Council workman:** Para reclamar las recompensas del conjunto Fremennik, habla con Yrsa en Rellekka, Advisor Ghrim en Miscellania o conmigo mismo.
            - (previous2)
          - [Choice]: Lo siento, me estaba yendo.
            - (end)
      - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
        - [Menu]: Elige una opción:
          - [Choice]: Fremennik sea boots 1
            - **Council workman:** Fremennik sea boots 1? Sí, pero me temo que te costaría 1.500 coins.
            - [Menu]: ¿Comprar otro por 1.500 coins?
              - [Choice]: si
                - [Te entregan otro Fremennik sea boots 1.]
                - (receives=Fremennik sea boots 1) (removes= 1,500 coins)
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: Fremennik sea boots 2
            - **Council workman:** Fremennik sea boots 2? Sí, pero me temo que te costaría 2500 coins.
            - [Menu]: ¿Comprar otro por 2500 coins?
              - [Choice]: si
                - [Te entregan otro Fremennik sea boots 2.]
                - (receives=Fremennik sea boots 2) (removes= 2,500 coins)
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: Fremennik sea boots 3
            - **Council workman:** Fremennik sea boots 3? Sí, pero me temo que te costaría 7.500 coins.
            - [Menu]: ¿Comprar otro por 7.500 coins?
              - [Choice]: si
                - [Te entregan otro Fremennik sea boots 3.]
                - (receives=Fremennik sea boots 3) (removes= 7,500 coins)
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: Fremennik sea boots 4
            - **Council workman:** Fremennik sea boots 4? Sí, pero me temo que te costaría 15.000 coins.
            - [Menu]: ¿Comprar otro por 15.000 coins?
              - [Choice]: si
                - [Te entregan otro Fremennik sea boots 4.]
                - (receives=Fremennik sea boots 4) (removes= 15,000 coins)
              - [Choice]: No
                - **Player:** No, gracias.
      - [Choice]: Lo siento, me estaba yendo.
        - (end)

#### Usando una cerveza con él.

- (removes=beer) (receives=strange object)
- **Council workman:** Me gusta mucho. Eso dará en el clavo. Toma, puedes tener esto. Lo compré como recuerdo en mis últimas vacaciones.
- **Player:** ¿Qué es?
- **Council workman:** No lo sé bien, pero si usas un yesquero, ¡no hace ni la mitad de ruido!
