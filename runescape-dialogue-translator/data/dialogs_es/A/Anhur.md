# Anhur

- **Original Wiki Page**: [Transcript:Anhur](https://runescape.wiki/w/Transcript%3AAnhur)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Anhur:** ¿Quién eres en Gielinor?

### City quest dialogue

- **Anhur:** ¿Qué quieres? En realidad... si no estás haciendo nada, ¿ser útil?
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Anhur:** Eso será suficiente.
    - (Condition: Si el tipo de misión de la ciudad es "Atacada por vida silvestre":)
      - (continue)
    - (Condition: Si el tipo de misión de la ciudad es "En espera de entrega":)
      - (continue)
    - (Condition: Si el tipo de misión de la ciudad es "Los niños no pueden dormir":)
      - (continue)
    - (Condition: Si el tipo de misión de la ciudad es "Coleccionista de curiosidades":)
      - (continue)
    - (Condition: Si el tipo de misión de la ciudad es "Crondis está enojado":)
      - (continue)
    - (Condition: Si el tipo de misión de la ciudad es "Plagas de cultivos":)
      - (continue)
    - (Condition: Si el tipo de misión de la ciudad es "Ayuda de entrega":)
      - (continue)
    - (Condition: Si el tipo de misión de la ciudad es "El hijo de un amigo muere lentamente":)
      - (continue)
    - (Condition: Si el tipo de misión de la ciudad es "Nuevo producto":)
      - (continue)
    - (Condition: Si el tipo de misión de la ciudad es "Slayer master":)
      - (continue)
    - (Condition: Si el tipo de misión de la ciudad es "esfuerzo War":)
      - (continue)
  - [Choice]: No ahora mismo.
    - **Anhur:** No importa.

#### Atacado por vida silvestre

- {{transcript missing}}

#### Esperando entrega

- **Anhur:** He estado esperando una entrega que contenga algo de [item 1] y algo de [item 2]. Necesito urgentemente el [item 1], pero la gente en el muelle dice que no hay señales del barco en millas.
- (Condition: Si el artículo deseado es mineral de cobre:)
  - **Anhur:** ¿Crees que podrías conseguirme [número]trozos de mineral de cobre? Estoy desesperado por rocas ricas en cobre.
  - **Player:** ¿Dónde podría encontrar un trozo de mineral de cobre?
  - **Anhur:** El mineral de cobre se puede encontrar al sureste de Varrock. ¿Está bien?
  - (continue)
- (Condition: Si el artículo deseado son semillas de agracejo:)
  - **Anhur:** ¿Crees que podrías conseguirme semillas de agracejo [número]? Estoy desesperado por semillas que se conviertan en agracejos.
  - **Player:** ¿Dónde puedo encontrar una semilla de agracejo?
  - **Anhur:** Las semillas de agracejo a menudo las dejan los monstruos, o se pueden conseguir de los maestros agricultores alrededor de Gielinor. ¿Está bien?
  - (continue)
- (Condition: Si el artículo deseado son semillas de romero:)
  - **Anhur:** ¿Crees que podrías conseguirme semillas de romero [número]? Estoy desesperado por semillas que se conviertan en plantas de romero.
  - **Player:** ¿Dónde puedo encontrar una semilla de romero?
  - **Anhur:** Las semillas de romero a menudo las dejan los monstruos, o se pueden conseguir de los maestros agricultores alrededor de Gielinor. ¿Está bien?
  - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Anhur:** Eso será suficiente.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Anhur:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Anhur:** No importa.
      - [Choice]: No.
        - **Anhur:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes [número] [item]? Es bastante urgente. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes [número] [item]? Es bastante urgente. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Anhur ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Anhur:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes [número] [item]? Es bastante urgente. ([número] restantes)
    - **Player:** ¡Sí! Tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Anhur ([número]/[número])
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Tarea #2


##### Primera vez

- **Anhur:** ¡Sí! Gracias.
- **Anhur:** Ahora que está hecho, necesitamos el siguiente bloque de suministros.

##### Después

- **Anhur:** Los siguientes suministros que me faltan son un montón de [item].
- **Player:** ...¿y todavía no han llegado?
- (Condition: Si el artículo deseado son bolsas de alcohol kalphite:)
  - **Anhur:** ¡No! Todo lo que necesito son kalfitas instantáneas, que se pueden invocar desde bolsas y los trabajadores del puerto me dicen que pasarán días antes de que las vea.
  - (continue)
- (Condition: Si el objeto deseado son bastones de batalla de fuego:)
  - **Anhur:** ¡No! Todo lo que necesito es un staff con magia de fuego y los trabajadores del puerto me dicen que pasarán días antes de que los vea.
  - (continue)
- (Condition: Si el artículo deseado son patatas:)
  - **Anhur:** ¡No! Todo lo que necesito es una cosecha de tubérculos y almidón y los trabajadores del puerto me dicen que pasarán días antes de que los vea.
  - (continue)
- **Anhur:** ¿Podrías conseguirme algo para ayudarme por ahora? Acerca de [número] [item] debería funcionar.
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Anhur:** Eso será suficiente.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Anhur:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Anhur:** No importa.
      - [Choice]: No.
        - **Anhur:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes [número] [item]? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Anhur ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Anhur:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes [número] [item]? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Anhur ([número]/[número])
    - **Anhur:** Excelente. Salvando el día con el [item 1] y ahora algunos [item 2], agradezco su generosidad.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Tarea #3

- **Anhur:** Dado que eres tan ingenioso, me pregunto si podrías ahorrarme un viaje por la ciudad...
- **Player:** Continúa…
- (Condition: Si el artículo deseado son tiras de tela:)
  - **Anhur:** Necesito algo de material para vendas para pasar el mes. Aproximadamente [número] tiras de tela me ahorrarán muchos problemas.
  - (continue)
- (Condition: Si el artículo deseado son semillas de malezas enanas:)
  - **Anhur:** Necesito una forma de cultivar arbustos de malezas enanas para pasar el mes. Aproximadamente las semillas de malezas enanas [número] me ahorrarán muchos problemas.
  - (continue)
- (Condition: Si el artículo deseado son cuernos de cabra:)
  - **Anhur:** Necesito suministros de pociones para terminar el mes. Aproximadamente [número] los cuernos de cabra me ahorrarán muchos problemas.
  - (continue)
- **Anhur:** ¿[número] [item] es mucho pedir? ¿Me encontrarás algunos?
- [Menu]: Selecciona una opción
  - [Choice]: Por supuesto.
    - **Anhur:** Eso será suficiente.
  - [Choice]: Es demasiado.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Anhur:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Anhur:** No importa.
      - [Choice]: No.
        - **Anhur:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el artículo deseado son tiras de tela:)
      - **Anhur:** ¿Tienes tiras de tela [número]? Podrías hacerlos en un telar. ([número] restante)
    - (Condition: Si el artículo deseado son semillas de malezas enanas:)
      - **Anhur:** ¿Tienes semillas de hierba enana [número]? Las semillas de malezas enanas a menudo las dejan caer los monstruos, o se pueden obtener de los maestros agricultores alrededor de Gielinor. ([número] restante)
    - (Condition: Si el artículo deseado son cuernos de cabra:)
      - **Anhur:** ¿Tienes cuernos de cabra [número]? Se pueden encontrar cabras alrededor de Nardah o al oeste de Kalphite Hive. ([número] restante)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el artículo deseado son tiras de tela:)
      - **Anhur:** ¿Tienes tiras de tela [número]? Podrías hacerlos en un telar. ([número] restante)
      - (continue)
    - (Condition: Si el artículo deseado son semillas de malezas enanas:)
      - **Anhur:** ¿Tienes semillas de hierba enana [número]? Las semillas de malezas enanas a menudo las dejan caer los monstruos, o se pueden obtener de los maestros agricultores alrededor de Gielinor. ([número] restante)
      - (continue)
    - (Condition: Si el artículo deseado son cuernos de cabra:)
      - **Anhur:** ¿Tienes cuernos de cabra [número]? Se pueden encontrar cabras alrededor de Nardah o al oeste de Kalphite Hive. ([número] restante)
      - (continue)
    - (removes=the requested items)
    - Número de [item] dado a Anhur ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Anhur:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el artículo deseado son tiras de tela:)
      - **Anhur:** ¿Tienes tiras de tela [número]? Podrías hacerlos en un telar. ([número] restante)
      - (continue)
    - (Condition: Si el artículo deseado son semillas de malezas enanas:)
      - **Anhur:** ¿Tienes semillas de hierba enana [número]? Las semillas de malezas enanas a menudo las dejan caer los monstruos, o se pueden obtener de los maestros agricultores alrededor de Gielinor. ([número] restante)
      - (continue)
    - (Condition: Si el artículo deseado son cuernos de cabra:)
      - **Anhur:** ¿Tienes cuernos de cabra [número]? Se pueden encontrar cabras alrededor de Nardah o al oeste de Kalphite Hive. ([número] restante)
      - (continue)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Anhur ([número]/[número])
    - **Anhur:** ¡Muchas gracias por ayudarme!
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

