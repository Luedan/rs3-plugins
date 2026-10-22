# The Raptor

- **Original Wiki Page**: [Transcript:The Raptor](https://runescape.wiki/w/Transcript%3AThe%20Raptor)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{ToC|limit=1}}

### Roaming


#### Robar creación

- (Es un diálogo entre the Raptor y Head Mystic).
- **The Raptor:** Quiero pelear.
- **Head Mystic** Bienvenido, mi... niño. Alabado sea los Santos por traerte aquí.
- **The Raptor:** Los Santos. Cuéntame sobre ellos.
- **Head Mystic** ¡Los Santos! Son las más benditas de todas las criaturas de los dioses.
- **Head Mystic** Hace mucho tiempo, sirvieron a sus dioses en las guerras gloriosas. Incluso ahora, cuando sus cuerpos han desaparecido, continúan fielmente la lucha.
- **The Raptor:** Ajá. Suena como mi tipo de gente.
- **Head Mystic** Estamos trabajando para restaurar los cuerpos de los Santos. ¿Nos ayudarías a luchar por el barro sagrado que necesitamos?
- **The Raptor:** ¡Sí!
- **Head Mystic** Primero, debes liberarte de todos los apegos mundanos antes de poder recorrer el camino entre mundos.
- **The Raptor:** No. No quitarme la armadura. No quitarse el casco.
- **Head Mystic** Puedes hacerte un casco nuevo con arcilla sagrada una vez que llegues a-
- **The Raptor:** ¡No! ¡Sin quitarse el casco!
- **The Raptor:** ¡Mantén a tus Santos! ¡Conserva tu arcilla mágica! ¡Soy the Raptor! Nadie ve mi cara.
- (Action: The Raptor se teletransporta lejos del vestíbulo.)

### Quest-related dialogue


#### No se han realizado misiones relevantes

- The Raptor te ignora.

#### Después de la búsqueda de Legends

- **The Raptor:** Escuché que mataste a Nezikchened. No impresionado. Sólo un demonio. Mató a muchos demonios.

#### Después de que el vacío te devuelva la mirada

- **The Raptor:** Escuché que mataste a Pest Queen. Interesante pelea. Lástima que no pude estar allí.

#### Después de Dragon Slayer

- **The Raptor:** Escuché que mataste a Elvarg. No impresionado. Sólo un dragón. Mató a muchos dragones.

#### Después Mientras Guthix Duerme

- **The Raptor:** Escuché que mataste a Balance Elemental y ayudaste a aclarar a Lucien. Lástima que no te hayas enfrentado a los dragonantes.

#### Después de una misión nómada

- Escuché que mataste a Nomad. Impresionado. Quizás seas tan bueno como yo.

#### Después de una misión de elfos

- **The Raptor:** Escuché que limpiaste el Templo de la Luz. Camino encontrado a Prifddinas.

#### Después del mentor del sueño

- **The Raptor:** Escuché que mataste a 'The Inadequacy'. Dentro de la cabeza de Cyrisus. Eh. Monstruo imaginario. No impresionado.

### Kuradal

- **The Raptor:** Dame una tarea.
- **Kuradal:** Has hecho todas mis tareas, Raptor. No hay nada más que pueda enseñarte.
- **The Raptor:** Dame. Una tarea.
- **Kuradal:** Mira, ¿no deberías hacer otra cosa? Acabas de terminar mi última tarea.
- **The Raptor:** ¡Demasiado fácil!
- **Kuradal:** Todo lo que sugiero será demasiado fácil. Podrías ser un slayer master si quisieras. Deberías estar enseñándome.
- **The Raptor:** Quédate ahí. Eh. No the Raptor. ¡Yo peleo!
- **Kuradal:** Bueno, está bien, pero todavía no hay nada que pueda-
- **The Raptor:** Da. A mí. ¡Una tarea!
- **Kuradal:** ¡Muy bien! Ve y mata... oh, no lo sé... cinco mil dagannoths.
- **The Raptor:** Dagannoths. Eh. Eh, eh.
- **Kuradal:** Adiós. Nos vemos cuando hayas terminado, sin duda.
- (The Raptor se teletransporta)
- **Kuradal:** Hola Player. Dioses, espero que nunca termines así.

### Player-owned farm


#### Vender animales

- **Raptor (experto en dragones):** Tengo una solicitud especial para [breed]. ¡Especialmente si tiene el rasgo [Trait]!
- **Raptor (experto en dragones):** También busco algunos dragones, de hecho compraré hasta [número] más mientras esté aquí.
- ((Repeated for each dragon in backpack:))
  - ¿Le gustaría vender [name] por frijoles [número]?
  - [Menu]: ¿Vender [name] por frijoles [número]?
    - [Choice]: Sí.
      - ((If the player has a million beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Raptor (experto en dragones):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - (continue)
      - ((If transaction would take the player over a million beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - [Menu]: ¿Completar la transacción de todos modos?
          - [Choice]: Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - [Choice]: No.
            - **Raptor (experto en dragones):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((Otherwise:))
        - (Action: El animal está vendido.)
        - Frijoles [número] agregados a su bolsa de divisas.
        - (continue)
    - [Choice]: No.
      - (end)
- ((If animals were not sold:))
  - **Player:** Déjame comprobar qué animales tengo que coincidan con tu solicitud.
- ((If animals were sold:))
  - ((If Raptor can still buy more:))
    - (end)
  - ((If Raptor can't buy more:))
    - **Raptor (experto en dragones):** He comprado todos los animales que necesito por ahora, ¡nos vemos más tarde!
    - (Action: The Raptor se teletransporta.)

#### Animales de venta rápida

- **Raptor (experto en dragones):** ¿Estás seguro de que quieres que me lleve todos los dragones que tienes? No aceptaré ninguno de tus favoritos.
- [Menu]: ¿Vender todos tus dragones?
  - [Choice]: si
    - ((With dragons in backpack:))
      - ((If the player has a million beans:))
        - ((Repeated for each remaining animal, then continues below:))
          - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - **Raptor (experto en dragones):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - No tienes animales para vender. ¡Cero animales, cero frijoles!
      - ((If transaction would take the player over a million beans:))
        - ((Repeated for each animal not surpassing the cap, then continues below:))
          - (Action: El animal está vendido.)
          - Frijoles [número] agregados a su bolsa de divisas.
        - ((Repeated for each animal left to sell, then continues below:))
          - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
          - [Menu]: ¿Completar la transacción de todos modos?
            - [Choice]: Sí.
              - (Action: El animal está vendido.)
              - Frijoles [número] agregados a su bolsa de divisas.
              - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
              - ((Repeated for each remaining animal, then continues below:))
                - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
                - **Raptor (experto en dragones):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - ((If multiple animals were sold:))
                - Has vendido animales [número] por un total de frijoles [número].
            - [Choice]: No.
              - **Raptor (experto en dragones):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - (continue)
        - ((If no animals were sold:))
          - No tienes animales para vender. ¡Cero animales, cero frijoles!
        - ((If multiple animals were sold:))
          - Has vendido animales [número] por un total de frijoles [número].
      - ((Otherwise:))
        - ((Repeated for each animal not surpassing the cap, then continues below:))
          - (Action: El animal está vendido.)
          - Frijoles [número] agregados a su bolsa de divisas.
        - ((If multiple animals were sold:))
          - Has vendido animales [número] por un total de frijoles [número].
    - ((Without dragons in backpack:))
      - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - [Choice]: No
    - (end)

### Glacor Front

- **The Raptor:** Ayuda o déjame en paz.

### The Raptor's Rampage


#### Habla con

- (Condition: Only on first time:)
  - **Player:** ¡Hola! ¿Qué está pasando aquí?
  - **The Raptor:** Bien conocido y bienvenido al retiro de War.
  - **The Raptor:** Me conocen como the Raptor y estoy aquí a petición de nuestro anfitrión para otorgar una bendición a los mejores guerreros de Gielinor.
  - **The Raptor:** Una vez al día, puedo otorgarte el Favor de Raptor, lo que aumenta las posibilidades de que ganes un trofeo adecuado en una batalla gloriosa.
  - [Mientras Raptor's Favor esté activo, tu próxima muerte de jefe antes del reinicio diario (00:00 UTC) te otorgará tres oportunidades de acceder a objetos raros específicos del jefe, en lugar de una.]
  - **The Raptor:** Habla conmigo, pide el favor de Raptor, luego atraviesa uno de estos portales y entra en la refriega.
  - (continue)
- (Condition: Only after the first time:)
  - **The Raptor:** ¿Has vuelto por más?
  - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: cond=Only if not asked last:|¿Qué es este evento nuevamente y cómo funciona?
    - **The Raptor:** ¿Ves al tipo grande que está junto a la entrada? Alto. Expresión vacante. Personificación antropomorfa del conflicto mortal.
    - **Player:** ¿War? Es un poco difícil extrañarlo.
    - **The Raptor:** Nos remontamos a mucho tiempo atrás. Entonces, cuando me pidió que respaldara su evento especial como invitado de honor, ¿cómo podría decirle que no?
    - **The Raptor:** Especialmente cuando se trata de matar cosas.
    - **The Raptor:** En pocas palabras, una vez al día puedo otorgarte el Favor de Raptor, una bendición que aumenta las posibilidades de que recojas un trofeo adecuado del cuerpo de un enemigo digno.
    - **Player:** ¿Qué se considera un enemigo digno?
    - **The Raptor:** Algo lo suficientemente desagradable como para que valga la pena. Pasar por uno de estos portales aquí debería situarlo en el camino correcto.
    - [Mientras Raptor's Favor esté activo, tu próxima muerte de jefe antes del reinicio diario (00:00 UTC) te otorgará tres oportunidades de acceder a objetos raros específicos del jefe, en lugar de una.]
    - [Se puede activar una vez al día mientras dure el evento hablando con the Raptor.]
    - (previous)
  - [Choice]: cond=Only if not asked last:|Grant ¡El favor de Raptor!
    - (Condition: Without having received Raptor's Favour today:)
      - (Condition: During the event:)
        - (Action: el player recibe el favor de Raptor.)
        - **The Raptor:** Ahí. ¡Ahora, adelante y mata!
        - [¡El favor del raptor está activo! La próxima muerte de tu jefe antes del reinicio diario (00:00 UTC) te otorgará tres oportunidades de acceder a objetos raros específicos del jefe, en lugar de una.]
        - (previous)
      - (Condition: After the event has ended:)
        - **The Raptor:** Lo sentimos, el evento de War terminó.
    - (Condition: Having received Raptor's Favour today:)
      - (Condition: With Raptor's Favour active:)
        - **The Raptor:** Ya tienes Raptor's Favor. ¿Qué estás esperando? ¡Mata algo! ¡Algo grande!
        - [¡El favor del raptor está activo! La próxima muerte de tu jefe antes del reinicio diario (00:00 UTC) te otorgará tres oportunidades de acceder a objetos raros específicos del jefe, en lugar de una.]
        - (previous)
      - (Condition: Without Raptor's Favour active:)
        - **The Raptor:** Parece que has agotado tu Favor de Raptor por hoy.
        - [Raptor's Favor estará disponible nuevamente después del reinicio diario (00:00 UTC).]
        - (previous)
  - [Choice]: cond=Only if not asked last:|¿Quién eres tú, de todos modos?
    - **The Raptor:** No me sirven mucho los nombres, pero algunos me llaman the Raptor. Sirve bastante bien.
    - **The Raptor:** Baste decir que soy un guerrero errante, siempre atento al próximo desafío.
    - **The Raptor:** Idealmente, un desafío con colmillos venenosos y goteantes. ¡O garras afiladas que pueden partir en dos a un hombre adulto! ¡Oh! O espinas paralizantes que salen disparadas de su...
    - **Player:** Te... dejaré con eso.
    - (previous)
  - [Choice]: Adiós
    - **The Raptor:** Buena caza.
    - (end)

#### Dar favor

- (above|Raptor's Favour)

### Fort Forinthry


#### Habla con

- [Menu]: Elige una opción:
  - [Choice]: ¿Podemos hablar de asignaciones?
    - **Player:** Necesito otra tarea.
    - (Condition: If currently not on a Slayer assignment:)
      - (Condition: If the player is randomly chosen to receive the Raptor's special slayer challenge:)
        - (continue|Receiving a special challenge)
      - (Condition: If the player is wearing a Slayer master cape and is randomly chosen to select the next task:)
        - [pic=Slayer master capa detail.png]
        - (opens=The Raptor#Assignment)
      - (Condition: If the player didn't get to choose their task and has Slayer VIP tickets:)
        - [Menu]: ¿Cambiar su tarea Slayer asignada?
          - [Choice]: [número] [monsters] (predeterminado)
            - (continue)
          - [Choice]: [número] [monsters] (cuesta 1 token Slayer)
            - (Action: Se cambia la asignación.)
            - (continue)
      - (Condition: With Slayer Introspection harnessed:)
        - [Menu]: ¿Modificar su tarea Slayer asignada?
          - [Choice]: [número] [monsters] (predeterminado)
            - (continue)
          - [Choice]: [minimal number] [monsters] (min)
            - (Action: La cantidad en la asignación se cambia al mínimo.)
            - (continue)
          - [Choice]: [maximal number] [monsters] (máx.)
            - (Action: La cantidad en la asignación se cambia al máximo.)
            - (continue)
      - ((One of the following appears, then continues below:))
        - **The Raptor:** Está bien, entonces, supongo. Tu nueva tarea es matar a [número] [monsters].
        - **The Raptor:** Lo estás haciendo bien, supongo. Tu nueva tarea es matar a [número] [monsters].
      - [Menu]: Selecciona una opción
        - [Choice]: ¿Tienes algún consejo para mí?
          - **Player:** ¿Tienes algún consejo para mí?
          - (continue|Assignment advice)
        - [Choice]: ¡Vale, genial!
          - **Player:** ¡Vale, genial!
          - **The Raptor:** No falles y no olvides volver cuando necesites una nueva tarea.
        - [Choice]: No gracias. (Tarea clara, cuesta 30 puntos Slayer)
          - {{Transcript missing}}
    - (Condition: If currently on a Slayer assignment:)
      - **The Raptor:** Todavía estás cazando a [monsters]; Vuelve cuando hayas terminado tu tarea.
  - [Choice]: Hablemos de ti.
    - **The Raptor:** Los nombres no importan. Llámame the Raptor.
    - **The Raptor:** El combate es lo único que importa. El valor viene en la batalla.
    - **The Raptor:** Con cada monstruo que mato, me hago más fuerte.
    - (previous)
  - [Choice]: cond=Only with the skeleton trophy mounted:|¿Podemos hablar de cambiar la duración de tu tarea?
    - ((The following is shown in an interface titled "SELECT AN OPTION" with the currently active task length selection is disabled.))
      - [Menu]: Elija la duración de su tarea:
        - [Choice]: Predeterminado
          - [Las tareas Slayer de the Raptor ahora tendrán la duración predeterminada.]
        - [Choice]: corto
          - [Ahora recibirás tareas de asesino más cortas de the Raptor.]
        - [Choice]: largo
          - [Ahora recibirás tareas de asesino más largas de the Raptor.]
  - [Menu]: cond=Solo antes de completar A Place For My Heads:|¿Podemos hablar de tus trofeos de recompensa?
    - (Condition: If the player has Slayer challenges toggled off:)
      - {{Transcript missing}}
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Puedes hablarme un poco más sobre las recompensas de trofeos?
        - **The Raptor:** Los trofeos mejoran tu habilidad Slayer. Tienen beneficios que te ayudarán mientras completas mis tareas.
        - **The Raptor:** Cada vez que regreses a mí después de completar uno de mis desafíos, te otorgaré un nuevo trofeo para que lo coloques en tu caseta de vigilancia, siempre que seas lo suficientemente fuerte.
        - [Recibirás una nueva recompensa de punto de acceso de the Raptor después de completar sus tareas de Slayer en 30, 50 y 90 Slayer.]
      - [Choice]: ¿Tienes alguna recompensa para mí?
        - (Condition: If the player has unclaimed slayer trophy rewards:)
          - (Condition: Without space in backpack:)
            - **The Raptor:** Lo siento, no tienes suficiente espacio para todas tus recompensas. {{Sic|Come back once you've up some space.}}
          - (Condition: With space in backpack:)
            - (Condition: With one unclaimed reward:)
              - (receives=the next slayer trophy in sequence)
              - [Has recibido: Trofeo Slayer ([Zombie/Skeleton/Phantom])]
              - **The Raptor:** Aquí está tu recompensa. Si lo montas en la caseta de vigilancia, debería ofrecerte algunos efectos positivos.
            - (Condition: With multiple unclaimed rewards:)
              - (Condition: For each unclaimed trophy:)
                - (receives=the next slayer trophy in sequence)
                - [Has recibido: Trofeo Slayer ([Zombie/Skeleton/Phantom])]
                - (continue)
              - **The Raptor:** Aquí están todas las recompensas que se le deben. Si los montas en la caseta de vigilancia, deberían ofrecerte algunos efectos positivos.
        - (Condition: If the player does not have an unclaimed slayer trophy reward:)
          - **The Raptor:** No tienes ninguna recompensa disponible.
  - [Choice]: Eh... nada...
    - **Player:** Eh... nada...
    - (end)

#### Recibiendo un desafío especial

- **The Raptor:** Los muertos vivientes en las criptas del norte arrasarán el fuerte si no haces nada.
- **The Raptor:** Mata a [número] de ellos. Yo haré lo mismo y nos encontraremos aquí.
- **The Raptor:** Los objetivos más fuertes merecen varias muertes. ¿Lo entiendes?
- (Condition: If the player has not yet claimed all three slayer trophies:)
  - **The Raptor:** Completa esta tarea y ganarás un trofeo. Los trofeos mejoran tu habilidad de asesino.
  - (continue)
- (Condition: If the player has already claimed all three slayer trophies:)
  - [Completar esta tarea otorgará puntos de cazador adicionales.]
  - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: Muy bien, acepto tu desafío.
    - **The Raptor:** Bien.
  - [Choice]: No, gracias. Preferiría una tarea normal.
    - (above|Regular slayer assignment)

#### Obtener tarea

- (above|I need another assignment)

#### Comercio

- (opens=Slayer Equipment)

#### Recompensas

- ((Slayer Rewards interface opens.))

#### Al completar un desafío especial

- Has completado tu tarea especial de the Raptor y recibes 3000 experiencia de cazador y 20 puntos de cazador.
- (Condition: If the player has not yet claimed all three slayer trophies:)
  - The Raptor tiene una nueva recompensa para ti.

#### Usando fragmentos de hueso

- ((The following is shown in an input prompt interface:))
  - {{Tinput|How many bone fragments would you like to hand in? (0-[number])}}
  - ((Continues after entering a positive number, or ends after entering "0".))
- (removes=as many bone fragments as they entered)
- (Action: el player gana experiencia Slayer.)
- The Raptor te enseña sobre Slayer.
- **The Raptor:** Gracias, los agregaré a mi colección.

### Activating the [[Enchanted gem]]

{{Transcript missing}}

### Casting NPC contact

- **Player:** ¿Hola? ¿Es {{Sic}} este the Raptor?
- **The Raptor:** No tienes nada que hacer en mi cabeza. Mis pensamientos son míos.
- **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo.
- **The Raptor:** Explícate.
- [Menu]: Selecciona una opción
  - [Choice]: Necesito otra tarea.
    - **Player:** Necesito otra tarea.
    - (arriba)
  - [Choice]: Eh... nada.
    - **Player:** Eh... nada...
    - (end)

### Assignment advice


#### Espectros aberrantes

- Los espectros aberrantes son fantasmas fétidos y viles. El solo olor de ellos te paralizará y te hará daño. Aconsejaría utilizar una clavija en la nariz para evitar su mal olor. Harías bien en usar un arma a distancia contra ellos.

#### Demonios abisales

- **The Raptor:** El último demonio abisal que maté encontré que los ataques cortantes los derribaron de manera efectiva.
- Los demonios abisales son criaturas desagradables con las que lidiar. Se teletransportan para confundir y atrapar a sus presas. Se pueden encontrar dentro de la Torre Canifis Slayer o habitando el Asilo Senntisten.

#### mamuts de Acheron

- **The Raptor:** El último Acheron mammoth que maté descubrí que los ataques de apuñalamiento los derribaron de manera efectiva.
- Los mamuts de Acheron son bestias honorables y orgullosas del norte helado que conocen el verdadero valor de la batalla. Cuando te cobren, asegúrate de apartarte del camino. Se pueden encontrar en un iceberg al que se puede acceder desde un muelle al este de Rellekka.

#### Ankou

- **The Raptor:** El último Ankou que maté descubrí que los hechizos de tierra los derribaron de manera efectiva.
- Los ankou son seres no muertos que no pueden describirse ni como fantasmas ni como esqueletos, sino como una combinación de ambos. No se sabe mucho sobre estas criaturas, sin embargo, tienen su hogar en la Fortaleza de Seguridad.

#### Fantasmas blindados

- **The Raptor:** El último fantasma blindado que maté encontré que los ataques aplastantes los derribaron de manera efectiva.
- Puedes encontrar fantasmas blindados pululando dentro de las criptas al norte de Fort Forinthry. Sus espíritus odiosos sólo buscan la violencia. Encontrarás que las armas aplastantes son efectivas para debilitar su capacidad de moverse.

#### Avianas

- Los aviansies se pueden encontrar dentro del God Wars Dungeon al norte de Trollheim. Mientras vuelan, te resultará difícil alcanzarlos con armas cuerpo a cuerpo, así que intenta usar armas mágicas o a distancia.

#### Demonios negros

- **The Raptor:** El último demonio negro que maté encontré una ballesta con pernos que los derribó de manera efectiva.
- Los demonios negros se encuentran entre los demonios avernicos más fuertes. Se pueden encontrar dentro de las mazmorras Brimhaven y Taverley. Usar ballestas sería una ventaja.

#### Dragones negros

- **Raptor:** El último dragón negro que maté encontré una ballesta con pernos que los derribó de manera efectiva.
- Los dragones negros son los más fuertes de los dragones cromáticos. Se pueden encontrar descansando dentro de Taverley Dungeon. Usar ballestas sería una ventaja.

#### Esqueletos atados

- **The Raptor:** El último esqueleto atado que maté encontré que los hechizos de tierra los derribaron de manera efectiva.
- Animado por Zemouregal, puedes encontrar esqueletos atados pululan dentro de las criptas al norte de Fort Forinthry. Encontrarás que la magia de la tierra es eficaz para descomponer sus huesos antiguos.

#### guerreros Camel

- **The Raptor:** El último guerrero Camel que maté encontré que los ataques aplastantes lo derribaron de manera efectiva.
- Los guerreros Camel usan magia antigua para atacarte. Pueden usar magia de desorientación cobarde para confundirte. Puedes encontrarlos en lo profundo del desierto, darles una lección de humildad.

#### Dagannot

- **The Raptor:** El último Dagannoth que maté encontré que los hechizos de aire los derribaron de manera efectiva.
- Los Dagannoth son criaturas marinas grandes que son muy agresivas. A menudo los encontrarás en cuevas cerca del agua de mar.

#### Bestias oscuras

- **The Raptor:** La última bestia oscura que maté encontré una ballesta con pernos que los derribó de manera efectiva.
- Las bestias oscuras son depredadores grandes, parecidos a perros, con cuerpos enormemente musculosos que los protegen de las armas aplastantes. Se pueden encontrar dentro de los túneles Mourner.

#### Demonios

- **The Raptor:** El último demonio abisal que maté encontré que los ataques cortantes los derribaron de manera efectiva.
- Puedes encontrar muchos tipos de demonios alrededor de Gielinor, en particular los demonios abisales que infestan la Torre Canifis Slayer.

#### dragones

- **The Raptor:** El último dragón verde que maté encontré una ballesta con pernos que los derribó de manera eficiente.
- Puedes encontrar dragones a través de Gielinor. Se pueden encontrar muchos tipos de ellos en Brimhaven Dungeon.

#### Zombis fétidos

- **The Raptor:** El último zombi fétido que maté encontré que los hechizos de aire los derribaron de manera efectiva.
- Estas lamentables criaturas no tienen voluntad propia y sólo buscan la carne de sus enemigos. Puedes encontrar zombis fétidos dentro de las criptas al norte de Fort Forinthry. Descubrirás que usar magia es efectivo contra ellos.

#### Gigantes de fuego

- **The Raptor:** El último gigante de fuego que maté encontré que los hechizos de agua los derribaron de manera efectiva.
- Al igual que otros gigantes, los gigantes de fuego suelen empuñar armas grandes. Aprende a reconocer qué tipo de arma es y actúa en consecuencia. Se pueden encontrar en Brimhaven Dungeon. Usar hechizos de agua sería una ventaja.

#### Fantasmas

- **The Raptor:** El último fantasma resucitado que maté encontré un arco y las flechas los derribaron de manera efectiva.
- Puedes encontrar muchos tipos de fantasmas alrededor de Gielinor, en particular los que inundan las criptas al norte de Fort Forinthry.

#### Demonios mayores

- **The Raptor:** El último demonio mayor que maté encontré una ballesta con pernos que los derribó de manera efectiva.
- Los demonios mayores son relativamente débiles, sin embargo, debes tener cuidado ya que pueden ser peligrosos. Se pueden encontrar en Brimhaven Dungeon. Usar ballestas sería una ventaja.

#### Dragones verdes

- Los dragones verdes son los más débiles de los dragones cromáticos y se pueden encontrar al oeste de la Fortaleza de los Guerreros Oscuros. Usar ballestas sería una ventaja.

#### Gusanos de grosella

- **The Raptor:** El último gusano joven que maté encontré una ballesta con pernos que los derribó de manera efectiva.
- Se han visto gusanos de grot en una cueva cerca de Rimmington. Morderán y atacarán con una especie de saliva ácida.

#### Perros del infierno

- Los Hellhounds son demonios Avernic de clase Shakroth, la clase más baja de demonios de Infernus. Puedes encontrarlos en Taverley Dungeon y encontrarás armas cortantes efectivas contra ellos.

#### Calfitos

- **The Raptor:** El último soldado calfita que maté descubrí que los hechizos de agua los derribaron de manera efectiva.
- Los calfitos son grandes insectoides que viven en colmenas bajo el Kharidian desert. Puedes encontrarlos al suroeste del paso Shantay.

#### Demonios menores

- Los demonios menores son algunos de los demonios avernicos más débiles. Se pueden encontrar habitando la mazmorra Karamja. Usar ballestas sería una ventaja.

#### Wyverns vivientes

- **The Raptor:** El último Wyvern que maté descubrí que los hechizos de fuego los derribaron de manera efectiva.
- Los wyverns vivos respiran un veneno que te matará rápidamente a menos que puedas congelar tu sangre usando la temperatura glacial de su hogar. Pero cuidado; cuanto más frío tengas, más fuerte te golpearán sus ataques habituales. Se pueden encontrar dentro de la Mazmorra de Hielo de Asgarnia.

#### Demonios destripadores

- **The Raptor:** El último Demonio Destripador que maté encontré que los hechizos de tierra los derribaron de manera efectiva.
- Los demonios destripadores disfrutan de la sed de sangre de la batalla, un sentimiento con el que estoy de acuerdo. Expondrán tus debilidades y te golpearán con más fuerza cuanto peores sean tus lesiones. Se pueden encontrar en una fisura al este de Al Kharid.

#### Fantasmas resucitados

- Estos espíritus torturados han sido resucitados por Zemouregal y están sujetos a su voluntad. Puedes encontrar fantasmas resucitados que habitan en las profundidades de las criptas al norte de Fort Forinthry, esperando la orden de Zemouregal. Encontrarás arcos efectivos contra este objetivo.

#### Esqueletos

- **The Raptor:** El último esqueleto atado que maté encontré que los hechizos de tierra los derribaron de manera efectiva.
- Puedes encontrar muchos tipos de esqueletos alrededor de Gielinor, en particular los que inundan las criptas al norte de Fort Forinthry.

#### No-muertos

- **The Raptor:** El último esqueleto atado que maté encontré que los hechizos de tierra los derribaron de manera efectiva.
- Puedes encontrar muchos tipos de muertos vivientes alrededor de Gielinor, en particular los que se pudren dentro de las criptas al norte de Fort Forinthry.

#### No-muertos de Zemouregal

- **The Raptor:** El último esqueleto atado que maté encontré que los hechizos de tierra los derribaron de manera efectiva.
- No-muerto criado por el nigromante Zemouregal. Acechan en la cripta al norte de Fort Forinthry.

#### Zombis

- **The Raptor:** El último zombi fétido que maté encontré que los hechizos de aire los derribaron de manera efectiva.
- Puedes encontrar muchos tipos de zombis alrededor de Gielinor, en particular los que inundan las criptas al norte de Fort Forinthry.
