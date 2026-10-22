# Kazgar

- **Original Wiki Page**: [Transcript:Kazgar](https://runescape.wiki/w/Transcript%3AKazgar)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the tunnel near Lumbridge Castle cellar


#### Hablando con él

- **Kazgar:** Hola, habitante de la superficie.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Kazgar:** Mistag me publicó aquí cuando los habitantes de la superficie comenzaron a visitar la mina. Si tienes negocios en las minas de Dorgeshuun, te guiaré a través de los túneles.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Puedes mostrarme el camino a la mina?
        - **Player:** ¿Puedes mostrarme el camino a la mina?
        - (Condition: Before Death to the Dorgeshuun:)
          - **Kazgar:** Muy bien. Sígueme.
          - (continue)
        - (Condition: After Death to the Dorgeshuun:)
          - **Kazgar:** ¡Por supuesto! ¡Siempre serás bienvenido en nuestras minas!
          - (continue)
        - Kazgar te muestra el camino a través de los túneles.
      - [Choice]: cond=After Death to the Dorgeshuun|¿Puedes mostrarme el camino al sótano del molino de agua?
        - **Player:** ¿Puedes mostrarme el camino al sótano del molino de agua?
        - **Kazgar:** ¡Por supuesto!
        - Kazgar te muestra el camino a través de los túneles.
      - [Choice]: Quizás en otro momento.
        - **Player:** Quizás en otro momento.
  - [Choice]: ¿Puedes mostrarme el camino a la mina?
    - (arriba)
  - [Choice]: cond=After Death to the Dorgeshuun|¿Puedes mostrarme el camino al sótano del molino de agua?
    - (arriba)

#### Seguir opción


##### Antes de la muerte del Dorgeshuun

- Kazgar te muestra el camino a través de los túneles.

##### Después de la muerte del Dorgeshuun

- [Menu]: ¿A dónde quieres ir?
  - [Choice]: Minas Dorgeshuun
    - Kazgar te muestra el camino a través de los túneles.
  - [Choice]: Bodega del molino de agua
    - Kazgar te muestra el camino a través de los túneles.
  - [Choice]: En ninguna parte
    - (end)
