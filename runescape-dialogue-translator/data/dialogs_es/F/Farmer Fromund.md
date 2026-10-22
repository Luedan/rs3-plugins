# Farmer Fromund

- **Original Wiki Page**: [Transcript:Farmer Fromund](https://runescape.wiki/w/Transcript%3AFarmer%20Fromund)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### On Etceteria, before Royal Trouble

- **Farmer Fromund:** ¡Oye! Esta es la granja de la Reina. Necesitará su aprobación para utilizarlo.

### Standard dialogue after Royal Trouble

- [Menu]: ¿De qué te gustaría hablar?
  - [Choice]: Farmer Fromund.
    - **Player:** Buenos días. ¿Qué estás haciendo?
    - **Farmer Fromund:** Estoy atendiendo estos terrenos agrícolas. Necesitan un poco más de trabajo antes de que pueda plantar algo.
    - [Menu]: Selecciona una opción
      - [Choice]: Buena suerte con eso.
        - **Player:** Buena suerte con eso.
        - **Farmer Fromund:** Gracias, [Fremennik name].
      - [Choice]: ¿Qué pasa con los parches?
        - **Player:** ¿Qué pasa con los parches?
        - **Farmer Fromund:** El parche central está lleno de malas hierbas y, en cuanto las limpio, vuelven a crecer. La zona sur siempre es demasiado seca. Y el suelo en la zona norte es terrible; necesita una buena dosis de abono.
  - [Choice]: Su índice de aprobación.
    - **Player:** ¿Qué piensa la gente de mí por aquí?
    - (Condition: If your approval rating is between 25% and 49%:)
      - **Farmer Fromund:** Su gente está cada vez más insatisfecha con el régimen, Su Alteza Real. En la última encuesta, sólo el [approval rating]% de la población lo apoyó.
    - (Condition: If your approval rating is between 50% and 74%:)
      - **Farmer Fromund:** Usted es bien considerado, Su Alteza Real. En la última encuesta, el [approval rating]% de la población lo apoyó.
    - (Condition: If your approval rating is at 75% or higher:)
      - **Farmer Fromund:** Usted es universalmente adorado, Su Alteza Real. En la última encuesta, el [approval rating]% de la población lo apoyó.

### Working on the island

*Cuando el jugador rastrilla la zona de maleza o riega la zona seca cercana*
- (Condition: Below 100% approval rating:)
  - **Farmer Fromund:** {{RSChat|Thanks!}}
- (Condition: At 100% approval rating:)
  - (Condition: Before Royal Trouble:)
    - **Farmer Fromund:** No te preocupes más, [Sir/Madam], ¡ya has hecho mucho!
  - (Condition: After Royal Trouble:)
    - **Farmer Fromund:** No se preocupe más, Alteza, ¡ya ha hecho mucho!

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- **¿Qué te gustaría hacer?**
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Farmer Fromund:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Farmer Fromund:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **Farmer Fromund:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - **Farmer Fromund:** Si completas esto, te daré: bendición de reputación Farming (pequeña) x 1. ¡Estoy seguro de que también ganarás algo de reputación con el gremio de agricultores!
    - **Farmer Fromund:** ¡Tendrás que ser rápido! Solo estoy aquí por [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - ((Without the requested items:))
      - **Farmer Fromund:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Farmer Fromund:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **Farmer Fromund:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - ((With the requested items:))
      - (removes=the requested items) (receives=the reward)
      - ((If a Brassica primer was rewarded:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - ((Repeated in a pop-up:))
          - Por completar esta solicitud, recibió 1 imprimación para Brassica.
          - (continue)
      - Has recibido: bendición de reputación Farming (pequeña) x 1<br> y 2750 de reputación agrícola.

##### Después de completar la solicitud

- **Farmer Fromund:** ¡Gracias por tu ayuda!
- [Una nueva solicitud estará disponible en [time].]

#### Entregar solicitud fácil


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Farmer Fromund:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Farmer Fromund:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Farmer Fromund:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]

##### Con artículos solicitados

- (removes=the requested items) (receives=the reward)
- ((If a Brassica primer was rewarded:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - ((Repeated in a pop-up:))
    - Por completar esta solicitud, recibió 1 imprimación para Brassica.
    - (continue)
- Has recibido: bendición de reputación Farming (pequeña) x 1 <br> y 2750 de reputación agrícola.

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud diaria en [time].
