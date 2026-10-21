# Ulifed

- **Original Wiki Page**: [Transcript:Ulifed](https://runescape.wiki/w/Transcript%3AUlifed)
- **Letter**: `U`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In eastern Keldagrim

- **Ulifed:** Dime, ¿no eres tú el humano que fue arrestado aquí el otro día, junto al barco?
- **Player:** Sí, pero aclaramos toda la situación.
- **Ulifed:** Bien, bien.

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Ulifed:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Ulifed:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **Ulifed:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - **Ulifed:** Si completas esto, te daré: Anillo de forja x 5. ¡Estoy seguro de que también ganarás reputación en el gremio de agricultores!
    - **Ulifed:** ¡Tendrás que ser rápido! Solo estoy aquí por [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - ((Sin los artículos solicitados:))
      - **Ulifed:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Ulifed:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **Ulifed:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - ((Con los artículos solicitados:))
      - (removes=the requested items) (receives=five rings of forging and possibly a Brassica primer)
      - ((Si se premió una imprimación de Brassica:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - ((Repetido en una ventana emergente:))
          - (Ventana emergente: por completar esta solicitud, recibió 1 imprimación para Brassica.|color=#EBE0BC)
          - (continue)
      - [Has recibido: Anillo de forja x 5<br>Y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- **Ulifed:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time].

#### Entregar solicitud fácil


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Ulifed:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Ulifed:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Ulifed:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]

##### Con artículos solicitados

- (removes=the requested items) (receives=five rings of forging and possibly a Brassica primer)
- ((Si se premió una imprimación de Brassica:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - ((Repetido en una ventana emergente:))
    - (Ventana emergente: por completar esta solicitud, recibió 1 imprimación para Brassica.|color=#EBE0BC)
    - (continue)
- [Has recibido: Anillo de forja x 5<br>Y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud diaria en [time].
