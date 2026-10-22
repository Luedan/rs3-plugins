# Khattak

- **Original Wiki Page**: [Transcript:Khattak](https://runescape.wiki/w/Transcript%3AKhattak)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|Missing city quest dialogue.}}

### Standard dialogue

- **Khattak:** El carro conducido por un auriga loco lo sabe, le encanta mantener alerta a las ratas codiciosas. Mientras corre por un camino de aflicciones, aplasta por igual; amigos y enemigos.

### Overhead dialogue

*Khattak ocasionalmente producirá diálogos generales.*
- {{RSChat|Roses are red.|colour=yellow|shadow=yes}}
- {{RSChat|Violets are blue.|colour=yellow|shadow=yes}}
- {{RSChat|No matter where,|colour=yellow|shadow=yes}}
- {{RSChat|They're watching you.|colour=yellow|shadow=yes}}

### City quest dialogue

- **Khattak:** Saludos. Soy conocido por Khattak. Necesito un alma bondadosa que libere una válvula que está acumulando presión en mi mente. ¿Podrías ayudar?
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Khattak:** Mi agradecimiento. Escribiré otra estrofa que describa tu amable acto...
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
    - **Khattak:** Tal vez alguien más arroje una cuerda a este enorme vacío...

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


##### Tarea #1

- **Khattak:** El hijo adolescente de un buen amigo mío está muriendo lentamente. Ahora no es el momento de dejar que la arena nos lo quite.
- (Condition: If the item desired is balls of wool:)
  - {{anchor|first}} **Khattak:** ¿Podrías traerme [número] ovillos de lana? Realmente nos vendría bien algo con lo que juegue el gato.
  - (continue)
- (Condition: If the item desired is potatoes:)
  - {{anchor|first}} **Khattak:** ¿Podrías traerme patatas [número]? Realmente nos vendría bien un cultivo tuberoso y almidonado.
  - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Khattak:** Mi agradecimiento. Escribiré otra estrofa que describa tu amable acto...
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Khattak:** Tal vez alguien más arroje una cuerda a este enorme vacío...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Khattak:** Tal vez alguien más arroje una cuerda a este enorme vacío...
      - [Choice]: No.
        - **Khattak:** Tal vez alguien más arroje una cuerda a este enorme vacío...

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Khattak:** ¿Tienes [número] [item]? El niño realmente necesita ayuda. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Khattak:** ¿Tienes [número] de [item]? El niño realmente necesita ayuda. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Khattak ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Khattak:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Khattak:** ¿Tienes [número] de [item]? El niño realmente necesita ayuda. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items)  (receives=experience)
    - Número de [item] dado a Khattak ([número]/[número])
    - **Khattak:** Fantástico, gracias.
    - **Khattak:** Bien, muchas gracias.
    - **Khattak:** Ahora que está hecho, necesitamos el siguiente bloque de suministros.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2

- **Khattak:** Los siguientes suministros que necesito son una carga de [item].
- **Player:** Correcto. ¿Por qué [item]?
- **Khattak:** El taumaturgo nos dice que necesitamos [item]. No nos pareció prudente discutir.
- **Player:** Correcto. Si este... taumaturgo cree que un [item] podría ayudar, entonces supongo que deberíamos buscar a [item].
- **Khattak:** Haré los preparativos mientras no estás; ¿Es una petición razonable?
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Khattak:** Mi agradecimiento. Escribiré otra estrofa que describa tu amable acto...
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Khattak:** Tal vez alguien más arroje una cuerda a este enorme vacío...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Khattak:** Tal vez alguien más arroje una cuerda a este enorme vacío...
      - [Choice]: No.
        - **Khattak:** Tal vez alguien más arroje una cuerda a este enorme vacío...

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Khattak:** ¿Tienes [número] [item]? El niño necesita ayuda. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Khattak:** ¿Tienes [número] [item]? El niño necesita ayuda. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Khattak ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Khattak:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Khattak:** ¿Tienes [número] [item]? El niño necesita ayuda. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Khattak ([número]/[número])
    - **Khattak:** Estoy agradecido. Ayudándome con el [item 1] y ahora un poco de [item 2], se lo agradezco.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Khattak:** Oh, no...
- **Player:** ¿Qué?
- **Khattak:** Tengo... esperanzas. Me preocupa que nos hayas dado esperanza, sólo para que la arena nos la arrebate.
- **Khattak:** No importa. Tomaré este breve momento de consuelo por lo que es.
- **Player:** Una buena idea. ¿De qué otra manera puedo ayudar?
- **Khattak:** Tenemos todo lo que necesitamos. Si aún quieres ayudar: mientras cuidamos al niño, hemos descuidado nuestras tareas diarias.
- (Condition: If the item desired is coal:)
  - {{anchor|first}} **Khattak:** Si pudieras conseguirnos combustible para el horno, nos permitirías otro día de paz.
  - (continue)
- (Condition: If the item desired is wolf bones:)
  - {{anchor|first}} **Khattak:** Si pudieras obtener huesos de lobo, arrojados por los lobos para nosotros, nos permitirías otro día de paz.
  - (continue)
- **Khattak:** Conseguir [número] [item] debería ser suficiente.
- [Menu]: Selecciona una opción
  - [Choice]: Por supuesto.
    - **Khattak:** Mi agradecimiento. Escribiré otra estrofa que describa tu amable acto...
  - [Choice]: No tengo tiempo ahora.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Khattak:** Tal vez alguien más arroje una cuerda a este enorme vacío...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Khattak:** Tal vez alguien más arroje una cuerda a este enorme vacío...
      - [Choice]: No.
        - **Khattak:** Tal vez alguien más arroje una cuerda a este enorme vacío...

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Khattak:** ¿Tienes [número] [item]? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Khattak:** ¿Tienes [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Khattak ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Khattak:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Khattak:** ¿Tienes [número] de [item]? ([número] restantes)
    - **Player:** Sí, tengo el [item]. Espero que esto sirva.
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Khattak ([número]/[número])
    - **Khattak:** Estoy agradecido. Todos lo apreciamos.
    - **Khattak:** ¡Muchas gracias por ayudarme!
    - (receives=Menaphite gift offering and 2,000 reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

#### Nuevo producto

- {{transcript missing}}

#### Slayer master

- {{transcript missing}}

#### esfuerzo War

- {{transcript missing}}
