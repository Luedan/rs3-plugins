# Doctor Orbon

- **Original Wiki Page**: [Transcript:Doctor Orbon](https://runescape.wiki/w/Transcript%3ADoctor%20Orbon)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue before Sheep Herder

- **Player:** Hola.
- **Doctor Orbon:** ¿Cómo te sientes? ¿No tienes gripe fuerte, escalofríos, náuseas o pérdida de apetito?
- **Player:** Uh... no... Me siento bien...
- **Doctor Orbon:** ¿Qué tal las pesadillas entonces? ¿Tiene algún problema con pesadillas especialmente aterradoras?
- **Player:** No... no desde que era joven.
- **Doctor Orbon:** Bien, bien, tenía que asegurarme. Esta plaga realmente tiene una tasa de contagio increíblemente rápida. ¡Se propaga más rápido que el resfriado común!
- [Menu]: Selecciona una opción
  - [Choice]: ¿La plaga? Cuéntame más.
    - **Player:** ¿La plaga? Cuéntame más.
    - **Doctor Orbon:** Vino de alguna parte del oeste. Se propaga extremadamente rápido y es absolutamente mortal.
    - **Player:** ¿Cuáles son los síntomas?
    - **Doctor Orbon:** Varía ligeramente de un caso a otro, pero generalmente tiene pesadillas anormales y síntomas parecidos a los de la gripe, que progresan a medida que sucumbe más. Con el tiempo, resulta en la presencia de una sustancia espesa y negra parecida al alquitrán secretada por la nariz y los ojos.
  - [Choice]: Está bien, tendré cuidado.
    - **Player:** Está bien, tendré cuidado.
    - **Doctor Orbon:** Tú haces ese aventurero. No querrás infectarte con la peste.

### Between Sheep Herder and Plague's End

- [Menu]: Selecciona una opción
  - [Choice]: Acerca del sistema de tareas...
    - (below|task)
  - [Choice]: Habla de otra cosa.
    - (Condition: If not wearing mourner gear:)
      - **Doctor Orbon:** Bueno, hola de nuevo. Me sentí muy aliviado cuando supe que había logrado deshacerse de las ovejas plagadas con éxito. Significa que nuestra cuarentena está funcionando nuevamente.
    - (Condition: If wearing a full set of mourner gear:)
      - **Player:** Hola.
      - **Doctor Orbon:** Buen día, ¿tienes mi próximo pago? No sigo esta farsa por diversión, ¿sabes?
      - **Player:** Lo siento, no.
      - **Doctor Orbon:** Bueno, si lo mencionaras la próxima vez que veas el Head Mourner, te lo agradeceríamos.
      - **Player:** Lo tendré en cuenta.

### After Plague's End

- [Menu]: Selecciona una opción
  - [Choice]: Acerca del sistema de tareas...
    - (below|task)
  - [Choice]: Habla de otra cosa.
    - (Condition: If not wearing mourner gear:)
      - **Doctor Orbon:** Estaba medio muerto de preocupación por esa plaga, ¡y ahora resulta que era un engaño que involucraba ovejas teñidas! No sé por qué no me di cuenta de eso. Quizás no soy el médico que pensaba.
    - (Condition: If wearing a full set of mourner gear:)
      - **Doctor Orbon:** Sabía que no podríamos seguir con esta farsa para siempre. Maldice a ese aventurero entrometido.
      - **Doctor Orbon:** Harías bien en huir de West Ardougne antes de que los ciudadanos te hagan cosas desagradables.

### {{anchor|task}}About the Task System

- (Condition: If the player has completed the Easy tasks in the Ardougne set and the reward is not yet claimed:)
  - **Player:** He completado todas las tareas fáciles del conjunto Ardougne.
  - **Doctor Orbon:** Ah, eso es un alivio. Puedes usar un Ardougne cloak ahora; tengo uno para ti.
  - [Doctor Orbon te entrega una capa y una lámpara vieja.]
  - ¡Ahora tienes un teletransporte al monasterio Kandarin en tu libro de habilidades!
  - **Doctor Orbon:** Es extraña esa capa. Estoy seguro de que tiene poderes mágicos. Las personas como los vendedores del mercado no parecen darse cuenta de que hacen ciertas... cosas cuando lo usan. Verás a qué me refiero cuando te lo pruebes. Oh, también hay una lámpara aquí que encontré en el almacén; puede que le encuentres utilidad.
  - **Player:** ¡Gracias! ¿Qué más hace?
  - **Doctor Orbon:** Bueno, ahora parece poder teletransportarte al monasterio al sur de Ardougne, aunque no sé por qué querrías visitar a esos monjes borrachos. Estoy seguro de que hay otros bonos de los que no he oído hablar, pero tal vez puedas encontrarlos.
  - (continue)
- (Condition: If the player has lost their Ardougne cloak 1:)
  - **Doctor Orbon:** ¿Tú otra vez? ¿Cómo te fue con la capa?
  - **Player:** Lo perdí.
  - **Doctor Orbon:** ¿Lo perdiste? Bueno, da la casualidad de que encontré otro. Cuida mejor este.
  - (receives=Ardougne cloak 1)
  - [Doctor Orbon te entrega una capa.]
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: Háblame del Sistema de Logros.
    - **Doctor Orbon:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
    - **Doctor Orbon:** Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
    - **Doctor Orbon:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
    - [Menu]: Elige una opción:
      - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
        - **Player:** Cuéntame sobre la recompensa establecida para esta localidad.
        - **Doctor Orbon:** Por completar el conjunto Ardougne, se te presenta una capa.
        - **Doctor Orbon:** Esta capa será cada vez más útil con cada nivel de dificultad del conjunto que completes.
        - **Doctor Orbon:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
        - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
        - (previous2)
      - [Choice]: ¿Cómo reclamo las recompensas?
        - **Player:** ¿Cómo reclamo las recompensas?
        - **Doctor Orbon:** Debes completar todas las tareas de un conjunto de una dificultad particular y luego podrás reclamar tu recompensa.
        - **Doctor Orbon:** Algunas de las tareas del conjunto Ardougne son simples, algunas requerirán skill levels y otras pueden requerir que se inicien o completen misiones.
        - **Doctor Orbon:** Para reclamar las recompensas de la tarea Ardougne, habla con town crier de Ardougne, Aleck en Yanille o conmigo mismo.
        - (previous2)
      - [Choice]: Lo siento, me estaba yendo.
        - (end)
  - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
  - [Menu]: Elige una opción:
    - [Choice]: Ardougne cloak 1
      - **Doctor Orbon:** Ardougne cloak 1? Sí, pero me temo que te costaría 1.500 coins.
      - [Menu]: ¿Comprar otro por 1.500 coins?
        - [Choice]: si
          - [Te entregan otro Ardougne cloak 1.]
          - (receives=Ardougne cloak 1) (removes= 1,500 coins)
        - [Choice]: No
          - **Player:** No, gracias.
    - [Choice]: Ardougne cloak 2
      - **Doctor Orbon:** Ardougne cloak 2? Sí, pero me temo que te costaría 2500 coins.
      - [Menu]: ¿Comprar otro por 2500 coins?
        - [Choice]: si
          - [Te entregan otro Ardougne cloak 2.]
          - (receives=Ardougne cloak 2) (removes= 2,500 coins)
        - [Choice]: No
          - **Player:** No, gracias.
    - [Choice]: Ardougne cloak 3
      - **Doctor Orbon:** Ardougne cloak 3? Sí, pero me temo que te costaría 7.500 coins.
      - [Menu]: ¿Comprar otro por 7.500 coins?
        - [Choice]: si
          - [Te entregan otro Ardougne cloak 3.]
          - (receives=Ardougne cloak 3) (removes= 7,500 coins)
        - [Choice]: No
          - **Player:** No, gracias.
    - [Choice]: Ardougne cloak 4
      - **Doctor Orbon:** Ardougne cloak 4? Sí, pero me temo que te costaría 15.000 coins.
      - [Menu]: ¿Comprar otro por 15.000 coins?
        - [Choice]: si
          - [Te entregan otro Ardougne cloak 4.]
          - (receives=Ardougne cloak 4) (removes= 15,000 coins)
        - [Choice]: No
          - **Player:** No, gracias.
  - [Choice]: cond=If at least the hard Ardougne achievements are completed and the rewards claimed|Me gustaría cambiar mi punto de teletransporte.
    - **Player:** Me gustaría cambiar mi punto de teletransporte de Watchtower.
    - [Menu]: ¿Alternar teletransporte de Watchtower a [Watchtower/Yanille]?
      - [Choice]: si
        - Watchtower Teleport ahora te teletransportará al [Watchtower/centre of Yanille].
      - [Choice]: No
        - (end)
  - [Choice]: Lo siento, me estaba yendo.
    - (end)
