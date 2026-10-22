# Ifaba

- **Original Wiki Page**: [Transcript:Ifaba](https://runescape.wiki/w/Transcript%3AIfaba)
- **Letter**: `I`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Marim, on Ape Atoll


#### Mientras no uses un amuleto de mono

- **Ifaba:** ¡Ok! ¡Ah, ah, ah! ¡Ah, uh! ¡Ok, ah, ook!
- No puedes entender lo que está diciendo.

#### Mientras llevas un amuleto de mono

- **Ifaba:** ¿Te gustaría comprar o vender algo?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, por favor.
    - **Player:** Sí, por favor.
    - (opens=Ifaba's General Store)
  - [Choice]: No, gracias.
    - **Player:** No, gracias.

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Ifaba:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Ifaba:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - (Condition: With 3 requested animals:)
      - **Ifaba:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
      - (continue)
    - (Condition: With 4 requested animals:)
      - **Ifaba:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
      - (continue)
    - **Ifaba:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - **Ifaba:** Si completas esto, te daré: La oportunidad de obtener un cosmético con temática de plátano x 1. ¡Estoy seguro de que también ganarás reputación en el gremio de agricultores!
    - **Ifaba:** ¡Tendrás que ser rápido!, solo estoy aquí por [número] días, [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - ((Without the requested items:))
      - **Ifaba:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Ifaba:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - (Condition: With 3 requested animals:)
        - **Ifaba:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
        - (continue)
      - (Condition: With 4 requested animals:)
        - **Ifaba:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
        - (continue)
      - **Ifaba:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - ((With the requested items:))
      - (removes=the requested items) (receives=a banana, the left banana of knowledge, or the right banana of knowledge)
      - Por completar esta solicitud, recibió 1 imprimación para Brassica.
      - ((Repeated in a pop-up:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - (continue)
      - (Condition: If a regular banana was received:)
        - [Has recibido: Plátano x 1<br>Y 5500 de reputación agrícola.]
      - (Condition: If the left banana of knowledge was received:)
        - [Has recibido: Plátano izquierdo de conocimiento x 1<br>Y 5500 de reputación agrícola.]
      - (Condition: If the right banana of knowledge was received:)
        - [Has recibido: Plátano correcto de conocimiento x 1<br>Y 5500 de reputación agrícola.]

##### Después de completar la solicitud

- **Ifaba:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time].

#### Entregar solicitud mediana


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Ifaba:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Ifaba:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- (Condition: With 3 requested animals:)
  - **Ifaba:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
  - (continue)
- (Condition: With 4 requested animals:)
  - **Ifaba:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
  - (continue)
- **Ifaba:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]

##### Con artículos solicitados

- (Condition: With multiple applicable animals:)
  - [Menu]: ¿Qué animal te gustaría entregar?
    - ((The following is repeated for each applicable animal:))
      - [Choice]: [Animal name]
        - (continue)
- (removes=the requested items) (receives=the reward)
- Por completar esta solicitud, recibió 1 imprimación para Brassica.
- ((Repeated in a pop-up:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - (continue)
- (Condition: If a regular banana was received:)
  - [Has recibido: Plátano x 1<br>Y 5500 de reputación agrícola.]
- (Condition: If the left banana of knowledge was received:)
  - [Has recibido: Plátano izquierdo de conocimiento x 1<br>Y 5500 de reputación agrícola.]
- (Condition: If the right banana of knowledge was received:)
  - [Has recibido: Plátano correcto de conocimiento x 1<br>Y 5500 de reputación agrícola.]

##### Después de completar la solicitud

- Ya completó esta solicitud, habrá una nueva solicitud tridiaria en [time].
