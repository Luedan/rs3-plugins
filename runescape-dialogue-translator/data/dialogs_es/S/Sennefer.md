# Sennefer

- **Original Wiki Page**: [Transcript:Sennefer](https://runescape.wiki/w/Transcript%3ASennefer)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|city quest}}

### Standard dialogue

- **Sennefer:** No atiendo a forasteros. Lo siento.

### Overhead dialogue

- **Sennefer:** {{RSChat|I have wares at a reasonable price.}}

### City Quest

- **Sennefer:** ¿Qué te trae por aquí, aventurero? ¿Me ayudarás?
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Sennefer:** Lo has hecho bien.
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
    - No importa.

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


##### Tarea #1

- **Sennefer:** ¡Esos molestos [monster] se están comiendo mis cultivos!
- **Player:** Bueno, eso es un problema. ¿Puedo hacer algo para ayudar?
- **Sennefer:** Sí, tengo un plan.
- **Sennefer:** Creo que si cubrimos los cultivos con algún tipo de mezcla desagradable, los disuadiremos.
- **Player:** Sí, eso parece razonable.
- **Sennefer:** Primero que nada necesito [número] de [item]. ¿Podrías conseguirlos para mí?
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Sennefer:** Lo has hecho bien.
    - **Player:** ¿Dónde puedo encontrar [item]?
    - (Condition: If the item assigned is a seed:)
      - {{anchor|first}} **Sennefer:** Las semillas de [Herb] a menudo las dejan los monstruos, o se pueden obtener de maestros agricultores en Gielinor. Pero date prisa antes de que se acaben todas mis cosechas.
  - [Choice]: No.
    - {{transcript missing}}

##### Hablar con ella de nuevo sin el primer elemento

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Tienes el [número] de [item]? ([número] restantes)
    - **Player:** Todavía no. ¿Dónde podría encontrar [item] nuevamente?
    - (continuea|first)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Hablando con ella de nuevo con algo del primer elemento.

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Tienes el [número] de [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Sennefer ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Sennefer:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Hablando con ella de nuevo con todo el primer elemento.

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Tienes el [número] de [item]? ([número] restantes)
    - **Player:** ¡Sí, tengo el [item]!
    - (removes=the requested items) (receives= experience)
    - **Sennefer:** ¡Excelente, el [item] será una excelente base para el brebaje!
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2

- **Sennefer:** Ahora, pensemos en lo que necesitaremos a continuación.
- **Sennefer:** Lo que necesitamos es combustible para el horno.
- **Player:** ¿Qué tal [item]?
- **Sennefer:** ¡Perfecto! Creo que si me consigues [número] de [item] estaremos listos.
- [Menu]: Selecciona una opción
  - [Choice]: Muy bien.
    - **Sennefer:** Lo has hecho bien.
    - **Player:** ¿Sabes dónde puedo conseguir [item]?
    - (Condition: If the item requested is coal:)
      - {{anchor|second}} **Sennefer:** Puedes extraer carbón al norte de Al Kharid.
  - [Choice]: No, lo siento.
    - {{transcript missing}}

##### Hablando con ella de nuevo sin el segundo elemento

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Ya has encontrado [número] de [item]? ([número] restantes)
    - **Player:** No, ¿dónde debería buscar el [item]?
    - (continuea|second)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Hablando con ella de nuevo con algo del segundo elemento.

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Ya has encontrado [número] de [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Sennefer ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Sennefer:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Hablando con ella de nuevo con todo el segundo elemento.

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Ya has encontrado [número] de [item]? ([número] restantes)
    - **Player:** Tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Sennefer ([número]/[número])
    - **Sennefer:** Bueno, ahora podemos terminar nuestro elemento disuasorio.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Player:** ¿Pasa algo?
- **Sennefer:** Mientras no estabas, ¡el [monster] regresó y se comió aún más de mis cultivos!
- **Sennefer:** ¡Este elemento disuasorio no será suficiente! ¡Necesito que envíes un mensaje de que nadie se mete con mis cultivos!
- **Player:** Uh... Bueno, no hemos probado el detector.
- **Sennefer:** ¡Olvídate del elemento disuasorio! ¡Necesito que mates a [número] de [monster] por mí!
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Player:** ¿Qué sabes sobre [monster]?
    - (Condition: If the monster is desert lizards:)
      - {{anchor|third}} **Sennefer:** ¿Aparte del hecho de que son demonios ladrones de cosechas? Se pueden encontrar al este en el desierto.
  - [Choice]: No.
    - {{transcript missing}}

##### Hablando con ella de nuevo con la tarea de cazadora incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Trataste con el [número] de [monster]? ([número] restantes)
    - **Player:** Todavía no. ¿Podrías indicarme la dirección de algún [monster]?
    - (continuea|third)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Hablando con ella de nuevo con la tarea de cazador completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Trataste con el [número] de [monster]? (0 restante)
    - **Player:** Sí, sus cultivos deberían estar seguros ahora.
    - (receives= Slayer experience)
    - **Sennefer:** ¡Por fin mis cultivos están a salvo!
    - **Sennefer:** Entonces…
    - **Sennefer:** Supongo que no querrás comprar [first item] y [second item].
    - **Player:**No, gracias.
    - (receives=Menaphite gift offering)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

#### Ayuda de entrega

- {{transcript missing}}

#### El hijo de un amigo está muriendo lentamente.

- {{transcript missing}}

#### Nuevo producto


##### Tarea #1

- **Sennefer:** He tenido una idea brillante para un nuevo producto que puedo vender en la ciudad. Es tan brillante que sería una mala decisión compartir con ustedes lo que es... todavía.
- **Sennefer:** ¡Te lo podría decir si me ayudases a conseguir lo que necesitaré para crear mi invento!
- **Sennefer:** ¿Qué opinas? ¿Podrías traerme [número] [item]?
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Sennefer:** Lo has hecho bien.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Sennefer:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Sennefer:** No importa.
      - [Choice]: No.
        - **Sennefer:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Cómo te llevas consiguiendome [número] [item]? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Cómo te llevas consiguiendome [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Sennefer ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Sennefer:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Cómo te llevas consiguiendome [número] [item]? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Sennefer ([número]/[número])
    - **Sennefer:** ¡Solo el boleto!
    - **Sennefer:** Ahora que tengo los artículos básicos, ¡necesito agregar algunos componentes más para completar mi producto!
    - **Sennefer:** Déjame ver... Sí, sí, ¡eso es lo que necesitaría!
    - **Player:** ¿Qué es eso?
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2

- **Sennefer:** Necesitaría... algo de [item].
- **Player:** ¿Algunos [item]? ¿Pero por qué?
- **Sennefer:** ¿Y revelar mis secretos comerciales? No, Player, ¡no me sacarás ese conocimiento!
- **Sennefer:** No te preocupes. Si me consigues [número] [item], me aseguraré de reembolsarte tu tiempo.
- [Menu]: Selecciona una opción
  - [Choice]: Bien, entonces.
    - **Sennefer:** Lo has hecho bien.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Sennefer:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Sennefer:** No importa.
      - [Choice]: No.
        - **Sennefer:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:**¿Cómo va tu búsqueda para encontrarme [número] [item], Player? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:**¿Cómo va tu búsqueda para encontrarme [número] [item], Player? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Sennefer ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Sennefer:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¿Cómo va tu búsqueda para encontrarme [número] [item], Player? ([número] restantes)
    - **Player:** Ahí. Tu [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Sennefer ([número]/[número])
    - **Sennefer:** ¡Mi proyecto está a punto de completarse! ¡Has sido de gran ayuda!
    - **Sennefer:** ¡Mi invento está casi listo!
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Sennefer:** ¡Hay un tipo más de componente que necesito para terminar este increíble invento mío!
- **Player:** Por favor, dímelo...
- **Sennefer:** No es otro que...[número] [item].
- **Sennefer:** ¡Si me haces este último favor, seré rico! ¡Y usted también puede aprovechar los beneficios!
- [Menu]: Selecciona una opción
  - [Choice]: Claro, está bien, lo que sea.
    - **Sennefer:** Lo has hecho bien.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Sennefer:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Sennefer:** No importa.
      - [Choice]: No.
        - **Sennefer:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¡Ah, Player! Por favor, dime que has logrado adquirir [número] [item]. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¡Ah, Player! Por favor, dime que has logrado adquirir [número] [item]. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Sennefer ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Sennefer:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Sennefer:** ¡Ah, Player! Por favor, dime que has logrado adquirir [número] [item]. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Sennefer ([número]/[número])
    - **Sennefer:** ¡Brillante! ¡Tan brillante como mi invento, debo decir! ¡Es hora de armarlo!
    - **Player:** Entonces... ¿Cuál es ese increíble invento que se te ocurrió entonces?
    - **Sennefer:** Ah, el fruto de mi arduo trabajo, la niña de mis ojos, mi nueva creación, lo que revolucionará la vida de los aventureros de todo el mundo... ¡para lo cual todavía tengo que encontrar un buen nombre!
    - **Sennefer:** Espera, realmente no es prudente hablar contigo sobre esto hasta que el prototipo esté funcionando completamente... No puedo arriesgarme a que robes mi idea y la fabriquen en otro lugar por menos dinero.
    - **Player:** Gracias por el voto de confianza.
    - **Sennefer:** ¡Espero no haberte ofendido! Por favor, Player, acepta esta recompensa como muestra de mi agradecimiento.
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

#### Slayer master

- {{transcript missing}}

#### esfuerzo War

- {{transcript missing}}
