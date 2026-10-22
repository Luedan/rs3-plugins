# Furies' Chosen

- **Original Wiki Page**: [Transcript:Furies' Chosen](https://runescape.wiki/w/Transcript%3AFuries%27%20Chosen)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Furies' Chosen:** Bienvenido, mortal.
- ((With an anima crystal in backpack:))
  - **Furies' Chosen:** El cristal de Anima que tienes ahí es interesante. ¿Estarías dispuesto a donarlo?
  - [Menu]: ¿Entregar tu cristal de Anima?
    - [Choice]: Sí. (Gana 500 de reputación con Zamorak)
      - (removes=anima crystal)
      - (Condition: Without 5,000 Zamorak reputation:)
        - ¡Has ganado 500 puntos de reputación con las fuerzas zamorakianas!
        - (Condition: If new rewards were unlocked:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - (continue)
      - **Furies' Chosen:** Gracias por tu ayuda.
      - (continue)
    - [Choice]: No.
      - (continue)
- (Condition: With seals of opposing factions in backpack and under 2,000 Zamorak reputation:)
  - **Furies' Chosen:** Noté que tienes un stock de sellos de todo el Corazón. ¿Estarías interesado en donarlos?
  - **¿CAMBIAR SELLOS POR REPUTACIÓN CON LOS ZAMORAKIANOS?**
    - ((With Seals of the Cywir in backpack:))
      - Entregue los sellos Seren.
        - (Los sellos se intercambian por reputación).
        - ¡Tus Sellos de Cywir valían [número] reputación ante las fuerzas zamorakianas!
        - (Condition: If new rewards were unlocked:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - ((With other seals of the opposing factions left:))
          - (above|seals)
        - ((Without other seals of the opposing factions left:))
          - (continue)
    - ((With Seals of the Faceless in backpack:))
      - Entregue los sellos Sliske.
        - (Los sellos se intercambian por reputación).
        - ¡Tus Sellos de los sin rostro valían [número] reputación ante las fuerzas zamorakianas!
        - (Condition: If new rewards were unlocked:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - ((With other seals of the opposing factions left:))
          - (above|seals)
        - ((Without other seals of the opposing factions left:))
          - (continue)
    - ((With Seals of the Dragon riders in backpack:))
      - Entrega de sellos de Zaros
        - (Los sellos se intercambian por reputación).
        - ¡Tus jinetes de los Sellos del Dragón valían [número] reputación con las fuerzas zamorakianas!
        - (Condition: If new rewards were unlocked:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - ((With other seals of the opposing factions left:))
          - (above|seals)
        - ((Without other seals of the opposing factions left:))
          - (continue)
    - ((With multiple types of opposing factions' seals in backpack:))
      - Entregue todos los sellos.
        - (Los sellos se intercambian por reputación).
        - ((If Seals of the Cywir were handed in:))
          - ¡Tus Sellos de Cywir valían [número] reputación ante las fuerzas zamorakianas!
          - (continue)
        - ((If Seals of the Faceless were handed in:))
          - ¡Tus Sellos de los sin rostro valían [número] reputación ante las fuerzas zamorakianas!
          - (continue)
        - ((If Seals of the Dragon riders were handed in:))
          - ¡Tus jinetes de los Sellos del Dragón valían [número] reputación con las fuerzas zamorakianas!
          - (continue)
        - (Condition: If new rewards were unlocked:)
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
    - ((Zamorak Reputation Rewards interface opens.))
  - ¿Cómo puedo mejorar mi reputación?
    - **Furies' Chosen:** Hay algunas formas de mejorar tu posición. Lo más fácil que puedes hacer es derrotar a nuestros enemigos y usar fragmentos de Ingresión para pedir refuerzos para nosotros. El maestro de recompensas de allí, Feng, también puede ayudarte a mejorar tu posición ofreciéndote recompensas. Habla con él si quieres saber más. Ah, y estoy seguro de que si de alguna manera pudieras encontrar una manera de derrotar a los generales de las otras facciones, eso sin duda te haría ganar mucho favor.
    - (previous)
  - ¿Dónde puedo conseguir una armadura así?
    - **Furies' Chosen:** Puedes recolectar fragmentos de armadura y crestas alrededor del Corazón que luego se pueden combinar para crear una armadura similar a la mía. Si me demuestras tu valía, puedo mostrarte cómo mejorarlo aún más y desbloquear su verdadero potencial.
    - (previous)
  - Me gustaría reclamar mis recompensas.
    - ((If you currently have no rewards to claim:))
      - **Furies' Chosen:** No hay nada que pueda darte.
      - (previous)
    - ((With rewards to claim:))
      - **ELIGE UNA OPCIÓN:**
        - Me gustaría reclamar mi insignia.
          - Furies' Chosen te entrega una insignia de Zamorak.
          - (previous2)
        - No importa.
          - (previous2)

### Reputation

- ((Zamorak Reputation Rewards interface opens.))

### Reclaim

- (above|reclaim)

### Using anima crystal

- **Furies' Chosen:** El cristal de Anima que tienes ahí es interesante. ¿Estarías dispuesto a donarlo?
- [Menu]: ¿Entregar tu cristal de Anima?
  - [Choice]: Sí. (Gana 500 de reputación con Zamorak)
  - (removes=anima crystal)
  - ¡Has ganado 500 puntos de reputación con las fuerzas zamorakianas!
  - ((If Avernic components were unlocked:))
    - Ahora puede descubrir el plano de los componentes de Avernic si tiene al menos 89 Invention.
    - (continue)
  - ((If Fury Wings were unlocked:))
    - Has desbloqueado la anulación cosmética Fury Wings.
    - (continue)
  - **Furies' Chosen:** Gracias por tu ayuda.
  - [Choice]: No.
    - (end)

### Attempting to use a seal of opposing faction with 2,000 Zamorak reputation

- [No puedes ganar más reputación con esa facción.]
