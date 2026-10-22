# Olivia (Menaphos)

- **Original Wiki Page**: [Transcript:Olivia (Menaphos)](https://runescape.wiki/w/Transcript%3AOlivia%20%28Menaphos%29)
- **Letter**: `O`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

*Al hablar con Olivia en los muelles del Distrito Portuario en Menaphos.*
- **Olivia:** He estado echando un vistazo a la vida salvaje local, pero los guardias no me dejan volver a entrar.

### City quest dialogue

- **Olivia:** Me alegro de encontrarte aquí. ¿Estás ocupado? Necesito un poco de ayuda.
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Olivia:** ¡Salud, amor!
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
    - **Olivia:** Oh, bueno, tal vez aparezca alguien más.

#### Atacado por vida silvestre

- {{transcript missing}}

#### Esperando entrega

- {{transcript missing}}

#### Los niños no pueden dormir

- {{transcript missing}}

#### Coleccionista de curiosidades

- {{transcript missing}}

#### Crondis está enojado


##### Tarea #1

- **Olivia:** El magnífico Crondis se ha enfadado con [monster]. Requiere un sacrificio de sangre y un tributo.
- **Olivia:** Primero, ve y mata a [número] [monster].
- **Player:** ¿Qué han hecho los [monster] para enojar al todopoderoso Crondis?
- **Olivia:** No necesitas saberlo. ¿Irás a matarlos?
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Olivia:** ¡Salud, amor!
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
      - [Choice]: No.
        - **Olivia:** Oh, bueno, tal vez aparezca alguien más.

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Has vencido al [número] [monster] para Lady Crondis? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Has vencido al [número] [monster] para Lady Crondis? ([número] restantes)
    - **Player:** Sí, he masacrado al [monster].
    - (receives=Slayer experience)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea #2


##### Primera vez

- **Olivia:** ¡Alabado sea Crondis!
- **Olivia:** Ahora que los miserables han pagado por sus transgresiones, requerimos un holocausto.

##### Después

- **Olivia:** Lo siguiente que necesito es [item].
- **Player:** Correcto. ¿Por qué [item]?
- **Olivia:** El primer paso para apaciguar a Crondis es tradicionalmente una ofrenda quemada de [item].
- **Olivia:** Así que ve y consigue [número] [item].
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Olivia:** ¡Salud, amor!
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
      - [Choice]: No.
        - **Olivia:** Oh, bueno, tal vez aparezca alguien más.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Tienes el tributo a Crondis? Ella se impacienta. Necesito [número] [item]. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Tienes el tributo a Crondis? Ella se impacienta. Necesito [número] [item]. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Olivia ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Olivia:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Tienes el tributo a Crondis? Ella se impacienta. Necesito [número] [item]. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Olivia ([número]/[número])
    - **Olivia:** ¡Que el gran cocodrilo te sonría!
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Olivia:** Finalmente, según la tradición, Crondis requiere que se vierta una ofrenda líquida en el Elid.
- **Player:** ¿Una oferta líquida?
- **Olivia:** Sí, reúne [número] [item] para mí y haré que los trabajadores los liquiden.
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Olivia:** ¡Salud, amor!
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
      - [Choice]: No.
        - **Olivia:** Oh, bueno, tal vez aparezca alguien más.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Has reunido el [número] [item]? ¡Necesitamos apaciguar a Crondis lo antes posible! ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Has reunido el [número] [item]? ¡Necesitamos apaciguar a Crondis lo antes posible! ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Olivia ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Olivia:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Has reunido el [número] [item]? ¡Necesitamos apaciguar a Crondis lo antes posible! ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Olivia ([número]/[número])
    - **Olivia:** ¿No eres trabajador? Buen trabajo.
    - **Olivia:** ¡Muchas gracias por ayudarme!
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

#### Plagas de cultivos

- {{transcript missing}}

#### Ayuda de entrega

- {{transcript missing}}

#### El hijo de un amigo está muriendo lentamente.

- {{transcript missing}}

#### Nuevo producto

- {{transcript missing}}

#### Slayer master


##### Tarea #1

- **Olivia:** Estoy listo para un cambio de carrera.
- **Player:** Oh, ¿en serio? ¿Cómo puedo ayudar?
- **Olivia:** Bueno, realmente quiero ser un Slayer master, aunque me vendría bien un poco de práctica.
- **Player:** Muy bien, haz tu mejor esfuerzo.
- **Olivia:** ¡Saludos, aventurero! ¡Soy yo, el Slayer master!
- **Olivia:** ¿Cómo estuvo eso?
- **Player:** Sí, eso estuvo genial, pero tienes que decirme qué quieres que mate.
- **Olivia:** ¡Ah, claro!
- **Olivia:** ¡Aventurero! Necesito que mates... uh...
- **Olivia:** Necesito que mates...[número]...[monster]?
- [Menu]: Selecciona una opción
  - [Choice]: Puedo hacer eso.
    - **Olivia:** ¡Salud, amor!
    - **Player:** ¿Dónde puedo encontrar [monster]?
    - (Condition: If the monster assigned is Bandits:)
      - {{anchor|first}} **Olivia:** Creo que hay un gran campamento de bandidos al norte de aquí, más allá de la cantera.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - {{transcript missing}}
      - [Choice]: No.
        - **Olivia:** Oh, bueno, tal vez aparezca alguien más.

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Mataste al [número] [monster]? ([número] restantes)
    - **Player:** Todavía no. ¿Dónde podría encontrar [monster] nuevamente?
    - (continuea|first)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Mataste al [número] [monster]? (0 restante)
    - **Player:** ¡Sí, los [monster] han sido asesinados!
    - **Olivia:** ¡Buen trabajo, aventurero!
    - **Olivia:** Entonces, ¿qué hago ahora?
    - **Player:** Dime qué necesito acabar a continuación.
    - **Olivia:** ¿Otra vez? ¡Bueno!
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2

- **Olivia:** ¡Aventurero! ¡Necesito que mates más cosas por mí!
- **Player:** ¿Qué debo matar por ti, Slayer master?
- **Olivia:** He decidido que debes matar a [número] [monster].
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Olivia:** ¡Salud, amor!
    - **Player:** ¿Dónde puedo encontrar [monster]?
    - (Condition: If the monster assigned is kalphites:)
      - {{anchor|first}} **Olivia:** Se encuentran dentro de colmenas calfitas bajo las arenas del desierto. Al menos ahí me dijeron...
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - {{transcript missing}}
      - [Choice]: No.
        - **Olivia:** Oh, bueno, tal vez aparezca alguien más.

#### esfuerzo War


##### Tarea #1

- **Olivia:** Me han encomendado la tarea de conseguir suministros para el esfuerzo bélico.
- **Player:** ¿Quiénes somos? ¿Con quién estás en guerra TÚ?
- **Olivia:** Todo será revelado. Primero necesito [número] [items]. ¿Puedo confiar en ti?
- [Menu]: Selecciona una opción
  - [Choice]: Afirmativo.
    - **Olivia:** ¡Salud, amor!
  - [Choice]: Negativo.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
      - [Choice]: No.
        - **Olivia:** Oh, bueno, tal vez aparezca alguien más.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Olivia ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Olivia:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Olivia ([número]/[número])
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2


##### Primera vez

- **Olivia:** ¡Buen trabajo, soldado!
- **Olivia:** Ahora que está hecho, necesitamos el siguiente bloque de suministros.

##### Después

- **Olivia:** Los siguientes suministros que necesito son una carga de [item].
- **Player:** Correcto. ¿Por qué [item]?
- **Olivia:** ¿Alguna vez has intentado pelear una guerra sin [item]? No lo creo.
- **Olivia:** El esfuerzo de guerra requiere [número] [item]. ¿Asumo que puedo confiar en usted para obtener el [item]?
- [Menu]: Selecciona una opción
  - [Choice]: Seguro que puedes.
    - **Olivia:** ¡Salud, amor!
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
      - [Choice]: No.
        - **Olivia:** Oh, bueno, tal vez aparezca alguien más.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Olivia ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Olivia:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Olivia:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Olivia ([número]/[número])
    - **Olivia:** ¡Genial! ¡Ahora estamos listos para llevar la ofensiva a casa!
    - **Player:** ¿Puedo preguntar por qué hablas así?
    - **Olivia:** ¿Qué quieres decir, soldado?
    - **Player:** Estás hablando como un general imperial. Es un poco desagradable.
    - **Olivia:** ...
    - **Olivia:** Los guardias siempre están mirando. Tengo que guardar las apariencias.
    - **Player:** Cierto... bastante justo. ¿Qué más... nosotros... necesitamos para el esfuerzo bélico?
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Olivia:** ¡Ahora es el momento que estabas esperando, soldado! ¡La matanza!
- **Olivia:** ¡Finalmente venceremos a nuestro temido enemigo, el [monster]!
- **Player:** ¿Qué?
- **Olivia:** ¡Sí, mata a [número] [monster] en nombre del propio Faraón!
- [Menu]: Selecciona una opción
  - [Choice]: Está bien.
    - **Olivia:** ¡Salud, amor!
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Olivia:** Oh, bueno, tal vez aparezca alguien más.
      - [Choice]: No.
        - **Olivia:** Oh, bueno, tal vez aparezca alguien más.

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: If the monster is kalphites:)
      - **Olivia:** ¿Has matado a los calfitos de [número]? Se encuentran dentro de colmenas calfitas bajo las arenas del desierto. ¡Podríamos ganar esta guerra todavía! ([número] restante)
    - (Condition: If the monster is plague frogs:)
      - **Olivia:** ¿Has matado las ranas plaga [número]? Por lo general, están adelgazando alrededor de Sophanem. ¡Podríamos ganar esta guerra todavía! ([número] restante)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: If the monster is kalphites:)
      - **Olivia:** ¿Has matado a los calfitos de [número]? Se encuentran dentro de colmenas calfitas bajo las arenas del desierto. ¡Podríamos ganar esta guerra todavía! ([número] restante)
      - (continue)
    - (Condition: If the monster is plague frogs:)
      - **Olivia:** ¿Has matado las ranas plaga [número]? Por lo general, están adelgazando alrededor de Sophanem. ¡Podríamos ganar esta guerra todavía! (0 restante)
      - (continue)
    - **Player:** Sí, he matado al [monster].
    - (receives=Slayer experience)
    - **Olivia:** ¿Has bailado, como dicen, en la sangre de tus enemigos? ¿Has enviado las almas de [número] [monster] al Inframundo?
    - **Olivia:** No es que esos [monster] tengan alma, creo que realmente no pueden recibir ayuda.
    - **Olivia:** ¡Muchas gracias por ayudarme!
    - **Player:** Me temo que todavía necesitas mucha más ayuda.
    - **Olivia:** Lo siento, ¿qué?
    - **Player:** Nada. Fue un placer.
    - (receives=a Menaphite gift offering and 2,000 reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

### Overhead dialogue

*Olivia ocasionalmente producirá diálogos generales.*
- **Olivia:** {{RSChat|Blimey.|colour=yellow|shadow=yes}}
