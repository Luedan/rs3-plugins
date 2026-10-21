# Sharrigan

- **Original Wiki Page**: [Transcript:Sharrigan](https://runescape.wiki/w/Transcript%3ASharrigan)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Anachronia base camp


#### Habla con

- (Condition: Antes de completar Único en su clase:)
  - **Sharrigan:** Bien conocido.
  - (continue)
- (Condition: Después de completar Único en su clase:)
  - **Sharrigan:** Nos volvemos a encontrar.
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Sharrigan:** Soy Sharrigan. Yo soy... era el Guardián del Pasado de Ilujanka. Bueno, supongo que todavía lo soy, pero ahora también algo más.
    - **Sharrigan:** Mi función era recordar las historias de nuestra gente, pero desde que Vindicta visitó Iaia, algunos de nuestros jóvenes han decidido convertirse en pioneros, viajar aquí y encontrar un nuevo hogar.
    - **Sharrigan:** Muchos de ellos han decidido colonizar esta isla, o al menos detenerse aquí inicialmente, ya que tiene cierto parecido con nuestro mundo: las selvas, los animales, el clima.
    - **Sharrigan:** Desde que visité este mundo, me ofrecí como voluntario para acompañarlos y apoyarlos, para seguir recordándoles de dónde vienen.
    - (initial|initial-options-anachronia)
  - [Choice]: ¿Qué estás coleccionando?
    - **Sharrigan:** ¿Le gustaría ver mis colecciones o simplemente discutirlas?
    - [Menu]: ¿Qué te gustaría hacer?
      - [Choice]: Ver colecciones.
        - (se abre=Sharrigan#Archaeology colecciones{{!)Ilujank' Antiquities}}
      - [Choice]: Habla de colecciones.
        - **Sharrigan:** Supongo que también podría aprender algunas de las historias de quienes alguna vez vivieron aquí. Contar historias del pasado es mi razón de ser.
        - **Sharrigan:** Estoy fascinado con los dragonantes que una vez vivieron aquí, y por eso aceptaré cualquier artefacto que se encuentre en esta isla.
        - (initial|initial-options-anachronia)
  - [Choice]: ¿Cuáles son las recompensas de tu colección?
    - **Sharrigan:** Por supuesto, ustedes, los humanos, disfrutan de sus recompensas...
    - **Sharrigan:** He llegado a un acuerdo con los arqueólogos que trabajan aquí. Han aceptado darme cualquier recurso compactado que encuentren mientras realizan sus tareas.
    - **Sharrigan:** Ahora tengo muchas cajas llenas de madera, enredaderas, hojas, pieles, piedras y arcilla.
    - **Sharrigan:** Por completar mi primera colección, cambiaré seis de estas cajas. Podrás seleccionar qué recurso compactado te otorga cada uno de ellos. Tengo bastante stock de todo tipo.
    - **Sharrigan:** Luego, para mi segunda y cuarta colección, intercambiaré algunos fragmentos de esqueleto de rex. Me intriga la reconstrucción que se está llevando a cabo en otras partes del campo base.
    - (Condition: Antes de completar Sharrigan III:)
      - **Sharrigan:** Y en cuanto a mi tercera colección, descubrí una poderosa reliquia mágica de una de las criptas dragonkin.
      - **Sharrigan:** Una vez fue propiedad de un dragonante llamado Kaladan. El staff en sí se llama Kaladanda, lo que sugiere que este dragonante lo nombró o lo creó.
      - **Player:** Entonces, coloquialmente, ¿el 'Staff de Kaladan'? ¿Qué hace?
      - **Sharrigan:** Hay tallas por todas partes que representan escenas de muerte: huesos, cenizas y cosas similares. Exuda un aura de magia de muerte, pero también de vida nueva; me recuerda a Iaia, a los Olun'dai.
      - **Sharrigan:** Creo que sus efectos se relacionan con el momento en que tus enemigos mueren, recolectando sus restos en una forma fácil de almacenar, dándoles un nuevo propósito.
      - (continue)
    - (Condition: Después de completar Sharrigan III:)
      - **Sharrigan:** ¿Has desbloqueado el poder de Kaladanda staff?
      - (continue)
    - **Sharrigan:** Recientemente, varios arqueólogos han regresado con fichas de la mazmorra de Daemonheim. Para mi quinta colección puedo proporcionarles dos cajas grandes de estas fichas.
    - (Condition: Antes de completar Sharrigan VI:)
      - **Sharrigan:** Para completar mi sexta colección, también adquirí una reliquia bastante única del pasado. Un tapiz que representa un encuentro entre los y gorajo.
      - **Sharrigan:** Tras un estudio más profundo, este tapiz parece ser más que un simple registro de esta reunión.
      - **Sharrigan:** Ha sido imbuido de las técnicas precisas de su propia y meticulosa creación. A través de más estudios, podrá aprovechar esta meticulosa precisión para su propio beneficio.
      - (continue)
    - (Condition: Después de completar Sharrigan VI:)
      - **Sharrigan:** ¿Pudiste hacer uso del poder imbuido dentro del tapiz?
      - **Sharrigan:** Para completar aún más mi sexta colección, puedo proporcionarles más de estas cajas de fichas grandes, incluso incluiré una de estas tarjetas misteriosas que descubrieron algunos de los arqueólogos.
      - (continue)
    - **Sharrigan:** En cuanto a mi séptima colección, puedo ofrecerles una pieza de tetracompass.
    - **Sharrigan:** Además de todo eso, también tengo cronotas.
    - (Condition: Si el player no le ha dado una máscara mortuoria al gato Bob:)
      - **Sharrigan:** ¡Oh! ¡Una última cosa! Esto es extraño, pero Mr Mordaut también me informó que el amigo de un amigo solicitó una máscara mortuoria de dragón. ¿Quizás conoces el llamado 'el gato Bob'?
      - (continue)
    - (initial|initial-options-anachronia)
  - [Choice]: cond=With Balarak's sash brush (damaged) in backpack:|¿Sabes lo que necesito para restaurar este pincel?
    - (Condition: Antes de aprender a restaurar el cepillo de marco de Balarak:)
      - [Sharrigan mira por encima del mango del cepillo dañado.]
      - **Sharrigan:** Este es el mango de un cepillo de fajín dragonkin. He leído sobre ellos, pero esta es la primera vez que veo uno.
      - **Sharrigan:** Se utilizaron en la preparación de muestras experimentales para garantizar que no hubiera contaminantes presentes; según mis lecturas, fueron extremadamente efectivos.
      - **Player:** Interesante, ¿sabes qué voy a necesitar para restaurar esto a un estado utilizable?
      - **Sharrigan:** Restaurar el mango debería ser sencillo; una combinación de fieltro, negro de humo y metal de dragón debería bastar.
      - **Sharrigan:** Las cerdas son más complejas de obtener. Necesitarás encontrar un poco de pelo de zigomita seco y molerlo con un poco de polvo de ónix.
      - **Sharrigan:** Luego, una vez que el mango y el pelo de zigomita suavizado están unidos, el último paso es una infusión de energía dracónica.
      - (initial|initial-options-anachronia)
    - (Condition: Después de aprender cómo restaurar el cepillo de marco de Balarak:)
      - **Player:** ¿Podrías recordarme qué necesito para restaurar este cepillo dañado?
      - (continuea|restore-brush-steps)
  - [Choice]: Adiós.
    - **Sharrigan:** Hasta la próxima.

#### Colección Archaeology

- (se abre=Sharrigan#Archaeology colecciones{{!)Ilujank' Antiquities}}

### Dream of Iaia


#### Habla con

- **Guardián del pasado Sharrigan:** Hola, Player.
- ((Con el amuleto Pastkeeper:))
  - **Player:** Hola, Sharrigan. Tengo algo para ti.
  - **Guardián del pasado Sharrigan:** ¿Oh?
  - **Player:** Antes de dejar Iaia, intenté que el viejo Guardián del Pasado evacuara. Ella se negó a irse, pero me dio este amuleto.
  - **Player:** Ella me pidió que te lo diera y te dijera que estabas listo.
  - (removes=Pastkeeper amulet)
  - ¡Felicitaciones! Has completado: 'Fuera del pasado': entrega a Sharrigan el amuleto del guardián del pasado de su mentor.
  - **Pastkeeper Sharrigan:** ¿Su amuleto?
  - **Pastkeeper Sharrigan:** No puedo describir cuánto la extraño. Ella me enseñó todo. Al menos una pequeña parte de ella sobrevive en esto. Y sus historias -nuestras historias- sobreviven en mí.
  - **Guardián anterior Sharrigan:** Gracias, Player. Atesoraré esto mientras viva.
  - (continue|hear-pastkeeper-stories)
- **Pastkeeper Sharrigan:** ¿Te gustaría escuchar alguna historia de pastkeeper?
- Seleccione una opción
  - Sí.
    - ((Sin ninguna historia desbloqueada:))
      - **Pastkeeper Sharrigan:** {{AnchorText|You must train with the other ilujanka here first}}, para poder acceder a sus historias.
    - ((Con historias desbloqueadas:))
      - **Guardián del pasado Sharrigan:** ¿{{AnchorText|Which story do you wish to hear}}?
      - (Se abre una interfaz de selección de historias con historias desbloqueadas seleccionables).
        - Reflexionar sobre las malas decisiones
          - **Pastkeeper Sharrigan:**El orgullo es una virtud. Siempre debemos estar orgullosos de nosotros mismos y de lo que hacemos. Pero como tantas cosas, demasiado o una virtud puede convertirse en un vicio. El orgullo puede fácilmente transformarse en vanidad o arrogancia. Lamilos era un hombre muy orgulloso.
          - **Pastkeeper Sharrigan:**Lamilos tenía escamas que eran tan brillantes como las lunas durante una conjunción. Brillaban a la luz de la mañana y reflejaban el suave resplandor del crepúsculo en una deslumbrante variedad de colores. La gente estaba asombrada por su belleza, pero nadie tanto como él mismo.
          - **Pastkeeper Sharrigan:** Lamilos estaba tan enamorado de su propia belleza que decidió que necesitaba vivir en un lugar donde pudiera admirarse adecuadamente. Consultó con los arquitectos y albañiles del pueblo y les encargó una casa tan magnífica que sería la envidia de todos. Quería una casa con paredes interiores de cristal reluciente y paredes exteriores de piedra pulida. Para poder contemplar su belleza reflejada cuando le apeteciera.
          - **Guarda del pasado Sharrigan:** Los albañiles y arquitectos le advirtieron que una casa así era una locura, pero Lamilos no quiso oír nada de eso. Exigió que le hicieran esta casa de espejos y, a regañadientes, accedieron.
          - **Guardián del pasado Sharrigan:** Durante muchos días y noches, Lamilos se deleitó en una casa que se mostraba cada vez que miraba. Se deleitaba con sus reflexiones y conversaba con su rostro con un deleite tan profundo que apenas dormía.
          - **Pastkeeper Sharrigan:** Pero el orgullo viene antes del otoño y antes del otoño llega el verano. Este verano fue el más brillante y caluroso de todos. Un calor tan fuerte que las cosechas se marchitaron y el pantano empezó a secarse. Los rayos del sol eran tan brillantes y tan fuertes, pero cuando entraron en la casa de vidrio y espejos se convirtieron en un ardiente infierno de resplandor. En un instante, Lamilos (y todas sus hermosas escamas) se convirtieron en motas de polvo en el aire del verano.
          - **Pastkeeper Sharrigan:** O quizás me equivoque. Quizás vivieron felices para siempre, pero no lo sé, yo no estuve allí.
          - (above|Which story do you wish to hear)
        - Tempestad en una tetera
          - **Pastkeeper Sharrigan:** Los problemas siguen a algunas personas. No importa lo que hagan o adónde vayan, los acecha como una bestia varigun cazando a su presa. El pobre Eldibras era una de esas personas.
          - **Guardián del pasado Sharrigan:** Eldibras se había entrenado toda su vida como alfarero, anhelando crear hermosas obras de arte con la rica y colorida arcilla de Iaia. Pero sus ollas siempre se tambaleaban y sus tazas siempre se rompían. Lo intentó y lo intentó, pero era como si los Olundai hubieran decidido que su trabajo nunca tendría la calidad para la que había trabajado.
          - **Pastkeeper Sharrigan:** Entonces, un día, un extraño visitante llegó al pueblo. Era alto y olía a especias y flores exóticas que nadie había olido antes. Deambuló por las tiendas en busca de algo único, pero con cada pieza de artesanía perfecta se alejaba disgustado.
          - **Guarda del pasado Sharrigan:** Hasta que finalmente se encontró con el exiguo puesto del mercado de Eldibras y vio las creaciones torcidas, deformadas e imperfectas que el alfarero ofrecía a la venta.
          - **Guardián del Pasado Sharrigan:** '¡Qué maravillas!' habló el hombre. Su voz era como un viento rugiente y sacudió todas las piezas de la mesa. Las ollas se tambalearon. Las tazas tintinearon. Pero sus imperfecciones deformadas les impidieron caer. 'Nunca había visto obras tan singulares. Cada uno de ellos diferente. Cada uno de ellos una historia de lucha y supervivencia. ¡Debo tenerlos!'.
          - **Guarda del Pasado Sharrigan:** Le entregó a Eldibras no una bolsa de oro, ni una piedra preciosa, sino una pequeña caja que traqueteaba y se tambaleaba. 'Dentro de esta caja hay una hermosa imperfección. Un trozo de tiempo que se perdió y se despegó del resto. Mantenlo contigo para que siempre tengas el tiempo que necesitas.' y con eso el extraño tomó las ollas y tazas deformes y salió de esta historia y entró en otra.
          - **Pastkeeper Sharrigan:** A partir de entonces, Eldibras tuvo todo el tiempo del mundo, y él lo sabía. Se concentró en su oficio y con el tiempo pudo hacer ollas, tazones, platos y tazas sin imperfecciones. Aunque siempre guardaba los que no eran perfectos. Porque sabía que sus imperfecciones los hacían únicos, los hacían hermosos.
          - **Pastkeeper Sharrigan:** Quizás vivieron felices para siempre, pero no lo sé, yo no estuve allí.
          - (above|Which story do you wish to hear)
        - La perla de las lunas
          - **Guarda del pasado Sharrigan:** Les contaré la historia del pescador Omisha. Omisha no era una maestra en su oficio ni una novata. Su vida era un monumento a la mediocridad y así le gustaba a ella. Tenía pocas aspiraciones de grandeza y ningún deseo de poder, fama o riqueza. Ella simplemente quería vivir una vida cómoda y ser feliz.
          - **Guardia del pasado Sharrigan:** Pero Olun'dai es algo voluble y su Olun'det tenía otros planes para ella. Un día, mientras pescaba mariscos bajo la cálida luz del verano, se encontró con una concha de colores brillantes como nunca antes había visto. Con cuidado, quitó el caparazón y lo abrió para ver qué tipo de criatura había dentro.
          - **Pastkeeper Sharrigan:** Pero no encontró ninguna criatura. En lugar de eso, encontró sólo una perla, perfectamente encajada en la concha. La perla era algo hermoso. Cuando lo miró de una manera, parecía ser de un hermoso color plateado, pero cuando lo giró pareció cambiar primero a rojo, luego a morado y luego una vez más a plateado.
          - **Pastkeeper Sharrigan:** Se llevó la perla a casa y se preguntó cuál sería la mejor manera de usarla, cuando escuchó un golpe en la puerta. Al contestar, fue recibida por una mujer, con escamas de hermosa plata y largas túnicas a juego.
          - **Guarda del pasado Sharrigan:** 'He venido por mi perla', dijo. Omisha estaba confundida, porque la mujer no podía afirmar que poseía una concha y la despidió con rudeza.
          - **Guarda del pasado Sharrigan:** A la noche siguiente, volvieron a llamar a su puerta. En la puerta había una mujer que parecía idéntica a la primera, excepto que sus escamas eran de un color carmesí intenso. Ella también pidió la perla y fue rechazada.
          - **Guarda del pasado Sharrigan:** La tercera noche, como antes, alguien llamó a la puerta. Esta vez la mujer tenía escamas de un color púrpura intenso y vibrante. Ella pidió la perla y se la negaron como a los demás. "Sólo hemos pedido lo que es nuestro", dijo. 'Tal como nos lo has quitado, nosotros recuperaremos lo que también es nuestro. Hasta que nos devuelvas la perla. Y con eso se fue.
          - **Pastkeeper Sharrigan:** Contenta de no tener nada de lo que le habían dado, Omisha continuó al día siguiente con normalidad. Pero cuando cayó la noche, todo el pueblo quedó sumido en la más profunda oscuridad. Frenéticamente, Omisha buscó la luz de la luna entre las nubes, pero no había señales de lunas en el cielo.
          - **Pastkeeper Sharrigan:** Durante tres semanas no hubo nada más que oscuridad en la noche y ya no pudo escapar de los efectos. Los peces, que necesitaban luz, comenzaron a morir y sólo los pescadores más fuertes los reclamaron. Las cosechas comenzaron a marchitarse y perecer y una hambruna azotó la tierra. Omisha lloró por su codicia y se reprendió a sí misma por su arrogancia.
          - **Pastkeeper Sharrigan:** Con pesar en su corazón, devolvió la perla al agua y añadió sus lágrimas como disculpa. Esa noche las lunas volvieron a brillar.
          - **Pastkeeper Sharrigan:** Quizás vivieron felices para siempre, pero no lo sé, yo no estuve allí.
          - (above|Which story do you wish to hear)
        - El Gurh Estelarpino
          - **Pastkeeper Sharrigan:** Una vez, hace mucho tiempo, una semilla cayó del cielo y aterrizó en el jardín de una joven llamada Fridal.
          - **Pastkeeper Sharrigan:** Fridal era pobre y la granja de su familia estaba fracasando. Sufriendo una terrible plaga que provocó que se arruinaran todas sus cosechas y que sus animales enfermaran.
          - **Pastkeeper Sharrigan:** Fridal encontró la semilla y se maravilló de sus tonos coloridos y texturas brillantes. Temiendo que también se arruinara si lo plantaba en sus campos, lo plantó en la parte oscura del pantano, donde nadie se atrevía a ir.
          - **Guarda del pasado Sharrigan:** Esperaba que se convirtiera en algo hermoso, para que los pantanos fueran menos aterradores.
          - **Guardia del Pasado Sharrigan:** Durante trece días y catorce noches, observó cómo la semilla brotaba y crecía. Para su consternación, no era algo bello. Pero era un árbol retorcido y de aspecto malvado, con ramas largas y blancas que se extendían como garras y un nudo en el tronco que parecía la cara de un gurh enojado.
          - **Pastkeeper Sharrigan:** Sintiendo que todas las cosas tienen su lugar, incluso como leña, cortó el árbol malvado y regresó a su casa. Pero la madera estaba húmeda y no ardía. Para desahogar su frustración, Fridal optó por darle forma y tallar la madera, para que algo feo se volviera hermoso.
          - **Guardia del Pasado Sharrigan:** Talla la madera en un gurh elegante, aunque de aspecto enojado, y lo coloca en el jardín para que pueda vigilar sus cultivos.
          - **Guardia del pasado Sharrigan:** Al día siguiente, descubrió que sus campos estaban repletos de cultivos y que sus animales enfermos estaban sanos. El gurh tallado no se había movido, pero su expresión había cambiado de una de enojo a otra de gentil satisfacción. Fridal sonrió y rió. El árbol había sido feo, pero como ella siempre había pensado, en el fondo era verdaderamente hermoso.
          - **Pastkeeper Sharrigan:** A partir de ese día, las cosechas de Fridal fueron abundantes y sus animales sanos. Siguió mirando al cielo para ver si caía otra semilla. Después de todo, ningún gurh debería estar solo.
          - **Pastkeeper Sharrigan:** Quizás vivieron felices para siempre, pero no lo sé, yo no estuve allí.
          - (above|Which story do you wish to hear)
        - Aliranna y la bestia silbadora
          - **Pastkeeper Sharrigan:** Una vez, hace mucho tiempo, había un joven enamorado y, como suele ocurrir, su amada no tenía idea.
          - **Guarda del pasado Sharrigan:** Incluso nosotros, Ilujanka, podemos sufrir la cruel aflicción de la timidez y Aliranna lo pasó peor que la mayoría.
          - **Pastkeeper Sharrigan:** Lo único que quería era tener el coraje de hablar con ella, de decirle cuánto se preocupaba por ella. Pero las palabras eran como espinas en su garganta y no podía sacarlas.
          - **Pastkeeper Sharrigan:** Hay pocos enemigos tan poderosos como el enemigo dentro de nosotros mismos y el enemigo interno de Aliranna lo odiaba.
          - **Pastkeeper Sharrigan:** Su timidez hizo que desapareciera de la vista de los demás y se volvió tan silencioso como un ratón. Podría cruzar el pueblo en mitad de la noche y nadie sabría que estaba allí.
          - **Pastkeeper Sharrigan:** Si hubiera tenido el corazón frío, podría haber sido un excelente ladrón, pero esa idea nunca se le pasó por la cabeza.
          - **Pastkeeper Sharrigan:** Estaba tan callado y tan fácilmente olvidado que se convirtió en un fantasma. A él no le importó. Mientras la veía de vez en cuando, sentía que valía la pena vivir la vida.
          - **Guardián del pasado Sharrigan:** Pero un día llegó the beast. Una cosa enorme y furiosa, con unas fauces tan anchas que podría tragarse una manada entera de gurh y con ojos tan feroces que cualquiera que se encontrara con su mirada se quedaba helado de terror.
          - **Guarda del Pasado Sharrigan:** Mientras acechaba por la aldea, comiendo y destruyendo a medida que avanzaba, silbaba una extraña melodía que hacía que las aletas en la nuca de las personas se pusieran de punta.
          - **Pastkeeper Sharrigan:** Durante el día asaltaba la aldea, consumía reservas de comida y aterrorizaba a las familias. Por la noche se enroscaba alrededor del gran árbol del centro de la ciudad y caía en un extraño sueño silbante.
          - **Guardián del pasado Sharrigan:** Los guerreros de la aldea intentaban acercarse sigilosamente a la criatura para ahuyentarla, pero cada vez the beast los veía venir.
          - **Pastkeeper Sharrigan:** Un día los gustos de the beast dieron un giro más oscuro. Una noche, robó la luz de la vida de Aliranna y la arrastró hasta su nido.
          - **Guarda del pasado Sharrigan:** Aunque su timidez le gritaba, Aliranna no podía permitir que ella se convirtiera en alimento para the beast, por lo que fue a las marismas y allí recogió tres hojas de la planta jabracat. Las hojas eran mortales al tacto, pero los dedos de Aliranna eran ágiles y no representaban ningún peligro para él.
          - **Guardián del pasado Sharrigan:** Se escabulló en mitad de la noche y se acercó sigilosamente a la criatura. Sus pasos eran silenciosos y cada respiración no era más fuerte que el latido del corazón de un insecto. El mundo lo había olvidado y él usó eso a su favor.
          - **Guardián del pasado Sharrigan:** Mientras the beast dormía, colocó las hojas del árbol de la planta jabracat sobre él. Uno yacía sobre sus ojos, para que los venenos lo cegaran. Uno se colocó sobre su nariz, para que las toxinas le quitaran el sentido del olfato.
          - **Pastkeeper Sharrigan:** El final lo puso en sus labios, de modo que la capa mortal de {{Sic|it's}} podría obligar a the beast a dormir más profundamente. Cuando the beast fue sometido, Aliranna se metió en su nido y rescató a su amor.
          - **Guarda del pasado Sharrigan:** Por la mañana, los guerreros expulsaron a the beast de la aldea y, una semana después, Aliranna finalmente reunió el coraje para cortejar a su amor.
          - **Pastkeeper Sharrigan:** Quizás vivieron felices para siempre, pero no lo sé, yo no estuve allí.
          - (above|Which story do you wish to hear)
        - El cuento de Radri el Rojo
          - **Pastkeeper Sharrigan:** Reúnete y escucha a Radri el Rojo, quien viajó al corazón del mundo en busca de secretos.
          - **Pastkeeper Sharrigan:** Hace mucho tiempo, cuando comienzan estas historias, había un joven guerrero llamado Radri el Rojo. Se llamaba así por sus escamas, que eran de un color carmesí intenso, como ninguna otra.
          - **Guardia del pasado Sharrigan:** Los aldeanos tomaron sus escamas rojas como una señal de que fue elegida por Akash, la gran luna roja y, por lo tanto, estaba destinada a grandes cosas.
          - **Pastkeeper Sharrigan:** Cuando alcanzó la mayoría de edad, la joven guerrera partió por todo el mundo en busca de su destino. Sabiendo que algo maravilloso debía estar esperándola.
          - **Guardia del Pasado Sharrigan:** Viajó a través de montañas, pero no encontró ningún tesoro ni arriba ni abajo. Nadó a través de los ríos más caudalosos, pero ningún espíritu se detuvo para preguntarle acertijos. Incluso desafió los grandes lagos de fuego, pero todo lo que encontró fueron llamas crepitantes y columnas de humo inofensivas.
          - **Pastkeeper Sharrigan:** Durante años vagó por el mundo en busca de su destino, hasta que un día llegó a un gran abismo que parecía caer en el corazón mismo del mundo.
          - **Guardian del pasado Sharrigan:** '¡Hola!' Ella gritó en la oscuridad. Pero sólo el silencio respondió. Habiendo viajado a todos lados, este era el único lugar que le quedaba, así que ató una cuerda alrededor de un árbol cercano y descendió a la oscuridad.
          - **Pastkeeper Sharrigan:** El corazón del mundo es un lugar oscuro, donde las paredes están juntas y el aire flota pesado y denso. A medida que Radri ascendía, cada respiración se hacía más y más fuerte, hasta que sintió que no tendría fuerzas para regresar.
          - **Pastkeeper Sharrigan:** Pero ella sabía que el destino estaba ahí abajo, en el fondo del mundo, así que se armó de valor y descendió.
          - **Pastkeeper Sharrigan:** Después de lo que parecieron días, finalmente llegó al fondo del abismo. A su alrededor solo había oscuridad, y la única fuente de luz era la parpadeante antorcha que sostenía en sus manos. Incluso el sol y las lunas habían abandonado este lugar.
          - **Pastkeeper Sharrigan:** En el corazón del mundo encontró una calma como nunca había sentido. Aunque el aire era denso y pesado, no le quemaba la garganta ni le sofocaba la respiración.
          - **Guarda del Pasado Sharrigan:** Mientras vagaba por las catacumbas bajo tierra, se encontró con la gran cueva iluminada por piedras brillantes que descansaban dentro de las paredes. En el corazón de la habitación había una antigua Ilujanka con escamas tan carmesí como las del propio Radri.
          - **Pastkeeper Sharrigan:** 'Ah, ¿entonces has venido a verme? Por fin. preguntó la anciana. '¿Vienes a buscar el destino?'.
          - **Guarda del Pasado Sharrigan:** Radri asintió, complacida de haber finalmente buscado lo que había buscado todos estos años. Pero la anciana se limitó a reír, con una risa fría y hueca.
          - **Pastkeeper Sharrigan:** Entonces ven, pequeño Radri, toma mi mano y mira cómo es el destino.
          - **Guarda del pasado Sharrigan:** Radri dio un paso adelante, con la mano extendida en señal de triunfo y, mientras avanzaba, su mano tocó la superficie del agua y la anciana se hizo añicos en ondas de colores.
          - **Guardia anterior Sharrigan:** Momentos después, regresó y enfrentó a Radri con la mano extendida para igualar la de Radri.
          - **Pastkeeper Sharrigan:** Fue entonces cuando Radri reconoció a la anciana, porque en sus ojos vio los ojos de su juventud. Había pasado tanto tiempo buscando el destino, que se había vuelto cada vez más vieja. Había abandonado todas las alegrías de la vida en busca de un sueño y ahora era demasiado tarde para buscar otro.
          - **Pastkeeper Sharrigan:** Porque no es sabio insistir en sueños a costa de la vida. Al destino, después de todo, no le gusta que la persigan.
          - **Pastkeeper Sharrigan:** Quizás vivieron felices para siempre, pero no lo sé, yo no estuve allí.
          - (above|Which story do you wish to hear)
        - [Cancelar.]
          - (above|hear-pastkeeper-stories)
  - No.
    - **Pastkeeper Sharrigan:** Quizás en otro momento.

#### Historias de guardianes del pasado


##### Sin tener historias desbloqueadas

- (above|You must train with the other ilujanka here first)

##### Tener historias desbloqueadas

- (above|Which story do you wish to hear)
