# My Arm

- **Original Wiki Page**: [Transcript:My Arm](https://runescape.wiki/w/Transcript%3AMy%20Arm)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At Troll Stronghold after My Arm's Big Adventure

- **My Arm:** ¿Qué puede hacer My Arm por ti hoy, Player?
- [Menu]: Selecciona una opción
  - [Choice]: cond=If the player has lost their farming manual|¿Puedo conseguir otra copia de ese libro sobre agricultura, por favor?
    - **Player:** ¿Puedo conseguir otra copia de ese libro sobre agricultura, por favor?
    - **My Arm:** Toma, toma este.
    - (receives=Farming manual)
    - **Player:** Gracias.
  - [Choice]: ¿Cómo va tu agricultura?
    - **Player:** ¿Cómo va tu agricultura?
    - **My Arm:** My Arm se está volviendo bueno en dis. Estoy cultivando mucha hierba gotosa para Burntmeat y él está muy feliz.
    - **Player:** Bien, bien.
    - **My Arm:** ¿Algo más?
    - **Player:** Nada, gracias.
    - **My Arm:** Está bien, Player. Vuelve cuando quieras.
  - [Choice]: cond=After The Mighty Fall|Quiero hablarte sobre el Kyzaj.
    - **My Arm:** ¡Ja, ja! ¡Fue genial! ¡Nunca había visto nada parecido! Espero que se pongan uno pronto.
    - [Menu]: Selecciona una opción
      - [Choice]: cond=If Zanik was killed|¿Qué opinas sobre Zanik?
        - **My Arm:** Es una pena que tuvieras que matarla, pero supongo que Zarador presentó un argumento convincente.
        - **My Arm:** ¡Sólo espero que nunca me arrojen a un pozo contigo!
      - [Choice]: ¿Qué opinas de Graardor?
        - **My Arm:** Nunca había oído hablar de él antes de este torneo. Es un luchador bastante bueno.
        - **My Arm:** ¡Por tu cuenta, por supuesto!
      - [Choice]: cond=If Zanik was spared|¿No elegiste Zanik?
        - **My Arm:** No. Suena como una aventura bastante buena, pero no podía simplemente irme. Estas hierbas podrían morir si hiciera eso.
      - [Choice]: Adiós.
        - (end)
  - [Choice]: Nada, gracias.
    - **Player:** Nada, gracias.
    - **My Arm:** Está bien, Player. Vuelve cuando quieras.

### In the Barendir Tunnels after King of the Dwarves

- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué estás haciendo aquí?
    - **Player:** ¿Qué haces aquí?
    - **My Arm:** Pretty Flower cree que alguien intentó envenenarlo, así que me hizo cultivar nuevos ingredientes alimentarios para él.
  - [Choice]: ¿Cómo va vuestro Farming?
    - **Player:** ¿Cómo va tu Farming?
    - **My Arm:** My Arm se está volviendo bueno en dis. Estoy cultivando mucha hierba gotosa para Burntmeat y él está muy feliz.
  - [Choice]: Necesito otra flor bonita.
    - **Player:** Necesito otra flor bonita.
    - (receives=Pretty flower)
    - [My Arm te regala otra bonita flor.]
    - **My Arm:** My Arm ¡espero que lo disfrutes!
  - [Choice]: Adiós.
    - **Player:** Adiós.

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **My Arm:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **My Arm:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **My Arm:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - **My Arm:** Si completas esto, te daré: bendición de reputación Farming (mediana) x 1. ¡Estoy seguro de que también ganarás algo de reputación con el gremio de agricultores!
    - **My Arm:** ¡Tendrás que ser rápido! Solo estoy aquí por [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - ((Sin los artículos solicitados:))
      - **My Arm:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **My Arm:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **My Arm:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - ((Con los artículos solicitados:))
      - (removes=the requested items) (receives=Farming reputation boon (medium) y posiblemente una imprimación Brassica)
      - ((Si se premió una imprimación de Brassica:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - ((Repetido en una ventana emergente:))
          - Por completar esta solicitud, recibió 1 imprimación para Brassica.
          - (continue)
      - [Has recibido: bendición de reputación Farming (mediana) x 1 <br> y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- **My Arm:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time].

#### Entregar solicitud fácil


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **My Arm:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **My Arm:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **My Arm:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]

##### Con artículos solicitados

- (removes=the requested items) (receives=Farming reputation boon (medium) y posiblemente una imprimación Brassica)
- ((Si se premió una imprimación de Brassica:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - ((Repetido en una ventana emergente:))
    - Por completar esta solicitud, recibió 1 imprimación para Brassica.
    - (continue)
- [Has recibido: bendición de reputación Farming (mediana) x 1 <br> y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud diaria en [time].
