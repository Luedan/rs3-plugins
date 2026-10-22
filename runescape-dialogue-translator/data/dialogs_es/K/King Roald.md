# King Roald

- **Original Wiki Page**: [Transcript:King Roald](https://runescape.wiki/w/Transcript%3AKing%20Roald)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Claiming the fire beacon rewards for the first time}}

### In Varrock Palace


#### Ante el sacerdote en peligro

- **Player:** Saludos, majestad.
- **King Roald:** Bueno, hola. ¿Qué deseas?
- **Player:** ¡Estoy buscando una misión!
- (ver|Sacerdote en peligro)

#### Después de un sacerdote en peligro

- [Menu]: ¿Qué quieres hacer?
  - [Choice]: Habla sobre Sacerdote en peligro.
    - **King Roald:** Bueno, hola. ¿Qué deseas?
    - **King Roald:** Ah, eres tú otra vez. Hola.
    - **Player:** Hola, Su Majestad. Me complace informarles que la situación en el Templo de Paterdomus se ha solucionado. Las fronteras de Misthalin deberían volver a estar completamente protegidas contra las amenazas de Morytania.
    - **King Roald:** Excelente, excelente. El Reino de Misthalin está en deuda contigo.
    - **Player:** ¿Estás en deuda conmigo? ¿Eso significa que me vas a dar fabulosas recompensas por mis esfuerzos?
    - **King Roald:** Por supuesto que no; sin embargo, si lo que buscas son recompensas, se me ocurre que podrías ser de aún más servicio para el reino.
    - (Condition: Without 43 Firemaking:)
      - **King Roald:** Aunque es posible que primero necesites un poco más de experiencia en el cuidado de incendios. Si estás interesado, ven a hablar conmigo cuando hayas practicado un poco más.
      - [Necesitas tener al menos 43 Firemaking para iniciar All Fired Up.]
    - (Condition: With 43 Firemaking:)
      - (ver|Todos entusiasmados)
  - [Choice]: Saluda al rey.
    - **Player:** Saludos, majestad.
    - **Player:** Hola, Su Majestad. Me complace informarles que la situación en el Templo de Paterdomus se ha solucionado. Las fronteras de Misthalin deberían volver a estar completamente protegidas contra las amenazas de Morytania.
    - (continuea|excellent)

#### Después de todo entusiasmado

- [Menu]: ¿Qué quieres hacer?{{anchor|init}}
  - [Choice]: cond=If the player has completed River of Blood|Hablando de Río de Sangre.
    - **King Roald:** Varrock ha sobrevivido a muchos ataques desde su fundación, pero estoy agradecido de que esta situación de vampyre se haya resuelto pacíficamente.
    - **Player:** Al menos por ahora. Es posible que la paz negociada no se mantenga.
    - **King Roald:** Y si no es así, nos ocuparemos de la situación. Estoy tomando medidas que, si no se cumplen, Varrock estará en una posición mucho más fuerte para afrontarlo.
    - **King Roald:** Por ejemplo, Aeonisig ofrece ayuda a los ciudadanos de Meiyerditch a cambio de envíos de blisterwood.
    - **King Roald:** La verdad es que mis preocupaciones han pasado a otros asuntos. Si no es una cosa, es otra, eso dicen.
    - **Player:** ¿Por ejemplo?
    - **King Roald:** Parece que su intervención en Salve está dirigida únicamente a vampyres. Los hombres lobo, por otro lado, son libres de cruzar.
    - **King Roald:** Los informes afirman que efectivamente han declarado su independencia de vampyres. Tendremos que vigilar de cerca lo que hacen con esta nueva libertad.
    - [Menu]: Repetir escena: ¿Te gustaría volver a reproducir el asedio de Paterdomus?
      - [Choice]: Cancelar
        - (end)
      - [Choice]: Ok
        - (Action: Reproducciones de escenas.)
  - [Choice]: Pregunta por las balizas.
    - (continue|Beacon dialogue)
  - [Choice]: Saluda al rey.
    - **Player:** Saludos, majestad.
    - **King Roald:** ¿Tienes algo importante que decir?
    - **Player:** ...En realidad no.
    - **King Roald:** Tendrás que disculparme, estoy muy ocupado.
    - **King Roald:** Debo mantener un ojo fijo en Morytania al este.
    - **Player:** ¿O quizás ambos ojos?
    - **King Roald:** De hecho, no todos podemos ser héroes y pasar de una crisis a otra.
    - **King Roald:** Desde que Kara-Meir y sus amigos se hicieron famosos, las aventuras se han convertido en una carrera preferida entre nuestros jóvenes. Sin embargo, la gente olvida que su historia es una advertencia.
    - **Player:** ¿Por qué? ¿Qué pasó con ella?
    - **King Roald:** Ocultó información importante sobre uno de sus asociados, y eso estuvo a punto de provocar un desastre para todos nosotros: cada hombre, mujer y niño.
    - **Player:** ¿Y?
    - **King Roald:** ¿Y qué? He dedicado suficiente tiempo a ti, aventurero. Tendrás que disculparme, tengo un reino que administrar.

#### Diálogo de baliza

- **Player:** Me preguntaba si podría contarme más sobre las balizas.
- **King Roald:** Por supuesto. ¿Qué te gustaría saber?
- [Menu]: Selecciona una opción
  - [Choice]: cond=If the player has rewards to claim|Estoy aquí para reclamar mi recompensa.
    - **Player:** ¡Estoy aquí para reclamar mi recompensa!
    - (Condition: If obtaining the ring of fire for the first time:)
      - **King Roald:** Para mantener seis balizas encendidas simultáneamente, te presento el Anillo de Fuego.
      - **Player:** ¡Muchas gracias!
      - (receives=ring of fire)
      - (continue)
    - (Condition: If the ring of fire has been lost:)
      - **King Roald:** ¿Perdiste el Anillo de Fuego, verdad? Por suerte parece que tengo uno de repuesto.
      - **Player:** ¡Muchas gracias!
      - (receives=ring of fire)
      - (continue)
    - (Condition: If obtaining the flame gloves for the first time:)
      - {{transcript missing}}
      - (continue)
    - (Condition: If the flame gloves have been lost:)
      - **King Roald:** Hmm, parece que has extraviado tus guantes Flame, ¡qué bueno que tenemos más!
      - **Player:** ¡Muchas gracias!
      - (receives=flame gloves)
      - (continue)
    - (Condition: If obtaining the inferno adze for the first time:)
      - {{transcript missing}}
      - (continue)
    - (Condition: If the inferno adze has been lost:)
      - **King Roald:** Esto apareció recientemente en el objeto perdido y encontrado, tu Inferno Adze.
      - **Player:** ¡Muchas gracias!
      - (receives=inferno adze)
      - (continue)
    - **King Roald:** Gracias de nuevo, Player. Misthalin está verdaderamente en deuda contigo.
    - **King Roald:** ¿Hay algo más que quieras preguntarme?
    - (previous)
  - [Choice]: ¿Qué más hay que hacer para probar la red de balizas?
    - **Player:** ¿Qué más hay que hacer para probar la red de balizas?
    - **King Roald:** ¡Lo que *no* es necesario hacer es más bien! Necesitamos asegurarnos de que toda la red de balizas sea lo más sólida posible.
    - **King Roald:** Le agradecería mucho que nos ayudara intentando mantener encendidas tantas balizas simultáneamente como sea posible.
    - **Player:** ¿Cómo ayuda eso?
    - **King Roald:** Bueno, obviamente, nos ayuda a verificar que todas las balizas estén en buen estado de funcionamiento, por supuesto.
    - **King Roald:** Cuantas más pruebas, mejor, Player. Tengo generosas recompensas para ti si logras mantener seis, diez y catorce balizas encendidas simultáneamente.
    - **King Roald:** Sin embargo, estaría encantado si continuaras probándolos día y noche, una y otra vez, sin descanso y sin cesar.
    - **Player:** Veo que esto significa mucho para ti.
    - **King Roald:** Oh, así es. La seguridad del reino de uno es de suma importancia, ¿sabes?
    - **King Roald:** ¿Tienes alguna otra pregunta para mí, Player?
    - (previous)
  - [Choice]: cond=If there aren't any rewards to claim|Cuéntame sobre las recompensas.
    - **Player:** Háblame sobre las recompensas.
    - **King Roald:** Ejem, bueno. Está muy bien tener una red de balizas, pero es importante asegurarse de que funcione correctamente... y siga funcionando. Por lo tanto, estoy dispuesto a ofrecer varias recompensas si estás dispuesto a ayudarme. Hay recompensas disponibles por mantener encendidas seis, diez y catorce balizas simultáneamente.
    - (Condition: If the player hasn't unlocked the ring of fire:)
      - **King Roald:** Por mantener seis balizas encendidas, estoy dispuesto a otorgarte un anillo que te ayudará en Firemaking.
      - (continue)
    - (Condition: If the player has unlocked the ring of fire:)
      - **King Roald:** Te he concedido el Anillo de Fuego por mantener encendidas seis balizas.
      - (continue)
    - (Condition: If the player hasn't unlocked the flame gloves:)
      - **King Roald:** Por mantener diez balizas encendidas, te daré un par de guantes que funcionarán en combinación con el anillo.
      - (continue)
    - (Condition: If the player has unlocked the flame gloves:)
      - **King Roald:** Ya has reclamado los guantes de llamas por mantener encendidas diez balizas.
      - (continue)
    - (Condition: If the player hasn't unlocked the inferno adze:)
      - **King Roald:** Para mantener encendidas las catorce balizas, bueno, tengo el magnífico Inferno Adze, una herramienta de encantamiento de fuego tanto para Woodcutting como para Mining, de la que estoy dispuesto a desprenderme. Creo que lo encontrarás de gran utilidad.
      - (continue)
    - (Condition: If the player has unlocked the inferno adze:)
      - **King Roald:** Por mantener las catorce balizas encendidas simultáneamente, se te ha otorgado el Inferno Adze. ¿Hay algo más?
      - (previous)
  - [Choice]: Me gustaría algunos detalles más, por favor.
    - **Player:** Me gustaría tener más detalles, por favor.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Por qué has creado todas estas balizas?
        - **Player:** ¿Por qué has creado todas estas balizas?
        - **King Roald:** Ya has vislumbrado los peligros que enfrentamos desde Morytania. Más peligros amenazan desde el Wilderness en el norte.
        - **King Roald:** Debido a estas crecientes amenazas, los reinos del sur se han unido para tomar medidas.
        - **King Roald:** Hemos construido una red de balizas que se extiende desde el nacimiento del río Salve hasta el extremo noroeste del Wilderness.
        - **King Roald:** Si hubiera alguna amenaza proveniente de estas tierras incivilizadas, podremos correr la voz tan rápido como la luz de las llamas pueda viajar.
        - (previous)
      - [Choice]: ¿Cómo funcionarán estas balizas en caso de emergencia?
        - **Player:** ¿Cómo funcionarán estas balizas en caso de emergencia?
        - **King Roald:** Sencillo. He equipado a cada bombero con una reserva de encendedores gnomos. En caso de una emergencia real, las balizas arderán con llamas de colores.
        - **Player:** Ya veo. Supongo que no tendrás ningún encendedor extra por ahí del que quieras deshacerte, ¿verdad?
        - **King Roald:** No me molestes con charlas ociosas. ¿Hay algo más?
        - (previous)
      - [Choice]: ¿Quiénes son estos bomberos?
        - **Player:** ¿Quiénes son estos bomberos?
        - **King Roald:** Estos son reclutas especiales de todo el mundo civilizado. Han sido cuidadosamente seleccionados por sus ojos agudos y su visión de larga distancia.
        - **King Roald:** Sin mencionar su dedicación y confiabilidad. No podíamos confiar un trabajo tan importante a cualquiera, ¿sabes?
        - (previous)
      - [Choice]: En realidad, no tengo nada más de qué hablar.
        - **Player:** En realidad, no tengo nada más de qué hablar.
        - **King Roald:** Entonces vete; Soy un hombre ocupado.
  - [Choice]: En realidad, no tengo nada más de qué hablar.
    - **Player:** En realidad, no tengo nada más de qué hablar.
    - **King Roald:** Entonces vete; Soy un hombre ocupado.

#### Senderos del tesoro

- (Condition: Only the first time:)
  - **King Roald:** ¿Hay alguna razón para que estés aquí?
  - **Player:** Bueno, estoy siguiendo la pista del tesoro.
  - **King Roald:** ¡Oh! Bien, entonces puedes responderme esta pregunta.
- (receives=challenge scroll (medium))
- [¡King Roald te ha dado un pergamino de desafío!]

##### Cuando hablé de nuevo

- **King Roald:** Ingrese la respuesta a la pregunta.
- Ingrese la cantidad:<br>[Input field]
- ((When given the wrong answer:))
  - **King Roald:** Err, eso me suena un poco mal.
- ((When given the correct answer:))
  - (removes=the old clue scroll (medium) y desplazamiento de desafío (medio))
  - ((If the trail continues:))
    - (receives=a new clue scroll (medium))
    - [¡King Roald te ha dado otro pergamino de pistas!]
  - ((If the trail ends:))
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
  - **King Roald:** ¡Correcto!

#### Diálogo histórico

- [Menu]: ¿Qué quieres hacer?{{anchor|init_2022_10_31}}
  - [Choice]: Habla sobre Sacerdote en peligro.
    - (ver|Sacerdote en peligro)
  - [Choice]: Pregunta sobre el reino.
    - **Player:** Saludos, majestad. ¿Cómo le va al reino?
    - (Condition: During the Battle of Lumbridge:)
      - **King Roald:** ¡Es terrible! ¿No lo has oído? ¡Zamorak y Saradomin están peleando cerca de Lumbridge! ¡Han destruido gran parte del castillo! ¡Eso es propiedad real! Estoy muy molesto.
      - **King Roald:** Le he encargado a Duke Horacio que solucione el problema y él afirma que necesita más tropas.
      - **King Roald:** Como puedes ver, estoy muy ocupado en este momento. Por favor, no me hagas perder el tiempo.
      - (initial)
    - (Condition: After the Battle of Lumbridge:)
      - **King Roald:** ¡El reino vuelve a estar en paz después de la batalla de Lumbridge! Me alegra ver que Saradomin y Zamorak ya no están allí.
      - **King Roald:** ¡Realmente espero que ese tipo de cosas no vuelvan a suceder en mi reino! ¡Hay mucho que ordenar!
      - **King Roald:** Como puedes ver, estoy muy ocupado en este momento. Por favor, no me hagas perder el tiempo.
  - [Choice]: Pregunta por el árbol protegido.
    - (Condition: When the tree was diseased:)
      - **Player:** Su majestad, traigo noticias preocupantes. ¡El árbol que estás protegiendo cerca de la ribera occidental de Varrock ha enfermado!
      - **King Roald:** Gracias por informarme sobre esto. Ya he mandado llamar a un maestro jardinero para restaurarlo.
      - **Player:** Oh, bien. Odiaría que le pasara algo más a ese árbol.
      - (initial|init_2022_10_31)
    - (Condition: When the tree died:)
      - **Player:** Su majestad, traigo noticias preocupantes. ¡El árbol que estás protegiendo cerca de la ribera occidental de Varrock ha muerto!
      - **King Roald:** ¿Cómo sucedió esto? ¡Mandé llamar a un maestro jardinero para restaurarlo hace más de una semana! Tiene algunas explicaciones que dar. Una vez que él aparezca, al menos.
      - **Player:** Otro árbol desaparecido...
      - (initial|init_2022_10_31)
    - (Condition: When the tree was replanted:)
      - **Player:** Saludos, majestad. ¿Cómo le va al árbol al oeste del banco Varrock?
      - **King Roald:** Recibí informes de que el árbol había muerto. Yo mismo visité el árbol y vi crecer un árbol sano.
      - **Player:** Sí, ¡eso es porque Farmer Jimbo reemplazó el árbol muerto!
      - **King Roald:** ¡Silencio! No volveré a oír más rumores sobre estos rumores.
      - (initial|init_2022_10_31)
  - [Choice]: Saluda al rey.
    - (above|greet)
