# TzHaar-Hur-Zuh

- **Original Wiki Page**: [Transcript:TzHaar-Hur-Zuh](https://runescape.wiki/w/Transcript%3ATzHaar-Hur-Zuh)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Dialogue is from after all TzHaar quests are completed}}

### TzHaar City


#### Habla con

- **TzHaar-Hur-Zuh:** ¿Puedo ayudarte, TzHaar-Mej-Player?
- (Condition: Si tiene artículos para recoger en Grand Exchange:)
  - **TzHaar-Hur-Zuh:** Antes de continuar, debo informarle que tiene artículos listos para ser recogidos en Grand Exchange.
  - (continue)
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: Me gustaría acceder a mi cuenta bancaria, por favor.
    - (opens=Bank)
  - [Choice]: Me gustaría verificar la configuración de mi PIN.
    - (opens=Bank PIN)
  - [Choice]: Me gustaría ver mi caja de colección.
    - (opens=Grand Exchange collection box)
  - [Choice]: ¿Cómo me llamaste?
    - **TzHaar-Hur-Zuh:** ¿No eres TzHaar-Mej?
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Por qué me llamas 'TzHaar-Mej'?
        - **Tzhaar-Hur-Zuh:** Eso es lo que eres...usuario de poderes místicos, ¿no?
        - **Tzhaar-Hur-Zuh:** Y ya no eres JalYt. Ahora eres TzHaar.
        - **Player:** Bueno, sí, supongo que lo soy...
        - **Tzhaar-Hur-Zuh:** ¡Entonces tú, TzHaar-Mej!
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Qué eres entonces?
            - **Tzhaar-Hur-Zuh:** Soy Tzhaar-Hur, uno de los artesanos de esta ciudad. Fabricamos herramientas y esculturas, y tallamos casas para los TzHaar.
            - **Tzhaar-Hur-Zuh:** También están los sabios TzHaar-Mej que nos guían, los poderosos TzHaar-Ket que nos protegen y los veloces TzHaar-Xil que cazan nuestra comida.
          - [Choice]: Gracias por explicarlo.
            - (end)
      - [Choice]: Sí, ciertamente lo soy.
        - **Tzhaar-Hur-Zuh:** Entonces es un honor hablar contigo, TzHaar-Mej-Player. <br>Tú, gran y poderoso TzHaar, y defensor de nuestra ciudad.
      - [Choice]: Debes haberme confundido con otro TzHaar.
        - **Tzhaar-Hur-Zuh:** Escuché que eres modesto, TzHaar-Mej-Player.
        - **Tzhaar-Hur-Zuh:** No es necesario. Deléitate con nuestra alabanza. Mereces todo honor.

#### Reclamar Tokkul

- (Condition: Si el player no es elegible:)
  - {{transcript missing}}
- (Condition: Si un jugador elegible no ha cobrado su recompensa:)
  - [TzHaar-Hur-Zuh te entrega 150.000 TokKul.]
- (Condition: Si el player ya cobró su recompensa:)
  - **TzHaar-Hur-Zuh:** Ya te he dado TokKul.

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **TzHaar-Hur-Zuh:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **TzHaar-Hur-Zuh:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **TzHaar-Hur-Zuh:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - **TzHaar-Hur-Zuh:** Si completas esto, te daré: Tokkul x 15000. ¡Estoy seguro de que también ganarás algo de reputación en el gremio de agricultores!
    - **TzHaar-Hur-Zuh:** ¡Tendrás que ser rápido! Solo estoy aquí por [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - ((Sin los artículos solicitados:))
      - **TzHaar-Hur-Zuh:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **TzHaar-Hur-Zuh:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **TzHaar-Hur-Zuh:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - ((Con los artículos solicitados:))
      - (removes=the requested items) (receives=15,000 Tokkul)
      - ((Si se premió una imprimación de Brassica:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - ((Repetido en una ventana emergente:))
          - Por completar esta solicitud, recibió 1 imprimación para Brassica.
          - (continue)
      - [Has recibido: Tokkul x 15000 <br>Y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- **TzHaar-Hur-Zuh:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time].

#### Entregar solicitud fácil


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **TzHaar-Hur-Zuh:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **TzHaar-Hur-Zuh:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **TzHaar-Hur-Zuh:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]

##### Con artículos solicitados

- (removes=the requested items) (receives=15,000 Tokkul)
- ((Si se premió una imprimación de Brassica:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - ((Repetido en una ventana emergente:))
    - Por completar esta solicitud, recibió 1 imprimación para Brassica.
    - (continue)
- [Has recibido: Tokkul x 15000 <br>Y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud diaria en [time].
