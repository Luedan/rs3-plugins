# Boric

- **Original Wiki Page**: [Transcript:Boric](https://runescape.wiki/w/Transcript%3ABoric)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the basement of Doric's hut, north of Falador

- **Boric:** Me alegro de verte de nuevo, compañero. ¿Hay algo que necesites?
- [Menu]: Elige una opción:
  - [Choice]: ¿Tiene alguna tarea Mining para mí?
    - (ver|Tareas Doric y Boric)
  - [Choice]: ¿Cómo va el negocio?
    - (Condition: Before Boric's Task I:)
      - **Boric:** Lentamente. Nos está tomando más tiempo del que estimé alcanzar nuestros objetivos.
    - (Condition: After Boric's Task I:)
      - **Boric:** Estamos llegando allí. Estamos gestionando nuestros suministros por ahora, pero vamos a tener que buscar un mayor crecimiento si queremos internacionalizarnos.
    - (Condition: After Boric's Task II:)
      - **Boric:** Estamos mejorando. Tener trabajadores en minas de todo el mundo ha mejorado nuestros suministros y nos ha permitido un alcance mucho mayor en el mercado.
    - (Condition: After Boric's Task III:)
      - **Boric:** Desde que conseguiste el acuerdo con el Gremio Mining, hemos tenido que rechazar pedidos. ¡Estamos muy ocupados! ¡Doric & Son es una fuerza a tener en cuenta!
  - [Choice]: Lea el Libro del metal de Boric ([number found]/8).
    - (Condition: Before having obtained a Boric's Book of Metal drop:)
      - [Has encontrado 0/8 entradas. Extraiga mithril, luminita y otros minerales y catalizadores que se funden en metales centrales para encontrar sus entradas.]
      - (initial)
    - (Condition: After having obtained a Boric's Book of Metal drop:)
      - (Condition: If all 8 entries have been found and the Heavy Metal achievement has not yet been completed:)
        - ¡Felicitaciones! Has completado: 'Heavy Metal': obtén todas las entradas del Libro de metales de Boric extrayendo los minerales o catalizadores enumerados.
        - (continue)
      - (Se abre el Libro del Metal de Boric).
      - (ver | Libro del metal de Boric)
  - [Choice]: No, sólo estoy de paso.
    - **Boric:** Cuídate.
