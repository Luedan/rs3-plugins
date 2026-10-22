# Morvran

- **Original Wiki Page**: [Transcript:Morvran](https://runescape.wiki/w/Transcript%3AMorvran)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Missing dialogue for met requirements and Rush of Blood}}
{{ToC|limit=1}}

### In Prifddinas, after Plague's End

- **Morvran:** ¿Qué quieres?
- [Menu]: Seleccione una opción|hablar con
  - [Choice]: ¿Podemos hablar de asignaciones?
    - **Player:** ¿Podemos hablar de asignaciones?
    - **Morvran:** Supongo que podemos. ¿Qué quieres preguntar?
    - [Menu]: Elige una opción:
      - [Choice]: cond=If the player is already on special challenge assignment:|Sobre tu desafío...
        - **Player:** Acerca de tu desafío...
        - **Morvran:** Mmmm. A ver cómo vas progresando.
        - Debes matar a los siguientes jefes mientras llevas todos los cristales oscuros acumulados: Topo gigante (modo difícil), Kalphite Queen, Dagannoth Kings, King Black Dragon, Queen Black Dragon, Kree'arra, Commander Zilyana, K'ril Tsutsaroth, General Graador y Araxxi.
        - Si deseas admitir la derrota, dímelo ahora y te liberaré.
        - Y viendo lo amable que soy, ni siquiera habrá penalización, sólo la vergüenza que supone rendirse tan fácilmente.
          - **Player:** 1. Sí, cancelar.
            - **Morvran:** Ya está. Eres libre de solicitarme otra tarea... una vez que te sientas capaz de hacerlo.
            - (Salir del diálogo.)
          - **Player:** 2. No, guárdalo.
            - (Salir del diálogo.)
      - [Choice]: Necesito otra tarea.
        - **Player:** Necesito otra tarea.
        - (Condition: If the player does not have the required skill levels:)
          - **Morvran:** Lo siento, pero no eres lo suficientemente fuerte para que yo te enseñe. Hazte más fuerte. Tu mejor trainer sería [slayer master] en [location].
          - Debes tener al menos el nivel 120 en Combate y el nivel 85 en Slayer para entrenar con este Slayer Master.
        - (Condition: If currently on a new Slayer assignment:)
          - **Morvran:** Ya estás en una tarea perfectamente buena. ¿Qué más quieres?
        - (Condition: If currently on a used Slayer assignment:)
          - **Morvran:** Todavía estás cazando a [assigned monster]; Vuelve cuando hayas terminado tu tarea.
          - (Salir del diálogo.)
        - (Condition: If currently on Morvran's Slayer challenge:)
          - **Morvran:** Aún debes completar mi desafío antes de que pueda asignarte otra tarea.
          - **Player:** ¿Qué querías que hiciera otra vez?
          - **Morvran:** Necesito que reúnas diez cristales oscuros de varios monstruos famosos. Para que su corrupción se muestre, debes hacerlo solo.
        - (Condition: If not currently on an assignment and first time challenge:)
          - **Morvran:** ¿Te gustaría un desafío especial esta vez, en lugar de una tarea normal?
            - Muy bien, acepto tu desafío.
              - **Morvran:** Muy bien.
              - {{Transcript missing}}
            - No gracias. Preferiría una tarea regular.
              - {{Transcript missing}}
            - ¿Qué quieres decir?
              - {{Transcript missing}}
            - No y por favor no me vuelvas a preguntar.
              - {{Transcript missing}}
      - [Choice]: cond=If not first time challenge task:|¿Tienes alguna tarea especial para mí?
        - (Condition: If already on Slayer assignment:)
          - **Morvran:** Ya estás en una tarea perfectamente buena. ¿Qué más quieres?
            - *(Vuelve a las opciones anteriores.)*
        - (Condition: If already on Morvran's Slayer challenge:)
          - **Morvran:** Ya estás haciendo un desafío especial para mí. ¿Qué más quieres?
            - *(Vuelve a las opciones iniciales)*
        - (Condition: If not on Slayer asssignment:)
          - **Player:** ¿Tienes alguna tarea especial para mí?
          - **Morvran:** Tengo un desafío especial que he estado reservando para estudiantes más capaces... pero tal vez podrías usar algunos de tus puntos de cazador para persuadirme.
          - He oído decir que algunos pequeños fragmentos de Seren han llegado a zonas de gran conflicto.  Temo que este conflicto pueda corromper esos fragmentos.
          - Me gustaría que los recuperaras para que el Clan Hefin pueda limpiarlos adecuadamente.
          - **Player:** ¿Qué quieres decir con gran conflicto?
          - **Morvran:** Están en medio de algunos de los llamados monstruos "famosos".  Deseo que los mates, recuperes estos fragmentos y me los devuelvas.
          - Las bestias en cuestión son el topo gigante de Falador, el Kalphite Queen, el Rey y la Reina Black Dragons, los tres Reyes Dagannoth, los cuatro generales de God Wars Dungeon y, finalmente, Araxxi.
          - Sin embargo, esto no será tan simple como parece.  Estos fragmentos se habrán corrompido por tanto derramamiento de sangre cercano y probablemente te causarán efectos negativos.
          - Y necesitas llevar todos estos "cristales oscuros" que encuentres para poder sacar más.
          - Puedes aceptar este desafío ahora mismo a cambio de 100 puntos de cazador.  O podría darte una tarea regular.  Tu decides.
          - **Player:**
            - 1. Acepto tu desafío (100 puntos de cazadora)
            - 2. En lugar de eso, quiero una tarea regular.
            - 3. Necesito algo de tiempo para pensar en esto.
              - *(Vuelve a las opciones anteriores a anteriores)*
  - [Choice]: ¿Podemos hablar de artículos e incentivos?
    - **Player:** ¿Podemos hablar de artículos e incentivos?
    - **Morvran:** Bueno, ¿cuál es? ¿Artículos en venta o incentivos?
    - Hablemos de elementos.
      - **Morvran:** Tengo mucho equipo de cazadora. Échale un vistazo.
        - *(Se abre la interfaz del equipo Slayer)*
    - Hablemos de incentivos.
      - Ver recompensas
        - *(Se abre la interfaz de recompensas Slayer)*
      - ¿Cómo gano puntos cooperativos para gastarlos en recompensas?
        - **Morvran:** Obtendrás puntos cooperativos si completas al menos la mitad de tu contribución a una tarea con un amigo. Eso significa que debes estar en un grupo la mayor parte del tiempo que estás trabajando en tu tarea, ¡pero no importa si tu amigo te gana en la mayoría de las muertes! Aún habrás estado en un grupo durante la mayor parte de tu contribución, por lo que aún tendrás derecho a un punto de recompensa cooperativa.
          - Ver recompensas
            - *(Se abre la interfaz de recompensas Slayer)*
          - ¿Dónde puedo usar las recompensas cooperativas de comida y pociones?
            - *(Igual que a continuación)*
          - Eso es todo, gracias.
      - ¿Dónde puedo usar las recompensas cooperativas de comida y pociones?
        - **Morvran:** Las recompensas se pueden usar en la mayoría de las áreas que comúnmente te enviamos para completar tus tareas.
          - Ver recompensas
            - *(Se abre la interfaz de recompensas Slayer)*
          - ¿Cómo gano puntos cooperativos para gastarlos en recompensas?
            - *(Igual que arriba)*
          - Eso es todo, gracias.
    - ¿Tienes alguna otra recompensa?
      - **Player:** ¿Tienes otras recompensas?
      - **Morvran:** Para mis estudiantes más capaces, tengo un desafío especial que ofrezco, y hay algunas pequeñas recompensas, además de la gloria, que ofrezco por completarlo. Cada vez que completes el desafío, pagaré por una nueva sintonización gratuita de los portales del Gremio Max, aunque no pagaré más de 30 por adelantado. También te permitiré llevar cristales negros especiales que tienen un efecto debilitante sobre ti, para que tu asesinato sea más desafiante.
        - ¿Qué son los cristales negros?
          - **Player:** ¿Qué son los cristales negros?
          - **Morvran:** Los cristales negros son cristales corruptos que han resistido nuestros intentos de limpiarlos. La corrupción es demasiado fuerte. Al igual que los cristales oscuros, cuando se transportan tienen efectos debilitantes. Algunos de mis alumnos más valientes han empezado a llevar algunos para que su asesinato sea más desafiante. Permito que las personas los lleven solo si han demostrado su valía al completar mi desafío.
          - **Player:** ¿Tiene algún beneficio llevarlos?
          - **Morvran:** No hay recompensa material. Pero ¡la gloria! ¡El desafío! ¿No son estos lo suficientemente buenos para ti?
            - *(Vuelve a las opciones anteriores a anteriores)*
        - Habla de otra cosa.
          - *(Vuelve a las opciones anteriores a anteriores)*
  - [Choice]: Hablemos de ti.
    - **Player:** Hablemos de ti.
    - **Morvran:** Mi tema favorito. ¿Qué quieres saber?
    - [Menu]: Selecciona una opción
      - [Choice]: Cuéntame más sobre tus antecedentes.
        - **Player:** Cuéntame más sobre tus antecedentes.
        - **Morvran:** Soy el sobrino de Lord Iorwerth. El viejo Lord Iorwerth, claro está. Me criaron como líder de nuestro clan. Admiraba a mi tío; Fue él quien me nombró Jefe de Inteligencia de nuestro clan.
        - **Morvran:** Era mi deber acumular conocimientos sobre nuestros enemigos (sus fortalezas y debilidades) y la mejor manera de derrotarlos.
        - **Morvran:** También estuve a cargo de interrogatorios y asesinatos.
        - **Player:** ¿Cómo te convertiste en slayer master?
        - **Morvran:** Mis deberes me dieron motivo para viajar mucho más allá de las fronteras de Tirannwn, aunque siempre disfrazado, por supuesto.
        - **Morvran:** En mis viajes, conocí a una encantadora joven llamada Kuradal.
        - **Morvran:** Ella me enseñó mucho sobre el mundo en general, y yo le aprendí sobre los muchos misterios de este mundo cerrado para ella.
        - **Morvran:** Es una mujer extraordinaria. Me sentí fascinado por ella y lo que hace, y por eso decidí dedicar mis talentos y conocimientos a la matanza.
        - **Morvran:** Tenemos que encontrar nuestro lugar nuevamente entre los otros clanes. Algunos de nosotros todavía lamentamos cómo se desarrollaron las cosas, pero tengo la intención de aceptar este cambio.
        - **Morvran:** Mi propio conocimiento sobre matar ahora ha superado incluso el de Kuradal... teóricamente hablando, por supuesto. Ella es más adecuada para aplicaciones prácticas...
        - **Player:** ¿Solo en teoría?
        - **Morvran:** Oh, podría matar fácilmente a cualquier bestia si así lo deseara. Ciertamente he hecho mucho en mi tiempo... pero siempre hay otros dispuestos a hacer el trabajo sucio. Prefiero mirar estos días, estudiar y aprender.
        - **Morvran:** A pesar de lo que puedas pensar de Iorwerth, creo que ya se ha derramado suficiente sangre durante la guerra civil. Siempre he preferido matar sólo cuando sea absolutamente necesario.
        - (initial|talkto)
      - [Choice]: Acerca del clan Iorwerth...
        - **Player:** Acerca del Clan Iorwerth...
        - **Morvran:** Mira, nunca fui fanático de todo ese asunto del Señor Oscuro. Tengo mis propios intereses y todavía puedo satisfacerlos.
        - **Morvran:** Pero como Iorwerth, tengo un deber para con mi señor. Nos tomamos el deber en serio, algo que a los demás clanes les preocupa menos.
        - **Player:** ¿Entonces solo estabas siguiendo órdenes? Como si eso fuera una justificación.
        - **Morvran:** No puedo hablar por las acciones de los demás, pero siempre me aseguré de que mis propias acciones (mis órdenes) fueran justas.
        - **Morvran:** Dentro de cualquier guerra, cada individuo debe trazar sus propias líneas. Puedo mantener la cabeza en alto sabiendo que me mantuve fiel a mis creencias.
        - **Player:** ¿No eras asesino e interrogador?
        - **Morvran:** Las guerras requieren ambos. Todos mis objetivos eran de valor militar, nunca civiles o inocentes, y nunca recurrí al uso de la tortura.
        - **Morvran:** Nuevamente, solo puedo ser responsable de mis propias acciones, no de las de los demás.
        - **Player:** ¿Crees que una masacre es justificable?
        - **Morvran:** No, por supuesto que no, y me alegra que hayas puesto fin a esto.
        - **Morvran:** No pintes todo Iorwerth con el mismo pincel simplemente por las acciones de mi tío. Se equivocó, eso está claro, y ahora debemos encontrar la manera de vivir una vez más entre nuestros hermanos.
        - **Morvran:** Se necesita alguien como yo para garantizar la seguridad de todos los clanes, el Clan Iorwerth necesita un líder con una perspectiva más... agradable.
        - **Morvran:** Es por eso que he renunciado a mi derecho de señorío sobre Lestin. Es una elección poco convencional, pero necesaria.
        - **Morvran:** Algunos de los más antiguos y acérrimos de Iorwerth están teniendo dificultades para aceptarlo, pero los mantendré a raya. Me respetan y mientras yo apoye a Iestin, seguirán su ejemplo o no serán bienvenidos aquí.
          - (initial|talkto)
      - [Choice]: Entonces, ¿qué hay en esta mazmorra?
        - **Player:** Entonces, ¿qué hay en esta mazmorra?
        - **Morvran:** Desde que Prifddinas volvió a crecer, le he encargado al encantador Kuradal que me proporcione criaturas para mi... colección.
        - **Player:** ¿Con qué fin?
        - **Morvran:** ¡Un desafío, pero solo para los cazadores más selectos!
        - **Player:** ¿Puedo entrar ahí?
        - (Condition: If you do not yet have the required skill levels:)
          - **Morvran:** No. No eres digno de mi tiempo.
          - Necesitas 85 Slayer para acceder a la arena de Morvran.
        - (Condition: Otherwise:)
          - **Morvran:** Sí. Disfrutaré viéndote pelear... pero no me aburras o podría reconsiderarlo.
          - **Player:** Entonces, ¿cuál es el desafío?
          - **Morvran:** Te arrojaré una serie de criaturas en cada ronda; Tienes diez minutos para completar tantas rondas como puedas.
          - **Morvran:** Cuantas más rondas completes en el tiempo indicado, mayor será tu recompensa.
          - **Player:** ¿Qué criaturas?
          - **Morvran:** Podrían ser cualquiera que de otro modo te asignaría, incluso aquellos que hayas decidido bloquear. Después de todo, se supone que es un desafío.
          - **Player:** ¿Entonces debería estar preparado para casi cualquier cosa?
          - **Morvran:** Puedes acceder a un cofre del banco allí abajo y comprar equipo de cazador si olvidaste algo.
          - **Morvran:** Pero hacerlo durante el desafío te costará tiempo, por lo que es mejor estar bien preparado antes de comenzar.
          - **Player:** ¿Qué pasa si muero?
          - **Morvran:** Entonces mueres.
        - **Morvran:** ¿Eso es todo?
        - (initial|talkto)
  - [Choice]: ¿Puedo usar tu mazmorra?
    - **Player:** ¿Puedo usar tu mazmorra?
    - (Condition: Without having the required skill levels:)
      - **Morvran:** No lo creo. No tienes la habilidad suficiente para entrar a mi mazmorra.
      - Necesitas 85 Slayer para ingresar a la arena Rush of Blood de Morvran.
    - (Condition: Having already completed the challenge this week:)
      - {{Transcript missing}}
    - (Condition: Otherwise:)
      - **Morvran:** No has intentado mi desafío en lo que va de esta semana. Estaré observando esta vez, así que prepárate para impresionarme.
      - **Morvran:** ¿A menos que prefieras hacer solo una "prueba" por ahora?
      - [Menu]: ¿Realizar una recompensa o una prueba?
        - [Choice]: Carrera de recompensa.
          - **Morvran:** ¿Qué desafío te gustaría intentar? Recuerde que esta es una carrera de recompensa, ¡así que haga lo mejor que pueda!
          - (continue)
        - [Choice]: Ejecución de prueba.
          - **Morvran:** ¿Qué desafío te gustaría intentar? Recuerde que esto es sólo una prueba.
          - (continue)
      - [Menu]: ¿Qué nivel de desafío te gustaría?
        - [Choice]: Bronce (85 Slayer).
          - (Condition: If the option is struck through:)
            - **Morvran:** Aún no eres elegible para el desafío Bronce.
            - **Morvran:** Necesito saber que puedes matar a vampyres primero.
            - Para intentar el desafío Bronce se requieren 85 Slayer y completar la misión Legacy of Seergaze.
            - (previous)
          - (Condition: If the option is not struck through:)
            - {{Tmissing}}
        - [Choice]: Plata (90 Slayer).
          - (Condition: If the option is struck through:)
            - **Morvran:** Aún no eres elegible para el desafío Plata.
            - Para intentar el desafío Plata se requieren 90 Slayer y completar la misión Legacy of Seergaze.
            - (previous)
          - (Condition: If the option is not struck through:)
            - {{Tmissing}}
        - [Choice]: Oro (95 Slayer).
          - (Condition: If the option is struck through:)
            - **Morvran:** Aún no eres elegible para el desafío Gold.
            - **Morvran:** Primero necesito saber que eres un cazador experimentado de vyres, dagannoth y TokHaar.
            - Para intentar el desafío Gold se requieren 95 Slayer, 90 Dungeoneering y completar las misiones Blood Runs Deep, Branches of Darkmeyer, Ritual of the Mahjarrat, The Chosen Commander, The Elder Kiln, The Firemaker's Curse y The Void Stares Back.
            - (previous)
          - (Condition: If the option is not struck through:)
            - {{Tmissing}}
        - [Choice]: Platino (99 Slayer).
          - (Condition: If the option is struck through:)
            - **Morvran:** Aún no eres elegible para el desafío Platino.
            - **Morvran:** Necesito saber que primero puedes encargarte de algunas de las criaturas asesinas más duras que existen.
            - Para intentar el desafío Platnium se requieren 99 Slayer, 90 Dungeoneering y completar Branches of Darkmeyer, Fate of the Gods, One of a Kind, Ritual of the Mahjarrat, The Chosen Commander, The Firemaker's Curse, The Void Stares Back, The World Wakes y While Guthix Sleeps.
            - misiones.
            - (previous)
          - (Condition: If the option is not struck through:)
            - {{Tmissing}}
        - [Choice]: ¿Cuál es la diferencia?
            - **Morvran:** ¿Cuál es la diferencia? ¿Cuál crees que sería la diferencia? Se vuelven más difíciles, obviamente.
            - **Morvran:** Todos los monstruos a los que te enfrentarás en mi mazmorra son aquellos que de otro modo te encargaría matar.
            - **Morvran:** Cuanto mayor sea el nivel del desafío que intentes, más difíciles serán las criaturas a las que posiblemente te enfrentes.
            - **Morvran:** Pero luego, con mayor peligro viene la oportunidad de impresionarme y una mayor recompensa si lo haces bien.
            - (previous)
  - [Choice]: Eh... nada...
    - **Player:** Eh... nada...

### Activating the enchanted gem


#### Si Morvran es tu Slayer Master actual

- **Morvran:**  Hola, Player, ¿en qué puedo ayudarte?
  - ¿Cómo estoy hasta ahora?
    - **Player:** ¿Cómo me va hasta ahora?
    - **Morvran:**  Actualmente estás asignado para matar a [assigned creatures]; sólo faltan X más.
      - ¿Quién eres?
        - *(Igual que a continuación)*
      - ¿Dónde estás?
        - *(Igual que a continuación)*
      - ¿Tienes algún consejo para mí?
        - *(Igual que a continuación)*
      - Eso es todo gracias.
        - **Player:** Eso es todo, gracias.
  - ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Morvran:**  Mi nombre es Morvran; Soy un Slayer Master.
      - ¿Cómo estoy hasta ahora?
        - *(Igual que arriba)*
      - ¿Dónde estás?
        - *(Igual que a continuación)*
      - ¿Tienes algún consejo para mí?
        - *(Igual que a continuación)*
      - Eso es todo gracias.
        - *(Igual que arriba)*
  - ¿Dónde estás?
    - **Player:** ¿Dónde estás?
    - **Morvran:**  Me encontrarás en Prifddinas. Estaré aquí cuando necesites una nueva tarea.
      - ¿Cómo estoy hasta ahora?
        - *(Igual que arriba)*
      - ¿Quién eres?
        - *(Igual que arriba)*
      - ¿Tienes algún consejo para mí?
        - *(Igual que a continuación)*
      - Eso es todo gracias.
  - ¿Tienes algún consejo para mí?
    - **Player:** ¿Tienes algún consejo para mí?
    - **Morvran:**  El último [assigned creature] que maté descubrí que [weapons] los derribó de manera efectiva.
    - [sugerencia de tarea]
      - ¿Cómo estoy hasta ahora?
        - *(Igual que arriba)*
      - ¿Quién eres?
        - *(Igual que arriba)*
      - ¿Dónde estás?
        - *(Igual que arriba)*
      - Eso es todo gracias.
        - *(Igual que arriba)*
  - Nada realmente.
    - **Player:**  En realidad, nada.

### NPC Contact

- **Player:** ¿Hola?
- **Morvran:** No tienes nada que hacer en mi cabeza. Mis secretos no son para tus ojos. Salir.
- **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo.
- **Morvran:** Tienes demasiado miedo para buscarme en persona, ¿eh? Bueno, ¿qué es?
- Seleccione una opción
  - Necesito otra tarea.
    - *(Igual que 'Necesito otra tarea' arriba)*
  - Eh... nada.
    - **Player:** Eh... nada...

### Assignment advice


#### Demonios abisales

**Morvran:** Los demonios abisales son criaturas desagradables con las que lidiar. En realidad, no son parte de este reino y pueden moverse muy rápidamente para atrapar a sus presas. Se pueden encontrar en la Torre Canifis Slayer y en el Asilo Senntisten.

#### mamuts de Acheron

**Morvran:** Los mamuts de Acheron son bestias honorables pero poderosas del norte helado. Cuando te cobren, ¡apártate del camino! Se pueden encontrar en un iceberg al que se puede acceder desde un muelle cerca de Rellekka.

#### Dragones inflexibles

**Morvran:** Los dragones Adamant son incluso más peligrosos que los dragones de mithril. Búscalos en la mazmorra Brimhaven, debajo de una escalera al noroeste de los dragones de hierro y acero.

#### Airut

**Morvran:** Los airut son criaturas agresivas de otro mundo. Tienen brazos poderosos y atacan con gran vigor. Sin embargo, ciertas habilidades pueden contrarrestarlos y aturdirlos.

#### Acuanitas

**Morvran:** Los acuanitas son criaturas anfibias que atraen a sus presas utilizando los señuelos brillantes que tienen en la cabeza. Atacan a oponentes más fuertes desde la distancia con magia de agua y no les agradan aquellos que rezan en contra de ella. Habitan en la mazmorra Fremennik Slayer, en una cámara más allá de los kurasks.

#### Orden de ascensión de los miembros.

**Morvran:** La Orden de la Ascensión son usuarios de magia. Se recomienda encarecidamente utilizar ataques a distancia. Sus tácticas pueden hacerlos difíciles uno a uno, por lo que sería beneficioso traer a un amigo.

#### Aviación

**Morvran:** Aviansie se puede encontrar en God Wars Dungeon al norte de Trollheim. Mientras vuelan, descubrirás que los ataques cuerpo a cuerpo no serán suficientes.

#### Demonios negros

**Morvran:** Los demonios negros son débiles ante los ataques a distancia. Sin embargo, siguen siendo el demonio más fuerte y muy peligroso. Búscalos en las mazmorras Edgeville o Brimhaven.

#### Dragones negros

**Morvran:** Los dragones negros se encuentran entre los dragones más fuertes y son muy feroces. Cuidado con su aliento de fuego. Estoy seguro de que los habrás visto en tus viajes y habrás perfeccionado tus técnicas con dragones menores.

#### guerreros Camel

**Morvran:** Los guerreros Camel pueden usar magia antigua para atacarte. También cuentan con las bendiciones de Akthanakos y pueden crear espejismos poderosos y desorientadores.  Se pueden encontrar en lo profundo del desierto.

#### Dragones celestiales

**Morvran:** Los dragones celestiales son uno de los dragones más extraños que asigno. Usan cuerpo a cuerpo pero también tienen un poderoso ataque de fuego de dragón, así como una habilidad fascinante para detener el tiempo momentáneamente. Puedes encontrarlos en las profundidades de la isla Dragontooth.

#### Gigantes del caos

**Morvran:** Puedes encontrar gigantes del Caos en los túneles de Barendir, más allá de Keldagrim. Ten cuidado, ya que pueden lanzar su hacha arrojadiza Dragón a distancia o golpearte si te acercas. Quizás puedas recuperar algo.

#### Criaturas corruptas

**Morvran:** Puedes encontrar criaturas corruptas en la mazmorra Sophanem Slayer.

#### Criaturas de la arboleda perdida

**Morvran:** Puedes encontrar las criaturas de la arboleda perdida dentro de la arboleda perdida, al sur del páramo venenoso.

#### Autómatas de Cres

**Morvran:** Sin su maestro, los autómatas de Cres deambulan por las cámaras de Guthix atacando a cualquiera que entre. Están programados para usar magia, cuerpo a cuerpo o a distancia y pueden realizar un violento ataque de área de efecto. Se puede llegar a las cámaras de Guthix a través de su santuario o de la excavación al oeste de Legends' Guild.

#### Cambiaformas de cristal

**Morvran:** Los cambiaformas de cristal son restos trastornados de los elfos de Tarddiad. Están bastante locos y, según Angof, no tienen redención. Muéstrales misericordia poniendo fin a su sufrimiento.

#### Dagannot

**Morvran:** Los Dagannoth son criaturas marinas grandes que son muy agresivas. A menudo los encontrarás en cuevas cerca del agua de mar. No hay alegría tan grande como limpiar estos de the face de Gielinor.

#### Bestias oscuras

**Morvran:** Las bestias oscuras son depredadores grandes, parecidos a perros, con cuerpos enormemente musculosos que los protegen de las armas aplastantes. Encontramos algunos mientras minábamos los túneles Mourner, en busca del Templo de la Luz.

#### Vermis del desierto

**Morvran:** Los encontrarás al este de Al Kharid, en la cima de la montaña. ¡Cuidado con sus feroces ataques a distancia!

#### Edimmu

**Morvran:** Edimmu son fantasmas que no lograron escapar de su cuerpo. Son fantasmas y zombis, pero de alguna manera completamente diferentes. Usan ataques a distancia y son muy agresivos. Puedes encontrarlos en una mazmorra de recursos a la que tiene acceso el clan Meilyr en Prifddinas.

#### Elfos

**Morvran:** No estoy recomendando matar a los de mi especie, ¿entiendes? Nos gusta que nos pongan a prueba en combate. Encontrarás luchadores cuerpo a cuerpo en el segmento de Prifddinas del Clan Iorwerth; magos y guardabosques en el segmento del Clan Cadarn.

#### Criaturas ganodermicas

**Morvran:** Las bestias ganodermicas y los enanos viven en las profundidades de una cueva al noreste de Mage Training Arena. Las criaturas de esa mazmorra están cubiertas de hongos tóxicos, por lo que debes luchar contra ellas desde la distancia. El hongo les ayuda a reparar el daño físico, por lo que quizás prefieras usar ataques mágicos.

#### Gárgolas

**Morvran:** Las gárgolas son criaturas aladas de piedra. Tendrás que luchar contra ellos hasta que estén al borde de la muerte antes de romperlos con un martillo de piedra. Se pueden encontrar en la Torre Canifis Slayer.

#### Dragones de piedras preciosas

**Morvran:** Puedes encontrar dragones de piedras preciosas debajo de la mina de gemas en Shilo Village.

#### Glaciares

**Morvran:** Lucien trajo los glacors a este mundo. Usan ataques mágicos, a distancia y cuerpo a cuerpo. Puedes encontrarlos en una caverna subterránea en Frozen Plateau.

#### Demonios mayores

**Morvran:** Los demonios mayores son débiles ante los ataques a distancia. Aunque no son los demonios más fuertes, siguen siendo peligrosos. Hay algunos en Brimhaven Dungeon.

#### Gusanos de grosella

**Morvran:** Recientemente se han visto gusanos grot en una cueva cerca de Rimmington. Morderán y atacarán con una especie de saliva ácida. Tenga cuidado, son muy agresivos.

#### Vermis de hielo

**Morvran:** Los más fríos de su tipo, se encuentran debajo de las montañas Fremennik. Como son seres de hielo, descubrí que los hechizos de fuego les infligen mucho más daño.

#### Dragones de hierro

**Morvran:** Los dragones de hierro son algunos de los dragones metálicos más débiles, con escamas de hierro que son mucho más gruesas que las armaduras de hierro normales. Su aliento de fuego y sus afiladas garras pueden anularse de diversas formas. Búscalos en Brimhaven Dungeon.

#### Demonios Kal'gerion

**Morvran:** Los demonios Kal'gerion son criaturas poderosas que usan tanto magia como cuerpo a cuerpo. Residen en una mazmorra de recursos cerca de Daemonheim. Te recomendaría que te cubrieras cuando rompan el suelo o cuando usen magia para atraerte hacia ellos.

#### Calfitos

**Morvran:** Los calfitos son insectos grandes que viven en colmenas bajo las arenas del desierto. Estoy seguro de que ya los habrás visto al suroeste del paso Shantay.

#### Vermis de lava

**Morvran:** Los strykewyrms de lava son los más poderosos de su tipo. Atacan con todos los estilos de combate y son débiles o nada. Se pueden encontrar en lo profundo de Wilderness, por lo que yo te cuidaría las espaldas mientras los mato.

#### Wyverns vivientes

**Morvran:** Los wyverns vivos respiran un veneno que te matará rápidamente a menos que te congeles. Pero cuidado; cuanto más frío tengas, más duro te golpearán sus ataques habituales.  Se pueden encontrar en la mazmorra de hielo de Asgarnia.

#### Dragones de mitril

**Morvran:** Los dragones de mitril son oponentes muy peligrosos. Hay algunos en la Caverna Antigua, al norte de donde encontrarás Kuradal. Eres un maestro de batalla: prueba tus habilidades.

#### Muspa

**Morvran:** Los muspah son criaturas nacidas de pesadillas. La magia antigua es lo más eficaz que se puede utilizar contra ellos. Puedes encontrarlos viajando a Freneskae. Serán agresivos a menos que uses tu fragmento de Zaros.

#### Jadinkos mutados

**Morvran:** Estas criaturas deformadas de enredadera de jade no dudarán en utilizar su entorno para ayudarles en el combate si no pueden tomar represalias de otra manera. Las crías de jadinkos son más fáciles de matar, pero los machos ofrecen las mayores recompensas. Las armas Ranged hechas de enredaderas son mejores contra ellos.

#### Necriael

**Morvran:** Nechryael son demonios de la decadencia que convocan a pequeños seres alados para que les ayuden a luchar contra sus víctimas. Se pueden encontrar en los Túneles del Caos o en la Torre Canifis Slayer.

#### Criaturas de pesadilla

**Morvran:** Puedes encontrar criaturas de pesadilla en Freneskae, a las que se puede acceder a través de la puerta del mundo.

#### nihil

**Morvran:** Los sujetos supervivientes de los experimentos de Zaros. Tienen poderosos ataques cargados y luchan en grupos de cuatro. Puedes encontrarlos viajando a Freneskae. Serán agresivos a menos que uses tu fragmento de Zaros.

#### Dragonantes de Nodon

**Morvran:** Los dragonantes nodon son criaturas profundamente inteligentes, armadas con armamento de asedio avanzado. Sin embargo, son débiles ante las armas dragonbane. Puedes encontrarlos luchando por Jas en Senntisten.

#### Demonios destripadores

**Morvran:** Los demonios destripadores se vuelven locos por el olor a sangre. Te golpearán más fuerte cuanto peores sean tus lesiones. Y cuidado; A veces pueden caer sobre ti desde arriba, lo cual es letal.  Se pueden encontrar en una fisura cerca de Al Kharid.

#### Dragones rúnicos

**Morvran:** Los dragones rúnicos son incluso más peligrosos que los dragones inflexibles. Te recomiendo que traigas munición dragonbane para perforar su armadura. Para encontrarlos, debes viajar a Kethsi a través de la Puerta del Mundo en Arandar.

#### Criaturas de las sombras

**Morvran:** Las sombras son criaturas ligeras que han sido corrompidas por el Señor Oscuro. Los Amlodd los convocan a su sección de la ciudad para derrotarlos y luego limpiar sus núcleos.

#### Devoradores de almas

**Morvran:** Puedes encontrar devoradores de almas en la mazmorra Sophanem Slayer.

#### Criaturas acosadoras

**Morvran:** Puedes encontrar criaturas acosadoras dentro del escondite de Zamorak.

#### Dragones de acero

**Morvran:** Los dragones de acero son peligrosos y metálicos, con escamas de acero que son mucho más gruesas que las armaduras de acero normales. Búscalos en Brimhaven Dungeon.

#### Demonios atormentados

**Morvran:** Los demonios atormentados son criaturas poderosas que usan ataques mágicos, a distancia y cuerpo a cuerpo. También tienen la capacidad de protegerse. Puedes encontrarlos debajo de la cueva Lágrimas de Guthix.

#### Tzhaar

**Morvran:** Los TzHaar son guerreros poderosos: pruébate contra ellos. Los encontrarás en lo profundo del volcán Karamja.

#### Vyrewatch

**Morvran:** Estas repugnantes criaturas se pueden encontrar en Meiyerditch y Darkmeyer en Morytania. Tienen una habilidad telepática que les permite esquivar los ataques entrantes, por lo que necesitarás un arma especialmente creada para dañarlos.

#### Demonios del agua

**Morvran:** Los Waterfiends son criaturas elementales que se encuentran al norte de Kuradal en la Caverna Antigua. Los que siguen a sus familiares están ansiosos por matarlos.

### As part of the Make Them Bleed achievement

{{Incomplete|I wasn't prepared for the dialogue, so I didn't transcribe it properly}}
- **Morvran:** ¿Qué quieres? Oh, en realidad, te ha ido bastante bien en mi campo. Aquí tienes una lámpara XP por tus esfuerzos. Úsalo o piérdelo, no me importa.
