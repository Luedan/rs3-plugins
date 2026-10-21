# Blurberry

- **Original Wiki Page**: [Transcript:Blurberry](https://runescape.wiki/w/Transcript%3ABlurberry)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Cocktail training


#### Empezando

- **Player:** Hola.
- **Blurberry:** Bueno, hola viajero. Si está buscando un cóctel, el barman estará encantado de prepararle uno.
- **Blurberry:** O si estás buscando capacitación en preparación de cócteles, ¡soy tu gnomo! Aluft Gianne jnr. está buscando cocineros y camareros gnomos que le ayuden en su nueva empresa, por lo que es una habilidad útil.
- Seleccione una opción
  - No gracias, prefiero quedarme de este lado de la barra.
    - **Player:** No gracias, prefiero quedarme de este lado de la barra.
  - Ok, entonces lo intentaré.
    - **Player:** Ok, entonces lo intentaré.
    - **Blurberry:** Excelente. No es un trabajo fácil, tendré que probarte primero. Aunque estoy seguro de que te irá genial.
    - (receives=cocktail guide)
    - **Blurberry:** Toma, toma esta guía de cócteles. El libro te explica cómo preparar todos los cócteles que servimos. Te diré lo que necesito y podrás hacerlos.
    - **Player:** Suena bastante fácil.
    - **Blurberry:** Echa un vistazo al libro y luego ven a hablar conmigo.

#### Explosión de frutas

- **Player:** Hola Blurberry.
- **Blurberry:** Hola, ¿estás listo para preparar tu primer cóctel?
- **Player:** Absolutamente.
- *Si el player no tiene suficiente espacio en el inventario:*
  - **Blurberry:** Oh, no tienes suficiente espacio para llevar los artículos. Vuelve cuando lo hagas.
- *Si el player tiene suficiente espacio:*
  - **Blurberry:** Bueno, entonces, para empezar, haz un Fruit Blast. Toma, necesitarás estos ingredientes, pero me temo que no puedo darte más si te equivocas.
  - (receives=two lemons, an orange, a pineapple, a cocktail glass, a knife and a cocktail shaker)
  - Blurberry te regala dos limones, una naranja, una piña, una coctelera, un vaso y un cuchillo.

#### Ponche de piña

- **Blurberry:** Entonces, ¿dónde está mi Fruit Blast?
- *Si el player no tiene coctelera:*
  - (continue|get-shaker)
- *Si el player no tiene Fruit Blast:*
  - **Blurberry:** ¡No sé qué tienes ahí, pero no es Fruit Blast!
- *Si el player tiene Fruit Blast:*
  - **Player:** Aquí tienes.
  - Le das a Blurberry el Fruit Blast. Él toma un sorbo...
  - **Blurberry:** Hmmm... no está mal, nada mal.
  - *Si el player no tiene suficiente espacio en el inventario:*
    - **Blurberry:** ¡Podremos continuar tu entrenamiento cuando tengas suficiente espacio para guardar los ingredientes para un ponche de piña!
  - *Si el player tiene suficiente espacio:*
    - **Blurberry:** ¿Ahora puedes prepararme un ponche de piña? Puedo darte lo que necesitas, pero nuevamente no podré darte más si cometes un error.
    - (removes=Fruit Blast) (receives=a cocktail glass, three pineapples, a lemon, a lime and two oranges)
    - Blurberry te regala tres piñas, un par de naranjas, un limón y una lima.
    - **Blurberry:** Avísame cuando esté listo.

#### Asistente de Blizzard

- **Player:** Hola Blurberry.
- **Blurberry:** ¿Cómo te va con el ponche de piña?
- *Si el player no tiene coctelera:*
  - (continue|get-shaker)
- *Si el player no tiene ponche de piña:*
  - **Blurberry:** No sé qué tienes ahí, ¡pero no es ponche de piña!
- *Si el player tiene ponche de piña:*
  - **Player:** Aquí tienes.
  - Le das a Blurberry el ponche de piña. Él toma un sorbo...
  - **Blurberry:** Nada mal, nada mal... Ciertamente puedo vender bebidas de esa calidad.
  - *Si el player no tiene suficiente espacio en el inventario:*
    - **Blurberry:** ¡Podremos continuar tu entrenamiento cuando tengas suficiente espacio para guardar los ingredientes para una Wizard Blizzard!
  - *Si el player tiene suficiente espacio:*
    - **Blurberry:** ¡Bien, entonces probemos algo que contenga algo de alcohol de verdad! Hazme un mago Blizzard.
    - (removes=Pineapple Punch) (receives=a cocktail glass, two vodka bottles, a bottle of gin, an orange, a pineapples, a lemon and two limes)
    - Blurberry te regala vodka, ginebra, un limón, una piña, un par de limas y una naranja.

#### Corto Verde Guy

- **Player:** Hola Blurberry.
- **Blurberry:** Hola, ¿cómo te fue con Wizard Blizzard?
- *Si el player no tiene coctelera:*
  - (continue|get-shaker)
- *Si el player no tiene un Wizard Blizzard:*
  - **Player:** No he logrado hacerlo todavía.
  - **Blurberry:** Ok, necesito un Wizard Blizzard. hecho.
- *Si el player tiene un Wizard Blizzard:*
  - **Player:** Toma, prueba un poco.
  - Le das a Blurberry el Asistente Blizzard. Él toma un sorbo...
  - **Blurberry:** Bueno, eso es Wizardy y Blizzardy. Eres todo un barman. Bien, vamos a ponerte a prueba una vez más. Hazme un SGG y luego veremos si tienes lo necesario.
  - **Player:** ¿Un qué?
  - **Blurberry:** Un Guy verde corto. Tengo los ingredientes aquí...
  - (removes=Wizard Blizzard) (receives=a cocktail glass, a bottle of vodka, four limes and equa leaves)
  - **Player:** Ok, haré lo mejor que pueda.
  - **Blurberry:** Estoy seguro de que serás un gran barman.

#### Terminando

- **Player:** Hola Blurberry.
- **Blurberry:** Entonces, ¿tienes mi Short Green Guy?
- *Si el player no tiene coctelera:*
  - (continue|get-shaker)
- *Si el player no tiene un Guy verde corto:*
  - **Blurberry:** ¡No sé qué tienes ahí, pero no es SGG!
- *Si el player tiene un Guy verde corto:*
  - **Player:** Aquí tienes.
  - Le das a Blurberry el SGG. Él toma un sorbo...
  - (removes=Short Green Guy)
  - **Blurberry:** Oh, ese es un número pequeño y juguetón. Muy ácido, como debe ser. Excelente. Bueno, estoy feliz de recomendarte a los Giannes. Realmente eres un camarero gnomo ahora...
  - *Si el player aún no ha completado la formación de cocina Gnome con Aluft Gianne snr.:*
    - **Blurberry:{{anchor|training-halffinished}}** Bueno, tu entrenamiento ha terminado Player. ¿Estás interesado en algún trabajo?
    - **Player:** Puede que sea...
    - **Blurberry:** Creo que ya casi estás listo para trabajar un poco para Aluft Gianne Jnr. Está a cargo de un nuevo emprendimiento familiar: Gnome Food Delivery. Hay buenos consejos que puedes dar si preparas y entregas alimentos para gnomos, aunque es posible que tengas que viajar por todo Gielinor para cumplir con algunos de los otros pedidos...
    - **Blurberry:** Sin embargo, necesitarás algo de formación básica en cocina de gnomos si quieres trabajar para Lufty. Vaya y charle con su Dad, Aluft Gianne Snr. Él te dirá lo que debes hacer.
    - **Player:** ¡Gracias por tu ayuda!
  - *Si el player ha completado la formación de cocina Gnome con Aluft Gianne snr.:*
    - **Blurberry:{{anchor|training-finished}}** Aluft Gianne Sr. me dice que has terminado de entrenar con él, así que creo que estás listo para trabajar un poco para Aluft Gianne Jnr. Está a cargo del nuevo servicio de entrega de comida Gnome. He oído que se pueden dar buenos consejos si preparas y entregas comida de gnomos, aunque es posible que tengas que viajar por todo Gielinor para cumplir con algunos de los otros pedidos...
    - **Player:** Suena interesante....
    - **Blurberry:** Ve y charla con mi joven Lufty Jnr. y él te pondrá al día con los detalles.

#### Si el player pierde la coctelera

- Seleccione una opción{{anchor|get-shaker}}
  - Me temo que perdí la coctelera que me diste.
    - **Player:** Me temo que perdí la coctelera que me diste.
    - (receives=cocktail shaker)
    - **Blurberry:** Puedo ver cómo eso dificultaría la preparación de cócteles. Te daré otro, pero por favor intenta no perder más.
  - Aún no he terminado.
    - **Player:** Aún no he terminado.
    - **Blurberry:** Ok, avísame cuando hayas terminado.

### After finishing cocktail training

- ''Si aún no has terminado el entrenamiento de cocina de gnomos
  - (arriba2|entrenamiento-a medio terminar)
- ''Si has terminado el entrenamiento de cocina de gnomos
  - (arriba2|entrenamiento-terminado)

### During the advanced NovtumberFest Bar Crawl

- **Player:** Estoy haciendo el recorrido por el bar NovtumberFest.
- **Blurberry:** ¡Ah, has llegado a la mejor parada de tu lista! La mejor bebida que tenemos; ¡un dragón borracho! Te costará 10 coins.
- Se han eliminado 10 coins de tu bolsa de dinero.
- Compras un Dragón Borracho.
- Tu boca y garganta arden mientras lo tragas.
- ¡Has completado una de las tareas en tu tarjeta de rastreo de bares!
