# Bob

- **Original Wiki Page**: [Transcript:Bob](https://runescape.wiki/w/Transcript%3ABob)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Lumbridge

- [Menu]: Selecciona una opción
  - [Choice]: cond=With a construction contract for Bob's Axes|Quiero hablar de mi contrato.
  - [Menu]: Selecciona una opción
    - [Choice]: ¿Qué necesitas reparar?
      - **Player:** ¿Qué necesitas reparar?
      - **Bob:** Déjame ver, ahora mismo necesito que repares el siguiente pieces of furniture.
      - **Bob:** [Furniture 1], [Furniture 2], [Furniture 3], [Furniture 4], [Furniture 5]
      - (previous)
    - [Choice]: ¿Qué materiales necesito?
      - **Player:** ¿Qué materiales necesito?
      - **Bob:** Necesitas: Planks x [número], Steel nails x [número], [Additional material] x [número]
      - (previous)
    - [Choice]: salir
      - (end)
  - [Choice]: Me gustaría negociar.
    - **Player:** Me gustaría realizar un intercambio.
    - **Bob:** ¡Genial! Compro y vendo picos y hachas. Hay mucho para elegir y también tengo algunas muestras gratis. Elija... o hacha.
    - (opens=Bob's Brilliant Axes)
  - [Choice]: ¿Pueden reparar mis artículos por mí?
    - **Player:** ¿Pueden reparar mis artículos por mí?
    - **Bob:** Por supuesto que puedo, aunque los materiales pueden costarte. Sólo dame el artículo y echaré un vistazo.
  - [Choice]: Acerca del sistema de tareas...
    - (Condition: If the player has completed the Easy tasks in the Lumbridge and Draynor set and the rewards not claimed:)
      - **Player:** He completado todas las tareas sencillas del conjunto Lumbridge.
      - **Bob:** Ah, digno, por decir lo menos.
      - **Player:** Gracias. ¿Hubo recompensa?
      - **Bob:** ¿Una recompensa? Sí, de hecho. Puedo darte un Anillo de Explorador mejorado.
      - [Bob te entrega un anillo de plata.]
      - **Bob:** Ahí. Creo que encontrarás este anillo más adecuado para un aventurero de tus talentos.
      - **Bob:** ¡Posee todas las funciones de tu anillo anterior, con la ventaja adicional de una carga de energía de ejecución adicional, así como 30 cargas del hechizo de Baja Alquimia!
      - **Bob:** El hechizo te permitirá transformar ciertos elementos de tu inventario en coins.
      - **Bob:** Ahora no se puede decir que sea más justo que recibir dinero gratis, ¿eh?
      - **Bob:** No solo eso, sino que si decides hacer algo de Runecrafting, usar este anillo te dará la oportunidad de obtener runas adicionales al crear runas de fuego, tierra, aire o agua.
      - **Bob:** Te lo digo, los aventureros de hoy en día son muy mimados. Pues, en mis días...(murmullo)...dragones...(murmullo)...manos desnudas.
      - **Player:** Mmm.
      - **Bob:** ¡Oh, lo siento! Me distraje un poco ahí. Ahora, como recompensa extra, también te he dado una lámpara mágica para ayudarte con tus habilidades.
      - **Player:** ¡Muchas gracias! ¿Qué pasa si pierdo el nuevo anillo?
      - **Bob:** Bueno, espero que te enorgullezcas un poco más de tus posesiones que eso. Si lo pierdes, vuelve conmigo y te daré otro. Ahora, ¿algo más?
      - (continue)
    - (Condition: If the player has lost their Explorer's ring 2:)
      - **Bob:** ¿No me digas que perdiste el anillo que te di?
      - **Player:** Sí, lo siento. No sé qué pasó con eso.
      - (receives=Explorer's ring 2)
      - **Bob:** ¡Eh! Aventureros de estos días. ¿No hay respeto por lo valioso? ¿Hay algo más?
      - (continue)
    - [Menu]: Elige una opción:
      - [Choice]: Háblame del Sistema de Logros.
        - **Bob:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
        - **Bob:** Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
        - **Bob:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
        - [Menu]: Elige una opción:
          - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
            - **Bob:** Por completar el conjunto Lumbridge y Draynor, se te presenta un anillo de explorador.
            - **Bob:** Este anillo será cada vez más útil con cada nivel de dificultad del conjunto que completes.
            - **Bob:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
            - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
            - (previous)
          - [Choice]: ¿Cómo reclamo estas recompensas?
            - **Bob:** Debes completar todas las tareas de un conjunto de una dificultad particular y luego podrás reclamar tu recompensa. La mayoría de las tareas del conjunto Lumbridge son sencillas, aunque es posible que algunas requieran que se inicien, si no se terminan.
            - **Bob:** Para reclamar la recompensa del conjunto Lumbridge, habla con Ned en Draynor Village, Explorer Jack en Lumbridge o conmigo mismo.
            - (previous)
          - [Choice]: Lo siento, me estaba yendo.
            - (end)
      - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
      - [Menu]: Elige una opción:
        - [Choice]: Anillo del explorador 1
          - **Bob:** ¿Anillo 1 del explorador? Sí, pero me temo que te costaría 500 coins.
          - [Menu]: ¿Comprar otro por 500 coins?
            - [Choice]: si
              - [Te entregan el anillo de otro Explorador 1.]
              - (receives=Explorer's ring 1) (removes= 500 coins)
            - [Choice]: No
              - **Player:** No, gracias.
        - [Choice]: Anillo del explorador 2
          - **Bob:** ¿Anillo del explorador 2? Sí, pero me temo que te costaría 1.000 coins.
          - [Menu]: ¿Comprar otro por 1.000 coins?
            - [Choice]: si
              - [Te entregan el anillo de otro Explorador 2.]
              - (receives=Explorer's ring 2) (removes= 1,000 coins)
            - [Choice]: No
              - **Player:** No, gracias.
        - [Choice]: Anillo del explorador 3
          - **Bob:** ¿Anillo del explorador 3? Sí, pero me temo que te costaría 2000 coins.
          - [Menu]: ¿Comprar otro por 2000 coins?
            - [Choice]: si
              - [Te entregan el anillo de otro Explorador 3.]
              - (receives=Explorer's ring 3) (removes= 2,000 coins)
            - [Choice]: No
              - **Player:** No, gracias.
        - [Choice]: Anillo del explorador 4
          - **Bob:** ¿Anillo del explorador 4? Sí, pero me temo que te costaría 10.000 coins.
          - [Menu]: ¿Comprar otro por 10.000 coins?
            - [Choice]: si
              - [Te entregan el anillo de otro Explorador 4.]
              - (receives=Explorer's ring 4) (removes= 10,000 coins)
            - [Choice]: No
              - **Player:** No, gracias.
      - [Choice]: Lo siento, me estaba yendo.
        - (end)

### Using an item on Bob to have it repaired or using right-click Repair-all option


#### Con elementos para reparar en el backpack o usando un elemento en él para reparar

- [Menu]: ¿Pagar a [número] GP para arreglarlo?
  - [Choice]: Sí.
    - [número] coins se han eliminado de su bolsa de dinero.
  - [Choice]: No.
    - (end)

#### Si el player no tiene elementos para reparar

- **Bob:** No tienes ningún artículo que pueda repararse o recargarse.
