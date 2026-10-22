# Gregorovic's Chosen

- **Original Wiki Page**: [Transcript:Gregorovic's Chosen](https://runescape.wiki/w/Transcript%3AGregorovic%27s%20Chosen)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Gregorovic's Chosen:** ¿Síiiiiiiiii?
- ((With an anima crystal in backpack:))
  - **Gregorovic's Chosen:** El cristal de Anima que tienes ahí es interesante. ¿Estarías dispuesto a donarlo?
  - [Menu]: ¿Entregar tu cristal de Anima?
    - [Choice]: Sí. (Gana 500 de reputación con Sliske)
      - (removes=anima crystal)
      - ¡Has ganado 500 de reputación con las fuerzas de Sliske!
      - (Condition: If new rewards were unlocked:)
        - (ver|Reputación (Corazón de Gielinor))
        - (continue)
      - **Gregorovic's Chosen:** Gracias por tu ayuda.
      - (continue)
    - [Choice]: No.
      - (continue)
- (Condition: With seals of opposing factions in backpack and under 2,000 Sliske reputation:)
  - **Gregorovic's Chosen:** Noté que tienes un stock de sellos de todo el Corazón. ¿Estarías interesado en donarlos?
  - **¿CAMBIAR SELLOS POR REPUTACIÓN CON LOS SLISKEANS?**
    - ((With Seals of the Cywir in backpack:))
      - Entregue los sellos Seren.
        - (Los sellos se intercambian por reputación).
        - ¡Tus Sellos de Cywir valían [número] reputación ante las fuerzas de Sliske!
        - (Condition: If new rewards were unlocked:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - ((With other seals of the opposing factions left:))
          - (above|seals)
        - ((Without other seals of the opposing factions left:))
          - (continue)
    - ((With Seals of the Furies in backpack:))
      - Entregue los sellos Zamorak.
        - (Los sellos se intercambian por reputación).
        - ¡Tus Sellos de las Furias valían [número] reputación ante las fuerzas de Sliske!
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
        - ¡Tus jinetes de los Sellos del Dragón valían [número] reputación con las fuerzas de Sliske!
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
          - ¡Tus Sellos de Cywir valían [número] reputación ante las fuerzas de Sliske!
          - (continue)
        - ((If Seals of the Furies were handed in:))
          - ¡Tus Sellos de las Furias valían [número] reputación ante las fuerzas de Sliske!
          - (continue)
        - ((If Seals of the Dragon riders were handed in:))
          - ¡Tus jinetes de los Sellos del Dragón valían [número] reputación con las fuerzas de Sliske!
          - (continue)
        - (Condition: If new rewards were unlocked:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - (continue)
    - No, gracias.
      - (continue)
- **SELECCIONA UNA OPCIÓN**
  - ¿Qué está pasando aquí?
    - **Gregorovic's Chosen:** Te encuentras en el Corazón de Gielinor, aventurero. Aquí los indefensos secuaces de Zamorak, Seren y Zaros se enfrentan al implacable ataque de las fuerzas de Sliske. Incluso nos guía el arma secreta de Sliske, la más terrible de todas: Gregorovic, el sin rostro.
    - **Player:** ¿Por qué están todos aquí parados? ¿No deberías estar peleando?
    - **Gregorovic's Chosen:** No todos somos salvajes. Sobre esta plataforma se ha establecido una tregua que nos permite a nosotros, los enviados de cada facción, utilizar palabras en lugar de violencia para influir en nuevos reclutas. Porque abajo la batalla continúa, por lo que debemos hacer lo que podamos para persuadir a los mercenarios que se unen a la refriega para que luchen por nuestra causa. Echa un vistazo a lo que tengo para ofrecerte. Te lo aseguro, haré que valga la pena luchar por Sliske.
    - (previous)
  - ¿Cuál es tu opinión sobre mí?
    - ((Sliske Reputation Rewards interface opens.))
  - ¿Cómo puedo mejorar mi reputación?
    - **Gregorovic's Chosen:** Hay algunas formas de mejorar tu posición. Lo más fácil que puedes hacer es derrotar a nuestros enemigos y usar fragmentos de Ingresión para pedir refuerzos para nosotros. El maestro de recompensas de allí, Feng, también puede ayudarte a mejorar tu posición ofreciéndote recompensas. Habla con él si quieres saber más. Ah, y estoy seguro de que si de alguna manera pudieras encontrar una manera de derrotar a los generales de las otras facciones, eso sin duda te haría ganar mucho favor.
    - (previous)
  - ¿Dónde puedo conseguir una armadura así?
    - **Gregorovic's Chosen:** Puedes recolectar fragmentos de armadura y crestas alrededor del Corazón que luego se pueden combinar para crear una armadura similar a la mía. Si me demuestras tu valía, puedo mostrarte cómo mejorarlo aún más y desbloquear su verdadero potencial.
    - (previous)
  - Me gustaría reclamar mis recompensas.
    - ((If you currently have no rewards to claim:))
      - **Gregorovic's Chosen:** No hay nada que pueda darte.
      - (previous)
    - ((With rewards to claim:))
      - (Condition: Without free backpack space:)
        - **Gregorovic's Chosen:** No tienes suficiente espacio en tu inventario.
        - (previous2)
      - (Condition: With free backpack space:)
        - [Menu]: Elige una opción:
          - [Choice]: Me gustaría reclamar mi insignia.
            - (receives=Sliske insignia)
            - [Gregorovic's Chosen te entrega una insignia de Sliske.]
            - (previous2)
          - [Choice]: cond=With the faction specific toy unlocked:|Me gustaría recuperar mi juguete.
            - (receives=mysterious bottle)
            - [Gregorovic's Chosen te entrega una botella misteriosa.]
            - (previous2)
          - [Choice]: No importa.
            - (previous2)

### Reputation

- ((Sliske Reputation Rewards interface opens.))

### Reclaim

- (above|reclaim)

### Attempting to use a seal of opposing faction with 2,000 Sliske reputation

- [No puedes ganar más reputación con esa facción.]
