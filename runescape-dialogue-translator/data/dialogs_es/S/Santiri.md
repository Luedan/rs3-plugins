# Santiri

- **Original Wiki Page**: [Transcript:Santiri](https://runescape.wiki/w/Transcript%3ASantiri)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In western Keldagrim


#### Diálogo estándar

- (Condition: Antes de La primogenitura de los enanos:)
  - **Santiri:** ¡Bienvenido, humano, a Quality Weapons Shop! ¿Puedo interesarte en una compra?
  - (continue)
- (Condition: Después de La primogenitura de los enanos:)
  - **Santiri:** ¡Bienvenido, humano, a Quality Weapons Shop! Desde la derrota del Hacha Roja, ahora tengo bastones de batalla de dragones en stock. ¿Puedo interesarte en una compra?
  - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: Sí, estoy buscando algunas armas.
    - **Player:** Sí, estoy buscando algunas armas.
    - (opens= Quality Weapons Shop)
  - [Choice]: cond=After Birthright of the Dwarves|¿Bastones de batalla de dragones?
    - **Player:** ¿Bastones de batalla de dragones?
    - **Santiri:** ¡Sí! Colonel Grenda recuperó el dragón battlestaff de Hreidmar de su palacio. Lo examiné y aprendí a crear más.
    - **Santiri:** Es un arma extraordinaria. Hugi, el bibliotecario, afirma que podría remontarse a los primeros días de Keldagrim, ¡incluso antes de la Era de los Reyes!
    - **Santiri:** Desafortunadamente requiere muchas materias primas costosas, así que tengo que cobrarte por ellas, incluso si condujiste a su captura.
    - **Santiri:** ¿Estás interesado?
    - (otro)
  - [Choice]: No gracias.
    - **Player:** No, gracias.

#### Diálogo de minitarea

- **Santiri:** Buenos días para ti, humano. Tengo una pequeña tarea para ti, ¿estás interesado?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Cuál es la tarea?
    - **Player:** ¿Cuál es la tarea?
    - **Santiri:** Oh, no es nada demasiado importante. Pero necesito [item] en los próximos minutos [número].
    - **Player:** Claro, lo tengo. Eso es [item] en los próximos minutos [número], me pondré manos a la obra.
  - [Choice]: Lo siento, estoy un poco ocupado.
    - **Player:** Lo siento, estoy un poco ocupado.
    - **Santiri:** No hay problema, ¡buscaré a alguien más para hacerlo!

##### Hablar con Santiri sin el elemento

- **Santiri:** ¿Conseguiste [item], tal vez?
- [Menu]: Selecciona una opción
  - [Choice]: No, he renunciado a eso.
    - **Player:** No, ya me di por vencido.
    - **Santiri:** Es muy desafortunado escuchar eso. Supongo que tendré que encontrar a alguien más ahora.
  - [Choice]: No, todavía los estoy buscando.
    - **Player:** No, todavía los estoy buscando.
    - **Santiri:** Sigue así, estoy seguro de que lo conseguirás.

##### Hablando con Santiri con el artículo

- **Player:** ¡Mira, te tengo tu [item]!
- **Santiri:** ¡Eso es maravilloso, muchas gracias Player! ¿Quieres que te pague en oro o quieres que te enseñe a atacar con estos?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Muéstrame el oro!
    - **Player:** ¡Muéstrame el oro!
    - (receives=coins)
  - [Choice]: Ilumíname.
    - **Player:** Ilumíname.
    - (Action: La pantalla aparece y desaparece)
    - (receives=experience)
    - Te sientes más experimentado.
