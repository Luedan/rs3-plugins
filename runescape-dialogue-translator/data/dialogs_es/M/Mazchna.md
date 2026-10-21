# Mazchna

- **Original Wiki Page**: [Transcript:Mazchna](https://runescape.wiki/w/Transcript%3AMazchna)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Missing some standard Slayer Master dialogue and being offered the special challenge. Need to clarify how dialogue changes when rings are visited in a different order.}}
{{ToC|limit=1}}

### Talking to Mazchna in Canifis

- **Mazchna:** 'Hola, ¿y qué buscas entonces?
  - *Si has recibido alguna asignación Slayer de cualquier Slayer Master*
    - Necesito otra tarea.
      - (continue|Get task)
  - ¿Tienes algo para intercambiar?
    - **Player:** ¿Tienes algo para intercambiar?
    - **Mazchna:** Tengo una amplia selección de equipos Slayer; ¡eche un vistazo!
      - *(Se abre la interfaz del equipo Slayer)*
  - *Si has recibido alguna asignación Slayer de cualquier Slayer Master*
    - Estoy aquí para discutir cualquier recompensa para la que pueda ser elegible.
      - Ver recompensas.
        - *(Se abre la interfaz de recompensas Slayer)*
      - ¿Cómo gano puntos cooperativos para gastarlos en recompensas?
        - **Mazchna:** Obtendrás puntos de recompensa cooperativa si completas al menos la mitad de tu contribución a una tarea con un amigo. Eso significa que debes estar en un grupo la mayor parte del tiempo que estés trabajando en la tarea, ¡pero no importa si tu amigo te gana en la mayoría de las muertes! Aún habrás estado en un grupo durante la mayor parte de tu contribución, por lo que aún tendrás derecho a un punto de recompensa cooperativa.
          - Ver recompensas.
            - *(Igual que arriba)*
          - ¿Dónde puedo usar las recompensas cooperativas de comida y pociones?
            - *(Igual que a continuación)*
          - Eso es todo, gracias.
      - ¿Dónde puedo usar las recompensas cooperativas de comida y pociones?
        - **Mazchna:**  Las recompensas se pueden usar en la mayoría de las áreas que comúnmente te enviamos para completar tus tareas.
          - Ver recompensas.
            - *(Igual que arriba)*
          - ¿Cómo gano puntos cooperativos para gastarlos en recompensas?
            - *(Igual que arriba)*
          - Eso es todo, gracias.
  - Eh... nada...
    - **Player:** Eh... nada...

### Get task

- **Player:** Necesito otra tarea.
- (Condition: Con una tarea Slayer en curso:)
  - **Mazchna:** Todavía estás cazando a [task]; Vuelve cuando hayas terminado tu tarea.
- (Condition: Sin una tarea Slayer en curso:)
  - (Condition: Condición desconocida:)
    - **Mazchna:** En realidad eres muy fuerte. ¿Estás seguro de que no quieres que Laniakea en Anacronia te asigne una tarea?
    - [Menu]: Selecciona una opción
      - [Choice]: No, está bien, te encargaré una tarea.
        - **Player:** No, está bien, te encargaré una tarea.
        - [Menu]: ¿Cambiar su tarea Slayer asignada?
          - [Choice]: [número] [task] (predeterminado)
            - (Condition: Con Slayer Introspection aprovechado:)
              - [Menu]: ¿Modificar su tarea Slayer asignada?
                - [Choice]: [número] [task] (predeterminado)
                  - (continue)
                - [Choice]: [número] [task] (min)
                  - (continue)
                - [Choice]: [número] [task] (máx.)
                  - (continue)
            - **Mazchna:** Excelente, lo estás haciendo muy bien. Tu nueva tarea es matar a [número] [task].
            - [Menu]: Selecciona una opción
              - [Choice]: ¿Tienes algún consejo para mí?
                - **Player:** ¿Tienes algún consejo para mí?
                - (continue|Assignment advice)
              - [Choice]: ¡Vale, genial!
                - {{Transcript missing}}
              - [Choice]: No gracias. (Tarea clara, cuesta 30 puntos Slayer)
                - {{Transcript missing}}
          - [Choice]: [número] [task] (cuesta 1 token Slayer)
            - {{Transcript missing}}
      - [Choice]: Ah, está bien, entonces iré a Laniakea.
        - **Player:** Oh, está bien, entonces iré a hablar con Laniakea.
      - [Choice]: Te aceptaré una tarea y no me la vuelvas a preguntar.
        - {{Transcript missing}}

### Activating the enchanted gem with Mazchna as the current Slayer Master

- **Mazchna:** Hola, Player, ¿en qué puedo ayudarte?
  - ¿Cómo estoy hasta ahora?
    - **Player:** ¿Cómo me va hasta ahora?
    - **Mazchna:** Actualmente estás asignado a matar a [assigned creatures]; sólo faltan X más.
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
    - **Mazchna:** Mi nombre es Mazchna; Soy un Slayer Master.
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
    - **Mazchna:** Me encontrarás en Canifis. Estaré aquí cuando necesites una nueva tarea.
      - ¿Cómo estoy hasta ahora?
        - *(Igual que arriba)*
      - ¿Quién eres?
        - *(Igual que arriba)*
      - ¿Tienes algún consejo para mí?
        - *(Igual que a continuación)*
      - Eso es todo gracias.
  - ¿Tienes algún consejo para mí?
    - **Player:** ¿Tienes algún consejo para mí?
    - **Mazchna:** El último [assigned creature] que maté descubrí que [weapons] los derribó de manera efectiva.
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
    - **Player:** Nada realmente.

### NPC Contact

- **Player:** ¿Hola?
- **Mazchna:** 'Hola, ¿quién es ese?
- **Player:** Soy Player. Estoy usando magia para comunicarme contigo.
- **Mazchna:** Extraño. Anda entonces, ¿qué quieres?
*Durante Mientras Guthix duerme antes de reclutar a Mazchna*
- **Player:** ¡Necesito hablarte sobre Lucien!
- **Mazchna:** ¿Lucien? Pensé que no tramaba nada bueno, pero no he oído mucho últimamente.
- **Player:** Su poder está creciendo y debemos detenerlo. ¿Estaría interesado en unirse a un pequeño grupo encargado de hacerlo?
- **Mazchna:** Tengo algunas razones personales para asegurarme de que sus planes fracasen... Por supuesto, cuenta conmigo. Soy prácticamente inmortal, por lo que el peligro para ti es una diversión para mí. Espero con ansias un baño de sangre.
*Hablando con Mazchna otra vez*
- **Player:** ¡Necesito hablarte sobre Lucien!
- **Mazchna:** Controla tu entusiasmo, ya acepté ayudarte. Si me molestan demasiado, puedo cambiar de opinión.
- *(Termina el diálogo)*
- *Pregunta sobre otra cosa*
  - Necesito otra tarea.
    - **Player:** Necesito otra tarea.
    - **Mazchna:** Todavía estás cazando a [assigned creature]; Vuelve cuando hayas terminado tu tarea.
  - *Eh... Nada...*
    - **Player:** Er... Nada...
    - *(Termina el diálogo)*
- pregunta sobre otra cosa
  - Necesito otra tarea.
    - *(Igual que arriba)*
  - Eh... nada...
    - *(Igual que arriba)*
*Si Player está muy cerca de Mazchna*
- **Player:** ¿Hola?
- **Mazchna:** 'Hola, ¿quién es ese?
- **Player:** Soy Player. Estoy usando magia para comunicarme contigo.
- **Mazchna:** Bueno, por favor no lo hagas. Si quieres hablar conmigo, hazlo cara a cara. Puedo verte, ¿sabes?
- *(Termina el diálogo)*

### Special Slayer challenge


#### Que le ofrezcan el desafío

{{Transcript missing}}

#### Usando una gema encantada cerca de un anillo de hadas moritano

- **Mazchna:** Hola, Player. ¿Estás en uno de los anillos de hadas ahora?
- (continue)

##### Al oeste de Canifis

- **Player:** Sí, llegué al anillo cerca de la parcela agrícola al oeste de Canifis.
- **Mazchna:** Excelente. ¿Puedes ver algo fuera de lo común?
- **Player:** "Fuera de lo común" puede ser difícil de definir en estos lugares.
- (Action: Una columna de mariposas aparece brevemente pululando alrededor del centro del anillo de hadas.)
- **Player:** ¡Espera! Algo parece estar pasando con el anillo.
- **Mazchna:** ¿Qué está pasando?
- **Player:** El anillo brilla con algún tipo de magia.
- (Action: Un demonio voraz aparece cerca y comienza a atacar a el player.)
- **Mazchna:** Qué extraño. ¡Espera, Player! ¡Estar atento!

##### Después de derrotar al ghoul voraz

- **Mazchna:** ¿Estás bien, Player?
- **Player:** Sí, eso creo.
- **Mazchna:** Hmm, esto no augura nada bueno. Será mejor que continuemos nuestra investigación con los otros anillos en los pantanos y los bosques encantados.

##### Al este de Canifis

- **Player:** Sí, llegué al ring en el bosque encantado al este de Canifis.
- **Mazchna:** Bien hecho, Player. ¿Puedes ver algo de interés?
- **Player:** No lo creo... Espera, ¿qué es eso en el cielo?
- **Mazchna:** ¡Oh, no! ¡Cuidado, Player!
- (Action: Un voraz vampyre aparece en el centro del anillo de hadas.)

##### Después de derrotar al voraz vampyre

- **Mazchna:** ¿Estás bien, Player?
- **Player:** Sí, casi.
- **Machna:** El mal de la zona parece sentirse atraído por tu presencia. Será mejor que terminemos nuestra investigación con el último anillo en los pantanos.

##### Al sur de Canifis

- **Player:** Sí, llegué al ring en Swamplands al sur de Canifis.
- **Mazchna:** Buen trabajo. ¿Está sucediendo algo antinatural?
- **Player:** ¿Cuenta mi posición en un pantano pestilente y supurante?
- **Mazchna:** ¡En realidad no, Player!
- **Player:** Bueno, no veo nada que merezca la pena informar.
- **Mazchna:** Muy bien, entonces te traemos... espera, ¿qué es ese ruido?
- (Action: Un caracol voraz aparece cerca y comienza a atacar a el player.)

##### Después de derrotar al caracol voraz

- ¡Felicitaciones! Has completado tu desafío. Obtienes 2000 de experiencia Slayer y 3 puntos.
- **Mazchna:** Esto no me gusta ni un poco, Player. Estos ataques tienen que ser más que una mera coincidencia. Investigaré más a fondo este asunto. Deberías recuperar tus fuerzas ahora. No olvides venir a verme si quieres un nuevo encargo. Gracias por tu ayuda, Player.

### Assignment advice


#### Espectros aberrantes

- **Mazchna:** Los espectros aberrantes son fantasmas fétidos y viles. El solo olor de ellos te paralizará y te hará daño. Una clavija te ayudará a ignorar su hedor y te hará luchar a pleno rendimiento. Huelelos en la Torre Slayer en Morytania.

#### Ankous

- **Mazchna:** Los Ankous no son ni fantasmas ni esqueletos, sino una combinación de ambos. No se sabe mucho de estas criaturas. Realiza una investigación en las profundidades de la Fortaleza de Seguridad.

#### almas en pena

- **Mazchna:** Las Banshees usan un grito desgarrador para sorprender a sus enemigos; Necesitarás unas orejeras para protegerte de ellos. Sus gritos resuenan por toda la Torre Slayer en Morytania.

#### Basiliscos

- **Mazchna:** Los basiliscos, al igual que las cockatrices, tienen una mirada que paraliza y daña a sus presas. Necesitarás un escudo de espejo para protegerte. Los basiliscos viven en las cuevas Rellekka Slayer, junto con sus parientes cockatrice.

#### Perros del maestro de bestias

- **Mazchna:** El último perro de Beastmaster que maté encontré que los ataques aplastantes lo derribaron de manera efectiva.
- [Los perros del Señor de las Bestias reinan el terror en Mazcab a su antojo.]

#### Mantos de sangre

- **Mazchna:** Los Bloodveld son criaturas extrañas y demoníacas que usan su lengua larga y áspera para alimentarse de casi cualquier cosa que puedan encontrar. Si deseas matar a algunos, viven en la Torre Slayer al noroeste de Canifis.

#### Ratas de salmuera

- **Mazchna:** Las ratas de salmuera se pueden encontrar en cuevas cercanas al mar. No tienen pelo, tienen mal carácter y, en general, son antipáticos. Si has encontrado el tesoro pirata de Olaf, sabrás dónde encontrar estos objetivos.

#### Rastreadores de cuevas

- **Mazchna:** El último rastreador de cavernas que maté descubrí que los ataques cortantes los derribaron de manera efectiva.
- [Los rastreadores de cuevas son pequeños y rápidos, y a menudo se los ve arrastrándose en la mazmorra Rellekka Slayer. Evita su lengua con púas o te envenenarán.]

#### Cockatrices

- **Mazchna:** Las cocatrices, al igual que los basiliscos, tienen una mirada que paraliza y daña a sus presas. Necesitarás un escudo de espejo para protegerte. Si eres lo suficientemente valiente, dirígete a las cuevas Slayer al este de Rellekka.

#### Cocodrilos

- **Mazchna:** Los cocodrilos son reptiles grandes que viven en el Kharidian Desert cerca del agua. Los cocodrilos de río son un desafío mayor que los que se encuentran junto al océano en el sureste.

#### cíclopes

- **Mazchna:** Los cíclopes son gigantes astutos, originarios de las tierras del lejano oriente. Los valientes guerreros del gremio cerca de Burthorpe tienen una colección de ellos; sin embargo, son inmunes a cualquier otra cosa que no sean ataques cuerpo a cuerpo. Otros especímenes no son tan resistentes y se pueden encontrar en God Wars Dungeon.

#### Lagartos del desierto

- **Mazchna:** Los lagartos del desierto son reptiles grandes con piel dura. Tienen sangre fría, por lo que rociarlos con agua helada acabará con ellos después de una dura batalla. Puedes encontrarlos al este de Sophanem.

#### Perros

- **Mazchna:** El último perro salvaje que maté descubrí que los hechizos de agua los derribaron de manera efectiva.
- [Los perros se parecen mucho a los lobos; Son criaturas de manada que cazarán en grupos. He oído que hay temibles perros salvajes debajo de Karamja, o cerca de Ardougne si eres menos aventurero.]

#### guerreros de la tierra

- **Mazchna:** Los guerreros de la Tierra son guerreros elementales unidos por rocas. El agua los elimina fácilmente, así que usa hechizos de ese tipo. Se forman a partir de las rocas debajo de Edgeville.

#### demonios

- **Mazchna:** El último Ghoul que maté encontré que los hechizos de fuego los derribaron de manera efectiva.
- [ &nbsp;]Al norte de Canifis.}}

