# Professor Imblewyn

- **Original Wiki Page**: [Transcript:Professor Imblewyn](https://runescape.wiki/w/Transcript%3AProfessor%20Imblewyn)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Player:** No sabía que los gnomos estaban interesados ​​en la magia.
- **Professor Imblewyn:** A los gnomos les interesa todo, muchacho.
- **Player:** Por supuesto.
- **Professor Imblewyn:** Tenemos un dicho: "La curiosidad mató al gato". Pero los gatos no son lo suficientemente inteligentes como para entender lo que encuentran. Los gnomos lo son.
- (Condition: Si el player ha completado La cola de dos gatos:)
  - **Player:** ¡Oye! ¡Algunos de mis mejores amigos son gatos!
  - **Professor Imblewyn:** Creo que eso dice más de ti que los gatos.

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Professor Imblewyn:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Professor Imblewyn:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **Professor Imblewyn:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - **Professor Imblewyn:** Si completas esto, te daré: Runa cósmica x 50. ¡Estoy seguro de que también ganarás algo de reputación en el gremio de agricultores!
    - **Professor Imblewyn:** ¡Tendrás que ser rápido! Solo estoy aquí por [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - ((Sin los artículos solicitados:))
      - **Professor Imblewyn:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Professor Imblewyn:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **Professor Imblewyn:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - ((Con los artículos solicitados:))
      - (removes=the requested items) (receives=50 cosmic runes)
      - ((Si se premió una imprimación de Brassica:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - ((Repetido en una ventana emergente:))
          - Por completar esta solicitud, recibió 1 imprimación para Brassica.
          - (continue)
      - [Has recibido: Runa cósmica x 50 <br>Y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- **Professor Imblewyn:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time].

#### Entregar solicitud fácil


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Professor Imblewyn:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Professor Imblewyn:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Professor Imblewyn:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]

##### Con artículos solicitados

- (removes=the requested items) (receives=50 cosmic runes)
- ((Si se premió una imprimación de Brassica:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - ((Repetido en una ventana emergente:))
    - Por completar esta solicitud, recibió 1 imprimación para Brassica.
    - (continue)
- [Has recibido: Runa cósmica x 50 <br>Y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud diaria en [time].

### Gnome Restaurant delivery

- **Professor Imblewyn:** Hmm, me pregunto... Oh. Mi pedido. Gracias. Tenga en cuenta que no incluye comida ni bebida en los libros.
