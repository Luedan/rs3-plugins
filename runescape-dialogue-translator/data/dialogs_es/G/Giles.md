# Giles

- **Original Wiki Page**: [Transcript:Giles](https://runescape.wiki/w/Transcript%3AGiles)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before setting up the Anachronia base camp

- (ver|Tutorial del campamento base de Anacronia#Instalarse en el campamento base)

### Standard dialogue at Anachronia base camp

- [Menu]: Selecciona una opción
  - [Choice]: Administrar el campamento base.
    - (Se abre la Gestión del Campamento Base.))
  - [Choice]: Colección Archaeology.
    - **Player:** ¿Qué estás coleccionando?
    - ((Before the collection is completed.))
      - **Giles:** He oído que se han encontrado algunos objetos dragonkin en la isla. Estoy buscando un dispositivo y una tableta dragonkin ceremoniales.
      - ((Archaeology collection interface opens.))
    - ((After the collection is completed:))
      - **Giles:** No estoy recopilando nada más por el momento. Ya me has dado todo lo que estaba buscando.
      - ((Archaeology collection interface opens.))
  - [Choice]: Háblame de ti.
    - **Giles:** Ah, realmente no hay mucho que contar...
    - **Giles:** Veamos. Soy contador senior del museo Varrock. Mientras me entrenaba y trabajaba en el palacio, mostré un gran interés por la historia y fui transferido allí para ayudar con la dirección de sus operaciones.
    - **Giles:** Hay muchos grandes planes ahí, pero no tienen mucho sentido cuando se trata de dinero. Por suerte, les ayudé a gestionar un poco mejor sus recursos.
    - **Player:** ¿Es por eso que tardó tanto en construirse el barco que nos trajo aquí?
    - **Giles:** Ah. Ja ja. Sí, ese fue un proyecto que comenzó antes de que yo asumiera el mando. No vi la oportunidad, así que dejé un equipo reducido mientras el museo se centraba en diferentes áreas de interés.
    - **Giles:** Por supuesto, luego ocurrieron ciertos eventos que cambiaron las prioridades. De repente construir el barco era lo más importante y aquí estamos.
    - (initial)
  - [Choice]: Reclamar.
    - **Player:** ¿Tienes algo que pueda reclamar?
    - ((If there is nothing to reclaim or if Desperate Measures hasn't been completed:))
      - **Giles:** No tienes nada que reclamarme en este momento.
    - ((Before creating the cosmic accumulator:))
      - ((If the cosmic focus has been lost:))
        - **Giles:** Encontré este enfoque cósmico, creo que es tuyo.
        - ((Without space in backpack:))
          - **Giles:** Parece que no tienes espacio en el inventario para esto en este momento.
        - ((With space in backpack:))
          - (receives=cosmic focus)
          - Giles amablemente entrega el enfoque Cósmico.
      - ((If the cosmic pyramid has been lost:))
        - **Giles:** ¡Veo que has perdido la pirámide cósmica que te di! Por suerte tengo otro que puedes tener.
        - ((Without space in backpack:))
          - **Giles:** Parece que no tienes espacio en el inventario para esto en este momento.
        - ((With space in backpack:))
          - (receives=cosmic pyramid)
          - Giles amablemente entrega la pirámide cósmica.
    - ((After creating the cosmic accumulator:))
      - **Giles:** Encontré este objeto que se parece a la pirámide cósmica que te di, supuse que era tuyo.
      - ((Without space in backpack:))
        - **Giles:** Parece que no tienes espacio en el inventario para esto en este momento.
      - ((With space in backpack:))
        - (receives=cosmic accumulator)
        - Giles amablemente entrega el acumulador Cósmico.
  - [Choice]: Adiós.
    - **Giles:** Me aseguraré de que el campamento base persevere mientras no estés.