#### Dragones verdes

- **Mazchna:** Los dragones verdes son los dragones más débiles pero siguen siendo muy poderosos. Cuidado con su aliento de fuego. Estos brutos viven en Wilderness.

#### Gusanos de grosella

- **Mazchna:** Recientemente se han visto gusanos grot en una cueva cerca de Rimmington. Los ejemplares más jóvenes aún no han desarrollado completamente sus mandíbulas y atacarán con una especie de saliva ácida.

#### Gigantes de hielo

- **Mazchna:** El último gigante de hielo que maté encontré que los hechizos de fuego los derribaron de manera efectiva.
- [Al igual que otros gigantes, los gigantes de hielo suelen empuñar armas grandes. Intenta usar hechizos de fuego para derretirlos antes de que puedan golpearte. Se pueden encontrar gigantes de hielo bajo tierra al sur de Port Sarim.]

#### Guerreros de hielo

- **Mazchna:** Los guerreros de hielo son una especie de elemental de hielo. El enano Thurgo vio recientemente algunos en las cuevas al sur de Port Sarim.

#### Magos infernales

- **Mazchna:** Los magos infernales son usuarios de hechizos peligrosos; ten cuidado con sus hechizos Magic y ve debidamente preparado. Se han apoderado de un área de arriba en la Torre Slayer, planeando tu perdición.

