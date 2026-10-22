# Sorebones

- **Original Wiki Page**: [Transcript:Sorebones](https://runescape.wiki/w/Transcript%3ASorebones)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Manor Farm


#### Ayuda


##### Antes de haber completado la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Sorebones:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Sorebones:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **Sorebones:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
    - **Sorebones:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - **Sorebones:** Si completas esto, te daré: The Stuff x 2. ¡Estoy seguro de que también ganarás algo de reputación en el gremio de agricultores!
    - **Sorebones:** ¡Tendrás que ser rápido! Solo estoy aquí por [time]. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - (Condition: Without the requested items:)
      - **Sorebones:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Sorebones:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **Sorebones:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
      - **Sorebones:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - (Condition: With the requested items:)
      - (Condition: With multiple applicable animals:)
        - [Menu]: ¿Qué animal te gustaría entregar?
          - ((The following is given for each applicable animal:))
            - [Choice]: [Name]
              - (continue)
      - (removes=the requested items) (receives=2 bags of The Stuff and 3 Brassica primers)
      - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
      - ((Repeated in a pop-up:))
        - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
        - (continue)
      - [Has recibido: The Stuff x 2<br>Y 13,750 reputación agrícola.]

##### Después de haber completado la solicitud

- **Sorebones:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time]{{Sic|..}}

#### Entregar solicitud dura


##### Antes de haber completado la solicitud


##### Sin artículos solicitados

- **Sorebones:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Sorebones:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Sorebones:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
- **Sorebones:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]

##### Con artículos solicitados

- (Condition: Without the requested items:)
  - **Sorebones:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
  - **Sorebones:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
  - **Sorebones:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
  - **Sorebones:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
- (Condition: With the requested items:)
  - (removes=the requested items) (receives=2 bags of The Stuff and 3 Brassica primers)
  - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
  - ((Repeated in a pop-up:))
    - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
    - (continue)
  - [Has recibido: The Stuff x 2<br>Y 13,750 reputación agrícola.]

##### Después de haber completado la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud semanal en [time]{{Sic|..}}
