# Helwyr's Chosen

- **Original Wiki Page**: [Transcript:Helwyr's Chosen](https://runescape.wiki/w/Transcript%3AHelwyr%27s%20Chosen)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Helwyr's Chosen:** Aventurero.
- ((Con un cristal de anima en backpack:))
  - **Helwyr's Chosen:** El cristal de Anima que tienes ahí es interesante. ¿Estarías dispuesto a donarlo?
  - [Menu]: ¿Entregar tu cristal de Anima?
    - [Choice]: Sí. (Gana 500 de reputación con Seren)
      - (removes=anima crystal)
      - **Helwyr's Chosen:** Gracias por tu ayuda.
      - (continue)
    - [Choice]: No.
      - (continue)
- (Condition: Con sellos de facciones opuestas en backpack y menos de 2000 reputación en Seren:)
  - **Helwyr's Chosen:** Noté que tienes un stock de sellos de todo el Corazón. ¿Estarías interesado en donarlos?
  - **¿CAMBIAR SELLOS POR REPUTACIÓN CON LOS SERENISTAS?**
    - ((Con Sellos de los Sin Rostro en backpack:))
      - Entregue los sellos Sliske.
        - (Los sellos se intercambian por reputación).
        - ¡Tus Sellos de los sin rostro valían [número] reputación ante las fuerzas serenistas!
        - (Condition: Si se desbloquearan nuevas recompensas:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - ((Con otros sellos de las facciones opuestas restantes:))
          - (above|seals)
        - ((Sin otros sellos de las facciones opuestas quedaron:))
          - (continue)
    - ((Con Sellos de las Furias en backpack:))
      - Entregue los sellos Zamorak.
        - (Los sellos se intercambian por reputación).
        - ¡Tus Sellos de las Furias valían [número] reputación ante las fuerzas serenistas!
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
        - ¡Tus jinetes de Seals of the Dragon valían [número] reputación con las fuerzas serenistas!
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
        - ((Si se entregaron los Sellos de los Sin Rostro:))
          - ¡Tus Sellos de los sin rostro valían [número] reputación ante las fuerzas serenistas!
          - (continue)
        - ((Si se entregaron los Sellos de las Furias:))
          - ¡Tus Sellos de las Furias valían [número] reputación ante las fuerzas serenistas!
          - (continue)
        - ((Si se entregaron los jinetes de los Sellos del Dragón:))
          - ¡Tus jinetes de Seals of the Dragon valían [número] reputación con las fuerzas serenistas!
          - (continue)
        - (Condition: Si se desbloquearan nuevas recompensas:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - (continue)
    - No, gracias.
      - (continue)
- **SELECCIONA UNA OPCIÓN**
  - ¿Qué está pasando aquí?
    - **Helwyr's Chosen:** Te encuentras en el Corazón de Gielinor, aventurero. ¡Este lugar es un campo de batalla brutal, pero los elfos debemos enfrentarlo si queremos luchar contra las hordas de Zamorak, Zaros y Sliske en nombre de Seren! Nuestro líder es el antiguo cazador Cywir Helwyr. Con su inigualable poder de cambio de forma al mando, no podemos fallar.
    - **Player:** ¿Por qué están todos aquí parados? ¿No deberías estar peleando?
    - **Helwyr's Chosen:** No todos somos salvajes. Sobre esta plataforma se ha establecido una tregua que nos permite a nosotros, los enviados de cada facción, utilizar palabras en lugar de violencia para influir en nuevos reclutas. Porque abajo la batalla continúa, por lo que debemos hacer lo que podamos para persuadir a los mercenarios que se unen a la refriega para que luchen por nuestra causa. Echa un vistazo a lo que tengo para ofrecerte. Te lo aseguro, haré que valga la pena luchar por Seren.
    - (previous)
  - ¿Cuál es tu opinión sobre mí?
    - ((Se abre la interfaz de Recompensas de reputación de Seren.))
  - ¿Cómo puedo mejorar mi reputación?
    - **Helwyr's Chosen:** Hay algunas formas de mejorar tu posición. Lo más fácil que puedes hacer es derrotar a nuestros enemigos y usar fragmentos de Ingresión para pedir refuerzos para nosotros. El maestro de recompensas de allí, Feng, también puede ayudarte a mejorar tu posición ofreciéndote recompensas. Habla con él si quieres saber más. Ah, y estoy seguro de que si de alguna manera pudieras encontrar una manera de derrotar a los generales de las otras facciones, eso sin duda te haría ganar mucho favor.
    - (previous)
  - ¿Dónde puedo conseguir una armadura así?
    - **Helwyr's Chosen:** Puedes recolectar fragmentos de armadura y crestas alrededor del Corazón que luego se pueden combinar para crear una armadura similar a la mía. Si me demuestras tu valía, puedo mostrarte cómo mejorarlo aún más y desbloquear su verdadero potencial.
    - (previous)
  - Me gustaría reclamar mis recompensas.
    - ((Si actualmente no tienes recompensas para reclamar:))
      - **Helwyr's Chosen:** No hay nada que pueda darte.
      - (previous)
    - ((Con recompensas para reclamar:))
      - (Condition: Sin espacio libre backpack:)
        - **Helwyr's Chosen:** No tienes suficiente espacio en tu inventario.
        - (previous2)
      - (Condition: Con espacio gratuito backpack:)
        - [Menu]: Elige una opción:
          - [Choice]: Me gustaría reclamar mi insignia.
            - (receives=Seren insignia)
            - [Helwyr's Chosen te entrega una insignia de Seren.]
            - (previous2)
          - [Choice]: cond=With the faction specific toy unlocked:|Me gustaría recuperar mi juguete.
            - (receives=daystone)
            - [Helwyr's Chosen te entrega una Daystone.]
            - (previous2)
          - [Choice]: No importa.
            - (previous2)

### Reputation

- ((Se abre la interfaz de Recompensas de reputación de Seren.))

### Reclaim

- (above|reclaim)

### Using a seal of the Cywir

- [No crees que a los elegidos les agradaría oír hablar de ese logro en particular.]
