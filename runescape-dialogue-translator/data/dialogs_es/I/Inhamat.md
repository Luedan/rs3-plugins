# Inhamat

- **Original Wiki Page**: [Transcript:Inhamat](https://runescape.wiki/w/Transcript%3AInhamat)
- **Letter**: `I`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Inhamat:** Solía ​​ser un comerciante, famoso por mis vinos. Bastan dos malas cosechas seguidas para arruinar a un hombre.

### City quest dialogue

- **Inhamat:** Por favor... dedica algo de tiempo. Realmente me vendría bien un poco de ayuda.
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Inhamat:** Ah... gracias.
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
    - **Inhamat:** No importa.

#### Atacado por vida silvestre

- {{transcript missing}}

#### Esperando entrega


##### Tarea #1

- **Inhamat:** He estado esperando una entrega que contenga algo de [item 1] y algo de [item 2]. Necesito urgentemente el [item 1], pero la gente en el muelle dice que no hay señales del barco en millas.
- (Condition: Si el artículo deseado son semillas de agracejo:)
  - **Inhamat:** ¿Crees que podrías conseguirme semillas de agracejo [número]? Estoy desesperado por semillas que se conviertan en agracejos.
  - **Player:** ¿Dónde puedo encontrar una semilla de agracejo?
  - **Inhamat:** Las semillas de agracejo a menudo las dejan los monstruos, o se pueden conseguir de los maestros agricultores alrededor de Gielinor. ¿Está bien?
  - (continue)
- (Condition: Si el artículo deseado son semillas de romero:)
  - **Inhamat:** ¿Crees que podrías conseguirme semillas de romero [número]? Estoy desesperado por semillas que se conviertan en plantas de romero.
  - **Player:** ¿Dónde puedo encontrar una semilla de romero?
  - **Inhamat:** Las semillas de romero a menudo las dejan los monstruos, o se pueden conseguir de los maestros agricultores alrededor de Gielinor. ¿Está bien?
  - (continue)
- (Condition: Si el artículo deseado son huesos:)
  - **Inhamat:** ¿Crees que podrías conseguirme semillas de romero [número]? Estoy desesperado por algunos huesos viejos y normales, caídos de criaturas.
  - **Player:** ¿Dónde podría encontrar un montón de huesos?
  - **Inhamat:** Casi todos los seres vivos tienen huesos, ¿verdad? No debería ser demasiado difícil encontrar algunos. ¿Está bien?
  - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Inhamat:** Ah... gracias.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Inhamat:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Inhamat:** No importa.
      - [Choice]: No.
        - **Inhamat:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Inhamat:** ¿Tienes [número] [item]? Es bastante urgente. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Inhamat:** ¿Tienes [número] [item]? Es bastante urgente. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Inhamat ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Inhamat:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Inhamat:** ¿Tienes [número] [item]? Es bastante urgente. ([número] restantes)
    - **Player:** ¡Sí! Tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Inhamat ([número]/[número])
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2


##### Primera vez

- **Inhamat:** ¡Sí! Gracias.
- **Inhamat:** Ahora que está hecho, necesitamos el siguiente bloque de suministros.

##### Después

- **Inhamat:** Los siguientes suministros que me faltan son un montón de [item].
- **Player:** ...¿y todavía no han llegado?
- (Condition: Si el objeto deseado son bastones de batalla de fuego:)
  - **Inhamat:** ¡No! Todo lo que necesito es un staff con magia de fuego y los trabajadores del puerto me dicen que pasarán días antes de que los vea.
  - (continue)
- (Condition: Si el artículo deseado son patatas:)
  - **Inhamat:** ¡No! Todo lo que necesito es una cosecha de tubérculos y almidón y los trabajadores del puerto me dicen que pasarán días antes de que los vea.
  - (continue)
- (Condition: Si el artículo deseado es vidrio fundido:)
  - **Inhamat:** ¡No! Lo único que necesito es un vaso caliente y los trabajadores del puerto me dicen que pasarán días antes de que los vea.
  - (continue)
- **Inhamat:** ¿Podrías conseguirme algo para ayudarme por ahora? Acerca de [número] [item] debería funcionar.
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Inhamat:** Ah... gracias.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Inhamat:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Inhamat:**No importa.
      - [Choice]: No.
        - **Inhamat:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Inhamat:** ¿Tienes [número] [item]? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Inhamat:** ¿Tienes [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Inhamat ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Inhamat:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Inhamat:** ¿Tienes [número] [item]? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Inhamat ([número]/[número])
    - **Inhamat:** Excelente. Salvando el día con el [item 1] y ahora algunos [item 2], agradezco su generosidad.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Inhamat:** Dado que eres tan ingenioso, me pregunto si podrías ahorrarme un viaje por la ciudad...
- **Player:** Continúa...
- (Condition: Si el artículo deseado son semillas de malezas enanas:)
  - **Inhamat:** Necesito una forma de cultivar arbustos de malezas enanas para pasar el mes. Aproximadamente las semillas de malezas enanas [número] me ahorrarán muchos problemas.
  - (continue)
- (Condition: Si el artículo deseado son cuernos de cabra:)
  - **Inhamat:** Necesito suministros de pociones para terminar el mes. Aproximadamente [número] los cuernos de cabra me ahorrarán muchos problemas.
  - (continue)
- (Condition: Si el artículo deseado es cuerda:)
  - **Inhamat:** Necesito equipo de escalada para pasar el mes. Aproximadamente [número] longitudes de cuerda me ahorrarán muchas molestias.
  - (continue)
- **Inhamat:** ¿[número] [item] es mucho pedir? ¿Me encontrarás algunos?
- [Menu]: Selecciona una opción
  - [Choice]: Por supuesto.
    - **Inhamat:** Ah... gracias.
  - [Choice]: Es demasiado.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Inhamat:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Inhamat:** No importa.
      - [Choice]: No.
        - **Inhamat:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el artículo deseado son semillas de malezas enanas:)
      - **Inhamat:** ¿Tienes semillas de hierba enana [número]? Las semillas de malezas enanas a menudo las dejan caer los monstruos, o se pueden obtener de los maestros agricultores alrededor de Gielinor. ([número] restante)
    - (Condition: Si el artículo deseado son cuernos de cabra:)
      - **Inhamat:** ¿Tienes cuernos de cabra [número]? Se pueden encontrar cabras alrededor de Nardah o al oeste de Kalphite Hive. ([número] restante)
    - (Condition: Si el artículo deseado es cuerda:)
      - **Inhamat:** ¿Tienes [número] trozos de cuerda? Deberían estar en cualquier general store. ([número] restante)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el artículo deseado son semillas de malezas enanas:)
      - **Inhamat:** ¿Tienes semillas de hierba enana [número]? Las semillas de malezas enanas a menudo las dejan caer los monstruos, o se pueden obtener de los maestros agricultores alrededor de Gielinor. ([número] restante)
      - (continue)
    - (Condition: Si el artículo deseado son cuernos de cabra:)
      - **Inhamat:** ¿Tienes cuernos de cabra [número]? Se pueden encontrar cabras alrededor de Nardah o al oeste de Kalphite Hive. ([número] restante)
      - (continue)
    - (Condition: Si el artículo deseado es cuerda:)
      - **Inhamat:** ¿Tienes [número] trozos de cuerda? Deberían estar en cualquier general store. ([número] restante)
      - (continue)
    - (removes=the requested items)
    - Número de [item] dado a Inhamat ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Inhamat:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el artículo deseado son semillas de malezas enanas:)
      - **Inhamat:** ¿Tienes semillas de hierba enana [número]? Las semillas de malezas enanas a menudo las dejan caer los monstruos, o se pueden obtener de los maestros agricultores alrededor de Gielinor. ([número] restante)
      - (continue)
    - (Condition: Si el artículo deseado son cuernos de cabra:)
      - **Inhamat:** ¿Tienes cuernos de cabra [número]? Se pueden encontrar cabras alrededor de Nardah o al oeste de Kalphite Hive. ([número] restante)
      - (continue)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Inhamat ([número]/[número])
    - **Inhamat:** ¡Muchas gracias por ayudarme!
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

### During the Gielinor Egg Hunt

- (ver|Gielinor Egg Hunt (2024)#Hablando con Inhamat)
