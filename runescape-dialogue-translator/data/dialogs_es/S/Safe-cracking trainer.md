# Safe-cracking trainer

- **Original Wiki Page**: [Transcript:Safe-cracking trainer](https://runescape.wiki/w/Transcript%3ASafe-cracking%20trainer)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Thieves' Guild


#### Diálogo por primera vez

- **Player:** Hola. ¿A qué te dedicas?
- **Safe-cracking trainer:** Soy el trainer de las cajas fuertes como estas.
- **Player:** No parece que necesiten mucho entrenamiento...
- **Safe-cracking trainer:** Har-dee-har. No, entreno a ladrones para que los abran. ¿Quieres escuchar más?
- [Menu]: Selecciona una opción
  - [Choice]: Con mucho gusto.
    - (Condition: Ante un gremio propio:)
      - **Safe-cracking trainer:** El defecto fatal de las cajas fuertes es que sus mecanismos de cierre son muy ruidosos.
      - **Safe-cracking trainer:** Si escuchas, podrás oír cómo los vasos hacen clic cuando los colocas en el lugar correcto. Pero estoy seguro de que un ladrón de tu calibre los abrirá en poco tiempo.
      - **Safe-cracking trainer:**Una vez que hayas contribuido más al gremio, incluso te enseñaré cómo abrir estas intrincadas cajas fuertes.
      - **Safe-cracking trainer:** Eres más que bienvenido a ejercitar tus dedos en mis cajas fuertes de pared falsas. No hay nada en ellos más que pañuelos, tengo que guardarlos en algún lugar.
    - (Condition: Después de Un gremio propio:)
      - (below|youllcomeacross)
  - [Choice]: Sobre esos pañuelos...
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Para qué sirven estos pañuelos?{{anchor|hankies}}
        - **Player:** ¿Para qué sirven estos pañuelos?
        - **Safe-cracking trainer:** Oh, los usamos para realizar un seguimiento del regimiento de entrenamiento de nuestros miembros. Los pañuelos azules te darán un punto, los rojos valen cuatro. Puedes reclamar una recompensa de cualquier trainer con tus puntos pañuelo.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Para qué sirven estos pañuelos?
            - (arriba)
          - [Choice]: ¿Con qué frecuencia puedo hacer esto?
            - **Player:** ¿Con qué frecuencia puedo hacer esto?
            - **Safe-cracking trainer:** La cantidad de puntos de pañuelo que puedes reclamar depende de tu dedicación al arte. Por el momento, puedes reclamar un pañuelo de puntos [amount] y {{Sic}} de entrenamiento por semana.
            - (otro)
          - [Choice]: ¿Qué actividades dan qué pañuelos?
            - **Player:** ¿Qué actividades dan qué pañuelos?
            - **Safe-cracking trainer:** Nuestras zapatillas de carterismo, cajas fuertes y cofres fáciles llevan pañuelos azules; Los pañuelos rojos se pueden encontrar en las zapatillas deportivas y detrás de cerraduras más duras.
            - (otro)
          - [Choice]: Adiós por ahora.
            - **Player:** Adiós por ahora.
      - [Choice]: ¿Cuantos puntos de pañuelo tengo?
        - **Player:** ¿Cuántos puntos de pañuelo tengo?
        - (Condition: Sin puntos:)
          - **Safe-cracking trainer:** Aún no has acumulado puntos de pañuelo. Puedes reclamar la recompensa hasta [amount] puntos más esta semana.
        - (Condition: Con puntos:)
          - **Safe-cracking trainer:** Has acumulado puntos de pañuelo [amount]. Puedes reclamar la recompensa hasta [amount] puntos más esta semana.
          - (otro)
      - [Choice]: Me gustaría reclamar una recompensa por mis puntos de pañuelo.
        - **Player:** Me gustaría reclamar una recompensa por mis puntos de pañuelo.
        - (Condition: Aún quedan puntos por reclamar:)
          - **Safe-cracking trainer:** ¡Claro! Veamos ahora...
          - Obtienes [amount] Thieving XP. Le quedan [amount] puntos y puede entregar hasta [amount] puntos más esta semana.
        - (Condition: Sin puntos de pañuelo por reclamar:)
          - **Safe-cracking trainer:** Lo sentimos, has reclamado tantos puntos de pañuelo esta semana como puedas en tu nivel.
      - [Choice]: Adiós por ahora.
        - **Player:** Adiós por ahora.
  - [Choice]: No me interesa, gracias.
    - **Player:** No me interesa, gracias.
    - **Safe-cracking trainer:** Si quieres, ejercita tus dedos sobre mis cajas fuertes falsas, aunque no hay nada en ellas más que pañuelos. Tengo que guardarlos en algún lugar.

#### Inspeccionar una caja fuerte antes de aprender a abrir cajas fuertes


##### Ante un gremio propio

- **Safe-cracking trainer:**Una vez que hayas contribuido más al gremio, te enseñaré cómo abrir estas intrincadas cajas fuertes.

##### Después de Un gremio propio, sin espacio en la mochila{{anchor|youllcomeacross}}

- **Safe-cracking trainer:** Necesitas algo de espacio libre en tu bolso, así que haz algo de espacio y hablemos sobre cómo abrir cajas fuertes una vez que hayas terminado.

##### Después de Un gremio propio, con espacio en backpack

- **Safe-cracking trainer:** Encontrarás cajas fuertes como la que tengo al lado en algunos lugares. A menudo contienen objetos de valor "portátiles" en su interior.
- **Safe-cracking trainer:** El defecto fatal de las cajas fuertes es que sus mecanismos de bloqueo son muy ruidosos.
- **Safe-cracking trainer:** Si escuchas, podrás oír cómo los vasos hacen clic cuando los colocas en el lugar correcto. Pero estoy seguro de que un ladrón de tu calibre los abrirá en poco tiempo.
- **Safe-cracking trainer:** Aunque, sin un estetoscopio, puede que le resulte más difícil escuchar el ruido de los tambores en cajas fuertes más complejas.
- **Safe-cracking trainer:** Mira, hay diferentes dificultades de seguridad que pondrán a prueba tus habilidades de ladrón en grados cada vez mayores.
- **Safe-cracking trainer:** ¿Tienes todo eso?
- **Player:** Creo que lo he resuelto.
- (receives=loot bag and stethoscope)
- El trainer te entrega una bolsa de botín y un estetoscopio.
- **Player:** ¿Para qué es la bolsa de botín?
- **Safe-cracking trainer:** Cuando saquees cajas fuertes, automáticamente deslizarás el contenido de la bolsa. Las bolsas de botín hacen que las cosas sean fáciles de transportar, menos sospechosas y están increíblemente de moda.
- **Safe-cracking trainer:** ¿Tienes más preguntas?
- [Menu]: ¿Qué te gustaría saber?{{anchor|cracksafe}}
  - [Choice]: ¿Hay alguna recompensa?
    - **Safe-cracking trainer:** ¿Aparte de entrenar tu prestidigitación y adquirir riqueza? Bueno, supongo que podrás ganar puntos Pilfer.
    - **Safe-cracking trainer:** Llena esa bolsa con cualquier cantidad de botín, luego llévala a Robin en la entrada y él la cercará para obtener Pilfer Points.
    - **Safe-cracking trainer:** Luego visita la tienda de Dodgy Derek para gastarlos en sus ofertas francamente sucias. Tiene algunos artículos dulces, como un amortiguador. Evitará que te sorprendas cuando te pillen robando de tus bolsillos.
    - (previous)
  - [Choice]: ¿Qué hago con los objetos que robo?
    - **Safe-cracking trainer:** ¡Ah, buena pregunta! El problema con los bienes robados es que al venderlos en tiendas generales, te cortarán los dedos, si los tribunales se muestran malos.
    - **Safe-cracking trainer:** Afortunadamente, en el Gremio de Ladrones ofrecemos nuestros servicios de esgrima. Has demostrado ser un gran ladrón, por lo que tienes acceso completo.
    - **Safe-cracking trainer:** Simplemente habla con Robin en la entrada y él solucionará tu problema de bienes robados. Aunque se llevará una parte. Literalmente, si no le gustas.
    - (previous)
  - [Choice]: ¿Sabes dónde puedo encontrar las cajas fuertes de alto nivel?
    - (Condition: Con 68 Thieving o menos:)
      - **Safe-cracking trainer:** Con tus habilidades, recomendaría buscar cajas fuertes en el Reino de Misthalin. Ya sabes: Lumbridge, Varrock.
      - (previous)
    - (Condition: Con 69 a 75 Thieving:)
      - **Safe-cracking trainer:** Con tus habilidades, recomendaría buscar cajas fuertes en Kharidian desert. Ya sabes: Al Kharid, Menaphos, Pollnivneach.
      - (previous)
    - (Condition: Con 76 a 82 Thieving:)
      - **Safe-cracking trainer:** Con tus habilidades, recomendaría buscar cajas fuertes en el Reino de Asgarnia. Ya sabes: Falador, Burthorpe, Rimmington.
      - (previous)
    - (Condition: Con 83 a 89 Thieving:)
      - **Safe-cracking trainer:** Con tus habilidades, recomendaría buscar cajas fuertes en el Reino de Kandarin. Ya sabes: Ardougne, Seers' Village, Catherby.
      - (previous)
    - (Condition: Con 90 Thieving o superior:)
      - **Safe-cracking trainer:** Con tus habilidades, recomendaría buscar en los confines más lejanos de Gielinor. Eres un ladrón increíble y las cajas fuertes más valiosas son las más difíciles de encontrar.
      - (previous)
  - [Choice]: Eso es todo, gracias.
    - **Player:** Adiós.

#### Inspeccionar una caja fuerte después de aprender a abrir cajas fuertes

- **Safe-cracking trainer:** Esta es una de esas cajas fuertes intrincadas de las que hablaba. Los encontrarás en todo Gielinor, algunos más difíciles de descifrar que otros.
- **Safe-cracking trainer:** Para descifrarlos de manera efectiva, querrás traer un estetoscopio. Esto le permitirá girar el dial más rápido, ya que podrá escuchar los clics.
- (Action: La caja fuerte parpadea momentáneamente en azul.)
- **Safe-cracking trainer:** Cuando el dial esté en la posición correcta, escuchará un clic. Ahora, si eres lo suficientemente rápido, puedes aplicar fuerza bruta a la cerradura: ¡haz clic en la caja fuerte para abrirla al instante!

#### Diálogo posterior

- **Safe-cracking trainer:** Hola. ¿Le puedo ayudar en algo?
- [Menu]: Elige una opción:
  - [Choice]: Sobre cómo abrir cajas fuertes...
    - (above|cracksafe)
  - [Choice]: cond=Having lost the loot bag|Perdí mi bolsa de botín.
    - (Condition: Sin espacio en backpack:)
      - **Safe-cracking trainer:** Necesitas algo de espacio libre en tu inventario o no puedo devolverte tu bolso.
    - (Condition: Con espacio en backpack:)
      - (receives=small, medium or large loot bag, depending on tier unlocked)
      - **Safe-cracking trainer:** Aquí tienes. Intenta no perder este.
  - [Choice]: Sobre esos pañuelos...
    - (above|hankies)
  - [Choice]: Nada.
    - **Player:** Adiós.
