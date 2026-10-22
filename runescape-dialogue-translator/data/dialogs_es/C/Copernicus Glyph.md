# Copernicus Glyph

- **Original Wiki Page**: [Transcript:Copernicus Glyph](https://runescape.wiki/w/Transcript%3ACopernicus%20Glyph)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Initial dialogue

- (Condition: First time:)
  - **Copernicus Glyph:** No, no, no... ¡Nunca terminaré con esto!
  - (continue)
- (Condition: Subsequent times, before asking what should be done, he opens with this line:)
  - **Copernicus Glyph:** Si pudiera obtener un poco de ayuda aquí...
  - (continue)
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Quién eres?
    - **Copernicus Glyph:** Cuando estoy por negocios, soy Copernicus Glyph: Maestro escultor. Sin embargo, mis amigos simplemente me llaman Ernie.
    - **Copernicus Glyph:** Habrás visto mi trabajo sin darte cuenta en muchos pueblos y ciudades.
    - (Condition: If the player has not completed the statue stealing portion of Garden of Tranquility:)
      - **Copernicus Glyph:** Hay una hermosa estatua de Saradomin en Falador. También hice la mayoría de las estatuas alrededor del castillo Lumbridge. Debes pasar y verlos alguna vez. Las esculturas pueden ser bastante inspiradoras.
    - (Condition: If the player has completed the statue stealing portion of Garden of Tranquility:)
      - **Copernicus Glyph:** Tenía algunas estatuas preciosas en Lumbridge y Falador, ¡tal vez demasiado bonitas porque alguien las robó!
      - [Menu]: ¿Qué te gustaría decir?
        - [Choice]: ¡Ja! ¡Robé algunas estatuas!
          - **Copernicus Glyph:** ¡Y simplemente lo dices y me lo dices así! No tienes respeto y claramente no tienes remordimientos. ¡Buen día para ti!
        - [Choice]: Lo siento, robé algunas estatuas para el jardín del castillo Varrock.
          - **Copernicus Glyph:** Ah, he oído que la gente puede ser bastante manipuladora con los aventureros. Te ofrecieron algún tipo de recompensa, sin duda.
          - **Copernicus Glyph:** Bueno, escucharte decir que lo sientes es bueno, muestra remordimiento. Y ahora sé dónde recuperar mi trabajo. Gracias.
          - (initial)
        - [Choice]: Ah, me enteré del robo.
          - **Copernicus Glyph:** Sí, mi trabajo tiende a ocupar un lugar bastante destacado. No me sorprende que se haya corrido la voz.
          - **Copernicus Glyph:** No tengo idea de qué clase de alma egoísta robaría obras maestras destinadas a exhibición pública, pero espero que haya sido una pesadilla para ellos.
          - **Copernicus Glyph:** Necesitarían algún tipo de carrito para ello, y al mismo tiempo evitarían a los guardias.
          - (initial)
        - [Choice]: Que terrible, ¿quién haría tal cosa?
          - **Copernicus Glyph:** No tengo idea de qué clase de alma egoísta robaría obras maestras destinadas a exhibición pública, pero espero que haya sido una pesadilla para ellos.
          - **Copernicus Glyph:** Necesitarían algún tipo de carrito para ello, y al mismo tiempo evitarían a los guardias.
          - (initial)
  - [Choice]: ¿Qué estás intentando hacer?
    - **Copernicus Glyph:** Es lo mismo todos los meses: ¡la estatua de adoración ha sido arruinada!
    - **Copernicus Glyph:** Desmontado por personas que esperaban una reliquia sagrada o por fanáticos que ofendían al dios honrado por la estatua.
    - **Copernicus Glyph:** Molesto, podrías pensar, pero me mantiene trabajando, ¿eh? Estoy intentando reconstruir la estatua, pero me vendría bien una mano. Supongo que no podrás ayudarme, ¿verdad?
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Sí, ¿qué necesito hacer?
        - (below|about)
      - [Choice]: No, no tengo tiempo ahora.
        - **Copernicus Glyph:** Bueno, tal vez más tarde.
  - [Choice]: No importa.
    - (end)

### Standard dialogue


#### Antes de construir una estatua

- (Condition: If the player has never built a statue, he opens with this line:)
  - **Copernicus Glyph:** Bueno, ¿vas a ayudarme o no?
  - (continue)
- (Condition: If the player has previously built a statue, he opens with this line:)
  - **Copernicus Glyph:** ¡Qué bueno verte de nuevo! Tienes la costumbre de aparecer en el momento justo. Me vendría bien una mano otra vez.
  - (continue)
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: Déjame ayudarte.
    - **Copernicus Glyph:** ¡Genial! ¿Recuerdas cómo hacer esto?
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Sí, recuerdo cómo hacer esto.{{anchor|i-remember}}
        - **Copernicus Glyph:** Vale, nunca puedo recordar qué campeón es para qué dios. ¿Cuál es el adecuado para esta zona?
        - [Menu]: ¿Qué campeón? Puedes cambiar de opinión si te equivocas.
          - [Choice]: Juna (Guthix)
            - *(Si el campeón no está relacionado con el dios alineado con el área:)*
              - Da la sensación de que una estatua de <champion> no sería adecuada para la zona y podría molestar a los lugareños. Los fanáticos pueden atacarte si intentas rezar ante la estatua. ¿Estás seguro de que deseas construir esta estatua?
              - [Menu]: ¿Construir una estatua de <champion>?
                - [Choice]: Sí (puede ganar Slayer XP).
                  - **Copernicus Glyph:** ¡Genial! Pongámonos manos a la obra.
                - [Choice]: No, elige de nuevo.
                  - *(Volver a las opciones de selección de campeones)*
            - *(Si el campeón está relacionado con el dios alineado al área:)*
              - Da la sensación de que una estatua de <champion> se adaptaría perfectamente a la zona y no molestaría a ningún local. ¿Estás seguro de que deseas construir esta estatua?
              - [Menu]: ¿Construir una estatua de <champion>?
                - [Choice]: Sí (puede ganar Prayer XP).
                  - **Copernicus Glyph:** ¡Genial! Pongámonos manos a la obra.
                - [Choice]: No, elige de nuevo.
                  - *(Volver a las opciones de selección de campeones)*
          - [Choice]: Zilyana (Saradomin)
            - *(El mismo diálogo para todos los campeones - ver arriba)*
          - [Choice]: K'ril Tsutsaroth (Zamorak)
            - *(El mismo diálogo para todos los campeones - ver arriba)*
          - [Choice]: Graardor (Bandos)
            - *(El mismo diálogo para todos los campeones - ver arriba)*
      - [Choice]: No, ¿puedes recordármelo?
        - **Copernicus Glyph:{{anchor|about}}** Es simple: me alejaré del andamio para poder verlo todo claramente.
        - **Copernicus Glyph:** Estarás al frente ajustando la altura de las cinco columnas de andamios alrededor de la estatua.
        - **Copernicus Glyph:** Te diré cuántos andamios tenemos disponibles para usar y la columna más alta y más baja que debe tener cualquier columna de andamio.
        - **Copernicus Glyph:** Una vez que hayas colocado algunos andamios, pregúntame cómo queda y podré darte algunos consejos para ayudarte a que quede perfecto.
        - **Copernicus Glyph:** Pero recuerda preguntarme; Puedo ver lo que se necesita desde la distancia y estarás demasiado cerca de la estatua para ver el panorama general.
        - **Copernicus Glyph:** Y si has practicado mucho con Construction, la estatua se verá más espectacular. Piedras preciosas y pan de oro: ¡esa es la marca de una estatua de alta calidad!
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: ¿Con qué frecuencia puedo ayudarte?
            - **Copernicus Glyph:** Recibo mis comisiones mensualmente, así que ven a verme al comienzo de cada mes calendario para ayudar.
            - **Copernicus Glyph:** Cualquier estatua que hayas construido anteriormente probablemente ya estará arruinada para entonces, por lo que tendrás que restaurarla.
            - **Copernicus Glyph:** ¡Eso significa más experiencia para ti!
            - [Menu]: ¿Qué te gustaría decir?
              - *(Muestra opciones de diálogo estándar - ver más abajo)*
          - [Choice]: Bueno.
            - (above|i-remember)
  - [Choice]: Cuéntame sobre trabajar en esta área.
    - (abajo)
  - [Choice]: Háblame de los lugareños.
    - (abajo)
  - [Choice]: Hablemos de recompensas.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Cuénteme sobre las habilidades que puedo mejorar.
        - **Copernicus Glyph:** Trabajando junto a un maestro escultor mejorarás tus habilidades en la construcción. Rezar ante una estatua que honra al dios local debe mejorar tu conexión con lo divino.
        - **Player:** ¿Y si construyo una estatua para honrar a un dios que los lugareños no siguen?
        - **Copernicus Glyph:** ¡Buen punto! A los fanáticos de la zona no les agradará eso. Pero probablemente podrías obtener una idea de los métodos de lucha especializados ahuyentándolos.
        - **Copernicus Glyph:** Esa es una de las razones por las que las estatuas nunca duran mucho. ¡Tendré que vigilar a esos fanáticos!
        - (previous)
      - [Choice]: Háblame del cincel de construcción.
        - **Copernicus Glyph:** Si demuestras compromiso con nuestro trabajo y con un dios en particular, te recompensaré con un cincel de construcción. Hacer al menos una estatua de un dios en particular durante cuatro meses; eso debería mostrar suficiente dedicación.
        - **Copernicus Glyph:** ¡El cincel no solo aumentará tu habilidad, sino que también te permitirá mejorarla más rápidamente!
        - (previous)
      - [Choice]: Me gustaría reclamar un cincel de construcción.
        - *(Si el player no es elegible para reclamar un cincel divino:)*
          - **Copernicus Glyph:** Parece que todavía no te has dedicado lo suficiente a un solo dios como para ganarte uno de sus cinceles.
        - *(Si el player es elegible para reclamar solo un cincel divino:)*
          - *(El diálogo continúa directamente para reclamar el cincel disponible.)*
        - *(Si el player es elegible para reclamar más de un cincel divino:)*
          - **Copernicus Glyph:** ¿Qué cincel te gustaría?
          - [Menu]: ¿Qué cincel te gustaría?
            - [Choice]: Cincel para esculpir (Saradomin)
              - (receives=sculpting chisel (Saradomin))
              - Copérnico te entrega un cincel para esculpir teñido de azul saradominista.
              - (continue)
            - [Choice]: Cincel para esculpir (Zamorak)
              - (receives=sculpting chisel (Zamorak))
              - Copérnico te entrega un cincel para esculpir teñido de rojo zamorak.
              - (continue)
            - [Choice]: Cincel para esculpir (Guthix)
              - (receives=sculpting chisel (Guthix))
              - Copérnico te entrega un cincel para esculpir teñido de verde Guthixiano.
              - (continue)
            - [Choice]: Cincel para esculpir (Bandos)
              - (receives=sculpting chisel (Bandos))
              - Copérnico te entrega un cincel para esculpir teñido de negro bandosiano.
              - (continue)
          - **Copernicus Glyph:** Ahí lo tienes entonces. Eso le dará un impulso a tu habilidad en la construcción cuando lo uses, además de permitirte aprender más rápidamente a medida que practicas tu construcción.
          - (initial)
      - [Choice]: Hablemos de recompensas más tarde.
        - (previous2)
  - [Choice]: Más...
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Quién eres?
        - (arriba)
      - [Choice]: ¿Qué estás intentando hacer?
        - (arriba)
      - [Choice]: Hablemos de otra cosa.
        - (previous2)
      - [Choice]: No importa.
        - (end)

#### Intentando construir sin un seguidor

- **Copernicus Glyph:** No puedo concentrarme en esculpir con criaturas por todos lados. Deshazte de tu seguidor si quieres ayudarme.

#### Construyendo una estatua


##### Introducción

- **Copernicus Glyph:** Necesitaremos utilizar todas las piezas de andamio <number>.
- **Copernicus Glyph:** El andamio más alto que necesitaremos son bloques <number>.
- **Copernicus Glyph:** El andamio más bajo que necesitaremos son bloques <number> de altura.

##### Pidiendo consejo sobre el andamio

*Si no ha utilizado todas las piezas del andamio:*
- **Copernicus Glyph:** ¡No estás usando suficientes andamios!
*Si intenta utilizar más andamios que la cantidad prevista:*
- **Copernicus Glyph:** Ya no quedan andamios. Primero deberás quitar el andamio de otra columna.
*Si utiliza todos los andamios pero la columna más baja es inferior al mínimo especificado:*
- **Copernicus Glyph:** Casi, la columna más baja está un poco baja en este momento.
*Si utiliza todos los andamios pero la columna más alta es inferior al máximo especificado:*
- **Copernicus Glyph:** ¡Necesitamos llegar más alto que eso!
*Posibles líneas si una columna tiene la cantidad correcta de andamio:*
- **Copernicus Glyph:** ¡Brillante! ¡La primera columna es perfecta!
- **Copernicus Glyph:** ¡Buen progreso! ¡La cuarta columna es perfecta!
- **Copernicus Glyph:** ¡Ahí vamos, la última columna es perfecta!
*Posibles líneas si una columna tiene más andamiaje del necesario:*
- **Copernicus Glyph:** Parece que la primera columna es demasiado alta.
- **Copernicus Glyph:** No, la segunda columna es demasiado alta.
- **Copernicus Glyph:** ¡Vaya, la última columna es demasiado alta!
*Si todas las columnas tienen la cantidad adecuada de andamio:*
éxito
- **Copernicus Glyph:** ¡Sí! ¡Exactamente! ¡Esto es lo que quería!
- (Action: Si está habilitado, se produce una escena de el player y Copernicus Glyph construyendo la estatua.)

##### Completando la estatua

- Recibirás <number> Construction XP por completar la estatua.
- **Copernicus Glyph:** Gracias por toda tu ayuda. Realmente hicimos una obra maestra, ¿no? Sin duda, la estatua volverá a necesitar atención el próximo mes. Bueno, también puedes rezar ante la estatua mientras estás aquí.

#### Después de construir una estatua


##### Orando ante la estatua

- *(Si la estatua construida está relacionada con el dios alineado con el área:)*
  - Tu oración honra a <god>.
  - **Copernicus Glyph:** Parece que has elegido la estatua adecuada para esta zona, así que no te preocupes por que los fanáticos te ataquen aquí.
- *(Continúa con una de las siguientes líneas, dependiendo de la cantidad de estatuas completadas :)*
  - **Copernicus Glyph:** Bien, ese es otro trabajo bien hecho. Es un buen comienzo, pero aún quedan cuatro estatuas más.
  - **Copernicus Glyph:** Bien, ese es otro trabajo bien hecho. Estamos progresando, pero todavía me quedan tres estatuas.
  - **Copernicus Glyph:** Bien, ese es otro trabajo bien hecho. Ya estoy en la mitad de mis trabajos. Sólo faltan dos estatuas.
  - **Copernicus Glyph:** Bien, ese es otro trabajo bien hecho. Ya casi termino. Sólo queda una estatua.
- *(Si el player ha construido todas las estatuas:)*
  - **Copernicus Glyph:** ¡Por fin! Es hora de relajarse un rato. No podría haberlo hecho sin ti, por supuesto. ¡Muchas gracias! Voy a pasar algún tiempo contemplando nuestro excelente trabajo. Si vuelves a verme a principios del próximo mes, estoy seguro de que tendré más trabajo para que me ayudes.
- *(Continúa con una de las siguientes líneas, la ubicación es una en la que el player aún no ha construido una estatua :)*
  - **Copernicus Glyph:** La siguiente parada para mí es Falador. Gran ciudad. Egos más grandes. Caballeros brillantes con el plato completo haciendo ruido como si fueran importantes, y no me hagas hablar de su obsesión por el orden. En cualquier caso, también agradecería tu ayuda.
  - **Copernicus Glyph:** Bien, me voy a hacer un trabajo para los druidas en Taverley. Ojalá no vuelvan a intentar pagarme con sus turbias pociones. ¿Por qué no me ayudas con el trabajo?
  - **Copernicus Glyph:** Ahora me voy a Canifis, tengo trabajo que hacer para vampyres. Sé que las condiciones de trabajo son bastante horribles pero, si estás dispuesto, me vendría bien tu ayuda.
  - **Copernicus Glyph:** Hmm, el siguiente es mi trabajo menos favorito. Los ogros son unos empleadores terribles, con su mezcla única de olvido y violencia. Si te unes a mí para ayudar, podré salir de allí en la mitad del tiempo.
- *(Si el player no ha completado Plague's End:)*
  - **Copernicus Glyph:** Me dirijo a algún lugar de Tirannwn, pero no creo que puedas llegar allí todavía. Aunque espero verte allí algún día.
  - (continue)
- *(Si el player ha completado Plague's End:)*
  - **Copernicus Glyph:** ¡A la ciudad élfica de Prifddinas! Te veré allí. Pero no te apresures, me gusta estar allí.
  - (continue)
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: Está bien, nos vemos allí.
    - **Copernicus Glyph:** ¡Genial! Espero volver a trabajar con usted.
  - [Choice]: Quizás en otra ocasión.
    - **Copernicus Glyph:** Ah, bueno, tal vez alguien más me ayude. Gracias por tu ayuda hasta ahora.

##### Hablando con Copérnico después de construir la estatua

- **Copernicus Glyph:** Gracias por toda tu ayuda con la estatua nuevamente. Vuelve a consultar el mes que viene, estoy seguro de que para entonces ya habrá sido destruido. Me vendría bien tu ayuda cuando eso suceda.
- **Copernicus Glyph:** Lo mismo ocurre con las otras estatuas que mantengo. ¿Quién hubiera pensado que estaría tan ocupado? De Falador a Taverley; de Canifis a Gu'Tanoth; ¡Ciertamente me muevo!
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: Cuénteme sobre las habilidades que puedo mejorar.
    - (arriba)
  - [Choice]: Háblame del cincel de construcción.
    - (arriba)
  - [Choice]: Me gustaría reclamar un cincel de construcción.
    - (arriba)
  - [Choice]: Hablemos de recompensas más tarde.
    - (end)

### At Taverley

*(Acerca de trabajar en esta área:)*
- **Copernicus Glyph:** ¡No aceptes bebidas mientras trabajas! Un montón de bichos raros por aquí; ¡Se tragarán cualquier cosa que quepa en un frasco! ¡Algunas de las cosas que les he visto metiendo allí realmente son increíbles! Aun así, es un lugar agradable y tranquilo para trabajar.
*(Acerca de los lugareños:)*
- **Copernicus Glyph:** Siguen hablando de "el equilibrio". Aparentemente eso es algo que sólo Guthix puede aportar. Lo hacen parecer muy noble, pero para mí es sólo una forma de evitar tomar decisiones difíciles. Creo recordar que hay un dicho que dice que el mal gana simplemente porque los hombres buenos no hacen nada. Resulta que lo que se considera equilibrado depende completamente de tu perspectiva.

### At Falador

*(Acerca de trabajar en esta área:)*
- **Copernicus Glyph:** Una hermosa pieza de piedra, una excelente vista desde el cruce hacia Falador... este es un gran lugar para exhibir una estatua. Bueno, no perdamos el tiempo; ¡Démosle a la gente algo que admirar!
*(Acerca de los lugareños:)*
- **Copernicus Glyph:** Si has visto ese gran castillo de paredes blancas, y probablemente lo hayas hecho, te habrás dado cuenta de que son fanáticos del gran niño azul en Falador. Casi todo el mundo aquí adora a Saradomin. Dicen que es un dios benévolo y bondadoso, pero a mí me parece que sus seguidores disfrutan de los puñetazos tanto como cualquier otro.

### At Canifis

*(Acerca de trabajar en esta área:)*
- **Copernicus Glyph:** Es complicado hacer ejercicio aquí. Toda la humedad del aire hace que el polvo de piedra se adhiera a la estatua. Aún así, al menos no respiro gran parte de esa sustancia. Suena mucho más saludable hasta que recuerdas que hay hombres lobo por ahí.
*(Acerca de los lugareños:)*
- **Copernicus Glyph:** Aquí hay principalmente hombres lobo, pero son los vampyres más al este los que pagan por la estatua. Mira, en las Guerras de Dios, los hombres lobo fueron esclavizados por Zamorak para luchar por él. Sin embargo, los vampyres son parte de la vieja guardia de Zamorak y quieren una estatua en su honor para recordarles a los pulgones su lugar.

### At Gu'Tanoth

*(Acerca de trabajar en esta área:)*
- **Copernicus Glyph:** Hagamos esto rápido; No me gusta hacer ejercicio aquí. Los ogros apenas pueden recordar sus propios nombres, sin importar a quién hayan contratado. ¡En un momento me piden que trabaje para ellos y al siguiente me atacan!
*(Acerca de los lugareños:)*
- **Copernicus Glyph:** Ogros, ogros florecientes, como grandes patatas errantes.  Realmente no pueden recordar mucho de su pasado, pero se han transmitido historias sobre Bandos a través de generaciones. No tengo idea de hasta qué punto es cierto, pero esa es la estatua que pidieron. ¡Solo espero que lo recuerden cuando llegue el momento de pagar!

### At Prifddinas

*(Acerca de trabajar en esta área:)*
- **Copernicus Glyph:** ¡Oh, esta ciudad es maravillosa! Conocí su crecimiento a través de Anima Mundi. ¿Puedes creer que esta ciudad surgió de una semilla? Podría retirarme aquí. Es tan pacífico.
*(Acerca de los lugareños:)*
- **Copernicus Glyph:** Los elfos son una raza extraordinaria. No pensarías que acaban de salir de una guerra civil: ¡son tan... civiles! Los elfos fueron muy acogedores. ¡Especialmente cuando les dije que quería construir una estatua de su reina aquí!

### At Lumbridge (Removed)

*(Acerca de trabajar en esta área:)*
- **Copernicus Glyph:** Una hermosa pieza de piedra, una ciudad encantadora, mucha gente alrededor... este es un gran lugar para exhibir una estatua. Bueno, no perdamos el tiempo; ¡Démosle a la gente algo que admirar!
*(Acerca de los lugareños:)*
- **Copernicus Glyph:** Si has visto la iglesia Lumbridge, habrás notado que es saradominista. Casi todo el mundo aquí adora a Saradomin. Dicen que es un dios benévolo y bondadoso, pero a mí me parece que sus seguidores disfrutan de los puñetazos tanto como cualquier otro.
*(Si Lumbridge era el siguiente en la lista, pero aún no lo había visitado:)*
- **Copernicus Glyph:** La siguiente parada para mí es Lumbridge. Bonito lugar, tranquilo. En cualquier caso, si tienes tiempo, te agradecería tu ayuda también.