#### Jaleas

- **Mazchna:** La última Jelly que maté encontré que los ataques aplastantes los derribaron de manera efectiva.
- [Las jaleas son criaturas gelatinosas desagradables con forma de cubos que absorben todo lo que encuentran. Su toque ácido ataca de la misma manera que muchas magias, así que prepara tu armadura de antemano. Mantienen limpias partes de las cuevas Rellekka Slayer.]

#### Horrores de la jungla

- **Mazchna:** Los horrores de la jungla se pueden encontrar por todo Mos Le'Harmless. Son fuertes, agresivos y luchan en manadas, ¡así que ten cuidado!

#### Watts asesinos

- **Mazchna:** El último Killerwatt que maté encontré que los ataques aplastantes los derribaron de manera efectiva.
- [Los Killerwatts almacenan enormes cantidades de energía en sus cuerpos, que se liberan si se los toca. Necesitarás usar botas fuertemente aisladas para contrarrestar este efecto impactante, además pueden atacar rápidamente con magia y misiles. Para acceder a su plano nublado, deberás explorar Draynor Manor.]

#### Demonios menores

- **Mazchna:** Los demonios menores son criaturas mágicas, por lo que son débiles ante los ataques a distancia. Aunque son relativamente débiles, siguen siendo peligrosos. Taverley Dungeon es el hogar de estas repugnantes criaturas.

