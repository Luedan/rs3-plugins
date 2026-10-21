# Jossik

- **Original Wiki Page**: [Transcript:Jossik](https://runescape.wiki/w/Transcript%3AJossik)
- **Letter**: `J`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue at the Lighthouse

- **Jossik:** Hola de nuevo aventurero. ¿Qué te trae por este camino?
- [Menu]: Elige una opción:
  - [Choice]: ¿Puedo ver tus productos?
    - **Player:** ¿Puedo ver tus productos?
    - **Jossik:** ¡Claro! Creo que estarás de acuerdo, mis precios son notables.
    - (opens=The Lighthouse Store)
  - [Choice]: ¿Has encontrado algún libro de oraciones nuevo?
    - (below|holy book)
    - [Choice]: I think I may have found your uncle.|cond=Si la misión Blood Runs Deep se ha completado:
      - **Player:** Creo que pude haber encontrado a tu tío.
      - **Jossik:** ¿En serio? ¿Dónde está? ¿Cómo está él?
      - **Player:** Bueno, los magos de Lunar Isle lo estaban cuidando pero, cuando mejoró, quiso irse, así que tuvieron que dejarlo ir.
      - **Jossik:** ¿Se acaba de ir? Oh Dios... Bueno, ahora nunca lo encontraré.
      - **Player:** Al menos sabemos que está vivo y bien. Estoy seguro de que aparecerá tarde o temprano.

### Holy-book option

- {{anchor|holy book}}**Player:** ¿Has encontrado algún libro de oraciones nuevo?
- (Condition: Si el player no ha comprado todos los libros de dioses dañados disponibles:)
  - **Jossik:** ¡Curiosamente sí! ¡Encontré estos libros [número] en ataúdes el otro día! Te vendo uno por 5000 coins: ¿qué dices?
  - [Menu]: Selecciona una opción
    - [Choice]: comprar un libro
      - (Se abre la interfaz "Elegir un libro").
      - (Condition: Si compras alguno de los libros:)
        - (removes=5,000 coins) (receives=the selected damaged book)
        - **Jossik:** ¡Aquí tienes!
    - [Choice]: no compres nada
      - **Player:** No, gracias.
      - **Jossik:** ¡Está bien! Haz lo que quieras.
- (Condition: Si el player ha comprado todos los libros de dioses dañados disponibles:)
  - **Jossik:** No. Lo siento, aventurero, ¡supongo que los has encontrado todos! Sin embargo, te avisaré si aparece alguno nuevo.
- (Condition: Si el player ha perdido uno de los libros de dioses dañados que compró anteriormente:)
  - (receives=one of their missing god book with all previously attached pages intact)
  - **Jossik:** ¡De hecho, lo hice! Este libro apareció en la playa no hace mucho, ¡lo reconocí como tuyo inmediatamente! ¡Aquí tienes!
