# Reinald

- **Original Wiki Page**: [Transcript:Reinald](https://runescape.wiki/w/Transcript%3AReinald)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In eastern Keldagrim

- **Reinald** Bienvenido a mi casa. Tengo una excelente selección de protectores para brazos hechos en casa, así como ropa fina importada de Thessalia en Varrock, si estás interesado.
- (Condition: Si el player no tiene armadura equipada:)
  - (opens=Reinald's Smithing Emporium)
- (Condition: Si el player tiene armadura equipada:)
  - **Reinald** No puedes probarte mi ropa con toda esa armadura. Quítatelo y luego vuelve a hablarme.

#### Cambiar opción de guardabrazos

- (Condition: Si el player no tiene armadura equipada:)
  - (opens=Reinald's Smithing Emporium)
- (Condition: Si el player tiene armadura equipada:)
  - **Reinald** No puedes probarte mi ropa con toda esa armadura. Quítatelo y luego vuelve a hablarme.

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Reinald:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Reinald:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - (Condition: Con 3 animales solicitados:)
      - **Reinald:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
      - (continue)
    - (Condition: Con 4 animales solicitados:)
      - **Reinald:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
      - (continue)
    - **Reinald:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - **Reinald:** Si completas esto, te daré: Espíritu de piedra animica ligera x 10. ¡Estoy seguro de que también ganarás reputación en el gremio de agricultores!
    - **Reinald:** ¡Tendrás que ser rápido!, solo estoy aquí por [número] días, [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - (Condition: Sin los artículos solicitados:)
      - **Reinald:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Reinald:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - (Condition: Con 3 animales solicitados:)
        - **Reinald:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
        - (continue)
      - (Condition: Con 4 animales solicitados:)
        - **Reinald:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
        - (continue)
      - **Reinald:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - (Condition: Con los artículos solicitados:)
      - (removes=the requested items) (receives=ten light animica stone spirits and Brassica primer)
      - Por completar esta solicitud, recibió 1 imprimación para Brassica.
      - ((Repetido en una ventana emergente:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - (continue)
      - [Has recibido: Espíritu de piedra animica ligera x 10<br>Y 5500 reputación agrícola.]

##### Después de completar la solicitud

- **Reinald:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time]{{Sic|..}}

#### Entregar solicitud mediana


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Reinald:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Reinald:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Reinald:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal
- **Reinald:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]

##### Con artículos solicitados

- (Condition: Con múltiples animales aplicables:)
  - [Menu]: ¿Qué animal te gustaría entregar?
    - ((Lo siguiente se repite para cada animal aplicable:))
      - [Choice]: [Animal name]
        - (continue)
- (removes=the requested items) (receives=ten light animica stone spirits and Brassica primer)
- Por completar esta solicitud, recibió 1 imprimación para Brassica.
- ((Repetido en una ventana emergente:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - (continue)
- [Has recibido: Espíritu de piedra animica ligera x 10<br>Y 5500 reputación agrícola.]

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud bidiaria en [time]{{Sic|..}}