#### molaniscos

- **Mazchna:** Los molaniscos son criaturas subterráneas. Puedes encontrarlos en cuevas muy profundas bajo tierra. Escuché que los duendes recientemente tuvieron problemas con algunos, pero usan una campana para atraerlos desde la pared de la cueva.

#### Gigantes de musgo

- **Mazchna:** Descubrí que el último gigante musgoso que maté los hechizos de fuego los derribaron de manera efectiva.
- [Al igual que otros gigantes, los gigantes musgosos suelen empuñar armas grandes. Usa hechizos de fuego para reducirlos a cenizas antes de que puedan dañarte. Curiosamente para los gigantes, se han visto algunos al final de las alcantarillas de Varrock.]

#### Ogros

- **Mazchna:** Los ogros son criaturas brutales y prefieren las mazas y garrotes grandes y contundentes. A menudo atacan sin previo aviso. Al sur de Yanille hay un área gobernada por estos devoradores de hombres.

#### Seres de otro mundo

- **Mazchna:** El último ser de Otro Mundo que maté encontré que las armas arrojadizas lo derribaron de manera efectiva.
- [Los seres de otro mundo son criaturas etéreas, lo que los hace débiles ante los ataques a distancia. Se los puede encontrar rondando Zanaris.]

#### Pirefiends

