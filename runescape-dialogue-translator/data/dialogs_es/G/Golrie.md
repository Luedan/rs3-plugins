# Golrie

- **Original Wiki Page**: [Transcript:Golrie](https://runescape.wiki/w/Transcript%3AGolrie)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Gnome Village Dungeon


#### Antes de la búsqueda de la cascada

- **Golrie:** ¿Qué estás haciendo aquí abajo?<br>Vete antes de meterte en problemas.

#### Después de la búsqueda de la cascada

- **Player:** Hola Golrie. ¿Cómo estás?
- (Condition: With Glarial's pebble in backpack or bank:)
  - **Golrie:** Mejor ahora que estoy en el lado derecho de esas barras. Espero que ese guijarro te haya ayudado.
  - (continue|cadarn)
- (Condition: Without Glarial's pebble in backpack or bank:)
  - **Golrie:** Mejor ahora que estoy en el lado derecho de esas barras. De todos modos... Es curioso que deberías aparecer.
  - **Player:** ¿Por qué?
  - **Golrie:** ¿Recuerdas ese guijarro que te regalé? Bueno, apareció aquí en el suelo, ¿te gustaría recuperarlo?
  - [Menu]: Selecciona una opción
    - [Choice]: Sí por favor.
      - **Player:** Sí, por favor.
      - (receives=Glarial's pebble)
      - [Golrie te entrega un guijarro.]
      - (continue|cadarn)
    - [Choice]: No, gracias.
      - **Player:** No, gracias.
      - **Golrie:** Muy bien, pero está aquí si lo necesitas.
      - (continue|cadarn)
- (Condition: With Cadarn lineage in backpack or bank:)
  - **Golrie:** De todos modos tengo mucho que hacer. Esos Hob-gobs dejaron mis cosas aquí en un gran desastre.
  - (continue|a-key)
- (Condition: Without Cadarn lineage in backpack or bank:)
  - **Golrie:** Oh... eso me recuerda... Como te gustan las cosas élficas, encontré esto.
  - (receives=Cadarn lineage)
  - [Golrie te entrega un libro antiguo.]
  - (continue|a-key)
- (Condition: With a key in backpack or bank:)
  - **Player:** Bueno, adiós.
- (Condition: Without a key in backpack or bank:)
  - [Menu]: Selecciona una opción
    - [Choice]: ¿Puedo usar tu llave?
      - **Player:** ¿Puedo usar tu clave?
      - **Golrie:** Si quieres entrar allí con esos idiotas, es asunto tuyo.
      - (receives=a key)
      - [Golrie te entrega una llave.]
      - **Player:** Gracias, hasta luego.
    - [Choice]: Adiós Golrie.
      - **Player:** Adiós Golrie.
      - **Golrie:** Hasta luego.

#### Después del camino de Glouphrie

- **Player:** ¡Hola Golrie! ¿Cómo estás?
- **Golrie:** ¡Hola, Player! Fue amable de tu parte venir a charlar. Estoy ocupado clasificando las cosas en orden cronológico alfanumérico. ¿Puedo hacer algo por ti?
- [Menu]: Selecciona una opción
  - [Choice]: En realidad, vine aquí por el guijarro de Glarial.
    - (above|After Waterfall Quest)
  - [Choice]: Estaré bien, gracias.
    - **Player:** Estaré bien, gracias.

#### Después del prisionero de Glouphrie

- **Golrie:** Hola, Player. ¿Viniste a contarme sobre el abuelo?
- [Menu]: Selecciona una opción
  - [Choice]: [Talk about Prisoner of Glouphrie]
    - **Golrie:** ¡Player! ¡No puedo agradecerte lo suficiente por sacar al abuelo de ese aprieto! No puedes imaginar el problema en el que te habrías metido si le hubiera pasado algo. No puedo creer que hayas dejado esa carta en un libro.
    - **Player:** Está bien, Golrie. Todo salió bien al final. Aunque estoy bastante seguro de que tu abuelo no ha abandonado sus planes de acabar con Glouphrie y Arposandra. Vigílalo y asegúrate de que no haga ninguna tontería, ¿quieres?
    - **Golrie:** Mamá te ayudará con eso, no te preocupes. Seguiré haciendo lo que hago. Ya sabes, catalogación y esas cosas.
    - **Player:** Escuché que tu madre se quedará en el pueblo ahora para entrenarse como susurradora de árboles. Tu mamá está llena de sorpresas.
    - **Golrie:** ¿Sí? Bueno, tu mamá...
    - **Golrie:** ¡No, es broma!
    - **Golrie:** ¡De todos modos! ¡Gracias de nuevo, Player! ¡Nos vemos por ahí!
    - **Player:** ¡Adiós!
  - [Choice]: En realidad, vine aquí por el guijarro de Glarial.
    - **Player:** En realidad, vine aquí por el guijarro de Glarial.
    - (Condition: With Glarial's pebble in backpack or bank:)
      - **Golrie:** No lo he visto recientemente. ¿Supongo que lo tienes?
      - **Player:** ¡Efectivamente! Gracias.
      - (continue|cadarn)
    - (Condition: Without Glarial's pebble in backpack or bank:)
      - **Golrie:** Estás de suerte: alguien me lo tiró el otro día.
      - (receives=Glarial's pebble)
      - [Golrie te entrega un guijarro.]
      - (continue|cadarn2)
    - (Condition: Without Cadarn lineage in backpack or bank:)
      - **Golrie:** Oh... eso me recuerda: dado que eres un elfofilo, encontré esto.
      - (receives=Cadarn lineage)
      - [Golrie te entrega un libro antiguo.]
      - (continue|a-key2)
    - (Condition: With a key in backpack or bank:)
      - **Player:** Adiós Golrie.
      - **Golrie:** Hasta luego.
    - (Condition: Without a key in backpack or bank:)
      - [Menu]: Selecciona una opción
        - [Choice]: ¿Puedo usar tu llave?
          - **Player:** ¿Puedo usar tu clave?
          - **Golrie:** Si quieres entrar allí con esos idiotas, es asunto tuyo.
          - (receives=a key)
          - [Golrie te entrega una llave.]
          - **Player:** Gracias, hasta luego.
        - [Choice]: Adiós Golrie.
          - **Player:** Adiós Golrie.
          - **Golrie:** Hasta luego.
