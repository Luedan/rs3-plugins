# Marmaros the rewards trader

- **Original Wiki Page**: [Transcript:Marmaros the rewards trader](https://runescape.wiki/w/Transcript%3AMarmaros%20the%20rewards%20trader)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At Daemonheim

- **Comerciante de recompensas:** Oh, hola, no vi...
- **Player:** Hola. ¿Me preguntaba si podrías ayudarme?
- **Comerciante de recompensas:** ¿Ayuda? Uh... no estoy seguro de poder... uh...
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Comerciante de recompensas:** Yo soy... Yo solía ser...
    - **Player:** ¿Sí?
    - **Comerciante de recompensas:** Solo me encargo del... uh... equipo.
    - **Player:** Quiero decir, ¿quién eres? ¿Cómo te llamas?
    - **Comerciante de recompensas:** ¿Un nombre? Yo... eh...
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Me estás volviendo loco.
        - **Player:** Me estás volviendo loco.
        - **Comerciante de recompensas:** Lo siento. Yo soy...
        - **Player:** ¿Sí?
        - **Comerciante de recompensas:** Me llamaron Ma...
        - **Player:** ¿Malcolm? ¿Mandrágora? Ma... um... ¿Mango?
        - **Comerciante de recompensas:** Uh, no, esas no están del todo bien.
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: ¿Mencionaste algo sobre el equipo?
            - **Player:** ¿Mencionaste algo sobre el equipo?
            - **Comerciante de recompensas:** Sí, lo hice, tienes razón. Vendo cosas, reparo cosas. ¿Qué te interesa?
            - (continue|shop-opts)
          - [Choice]: Ya terminé contigo.
            - (below|done)
      - [Choice]: ¿Mencionaste algo sobre el equipo?
        - **Player:** ¿Mencionaste algo sobre el equipo?
        - **Comerciante de recompensas:** Sí... uh... Lo hice, tienes toda la razón. Vendo cosas, reparo cosas. ¿Qué te interesa?
        - [Menu]: ¿Qué te gustaría decir?{{anchor|shop-opts}}
          - [Choice]: Entonces, veamos qué vendes.
            - (opens=Daemonheim Rewards)
          - [Choice]: ¿Qué puedes reparar exactamente?
            - **Player:** ¿Qué puedes reparar exactamente?
            - **Comerciante de recompensas:** Armas, supongo. Me volví bueno remendando... allí. Si me compras algo, debería poder repararlo si está... uh... degradado. Muéstramelo y veré qué se puede hacer.
            - **Comerciante de recompensas:** Siento... que puedo confiar en usted. Déjame decirte algo: tengo un amigo ahí dentro, alguien que me trae herramientas y elementos de ese lugar. Así es como puedo ofrecerles servicios que otros... no pueden. No se lo digas a nadie. Por favor.
          - [Choice]: Ya terminé contigo.
            - (below|done)
      - [Choice]: Ya terminé contigo.
        - (below|done)
  - [Choice]: Ya terminé contigo.{{anchor|done}}
    - **Player:** Ya terminé contigo.
    - **Comerciante de recompensas:** Bien, bien, bien. Estaré aquí.
  - [Choice]: Acerca del sistema de tareas...
    - (Condition: En un mundo gratuito:)
      - **Comerciante de recompensas:** Me temo que necesitarás ser miembro para reclamar cualquier recompensa por la tarea establecida.
    - (Condition: Si el player ha completado los logros medios de Daemonheim y no se han reclamado las recompensas:)
      - **Player:** He completado todas las tareas medianas del conjunto Daemonheim.
      - **Comerciante de recompensas:** Así es. He mejorado el aura para ti.
      - [Marmaros te entrega un aura, 2000 fichas Dungeoneering y una lámpara.]
      - **Comerciante de recompensas:** Ahí lo tienes, que te proteja tan bien como Thok protege al suyo. Ah, y alguien me regaló esta lámpara, pero no me sirve para nada.
      - **Player:** ¡Gracias!
      - **Comerciante de recompensas:** Cuando uses el aura en Daemonheim, desperdiciarás menos flechas y triturarás huesos automáticamente. También te permitirá atravesar la barrera mágica cerca de los tejos hacia el este. Además de esto, porque usted
      - **Comerciante de recompensas:** completaste el conjunto de tareas medianas, ahora puedes vincular una poción y también hablé con el contrabandista, quien te ayudará con algunas runas para cada piso. Finalmente, descubrirás que tu anillo de parentesco se ha vuelto un poco más poderoso con su papel secundario.
      - (continue)
    - (Condition: Si el player no tiene recompensas para reclamar:)
      - [Menu]: Elige una opción:
        - [Choice]: Háblame del Sistema de Logros.
          - **Comerciante de recompensas:** Muy bien: el sistema de logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
          - **Comerciante de recompensas:** Puede ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
          - **Comerciante de recompensas:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
          - [Menu]: Elige una opción:
            - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
              - **Player:** Cuéntame sobre la recompensa establecida para esta área.
              - **Comerciante de recompensas:** Al completar el conjunto Daemonheim, se te presenta un aura.
              - **Comerciante de recompensas:** Esta aura será cada vez más útil a medida que completes conjuntos de tareas de mayor dificultad.
              - **Comerciante de recompensas:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
              - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
              - (previous2|about-tasks)
            - [Choice]: ¿Cómo reclamo estas recompensas?
              - **Player:** ¿Cómo reclamo las recompensas?
              - **Comerciante de recompensas:** Debes completar todas las tareas dentro de un conjunto de dificultad particular y luego podrás reclamar tu recompensa.
              - **Comerciante de recompensas:** Algunas de las tareas del conjunto Daemonheim son simples, algunas requieren cierto skill levels y otras requieren que se inicien o completen misiones.
              - **Comerciante de recompensas:** Para reclamar las recompensas del conjunto Daemonheim, hable con Drangund the Dungeoneering Tutor, Talsar, Thok o conmigo mismo.
              - (previous2|about-tasks)
            - [Choice]: Lo siento, me estaba yendo.
              - (end)
        - [Choice]: Lo siento, me estaba yendo.
          - (end)

#### Después del evento navideño de 2010

- (ver|Oh, pequeña ciudad de Daemonheim#Hablando con el comerciante de recompensas)
