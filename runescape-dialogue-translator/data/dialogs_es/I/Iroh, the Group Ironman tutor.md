# Iroh, the Group Ironman tutor

- **Original Wiki Page**: [Transcript:Iroh, the Group Ironman tutor](https://runescape.wiki/w/Transcript%3AIroh%2C%20the%20Group%20Ironman%20tutor)
- **Letter**: `I`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Iroh, the Group Ironman tutor:** ¡Buenos días! ¿Qué quieres saber del Grupo Ironman?
- [Menu]: Elija una opción:|anchor=initialOpts
  - [Choice]: Cuéntame más sobre el modo Grupo Ironman.
    - **Iroh, the Group Ironman tutor:** Group Ironman te permite disfrutar de la experiencia Ironman en grupo de 2 a 5 amigos. Ya sabes, cuando quieras alejarte de todo, pero hazlo con alguien.
    - **Iroh, the Group Ironman tutor:** A medida que trabajen juntos y crezcan, podrán completar Journey Achievements.
    - **Iroh, the Group Ironman tutor:** Los logros del viaje son un conjunto de objetivos que el grupo puede completar como individuos y como grupo; necesitarás mejorar tus habilidades, completar misiones, matar jefes y explorar todo lo que Gielinor tiene para ofrecer.
    - **Iroh, the Group Ironman tutor:** Completar los logros del viaje desbloqueará recompensas como almacenamiento grupal, una armadura cosmética actualizable y gestos de pose únicos.
    - **Iroh, the Group Ironman tutor:** O puedes trazar tu propio camino y establecer tus propios objetivos mientras experimentas un nuevo tipo de aventura. La elección, como dicen, es tuya.
    - (previous|initialOpts)
  - [Choice]: ¿Cómo creo o me uno a un grupo?
    - **Iroh, the Group Ironman tutor:** ¡Es bastante simple realmente! Hay dos opciones: puedes iniciar tu propio grupo o ser invitado a un grupo existente.
    - **Iroh, the Group Ironman tutor:** Si desea crear su propio grupo, simplemente haga clic en la opción 'Crear grupo' y luego elija qué conjunto de reglas desea que sea su grupo.
    - **Iroh, the Group Ironman tutor:** Una vez que lo hayas decidido, podrás invitar a quien quieras a unirse a tu grupo. Cada grupo puede tener entre 2 y 5 jugadores.
    - Puedes invitar jugadores a tu grupo haciendo clic en el botón {{Contrast|c=#036|t='Invite to Group'}} y escribiendo el nombre de el player, o haciendo clic derecho en los jugadores y seleccionando {{Contrast|c=#036|t='Invite'}}.
    - **Iroh, the Group Ironman tutor:** Cada grupo puede tener su propio nombre único, así que elige el que mejor te represente.
    - **Iroh, the Group Ironman tutor:** ¡Entonces estás listo para comenzar! ¡Confirma tu grupo y cruza el puente hacia el portal que te llevará a Lumbridge para comenzar tu aventura!
    - **Iroh, the Group Ironman tutor:** No olvides recoger una armadura del puesto de al lado; te proporcionará cierta protección inicial contra cualquier enemigo al que te puedas enfrentar.
    - (previous|initialOpts)
  - [Choice]: ¿Cuáles son los diferentes conjuntos de reglas de grupo?
    - **Iroh, the Group Ironman tutor:** Hay dos conjuntos de reglas diferentes entre los que puedes elegir: Competitivo y Regular.
    - **Iroh, the Group Ironman tutor:** Competitivo es un conjunto de reglas estrictas en el que solo puedes jugar con tu grupo; esto significa que todo su progreso y logros provienen únicamente del grupo.
    - **Iroh, the Group Ironman tutor:** En Competitivo, solo se puede formar un grupo con aquellos nuevos en Gielinor para que puedas iniciar como grupo y demostrar que eres el mejor de los mejores.
    - **Iroh, the Group Ironman tutor:** Regular es un conjunto de reglas más relajado que te permite jugar con otras personas fuera de tu grupo y no hay restricciones para salir o unirte a otros grupos en el futuro.
    - **Iroh, the Group Ironman tutor:** Elige el modo que mejor represente a tu grupo. Los grupos competitivos pueden optar por convertirse en un grupo regular más adelante; sin embargo, un grupo Regular nunca puede convertirse en un grupo Competitivo una vez que el grupo haya sido finalizado.
    - (previous)
  - [Choice]: cond=If you are in a group:|¿Puedo cambiar mi modo de juego?
    - (Condition: Si previamente confirmaste que no quieres abandonar nunca el modo Ironman grupal:)
      - **Iroh, the Group Ironman tutor:** Me temo que no puedes cambiar tu modo de juego, ya que previamente has optado por no desactivar nunca el modo Group Ironman.
      - (previous|initialOpts)
    - **Iroh, the Group Ironman tutor:** ¡Por supuesto! ¿Qué te gustaría hacer?
    - [Menu]: Selecciona una opción
      - [Choice]: Cambia al modo Estándar (abandona permanentemente el modo Ironman grupal).
    - **Iroh, the Group Ironman tutor:** Muy bien. Te enviaré a Burthorpe donde mi viejo amigo, Turael, podrá guiarte a partir de este punto.
      - [Choice]: Nunca desactives el modo Grupo Ironman.
        - **Iroh, the Group Ironman tutor:** ¡Nunca significa nunca! ¿Estás seguro de que deseas {{colour|#EB2F2F|permanente}} evitar salir del modo Grupo Ironman?
        - [Menu]: ¿Nunca deshabilitas el modo Grupo Ironman?
          - [Choice]: Sí, NUNCA quiero desactivar el modo Ironman grupal.
            - **Iroh, the Group Ironman tutor:** ¿Estás absolutamente seguro de que deseas {{colour|#EB2F2F|permanente}} evitar salir del modo Grupo Ironman? Esto no se puede revertir.
            - [Menu]: ¿Confirmar que nunca se deshabilitó el modo Group Ironman?
              - [Choice]: Sí, NUNCA quiero desactivar el modo Ironman grupal.
                - **Iroh, the Group Ironman tutor:** Que así sea, siempre seguirás siendo un Ironman grupal.
                - **Player:** ¡Gracias!
                - (initial|initialOpts)
              - [Choice]: No, quiero poder salir del modo Ironman grupal.
                - (initial|initialOpts)
          - [Choice]: No, quiero poder salir del modo Ironman grupal.
            - (initial|initialOpts)
      - [Choice]: No importa.
        - (initial|initialOpts)
  - [Choice]: Adiós.
    - **Iroh, the Group Ironman tutor:** Adiós.
