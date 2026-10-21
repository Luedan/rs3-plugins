# Vindicta's Chosen

- **Original Wiki Page**: [Transcript:Vindicta's Chosen](https://runescape.wiki/w/Transcript%3AVindicta%27s%20Chosen)
- **Letter**: `V`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Vindicta's Chosen:** Saludos.
- ((Con un cristal de anima en backpack:))
  - **Vindicta's Chosen:** El cristal de Anima que tienes ahí es interesante. ¿Estarías dispuesto a donarlo?
    - Sí. (Gana 500 de reputación con Zaros)
      - (removes=anima crystal)
      - ¡Has ganado 500 de reputación con las fuerzas zarosianas!
      - (Condition: Si se desbloquearan nuevas recompensas:)
        - (ver|Reputación (Corazón de Gielinor))
        - (continue)
      - **Vindicta's Chosen:** Gracias por tu ayuda.
      - (continue)
    - No.
      - (continue)
- (Condition: Con sellos de facciones opuestas en backpack y menos de 2000 Zaros de reputación:)
  - **Vindicta's Chosen:** Noté que tienes un stock de sellos de todo el Corazón. ¿Estarías interesado en donarlos?
  - **¿CAMBIAR SELLOS POR REPUTACIÓN CON LOS ZAROSIANOS?**
    - ((Con Sellos del Cywir en backpack:))
      - Entregue los sellos Seren.
        - (Los sellos se intercambian por reputación).
        - ¡Tus Sellos de Cywir valían [número] reputación ante las fuerzas zarosianas!
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
        - ¡Tus Sellos de los sin rostro valían [número] reputación ante las fuerzas zarosianas!
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
        - ¡Tus Sellos de las Furias valían [número] reputación ante las fuerzas zarosianas!
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
          - ¡Tus Sellos de Cywir valían [número] reputación ante las fuerzas zarosianas!
          - (continue)
        - ((Si se entregaron los Sellos de los Sin Rostro:))
          - ¡Tus Sellos de los sin rostro valían [número] reputación ante las fuerzas zarosianas!
          - (continue)
        - ((Si se entregaron los Sellos de las Furias:))
          - ¡Tus Sellos de las Furias valían [número] reputación ante las fuerzas zarosianas!
          - (continue)
        - (Condition: Si se desbloquearan nuevas recompensas:)
          - (ver|Reputación (Corazón de Gielinor))
          - (continue)
        - (continue)
    - No, gracias.
      - (continue)
- **SELECCIONA UNA OPCIÓN**
  - ¿Qué está pasando aquí?
    - **Vindicta's Chosen:** Te encuentras en el Corazón de Gielinor, aventurero. El Señor Vacío vigila esta vasta caverna. Bajo su mirada arrasaremos con los secuaces de Seren, Zamorak y Sliske que se nos oponen. Al mando de nuestras fuerzas desde arriba está la poderosa ilujanka Vindicta, montada sobre su dragón Gorvek e infundiendo miedo a nuestros enemigos.
    - **Player:** ¿Por qué están todos aquí parados? ¿No deberías estar peleando?
    - **Vindicta's Chosen:** No todos somos salvajes. Sobre esta plataforma se ha establecido una tregua que nos permite a nosotros, los enviados de cada facción, utilizar palabras en lugar de violencia para influir en nuevos reclutas. Porque abajo la batalla continúa, por lo que debemos hacer lo que podamos para persuadir a los mercenarios que se unen a la refriega para que luchen por nuestra causa. Echa un vistazo a lo que tengo para ofrecerte. Te lo aseguro, haré que valga la pena luchar por Zaros.
    - (previous)
  - ¿Cuál es tu opinión sobre mí?
    - ((Se abre la interfaz de Zaros Reputation Rewards.))
  - ¿Cómo puedo mejorar mi reputación?
    - **Vindicta's Chosen:** Hay algunas formas de mejorar tu posición. Lo más fácil que puedes hacer es derrotar a nuestros enemigos y usar fragmentos de Ingresión para pedir refuerzos para nosotros. El maestro de recompensas de allí, Feng, también puede ayudarte a mejorar tu posición ofreciéndote recompensas. Habla con él si quieres saber más. Ah, y estoy seguro de que si de alguna manera pudieras encontrar una manera de derrotar a los generales de las otras facciones, eso sin duda te haría ganar mucho favor.
    - (previous)
  - ¿Dónde puedo conseguir una armadura así?
    - **Vindicta's Chosen:** Puedes recolectar fragmentos de armadura y crestas alrededor del Corazón que luego se pueden combinar para crear una armadura similar a la mía. Si me demuestras tu valía, puedo mostrarte cómo mejorarlo aún más y desbloquear su verdadero potencial.
    - (previous)
  - Me gustaría reclamar mis recompensas.
    - ((Si actualmente no tienes recompensas para reclamar:))
      - **Vindicta's Chosen:** No hay nada que pueda darte.
      - (previous)
    - ((Con recompensas para reclamar:))
      - **ELIGE UNA OPCIÓN:**
        - Me gustaría reclamar mi insignia.
          - Vindicta's Chosen te entrega una insignia de Zaros.
          - (previous2)
        - ((Sólo con piedra nocturna desbloqueada:))
          - Me gustaría recuperar mi juguete.
            - (receives=nightstone)
            - Vindicta's Chosen te entrega una Nightstone.
            - (previous2)
        - No importa.
          - (previous2)

### Reputation

- ((Se abre la interfaz de Zaros Reputation Rewards.))

### Reclaim

- (above|reclaim)

### Attempting to use a seal of opposing faction with 2,000 Zaros reputation

- [No puedes ganar más reputación con esa facción.]
