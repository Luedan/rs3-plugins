# Alpheus

- **Original Wiki Page**: [Transcript:Alpheus](https://runescape.wiki/w/Transcript%3AAlpheus)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Building the Anachronia lodestone

- (Condition: Sólo la primera vez:)
  - **Alpheus:** Mr Mordaut mencionó que Wizards' Guild tiene un gran interés en extender su red lodestone hasta aquí.
  - **Alpheus:** Una vez que hayamos reunido suficientes recursos, ellos podrán hacer el resto para activarlo.
  - **Alpheus:** Personalmente estoy deseando que lo construyan, ya que hay cierto puesto de sándwiches en Ardougne que me encantaría volver a visitar.
  - **Alpheus:** De todos modos... probablemente estés más interesado en ver qué se necesita para construir, ¿verdad?
  - (continue)
- (opens=Base camp management)

### Talking to Alpheus


#### Antes de encontrar una pieza de tótem

- [Menu]: Elige una opción:
  - [Choice]: ¿Qué opinas de la isla? {{anchor|island}}
    - **Alpheus:** ¡Bueno, esto es una sorpresa! Todas nuestras investigaciones sugirieron que esta isla debería estar llena de fósiles...
    - **Player:** Creo que tu investigación debe estar equivocada.
    - **Alpheus:** Ciertamente no lo es.
    - **Player:** Pero esta isla está lo menos fosilizada posible. ¿Cómo podría ser correcta su investigación?
    - **Alpheus:** Esa es la pregunta que debemos responder.
    - (initial)
  - [Choice]: Debería irme.
    - **Alpheus:** ¡Feliz exploración!

### After finding a totem piece


#### Al entrar al campamento base

- **Eliza:** Hmm... ¿Qué es eso? ¡Las lecturas se han salido del gráfico!
- **Alpheus:** ¿Es una interferencia mágica? He estado viendo picos de vez en cuando.
- **Eliza:** Podría ser. Parece estar basado en la ubicación... Espera...
- **Eliza:** ¿Player? ¿Qué tienes ahí? Ven a hablar con nosotros rápidamente.

#### Inicialmente

- (Condition: Si el player no tiene la pieza tótem en backpack:)
  - **Eliza:** ¿Cuál es esa lectura de energía? ¿Has estado en contacto con algún artefacto mágico recientemente?
  - **Player:** ¿Encontré un trozo de tótem en la isla? ¿Podría ser eso?
  - (Action: continuar|descubrimiento)
- (Condition: Si el player tiene la pieza tótem en backpack:)
  - **Eliza:** ¿Qué tienes en tu backpack, Player? Está enviando nuestras lecturas de energía fuera del gráfico.
  - **Player:** ¿Te refieres a esto?
  - Muestras a los arqueólogos el tótem que descubriste.
  - (Action: continuar|descubrimiento)
- {{anchor|discovery}} **Alpheus:** ¡Qué descubrimiento! Sea lo que sea, parece contener una gran cantidad de energía en su interior.
- **Eliza:** ¡Mira! Es sólo una pieza de algo más grande. Quizás si pudieras encontrar todas las piezas podrían combinarse...
- **Alpheus:** ¿En serio le estás diciendo a Player que vuelva a ensamblar un antiguo artefacto de enorme energía sin considerar primero las precauciones de seguridad?
- **Player:** En realidad, está bien. Tiendo a apresurarme y la mayoría de las veces todo sale bien.
- **Alpheus:** ¡Dios mío! ¿Puedes creer esto?
- **Eliza:** ¿CÓMO LO HACES? ¡Toda mi vida me han dicho a qué temer! Ojalá pudiera tener tu coraje.
- **Player:** Uh... bueno... Me siento... obligado a hacer cosas, ¿sabes? Como si hubiera una fuerza externa guiando mis acciones.
- **Eliza:** ¡Oh, eso suena increíble! ¡Entonces suenas como la persona perfecta para llevar a cabo esta línea de investigación!
- **Alpheus:** Estoy de acuerdo. ¡Solo piensa en todo el papeleo que evitaremos!
- **Alpheus:** Si encuentras todas las piezas de ese tótem, júntalas y mira qué pasa después.

#### Diálogo posterior

- [Menu]: Elige una opción:
  - [Choice]: ¿Qué opinas de la isla?
    - (Action: arriba|isla)
  - [Choice]: ¿Qué puedes decirme sobre las piezas tótem?
    - **Alpheus:** Esos tótems parecen contener una gran cantidad de energía mágica, pero parecen haberse roto en pedazos. Si pudieras encontrar todas las piezas de un tótem y repararlo, probablemente crearías un objeto de inmenso poder.
    - (initial)
  - [Choice]: ¿Tienes algo donde pueda guardar piezas de tótem?
    - ''(Sin bolso tótem :)
      - {{tbox|pic=Totem bag detail.png|You receive a reinforced bag that looks like it will be strong enough to carry totem pieces.}}
      - (receives=totem bag)
      - **Alpheus:** Espero que eso ayude.
      - (initial)
    - *(Con un bolso totem en backpack :)*
      - **Alpheus:** Ya tienes uno en tu backpack. ¿Estás bien o te está afectando el calor?
      - (initial)
    - *(Con un bolso totem en el banco:)*
      - **Alpheus:** Ya tienes uno. Pero te diré una cosa: haré que alguien te lo traiga.
      - (Action: La pantalla se desvanece y desaparece.)
      - {{tbox|pic=Totem bag detail.png|You receive a reinforced bag that looks like it will be strong enough to carry totem pieces.}}
      - **Alpheus:** Espero que eso ayude.
      - (initial)
  - [Choice]: Debería irme.
    - **Alpheus:** ¡Feliz exploración!

### Block of Stone

- {{Main|Transcript:Helping Laniakea (miniquest)#Block of Stone}}

### Archaeology assistants


#### Mostrándoles un tótem ensamblado

- **Eliza:** ¿Has reconstruido un tótem? ¡Y todavía estás vivo! ¡Qué suerte!
- **Alpheus:** Y justo cuando hemos completado una investigación convincente que puede llevarnos al siguiente paso.
- **Eliza:** ¡Oh, sí! ¡Esto es muy emocionante! Como parte de nuestra investigación, hemos descubierto que la isla tiene lo que llamamos "líneas ley mágicas".
- **Alpheus:** Sí. Parece haber un flujo de magia en la isla y sus alrededores que parece formar concentraciones en ciertas áreas. Estoy seguro de que el tótem tiene una conexión con ellos.
- **Eliza:** Si exploras la isla, es posible que descubras dónde pertenecen estos tótems. Colocarlos debería crear la conexión entre la isla y el poder dentro del tótem.
- **Alpheus:** Y quién sabe qué hará eso.
- **Eliza:** ¿Quizás una explosión? Será emocionante de todos modos, estoy seguro.
- **Player:** Claro, veré qué puedo encontrar...

#### Hablar con ellos después de completar un ritual de tótem y con el rango de Asociado en Archaeology

- **Alpheus:** Oye, se ha corrido la voz de que ahora eres asociado del Gremio Archaeology y que has creado un equipo de investigación...
- **Eliza:** Alpheus y yo nos preguntábamos si podrías utilizarnos a los dos como asistentes de investigación...
- **Player:** ¡Oye, seguro! Cuantos más, mejor. Me vendría bien algunos asistentes mientras sucede.
- **Eliza:** ¡Eso es increíble, gracias! ¡Te haremos sentir orgulloso!
- **Alpheus:** Sí, Eliza y yo trabajaremos duro. ¡No te arrepentirás! Gracias.
- (continuea|NormalDialogue)