#### Los niños no pueden dormir


##### Tarea #1

- **Anhur:** Estoy exhausto porque mis hijos no pueden dormir por la noche.
- **Player:** Oh, eso es horrible, ¿por qué no pueden dormir?
- **Anhur:** Mi hijo mayor tiene demasiado miedo para dormir debido al [monster].
- **Anhur:** ¿Podrías ir a buscar algunos [monster] y reducir sus números?
- **Player:** Parece un poco excesivo... ¿Con cuántos tendría que lidiar?
- **Anhur:** ¿Podrías matar a [número] [monster] por mí?
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Anhur:** Eso será suficiente.
    - **Player:** ¿Dónde puedo encontrar [monster]?
    - (Condition: Si el monstruo asignado son matones menafitas:)
      - **Anhur:** Fueron exiliados. Se rumorea que se han instalado en Pollnivneach. Eso es lo que he oído.
    - (Condition: Si el monstruo asignado son guardias del campamento minero:)
      - **Anhur:** El campamento minero está en algún lugar del desierto, al norte. Eso es lo que he oído.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Anhur:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Anhur:** No importa.
      - [Choice]: No.
        - **Anhur:** No importa.

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Se ocuparon del [número] [monster]? ([número] restantes)
    - **Player:** Todavía no. ¿Dónde podría encontrar [monster] nuevamente?
    - (Condition: Si el monstruo asignado son matones menafitas:)
      - **Anhur:** Fueron exiliados. Se rumorea que se han instalado en Pollnivneach.
    - (Condition: Si el monstruo asignado son guardias del campamento minero:)
      - **Anhur:** El campamento minero está en algún lugar del desierto, al norte.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Se ocuparon del [número] [monster]? ([número] restantes)
    - **Player:** Sí, el [monster] no volverá a asustar a tu hijo en el corto plazo.
    - (receives=Slayer experience)
    - **Anhur:** Gracias. Por excesivo que pareciera, ¡era necesario!
    - **Anhur:** Ahora que puede dormir tranquilo, hablemos de mi hija.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea #2

