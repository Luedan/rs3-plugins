# Marius Giste

- **Original Wiki Page**: [Transcript:Marius Giste](https://runescape.wiki/w/Transcript%3AMarius%20Giste)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Lacking backpack space to claim a replacement replica piece}}

### In Varrock Museum


#### Hablando con él antes de encontrar una roca extraña.

- **Marius Giste:** Hola. ¡Bienvenidos al Museo Varrock! Siéntete libre de mirar a tu alrededor.

#### Diálogo por primera vez después de encontrar una roca extraña.

- **Marius Giste:** Hola. ¡Bienvenidos al Museo Varrock! Siéntete libre de mirar a tu alrededor.
- **Player:** Encontré una piedra mientras entrenaba.
- **Marius Giste:** ¿Una piedra? Bueno, echemos un vistazo, aunque dudo que podamos ayudarte con las piedras; Eso es más bien una geología.
- **Marius Giste:** ¡Dios mío!
- **Player:** ¿Qué?
- **Marius Giste:** ¡Caden Azro! ¿Estoy en lo cierto? ¿Podría ser?
- **Caden Azro:** Sí, ves la muesca aquí... y las líneas allá...
- **Player:** ¿Qué es? ¿Qué encontré?
- **Marius Giste:** Mi querido [sir/madam], mi estimado colega y yo coincidimos en que has descubierto parte de Dahmaroc, un mago de los primeros días de la magia.
- **Marius Giste:** Hasta ahora creíamos que el mito era solo eso: un mito. Sin embargo, parece que las historias pueden ser ciertas.
- **Player:** ¿Qué historias?
- **Marius Giste:** Bueno, solo hemos podido juntar fragmentos aquí y allá, pero parece que era un mago de gran poder que quedó atrapado en una batalla todopoderosa en la Segunda Edad.
- **Marius Giste:** Parece que esta batalla terminó sobre quién debería tener la mayor parte de las runas que las razas inteligentes habían encontrado alrededor de Gielinor.
- **Player:** ¿Runas? ¿Como los que uso para magia ahora? Seguramente son ilimitados.
- **Marius Giste:** Ahora lo son, sí, pero en aquel entonces había una oferta limitada. Al menos, eso es lo que indican los fragmentos de información que hemos encontrado.
- **Player:** Interesante. Entonces, ¿qué pasó con Dahmaroc?
- **Marius Giste:** Hasta donde sabemos, perdió, fue convertido en piedra y luego maldecido. Se dice que estaba condenado a pasar la eternidad con lo que más amaba...
- **Player:** Eso no suena tan mal. ¿Tenía esposa?
- **Marius Giste:** Bueno, no estamos seguros de eso. Sabemos que le encantaba adquirir conocimientos y habilidades en nuevas disciplinas. Aunque no tiene gusto por pelear. De hecho, fue el combate lo que resultó ser su perdición.
- [Menu]: Selecciona una opción
  - [Choice]: Voy a intentar recomponerlo.
    - **Player:** Voy a intentar recomponerlo. ¿Puedo usar ese pedestal de allí?
    - **Marius Giste:** Bueno, no estoy seguro. Estábamos reservando eso para una estatua de Saradomin...
    - **Player:** Oh, continúa. ¿Qué es lo peor que podría pasar? Ya hay toneladas de trozos de roca por aquí.
    - **Marius Giste:** Continúa entonces. Sin embargo, asegúrese de emparejar correctamente las rocas. Se entrelazan, ya ves.
    - {{anchor|givebag}}(Condición: Si no tienes una bolsa de colección de estatuas y tienes un espacio de inventario libre:)
      - **Marius Giste:** Por cierto, si quieres una bolsa para guardar más hallazgos, te la puedo proporcionar.
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: Sí por favor.
        - **Player:** Sí, por favor.
        - (Condition: Sin espacio en backpack:)
          - **Marius Giste:** Desafortunadamente, no tienes espacio para ello.
          - (otras|opciones iniciales)
        - (Condition: Con espacio en backpack:)
          - [Marius Giste te entrega una bolsa resistente.]
          - (receives=statue collection bag)
          - (otras|opciones iniciales)
      - [Choice]: No gracias.
        - **Player:** No, gracias.
        - (otras|opciones iniciales)
    - (otras|opciones iniciales)
  - [Choice]: ¿Cómo puedo dejar de recibir estas piedras?
    - (below|stoprocks)

#### Diálogo normal

- **Marius Giste:** Hola. ¡Bienvenidos al Museo Varrock! Siéntete libre de mirar a tu alrededor.
- {{anchor|initialoptions}} [Menú]: seleccione una opción
  - [Choice]: Dime otra vez de dónde viene la estatua.
    - **Player:** Dime otra vez de dónde viene la estatua.
    - (arriba2|estatuaesde)
  - [Choice]: ¿Gemelo? ¿Cómo consigo su gemelo?
    - **Player:** ¿Gemelo? ¿Cómo consigo su gemelo?
    - **Marius Giste:** Bueno, no estoy seguro, pero sospecho que de la misma manera que obtuviste el primero.
    - **Player:** ¿Por qué necesito un gemelo?
    - **Marius Giste:** Porque, curiosamente, se entrelazan en pares para formar toda la estatua sin necesidad de ningún tipo de adhesivo.
    - (Condition: Si el player ya tiene una bolsa de recolección de estatuas:)
      - **Marius Giste:** Ya tienes una bolsa de colección de estatuas.
    - (Condition: Si el player no tiene bolsa de recolección de estatuas:)
      - (continuea|givebag)
  - [Choice]: ¿Cómo lo agrego a la estatua?
    - **Player:** ¿Cómo lo agrego a la estatua?
    - **Marius Giste:** Si tienes rocas extrañas que encontraste durante el entrenamiento, simplemente usa los pares de piezas en el pedestal de allí.
    - **Marius Giste:** Si te refieres a una de las réplicas que hicimos para ti, usa los pares de piezas de réplica en el pedestal de tu casa.
    - (continuea|givebag2)
  - [Choice]: Más...
    - [Menu]: Elige una opción:
      - [Choice]: Atrás...
        - (initial|initialoptions)
      - [Choice]: Encontré una piedra mientras entrenaba.
        - **Player:** Encontré una piedra mientras entrenaba.
        - **Marius Giste:** ¿Una de esas rocas para la estatua? Bueno, si tienes su gemelo, adelante y agrégalo, por supuesto.
        - (continuea|givebag2)
      - [Choice]: Tendré que mantener una lista de piezas.
        - **Player:** Tendré que mantener una lista de piezas.
        - (Condition: Sin espacio en backpack:)
          - **Marius Giste:** Sí, eso es realmente sabio. Avísame cuando tengas espacio y te daré algo de papel.
          - (continuea|givebag2)
        - (Condition: Con espacio en backpack:)
          - **Marius Giste:** Sí, sería prudente. Aquí tienes algo de papel para usar.
          - [Marius Giste te entrega una hoja de papel en la que garabateas rápidamente.]
          - (receives=Statue of Dahmaroc list)
          - (initial|initialoptions)
        - (Condition: Con la lista ya en backpack:)
          - **Marius Giste:** Sí, sería prudente. Veo que ya tienes uno allí.
          - (initial|initialoptions)
      - [Choice]: cond=If the player has completed the statue at least once before, and destroyed a replica piece:|He perdido una réplica.
        - (Condition: Sin espacio en backpack:)
          - {{Tmissing}}
        - (Condition: Con espacio en backpack:)
          - **Player:** He perdido una réplica.
          - El arqueólogo te entrega un .
          - (receives=Replica statue piece)
          - **Marius Giste:** Ahí lo tienes.
          - (initial|initialoptions)
      - {{anchor|stoprocks}} [Elección]: cond=Con la recolección de rocas activada|¿Cómo puedo dejar de recibir estas rocas?
        - **Player:** ¿Cómo puedo dejar de recibir estas piedras?
        - **Marius Giste:** Ah, recuerdo un encantamiento que podría ayudar. Creo que fue...
        - (Action: Marius Giste lanza un hechizo)
        - {{RSChat|shadow=yes|colour=yellow|Incanto Negato Silicis}}
        - (initial|initialoptions)
      - [Choice]: cond=With collecting rocks turned off|¿Cómo puedo conseguir estas rocas nuevamente?
        - **Player:** ¿Cómo puedo recuperar estas rocas?
        - **Marius Giste:** Ah, recuerdo un encantamiento que podría ayudar. Creo que fue...
        - (Action: Marius Giste lanza un hechizo)
        - {{RSChat|shadow=yes|colour=yellow|Incanto Additto Silicis}}
        - (continuea|givebag)
      - [Choice]: Me gustaría restablecer mi estatua.
        - **Player:** Me gustaría restablecer mi estatua.
        - (Condition: Si el pedestal está vacío:)
          - **Marius Giste:** Ah, hay un pequeño problema ahí. No tienes que restablecer.
        - (Condition: Si al pedestal se le agregaron al menos un par de rocas:)
          - **Marius Giste:** ¿Estás seguro? ¡Perderás todo tu progreso!
          - Advertencia: perderás todo tu progreso, incluida cualquier estatua construida en tu casa. Esto no se puede revertir.
          - [Menu]: Elige una opción:
            - [Choice]: si
              - (Action: La estatua está limpia.)
            - [Choice]: No
              - (end)

#### Al completar la estatua

- (Action: Una escena de la estatua terminada ganando un color realista y luego comenzando a temblar en el pedestal.)
- **Player:** {{RSChat|shadow=yes|colour=yellow|What the...}}
- (Action: Una escena de la estatua desmoronándose en pedazos y empujando a el player hacia atrás y aturdiéndolos.)
- **Player:**{{RSChat|shadow=yes|colour=yellow|Oof!}}
- **Player:** ¡Lo logré! ¡Terminé la estatua!
- Marius Giste se quita pequeños trozos de roca.
- **Marius Giste:** Sí... Lo vi explotar. Parece que la maldición sigue activa.
- **Marius Giste:** Lo hiciste bien. Hemos estado estudiando la estatua mientras la construías y hemos logrado hacer una réplica de una de las piezas para ti. Quizás le gustaría empezar a construir usted mismo una estatua en su estudio.
- (Condition: Si el player nunca ha completado la estatua antes:)
  - (Condition: Sin un espacio backpack libre:)
    - **Marius Giste:** Cuando tengas espacio, regresa y recoge el pedestal para colocarlo.
  - (Condition: Con un espacio backpack gratuito:)
    - **Marius Giste:** Aquí tienes un pedestal para que construyas la estatua en tu casa.
    - (receives=statue plinth)
    - [El arqueólogo le entrega un pedestal resistente pero sorprendentemente ligero para su réplica de estatua.]
    - (continue)
- (Condition: Sin un espacio backpack libre:)
  - **Marius Giste:** Cuando tengas espacio, regresa y recoge la réplica.
- (Condition: Con un espacio backpack gratuito:)
  - **Marius Giste:** Ahí lo tienes.
  - (receives=replica statue piece)
  - [El arqueólogo te entrega una réplica de la estatua.]
  - **Marius Giste:**Ahí tienes.
  - (initial|initialoptions)

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
