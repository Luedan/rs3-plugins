# Lisah

- **Original Wiki Page**: [Transcript:Lisah](https://runescape.wiki/w/Transcript%3ALisah)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|needs city quest dialogue}}

### Standard dialogue

- **Lisah:** ¡Parece que probablemente podrías oler un poco mejor!

### Overhead dialogue

- **Lisah:** {{RSChat|Fine perfumes for sale!}}

### City quest dialogue

- **Lisah:** La gente tiende a ignorarme porque quizás me esfuerzo demasiado en venderles mis fragancias. ¿Quizás podrías ayudarme?
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Lisah:** Te lo agradezco.
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
    - **Lisah:** Hueles.

#### Atacado por vida silvestre

- {{transcript missing}}

#### Esperando entrega

- {{transcript missing}}

#### Los niños no pueden dormir

- {{transcript missing}}

#### Coleccionista de curiosidades


##### Tarea #1

- **Lisah:** Soy un coleccionista de curiosidades y actualmente tengo la mayor colección de [item] de todo Menaphos.
- **Lisah:** Bueno, lo hice...
- **Player:** ¿Qué pasó?
- **Lisah:** Otro coleccionista ha llegado a la ciudad y su colección eclipsa la mía.
- **Player:** ¿Cuántos [item] más tienen?
- **Lisah:** He oído que tienen [número] más [item] que yo.
- **Player:** Entonces, si alguien te trajera [número] [item], ¿volverías a tener la mejor colección?
- **Lisah:** ¡Sí! ¿Harías esto por mí?
- [Menu]: Selecciona una opción
  - [Choice]: Bien, entonces.
    - **Lisah:** Te lo agradezco.
    - **Player:** ¿Dónde puedo encontrar [item]?
    - (Condition: Si el artículo deseado son huesos de dragón:)
      - **Lisah:** Mata algunos dragones y recupera sus huesos.
    - (Condition: Si el artículo deseado es vidrio fundido:)
      - **Lisah:** El vidrio fundido se puede fabricar usando un balde de arena y un poco de carbonato de sodio.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Lisah:** Hueles.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Lisah:** Hueles.
      - [Choice]: No.
        - **Lisah:** Hueles.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Lisah:** ¿Tienes el [número] [item]? ([número] restantes)
    - **Player:** Todavía no. ¿Dónde podría encontrar [item] nuevamente?
    - (arriba)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Lisah:** ¿Tienes el [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Lisah ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Lisah:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Lisah:** ¿Tienes el [número] [item]? ([número] restantes)
    - **Player:** ¡Sí, tengo el [item]!
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Lisah ([número]/[número])
    - **Lisah:** Bueno, supongo que esto es un comienzo...
    - **Player:** ¿Un comienzo?
    - **Lisah:** Acabo de enterarme de que mi rival acaba de traer un nuevo envío de [item]...
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2

- **Lisah:** Escuchó que me trajiste algo de [item 1], ahora tiene [número] más [item 2] que yo, solo para fastidiarme.
- **Player:** ¿Qué significa eso para ti?
- **Lisah:** ¡Esto es una carrera armamentista! Necesitas conseguirme [número] más [item 2].
- **Player:** ¿Coleccionas [item 1] Y [item 2]?
- **Lisah:** ¡Colecciono muchas cosas! ¡Colecciono colecciones!
- **Player:** ...
- **Lisah:** Entonces, sobre esos [número] más [item 2]...
- [Menu]: Selecciona una opción
  - [Choice]: Bien, está bien.
    - **Lisah:** Te lo agradezco.
    - (Condition: Si el artículo deseado es mineral de cobre:)
      - **Lisah:** El mineral de cobre se puede encontrar al sureste de Varrock.
    - (Condition: Si el artículo deseado son huesos de murciélago:)
      - **Lisah:** Mata algunos murciélagos y recupera sus huesos.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Lisah:** Hueles.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Lisah:** Hueles.
      - [Choice]: No.
        - **Lisah:** Hueles.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Lisah:** ¿Ya tienes [número] [item]? ([número] restantes)
    - **Player:** No, ¿dónde puedo encontrar el [item] nuevamente?
    - (arriba)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Lisah:** ¿Ya tienes [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Lisah ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Lisah:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Lisah:** ¿Ya tienes [número] [item]? ([número] restantes)
    - **Player:** Tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Lisah ([número]/[número])
    - **Lisah:** Muchas gracias.
    - **Player:** No hay problema.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Lisah:** ¿Quizás podrías hacerme un pequeño trabajo más?
- **Player:** ¿Se trata de [item 1] o [item 2]?
- **Lisah:** ¡No, por supuesto que no!
- **Player:** ¿En serio?
- **Lisah:** ...
- **Lisah:** Sí, lo prometo, ¡necesito [número] más [item] para mi colección final!
- **Lisah:** Esta es la última vez que pregunto. Prometo.
- **Lisah:** [number] [item]?
- [Menu]: Selecciona una opción
  - [Choice]: [number] [item]...
    - **Lisah:** Eres una buena persona.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Lisah:** Hueles.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Lisah:** Hueles.
      - [Choice]: No.
        - **Lisah:** Hueles.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Lisah:** ¿Tienes el [item]? Necesito [número]. ([número] restantes)
    - **Player:** Todavía no. ¿Podrías indicarme la dirección de algún [item]?
    - (Condition: Si el artículo deseado son rollos de tela:)
      - **Lisah:** Podrías hacerlos en un telar.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Lisah:** ¿Tienes el [item]? Necesito [número]. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Lisah ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Lisah:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Lisah:** ¿Tienes el [item 3]? Necesito [número]. ([número] restantes)
    - **Player:** Sí, pero no les daré más [item 3], [item 1] O [item 2] después de esto.
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Lisah ([número]/[número])
    - **Lisah:** ¡Finalmente, una vez más tengo la mayor colección de [item 3] en Menaphos!
    - **Player:** ¿Qué planeas hacer con [item 1], [item 2] y [item 3] ahora que los tienes?
    - **Lisah:** Realmente no lo sé.
    - **Player:** Bueno, entonces...
    - **Player:** Buena suerte con eso.
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

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
