# Amunemen

- **Original Wiki Page**: [Transcript:Amunemen](https://runescape.wiki/w/Transcript%3AAmunemen)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|Missing city quest dialogue.}}
{{transcript NPC|Amunemen}}

### Standard dialogue

- **Amunemen:** Lo que necesitamos es un visionario. La visión da miedo. Podrían iniciar una revolución, refutando el enclave, un rebelde...

### City quest dialogue

- **Amunemen:** Estoy empezando a sentirme como un perro faldero, perro faldero. ¿No crees que podrías ayudarme?
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Amunemen:** Sólo quiero agradecerte.
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
    - **Amunemen:** Está bien. Todo se convertirá en humo...

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

- **Amunemen:** He tenido una idea brillante para un nuevo producto que puedo vender en la ciudad. Es tan brillante que sería una mala decisión compartir con ustedes lo que es... todavía.
- **Amunemen:** ¡Te lo podría decir si me ayudases a conseguir lo que necesitaré para crear mi invento!
- **Amunemen:** ¿Qué opinas? ¿Podrías traerme [número] [item]?
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Amunemen:** Sólo quiero agradecerte.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Amunemen:** Está bien. Todo se convertirá en humo...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Amunemen:** Está bien. Todo se convertirá en humo...
      - [Choice]: No.
        - **Amunemen:** Está bien. Todo se convertirá en humo...

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¿Cómo te llevas consiguiendome [número] [item]? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¿Cómo te llevas consiguiendome [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Amunemen ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Amunemen:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¿Cómo te llevas consiguiendome [número] [item]? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Amunemen ([número]/[número])
    - **Amunemen:** ¡Solo el boleto!
    - **Amunemen:** Ahora que tengo los artículos básicos, ¡necesito agregar algunos componentes más para completar mi producto!
    - **Amunemen:** Déjame ver... Sí, sí, ¡eso es lo que necesitaría!
    - **Player:** ¿Qué es eso?
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Tarea #2

- **Amunemen:** Necesitaría... algo de [item].
- **Player:** ¿Algunos [item]? ¿Pero por qué?
- **Amunemen:** ¿Y revelar mis secretos comerciales? No, Player, ¡no me sacarás ese conocimiento!
- **Amunemen:** No te preocupes. Si me consigues [número] [item], me aseguraré de reembolsarte tu tiempo.
- [Menu]: Selecciona una opción
  - [Choice]: Bien, entonces.
    - **Amunemen:** Sólo quiero agradecerte.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Amunemen:** Está bien. Todo se convertirá en humo...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Amunemen:** Está bien. Todo se convertirá en humo...
      - [Choice]: No.
        - **Amunemen:** Está bien. Todo se convertirá en humo...

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:**¿Cómo va tu búsqueda para encontrarme [número] [item], Player? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:**¿Cómo va tu búsqueda para encontrarme [número] [item], Player? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Amunemen ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Amunemen:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¿Cómo va tu búsqueda para encontrarme [número] [item], Player? ([número] restantes)
    - **Player:** Ahí. Tu [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Amunemen ([número]/[número])
    - **Amunemen:** ¡Mi proyecto está a punto de completarse! ¡Has sido de gran ayuda!
    - **Amunemen:** ¡Mi invento está casi listo!
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Tarea #3

- **Amunemen:** ¡Hay un tipo más de componente que necesito para terminar este increíble invento mío!
- **Player:** Por favor, dímelo...
- **Amunemen:** No es otro que...[número] [item].
- **Amunemen:** ¡Si me haces este último favor, seré rico! ¡Y usted también puede aprovechar los beneficios!
- [Menu]: Selecciona una opción
  - [Choice]: Claro, está bien, lo que sea.
    - **Amunemen:** Sólo quiero agradecerte.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Amunemen:** Está bien. Todo se convertirá en humo...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Amunemen:** Está bien. Todo se convertirá en humo...
      - [Choice]: No.
        - **Amunemen:** Está bien. Todo se convertirá en humo...

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¡Ah, Player! Por favor, dime que has logrado adquirir [número] [item]. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¡Ah, Player! Por favor, dime que has logrado adquirir [número] [item]. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Amunemen ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Amunemen:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¡Ah, Player! Por favor, dime que has logrado adquirir [número] [item]. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Amunemen ([número]/[número])
    - **Amunemen:** ¡Brillante! ¡Tan brillante como mi invento, debo decir! ¡Es hora de armarlo!
    - **Player:** Entonces... ¿Cuál es ese increíble invento que se te ocurrió entonces?
    - **Amunemen:** Ah, el fruto de mi arduo trabajo, la niña de mis ojos, mi nueva creación, lo que revolucionará la vida de los aventureros de todo el mundo... ¡para lo cual todavía tengo que encontrar un buen nombre!
    - **Amunemen:** Espera, realmente no es prudente hablar contigo sobre esto hasta que el prototipo esté funcionando completamente... No puedo arriesgarme a que robes mi idea y la fabriquen en otro lugar por menos dinero.
    - **Player:** Gracias por el voto de confianza.
    - **Amunemen:** ¡Espero no haberte ofendido! Por favor, Player, acepta esta recompensa como muestra de mi agradecimiento.
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

#### Slayer master

- {{transcript missing}}

#### esfuerzo War


##### Tarea #1

- **Amunemen:** Me han encomendado la tarea de conseguir suministros para el esfuerzo bélico.
- **Player:** ¿Quiénes somos? ¿Con quién estás en guerra TÚ?
- **Amunemen:** Todo será revelado. Primero necesito [número] [items]. ¿Puedo confiar en ti?
- [Menu]: Selecciona una opción
  - [Choice]: Afirmativo.
    - **Amunemen:** Sólo quiero agradecerte.
  - [Choice]: Negativo.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Amunemen:** Está bien. Todo se convertirá en humo.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Amunemen:** Está bien. Todo se convertirá en humo.
      - [Choice]: No.
        - **Amunemen:** Está bien. Todo se convertirá en humo.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Amunemen ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Amunemen:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Amunemen ([número]/[número])
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Tarea #2


##### Primera vez

- **Amunemen:** ¡Buen trabajo, soldado!
- **Amunemen:** Ahora que está hecho, necesitamos el siguiente bloque de suministros.

##### Después

- **Amunemen:** Los siguientes suministros que necesito son una carga de [item].
- **Player:** Correcto. ¿Por qué [item]?
- **Amunemen:** ¿Alguna vez has intentado pelear una guerra sin [item]? No lo creo.
- **Amunemen:** El esfuerzo de guerra requiere [número] [item]. ¿Asumo que puedo confiar en usted para obtener el [item]?
- [Menu]: Selecciona una opción
  - [Choice]: Seguro que puedes.
    - **Amunemen:** Sólo quiero agradecerte.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Amunemen:** Está bien. Todo se convertirá en humo.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Amunemen:** Está bien. Todo se convertirá en humo.
      - [Choice]: No.
        - **Amunemen:** Está bien. Todo se convertirá en humo.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Amunemen ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Amunemen:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Amunemen:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Amunemen ([número]/[número])
    - **Amunemen:** ¡Genial! ¡Ahora estamos listos para llevar la ofensiva a casa!
    - **Player:** ¿Puedo preguntar por qué hablas así?
    - **Amunemen:** ¿Qué quieres decir, soldado?
    - **Player:** Estás hablando como un general imperial. Es un poco desagradable.
    - **Amunemen:** ...
    - **Amunemen:** Los guardias siempre están mirando. Tengo que guardar las apariencias.
    - **Player:** Cierto... bastante justo. ¿Qué más... nosotros... necesitamos para el esfuerzo bélico?
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: arriba)

##### Tarea #3

- **Amunemen:** ¡Ahora es el momento que estabas esperando, soldado! ¡La matanza!
- **Amunemen:** ¡Finalmente venceremos a nuestro temido enemigo, el [monster]!
- **Player:** ¿Qué?
- **Amunemen:** ¡Sí, mata a [número] [monster] en nombre del propio Faraón!
- [Menu]: Selecciona una opción
  - [Choice]: Está bien.
    - **Amunemen:** Sólo quiero agradecerte.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Amunemen:** Está bien. Todo se convertirá en humo.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Amunemen:** Está bien. Todo se convertirá en humo.
      - [Choice]: No.
        - **Amunemen:** Está bien. Todo se convertirá en humo.

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: If the monster is kalphites:)
      - **Amunemen:** ¿Has matado a los calfitos de [número]? Se encuentran dentro de colmenas calfitas bajo las arenas del desierto. ¡Podríamos ganar esta guerra todavía! ([número] restante)
    - (Condition: If the monster is plague frogs:)
      - **Amunemen:** ¿Has matado las ranas plaga [número]? Por lo general, están adelgazando alrededor de Sophanem. ¡Podríamos ganar esta guerra todavía! ([número] restante)
    - (Condition: If the monster is crocodiles:)
      - **Amunemen:** ¿Has matado cocodrilos [número]? Los cocodrilos se encuentran deambulando alrededor del río hacia el norte. ¡Podríamos ganar esta guerra todavía! ([número] restante)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: If the monster is kalphites:)
      - **Amunemen:** ¿Has matado a los calfitos de [número]? Se encuentran dentro de colmenas calfitas bajo las arenas del desierto. ¡Podríamos ganar esta guerra todavía! ([número] restante)
      - (continue)
    - (Condition: If the monster is plague frogs:)
      - **Amunemen:** ¿Has matado las ranas plaga [número]? Por lo general, están adelgazando alrededor de Sophanem. ¡Podríamos ganar esta guerra todavía! (0 restante)
      - (continue)
    - (Condition: If the monster is crocodiles:)
      - **Amunemen:** ¿Has matado cocodrilos [número]? Los cocodrilos se encuentran deambulando alrededor del río hacia el norte. ¡Podríamos ganar esta guerra todavía! ([número] restante)
      - (continue)
    - **Player:** Sí, he matado al [monster].
    - (receives=Slayer experience)
    - **Amunemen:** ¿Has bailado, como dicen, en la sangre de tus enemigos? ¿Has enviado las almas de [número] [monster] al Inframundo?
    - **Amunemen:** No es que esos [monster] tengan alma, creo que realmente no pueden recibir ayuda.
    - **Amunemen:** ¡Muchas gracias por ayudarme!
    - **Player:** Me temo que todavía necesitas mucha más ayuda.
    - **Amunemen:** Lo siento, ¿qué?
    - **Player:** Nada. Fue un placer.
    - (receives=a Menaphite gift offering and 2,000 reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.
