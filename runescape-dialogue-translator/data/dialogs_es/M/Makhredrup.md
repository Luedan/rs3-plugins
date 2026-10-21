# Makhredrup

- **Original Wiki Page**: [Transcript:Makhredrup](https://runescape.wiki/w/Transcript%3AMakhredrup)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Makhredrup:** Raja es un gigante gentil. Está aquí por petición del faraón y espero que no lo retengan por mucho tiempo. No está acostumbrado a esas temperaturas.

### City quest dialogue

- **Makhredrup:** Bienvenido, bienvenido. ¿Tienes un momento para ayudarme?
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Makhredrup:** ¡Sí! Eres simplemente el mejor.
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

- {{transcript missing}}

#### Ayuda de entrega


##### Tarea #1

- (Condition: Si el artículo deseado son huesos:)
  - **Makhredrup:** Tengo un conocido al que le entrego huesos con regularidad. Dependen de mí para realizar las entregas según un cronograma regular.
  - **Makhredrup:** No tengo idea de por qué siempre se solicitan huesos. No voy a preguntar por qué alguien necesita algunos huesos viejos y normales, caídos de criaturas.
  - (continue)
- (Condition: Si el objeto deseado son bastones de batalla de fuego:)
  - **Makhredrup:** Tengo un conocido a quien le entrego regularmente bastones de fuego. Dependen de mí para realizar las entregas según un cronograma regular.
  - **Makhredrup:** No tengo idea de por qué siempre se solicitan bastones de batalla de fuego. No voy a preguntar por qué alguien necesita un staff con magia de fuego.
  - (continue)
- **Makhredrup:** ¿Podrías traerme [número] [item]?
- [Menu]: Selecciona una opción
  - [Choice]: Bien, entonces.
    - **Makhredrup:** ¡Sí! Eres simplemente el mejor.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Makhredrup:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Makhredrup:** No importa.
      - [Choice]: No.
        - **Makhredrup:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Makhredrup:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Makhredrup:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Makhredrup ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Makhredrup:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Makhredrup:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Makhredrup ([número]/[número])
    - **Makhredrup:** ¡Sí! Eres simplemente el mejor.
    - **Makhredrup:** Mientras estabas recogiendo [item], recordé que mi carrito tiene una rueda rota y necesito arreglarla antes de poder empezar a pensar en hacer una entrega.
    - **Makhredrup:** El carretero del distrito portuario no acepta gold coins como pago y tendré que intercambiar bienes con ella para que me arreglen la rueda.
    - **Player:** ¿Qué necesitas para intercambiarla?
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2

- **Makhredrup:** Para poder conseguir que el carretero arregle mis ruedas, a menudo necesito cambiarle una carga de [item].
- **Player:** Correcto. ¿Por qué [item]?
- (Condition: Si el artículo deseado es mineral de cobre:)
  - **Makhredrup:** No tengo idea. ¿Quién soy yo para preguntar por qué un carretero necesita rocas ricas en cobre?
  - (continue)
- (Condition: Si el producto deseado es pez cinturón crudo:)
  - **Makhredrup:** No tengo idea. ¿Quién soy yo para preguntar por qué un carretero necesita un pescado correoso, listo para ser cocinado?
  - (continue)
- **Makhredrup:** Si pudieras traerme [número] [item], me aseguraré de reembolsarte tu tiempo.
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Makhredrup:** ¡Sí! Eres simplemente el mejor.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Makhredrup:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Makhredrup:** No importa.
      - [Choice]: No.
        - **Makhredrup:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Makhredrup:** Espero que me arreglen la rueda lo antes posible, Player. ¿Tienes [número] [item]? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Makhredrup:** Espero que me arreglen la rueda lo antes posible, Player. ¿Tienes [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Makhredrup ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Makhredrup:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Makhredrup:** Espero que me arreglen la rueda lo antes posible, Player. ¿Tienes [número] [item]? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Makhredrup ([número]/[número])
    - **Makhredrup:** Estoy agradecido. Ayudándome con el [item 1] y ahora un poco de [item 2], se lo agradezco.
    - **Makhredrup:** Parece que mi carrito seguirá serpenteando por la arena durante muchos días más.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Makhredrup:** Ahora lo único que queda es conseguir algunos suministros para el viaje.
- **Player:** No es broma. ¿Qué necesitas?
  - (Condition: Si el artículo deseado son semillas de agracejo:)
    - **Makhredrup:** Tengo todo lo que necesito excepto las semillas que se convierten en arbustos de agracejo.
    - (continue)
  - (Condition: Si el artículo deseado son tiburones:)
    - **Makhredrup:** Tengo todo lo que necesito excepto unos tiburones bien cocinados.
    - (continue)
- **Makhredrup:** Si pudieras conseguirme [número] [item], entonces puedo seguir mi camino.
- [Menu]: Selecciona una opción
  - [Choice]: Claro, está bien, lo que sea.
    - **Makhredrup:** ¡Sí! Eres simplemente el mejor.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Makhredrup:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Makhredrup:** No importa.
      - [Choice]: No.
        - **Makhredrup:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Makhredrup:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Makhredrup:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Makhredrup ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Makhredrup:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Makhredrup:** ¿Tienes [número] [item]? Estoy un poco presionado por el tiempo. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Makhredrup ([número]/[número])
    - **Makhredrup:** Estoy agradecido. Los [item] están empacados y listos para funcionar, y ahora tengo algunos [item] para el viaje.
    - **Makhredrup:** ¡Muchas gracias por ayudarme!
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

### Overhead dialogue

*Makhredrup ocasionalmente producirá diálogos generales.*
- **Makhredrup:** {{RSChat|There, there. I know it's warm here, Raja.|colour=yellow|shadow=yes}}
