# Professor Henry

- **Original Wiki Page**: [Transcript:Professor Henry](https://runescape.wiki/w/Transcript%3AProfessor%20Henry)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Player:** ¡Hola!
- **Professor Henry:** ¡Buenos días!
- {{anchor|old-jail-block}}**Professor Henry:** ¿Querías saber sobre el antiguo pabellón de la cárcel? Siempre necesitamos aventureros para mantener a raya a las cucarachas.
- **Player:** ¿Necesito hacer tu examen?
- **Professor Henry:** No, el examen no es realmente para aventureros como tú. ¿Estás buscando el bloque de la cárcel?
- **Player:** Claro, cuéntame sobre la cárcel.
- **Professor Henry:** En las celdas de abajo hay un pasaje secreto a la antigua prisión. He oído que la fama y la fortuna esperan a un aventurero con las habilidades adecuadas.
- **Player:** Gracias, lo investigaré.

#### Si has completado previamente la prueba histórica de seguridad Player

- **Player:** Hola, profesor.
- **Professor Henry:** Ah, hola, Player. ¿Cómo va la aventura? ¿Confío en que estés disfrutando de tus aventuras?
- **Player:** Lo soy, gracias. Me preguntaba dónde podría estar el bloque de la cárcel.
- **Professor Henry:** Ah, sí. Busca en las celdas de abajo y estoy seguro de que lo encontrarás con bastante facilidad.
- **Player:** Está bien, gracias.

#### Si has hablado anteriormente sobre el player Prueba de seguridad

- **Player:** Hola, profesor.
- **Professor Henry:** Me alegro de verte de nuevo.
- (continuea|old-jail-block)

### Historical dialogue


#### Primera vez hablando con el profesor

- **Player:** Hola.
- **Professor Henry:** ¿Hola qué?
- **Player:** Eh... ¿hola?
- **Professor Henry:** Hola, 'Profesor'. Los modales no cuestan nada, ¿sabes? Cuando estés en mi salón de clases, te pido que uses la dirección adecuada para mi estación.
- **Player:** ¿Tu estación?
- **Professor Henry:** Sí. Significa "posición", por así decirlo.
- **Player:** Oh, está bien.
- **Professor Henry:** Ahora, ¿qué puedo hacer por ti exactamente?
- {{anchor|what-is-this-place}}**Player:** ¿Qué es este lugar?
- **Professor Henry:** Este es el Centro de Excelencia de Capacitación de Misthalin. Es donde los aventureros audaces, como usted, pueden aprender sobre los peligros del mundo y adquirir una valiosa experiencia al mismo tiempo.
- **Player:** ¿Qué puedo hacer aquí?
- **Professor Henry:** Aquí puedes participar en la prueba de seguridad el player: un conjunto de lecciones valiosas para aprender a mantenerte seguro.
- **Professor Henry:** Puedo darte un examen para que lo realices y, una vez completado, puedes entregármelo para corregirlo. ¿Quieres realizar la prueba? No te costará nada.
- [Menu]: Selecciona una opción
  - [Choice]: Sí, por favor.
    - **Player:** Sí, por favor.
    - (Condition: With the test paper already in backpack:)
      - **Professor Henry:** En ese momento, yo... ¡oh! ¿Ya tienes un examen? ¡Excelente! Bueno, buena suerte entonces.
      - **Player:** Eh, gracias.
    - (Condition: Without the test paper in backpack:)
      - **Professor Henry:** Justo entonces. Aquí está el examen. Cuando hayas completado todas las preguntas, tráemelas para que las califique.
      - **Player:** Está bien, gracias.
  - [Choice]: Ahora no, gracias.
    - **Player:** Ahora no, gracias.
    - **Professor Henry:** Muy bien. Vuelve a verme de nuevo si cambias de opinión.

#### Antes de completar la prueba

- **Player:** Hola, profesor.
- **Professor Henry:** Ah, hola de nuevo. ¿Cómo puedo ayudarte?
- (continuea|what-is-this-place)

#### Después de completar la prueba

- **Player:** Hola, profesor.
- **Professor Henry:** Ah, Player. ¿Cómo va la prueba?
- **Player:** Creo que ya terminé.
- **Professor Henry:** ¡Excelente! Entonces déjame marcarte el papel.
- **Professor Henry:** Mmm. Ajá, sí, ya veo. ¡Bien! Sí, eso es correcto.
- **Professor Henry:** ¡Excelente! Permíteme recompensarte por tu trabajo. Tengo estas dos lámparas viejas que quizás te resulten útiles.
- **Professor Henry:** Además, hay un antiguo bloque de cárcel conectado a las celdas debajo del centro de entrenamiento, que han sido invadidas por criaturas feroces. Si buscas en las celdas de la cárcel de abajo, deberías encontrarlo con bastante facilidad.
- **Professor Henry:** Ahora, tus recompensas.
- (removes=test paper) (receives=two Antique lamp (Misthalin Training Centre of Excellence))
- (Action: ¡Has completado la prueba de seguridad el player!)

### With the CS Week clue

- **Professor Henry:** ¡Ajá! ¡Las mejores notas! ¡Bien hecho por resolver esta pista!
- (removes=clue scroll (CS Week))
- (Condition: If the trail continues:)
  - (receives= a new clue scroll (CS Week))
- (Condition: If the trail ends:)
  - (receives=casket (CS Week) y ataúd de seguridad (CS Week))