- **Anhur:** Desde que era pequeña, no puede dormir sin [item].
- **Player:** Correcto. ¿Por qué [item]?
- **Anhur:** Sí, sé que es un poco extraño, pero [item] era lo único que la ayudaría a quedarse dormida.
- **Anhur:** Entonces, por favor, si pudieras conseguir [número] [item], te lo agradecería mucho.
- [Menu]: Selecciona una opción
  - [Choice]: Muy bien.
    - **Anhur:** Eso será suficiente.
    - **Player:** ¿Sabes dónde puedo conseguir [item]?
    - (Condition: Si el artículo deseado es mineral de cobre:)
      - **Anhur:** El mineral de cobre se puede encontrar al sureste de Varrock.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Anhur:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Anhur:** No importa.
      - [Choice]: No.
        - **Anhur:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Ya has encontrado [número] [item]? ([número] restantes)
    - **Player:** No, ¿dónde debería buscar el [item]?
    - (Action: continua)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Ya has encontrado [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Anhur ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Anhur:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Ya has encontrado [número] [item]? ([número] restantes)
    - **Player:** Tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Anhur ([número]/[número])
    - **Anhur:** ¡Excelente, mi hija podrá volver a dormir como un bebé!
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Tarea #3

- **Anhur:** Ahora, mi hijo menor, recientemente perdió su osito de peluche.
- **Player:** ¿Quieres que le busque un nuevo osito de peluche?
- **Anhur:** No, no. Puede que no lo parezca, pero soy bastante hábil en la elaboración. Planeo hacerle uno nuevo si pudieras conseguirme los materiales.
- **Player:** ¿Qué necesitas?
- **Anhur:** Necesito [número] [item] para salir.
- **Player:** ...
- **Anhur:** ...
- **Anhur:** Entonces, ¿podrías conseguirme [número] [item]?
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Anhur:** Eso será suficiente.
    - **Player:** ¿Qué sabes sobre [item]?
    - (Condition: Si el artículo deseado son velas negras:)
      - **Anhur:** He oído que hay un fabricante de velas de renombre en Catherby.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Anhur:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Anhur:** No importa.
      - [Choice]: No.
        - **Anhur:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Trajiste [número] [item]? ¡Este osito de peluche no se construirá solo! ([número] restantes)
    - **Player:** Todavía no. ¿Podrías indicarme la dirección de algún [item]?
    - (Action: continua)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Trajiste [número] [item]? ¡Este osito de peluche no se construirá solo! ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Anhur ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Anhur:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Trajiste [número] [item]? ¡Este osito de peluche no se construirá solo! ([número] restantes)
    - **Player:** Sí, he traído el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Anhur ([número]/[número])
    - **Player:** Entonces, ¿cómo se hace un osito de peluche con...?
    - **Player:** No. Creo que es mejor no saberlo.
    - **Anhur:** ¡Excelente! ¡Me pondré manos a la obra!
    - **Anhur:** Entonces, mi otro hijo...
    - **Player:** Eh... Adiós.
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

#### Coleccionista de curiosidades


##### Tarea #1

- **Anhur:** Soy un coleccionista de curiosidades y actualmente tengo la mayor colección de [item] de todo Menaphos.
- **Anhur:** Bueno, lo hice...
- **Player:** ¿Qué pasó?
- **Anhur:** Otro coleccionista ha llegado a la ciudad y su colección eclipsa la mía.
- **Player:** ¿Cuántos [item] más tienen?
- **Anhur:** He oído que tienen [número] más [item] que yo.
- **Player:** Entonces, si alguien te trajera [número] [item], ¿volverías a tener la mejor colección?
- **Anhur:** ¡Sí! ¿Harías esto por mí?
- [Menu]: Selecciona una opción
  - [Choice]: Bien, entonces.
    - **Anhur:** Eso será suficiente.
    - **Player:** ¿Dónde puedo encontrar [item]?
    - (Condition: Si el artículo deseado son huesos de dragón:)
      - **Anhur:** Mata algunos dragones y recupera sus huesos.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - {{transcript missing}}
      - [Choice]: No.
        - **Anhur:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes el [número] [item]? ([número] restantes)
    - **Player:** Todavía no. ¿Dónde podría encontrar [item] nuevamente?
    - (Action: arriba)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes el [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Anhur ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Anhur:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes el [número] [item]? ([número] restantes)
    - **Player:** ¡Sí, tengo el [item]!
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Anhur ([número]/[número])
    - **Anhur:** Bueno, supongo que esto es un comienzo...
    - **Player:** ¿Un comienzo?
    - **Anhur:** Acabo de enterarme de que mi rival acaba de traer un nuevo envío de [item]...
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Tarea #2

- **Anhur:** Escuchó que me trajiste algo de [item 1], ahora tiene [número] más [item 2] que yo, solo para fastidiarme.
- **Player:** ¿Qué significa eso para ti?
- **Anhur:** ¡Esto es una carrera armamentista! Necesitas conseguirme [número] más [item 2].
- **Player:** ¿Coleccionas [item 1] Y [item 2]?
- **Anhur:** ¡Colecciono muchas cosas! ¡Colecciono colecciones!
- **Player:** ...
- **Anhur:** Entonces, sobre esos [número] más [item 2]...
- [Menu]: Selecciona una opción
  - [Choice]: Bien, está bien.
    - **Anhur:** Eso será suficiente.
    - (Condition: Si el artículo deseado es mineral de cobre:)
      - **Anhur:** El mineral de cobre se puede encontrar al sureste de Varrock.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - {{transcript missing}}
      - [Choice]: No.
        - **Anhur:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Ya tienes [número] [item]? ([número] restantes)
    - **Player:** No, ¿dónde puedo encontrar el [item] nuevamente?
    - (Action: arriba)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Ya tienes [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Anhur ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Anhur:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Ya tienes [número] [item]? ([número] restantes)
    - **Player:** Tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Anhur ([número]/[número])
    - **Anhur:** Muchas gracias.
    - **Player:** No hay problema.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Tarea #3

- **Anhur:** ¿Quizás podrías hacerme un pequeño trabajo más?
- **Player:** ¿Se trata de [item 1] o [item 2]?
- **Anhur:** ¡No, por supuesto que no!
- **Player:** ¿En serio?
- **Anhur:** ...
- **Anhur:** Sí, lo prometo, ¡necesito [número] más [item] para mi colección final!
- **Anhur:** Esta es la última vez que pregunto. Prometo.
- **Anhur:** [number] [item]?
- [Menu]: Selecciona una opción
  - [Choice]: [number] [item]...
    - **Anhur:** Eres una buena persona.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - {{transcript missing}}
      - [Choice]: No.
        - **Anhur:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes el [item]? Necesito [número]. ([número] restantes)
    - **Player:** Todavía no. ¿Podrías indicarme la dirección de algún [item]?
    - (Condition: Si el artículo deseado son rollos de tela:)
      - **Anhur:** Podrías hacerlos en un telar.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes el [item]? Necesito [número]. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Anhur ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Anhur:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Anhur:** ¿Tienes el [item 3]? Necesito [número]. ([número] restantes)
    - **Player:** Sí, pero no les daré más [item 3], [item 1] O [item 2] después de esto.
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Anhur ([número]/[número])
    - **Anhur:** ¡Finalmente, una vez más tengo la mayor colección de [item 3] en Menaphos!
    - **Player:** ¿Qué planeas hacer con [item 1], [item 2] y [item 3] ahora que los tienes?
    - **Anhur:** Realmente no lo sé.
    - **Player:** Bueno, entonces...
    - **Player:** Buena suerte con eso.
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

#### Crondis está enojado

- {{transcript missing}}

#### Plagas de cultivos

- {{transcript missing}}

#### Ayuda de entrega

- {{transcript missing}}

#### El hijo de un amigo está muriendo lentamente.

- {{transcript missing}}

#### Nuevo producto

- {{transcript missing}}

#### esfuerzo War

- {{transcript missing}}
