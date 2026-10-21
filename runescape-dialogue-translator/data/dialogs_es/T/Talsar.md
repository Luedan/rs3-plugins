# Talsar

- **Original Wiki Page**: [Transcript:Talsar](https://runescape.wiki/w/Transcript%3ATalsar)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|Needs dialogue for all location hints for each sinkhole spawn point}}

### Standard dialogue

- **Talsar:** Hola. Este lugar... me sorprende y me aterroriza, de verdad. Pensar que lugares así pueden existir en primer lugar... Que los dioses sean misericordiosos.
- {{anchor|initial-menu}}[Menú]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Talsar:** Me llamo Talsar. Soy un vidente de Rellekka. Cuando me enteré de lo que mi gente encontró aquí, tuve una visión. Sabía que aquí había algo para mí.
    - **Talsar:** Así que viajé hasta aquí y al llegar sentí una conexión con este lugar. Puedo sentir su poder retorciéndose, doblándose, envolviéndome, incluso aquí afuera.
    - **Talsar:** Y fue entonces cuando me di cuenta de que podía sentir otros lugares que sentían lo mismo: existen otras mazmorras que son como aquí. Los entiendo rápidamente, pero creo que pueden ser lugares que interesen a aventureros como tú.
    - (initial)
  - [Choice]: ¿De qué estás hablando?{{anchor|what}}
    - **Talsar:** Cuando escuché sobre este lugar, viajé hasta aquí desde Rellekka. Al principio pensamos que este lugar era único, pero hay otras mazmorras similares en todo el mundo.
    - **Talsar:** La mayor parte del tiempo están ocultos bajo la superficie del mundo, pero ocasionalmente se abren paso. Tengo la sensación de que han estado escondidos durante mucho tiempo pero que la magia que los rodea se ha debilitado, permitiéndonos encontrarlos.
    - **Talsar:** Algunos de los guerreros Fremennik viajaron a uno de ellos y encontraron una mazmorra llena de tesoros, pero no pudieron atravesar la puerta para llegar a ella.
    - **Talsar:** Dicen que alguien más estaba allí, una criatura como las que hay dentro de Daemonheim, pero cuando Thok amenazó con golpearlo, desapareció y no llegamos más lejos.
    - **Talsar:** Ahí es donde entras tú. Creo que si pudiéramos hacer que esa criatura hablara, podríamos entrar en esa sala del tesoro y tomar lo que sea que haya allí.
    - (initial)
  - [Choice]: ¿Dónde aparecerá el próximo sumidero?
    - **Player:** ¿Dónde aparecerá el próximo sumidero?
      - (Si está en un mundo de miembros:)
        - **Talsar:** Intentemos ver...
        - (Action: Talsar golpea su bastón y una luz azul brilla debajo de él.)
        - (Condition: Si está cerca de Barbarian Outpost:)
          - **Talsar:** El próximo sumidero aparecerá cerca de donde los bárbaros entrenan su agilidad en aproximadamente [número] minutos.
        - (Condition: Si está cerca de los Túmulos:)
          - **Talsar:** El próximo sumidero aparecerá cerca de donde yacen varios hermanos famosos en aproximadamente [número] minutos.
        - (Condition: De lo contrario:)
          - **Talsar:** El próximo sumidero aparecerá [location hint] en aproximadamente [número] minutos.
      - (Si estás en un mundo gratuito:)
        - Debes estar en el servidor de un miembro para atacar los sumideros.
  - [Choice]: Más...
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué opinas de este lugar?
        - **Talsar:** Hay algo aterrador, pero relajante, en este lugar. Lo sé, lo sé, no tiene sentido ¿verdad?
        - **Talsar:** El poder que puedo sentir aquí es embriagador, pero finalmente siento que he encontrado un propósito aquí. Puedo usar mi don para mi gente y mantenerlos a salvo dentro de Daemonheim.
        - **Talsar:** Por supuesto, eso significa que tengo que aguantar a ciertas personas que pueden volverte loco.
        - **Player:** ¿Qué quieres decir?
        - **Talsar:** Estoy seguro de que has tenido el placer de conocer a ese loco, Skaldrun, que despotrica sobre vivir durante siglos y contar esos cuentos fantásticos.
        - **Talsar:** Honestamente, nunca había conocido a un hombre tan exasperante.
        - (initial)
      - [Choice]: Acerca del sistema de tareas...{{anchor|task-system}}
        - (Condition: En un mundo gratuito:)
          - **Talsar:** Me temo que necesitarás ser miembro para reclamar cualquier recompensa por la tarea establecida.
        - (Condition: Si el player ha completado los logros difíciles de Daemonheim y no se han reclamado las recompensas:)
          - **Player:** He completado todas las tareas difíciles del conjunto Daemonheim.
          - **Talsar:** Así que sí.
          - [Talsar te entrega un aura, 38.000 fichas Dungeoneering y una lámpara.]
          - **Talsar:** Ahí lo tienes. Ahora puedes atravesar la barrera mágica en la mazmorra de recursos de Dwarven Mine.
          - **Player:** ¡Gracias! ¿Qué más puedo hacer?
          - **Talsar:** Debido a que completó el conjunto de tareas difíciles, habrá ganado 2 espacios de enlace más en su grupo de enlaces. También hablé con Gorajo Hoardstalker y deberías obtener más recompensas por completar los juegos de Sinkhole.
          - **Talsar:** Marmaros también ha aceptado ofrecerte un pequeño descuento cuando recargues tus artículos.
          - **Thok of Daemonheim:** ¡Oye! ¿Talsar cree que la cabeza de una persona pequeña es lo suficientemente gruesa como para aprender de Thok?
          - **Talsar:** Erm...yo...¿creo que sí?
          - **Thok of Daemonheim:** Entonces Thok enseña.
          - Thok te ha enseñado una pálida sombra de su formidable cabezazo. <br>Puedes usarlo en lugar de la habilidad de revés. Puedes activar esto desde el Armario.
          - (continue)
        - [Menu]: Elige una opción:
          - [Choice]: Háblame del Sistema de Logros.
            - **Talsar:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
            - **Talsar:** Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
            - **Talsar:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
            - [Menu]: Elige una opción:
              - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
                - **Player:** Cuéntame sobre la recompensa establecida para esta área.
                - **Talsar:** Al completar el conjunto Daemonheim, se te presenta un aura.
                - **Talsar:** Esta aura será cada vez más útil a medida que completes conjuntos de tareas de mayor dificultad.
                - **Talsar:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
                - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
                - (previous2|task-system)
              - [Choice]: ¿Cómo reclamo estas recompensas?
                - **Player:** ¿Cómo reclamo las recompensas?
                - **Talsar:** Debes completar todas las tareas dentro de un conjunto en particular y luego podrás reclamar tu recompensa.
                - **Talsar:** Algunas de las tareas del conjunto Daemonheim son simples, algunas requieren cierto skill levels y otras requieren que se inicien o completen misiones.
                - **Talsar:** Para reclamar las recompensas del conjunto Daemonheim, habla con Drangund, Dungeoneering Tutor, Marmaros the Rewards trader, Thok o conmigo mismo.
                - (previous2|task-system)
          - [Choice]: Lo siento, me estaba yendo.
            - (end)

### When a sinkhole is active

- (Condition: Si falta aproximadamente un minuto antes de que aparezca el sumidero:)
  - **Talsar:** ¡Lo siento! ¡Un socavón está a punto de aparecer en la superficie en 1 minuto! Puedo teletransportarte allí, si lo deseas.
  - (continue)
- (Condition: Si aparece el sumidero:)
  - **Talsar:** ¡Lo siento! Un socavón... ¡Hay otro en la superficie! Puedo teletransportarte allí, si lo deseas.
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: Sí.
    - (Action: el player es teletransportado a la entrada del sumidero.)
  - [Choice]: No.
    - **Talsar:** Esa es tu decisión, supongo, pero creo que vale la pena investigar cualesquiera que sean estos lugares.
  - [Choice]: ¿De qué estás hablando?
    - (above|what)
  - [Choice]: Acerca del sistema de tareas...
    - (above|task-system)

### Teleport option

- (Condition: Si el socavón está a punto de aparecer:)
  - (Condition: Si el sumidero está a punto de aparecer dentro de varios minutos:)
    - **Talsar:** El sumidero no aparecerá hasta dentro de [número] minutos. ¿Estás seguro de que quieres teletransportarte allí ahora?
    - (continue)
  - (Condition: Si el sumidero está a punto de aparecer en un minuto:)
    - **Talsar:** El sumidero no aparecerá hasta dentro de un minuto. ¿Estás seguro de que quieres teletransportarte allí ahora?
    - (continue)
  - [Menu]: ¿Teletransportarse al sumidero?
    - [Choice]: Sí.
      - (Action: el player es teletransportado a la entrada del sumidero.)
    - [Choice]: No.
      - (end)
- (Condition: Si el socavón no está a punto de aparecer:)
  - **Talsar:** Por desgracia, no hay sumideros en la superficie en este momento. ¿Había algo más que quisieras?
  - (above|initial-menu)
