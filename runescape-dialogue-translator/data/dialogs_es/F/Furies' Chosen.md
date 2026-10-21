# Furies' Chosen

- **Original Wiki Page**: [Transcript:Furies' Chosen](https://runescape.wiki/w/Transcript%3AFuries%27%20Chosen)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Furies' Chosen:** Bienvenido, mortal.
- ((Con un cristal de anima en backpack:))
  - **Furies' Chosen:** El cristal de Anima que tienes ahí es interesante. ¿Estarías dispuesto a donarlo?
  - [Menu]: ¿Entregar tu cristal de Anima?
    - [Choice]: Sí. (Gana 500 de reputación con Zamorak)
      - (removes=anima crystal)
      - (Condition: Sin reputación de 5000 Zamorak:)
        - ¡Has ganado 500 puntos de reputación con las fuerzas zamorakianas!
        - (Condition: Si se desbloquearan nuevas recompensas:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - (continue)
      - **Furies' Chosen:** Gracias por tu ayuda.
      - (continue)
    - [Choice]: No.
      - (continue)
- (Condition: Con sellos de facciones opuestas en backpack y menos de 2000 reputación en Zamorak:)
  - **Furies' Chosen:** Noté que tienes un stock de sellos de todo el Corazón. ¿Estarías interesado en donarlos?
  - **¿CAMBIAR SELLOS POR REPUTACIÓN CON LOS ZAMORAKIANOS?**
    - ((Con Sellos del Cywir en backpack:))
      - Entregue los sellos Seren.
        - (Los sellos se intercambian por reputación).
        - ¡Tus Sellos de Cywir valían [número] reputación ante las fuerzas zamorakianas!
        - (Condition: Si se desbloquearan nuevas recompensas:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - ((Con otros sellos de las facciones opuestas restantes:))
          - (above|seals)
        - ((Sin otros sellos de las facciones opuestas quedaron:))
          - (continue)
    - ((Con Sellos de los Sin Rostro en backpack:))
      - Entregue los sellos Sliske.
        - (Los sellos se intercambian por reputación).
        - ¡Tus Sellos de los sin rostro valían [número] reputación ante las fuerzas zamorakianas!
        - (Condition: Si se desbloquearan nuevas recompensas:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - ((Con otros sellos de las facciones opuestas restantes:))
          - (above|seals)
        - ((Sin otros sellos de las facciones opuestas quedaron:))
          - (continue)
    - ((Con los jinetes de Seals of the Dragon en backpack:))
      - Entrega de sellos de Zaros
        - (Los sellos se intercambian por reputación).
        - ¡Tus jinetes de los Sellos del Dragón valían [número] reputación con las fuerzas zamorakianas!
        - (Condition: Si se desbloquearan nuevas recompensas:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - ((Con otros sellos de las facciones opuestas restantes:))
          - (above|seals)
        - ((Sin otros sellos de las facciones opuestas quedaron:))
          - (continue)
    - ((Con múltiples tipos de sellos de facciones opuestas en backpack:))
      - Entregue todos los sellos.
        - (Los sellos se intercambian por reputación).
        - ((Si se entregaron los Sellos del Cywir:))
          - ¡Tus Sellos de Cywir valían [número] reputación ante las fuerzas zamorakianas!
          - (continue)
        - ((Si se entregaron los Sellos de los Sin Rostro:))
          - ¡Tus Sellos de los sin rostro valían [número] reputación ante las fuerzas zamorakianas!
          - (continue)
        - ((Si se entregaron los jinetes de los Sellos del Dragón:))
          - ¡Tus jinetes de los Sellos del Dragón valían [número] reputación con las fuerzas zamorakianas!
          - (continue)
        - (Condition: Si se desbloquearan nuevas recompensas:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - (continue)
    - No, gracias.
      - (continue)
- **SELECCIONA UNA OPCIÓN**
  - ¿Qué está pasando aquí?
    - **Furies' Chosen:** Te encuentras en el Corazón de Gielinor, aventurero. ¡Escucha los gritos y disfruta del caos del campo de batalla mientras las fuerzas de Zamorak luchan contra los viles secuaces de Zaros, Sliske y Seren! Liderándonos a la batalla están las feroces Furias Gemelas: Avaryss la incesante y Nymora la vengativa.
    - **Player:** ¿Por qué están todos aquí parados? ¿No deberías estar peleando?
    - **Furies' Chosen:** No todos somos salvajes. Sobre esta plataforma se ha establecido una tregua que nos permite a nosotros, los enviados de cada facción, utilizar palabras en lugar de violencia para influir en nuevos reclutas. Porque abajo la batalla continúa, por lo que debemos hacer lo que podamos para persuadir a los mercenarios que se unen a la refriega para que luchen por nuestra causa. Echa un vistazo a lo que tengo para ofrecerte. Te lo aseguro, haré que valga la pena luchar por Zamorak.
    - (previous)
  - ¿Cuál es tu opinión sobre mí?
    - ((Se abre la interfaz de Recompensas de reputación de Zamorak.))
  - ¿Cómo puedo mejorar mi reputación?
    - **Furies' Chosen:** Hay algunas formas de mejorar tu posición. Lo más fácil que puedes hacer es derrotar a nuestros enemigos y usar fragmentos de Ingresión para pedir refuerzos para nosotros. El maestro de recompensas de allí, Feng, también puede ayudarte a mejorar tu posición ofreciéndote recompensas. Habla con él si quieres saber más. Ah, y estoy seguro de que si de alguna manera pudieras encontrar una manera de derrotar a los generales de las otras facciones, eso sin duda te haría ganar mucho favor.
    - (previous)
  - ¿Dónde puedo conseguir una armadura así?
    - **Furies' Chosen:** Puedes recolectar fragmentos de armadura y crestas alrededor del Corazón que luego se pueden combinar para crear una armadura similar a la mía. Si me demuestras tu valía, puedo mostrarte cómo mejorarlo aún más y desbloquear su verdadero potencial.
    - (previous)
  - Me gustaría reclamar mis recompensas.
    - ((Si actualmente no tienes recompensas para reclamar:))
      - **Furies' Chosen:** No hay nada que pueda darte.
      - (previous)
    - ((Con recompensas para reclamar:))
      - **ELIGE UNA OPCIÓN:**
        - Me gustaría reclamar mi insignia.
          - Furies' Chosen te entrega una insignia de Zamorak.
          - (previous2)
        - No importa.
          - (previous2)

### Reputation

- ((Se abre la interfaz de Recompensas de reputación de Zamorak.))

### Reclaim

- (above|reclaim)

### Using anima crystal

- **Furies' Chosen:** El cristal de Anima que tienes ahí es interesante. ¿Estarías dispuesto a donarlo?
- [Menu]: ¿Entregar tu cristal de Anima?
  - [Choice]: Sí. (Gana 500 de reputación con Zamorak)
  - (removes=anima crystal)
  - ¡Has ganado 500 puntos de reputación con las fuerzas zamorakianas!
  - ((Si los componentes de Avernic estuvieran desbloqueados:))
    - Ahora puede descubrir el plano de los componentes de Avernic si tiene al menos 89 Invention.
    - (continue)
  - ((Si Fury Wings estuviera desbloqueado:))
    - Has desbloqueado la anulación cosmética Fury Wings.
    - (continue)
  - **Furies' Chosen:** Gracias por tu ayuda.
  - [Choice]: No.
    - (end)

### Attempting to use a seal of opposing faction with 2,000 Zamorak reputation

- [No puedes ganar más reputación con esa facción.]
