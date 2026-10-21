# Golrana

- **Original Wiki Page**: [Transcript:Golrana](https://runescape.wiki/w/Transcript%3AGolrana)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Tree Gnome Village, after The Prisoner of Glouphrie


#### Diálogo por primera vez

- **Golrana:** Gracias de nuevo por ayudarme en el rescate de mi padre, Player. Mientras recupera su salud, he decidido quedarme en Tree Gnome Village y cuidarlo.
- **Golrana:** Pensé en aprovechar el tiempo para entrenarme como susurrador de árboles. Si tienes semillas de spirit tree, te las puedo guardar. Los estudio como parte de mi formación y ¡puedes recuperarlos cuando los necesites!
- **Golrana:** El tío Bolren también permitió a Belmondo establecer una ruta dorada hacia el pueblo. Belmondo lo convenció con historias de su aterrizaje en las montañas Galarpos y desde entonces se han hecho amigos rápidamente.
- **Golrana:** A Bolren ya no le preocupa tener una ruta de vuelo tan cerca del pueblo, ¡siempre que Belmondo opere la línea, por supuesto!
- **Golrana:** Tengo a todos los hombres de mi vida cerca de mí: mi papá, mi esposo, mi hijo e incluso mi tío.
- **Golrana:** Señora afortunada, ¿verdad?

#### Diálogo posterior


##### Sin semillas espirituosas almacenadas con Golrana o en backpack

- **Golrana:** ¡Hola, Player! ¿Has venido a traerme unas semillas de spirit tree? Te los guardaré.
- **Player:** No, sólo vine a ver cómo estaban las cosas.
- **Golrana:** ¡Qué diferente de un aventurero! Se agradece, por supuesto. Dad está bien; está arriba, recuperándose de su terrible experiencia en Arposandra, y ya está planeando el siguiente paso de su venganza, bendito sea. También visitamos la tumba de mamá todos los fines de semana.
- **Golrana:** Golrie está de vuelta en la cueva y retendré su mesada hasta que lo haya organizado todo.
- **Golrana:** Mi entrenamiento va bien; A los árboles espirituales les agrado bastante, aunque me dicen que tú mismo eres un gran susurrador. Estoy empezando a pensar que quizás, pero sólo quizás, puedas ser tan buen aventurero como yo. ¡Y eso es todo!
- **Player:** Me alegra saber que todo va bien. Te veré más tarde.

##### Con semillas espirituosas almacenadas en Golrana, o con semillas espirituosas en backpack

- (Condition: Sin semillas espirituosas almacenadas:)
  - **Golrana:** ¡Hola, Player! ¿Has venido a traerme unas semillas de spirit tree? Te los guardaré.
  - (continue)
- (Condition: Con exactamente una semilla espirituosa almacenada:)
  - **Golrana:** ¡Hola, Player! ¿Has venido a recuperar algunas de tus semillas de spirit tree? Estoy guardando uno hasta ahora para ti.
  - (continue)
- (Condition: Con dos o más semillas espirituosas almacenadas:)
  - **Golrana:** ¡Hola, Player! ¿Has venido a recuperar algunas de tus semillas de spirit tree? Estoy guardando [número] hasta ahora para ti.
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: cond=With spirit seeds in backpack:|Dale todas tus semillas.
    - (removes=all spirit seeds in backpack)
    - [Guardas las semillas con Golrana.]
    - **Golrana:** ¡Gracias! Los cuidaré preciosamente.
  - [Choice]: cond=With spirit seeds in backpack:|Dale algunas de tus semillas.
    - {{Tinput|Enter amount:}}
      - (above|store)
  - [Choice]: cond=With spirit seeds stored with Golrana:|Retira todas tus semillas
    - (Condition: Sin espacio en backpack:)
      - **Golrana:** Lo sentimos, pero no tienes suficiente espacio en tu inventario para las semillas. Haz un poco de espacio y habla conmigo de nuevo.
    - (Condition: Con espacio en backpack:)
      - (receives=spirit seeds)
      - [Recuperas todas tus semillas de Golrana.]
      - **Golrana:** Ahí lo tienes.
    - [Choice]: cond=With spirit seeds stored with Golrana:|Retira algunas de tus semillas.
    - {{Tinput|Enter amount:}}
      - (Condition: Sin espacio en backpack:)
        - (above|sorry)
      - (Condition: Con espacio en backpack:)
        - (Condition: Si retira todas las semillas:)
          - (above|withdrawal)
        - (Condition: Si retira solo algunas semillas:)
          - [Recuperas las semillas de Golrana.]
          - **Golrana:** Ahí lo tienes.
  - [Choice]: Habla de otra cosa.
    - (above|other)
