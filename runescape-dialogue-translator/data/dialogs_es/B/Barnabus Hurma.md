# Barnabus Hurma

- **Original Wiki Page**: [Transcript:Barnabus Hurma](https://runescape.wiki/w/Transcript%3ABarnabus%20Hurma)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Lacking backpack space to claim a replacement replica piece}}

### In Varrock Museum


#### Intentar interactuar con el pedestal antes de hablar con él.

- **Barnabus Hurma:** ¡Oye! Deja ese pedestal en paz. Es para la estatua de Saradomin que vamos a construir.

#### Diálogo por primera vez antes de encontrar una roca extraña.

- **Barnabus Hurma:** Hola. ¡Bienvenidos al Museo Varrock! Siéntete libre de mirar a tu alrededor.

#### Primera vez después de encontrar una roca extraña.

- **Barnabus Hurma:** Hola. ¡Bienvenidos al Museo Varrock! Siéntete libre de mirar a tu alrededor.
- **Player:** Encontré una piedra mientras entrenaba.
- **Barnabus Hurma:** ¿Una piedra? Bueno, echemos un vistazo, aunque dudo que podamos ayudarte con las piedras; Eso es más bien un geológico. ¡Dios mío!
- **Player:** ¿Qué?
- **Barnabus Hurma:** ¡Marius Giste! ¿Estoy en lo cierto? ¿Podría ser?
- **Marius Giste:** Sí, puedes ver la muesca aquí... y las líneas allá...
- **Player:** ¿Qué es? ¿Qué encontré?
- **Barnabus Hurma:** Mi querido señor, mi estimado colega y yo estamos de acuerdo en que ha descubierto parte de Dahmaroc, un mago de los primeros días de la magia.
- **Barnabus Hurma:** Hasta ahora creíamos que el mito era solo eso: un mito. Sin embargo, parece que las historias pueden ser ciertas.
- **Player:** ¿Qué historias?
- **Barnabus Hurma:** Bueno, solo hemos podido juntar fragmentos aquí y allá, pero parece que era un mago de gran poder que quedó atrapado en una batalla todopoderosa en la Segunda Edad.
- **Barnabus Hurma:** Parece que esta batalla terminó sobre quién debería tener la mayor parte de las runas que las razas inteligentes habían encontrado alrededor de Gielinor.
- **Player:** ¿Runas? ¿Como los que uso para magia ahora? Seguramente son ilimitados.
- **Barnabus Hurma:** Ahora lo son, sí, pero en aquel entonces había una oferta limitada. Al menos, eso es lo que indican los fragmentos de información que hemos encontrado.
- **Player:** Interesante. Entonces, ¿qué pasó con Dahmaroc?
- **Barnabus Hurma:** Hasta donde sabemos, perdió, fue convertido en piedra y luego maldecido. Se dice que estaba condenado a pasar la eternidad con lo que más amaba...
- **Player:** Eso no suena tan mal. ¿Tenía esposa?
- **Barnabus Hurma:** Bueno, no estamos seguros de eso. Sabemos que le encantaba adquirir conocimientos y habilidades en nuevas disciplinas. Aunque no tiene gusto por pelear. De hecho, fue el combate lo que resultó ser su perdición.
- [Menu]: Selecciona una opción
  - [Choice]: Voy a intentar recomponerlo.
    - **Player:** Voy a intentar recomponerlo. ¿Puedo usar ese pedestal de allí?
    - **Barnabus Hurma:** Bueno, no estoy seguro. Estábamos reservando eso para una estatua de Saradomin...
    - **Player:** Oh, continúa. ¿Qué es lo peor que podría pasar? Ya hay toneladas de trozos de roca por aquí.
    - **Barnabus Hurma:** Continúa entonces. Sin embargo, asegúrese de emparejar correctamente las rocas. Se entrelazan, ya ves.
    - {{anchor|givebag}}(Condición: Si no tienes una bolsa de recolección de estatuas y tienes un espacio libre en backpack :)
      - **Barnabus Hurma:** Por cierto, si quieres una bolsa para guardar más hallazgos, te la puedo proporcionar.
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: Sí por favor.
        - **Player:** Sí, por favor.
        - (Condition: Sin espacio en backpack:)
          - **Barnabus Hurma:** Desafortunadamente, no tienes espacio para ello.
          - (otras|opciones iniciales)
        - (Condition: Con espacio en backpack:)
          - [Barnabus Hurma te entrega una bolsa resistente.]
          - (receives=statue collection bag)
          - (otras|opciones iniciales)
      - [Choice]: No gracias.
        - **Player:** No, gracias.
        - (otras|opciones iniciales)
  - [Choice]: ¿Cómo puedo dejar de recibir estas piedras?
    - (below|stoprocks)

#### Diálogo estándar

- **Barnabus Hurma:** Hola. ¡Bienvenidos al Museo Varrock! Siéntete libre de mirar a tu alrededor.
- {{anchor|initialoptions}} [Menú]: seleccione una opción
  - [Choice]: Dime otra vez de dónde viene la estatua.
    - **Player:** Dime otra vez de dónde viene la estatua.
    - (arriba2|estatuaesde)
  - [Choice]: ¿Gemelo? ¿Cómo consigo su gemelo?
    - **Player:** ¿Gemelo? ¿Cómo consigo su gemelo?
    - **Barnabus Hurma:** Bueno, no estoy seguro, pero sospecho que de la misma manera que obtuviste el primero.
    - **Player:** ¿Por qué necesito un gemelo?
    - **Barnabus Hurma:** Porque, curiosamente, se entrelazan en pares para formar toda la estatua sin necesidad de ningún tipo de adhesivo.
    - (Condition: Si el player ya tiene una bolsa de recolección de estatuas:)
      - **Barnabus Hurma:** Ya tienes una bolsa de colección de estatuas.
    - (Condition: Si el player no tiene bolsa de recolección de estatuas:)
      - (continuea|givebag)
  - [Choice]: ¿Cómo lo agrego a la estatua?
    - **Player:** ¿Cómo agrego una pieza a la estatua?
    - **Barnabus Hurma:** Si tienes rocas extrañas que encontraste durante el entrenamiento, simplemente usa los pares de piezas en el pedestal de allí.
    - **Marius Giste:** Si te refieres a una de las réplicas que hicimos para ti, usa los pares de piezas de réplica en el pedestal de tu casa.
    - (continuea|givebag2)
  - [Choice]: Más...
    - [Menu]: Elige una opción:
      - [Choice]: Atrás...
        - (initial|initialoptions)
      - [Choice]: Encontré una piedra mientras entrenaba.
        - **Player:** Encontré una piedra mientras entrenaba.
        - **Barnabus Hurma:** ¿Una de esas rocas para la estatua? Bueno, si tienes su gemelo, adelante y agrégalo, por supuesto.
        - (continuea|givebag2)
      - [Choice]: Tendré que mantener una lista de piezas.
        - **Player:** Tendré que mantener una lista de piezas.
        - (Condition: Sin espacio en backpack:)
          - **Barnabus Hurma:** Sí, eso es realmente sabio. Avísame cuando tengas espacio y te daré algo de papel.
          - (continuea|givebag2)
        - (Condition: Con espacio en backpack:)
          - **Barnabus Hurma:** Sí, sería prudente. Aquí tienes algo de papel para usar.
          - [Barnabus Hurma te entrega una hoja de papel en la que garabateas rápidamente.]
          - (receives=Statue of Dahmaroc list)
          - (initial|initialoptions)
        - (Condition: Con la lista ya en backpack:)
          - **Barnabus Hurma:** Sí, sería prudente. Veo que ya tienes uno allí.
          - (initial|initialoptions)
      - [Choice]: cond=If the player has completed the statue at least once before, and destroyed a replica piece:|He perdido una réplica.
        - (Condition: Sin espacio en backpack:)
          - {{Tmissing}}
        - (Condition: Con espacio en backpack:)
          - **Player:** He perdido una réplica.
          - El arqueólogo te entrega un .
          - (receives=Replica statue piece)
          - **Barnabus Hurma:** Ahí lo tienes.
          - (initial|initialoptions)
      - {{anchor|stoprocks}} [Elección]: cond=Con la recolección de rocas activada|¿Cómo puedo dejar de recibir estas rocas?
        - **Player:** ¿Cómo puedo dejar de recibir estas piedras?
        - **Barnabus Hurma:** Ah, recuerdo un encantamiento que podría ayudar. Creo que fue...
        - (Action: Barnabus Hurma lanza un hechizo)
        - {{RSChat|shadow=yes|colour=yellow|Incanto Negato Silicis}}
        - (initial|initialoptions)
      - [Choice]: cond=With collecting rocks turned off|¿Cómo puedo conseguir estas rocas nuevamente?
        - **Player:** ¿Cómo puedo recuperar estas rocas?
        - **Barnabus Hurma:** Ah, recuerdo un encantamiento que podría ayudar. Creo que fue...
        - (Action: Barnabus Hurma lanza un hechizo)
        - {{RSChat|shadow=yes|colour=yellow|Incanto Additto Silicis}}
        - (continuea|givebag)
      - [Choice]: Me gustaría restablecer mi estatua.
        - **Player:** Me gustaría restablecer mi estatua.
        - (Condition: Si el pedestal está vacío:)
          - **Barnabus Hurma:** Ah, hay un pequeño problema ahí. No tienes que restablecer.
        - (Condition: Si al pedestal se le agregaron al menos un par de rocas:)
          - **Barnabus Hurma:** ¿Estás seguro? ¡Perderás todo tu progreso!
          - Advertencia: perderás todo tu progreso, incluida cualquier estatua construida en tu casa. Esto no se puede revertir.
          - [Menu]: Elige una opción:
            - [Choice]: si
              - (Action: La estatua está limpia.)
            - [Choice]: No
              - (end)

#### Recoge la bolsa de rocas

- (above|givebag2)

#### Alternar colección de rocas


##### Con la recolección de rocas activada

- Ya no encontrarás rocas extrañas.
- (ventana emergente)
  - (Ventana emergente: ya no encontrarás rocas extrañas).

##### Con la recolección de piedras desactivada

- Ahora encontrarás rocas extrañas.
- (ventana emergente)
  - (Ventana emergente: ahora encontrarás rocas extrañas).

#### Intentando completar otra estatua de Dahmaroc antes de que haya pasado una semana

- *Este diálogo ya no está disponible.*
- **Barnabus Hurma:** Una explosión por semana es suficiente, ¡gracias! Todavía estoy sacando trozos de mago petrificado de mi té.
