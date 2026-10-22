# Elf Tracker

- **Original Wiki Page**: [Transcript:Elf Tracker](https://runescape.wiki/w/Transcript%3AElf%20Tracker)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### After Regicide and before Plague's End

- **Player:** Hola, ¿sigues buscando pistas?
- **Elf Tracker:** Las huellas de mis hermanos son más difíciles de seguir de lo que puedas imaginar.
- **Player:** Supongo que sí.
- [Menu]: Selecciona una opción
  - [Choice]: Acerca del sistema de tareas...
    - (abajo2)
  - [Choice]: Adiós.
    - **Player:** Adiós.

### After Plague's End

- **Player: :** Hola, ¿sigues buscando pistas?
- **Elf Tracker: :** ¡No es necesario! Mis hermanos están prosperando en Prifddinas, gracias a ti. <br>¿Por qué no hacerles una visita?
- [Menu]: Selecciona una opción
  - [Choice]: Acerca del sistema de tareas...
    - (abajo2)
  - [Choice]: Adiós.
    - **Player:** Adiós.

### Task System

- (Condition: If the Easy Tirannwn achievements have been completed and the rewards not claimed:)
  - **Player:** He completado todas las tareas fáciles del conjunto Tirannwn.
  - **Elf Tracker:** Ah, eso es un alivio. Ya puedes usar el carcaj Tirannwn. Tengo uno para ti.
  - [El Elf Tracker te entrega un carcaj y una lámpara vieja.]
  - **Elf Tracker:** Este es un carcaj poderoso. Te ayudará a superar las trampas de hojas, facilitará la lucha contra los dolientes y actuará como un timbre.
  - **Player:** ¡Gracias!
  - **Elf Tracker:** Ahora que has completado el conjunto de tareas Fácil, también puedes vender tu piedra caliza a Meredith, reclamar alquitrán de pantano gratis en Lletya general store y mucho más.
  - (continue)
- (Condition: If the player has lost their Tirannwn quiver 1:)
  - **Elf Tracker:** ¿Tú otra vez? ¿Cómo te fue con el carcaj?
  - **Player:** Lo perdí.
  - **Elf Tracker:** ¿Perdido? Bueno, da la casualidad de que encontré otro. Cuida mejor este.
  - [El Elf Tracker te entrega un carcaj.]
  - (receives=Tirannwn quiver 1)
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: Háblame del Sistema de Logros.
    - **Elf Tracker:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
    - **Elf Tracker:** Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
    - **Elf Tracker:** Algunos también ofrecen elementos que ayudarán a completar otras tareas y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
    - [Menu]: Elige una opción:
      - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
        - **Player:** Cuéntame sobre la recompensa establecida para esta área.
        - **Elf Tracker:** Por completar el conjunto Tirannwn, se te presenta un carcaj.
        - **Elf Tracker:** Este carcaj será cada vez más útil a medida que completes conjuntos de tareas de mayor dificultad.
        - **Elf Tracker:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
        - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
        - (previous)
      - [Choice]: ¿Cómo reclamo estas recompensas?
        - **Player:** ¿Cómo reclamo las recompensas?
        - **Elf Tracker:** Debes completar todas las tareas dentro de un conjunto de dificultad particular y luego podrás reclamar tu recompensa.
        - **Elf Tracker:** Algunas de las tareas del conjunto Tirannwn son simples, algunas requieren cierto skill levels y otras requieren que se inicien o completen misiones.
        - **Elf Tracker:** Para reclamar las recompensas del conjunto Tirannwn, habla con Gwir en Lletya, Arianwyn en la ciudad, Elen en la ciudad o conmigo mismo.
        - (previous)
      - [Choice]: Lo siento, me estaba yendo.
        - (end)
  - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
    - [Menu]: Elige una opción:
      - [Choice]: Tirannwn carcaj 1
        - **Elf Tracker:** Tirannwn carcaj 1? Sí, pero me temo que te costaría 5.000 coins.
        - [Menu]: ¿Comprar otro por 5.000 coins?
          - [Choice]: si
            - (receives=Tirannwn quiver 1) (removes= 5,000 coins)
            - [Te entregan otro carcaj Tirannwn 1.]
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Tirannwn carcaj 2
        - **Elf Tracker:** ¿Tirannwn carcaj 2? Sí, pero me temo que te costaría 10.000 coins.
        - [Menu]: ¿Comprar otro por 10.000 coins?
          - [Choice]: si
            - (receives=Tirannwn quiver 2) (removes= 10,000 coins)
            - [Te entregan otro carcaj Tirannwn 2.]
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Tirannwn carcaj 3
        - **Elf Tracker:** Tirannwn carcaj 3? Sí, pero me temo que te costaría 25.000 coins.
        - [Menu]: ¿Comprar otro por 25.000 coins?
          - [Choice]: si
            - (receives=Tirannwn quiver 3) (removes= 25,000 coins)
            - [Te entregan otro carcaj Tirannwn 3.]
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Tirannwn carcaj 4
        - **Elf Tracker:** Tirannwn carcaj 4? Sí, pero me temo que te costaría 50.000 coins.
        - [Menu]: ¿Comprar otro por 50.000 coins?
          - [Choice]: si
            - (receives=Tirannwn quiver 4) (removes= 50,000 coins)
            - [Te entregan otro carcaj Tirannwn 4.]
          - [Choice]: No
            - **Player:** No, gracias.
  - [Choice]: Lo siento, me estaba yendo.
    - (end)
