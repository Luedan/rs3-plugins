# Pia

- **Original Wiki Page**: [Transcript:Pia](https://runescape.wiki/w/Transcript%3APia)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|city quest}}

### Standard dialogue

- **Pia:** Los del distrito obrero son buenas personas, pero tienen mala suerte en sus circunstancias.

### City Quest

- **Pia:** Saludos viajero. ¿Tienes un momento libre? Necesito ayuda.
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Pia:** ¡Muchas gracias!
    - (Condition: If the city quest type is "Attacked by wildlife":)
      - (continue)
    - (Condition: If the city quest type is "Awaiting delivery":)
      - (continue)
    - (Condition: If the city quest type is "Children can't sleep":)
      - (continue)
    - (Condition: If the city quest type is "Collector of curiosities":)
      - (continue)
    - (Condition: If the city quest type is "Crondis is angry":)
      - (continue)
    - (Condition: If the city quest type is "Crop pests":)
      - (continue)
    - (Condition: If the city quest type is "Delivery help":)
      - (continue)
    - (Condition: If the city quest type is "Friend's son slowly dying":)
      - (continue)
    - (Condition: If the city quest type is "New product":)
      - (continue)
    - (Condition: If the city quest type is "Slayer master":)
      - (continue)
    - (Condition: If the city quest type is "War effort":)
      - (continue)
  - [Choice]: No ahora mismo.
    - {{transcript missing}}

#### Atacado por vida silvestre

- {{transcript missing}}

#### Esperando entrega

- {{transcript missing}}

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


##### Tarea #1

- **Pia:** He tenido una idea brillante para un nuevo producto que puedo vender en la ciudad. Es tan brillante que sería una mala decisión compartir con ustedes lo que es... todavía.
- **Pia:** ¡Te lo podría decir si me ayudases a conseguir lo que necesitaré para crear mi invento!
- **Pia:** ¿Qué opinas? ¿Podrías traerme [número] [item]?
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Pia:** ¡Muchas gracias!
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - {{transcript missing}}
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - {{transcript missing}}
      - [Choice]: No.
        - {{transcript missing}}

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Pia:** ¿Cómo te llevas consiguiendome [número] [item]? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Pia:** ¿Cómo te llevas consiguiendome [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Pia ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Pia:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Pia:** ¿Cómo te llevas consiguiendome [número] [item]? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Pia ([número]/[número])
    - **Pia:** ¡Solo el boleto!
    - **Pia:** Ahora que tengo los artículos básicos, ¡necesito agregar algunos componentes más para completar mi producto!
    - **Pia:** Déjame ver... Sí, sí, ¡eso es lo que necesitaría!
    - **Player:** ¿Qué es eso?
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2

- **Pia:** Necesitaría... algo de [item].
- **Player:** ¿Algunos [item]? ¿Pero por qué?
- **Pia:** ¿Y revelar mis secretos comerciales? No, Player, ¡no me sacarás ese conocimiento!
- **Pia:** No te preocupes. Si me consigues [número] [item], me aseguraré de reembolsarte tu tiempo.
- [Menu]: Selecciona una opción
  - [Choice]: Bien, entonces.
    - **Pia:** ¡Muchas gracias!
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - {{transcript missing}}
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - {{transcript missing}}
      - [Choice]: No.
        - {{transcript missing}}

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Pia:**¿Cómo va tu búsqueda para encontrarme [número] [item], Player? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Pia:**¿Cómo va tu búsqueda para encontrarme [número] [item], Player? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Pia ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Pia:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Pia:** ¿Cómo va tu búsqueda para encontrarme [número] [item], Player? ([número] restantes)
    - **Player:** Ahí. Tu [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Pia ([número]/[número])
    - **Pia:** ¡Mi proyecto está a punto de completarse! ¡Has sido de gran ayuda!
    - **Pia:** ¡Mi invento está casi listo!
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Pia:** ¡Hay un tipo más de componente que necesito para terminar este increíble invento mío!
- **Player:** Por favor, dímelo...
- **Pia:** No es otro que...[número] [item].
- **Pia:** ¡Si me haces este último favor, seré rico! ¡Y usted también puede aprovechar los beneficios!
- [Menu]: Selecciona una opción
  - [Choice]: Claro, está bien, lo que sea.
    - **Pia:** ¡Muchas gracias!
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - {{transcript missing}}
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - {{transcript missing}}
      - [Choice]: No.
        - {{transcript missing}}

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Pia:** ¡Ah, Player! Por favor, dime que has logrado adquirir [número] [item]. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Pia:** ¡Ah, Player! Por favor, dime que has logrado adquirir [número] [item]. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Pia ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Pia:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Pia:** ¡Ah, Player! Por favor, dime que has logrado adquirir [número] [item]. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Pia ([número]/[número])
    - **Pia:** ¡Brillante! ¡Tan brillante como mi invento, debo decir! ¡Es hora de armarlo!
    - **Player:** Entonces... ¿Cuál es ese increíble invento que se te ocurrió entonces?
    - **Pia:** Ah, el fruto de mi arduo trabajo, la niña de mis ojos, mi nueva creación, lo que revolucionará la vida de los aventureros de todo el mundo... ¡para lo cual todavía tengo que encontrar un buen nombre!
    - **Pia:** Espera, realmente no es prudente hablar contigo sobre esto hasta que el prototipo esté funcionando completamente... No puedo arriesgarme a que robes mi idea y la fabriquen en otro lugar por menos dinero.
    - **Player:** Gracias por el voto de confianza.
    - **Pia:** ¡Espero no haberte ofendido! Por favor, Player, acepta esta recompensa como muestra de mi agradecimiento.
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

#### Slayer master

- {{transcript missing}}

#### esfuerzo War

- {{transcript missing}}
