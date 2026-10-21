# NPC Contact

- **Original Wiki Page**: [Transcript:NPC Contact](https://runescape.wiki/w/Transcript%3ANPC%20Contact)
- **Letter**: `N`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Tooltip

{{Información sobre herramientas de hechizos|
<poem>
Habla telepáticamente con una selección de NPC útiles.
</poem>
}}

### Non-random NPC dialogue


#### Honest Jimmy

- **Player:** ¿Hola?
- **Honest Jimmy:** Eh, ¿quién está ahí?
- **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo. No te preocupes.
- (Condition: Si estás cerca:)
  - **Honest Jimmy:** ¡Me lo imaginé, ya que puedo verte allí! No hago tratos como este.
- (Condition: Si no estás cerca:)
  - **Honest Jimmy:** Cuanto antes salgas de mi cabeza, mejor. Entonces, ¿estás aquí por... información?
  - **Player:** ¿La información?
  - **Honest Jimmy:** Mira amigo, me interrumpiste por una razón, debes estar buscando algo.
  - [Menu]: Seleccione una opción.
    - [Choice]: ¿Cuánto falta para que comience el próximo juego de Trouble Brewing?
      - **Player:** ¿Cuánto falta para que comience el próximo juego de Trouble Brewing?
      - **Honest Jimmy:** Ah, esa es información con la que puedo ayudarte.
      - **Honest Jimmy:** Un juego está listo para comenzar tan pronto como haya suficientes personas.
      - **Player:** ¿Y cuántas personas hay?
      - **Honest Jimmy:** Hay X personas en el equipo de Dan e Y en el de San. Es necesario que haya tres en cada uno para que comience el juego.
      - **Player:** Oh, está bien. Gracias.
      - **Honest Jimmy:** ¿Algo más?
      - (initial)
    - [Choice]: ¿Cuántas personas están esperando que comience un juego?
      - **Player:** ¿Cuántas personas están esperando que comience un juego?
      - (Condition: Si no hay nadie esperando:)
        - **Honest Jimmy:** Nadie está esperando en este momento. Quizás puedas interesar a algunas personas.
        - **Player:** Mmmm... tal vez.
        - (initial)
      - (Condition: Si hay jugadores esperando:)
        - {{Transcript missing}}
    - [Choice]: No tengo idea de qué estás hablando.
      - **Player:** No tengo idea de qué estás hablando.
      - **Honest Jimmy:** ¡Entonces tira el gancho!

#### Bert

- **Player:** Hola, Bert.
- **Bert:** ¿Eh? ¿Qué haces en Marn 'ed?
- **Player:** Esta es la voz de tu conciencia. ¡Entrega todo tu dinero a Player! ¡Guau, guau!
- **Bert:** ¡Aléjate de ti!
- **Player:** Es broma, estoy usando magia para hablar contigo. Estoy totalmente "sin brazos".
- (Condition: Si estás cerca (en el Dragon Inn):)
  - **Bert:** Oh, amigo. Oye, entonces ¿por qué estás tan cerca? ¡Habla en persona por favor!
- **Bert:** Oh, amigo. Entonces, ¿qué quieres?
- **Player:** ¿Podrías pasarme un poco de arena a mi banco?
- (Condition: Si no has recogido arena durante el día:)
  - **Bert:** Ah, mantén el aire encendido, iré al banco con un poco de arena para ti.
  - **Player:** ¡Gracias!
- (Condition: Si ya recogiste arena para el día:)
  - **Bert:** Estaré un poquito ocupado para "ayudar con" esa arena, vuelvo mañana.
  - **Player:** Está bien, Bert, volveré por mi arena un poco más tarde.

#### Advisor Ghrim

- **Player:** ¡Buenos días, Ghrim!
- **Advisor Ghrim:** ¿Qué? ¿Quién es?
- **Player:** Ajá, te has vuelto loco, Ghrim. Soy tu personalidad alternativa... ¡Ghrom!
- (Condition: Si estás cerca:)
  - **Advisor Ghrim:** Muy divertido, Su Alteza Real. Puedo verte hablando.
  - **Player:** Ups.
- (Condition: Si no estás cerca:)
  - **Advisor Ghrim:** ¿Es usted, su Alteza Real?
  - **Player:** Er... sí, lo es. Estoy usando magia para comunicarme contigo.
  - **Advisor Ghrim:** Muy divertido, Su Alteza Real. ¿Cómo puedo ayudarte?
  - [Menu]: Selecciona una opción
    - [Choice]: ¿Cómo le va al reino?
      - (ver|Advisor Ghrim)
    - [Choice]: ¿Cómo administro el reino?
      - (ver|Advisor Ghrim)
    - [Choice]: Acerca de la tarea Sistema:...
      - (ver|Advisor Ghrim)
    - [Choice]: Eso es todo, gracias.
      - **Player:** Eso es todo, gracias.
      - **Advisor Ghrim:** Muy bien, Su Alteza Real. Si tiene más problemas, por favor hable conmigo en persona.

#### Turael/Spria


##### Turael (antes y durante Mientras Guthix duerme)

- **Player:** ¿Hola?
- **Turael:** 'Hola, ¿quién es ese?
- **Player:** Soy Player. Estoy usando magia para comunicarme contigo.
- **Turael:** Extraño. Anda entonces, ¿qué quieres?
- [Menu]: Elige una opción:
- (Condition: Durante Mientras Guthix duerme antes de reclutar a Turael:)
  - [Choice]: Necesito hablar contigo sobre Lucien.
    - **Player:** ¡Necesito hablarte sobre Lucien!
    - **Turael:** Ah, sí, ¿y qué pasa con Lucien? Hace tiempo que no escucho ese nombre.
    - **Player:** Su poder está creciendo y debemos detenerlo. ¿Estaría interesado en unirse a un pequeño grupo encargado de hacerlo?
    - **Turael:** He pasado los últimos años diciéndoles a los aficionados que maten duendes. La emoción y el peligro suenan como el boleto antes de dejar el trabajo para siempre.
    - **Player:** ¡Buenas noticias Turael, muchas gracias!
  - [Choice]: pregunta sobre otra cosa
    - [Choice]: Necesito otra tarea.
      - **Player:** Necesito otra tarea.
      - (Condition: Si el jugador ya tiene una asignación Slayer:)
        - **Turael:** Todavía estás cazando a [assigned creature]; Vuelve cuando hayas terminado tu tarea.
  - [Choice]: Eh... nada...
    - **Player:** Er... Nada...
- (Condition: Después de reclutar a Turael (Mientras Guthix duerme))
  - **Player:** ¡Necesito hablarte sobre Lucien!
  - **Turael:** Pareces muy olvidadizo, de verdad. Ya me has reclutado, no tiene sentido volver a intentarlo.
  - (end)
(Condition: Si Player está muy cerca de Turael)
- **Player:** ¿Hola?
- **Turael:** 'Hola, ¿quién es ese?
- **Player:** Soy Player. Estoy usando magia para comunicarme contigo.
- **Turael:** Bueno, por favor no lo hagas. Si quieres hablar conmigo, hazlo cara a cara. Puedo verte, ¿sabes?
- (end)

##### Spria (después de Mientras Guthix duerme)

- **Player:** ¿Hola?
- **Spria:** 'Hola, ¿quién es ese?
- **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo.
- (Condition: Si estás cerca:)
  - **Spria:** Bueno, por favor no lo hagas. Si quieres hablar conmigo, hazlo cara a cara. Puedo verte, ¿sabes?
- (Condition: Si no estás cerca:)
  - **Spria:** Extraño. Anda entonces, ¿qué quieres?
  - [Menu]: Selecciona una opción
    - [Choice]: Necesito otra tarea.
      - (ver|Spria#Obtener tarea)
    - [Choice]: Eh... nada.
      - (end)

#### Lanthus

- **Player:** Hola, Lanthus
- **Lanthus:** ¿Eh?
- **Player:** ¡No tengas miedo! ¡Soy el dios todopoderoso de todos! ¡Inclínate ante tu creador!
- (Condition: Si estás cerca:)
  - **Lanthus:** No, no lo eres. Estás parado allí. ¡Déjame en paz!
- (Condition: Si no estás cerca:)
  - **Lanthus:** Está bien, está bien; Me inclino, me inclino. ¡Sólo no me hagas daño!
  - **Player:** ¿Me estás escuchando, Lanthus?
  - **Lanthus:** Yo... lo soy. ¿Cómo puedo ayudarte?
  - [Menu]: Selecciona una opción
    - [Choice]: ¿Cuánto falta para que empiece otro juego?
      - **Player:** ¿Cuánto falta para que comience otro juego?
      - **Lanthus:** El n-siguiente juego comienza en X minuto[s]. Señor.
      - **Player:** Muy bien.
      - **Lanthus:** ¿Pero por qué quieres saber eso?
      - **Player:** ¡Silencio!
      - (initial)
    - [Choice]: ¿Cuántas personas hay esperando en cada habitación?
      - **Player:** ¿Cuántas personas hay esperando en cada sala?
      - (Condition: Si la sala Zamorak está vacía:)
        - **Lanthus:** No hay nadie en la sala Zamorak,
      - (Condition: Si la sala Zamorak no está vacía:)
        - {{Transcript missing}}
      - (Condition: Si la sala Saradomin está vacía:)
        - **Lanthus:** y no hay nadie en la sala Saradomin.
      - (Condition: Si la sala Saradomin no está vacía:)
        - {{Transcript missing}}
      - (initial)
    - [Choice]: Eso es todo. Ahora no te metas en problemas.
      - **Player:** Eso es todo. Ahora no te metas en problemas.
      - **Lanthus:** S-sí.
      - **Player:** Te estoy observando, Lanthus.

#### Sumona

- **Player:** ¿Hola?
- (Condition: Si estás cerca:)
  - **Sumona:** 'Hola, ¿quién es ese?
  - **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo.
  - **Sumona:** Bueno, por favor no lo hagas. Si quieres hablar conmigo, hazlo cara a cara. Puedo verte, ¿sabes?
- (Condition: Si no estás cerca:)
  - **Sumona:** 'Hola, Player.
  - **Player:** Estoy usando magia para comunicarme contigo.
  - [Menu]: Selecciona una opción
    - [Choice]: Necesito otra tarea.
      - (ver|Sumona#After_Smoking_Kills)
    - [Choice]: Eh... nada.
      - (end)

#### Mazchna/Achtryn


##### Mazchna (antes/después mientras Guthix duerme)

- **Player:** ¿Hola?
- **Mazchna:** 'Hola, ¿quién es ese?
- **Player:** Soy Player. Estoy usando magia para comunicarme contigo.
- (Condition: Si estás cerca:)
  - **Mazchna:** Bueno, por favor no lo hagas. Si quieres hablar conmigo, hazlo cara a cara. Puedo verte, ¿sabes?
- (Condition: Si no estás cerca:)
  - **Mazchna:** Extraño. Anda entonces, ¿qué quieres?
  - [Menu]: Selecciona una opción
    - [Choice]: Necesito otra tarea.
      - (ver|Mazchna)
    - [Choice]: Er... Nada.
      - (end)

##### Achtryn (durante Mientras Guthix duerme)

- {{Transcript missing}}

#### Duradel/Lapalok


##### Duradel (antes Mientras Guthix duerme)

- {{Transcript missing}}

##### Lapalok (después de Mientras Guthix duerme)

- **Player:** ¿Hola?
- **Lapalok:** 'Hola, ¿quién es ese?
- **Player:** Soy Player. Estoy usando magia para comunicarme contigo.
- (Condition: Si estás cerca:)
  - **Lapalok:** Bueno, por favor no lo hagas. Si quieres hablar conmigo, hazlo cara a cara. Puedo verte, ¿sabes?
- (Condition: Si no estás cerca:)
  - **Lapalok:** Extraño. Anda entonces, ¿qué quieres?
  - [Menu]: Selecciona una opción
    - [Choice]: Necesito otra tarea.
      - (ver|Lapalok)
    - [Choice]: Er... Nada.
      - (end)

#### Vannaka

- **Player:** ¿Hola?
- **Vannaka:** 'Hola, ¿quién es ese?
- **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo.
- (Condition: Si estás cerca:)
  - **Vannaka:** Bueno, por favor no lo hagas. Si quieres hablar conmigo, hazlo cara a cara. Puedo verte, ¿sabes?
- (Condition: Si no estás cerca:)
  - **Vannaka:** Extraño. Anda entonces, ¿qué quieres?
  - [Menu]: Selecciona una opción
    - [Choice]: Necesito otra tarea.
      - (ver|Vannaka)
    - [Choice]: Eh... nada.
      - (end)

#### Murphy

- **Player:** Hola
- **Murphy:** ¿Qué...?
- **Player:** No te preocupes, Murphy. ¡Mi nombre es Player y estoy usando magia para contactarte!
- (Condition: Si estás cerca:)
  - **Murphy:** ¡Eso es tan grosero cuando podrías hablar conmigo en persona!
- (Condition: Si no estás cerca:)
  - **Murphy:** ¡Pues yo nunca! Tecnología en estos días. Está más allá de mí. Entonces, ¿cómo puedo ayudarte?
  - **Player:** Me preguntaba si había alguien ahí abajo ayudándote en el barco pesquero.
  - (Condition: Si el barco ha partido:)
    - **Murphy:** ¡El barco acaba de zarpar, de hecho! ¿Quizás, cuando regrese, puedas unirte a ellos en otra carrera?
    - **Player:** Suena como un plan.
  - (Condition: Si el barco no ha zarpado:)
    - **Murphy:** El barco está ahí, esperando a que alguien se una. ¿Qué tal?
    - **Player:** Tal vez vaya a echar un vistazo. Te veré más tarde.
    - **Murphy:** Está bien, amigo. ¡Adiós!

#### Chaeldar

- **Player:** ¿Hola?
- **Chaeldar:** 'Hola, ¿quién es ese?
- **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo.
- (Condition: Si estás cerca:)
  - **Chaeldar:** Bueno, por favor no lo hagas. Si quieres hablar conmigo, hazlo cara a cara. Puedo verte, ¿sabes?
- (Condition: Si no estás cerca:)
  - **Chaeldar:** Extraño. Anda entonces, ¿qué quieres?
  - [Menu]: Selecciona una opción
    - [Choice]: Necesito otra tarea.
      - (ver|Chaeldar)
    - [Choice]: Er... Nada.
      - (end)

#### Cyrisus

- {{Trandom}}
  - ''Conversación 1:
    - **Player:** Hola amigo. ¿Qué estás haciendo ahora?
    - **Cyrisus:** Erm, estoy un poco ocupado en este momento.
    - **Player:** Oooh, apuesto a que estás viajando por los mares. ¿O tal vez estás visitando a líderes mundiales?
    - **Cyrisus:** Bueno, estoy intentando luchar contra TzTok-Jad en este momento.
    - **Player:** ¡Debe ser muy duro!
    - **Cyrisus:** Sí, tiene un nivel de combate de 702.
    - **Player:** ¡Disfruta!
    - **Cyrisus:** Gracias. ¡Arghhhh, muerte para ti, bestia asquerosa!
  - ''Conversación 2:
    - **Player:** ¡Hola!
    - **Cyrisus:** Oh, hola.
    - **Player:** ¿En qué aventura estás ahora?
    - **Cyrisus:** Bueno, acabo de enviar a TzTok-Jad. ¡Bastante duro! Ahora estoy de camino al desierto. Voy a ver si puedo localizar a ese Kalphite Queen del que todo el mundo me habla.
    - **Player:** Debo advertirte que necesitarás un equipo para enfrentarte a esa bestia.
    - **Cyrisus:** Ya he pensado en eso. He hecho arreglos para que un par de slayer masters se unan a mí.
    - **Player:** ¡Guau! ¡Ojalá pudiera presenciar eso!
  - ''Conversación 3:
    - **Player:** ¡Hola de nuevo!
    - **Cyrisus:** Qué gracioso, justo estaba hablando de ti.
    - **Player:** ¿Lo estabas?
    - **Cyrisus:** Sí, he estado organizando a varios líderes de Runescape para discutir algunos temas políticos. ¡Parece que ya llevas un tiempo por aquí!
    - **Player:** Supongo que sí. ¿Qué temas se supone que debes discutir en esta reunión? ¿Quién estará allí?
    - **Cyrisus:** Lo siento, esa es información ultrasecreta.
    - **Player:** Está bien, lo entiendo.
  - ''Conversación 4:
    - **Player:** Hola, ¿dónde estás ahora?
    - **Cyrisus:** Estoy en la arena de Guerras de clanes todos contra todos: la que tiene el bonito portal rojo. Estoy conociendo a mucha gente interesante.
    - **Player:** ¿Ah? Es un lugar divertido para conocer gente.
    - **Cyrisus:** Bueno, yo también pensé eso, pero este tipo me dijo que trajera todos mis artículos más valiosos y lo siguiera hasta allí para encontrarse con sus amigos.
    - **Player:** Um, Cyrisus, ¿no tienes miedo de que te maten y pierdas todas tus cosas?
    - **Cyrisus:** Oh, sí, lo intentaron. Así que los maté a todos. Pero fue muy agradable conocerlos de todos modos.
    - **Player:** Supongo que estás bien.
  - ''Conversación 5:
    - **Player:** Hola. ¿Cómo estás?
    - **Cyrisus:** Summoning, invocaciones y más invocaciones!
    - **Player:** ¿En serio? Bonita. Entonces, ¿cuál es tu elección de mascota en este momento?
    - **Cyrisus:** ¡Dragón!
    - **Player:** ¡De ninguna manera! Estoy tan celoso.
    - **Cyrisus:** Ciertamente ha requerido mucho trabajo duro, ¡pero vale la pena!
    - **Player:** ¡Apuesto!

#### Eluned

- (Condition: Si tienes una semilla de teletransporte de cristal descargada en tu inventario:)
  - (opens=Crystal teleport seed#Charges)
- (Condition: Si no tienes una semilla de teletransporte Crystal descargada en tu inventario (o está parcialmente cargada):)
  - **Eluned:** ¿Player? ¿Quieres que te vuelva a encantar las semillas de teletransporte de cristal?
  - **Player:** No tengo ninguno de esos.
  - **Eluned:** Quizás en otro momento.

#### Larry/Chuck


##### Larry (antes de Hunt for Red Raktuber)

- {{Transcript missing}}

##### Chuck (después de la caza del Raktuber rojo)

- **Player:** Hola.
- **Chuck:** Saludos, voz en mi cabeza.
- **Player:** Quería hablarte sobre los pingüinos espías en todo el mundo.
- **Chuck:** ¿Qué pasa con ellos?
- [Menu]: Selecciona una opción
  - [Choice]: He encontrado más pingüinos.
    - **Player:** He encontrado más pingüinos.
    - **Chuck:** ¿Más? Mmmm, interesante. ¿Cuántos has encontrado?
    - **Player:** Encontré a X penguin[s] esta semana.
      - (Condition: Si no has encontrado todos los pingüinos esta semana:)
        - [Menu]: Selecciona una opción
          - [Choice]: Tengo problemas para encontrar los pingüinos. ¿Puedo tener una pista?
            - '' (Se muestra uno de los siguientes, dependiendo de la ubicación de los pingüinos:)
              - **Chuck:** He oído que hay un pingüino ubicado alrededor de un pueblo entre una gran torre y la mansión de vampyre.
              - **Chuck:** He oído que hay un pingüino ubicado alrededor de Ardougne.
              - **Chuck:** He oído que hay un pingüino ubicado alrededor de Feldip Hills, cerca de Gu'Tanoth.
              - **Chuck:** He oído que hay un pingüino ubicado alrededor de la región Al Kharid, al norte del paso Shantay.
              - **Chuck:** He oído que hay un pingüino ubicado alrededor de la región de Ice Mountain.
              - **Chuck:** He oído que hay un pingüino ubicado entre los Fremenniks y los Bárbaros.
              - **Chuck:** He oído que hay un pingüino ubicado en lo profundo de la jungla.
              - **Chuck:** He oído que hay un pingüino ubicado al este del Mage Training Arena.
              - **Chuck:** He oído que hay un pingüino ubicado en una ciudad de plagas dentro del desierto.
              - **Chuck:** He oído que hay un pingüino ubicado en un pueblo de druidas.
              - **Chuck:** He oído que hay un pingüino ubicado en Falador o sus alrededores.
              - **Chuck:** He oído que hay un pingüino ubicado al este del reino de Kandarin.
              - **Chuck:** He oído que hay un pingüino ubicado en el reino de las hadas.
              - **Chuck:** He oído que hay un pingüino ubicado en los páramos helados.
              - **Chuck:** He oído que hay un pingüino ubicado en el norte de Kharidian desert.
              - **Chuck:** He oído que hay un pingüino ubicado en el norte del reino de Misthalin.
              - **Chuck:** He oído que hay un pingüino ubicado en el sur de Kharidian desert.
              - **Chuck:** He oído que hay un pingüino ubicado en el sur del reino de Misthalin.
              - **Chuck:** He oído que hay un pingüino ubicado en el oeste del reino de Kandarin.
              - **Chuck:** He oído que hay un pingüino ubicado en wilderness.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de un gran árbol rodeado de gente baja.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de una montaña de lobos.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de un pantano contaminado.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de un pueblo de hombres lobo.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de Port Sarim.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de unos ogros en South Feldip Hills.
              - **Chuck:** He oído que hay un pingüino ubicado cerca del Puesto Bárbaro.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de las abejas y el lino.
              - **Chuck:** He oído que hay un pingüino ubicado cerca del Castillo de Arturo.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de la ciudad de los fantasmas.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de la costa, al este de Ardougne.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de la isla de Dragontooth.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de los saltamontes.
              - **Chuck:** He oído que hay un pingüino ubicado cerca de los de orejas puntiagudas.
              - **Chuck:** He oído que hay un pingüino ubicado al norte de Ardougne.
              - **Chuck:** He oído que hay un pingüino ubicado en una gran isla en forma de media luna.
              - **Chuck:** He oído que hay un pingüino ubicado en una isla, etc.
              - **Chuck:** He oído que hay un pingüino ubicado en islas donde los hermanos se pelean.
              - **Chuck:** He oído que hay un pingüino ubicado en algún lugar más allá de la detección.
              - **Chuck:** He oído que hay un pingüino ubicado en algún lugar de Gielinor.
              - **Chuck:** He oído que hay un pingüino ubicado al sur de Ardougne.
              - **Chuck:** He oído que hay un pingüino ubicado al oeste de Ardougne, en las colinas.
              - **Chuck:** He oído que hay un pingüino ubicado al oeste de Varrock.
              - **Chuck:** He oído que hay un pingüino ubicado donde habitan los contrabandistas de plátanos.
              - **Chuck:** He oído que hay un pingüino ubicado donde gobiernan los chupasangres.
              - **Chuck:** He oído que hay un pingüino ubicado donde vuelan las águilas.
              - **Chuck:** He oído que hay un pingüino ubicado donde los pescadores colonizan.
              - **Chuck:** He oído que hay un pingüino ubicado donde gobiernan los monos.
              - **Chuck:** He oído que hay un pingüino ubicado donde no pueden ir armas.
              - **Chuck:** He oído que hay un pingüino ubicado donde los piratas se sienten en su mayoría inofensivos.
              - **Chuck:** He oído que hay un pingüino ubicado donde habitan los duendes de ojos grandes.
              - **Chuck:** He oído que hay un pingüino ubicado donde los enanos excavan profundamente.
              - **Chuck:** He oído que hay un pingüino ubicado donde el Fremennik 'heim' y busca
              - **Chuck:** He oído que hay un pingüino ubicado donde entrena la Guardia Imperial.
              - **Chuck:** He oído que hay un pingüino ubicado donde estudian los magos.
  - [Choice]: Tengo problemas para encontrar los pingüinos. ¿Puedo tener una pista?
    - (arriba)
  - [Choice]: No importa.
    - **Player:** No importa.

#### Kuradal

{{Incomplete|Requires dialogue for if you interrupt her during a bad time, such as while a monster tries to escape the dungeon}}
- **Player:** ¿Hola?
- **Kuradal:** 'Hola, ¿quién es?
- **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo.
- (Condition: Si estás cerca:)
  - **Kuradal:** Qué desperdicio de runas. Puedo verte, ¿sabes? Hablemos cara a cara.
- (Condition: Si no estás cerca:)
  - **Kuradal:** Una aplicación útil del talento mágico. ¿Cómo puedo ayudar?
  - [Menu]: Selecciona una opción
    - [Choice]: Necesito otra tarea.
      - (ver|Kuradal)
    - [Choice]: Er... Nada.
      - (end)

#### Dark Mage

- **Player:** ¿Hola?
- **Dark Mage:** ¡¿Qué es esto?! ¡No debes romper mi concentración!
- **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo.
- (Condition: Si estás cerca:)
  - **Dark Mage:** ¡Qué desperdicio de runas! - Puedo verte, hablemos cara a cara.
- (Condition: Si no estás cerca:)
  - **Dark Mage:** ¿Estás intentando colapsar el Abismo? ¿Qué deseas? ¡Habla rápido!
  - (Condition: Si el libro Abyssal está en tu inventario o banco:)
    - **Player:** En realidad, no se me ocurre nada en este momento...
    - **Dark Mage:** ¡ENTONCES DEJA DE DISTRAERME!
    - **Dark Mage:** Honestamente, ¡no tienes idea de la presión que estoy bajo al intentar mantener este portal abierto!
  - (Condition: Si el libro Abyssal no está en tu inventario o banco:)
    - **Player:** Lamento molestarte. Solo necesitaba tu ayuda con algo rápido.
    - **Dark Mage:** ¿Qué? Ah... Muy bien. ¿Qué querías?
    - [Menu]: Elige una opción:
      - [Choice]: ¿Puedo tener otro libro de Abyssal?
        - **Player:** ¿Puedo tener otro libro de Abyssal? Parece que perdí el que me dieron.
        - **Dark Mage:** Toma, tómatelo, es importante aunar nuestra investigación. ¡Ahora déjame en paz, debo concentrarme!
        - (receives=Abyssal book)
      - [Choice]: La verdad es que ahora mismo no se me ocurre nada...
        - **Player:** En realidad, no se me ocurre nada en este momento...
        - **Dark Mage:** ¡ENTONCES DEJA DE DISTRAERME!
        - **Dark Mage:** Honestamente, ¡no tienes idea de la presión que estoy bajo al intentar mantener este portal abierto!

#### Pikkupstix

- **Player:** ¿Hola?
- **Pikkupstix:** ¡Ahh, una voz familiar en mi cabeza!
- [Menu]: Selecciona una opción
  - [Choice]: Entonces, ¿dónde está Pikkenmix?
    - (ver|Pikkupstix)
  - [Choice]: ¿De qué se trata?
    - (ver|Pikkupstix)

#### Pauline Polaris

- **Player:** ¡Hola Paulina!
- **Pauline Polaris:** ¡Bah! ¡Me hiciste saltar! ¿Supongo que quieres reclamar algunos deseos de recompensa?
- **Player:** Sí, por favor.
- (opens=Livid_Farm#Rewards)

#### Oneiromancer

- **Player:** Oneiromancer!
- **Oneiromancer:** ¿Qué? Ah, muy brillante que me contactes de esta manera.
- **Player:** Sí, pensé en utilizar el nuevo hechizo para hacer una pregunta.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Puedes cambiar mi libro de hechizos al estándar?
    - (Condition: Si no has completado las tareas del diario de logros de élite:)
      - **Oneiromancer:** Hmmm, no, creo que primero debes demostrar tu valía un poco más.
      - Si completas las tareas del diario de logros de élite, Oneiromancer te ayudará.
    - (Condition: Si has completado las tareas del diario de logros de élite:)
      - **Oneiromancer:** Ciertamente...
      - **Oneiromancer:** ¡Ahí!
  - [Choice]: ¿Puedo contarte un chiste?
    - **Oneiromancer:** Oh, me gustan las bromas, adelante.
    - **Player:** ¿Cómo se llama una luna loca?
    - **Oneiromancer:** Una luna loca... Hmm, no lo sé. ¿Qué?
    - **Player:** ¡Un lunático!
    - **Oneiromancer:** ¡Jajajajaja!
    - **Oneiromancer:** ¡Jajaa!
    - **Oneiromancer:** ¡Jajajaja!
    - **Player:** Está bien, está bien. No fue TAN gracioso.

#### Islwyn

- (Condition: Si tienes una semilla de teletransporte de cristal descargada en tu inventario:)
  - (opens=Crystal teleport seed#Charges)
- (Condition: Si no tienes una semilla de teletransporte Crystal descargada en tu inventario (o está parcialmente cargada):)
  - **Islwyn:** ¿Player? ¿Quieres que te vuelva a encantar las semillas de teletransporte de cristal?
  - **Player:** No tengo ninguno de esos.
  - **Islwyn:** Quizás en otro momento.

#### Mieliki Tapio

- **Mieliki Tapio:** Mieliki envió a Nyriki a un pantano, al sureste de Canifis.
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Quién eres?
    - **Mieliki Tapio:** Mieliki es un alquimista. El estúpido marido de Mieliki, Nyriki, busca chinchompas gigantes para conseguir productos químicos para Mieliki.
    - **Mieliki Tapio:** Nyriki necesita ayuda humana porque es estúpido. Utilice el portal Mieliki, en esta tienda, para acudir a él ahora.
    - (initial)
  - [Choice]: ¿Puedes teletransportarme?
    - (Condition: Si estás cerca:)
      - **Mieliki Tapio:** ¡Mieliki está trabajando! Utilice el portal.
    - (Condition: Si no estás cerca:)
      - **Mieliki Tapio:** ¡Mieliki está trabajando! Ven a la tienda de Mieliki en Gnome Stronghold y utiliza el portal.
    - (initial)
  - [Choice]: Gracias.
    - **Mieliki Tapio:** Muy bien, humano. Atarearse.

#### Morvran

- **Player:** ¿Hola?
- (Condition: Si estás cerca:)
  - **Morvran:** Si vas a molestarme con tu parloteo, al menos podrías tener la decencia de hacerlo en mi cara. Ven aquí.
- (Condition: Si no estás cerca:)
  - **Morvran:** No tienes nada que hacer en mi cabeza. Mis secretos no son para tus ojos. Salir.
  - **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo.
  - **Morvran:** Tienes demasiado miedo para buscarme en persona, ¿eh? Bueno, ¿qué es?
  - [Menu]: Selecciona una opción
    - [Choice]: Necesito otra tarea.
      - (ver|Morvran)
    - [Choice]: Er... Nada.
      - (end)

#### Urluk

- (ver|Urluk)

#### Laniakea

- **Player:** Laniakea?
- (Condition: Si estás cerca:)
  - **Laniakea:** ¿Por qué desperdiciarías las runas para contactarme cuando estás tan cerca?
- (Condition: Si no estás cerca:)
  - **Laniakea:** No tienes nada que hacer en mi cabeza. Mis pensamientos son míos.
  - **Plyer:** Es Player. Estoy usando mi magia para comunicarme contigo.
  - **Laniakea:** Es una pena. Hubiera sido bueno verte. Bueno, ¿qué es?
  - [Menu]: Selecciona una opción
    - [Choice]: Necesito otra tarea.
      - (ver|Laniakea)
    - [Choice]: Er... Nada.
      - (end)

#### Polletix


##### Antes de hablar con ella en el Jardín de Kharid

- **Player:** ¿Hola?
- **Polletix:** Uf, otro.
- **Player:** ¿Qué?
- **Polletix:** Oh, nada. ¿En qué puedo ayudar?
- **Player:** Oh, bueno, alguien dijo algo sobre unos druidas en el desierto, y en lugar de ir allí pensé en ver qué estaba pasando primero.
- **Polletix:** Mira, si quieres ayudar, tal vez vengas y conversemos en lugar de meterte en mi cabeza.
- **Player:** Bueno, lo hice-
- **Polletix:** ¡Buenos días!
- **Player:** ¿Hola?
- **Player:** ¿Holaaaa?
- No hay nadie allí excepto el vacío frío y oscuro de tu propia mente.

##### Después de hablar con ella en el Jardín de Kharid y pedirle que cultive hierbas.

- **Player:** Hola, ¿Polletix?
- (Condition: Si estás cerca:)
  - **Polletix:** ¿Qué estás haciendo?
  - **Player:** Bueno, solo estaba-
  - **Polletix:** Puedo verte. Estás justo aquí.
  - **Player:** Oh, yo-
  - **Polletix:** Ahora, si quieres hablar te sugiero que vengas y lo hagas en persona, en lugar de este mal uso de la magia.
- (Condition: Si no estás cerca:)
  - **Polletix:** Hola aventurero. Este es un pequeño truco ingenioso. ¿Cómo puedo ayudar?
  - **Player:** Me preguntaba qué hierba querías plantar hoy.
  - **Polletix:** Oh, hoy me gustaría que plantes y coseches: semilla [Herb type].
  - **Player:** ¡Genial, gracias!

#### The Raptor

- **Player:** ¿Hola? ¿Es este the Raptor?
- **The Raptor** No tienes nada que hacer en mi cabeza. Mis pensamientos son míos.
- **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo.
- **The Raptor** Explícate.
  - [Menu]: Selecciona una opción
    - [Choice]: Necesito otra tarea.
      - (ver|The Raptor)
    - [Choice]: Er... Nada.
      - (end)

### Random NPC dialogue


#### Lumbridge Sheep

- **Player:** ¿Hola?
- **Lumbridge Sheep:** Baaaa.
- **Player:** ¿Eh? Bueno.
- **Player:** ¡Baa, baaaa, BAA!
- **Lumbridge Sheep:** ¿Baaa?

#### Lumbridge Sage

- **Player:** ¡Hola!
- **Lumbridge Sage:** ¿Qué? ¿Quién es ese?
- **Player:** Jeje... ejem...
- **Player:** ¡Esta es la voz de tu conciencia! Has sido un chico muy travieso, ¿no?
- **Lumbridge Sage:** ¿Qué? ¡No, no lo he hecho!
- **Player:** ¡Sabes de lo que estoy hablando! ¡No mientas!
- **Lumbridge Sage:** ¡Está bien, está bien! Lo siento, no lo volveré a hacer nunca más.
- **Player:** Si lo vuelves a hacer, estarás en serios problemas.

#### Wise Old Man

- **Player:** Hola.
- (el player es golpeado por un hechizo de Ola de Fuego, pero no sufre daño).
- **Player:** ¡Ay!
- **Wise Old Man:** ¡Mantén tus magias extranjeras fuera de mi cabeza!

#### My Arm


##### Antes de completar la gran aventura de My Arm

- **Player:** Hola.
- **My Arm:** ¿Voz en mi cabeza?
- **Player:** ¿Eh?
- **My Arm:** Vete voz, deja My Arm.
- **Player:** Esa es la conversación más extraña que he tenido en mucho tiempo.

##### Después de completar la gran aventura de My Arm

- **Player:** Hola.
- **My Arm:** ¿Eres tú, Player? My Arm puede oírte pero no estás aquí.
- **Player:** Estoy usando magia para hablar contigo. ¿Cómo está la hierba gotosa?
- **My Arm:** Lo siento, Player, pero My Arm no sabe magia, así que My Arm no puede responder.

#### Hans

- **Player:** Hola.
- **Hans de Lumbridge:** ¡Oh! ¿Quién eres?
- **Player:** ¡Soy un caballero valiente! ¡Vengo a matar a cualquiera que esté en las cercanías del Castillo Lumbridge!
- **Hans de Lumbridge:** ¡Aaaaargh! ¡Huye, huye!
- **Player:** Jeje. ¡Tonto!

#### Evil Dave

- **Player:** ¡Hola!
- **Evil Dave:** ¡Vaya! ¡Una voz en mi cabeza! ¿Qué deseas?
- **Player:** ¡Soy tu malvado maestro!
- **Evil Dave:** ¡Estás usando magia oscura para contactarme! ¡Eso es TAN malvado! ¿Cuál es tu orden, oh Maestro?
- **Player:** ¡Constrúyeme un ejército digno de Zamorak!
- **Evil Dave:** ¡Sí, oh maestro! ¡Tan pronto como haga funcionar esta cosa de invocación, mi ejército de malvados UNDEAD CHAOS ZOMBIE DEMON ASSASSINS OF DARKNESS OF DARKNESS invadirá el mundo! ¡Mwuhahahahaaa!

#### Clay Golem

- **Player:** ¡Hola!
- **Clay Golem:** ¡Error! Desajuste de percepción (auditiva/visual).
- **Player:** ¡No te preocupes, Golem! ¡Es Player!
- **Clay Golem:** Lo siento. Puedo oírte pero no verte. Tendré que examinarme los ojos.
- **Player:** No, no puedes verme porque no estoy allí. ¡Me estoy contactando contigo por arte de magia!
- **Clay Golem:** Si no estás aquí, entonces no puedo escucharte. Tendré que examinarme los oídos.
- **Player:** No te preocupes, Golem.

#### General Wartface

- **Player:** ¡Hola!
- **General Wartface:** ¿Qué quieres, Bentnoze?
- **General Wartface:** ...
- **General Wartface:** Entonces, ¿quién dijo algo? ¿Quién ese?
- **Player:** ¡Es Player! ¡Te estoy hablando por arte de magia!
- **General Wartface:** ¡Hola, Player!
- **General Wartface:** Bentnoze, ¡[he/she] está aquí! ¡Escucho [him/her] en la cabeza!
- **General Wartface:** ...
- **General Wartface:** ¡No estoy loco, Bentnoze! [He/She] hablame por arte de magia!
- **General Wartface:** ...
- **General Wartface:** ¡Cállate Bentnoze! ¡Eres estúpido! ¡Solo estás celoso! Player ¡Habla conmigo, no tú!
- **General Wartface:** ...
- **General Wartface:** ¡Cállate Bentnoze! ¡Eres estúpido!
- **General Wartface:** ...
- **General Wartface:** ¡CÁLLATE!

#### Drunken Dwarf

- **Player:** Hola.
- **Drunken Dwarf:** ¡Waaahaaay! ¡Es Player! *hip* ¡Maate!
- **Player:** ¿Cómo van las cosas?
- **Drunken Dwarf:** Creo que estoy borracho demasiado.
- **Player:** Entonces, lo mismo de siempre.
- **Drunken Dwarf:** ¿Quieres kebab?
- **Player:** Uh, no, estoy bien, gracias.
- **Drunken Dwarf:** Bueno, oym goona pasa ahora. ¡Ten uno conmigo!
- **Player:** Oh, está bien.
- **Player:** ...
- **Player:** Erm, adiós.

#### Al Kharid Camel

- **Player:** ¡Hola!
- **Al Kharid Camel:** ¡Hola!
- **Player:** ¿Un camello?
- **Al Kharid Camel:** Bueno, esto es grandioso, cariño. ¡Qué lindo es conocerte!
- **Player:** Gracias. Estoy encantado de conocerte también.
- **Player:** Espera un minuto. ¿Cómo te hablo sin camuleto?
- **Al Kharid Camel:** Querida, soy un camello; ¿Cómo debería saberlo?
- **Player:** Mmmm. Supongo que este hechizo debe llegar directamente a tu mente, por lo que no es necesario que el lenguaje se interponga en tu camino.
- **Al Kharid Camel:** Creo que estoy algo confundido.
- **Al Kharid Camel:** ¿Puedo preguntar cómo me contactó?
- **Player:** Sólo estoy usando uno de los hechizos lunares.
- **Al Kharid Camel:** Dios mío, Dios mío. ¡Estos jóvenes de hoy y sus novedosos aparatos!

#### Sandwich Lady

- **Player:** ¿Hola?
- **Sandwich Lady:** ¿Qué quieres de té? ¡Y más vale que no sea una baguette!
- **Player:** ...
- **Player:** ... ...
- **Sandwich Lady:** ¡No me ignores, Player!
- **Player:** ...
- **Sandwich Lady:** ¿Por qué la gente no me habla?
- **Player:** ...
- **Sandwich Lady:** ¡Te daré una paliza!
- **Player:** Uhh, urr, ¿un sándwich, por favor?
- **Sandwich Lady:** ¡Está bien, querida! ¡Toodle-oo!

#### 1337mage43

- **Player:** ¿Hola?
- **1337mage43:** ¿Hola?
- **Player:** ¡Oye, comencé la conversación!
- **1337mage43:** No, no lo hiciste. ¡Sal de mi hechizo!
- **Player:** ¡No! ¡Sal de mi hechizo!
- **1337mage43:** Bebé llorón.
- **Player:** ¡Qué! ¡No soy un llorón, llorón!
- **1337mage43:** ¡Te estoy denunciando!
- **Player:** ¡Oh, qué miedo!
- **Player:** Idiota.

#### Osman

- **Player:** ¿Hola?
- **Osman:** ¡Revélate!
- **Player:** ¡Ja, llámate a ti mismo un maestro de espías! ¡No puedes verme!
- **Osman:** ¡Ahh, estoy alucinando! ¡Debemos reducir el consumo de sq'irks!

#### Helpline Assistant

- **Player:** ¿Hola?
- **Helpline Assistant:** Te comunicaste con la línea de ayuda de comunicación lunar. Lamento que no podamos responder tu pregunta telequinética en este momento. Nuestros horarios de apertura están cuidadosamente organizados para que coincidan con su actividad. Si tiene una emergencia, tiene
- **Helpline Assistant:** nuestras más profundas disculpas. Que tenga un lindo día. Adiós.
- **Player:** Típico.

#### Father Urhney

- **Player:** ¿Hola?
- **Father Urhney:** ¡Por fin! ¡La voz de Saradomin! ¡Mis años de meditación han dado sus frutos!
- **Player:** Eh...
- **Father Urhney:** ¡Oh, poderoso Saradomin! ¿Cuál es tu mensaje para mí?
- **Player:** ¡Deja de quedarte sentado en una casa en un pantano y ve y haz algo útil!
- **Father Urhney:** ¡Oh, gracias Saradomin! ¡Meditaré sobre lo que significa este mensaje!

#### Romeo (histórico)

- **Player:** ¿Hola?
- **Romeo:** Oh, hola. Suenas encantador.
- **Player:** ¿Perdón?
- **Romeo:** Suenas encantador. Tienes un hermoso... tono en tu voz.
- **Player:** ¿Tang? Es Romeo, ¿no?
- **Romeo:** ¿Puedo compararte con unos trozos de piña?
- **Player:** No, Romeo. Adiós.

#### Blurberry

- **Player:** ¿Hola?
- **Blurberry:** ¡Blurberry aquí! ¿Puedo ayudar?
- **Player:** Jeje. Sí puedes. Estoy buscando un Gnome. Gnome Compañeros.
- **Blurberry:** Está bien, preguntaré. ¡Cállate todo el mundo! ¿Hay algún Gnome Mates aquí? ¿Alguien entró con Gnome Mates?
- Se oyen risas de fondo.
- **Blurberry:** Ooooh, ¿quién es? ¡Te atraparé!
- **Player:** Jajaja.

#### Aris

- **Player:** Hola.
- **Aris:** Porque puedo predecir el futuro.
- **Player:** ¿Eh?
- **Aris:** Esa es la respuesta a tu siguiente pregunta.
- **Player:** ¿Pero cómo supiste lo que te preguntaría?
- **Aris:** Porque puedo predecir el futuro.
- **Player:** Ah, eso es muy inteligente.
- **Aris:** Gracias. Ah, y ten cuidado con el Wilderness. Esta noche no es tu noche.
- **Player:** ¡Salud!

#### Hakeem the Sandsweeper

- **Player:** ¡Hola! ¿Quién es?
- **Hakeem:** Hakeem.
- **Player:** ¿Hakeem quién?
- **Hakeem:** Soy Hakeem the Sandsweeper.
- **Player:** ¿Barres arena?
- **Hakeem:** ¡Por supuesto que sí! Soy el mejor barrendero de este lado del Lum.
- **Player:** ¿Hay más de ustedes?
- **Hakeem:** ¡Tenemos un sindicato, amigo! Siempre hay arena que barrer.
- **Player:** De hecho. Mmm, tengo que irme.

#### Hombre

- **Player:** Hola.
- **Hombre:** ¡Disculpe!
- **Player:** Oh, lo siento, ¿qué hice?
- **Hombre:** ¿No ves que estoy en el baño?
- **Player:** Espera un minuto... ¿un baño?
- **Hombre:** Sí. Un baño.
- **Player:** Correcto. Oh, hombre, ¿no te limpiaste las manos?
- **Hombre:** Supéralo.
- (Condition: Si contacta al hombre en el baño por primera vez:)
  - {{RSFontAchievement|Is This a Bad Time?}}

#### Party Pete

- **Player:** ¿Hola?
- **Party Pete:** ¡Oye! ¡Fiesta, fiesta, fiesta!
- **Player:** Eh, ¿Party Pete?
- **Party Pete:** ¡Sí! ¡La fiesta es el nombre y la fiesta es el juego! En realidad es una profesión de tiempo completo. No puedes detener la fiesta.
- **Player:** Party Pete. ¿Alguna vez has querido simplemente relajarte?
- **Party Pete:** ¡Relájate, no lo hagas! ¡Sí! ¡Manía de fiesta! ¡Sí!
- **Player:** Adiós fiesta.
- **Party Pete:** ¡Puedes abandonar la fiesta, pero la fiesta nunca te dejará a ti! ¡Fiesta!

#### Bob

- **Player:** ¿Hola?
- **Bob:** Hola.
- **Player:** ¡Ah, Bob! He querido hacerte algunas preguntas
- **Bob:** Está bien, pero date prisa.
- **Player:** Bueno, ¿de dónde vienes? ¿Por qué deambulas por Gielinor? ¡He oído muchos rumores sobre tu pasado!
- **Bob:** Es realmente simple...
- **Bob:** *tos* *tos*.
- **Player:** ¿Estás bien?
- **Bob:** *tos* Estoy *tos* solo...
- **Player:** Bob?
- **Player:** ¡Bob! ¡No mueras! ¡Nooooo!
- **Player:** ...
- **Bob:** Lo siento, tuve una bola de pelo.
- **Player:** ¡Uf! Eso es desagradable.
- **Bob:** Oye, es normal. ¡Me voy ahora!
- **Player:** Bob?
- **Player:** Oh no, Bob, por favor no te vayas.
- **Bob:** Adiós.

#### Captain Cain

- **Player:** ¿Quién es ese?
- **Captain Cain:** ¿Qué? ¡Qué insolencia! ¡Cómo te atreves a hablar así, pobre excusa para el regate duende!
- **Player:** ¿Qué?
- **Captain Cain:** ¡Déjame veinte!
- **Player:** Está bien, está bien. Los estoy haciendo ahora.
- **Player:** ...
- **Captain Cain:** ¡Mentiroso!
- **Player:** Espera un minuto, no tengo que aguantar esto. ¡Haces veinte!
- **Captain Cain:** ¡Por qué debería hacerlo!
- **Player:** Erm, sí. ¡Adiós!

#### Homúnculo

- **Player:** ¿Hola?
- **Homúnculo:** Es Player. ¿Cómo estás?
- **Player:** Bien, gracias. ¿Y tú?
- **Homúnculo:** Los alquimistas regresan el otro día. Yo los convierto en animales.
- **Player:** ¡No! ¿En realidad?
- **Homúnculo:** Sí, ¡hice un uniman y un pollueloquimista!
- **Player:** ¡Buen trabajo!

#### Agente KGP #1

- **Player:** ¿Hay alguien ahí?
- **Agente de KGP:** ¡INTRUSO! ¡Alerta roja! ¡Fijar con listones los encerados de escotilla! ¡BUCEO, BUCEO, BUCEO!
- **Player:** Err, tal vez vuelva a llamar más tarde.

#### Agente KGP #2

- **Player:** Hola.
- **Agente de KGP:** Los peces no pueden subirse al tren de la salsa.
- **Player:** ¿Perdón?
- **Agente de KGP:** ¿El cíclope no puede ver su morsa interior?
- **Player:** ¿Es este código?
- **Agente de KGP:** ¿Avanzar como un pato hacia un atardecer de caballa desmenuzada?
- **Player:** Ya me voy.
- **Agente KGP:** ¿La sardina se está saliendo de la lata?

#### Lumbridge Cow

- **Player:** ¿Hola?
- **Lumbridge Cow:** Muuuuuuuu.
- **Player:** ¡Oye, sé que puedes hablar!
- **Lumbridge Cow:** Muuuu.
- **Player:** ¡Deja de ignorarme!
- **Lumbridge Cow:** Mira, amigo. ¡Déjame en paz!
- **Player:** ¡Hablaste! ¡Hablaste!
- **Lumbridge Cow:** Muuuu.
- **Player:** Creo que comeré un poco de carne esta noche.

#### Zanik (antes de The Mighty Fall)

- {{Trandom}}
  - ''Conversación 1:
    - **Player:** ¿Hola?
    - **Zanik:** Player?
    - **Player:** ¡Me estoy contactando contigo por arte de magia!
    - **Zanik:** Hola Player, ¿conoces a alguien llamado Evil Dave? Me está contando sobre su plan para dominar el mundo, pero no estoy seguro de si habla en serio.
    - [Menu]: Selecciona una opción
      - [Choice]: ¡Es un mago malvado! ¡Tienes que detenerlo!
        - **Player:** ¡Es un mago malvado! ¡Tienes que detenerlo!
        - **Zanik:** Bien, ya lo tengo.
        - **Zanik:** ¡Detente ahora mismo, Evil Dave! ¡Si quieres conquistar el mundo, primero tendrás que superarme!
        - **Zanik:** ¡Está lanzando un hechizo, Player! ¡Ha hecho un círculo mágico y va a invocar algo! ¡Tengo que interrumpir la magia de alguna manera!
        - [Menu]: Selecciona una opción
          - [Choice]: ¡Haz que se equivoque en las palabras!
            - {{Transcript missing}}
          - [Choice]: ¡Interrumpe el círculo mágico!
            - **Player:** ¡Interrumpe el círculo mágico!
            - **Zanik:** ¡Ahí! ¡El círculo se ha roto! Aunque algo todavía está sucediendo...
            - **Zanik:** ¡Evil Dave se ha convertido en un pez! Él está dando vueltas y-
            - **Zanik:** Oh, ha regresado.
            - **Zanik:** Dice que va a ir a acostarse. Creo que sus malvados planes se han frustrado por el momento.
          - [Choice]: Sólo déjalo lanzar el hechizo
            - {{Transcript missing}}
      - [Choice]: Creo que es inofensivo.
        - **Player:** Creo que es inofensivo.
        - **Zanik:** ¿En serio? Me está pidiendo que me una a su malvado plan. Dice que podría ser su 'Asesino de la oscuridad portador de la muerte malvado'.
        - [Menu]: Selecciona una opción
          - [Choice]: Serías un gran asesino de la oscuridad.
            - **Player:** Serías un gran asesino de la oscuridad.
            - **Zanik:** ¡Ja! Apuesto que lo haría. Me paraba en un tejado, envuelto en una capa negra, una ballesta brillando a la luz de la luna mientras mi objetivo se movía desprevenido abajo...
            - **Zanik:** Um, si fuera malvado, por supuesto.
            - **Zanik:** Lo cual no soy.
            - **Zanik:** Creo que ya llevo bastante tiempo con Evil Dave. Te hablaré en otro momento, Player.
          - [Choice]: No vas a unirte a él, ¿verdad?
            - **Player:** No vas a unirte a él, ¿verdad?
            - **Zanik:** Por supuesto que no. ¡No me pillarás siendo parte de ningún plan malvado!
            - **Zanik:** Bueno, excepto esa vez, por supuesto. Pero no quiero hablar de eso.
            - **Zanik:** De todos modos, creo que debería dejar a Evil Dave con sus planes. Nos vemos por ahí, Player.
  - ''Conversación 2:
    - **Player:** ¿Hola?
    - **Zanik:** ¿Player? Oldak, algo está pasando. Tengo Player en mi cabeza.
    - **Player:** Me estoy contactando contigo por arte de magia.
    - **Zanik:** Mmm, está bien. Hola Player, ¿sabes qué es un 'vórtice de fatalidad abisal'?
    - **Zanik:** Porque eso es lo que Oldak dice que creó en su laboratorio.
    - **Zanik:** Se está haciendo más grande, creo que va a explotar.
    - [Menu]: Selecciona una opción
      - [Choice]: ¡Huye!
        - **Player:** ¡Huye!
        - **Zanik:** ¡Está bien! ¡Oldak! ¡Grubfoot! ¡Salgamos de aquí!
        - **Zanik:** Grubfoot!
        - **Zanik:** Grubfoot está atrapado debajo de una cosa. Voy a volver por él.
        - **Zanik:** ¡Oh, no!
        - ...
        - **Zanik:** Terminé en otro lugar. Las paredes son rojas... Creo que esto es el abismo.
        - **Zanik:** Puedo ver un portal, pero hay algunos monstruos entre él y yo.
        - [Menu]: Selecciona una opción
          - [Choice]: Deberías luchar contra ellos.
            - **Player:** Deberías luchar contra ellos.
            - **Zanik:** Vale, no tengo mi ballesta, pero tengo una dagger. Aquí va...
            - **Zanik:** ¡Ahí! No eran tan duros como parecían. He llegado al portal.
            - **Zanik:** ¡Estoy en casa! Y Grubfoot está bien. Eso es un alivio.
            - **Zanik:** Está bien, voy a ayudar a Oldak a limpiar el desorden. Nos vemos por ahí, Player.
          - [Choice]: Deberías escabullirte de ellos.
            - {{Transcript missing}}
      - [Choice]: ¡Tienes que cerrarlo!
        - **Player:** ¡Necesitas apagarlo!
        - **Zanik:** Sí, eso es lo que estaba pensando.
        - **Zanik:** ¡Oye, Oldak, Player cree que deberías cerrarlo!
        - **Zanik:** ¡Oh, no! ¡Oldak!
        - **Zanik:** ¡Oldak está paralizado!
        - **Zanik:** ¡No recuerdo cómo apagarlo! ¿Qué dijo Oldak? Se trataba de desalinear el inyector de runas o invertir la polaridad en el inversor de polaridad.
        - [Menu]: Selecciona una opción
          - [Choice]: ¡Desalinee el inyector!
            - **Player:** ¡Desalinee el inyector!
            - **Zanik:** ¡Está bien! Aquí va...
            - **Zanik:** ¡Funcionó! ¡Está apagado! Pero ha dejado esta porquería roja por todo el suelo.
            - **Zanik:** Oldak está raspando un poco en un frasco de muestra. Un resultado muy interesante, afirma.
            - **Zanik:** De todos modos, eso parece el final de ese vórtice abismal de fatalidad. Nos vemos en Player.
          - [Choice]: ¡Invierte la polaridad!
            - **Player:** ¡Invierte la polaridad!
            - **Zanik:** Bien, voy a darle la vuelta a esta parte...
            - **Zanik:** Vaya...
            - **Zanik:** Eso es lo más sorprendente... es... indescriptible...
            - **Player:** ¿Qué fue? ¿Qué pasó?
            - **Zanik:** ¡No puedo describirlo! ¡Es literalmente indescriptible!
            - **Zanik:** De todos modos, ya no está.
            - **Zanik:** Creo que debería dejar que Oldak y Grubfoot trabajen. Nos vemos por ahí, Player.
  - ''Conversación 3:
    - **Player:** ¿Hola?
    - **Zanik:** ¿Player? ¿Dónde estás? No puedo verte en el pantano.
    - **Player:** ¡Me estoy contactando contigo por arte de magia!
    - **Zanik:** ¡Oh! Estoy explorando Morytania y...
    - **Zanik:** ¡Vaya! ¡Me estoy resbalando! ¡Guau!
    - **Player:** ¿Zanik? ¿Estás bien?
    - **Zanik:** ¡Me caí en el pantano! ¿Qué debo hacer Player?
    - [Menu]: Selecciona una opción
      - [Choice]: ¡Enfréntate con tu ballesta!
        - **Player:** ¡Enfréntate con tu ballesta!
        - **Zanik:** Está bien, lo intentaré...
        - **Zanik:** Allí, la garra está atrapada en un árbol. Estoy saliendo...
        - **Zanik:** Aterricé en un arbusto y... ¡oye, hay alguien más aquí! ¡Ey! ¡Leñador! ¡Por aquí!
        - **Zanik:** Está girando hacia aquí y... oh. Oh, oh. Creo que es un zombi.
        - [Menu]: Selecciona una opción
          - [Choice]: ¡Corre por ello!
            - {{Transcript missing}}
          - [Choice]: ¡Puedes tomarlo! ¡Luchar!
            - **Player:** ¡Puedes aceptarlo! ¡Luchar!
            - **Zanik:** ¡No es tan difícil!
            - **Zanik:** ¡Se le ha caído el brazo, pero todavía viene hacia mí!
            - **Zanik:** Ahora le corté ambos brazos, ¡pero todavía intenta morderme!
            - **Zanik:** ¿Qué? ¡Está saltando hacia mí con una sola pierna! ¿Por qué no muere ya?
            - **Zanik:** Ahí. Le corté todas las extremidades y lo pateé al pantano. ¡Ningún zombi está a salvo de Zanik de Dorgeshuun!
            - **Zanik:** No creo que tenga problemas con nada más en este pantano. ¡Gracias por la ayuda, Player! ¡Ya nos veremos!
      - [Choice]: ¡Intenta nadar hasta la orilla!
        - **Player:** ¡Intenta nadar hasta la orilla!
        - **Zanik:** ¡Creo que puedo hacer eso! El banco es sólo...
        - **Zanik:** Oye, ¿qué es eso? Hay una cabeza asomando del agua...
        - **Zanik:** ¡Eek! Tentáculos! ¡Me tiene!
        - [Menu]: Selecciona una opción
          - [Choice]: Attack el tentáculo!
            - {{Transcript missing}}
          - [Choice]: Attack la cabeza!!
            - **Player:** ¡Attack la cabeza!
            - **Zanik:** Espero que mi ballesta todavía esté lo suficientemente seca...
            - **Zanik:** ¡Jaja! ¡Entiendo! ¡Perno de ballesta en el ojo!
            - **Zanik:** No pareció dolerme demasiado, pero me dejó ir. He vuelto al banco. Creo que puedo ver una salida del pantano desde aquí.
            - **Zanik:** ¡Gracias por tu ayuda, Player! Hablaré contigo en otro momento.

### Redial '[NPC]'

- (Condition: Si el player aún no ha llamado a un NPC:)
  - Último contacto no encontrado. Por favor llame nuevamente.
  - (ventana emergente)
    - {{popup|Last contact not found. <br>Please call again.|warning=yes}}
- (Condition: Si el player ha llamado a un NPC antes:)
  - Volviendo a marcar '[NPC]'...
  - (Condition: Sin suficientes runas:)
    - No tienes suficientes runas [rune type] para lanzar este hechizo.
    - (ventana emergente)
      - {{popup|You do not have enough [rune type]<br>runes to cast this spell.|warning=yes}}
  - (Condition: Con suficientes runas:)
    - (removes=runes)
    - (continuea)
