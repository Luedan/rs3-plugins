# Void Knight

- **Original Wiki Page**: [Transcript:Void Knight](https://runescape.wiki/w/Transcript%3AVoid%20Knight)
- **Letter**: `V`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Void Knight:** Hola, ¿en qué puedo ayudarte?
- **ELIGE UNA OPCIÓN:**
  - ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Void Knight:** Soy un Void Knight, uno de la orden de Guthix. Somos guerreros del equilibrio que hacemos el trabajo de Guthix aquí en Gielinor.
    - **SELECCIONA UNA OPCIÓN**
      - Vaya, ¿puedo unirme?
        - **Player:** Vaya, ¿puedo unirme?
        - **Void Knight:** La entrada es estrictamente solo por invitación, sin embargo, necesitamos ayuda para continuar con el trabajo de Guthix.
        - **SELECCIONA UNA OPCIÓN**
          - ¿Qué tipo de trabajo?
            - (below|what-kind-of-work)
          - Buena suerte con eso.
            - **Player:** Buena suerte con eso.
      - ¿Qué tipo de trabajo?
        - **Player:** ¿Qué tipo de trabajo?
        - **Void Knight:** Ah, bueno, verás, intentamos mantener Gielinor como pretendía Guthix, es un gran desafío. De hecho, hemos tenido algunos problemas recientemente, ¿quizás podrías ayudarnos?
        - **SELECCIONA UNA OPCIÓN**
          - ¿Cuál es el problema?
            - **Player:** ¿Cuál es el problema?
            - **Void Knight:** Bueno, el orden ha disminuido bastante con el paso de los años, es un proceso muy largo aprender las habilidades de un Void Knight. Recientemente ha habido irrupciones en nuestro reino desde algún otro lugar, y han estado entrando extrañas criaturas. No podemos permitir que eso suceda y le agradeceríamos mucho que nos ayudara.
            - (continue|help-options)
          - ¿Qué es 'Gielinor'?
            - (below|whats-gielinor)
          - Preferiría no hacerlo, lo siento.
            - **Player:** Preferiría no hacerlo, lo siento.
      - ¿Qué es 'Gielinor'?
        - **Player:** ¿Qué es 'Gielinor'?
        - **Void Knight:** Es el nombre que Guthix le dio a este mundo, por eso lo honramos con su uso.
      - Ajá, claro.
        - **Player:** Ajá, claro.
  - ¿Qué es este lugar?
    - **Player:** ¿Qué es este lugar?
    - **Void Knight:** Este es nuestro puesto de avanzada. Desde aquí enviamos lanchas a las islas cercanas para hacer retroceder a los invasores.
    - **SELECCIONA UNA OPCIÓN**
      - ¿Qué invasores?
        - **Player:** ¿Qué invasores?
        - **Void Knight:** Recientemente ha habido irrupciones en nuestro reino desde algún otro lugar y han estado entrando extrañas criaturas. No podemos permitir que eso suceda y le agradeceríamos mucho que nos ayudara.
        - **SELECCIONA UNA OPCIÓN**
          - ¿Cómo puedo ayudar?
            - (below|how-can-i-help)
          - Lo siento, pero no puedo.
            - **Player:** Lo siento, pero no puedo.
      - ¿Cómo puedo ayudar?
        - **Player:** ¿Cómo puedo ayudar?
        - **Void Knight:** Enviamos lanzadores desde nuestro puesto de avanzada a las islas cercanas. Si vas y esperas en el módulo de aterrizaje, eso sería de gran ayuda.
      - Buena suerte con eso.
        - **Player:** Buena suerte con eso.
  - ¿Pueden intercambiar mis elogios por capacitación?
    - (opens=Commendation Rewards)
  - Estoy bien gracias.
    - **Player:** Estoy bien, gracias.

### Using a Void knight commendation on Void Knight

- **Player:** Me gustaría canjear este elogio.
- **Void Knight:** Por supuesto.
- ¡Ahora tienes un total de elogios [número]!

### Manor Farm


#### Ayuda


##### Antes de haber completado la solicitud

- **¿QUÉ TE GUSTARÍA HACER?**
  - Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Void Knight:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Void Knight:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - ((Si se aceptan tres variantes animales:))
      - **Void Knight:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
      - (continue)
    - ((Si se aceptan cuatro variantes animales:))
      - **Void Knight:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
      - (continue)
    - **Void Knight:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - **Void Knight:** Si completas esto, te daré: Shifter, Ravager, Tocher o Spinner Charms x 15. ¡Estoy seguro de que también ganarás algo de reputación en el gremio de agricultores!
    - **Void Knight:** ¡Tendrás que ser rápido!, solo estoy aquí por [número] días, [número] horas y [número] minutos. Para ser exactos.
  - Dales los artículos y animales que soliciten.
    - ((Sin los artículos solicitados:))
      - **Void Knight:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Void Knight:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - ((Si se aceptan tres variantes animales:))
        - **Void Knight:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
        - (continue)
      - ((Si se aceptan cuatro variantes animales:))
        - **Void Knight:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
        - (continue)
      - **Void Knight:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - ((Con los artículos solicitados:))
      - (Condition: Con múltiples animales aplicables:)
        - [Menu]: ¿Qué animal te gustaría entregar?
          - ((Se da la siguiente opción para cada animal aplicable:))
            - [Choice]: [Animal name]
              - (continue)
      - (removes=the requested items) (receives=the reward)
      - Por completar esta solicitud, recibió 1 imprimación para Brassica.
      - ((Repetido en una ventana emergente:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - (continue)
      - Has recibido: [Reward] x 15<br>Y 5500 de reputación agrícola.

##### Después de haber completado la solicitud

- **Void Knight:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time]{{Sic|..}}

#### Entregar solicitud mediana


##### Antes de haber completado la solicitud


##### Sin artículos solicitados

- **Void Knight:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Void Knight:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- ((Si se aceptan tres variantes animales:))
  - **Void Knight:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
  - (continue)
- ((Si se aceptan cuatro variantes animales:))
  - **Void Knight:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
  - (continue)
- **Void Knight:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]

##### Con artículos solicitados

- (removes=the requested items) (receives=the reward)
- Por completar esta solicitud, recibió 1 imprimación para Brassica.
- ((Repetido en una ventana emergente:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - (continue)
- Has recibido: [Reward] x 15<br>Y 5500 de reputación agrícola.

##### Después de haber completado la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud tridiaria en [time]{{Sic|..}}
