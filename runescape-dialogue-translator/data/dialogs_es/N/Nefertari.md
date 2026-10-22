# Nefertari

- **Original Wiki Page**: [Transcript:Nefertari](https://runescape.wiki/w/Transcript%3ANefertari)
- **Letter**: `N`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|Missing city quest dialogue.}}

### Standard dialogue

- **Nefertari:** ¡Bienvenido a mi puesto! ¿Quieres un poco de pan?
- (opens=Nefertari's Bread Stall)

### Overhead dialogue

- **Nefertari:** {{RSChat|Buy my grains! Flour for sale!}}

### City quest dialogue

- **Nefertari:** ¡Bienvenido a mi puesto! ¿Quieres un poco de pan? En realidad... ¿podrías ayudarme por favor?
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Nefertari:** ¡Gracias!
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
    - **Nefertari:** No importa.

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


##### Tarea #1

- (Condition: If the item desired is bones:)
  - **Nefertari:** Tengo un conocido al que le entrego huesos con regularidad. Dependen de mí para realizar las entregas según un cronograma regular.
  - **Nefertari:** No tengo idea de por qué siempre se solicitan huesos. No voy a preguntar por qué alguien necesita algunos huesos viejos y normales, caídos de criaturas.
  - (continue)
- (Condition: If the item desired is fire battlestaves:)
  - **Nefertari:** Tengo un conocido a quien le entrego regularmente bastones de fuego. Dependen de mí para realizar las entregas según un cronograma regular.
  - **Nefertari:** No tengo idea de por qué siempre se solicitan bastones de batalla de fuego. No voy a preguntar por qué alguien necesita un staff con magia de fuego.
  - (continue)
- **Nefertari:** ¿Podrías traerme [número] [item]?
- [Menu]: Selecciona una opción
  - [Choice]: Bien, entonces.
    - **Nefertari:** ¡Gracias!
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Nefertari:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Nefertari:** No importa.
      - [Choice]: No.
        - **Nefertari:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Nefertari:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Nefertari:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Nefertari ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Nefertari:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Nefertari:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Nefertari ([número]/[número])
    - **Nefertari:** ¡Gracias!
    - **Nefertari:** Mientras estabas recogiendo [item], recordé que mi carrito tiene una rueda rota y necesito arreglarla antes de poder empezar a pensar en hacer una entrega.
    - **Nefertari:** El carretero del distrito portuario no acepta gold coins como pago y tendré que intercambiar bienes con ella para que me arreglen la rueda.
    - **Player:** ¿Qué necesitas para intercambiarla?
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2

- **Nefertari:** Para poder conseguir que el carretero arregle mis ruedas, a menudo necesito cambiarle una carga de [item].
- **Player:** Correcto. ¿Por qué [item]?
- (Condition: If the item desired is copper ore:)
  - **Nefertari:** No tengo idea. ¿Quién soy yo para preguntar por qué un carretero necesita rocas ricas en cobre?
  - (continue)
- (Condition: If the item desired is raw beltfish:)
  - **Nefertari:** No tengo idea. ¿Quién soy yo para preguntar por qué un carretero necesita un pescado correoso, listo para ser cocinado?
  - (continue)
- **Nefertari:** Si pudieras traerme [número] [item], me aseguraré de reembolsarte tu tiempo.
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Nefertari:** ¡Gracias!
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Nefertari:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Nefertari:** No importa.
      - [Choice]: No.
        - **Nefertari:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Nefertari:** Espero que me arreglen la rueda lo antes posible, Player. ¿Tienes [número] [item]? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Nefertari:** Espero que me arreglen la rueda lo antes posible, Player. ¿Tienes [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Nefertari ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Nefertari:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Nefertari:** Espero que me arreglen la rueda lo antes posible, Player. ¿Tienes [número] [item]? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Nefertari ([número]/[número])
    - **Nefertari:** Estoy agradecido. Ayudándome con el [item 1] y ahora un poco de [item 2], se lo agradezco.
    - **Nefertari:** Parece que mi carrito seguirá serpenteando por la arena durante muchos días más.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Nefertari:** Ahora lo único que queda es conseguir algunos suministros para el viaje.
- **Player:** No es broma. ¿Qué necesitas?
  - (Condition: If the item desired is barberry seeds:)
    - **Nefertari:** Tengo todo lo que necesito excepto las semillas que se convierten en arbustos de agracejo.
    - (continue)
  - (Condition: If the item desired is sharks:)
    - **Nefertari:** Tengo todo lo que necesito excepto unos tiburones bien cocinados.
    - (continue)
- **Nefertari:** Si pudieras conseguirme [número] [item], entonces puedo seguir mi camino.
- [Menu]: Selecciona una opción
  - [Choice]: Claro, está bien, lo que sea.
    - **Nefertari:** ¡Gracias!
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Nefertari:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Nefertari:** No importa.
      - [Choice]: No.
        - **Nefertari:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Nefertari:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Nefertari:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Nefertari ([número]/[número])
    - (Condition: If the player gave only one of the item:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: If the player had multiple of the item:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Nefertari:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Nefertari:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Nefertari ([número]/[número])
    - **Nefertari:** Estoy agradecido. Los [item] están empacados y listos para funcionar, y ahora tengo algunos [item] para el viaje.
    - **Nefertari:** ¡Muchas gracias por ayudarme!
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

#### El hijo de un amigo está muriendo lentamente.

- {{transcript missing}}

#### Nuevo producto

- {{transcript missing}}

#### Slayer master

- {{transcript missing}}

#### esfuerzo War

- {{transcript missing}}
