# Hisamitsu

- **Original Wiki Page**: [Transcript:Hisamitsu](https://runescape.wiki/w/Transcript%3AHisamitsu)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Missing city quest dialogue.}}

### Standard dialogue

- **Hisamitsu:** Esta ciudad es a la vez cálida y fría.

### City quest dialogue

- **Hisamitsu:** Oye, amigo mío, ¿podrías ayudarme?
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Hisamitsu:** Eres amable y amable.
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
    - **Hisamitsu:** Ay...

#### Atacado por vida silvestre

- {{transcript missing}}

#### Esperando entrega


##### Tarea #1

- **Hisamitsu:** He estado esperando una entrega que contenga algo de [item 1] y algo de [item 2]. Necesito urgentemente el [item 1], pero la gente en el muelle dice que no hay señales del barco en millas.
- (Condition: Si el artículo deseado son semillas de agracejo:)
  - **Hisamitsu:** ¿Crees que podrías conseguirme semillas de agracejo [número]? Estoy desesperado por semillas que se conviertan en agracejos.
  - **Player:** ¿Dónde puedo encontrar una semilla de agracejo?
  - **Hisamitsu:** Las semillas de agracejo a menudo las dejan los monstruos, o se pueden conseguir de los maestros agricultores alrededor de Gielinor. ¿Está bien?
  - (continue)
- (Condition: Si el artículo deseado son semillas de romero:)
  - **Hisamitsu:** ¿Crees que podrías conseguirme semillas de romero [número]? Estoy desesperado por semillas que se conviertan en plantas de romero.
  - **Player:** ¿Dónde puedo encontrar una semilla de romero?
  - **Hisamitsu:** Las semillas de romero a menudo las dejan los monstruos, o se pueden conseguir de los maestros agricultores alrededor de Gielinor. ¿Está bien?
  - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Hisamitsu:** Eres amable y amable.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Hisamitsu:** Ay...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Hisamitsu:** Ay...
      - [Choice]: No.
        - **Hisamitsu:** Ay...

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Hisamitsu:** ¿Tienes [número] [item]? Es bastante urgente. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Hisamitsu:** ¿Tienes [número] [item]? Es bastante urgente. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Hisamitsu ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Hisamitsu:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Hisamitsu:** ¿Tienes [número] [item]? Es bastante urgente. ([número] restantes)
    - **Player:** ¡Sí! Tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Hisamitsu ([número]/[número])
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2


##### Primera vez

- **Hisamitsu:** ¡Sí! Gracias.
- **Hisamitsu:** Ahora que está hecho, necesitamos el siguiente bloque de suministros.

##### Después

- **Hisamitsu:** Los siguientes suministros que me faltan son un montón de [item].
- **Player:** ...¿y todavía no han llegado?
- (Condition: Si el objeto deseado son bastones de batalla de fuego:)
  - **Hisamitsu:** ¡No! Todo lo que necesito es un staff con magia de fuego y los trabajadores del puerto me dicen que pasarán días antes de que los vea.
  - (continue)
- (Condition: Si el artículo deseado son patatas:)
  - **Hisamitsu:** ¡No! Todo lo que necesito es una cosecha de tubérculos y almidón y los trabajadores del puerto me dicen que pasarán días antes de que los vea.
  - (continue)
- **Hisamitsu:** ¿Podrías conseguirme algo para ayudarme por ahora? Acerca de [número] [item] debería funcionar.
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Hisamitsu:** Eres amable y amable.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Hisamitsu:** Ay...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Hisamitsu:** Ay...
      - [Choice]: No.
        - **Hisamitsu:** Ay...

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Hisamitsu:** ¿Tienes [número] [item]? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Hisamitsu:** ¿Tienes [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Hisamitsu ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Hisamitsu:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Hisamitsu:** ¿Tienes [número] [item]? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Hisamitsu ([número]/[número])
    - **Hisamitsu:** Excelente. Salvando el día con el [item 1] y ahora algunos [item 2], agradezco su generosidad.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Hisamitsu:** Dado que eres tan ingenioso, me pregunto si podrías ahorrarme un viaje por la ciudad...
- **Player:** Continúa...
- (Condition: Si el artículo deseado son semillas de malezas enanas:)
  - **Hisamitsu:** Necesito una forma de cultivar arbustos de malezas enanas para pasar el mes. Aproximadamente las semillas de malezas enanas [número] me ahorrarán muchos problemas.
  - (continue)
- (Condition: Si el artículo deseado son cuernos de cabra:)
  - **Hisamitsu:** Necesito suministros de pociones para terminar el mes. Aproximadamente [número] los cuernos de cabra me ahorrarán muchos problemas.
  - (continue)
- **Hisamitsu:** ¿[número] [item] es mucho pedir? ¿Me encontrarás algunos?
- [Menu]: Selecciona una opción
  - [Choice]: Por supuesto.
    - **Hisamitsu:** Eres amable y amable.
  - [Choice]: Es demasiado.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Hisamitsu:** Ay...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Hisamitsu:** Ay...
      - [Choice]: No.
        - **Hisamitsu:** Ay...

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el artículo deseado son semillas de malezas enanas:)
      - **Hisamitsu:** ¿Tienes semillas de hierba enana [número]? Las semillas de malezas enanas a menudo las dejan caer los monstruos, o se pueden obtener de los maestros agricultores alrededor de Gielinor. ([número] restante)
    - (Condition: Si el artículo deseado son cuernos de cabra:)
      - **Hisamitsu:** ¿Tienes cuernos de cabra [número]? Se pueden encontrar cabras alrededor de Nardah o al oeste de Kalphite Hive. ([número] restante)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el artículo deseado son semillas de malezas enanas:)
      - **Hisamitsu:** ¿Tienes semillas de hierba enana [número]? Las semillas de malezas enanas a menudo las dejan caer los monstruos, o se pueden obtener de los maestros agricultores alrededor de Gielinor. ([número] restante)
      - (continue)
    - (Condition: Si el artículo deseado son cuernos de cabra:)
      - **Hisamitsu:** ¿Tienes cuernos de cabra [número]? Se pueden encontrar cabras alrededor de Nardah o al oeste de Kalphite Hive. ([número] restante)
      - (continue)
    - (removes=the requested items)
    - Número de [item] dado a Hisamitsu ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Hisamitsu:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el artículo deseado son semillas de malezas enanas:)
      - **Hisamitsu:** ¿Tienes semillas de hierba enana [número]? Las semillas de malezas enanas a menudo las dejan caer los monstruos, o se pueden obtener de los maestros agricultores alrededor de Gielinor. ([número] restante)
      - (continue)
    - (Condition: Si el artículo deseado son cuernos de cabra:)
      - **Hisamitsu:** ¿Tienes cuernos de cabra [número]? Se pueden encontrar cabras alrededor de Nardah o al oeste de Kalphite Hive. ([número] restante)
      - (continue)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Hisamitsu ([número]/[número])
    - **Hisamitsu:** ¡Muchas gracias por ayudarme!
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

#### Los niños no pueden dormir

- {{transcript missing}}

#### Coleccionista de curiosidades

- {{transcript missing}}

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

#### Slayer master

- {{transcript missing}}

#### esfuerzo War

- {{transcript missing}}
