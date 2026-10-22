# Laniakea

- **Original Wiki Page**: [Transcript:Laniakea](https://runescape.wiki/w/Transcript%3ALaniakea)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Journey to Anachronia

- (ver|Tutorial del campamento base de Anacronia)

### In the Anachronia base camp


#### Primera vez

- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Laniakea:** Mi nombre es Laniakea, es un placer conocerte.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Podemos hablar de asignaciones?
        - (abajo)
      - [Choice]: La puerta en la cima de las ruinas.
        - **Laniakea:** Encuéntrame en las ruinas del sureste y podemos hablar más.
      - [Choice]: Hablemos de ti.
        - (below|about-you)
  - [Choice]: La puerta en la cima de las ruinas.
    - (arriba)
  - [Choice]: Estoy aquí para discutir cualquier recompensa para la que pueda ser elegible.
    - {{transcript missing}}
  - [Choice]: Eh... nada...
    - **Player:** Eh... nada...

#### Tiempos posteriores


##### Con una parte de lanza salvaje en backpack

- [Menu]: Selecciona una opción
  - [Choice]: Pregúntale a Laniakea sobre cómo construir una lanza.
    - (continue|Using savage spear parts on her)
  - [Choice]: Pregunta por otra cosa.
    - (below|Otherwise)

##### De lo contrario

- [Menu]: Selecciona una opción
  - [Choice]: ¿Podemos hablar de asignaciones?
    - **Player:** Necesito otra tarea.
    - (Condition: Without meeting the requirements:)
      - **Laniakea:** Lo siento, pero no eres un cazador lo suficientemente bueno como para que yo te enseñe. Tu mejor trainer sería [slayer master] en [location].
      - Debes tener al menos el nivel 120 en Combate y el nivel 90 en Slayer para entrenar con este Slayer Master.
    - (Condition: If already on a normal assignment:)
      - **Laniakea:** Todavía estás cazando a [monster]; Vuelve cuando hayas terminado tu tarea.
    - (Condition: If already on Laniakea's special assignment:)
      - **Laniakea:** Aún debes completar mi desafío antes de que pueda asignarte otra tarea.
      - **Player:** ¿Qué querías que hiciera otra vez?
      - **Laniakea:** Me he quedado sin viales de veneno de las flores viles que hay por toda la isla. ¿Podrías recoger una gota de veneno de la lampenflora, las hepáticas, los ladrones luminosos y la trampa del diablo? Te recompensaré generosamente.
    - (Condition: If not on an assignment:)
      - {{anchor|regular}} (Condición: Obtener una tarea normal :)
        - (Condition: Slayer master cape perk is activated:)
          - [Laniakea nota tu capa y te invita a seleccionar tu propia tarea.]
          - (opens=Select your slayer task)
          - (continue|regular-assignment-amount)
        - (Condition: With a Slayer VIP ticket only:)
          - [Menu]: ¿Cambiar su tarea Slayer asignada?
            - [Choice]: [Amount] [monsters] (predeterminado)
              - (continue)
            - [Choice]: [Amount] [monsters] (cuesta 1 token Slayer)
              - (continue)
        - (Condition: Only the Slayer mask perk is available:)
          - [Menu]: ¿Cambiar su tarea Slayer asignada?
            - [Choice]: [Amount] [monsters] (predeterminado)
              - (continue)
            - [Choice]: [Amount] [monsters] (Máscara Slayer - Una vez al día)
              - (continue)
        - (Condition: With a Slayer VIP ticket and available Slayer mask perk:)
          - [Menu]: ¿Cambiar su tarea Slayer asignada?
            - [Choice]: [Amount] [monsters] (predeterminado)
              - (continue)
            - [Choice]: [Amount] [monsters] (cuesta 1 token Slayer)
              - (continue)
            - [Choice]: [Amount] [monsters] (Máscara Slayer - Una vez al día)
              - (continue)
        - {{anchor|regular-assignment-amount}} **Laniakea:** Lo estás haciendo bien, supongo. Tu nueva tarea es matar a [amount] [monsters].
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Tienes algún consejo para mí?
            - **Player:** ¿Tienes algún consejo para mí?
            - **Laniakea:** [Standard tip for the assigned monster]
            - [Segunda línea de la punta estándar.]
          - [Choice]: ¡Vale, genial!
            - **Laniakea:** ¡Buena suerte! No olvides regresar cuando requieras una nueva asignación.
          - [Choice]: No gracias. (Tarea clara, cuesta 30 puntos Slayer)
            - {{Transcript missing}}
      - (Condition: Getting the special assignment:)
        - **Laniakea:** ¿Te gustaría un desafío especial esta vez, en lugar de una tarea normal?
        - [Menu]: Selecciona una opción
          - [Choice]: Muy bien, acepto tu desafío.
            - {{Transcript missing}}
          - [Choice]: No, gracias. Preferiría una tarea normal.
            - **Player:** No, gracias. Preferiría una tarea normal.
            - (continuea|regular)
          - [Choice]: ¿Qué quieres decir?
            - **Laniakea:** Me he quedado sin viales de veneno de las flores viles que hay por toda la isla. ¿Podrías recoger una gota de veneno de la lampenflora, las hepáticas, los ladrones luminosos y la trampa del diablo? Te recompensaré generosamente.
            - [Menu]: Selecciona una opción
              - [Choice]: Muy bien, acepto tu desafío.
                - **Laniakea:** Muy bien.
              - [Choice]: No, gracias. Preferiría una tarea normal.
                - {{Transcript missing}}
          - [Choice]: No y por favor no me vuelvas a preguntar.
            - {{Transcript missing}}
  - [Choice]: La puerta en la cima de las ruinas.
    - (arriba)
  - [Choice]: cond=After Desperate Times|Kerapac.
    - **Player:** ¿Has visto alguna señal de Kerapac?
    - **Laniakea:** No lo he hecho. Aunque hay algunas ruinas por aquí que parecen haber sido perturbadas, es muy probable que todavía esté aquí o haya hecho algo aquí. Las que están abiertas conducen a una red subterránea, pero los derrumbes de las cuevas han provocado que los pasillos se bloqueen. Se necesitaría mucha energía para moverse entre los escombros y llegar hasta ellos.
    - **Player:** ¿O magia?
    - **Laniakea:** O magia, pero a menos que conozcas un ejército completo de magos que están disponibles para ayudarnos, no tendremos suerte. Nuestra mejor opción es esperar que algunas de las ruinas selladas alrededor de la isla nos den paso a lo que sea que esté debajo.
    - (Condition: If the player is at the base camp:)
      - (end)
    - (Condition: If the player is in the south-eastern ruins:)
      - **Laniakea:** Por ahora, estoy interesado en la puerta en la cima de las ruinas. Está sellado con un antiguo hechizo dragonante.
      - **Player:** ¿Sabes leer el idioma?
      - **Laniakea:** No diría que lo hablo con fluidez, pero he estudiado pergaminos que descubrí y aprendí un poco del idioma.
      - **Player:** ¿Qué dicen entonces las ruinas?
      - **Laniakea:** La mayoría de las runas sobre la puerta están gastadas, pero hay pocas que puedo distinguir.
      - **Laniakea:** Incluso con unos pocos, parece que no puedo entender lo que significan.
      - **Laniakea:** Aquí, esta palabra. Esto significa "Bloqueado".
      - **Laniakea:** Y algunos más aquí. 'Sacrificio', 'Pérdida' y 'Unidad'.
      - **Laniakea:** ¿Qué podría ser tan peligroso como para estar enterrado en capas y capas de roca y luego encerrado detrás de antiguos sellos?
      - **Player:** No planeas descubrirlo, ¿verdad?
      - **Laniakea:** ¿No tienes la más mínima curiosidad, Player?
      - **Player:** Ya sabes lo que dicen: la curiosidad mató al gato...
      - **Laniakea:** ...Pero la satisfacción me lo devolvió.
      - **Laniakea:** Debo saberlo.
      - **Laniakea:** Por lo que sé de los dragonantes y su maldición, no es de extrañar que Kerapac haya hecho todo lo posible por su pueblo.
      - **Laniakea:** En cierto sentido, es admirable.
      - **Player:** ¿Pero qué pasa con la traición que ha causado? Todo el dolor, el dolor y la muerte.
      - **Laniakea:** Lo estás viendo desde tu perspectiva. ¿A qué renunciarías y sacrificarías para salvar a los de tu propia especie?
      - **Laniakea:** ¿Te quedarías quieto y dejarías que la maldición nos consuma? Ni siquiera podemos empezar a imaginar lo que han pasado.
      - **Player:** ¿Está del lado de Kerapac?
      - **Laniakea:** No tomo partido y me compadezco de quienes lo hacen. Hay dos lados en cualquier historia o conflicto y cada lado siempre cree que tiene razón. Sí, los dragonantes han infligido innumerables terrores, pero solo han hecho lo que tenían que hacer para proteger y sobrevivir.
      - **Laniakea:** Esa es la naturaleza de todas las criaturas.
      - **Laniakea:** Supervivencia.
  - [Choice]: Hablemos de ti. {{anchor|about-you}}
    - [Menu]: Selecciona una opción
      - [Choice]: Cuéntame más sobre tus antecedentes.
        - **Laniakea:** Nací y crecí en un pueblo lejano al este, un lugar traicionero. Lleno de muerte y peligro.
        - **Laniakea:** Para sobrevivir no puedes quedarte de brazos cruzados y esperar que tu familia te mantenga.
        - **Laniakea:** No. Era matar o morir y mi gente fue criada como luchadora.
        - **Laniakea:** Pero a un gran coste. Debo vivir con las cosas que he hecho y visto.
        - **Laniakea:** Hacemos lo que debemos para sobrevivir.
        - **Laniakea:** Al final fue demasiado y decidí que sería mejor para mí dejar ese lugar.
        - **Laniakea:** Me aventuré a salir, pero aún siendo consciente de lo que había a mi alrededor y quién era una amenaza.
        - **Laniakea:** Es seguro decir que no tengo muchos amigos ni personas en quienes confío y siempre seguiré mi propia agenda.
        - **Player:** Es bueno saberlo...
        - **Laniakea:** No temas. He oído hablar de tus triunfos. Eres un alma buena.
        - **Player:** ¿Alguna vez has regresado a casa?
        - **Laniakea:** Nunca. Aunque he oído historias sobre un tesoro escondido allí; algo que consideré sólo un cuento para asustar a los niños del pueblo.
        - **Player:** ¿Qué es?
        - **Laniakea:** Eso no es conocimiento que siento la necesidad de compartir contigo. Lo que puedes saber es que es muy poderoso y si se aprovecha... bueno, quién sabe qué se puede lograr con él.
        - **Player:** ¿Dónde dijiste que habías vuelto a crecer?
        - **Laniakea:** Buen intento.
        - (previous)
      - [Choice]: ¿Cómo te convertiste en slayer master?
        - {{anchor|background}} **Laniakea:** Es curioso que lo preguntes, nunca fue mi intención convertirme en miembro de la Orden.
        - **Laniakea:** Me encontré con una reunión de la Orden mientras estaban rastreando una bestia que yo también estaba persiguiendo, por lo que se convirtió en una especie de competencia. Al menos lo convertí en eso. Quería ver si podía ser yo quien lo derribara.
        - **Laniakea:** Terminé matando a the beast ante sus propios ojos.
        - **Laniakea:** Al principio dudaban en aceptarme, pero yo también. No quería ser parte de la Orden. Realmente no tuve tiempo para ello, pero no pude rechazar todas las valiosas lecciones que me han enseñado a lo largo de los años.
        - **Laniakea:** Una parte de mí también quería un sentido de pertenencia. Como alguien que creció sin familia, la Orden rápidamente se convirtió en todo lo que quería y nunca tuve.
        - **Laniakea:** Aprendí más de Morvran y Kuradal. Kuradal y yo compartíamos muchas similitudes por lo que entrenábamos juntos con más frecuencia; pero a Morvran le gustaba entrenar solo como a mí.
        - **Laniakea:** Hubo otro...
        - **Laniakea:** No diría que lo amaba pero...
        - **Laniakea:** Algo conectado con él más profundamente de lo que podría haber imaginado y eso me hizo...
        - **Laniakea:** ...Eso me hizo sentir vulnerable. El sentimiento de deseo, lujuria y anhelo. Todavía no había sentido nada parecido antes y me eran ajenos.
        - **Laniakea:** Tuve que irme; crear mi propio camino.
        - **Player:** ¿Quién era y por qué dejaste eso atrás?
        - **Laniakea:** Preferiría no hablar de esto. Ya te he dicho demasiado.
        - (previous)
      - [Choice]: ¿Qué es este templo?
        - **Laniakea:** Este sitio parece ser más grandioso que todas las demás áreas alrededor de la isla, con la excepción de las ruinas al sureste.
        - (previous)
      - {{anchor|poison}} [Elección]: Cuéntame sobre tus venenos.
        - **Laniakea:** Veneno... ¿Por dónde empezar? Cómo una gota de líquido tan pequeña puede matar a un hombre de la manera más pacífica o causarle la muerte más dolorosa que puedas imaginar.
        - **Laniakea:** Como puedes ver, como alguien de la Orden de Slayer Masters, no tengo marcas y no tengo las cicatrices que ves en mis compañeros.
        - **Laniakea:** Tiendo a pelear un poco más limpio, se podría decir. Si bien puedo manejarme en el fragor del combate, prefiero infligir veneno a mi enemigo y dejar que él pelee.
        - **Player:** Eso me suena a pelear sucio.
        - **Laniakea:** Sólo hace falta un corte. Una vez infligida la herida puedo desaparecer en las sombras y dejar que el veneno haga su trabajo.
        - **Player:** ¿Cómo no te has cortado accidentalmente?
        - **Laniakea:** Durante mis años de estudiar diferentes venenos, consideré apropiado beber dosis de cada uno diariamente para desarrollar inmunidad. Ahora podría beber un frasco de los venenos más mortales y no sentir nada.
        - **Player:** ¿Podrías enseñarme cómo hacer estos venenos?
        - **Laniakea:** No lo haré.
          - (Condition: If the player has not completed Helping Laniakea:)
            - (ver|Ayudando a Laniakea (minimisión))
          - (Condition: If the player has completed Helping Laniakea:)
            - (previous)
      - {{anchor|doll}} [Elección]: Cuéntame sobre la muñeca que llevas en el cinturón.
        - **Player:** ¿Cuál es el muñeco que llevas sujeto al cinturón?
        - **Laniakea:** Un tipo extraño de magia... Esta muñeca puede estar ligada a un alma y cualquier daño que le haga a la muñeca también será infligido al portador de su marca. Si torciera el brazo de una manera antinatural, entonces el alma que une también sentirá ese dolor.
        - **Laniakea:** Aunque es magia oscura. Tan oscuro que ni siquiera yo me atrevo a entrometerme en él con demasiada frecuencia.
        - **Player:** ¿Entonces por qué lo llevas contigo?
        - **Laniakea:** Esté siempre preparado para las situaciones. Es mejor tenerlo y no necesitarlo, que necesitarlo y no tenerlo.
        - **Player:** Tienes razón.
        - **Player:** ¿Cómo puedo hacer uno?
        - **Laniakea:** No sé que puedas. Este es un artefacto de un aquelarre de brujas que una vez prosperó. Ya no están y con ellos, sus conocimientos.
        - (previous)
  - [Choice]: cond=If the special challenge is toggled off|¿Puedo volver a recibir asignaciones especiales de asesino?
    - **Laniakea:** Claro, ahora comenzaré a darte tareas especiales de cazador nuevamente.
  - [Choice]: Eh... nada...
    - **Player:** Eh... nada...

#### Usando partes de lanza salvaje en ella

- **Player:** ¿Sabes algo sobre estas piezas de lanza que encontré?
- ((With all parts in backpack:))
  - [Le muestras a Laniakea la punta de la lanza.]
  - **Laniakea:** Esta es una pieza bastante hermosa, es inquietantemente similar a la mía.
  - [Le muestras a Laniakea el asta de la lanza.]
  - **Laniakea:** Interesante, tiene mucho peso, me imagino que es difícil de usar con precisión.
  - [Le muestras a Laniakea la tapa de la lanza.]
  - **Laniakea:** Este parece ser the partner de la punta de lanza que me mostraste. Están claramente dispuestos a trabajar juntos.
  - [Le muestras a Laniakea el penacho.]
  - **Laniakea:** Este diseño es exquisito, sería un gran adorno para un arma.
  - **Laniakea:** Parece que has adquirido una lanza completa. ¿Me permitirás verlo con mayor detalle?
  - **Player:** Por supuesto.
  - [Le entregas las partes de la lanza a Laniakea.]
  - Laniakea examina cada una de las piezas por un breve momento.
  - **Laniakea:** Muy interesante. Creo que podría convertir esto en un arma similar a la mía. Si lo deseas?
  - [Menu]: ¿Montar la lanza de Laniakea?
    - [Choice]: Sí.
      - (removes=the savage spear tip, shaft, cap, and plume) (receives=Laniakea's spear)
      - [Laniakea te devuelve una lanza ensamblada.]
      - **Player:** ¡Guau! Gracias.
    - [Choice]: No.
      - **Laniakea:** Muy bien. Sabes dónde estoy si cambias de opinión.
- ((Without all parts in backpack:))
  - ((With the spear tip in backpack:))
    - [Le muestras a Laniakea la punta de la lanza.]
    - **Laniakea:** Esta es una pieza bastante hermosa, es inquietantemente similar a la mía.
    - (continue)
  - ((With the spear shaft in backpack:))
    - [Le muestras a Laniakea el asta de la lanza.]
    - **Laniakea:** Interesante, tiene mucho peso, me imagino que es difícil de usar con precisión.
    - (continue)
  - ((With the spear cap in backpack:))
    - [Le muestras a Laniakea la tapa de la lanza.]
    - (Condition: Without a spear tip in backpack:)
      - **Laniakea:** Extraño. Este es del mismo origen que el mío. No entiendo cómo un objeto así pudo llegar a existir en esta isla.
      - (continue)
    - (Condition: With a spear tip in backpack:)
      - **Laniakea:** Este parece ser the partner de la punta de lanza que me mostraste. Están claramente dispuestos a trabajar juntos.
      - (continue)
  - ((With the plume in backpack:))
    - [Le muestras a Laniakea el penacho.]
    - **Laniakea:** Este diseño es exquisito, sería un gran adorno para un arma.
    - **Laniakea:** Creo que alguna vez pudo haber estado atado a una lanza, muy parecida a la mía.
    - (continue)
  - ((With the spear tip and spear cap in backpack:))
    - Le muestras a Laniakea la punta de la lanza.
    - **Laniakea:** Esta es una pieza bastante hermosa, es inquietantemente similar a la mía.
    - Le muestras a Laniakea la tapa de la lanza.
    - **Laniakea:** Este parece ser the partner de la punta de lanza que me mostraste. Están claramente dispuestos a trabajar juntos.
    - (continue)
  - **Laniakea:** Si recuperas el resto de la lanza, tráemela. Me gustaría mucho verlo.

### At the southeastern ruins

- [Menu]: Selecciona una opción
  - [Choice]: ¿Podemos hablar de asignaciones?
    - (arriba)
  - [Choice]: La puerta en la cima de las ruinas.
    - (Condition: If the player has not completed Raksha, the Shadow Colossus:)
      - (ver|Raksha, the Shadow Colossus (misión))
    - (Condition: If the player has completed Raksha, the Shadow Colossus:)
      - **Laniakea:** No puedo entrar a ese lugar. Duele.
      - **Laniakea:** Debes ir solo Player.
  - [Choice]: Hablemos de ti.
    - [Menu]: Selecciona una opción
      - [Choice]: Cuéntame más sobre tus antecedentes.
        - (above|background)
      - [Choice]: ¿Cómo te convertiste en slayer master?
        - (above|slayer)
      - [Choice]: ¿Qué es este templo?
        - **Laniakea:** Este templo, cualquiera que sea el propósito arquitectónico original para el que fue construido, creo que se alza sobre algo de gran importancia.
        - **Laniakea:** Hay señales de ofrendas de sacrificio y señales de intentos de apertura en las puertas.
        - **Player:** ¿Has explorado alguno de los otros templos de la isla?
        - **Laniakea:** He visitado algunos, pero ninguno me habló tanto como este. Si bien estoy seguro de que hay secretos entre los demás que me interesa explorar, hay algo en este que no puedo identificar.
        - (previous)
      - [Choice]: Cuéntame sobre tus venenos.
        - (above|poison)
      - [Choice]: Háblame de la muñeca que llevas en el cinturón.
        - (above|doll)
  - [Choice]: cond=If the special challenge is toggled off|¿Puedo volver a recibir asignaciones especiales de asesino?
    - (arriba)
  - [Choice]: Eh... nada...
    - **Player:** Eh... nada...

### Activating the Enchanted gem

- {{Transcript missing}}

### Casting NPC contact

- (ver|NPC Contact#Laniakea)

### Assignment advice


#### Demonios abisales

- **Laniakea:** El último demonio abisal que maté encontré que los ataques cortantes los derribaron de manera efectiva.
- [Los demonios abisales son criaturas desagradables con las que lidiar. En realidad, no son parte de este reino y pueden moverse muy rápidamente para atrapar a sus presas. Se pueden encontrar en la Torre Canifis Slayer y en el Asilo Senntisten.]

#### mamuts de Acheron

- **Laniakea:** Los mamuts de Acheron son bestias honorables pero poderosas del norte helado. Cuando te cobren, ¡apártate del camino! Se pueden encontrar en un iceberg al que se puede acceder desde un muelle cerca de Rellekka.

#### Dragones inflexibles

- **Laniakea:** El último dragón Adamant que maté encontré que los hechizos de aire los derribaron de manera efectiva.
- [Los dragones inflexibles son incluso más peligrosos que los dragones de mithril. Búscalos en la mazmorra Brimhaven, debajo de una escalera al noroeste de los dragones de hierro y acero.]

#### Airut

- **Laniakea:** Los airut son criaturas agresivas de otro mundo. Tienen brazos poderosos y atacan con gran vigor. Sin embargo, ciertas habilidades pueden contrarrestarlos y aturdirlos.

#### Acuanitas

- **Laniakea:** Los acuanitas son criaturas anfibias que atraen a sus presas utilizando los señuelos brillantes que tienen en la cabeza. Atacan a oponentes más fuertes desde la distancia con magia de agua y no les agradan aquellos que rezan en contra de ella. Habitan en la mazmorra Fremennik Slayer, en una cámara más allá de los kurasks.

#### Fantasmas blindados

- **Laniakea:** El último fantasma blindado que maté encontré que los ataques aplastantes los derribaron de manera efectiva.
- [Puedes encontrar fantasmas blindados pululando dentro de las criptas al norte de Fort Forinthry. Su espíritu de odio sólo busca la violencia. Encontrarás que las armas aplastantes son efectivas para debilitar su capacidad de moverse.]

#### Aviación

- **Laniakea:** El último Aviansie que maté encontré que una ballesta con pernos los derribó de manera efectiva.
- Aviansie se puede encontrar en God Wars Dungeon al norte de Trollheim. Mientras vuelan, descubrirás que los ataques cuerpo a cuerpo no serán suficientes.

#### Demonios negros

- **Laniakea:** Los demonios negros son débiles ante los ataques a distancia. Sin embargo, siguen siendo el demonio más fuerte y muy peligroso. Búscalos en las mazmorras Edgeville o Brimhaven.

#### Dragones negros

- **Laniakea:** Los dragones negros se encuentran entre los dragones más fuertes y son muy feroces. Cuidado con su aliento de fuego. Estoy seguro de que los habrás visto en tus viajes y habrás perfeccionado tus técnicas con dragones menores.

#### guerreros Camel

- **Laniakea:** Los guerreros Camel pueden usar magias antiguas para atacarte. También cuentan con las bendiciones de Akthanakos y pueden crear espejismos poderosos y desorientadores.  Se pueden encontrar en lo profundo del desierto.

#### Dragones celestiales

- **Laniakea:** Los dragones celestiales son uno de los dragones más extraños que asigno. Usan cuerpo a cuerpo pero también tienen un poderoso ataque de fuego de dragón, así como una habilidad fascinante para detener el tiempo momentáneamente. Puedes encontrarlos en las profundidades de la isla Dragontooth.

#### Gigantes del caos

- **Laniakea:** Puedes encontrar gigantes del Caos en los túneles de Barendir, más allá de Keldagrim. Ten cuidado, ya que pueden lanzar su hacha arrojadiza Dragón a distancia o golpearte si te acercas. Quizás puedas recuperar algo.

#### Criaturas corruptas

- **Laniakea:** Puedes encontrar criaturas corruptas en la mazmorra Sophanem Slayer.

#### Criaturas de Daemonheim

- **Laniakea:** El último demonio Kal'gerion que maté encontré que muchos estilos de combate diferentes los derrotaron de manera efectiva.
- Puedes encontrar varias criaturas de las profundidades de Daemonheim acechando en los sumideros de Gielinor.

#### Criaturas de la arboleda perdida

- **Laniakea:** Puedes encontrar las criaturas de la arboleda perdida dentro de la arboleda perdida, al sur del páramo venenoso.

#### Autómatas de Cres

- **Laniakea:** Sin su maestro, los autómatas de Cres deambulan por las cámaras de Guthix atacando a cualquiera que entre. Están programados para usar magia, cuerpo a cuerpo o a distancia y pueden realizar un violento ataque de área de efecto. Se puede llegar a las cámaras de Guthix a través de su santuario o de la excavación al oeste de Legends' Guild.

#### Cambiaformas de cristal

- **Laniakea:** El último cambiaformas de cristal que maté encontré que los hechizos de fuego los derribaron de manera efectiva.
- Los cambiaformas de cristal son restos trastornados de los elfos de Tarddiad. Están bastante locos y, según Angof, más allá de la redención. Muéstrales misericordia poniendo fin a su sufrimiento.

#### Dagannot

- **Laniakea:** El último Dagannoth que maté encontré que los ataques cortantes los derribaron de manera efectiva.
- Los Dagannoth son criaturas marinas grandes que son muy agresivas. A menudo los encontrarás en cuevas cerca del agua de mar. No hay alegría tan grande como limpiar estos de the face de Gielinor.

#### Bestias oscuras

- **Laniakea:** Las bestias oscuras son depredadores grandes, parecidos a perros, con cuerpos enormemente musculosos que los protegen de las armas aplastantes. Encontramos algunos mientras minábamos los túneles Mourner, en busca del Templo de la Luz.

#### Demonios

- **Laniakea:** Puedes encontrar muchos tipos de demonios alrededor de Gielinor.

#### Dinosaurios

- **Laniakea:** En el último dinosaurio salvaje que maté, encontré que muchos estilos de combate diferentes los derrotaron de manera efectiva.
- [Puedes encontrar una variedad de dinosaurios en Anacronia.]

#### dragones

- **Laniakea:** Puedes encontrar cualquier tipo de Dragón alrededor de Gielinor.

#### Edimmu

- **Laniakea:** El último Edimmu que maté encontré que los ataques cortantes los derribaron de manera efectiva.
- [Edimmu son fantasmas que no lograron escapar de su cuerpo. Son fantasmas y zombis, pero de alguna manera completamente diferentes. Usan ataques a distancia y son muy agresivos. Puedes encontrarlos en una mazmorra de recursos a la que tiene acceso el clan Meilyr en Prifddinas.]

#### Elfos

- **Laniakea:** Los elfos son luchadores expertos en todas las disciplinas de los que puedes aprender mucho. Recomiendo desafiar sólo a un tipo de combatiente elfo a la vez.

#### Criaturas ganodermicas

- **Laniakea:** El último Ganodermic beast que maté descubrí que los hechizos de fuego los derribaron de manera efectiva.
- Las bestias ganodermicas y los enanos viven en las profundidades de una cueva al noreste de Mage Training Arena. Las criaturas de esa mazmorra están cubiertas de hongos tóxicos, por lo que debes luchar contra ellas desde la distancia. El hongo les ayuda a reparar el daño físico, por lo que quizás prefieras usar ataques mágicos.

#### Gárgolas

- **Laniakea:** Las gárgolas son criaturas aladas de piedra. Tendrás que luchar contra ellos hasta que estén al borde de la muerte antes de romperlos con un martillo de piedra. Se pueden encontrar en la Torre Canifis Slayer.

#### Dragones de piedras preciosas

- **Laniakea:** Puedes encontrar dragones de piedras preciosas debajo de la mina de gemas en Shilo Village.

#### Glaciares

- **Laniakea:** Lucien trajo los glacors a este mundo. Usan ataques mágicos, a distancia y cuerpo a cuerpo. Puedes encontrarlos en una caverna subterránea en Frozen Plateau.

#### Demonios mayores

- **Laniakea:** Los demonios mayores son débiles ante los ataques a distancia. Aunque no son los demonios más fuertes, siguen siendo peligrosos. Hay algunos en Brimhaven Dungeon.

#### Vermis de hielo

- **Laniakea:** Los más fríos de su tipo, se encuentran debajo de las montañas Fremennik. Como son seres de hielo, descubrí que los hechizos de fuego les infligen mucho más daño.

#### Dragones de hierro

- **Laniakea:** Los dragones de hierro son algunos de los dragones metálicos más débiles, con escamas de hierro que son mucho más gruesas que las armaduras de hierro normales. Su aliento de fuego y sus afiladas garras pueden anularse de diversas formas. Búscalos en Brimhaven Dungeon.

#### Demonios Kal'gerion

- **Laniakea:** Los demonios Kal'gerion son criaturas poderosas que usan tanto magia como cuerpo a cuerpo. Residen en una mazmorra de recursos cerca de Daemonheim. Te recomendaría que te cubrieras cuando rompan el suelo o cuando usen magia para atraerte hacia ellos.

#### Calfitos

- **Laniakea:** Los calfitos son insectos grandes que viven en colmenas bajo las arenas del desierto. Estoy seguro de que ya los habrás visto al suroeste del paso Shantay.

#### Vermis de lava

- **Laniakea:** El último Lava strykewyrm que maté encontré que muchos estilos de combate diferentes los derribaron de manera efectiva.
- [Los strykewyrms de lava son los más poderosos de su tipo. Atacan con todos los estilos de combate y son débiles o nada. Se pueden encontrar en lo profundo de Wilderness, por lo que yo te cuidaría las espaldas mientras los mato.]

#### Wyverns vivientes

- **Laniakea:** Los wyverns vivos respiran un veneno que te matará rápidamente a menos que te congeles. Pero cuidado; cuanto más frío tengas, más duro te golpearán sus ataques habituales.  Se pueden encontrar en la mazmorra de hielo de Asgarnia.

#### Dragones de mitril

- **Laniakea:** Los dragones de mitril son oponentes muy peligrosos. Hay algunos en la Caverna Antigua, al norte de donde encontrarás Kuradal. Eres un maestro de batalla: prueba tus habilidades.

#### Muspa

- **Laniakea:** Los muspah son criaturas nacidas de pesadillas. La magia antigua es lo más eficaz que se puede utilizar contra ellos. Puedes encontrarlos viajando a Freneskae. Serán agresivos a menos que uses tu fragmento de Zaros.

#### Jadinkos mutados

- **Laniakea:** Estas criaturas deformadas de enredadera de jade no dudarán en utilizar su entorno para ayudarles en el combate si no pueden tomar represalias de otra manera. Las crías de jadinkos son más fáciles de matar, pero los machos ofrecen las mayores recompensas. Las armas Ranged hechas de enredaderas son mejores contra ellos.

#### Criaturas de pesadilla

- **Laniakea:** Puedes encontrar criaturas de pesadilla en Freneskae, a las que se puede acceder a través de la puerta del mundo.

#### nihil

- **Laniakea:** Los sujetos supervivientes de los experimentos de Zaros. Tienen poderosos ataques cargados y luchan en grupos de cuatro. Puedes encontrarlos viajando a Freneskae. Serán agresivos a menos que uses tu fragmento de Zaros.

#### Dragonantes de Nodon

- **Laniakea:** Los dragonantes nodon son criaturas profundamente inteligentes, armadas con armamento de asedio avanzado. Sin embargo, son débiles ante las armas dragonbane. Puedes encontrarlos luchando por Jas en Senntisten.

#### Orden de ascensión de los miembros.

- **Laniakea:** La Orden de la Ascensión son usuarios de magia. Se recomienda encarecidamente utilizar ataques a distancia. Sus tácticas pueden hacerlos difíciles uno a uno, por lo que sería beneficioso traer a un amigo.

#### Demonios destripadores

- **Laniakea:** Los demonios destripadores se vuelven locos por el olor a sangre. Te golpearán más fuerte cuanto peores sean tus lesiones. Y cuidado; A veces pueden caer sobre ti desde arriba, lo cual es letal.  Se pueden encontrar en una fisura cerca de Al Kharid.

#### Dragones rúnicos

- **Laniakea:** El último dragón rúnico que maté encontré que muchos estilos de combate diferentes lo derrotaron de manera efectiva.
- Los dragones rúnicos son incluso más peligrosos que los dragones inflexibles. Te recomiendo que traigas munición dragonbane para perforar su armadura. Para encontrarlos, debes viajar a Kethsi a través de la Puerta del Mundo en Arandar.

#### Criaturas de las sombras

- **Laniakea:** Las sombras son criaturas ligeras que han sido corrompidas por el Señor Oscuro. Los Amlodd los convocan a su sección de la ciudad para derrotarlos y luego limpiar sus núcleos.

#### Devoradores de almas

- **Laniakea:** El último Crocodile akh que maté encontré que los hechizos de agua los derribaron de manera efectiva.
- Puedes encontrar devoradores de almas en la mazmorra Sophanem Slayer.

#### Criaturas acosadoras

- **Laniakea:** Puedes encontrar criaturas acosadoras dentro del escondite de Zamorak.

#### Dragones de acero

- **Laniakea:** Los dragones de acero son peligrosos y metálicos, con escamas de acero que son mucho más gruesas que las armaduras de acero normales. Búscalos en Brimhaven Dungeon.

#### Strykewyrms

- **Laniakea:** Puedes encontrar strykewyrms de la jungla en junglas, strykewyrms de hielo en ambientes helados y strykewyrms de lava en ambientes cálidos.

#### Demonios atormentados

- **Laniakea:** Los demonios atormentados son criaturas poderosas que usan ataques mágicos, a distancia y cuerpo a cuerpo. También tienen la capacidad de protegerse. Puedes encontrarlos debajo de la cueva Lágrimas de Guthix.

#### No-muertos

- **Laniakea:** El último esqueleto atado que maté encontré que los hechizos de tierra los derribaron de manera efectiva.
- Puedes encontrar muchos tipos de muertos vivientes alrededor de Gielinor, en particular los que se pudren dentro de las criptas al norte de Fort Forinthry.

#### Flores viles

- **Laniakea:** La última Lampenflora que maté encontré que los hechizos de fuego los derribaron de manera efectiva.
- Puedes encontrar una variedad de flores viles en Anacronia.

#### Vyrewatch

- **Laniakea:** Estas repugnantes criaturas se pueden encontrar en Meiyerditch y Darkmeyer en Morytania. Tienen una habilidad telepática que les permite esquivar los ataques entrantes, por lo que necesitarás un arma especialmente creada para dañarlos.

#### Fantasmas blindados

- **Laniakea:** Puedes encontrar fantasmas blindados pululando dentro de las criptas al norte de Fort Forinthry. Sus espíritus odiosos sólo buscan la violencia. Encontrarás que las armas aplastantes son efectivas para debilitar su capacidad de moverse.

#### Fantasmas resucitados

- **Laniakea:** Estos espíritus torturados han sido resucitados de entre los muertos por Zemouregal y están sujetos a su voluntad. Puedes encontrar fantasmas resucitados que habitan en las profundidades de las criptas al norte de Fort Forinthry, esperando la orden de Zemouregal. Encontrarás arcos efectivos contra este objetivo.
