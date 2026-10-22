# Easty

- **Original Wiki Page**: [Transcript:Easty](https://runescape.wiki/w/Transcript%3AEasty)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talking to Easty

- **Easty:** Hola Player, ¿cómo te va?
- **Seleccione una opción**
  - ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Easty:** Soy el asociado Easty. Acting Guildmaster Reiniger me asignó para ayudarte con el monolito.
    - **Easty:** Puedo conservar cualquier reliquia que hayas descubierto hasta que estés listo para ofrecerla al monolito. También estaré encantado de ayudarle con cualquier investigación de monolitos que descubramos.
    - (previous)
  - ¿Qué estás haciendo aquí?
    - **Player:** ¿Qué haces aquí?
    - **Easty:** ¡Vigilando el monolito, por supuesto!
    - **Easty:** Sin embargo, eres más que bienvenido a usarlo, Player. Me han informado de la extraña conexión que tienes con ello. Principalmente estoy aquí para mantener alejados a los otros arqueólogos, para mantenerlos a salvo. Sólo tú pareces tener una conexión con ello hasta ahora, así que debemos tener cuidado.
    - **Easty:** Aunque sea triste, igual tendrás que lanzarme algunas cronotas si quieres usarlas.
    - **Player:** ¿Por qué?
    - **Easty:** Necesitamos asegurarnos de que el gremio se mantenga a flote de alguna manera, ¿verdad? Además, no soy pasante.
    - (previous)
  - Pregunta sobre la gestión de reliquias.
    - **Seleccione una opción**
      - ¿Puedes contarme más sobre el monolito?
        - **Player:** ¿Puedes contarme más sobre el monolito?
        - **Easty:** Has tenido más conexión con ello que yo. No me atrevo a tocarlo, no después de lo que le pasó a Guildmaster Tony.
        - **Player:** ¿Qué le pasó a Tony?
        - **Easty:** ¡Ah, sí! Nadie lo sabe realmente, con seguridad. Siempre fue muy práctico, incluso como Guildmaster. Se encargó de investigar el monolito, solo, después de que se activó.
        - **Easty:** Entonces, un día, hubo una conmoción y lo único que quedó de Tony fue su viejo azadón, que guardamos bajo llave en su oficina para guardarlo.
        - **Player:** ¿Sabes cómo se activó el monolito?
        - **Easty:** ¡Ah, sí! Eso es algo más que no sabemos... Un día, era sólo un trozo de piedra latente al que ya nadie prestaba atención: hallazgos recientes más interesantes, ¿entiendes?
        - **Easty:** Luego, al día siguiente, nos despertamos y estaba increíblemente erguido, flotando, balanceándose y retorciéndose de la forma inquietante que está haciendo detrás de mí en este momento.
        - **Player:** ¿Hay algo que SÍ sepas?
        - **Easty:** ¡Ah! Bueno, lo que sí sabemos es que el monolito emitió una explosión de energía esa mañana después de que se abrió por primera vez. Hemos visto un montón de lo que llamamos duendes del tiempo volando alrededor de las excavaciones. Esos son los que nos llevaron a establecer cada uno de nuestros sitios de excavación.
        - **Easty:** Incluso rastreamos algunos duendes del tiempo que volaban en dirección a Anacronia, pero aún no han aterrizado allí. Tendrá que ver con la extraña distorsión del tiempo que ocurre allí, pero eventualmente deberían aterrizar.
        - **Easty:** Es casi como si el monolito tuviera interés en algunas reliquias muy específicas de nuestro pasado, como si estuviera enviando sondas. Reliquias como la que tú le ofreciste.
        - **Easty:** Si te topas con más reliquias en tu viaje para convertirte en un maestro arqueólogo, querrás asegurarte de traerlas aquí y ver si el monolito está interesado.
        - **Easty:** Creemos que es la única manera de descubrir qué es realmente esto... y, con suerte, recuperar a Tony también, mientras estamos en ello.
        - (previous)
      - ¿Puedes explicarme los poderes de las reliquias?
        - **Player:** ¿Puedes explicarme los poderes de las reliquias?
        - **Easty:** Por lo que podemos deducir, el monolito consume cada reliquia que se le ofrece, pero atrae la cualidad o esencia inherente de la reliquia como poderes.
        - **Easty:** Estos poderes se pueden aprovechar aprovechando la fuente de energía interna del monolito. Bueno, al menos puedes hacer eso. Nadie más.
        - **Easty:** El monolito parece tener un límite de energía que puede ejercer, y ciertos poderes requieren una mayor cantidad de su reserva de poder que otros.
        - **Easty:** Podría haber una manera de aprovechar más reservas del monolito, pero no estoy muy seguro. Tendremos que investigar un poco.
        - **Easty:** Al menos, eso es lo que me parece a mí, por lo que he visto hasta ahora.
        - (previous)
      - ¿Tienes alguna reliquia?
        - **Player:** ¿Tienes alguna reliquia?
        - ((If no relics have been lost:))
          - **Easty:** No por el momento, pero si pierdes alguna reliquia, ven a verme.
          - (previous)
        - ((If relics have been lost:))
          - (Condition: Without free backpack space:)
            - **Easty:** Necesitarás algo de espacio en tu backpack.
            - (previous)
          - (Condition: With free backpack space:)
            - (receives=lost relic)
            - Recibirás: [relic].
            - **Easty:** ¡Ahí estás!
            - (previous)
      - Pregunta por otra cosa.
        - (initial)