- **Mazchna:** Los Pyrefiends son seres mágicos de fuego y roca fundida. Son rápidos y ágiles, así que intenta atacarlos con una ballesta y virotes. Puedes encontrar algunos demonios en las cuevas Rellekka Slayer.

#### Babosas de roca

- **Mazchna:** Las babosas de roca son babosas extrañas y pétreas, muchas de las cuales se han visto en la cueva Rellekka Slayer. Tendrás que luchar contra ellos hasta que estén al borde de la muerte, antes de acabar con ellos con sal.

#### Rastreadores sanguíneos

- **Mazchna:** El último rastreador Sanguine que maté encontré un arco y las flechas los derribaron de manera efectiva.
- [Los rastreadores sanguíneos son árboles jóvenes que han sido corrompidos por los Sanguine en Havenhythe.]

#### Serpientes marinas

- **Mazchna:** Las serpientes marinas son largas y resbaladizas, con una mordida venenosa. Los más grandes son más peligrosos, así que vigila tu salud. Viven en islas muy al noroeste o, mejor dicho, en las cuevas marinas de esas islas.

#### Sombras

- **Mazchna:** Las sombras son muertos vivientes: la ciudad de Mort'ton en Morytania está plagada de estas criaturas, así que ayuda si puedes. También hay algunas sombras en Stronghold of Security, pero no aprenderás mucho luchando contra ellas; quédate con Mort'ton.

#### Guerreros de las sombras

- **Mazchna:** Los guerreros de las sombras son oscuros y misteriosos. Se esconden en las sombras, así que ten cuidado con las emboscadas. El sótano del Legends' Guild alberga estas amenazas.

#### Turoths

- **Mazchna:** Los turoths son criaturas grandes y feroces con pieles gruesas. Necesitarás un arma con hoja de hoja, flechas anchas o un dardo mágico para dañarlos. Puedes encontrar un nido de ellos en las Cuevas Rellekka Slayer.

#### Vampyres

- **Mazchna:** El último Feral vampyre que maté descubrí que los hechizos de fuego los derribaron de manera efectiva.
- [Vampyres son seres extremadamente poderosos. Se alimentan de la sangre de los vivos, así que ten cuidado de que no te muerdan. Mira en el bosque de Morytania.]

#### Hombres lobo

- **Mazchna:** Los hombres lobo son criaturas salvajes; fuerte y resistente con garras y dientes afilados. El pueblo de Canifis alberga muchos de ellos.
