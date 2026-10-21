# Apprentice Clara

- **Original Wiki Page**: [Transcript:Apprentice Clara](https://runescape.wiki/w/Transcript%3AApprentice%20Clara)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Transcript npc|Apprentice Clara}}

### In Burthorpe

- **Apprentice Clara:** Tantas runas...
- **Player:** ¿Estás bien?
- **Apprentice Clara:** ¡Oh! No te preocupes. Estoy intentando aprender sobre runas con la señora Carwen. ¡Es un tema fascinante!
- [Menu]: Selecciona una opción
  - [Choice]: Necesito runas.
    - (opens=Carwen Essencebinder Magical Runes Shop)
  - [Choice]: ¿Qué puedes contarme sobre Runecrafting?
    - **Apprentice Clara:** ¡Hay mucho de qué hablar! Aunque recién estoy aprendiendo los entresijos. Sería mejor que hablaras con la señora Carwen.
    - **Apprentice Clara:** Como parte de mis deberes, la ayudo vendiendo runas. ¿Quieres echar un vistazo?
    - [Menu]: Selecciona una opción
      - [Choice]: Echaré un vistazo.
        - (opens=Carwen Essencebinder Magical Runes Shop)
      - [Choice]: Quizás más tarde.
        - **Apprentice Clara:** Claro. Si alguna vez necesitas que esa magia fluya, no seas tímido: ¡ven a vernos!

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Apprentice Clara:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Apprentice Clara:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **Apprentice Clara:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - **Apprentice Clara:** Si completas esto, te daré: Runa de aire x 250. ¡Estoy seguro de que también ganarás reputación en el gremio de agricultores!
    - **Apprentice Clara:** ¡Tendrás que ser rápido! Solo estoy aquí por [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - ((Sin los artículos solicitados:))
      - **Apprentice Clara:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Apprentice Clara:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **Apprentice Clara:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - ((Con los artículos solicitados:))
      - (removes=the requested items) (receives=the reward)
      - ((Si se premió una imprimación de Brassica:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - ((Repetido en una ventana emergente:))
          - Por completar esta solicitud, recibió 1 imprimación para Brassica.
          - (continue)
      - [Has recibido: Runa de aire x 250 <br>Y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- **Apprentice Clara:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time].

#### Entregar solicitud fácil


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Apprentice Clara:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Apprentice Clara:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Apprentice Clara:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]

##### Con artículos solicitados

- (removes=the requested items) (receives=the reward)
- ((Si se premió una imprimación de Brassica:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - ((Repetido en una ventana emergente:))
    - Por completar esta solicitud, recibió 1 imprimación para Brassica.
    - (continue)
- [Has recibido: Runa de aire x 250 <br>Y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud diaria en [time].
