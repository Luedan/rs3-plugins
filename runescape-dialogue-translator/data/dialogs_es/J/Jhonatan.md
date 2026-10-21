# Jhonatan

- **Original Wiki Page**: [Transcript:Jhonatan](https://runescape.wiki/w/Transcript%3AJhonatan)
- **Letter**: `J`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|city quest}}

### Standard dialogue

- **Jhonatan:** Eres bienvenido a nuestra casa.

### Overhead dialogue

- {{trandom}}
  - (Condition: Diálogo 1)
    - **Jhonatan:** {{RSChat|I love you, my dear.}}
    - **Sabrina:** {{RSChat|I know, my sweet.}}
  - (Condition: Diálogo 2)
    - **Jhonatan:** {{RSChat|We should go see a show or something.}}
    - **Sabrina:** {{RSChat|There's a performer nearby, I already bought tickets.}}
    - **Jhonatan:** {{RSChat|Haha! Of course.}}

### City Quest

- **Jhonatan:** Saludos. ¿Tienes un momento libre? Necesito ayuda.
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Jhonatan:** Mi agradecimiento.
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


##### Tarea #1

- **Jhonatan:** Estoy exhausto porque mis hijos no pueden dormir por la noche.
- **Player:** Oh, eso es horrible, ¿por qué no pueden dormir?
- **Jhonatan:** Mi hijo mayor tiene demasiado miedo para dormir debido al [monster].
- **Jhonatan:** ¿Podrías ir a buscar algunos [monster] y reducir sus números?
- **Player:** Parece un poco excesivo... ¿Con cuántos tendría que lidiar?
- **Jhonatan:** ¿Podrías matar a [número] [monster] por mí?
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Jhonatan:** Mi agradecimiento.
    - **Player:** ¿Dónde puedo encontrar [monster]?
    - (Condition: Si el monstruo asignado son matones menafitas:)
      - **Jhonatan:** Fueron exiliados. Se rumorea que se han instalado en Pollnivneach. Eso es lo que he oído.
    - (Condition: Si el monstruo asignado son guardias del campamento minero:)
      - **Jhonatan:** El campamento minero está en algún lugar del desierto, al norte. Eso es lo que he oído.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Jhonatan:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Jhonatan:** No importa.
      - [Choice]: No.
        - **Jhonatan:** No importa.

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Se ocuparon del [número] [monster]? ([número] restantes)
    - **Player:** Todavía no. ¿Dónde podría encontrar [monster] nuevamente?
    - (Condition: Si el monstruo asignado son matones menafitas:)
      - **Jhonatan:** Fueron exiliados. Se rumorea que se han instalado en Pollnivneach.
    - (Condition: Si el monstruo asignado son guardias del campamento minero:)
      - **Jhonatan:** El campamento minero está en algún lugar del desierto, al norte.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Se ocuparon del [número] [monster]? ([número] restantes)
    - **Player:** Sí, el [monster] no volverá a asustar a tu hijo en el corto plazo.
    - (receives=Slayer experience)
    - **Jhonatan:** Gracias. Por excesivo que pareciera, ¡era necesario!
    - **Jhonatan:** Ahora que puede dormir tranquilo, hablemos de mi hija.
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea #2

- **Jhonatan:** Desde que era pequeña, no puede dormir sin [item].
- **Player:** Correcto. ¿Por qué [item]?
- **Jhonatan:** Sí, sé que es un poco extraño, pero [item] era lo único que la ayudaría a quedarse dormida.
- **Jhonatan:** Entonces, por favor, si pudieras conseguir [número] [item], te lo agradecería mucho.
- [Menu]: Selecciona una opción
  - [Choice]: Muy bien.
    - **Jhonatan:** Mi agradecimiento.
    - **Player:** ¿Sabes dónde puedo conseguir [item]?
    - (Condition: Si el artículo deseado es mineral de cobre:)
      - **Jhonatan:** El mineral de cobre se puede encontrar al sureste de Varrock.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Jhonatan:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Jhonatan:** No importa.
      - [Choice]: No.
        - **Jhonatan:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Ya has encontrado [número] [item]? ([número] restantes)
    - **Player:** No, ¿dónde debería buscar el [item]?
    - (continuea)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Ya has encontrado [número] [item]? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Jhonatan ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Jhonatan:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Ya has encontrado [número] [item]? ([número] restantes)
    - **Player:** Tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Jhonatan ([número]/[número])
    - **Jhonatan:** ¡Excelente, mi hija podrá volver a dormir como un bebé!
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Jhonatan:** Ahora, mi hijo menor, recientemente perdió su osito de peluche.
- **Player:** ¿Quieres que le busque un nuevo osito de peluche?
- **Jhonatan:** No, no. Puede que no lo parezca, pero soy bastante hábil en la elaboración. Planeo hacerle uno nuevo si pudieras conseguirme los materiales.
- **Player:** ¿Qué necesitas?
- **Jhonatan:** Necesito [número] [item] para salir.
- **Player:** ...
- **Jhonatan:** ...
- **Jhonatan:** Entonces, ¿podrías conseguirme [número] [item]?
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Jhonatan:** Mi agradecimiento.
    - **Player:** ¿Qué sabes sobre [item]?
    - (Condition: Si el artículo deseado son velas negras:)
      - **Jhonatan:** He oído que hay un fabricante de velas de renombre en Catherby.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Jhonatan:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Jhonatan:** No importa.
      - [Choice]: No.
        - **Jhonatan:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Trajiste [número] [item]? ¡Este osito de peluche no se construirá solo! ([número] restantes)
    - **Player:** Todavía no. ¿Podrías indicarme la dirección de algún [item]?
    - (continuea)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Trajiste [número] [item]? ¡Este osito de peluche no se construirá solo! ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Jhonatan ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Jhonatan:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Trajiste [número] [item]? ¡Este osito de peluche no se construirá solo! ([número] restantes)
    - **Player:** Sí, he traído el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Jhonatan ([número]/[número])
    - **Player:** Entonces, ¿cómo se hace un osito de peluche con...?
    - **Player:** No. Creo que es mejor no saberlo.
    - **Jhonatan:** ¡Excelente! ¡Me pondré manos a la obra!
    - **Jhonatan:** Entonces, mi otro hijo...
    - **Player:** Eh... Adiós.
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

#### Coleccionista de curiosidades

- {{transcript missing}}

#### Crondis está enojado


##### Tarea #1

- **Jhonatan:** El magnífico Crondis se ha enfadado con [monster]. Requiere un sacrificio de sangre y un tributo.
- **Jhonatan:** Primero, ve y mata a [número] [monster].
- **Player:** ¿Qué han hecho los [monster] para enojar al todopoderoso Crondis?
- **Jhonatan:** No necesitas saberlo. ¿Irás a matarlos?
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Jhonatan:** Mi agradecimiento.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - {{transcript missing}}
      - [Choice]: No.
        - **Jhonatan:** No importa.

##### Hablando con él de nuevo con la tarea de cazador incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Has vencido al [número] [monster] para Lady Crondis? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

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


##### Tarea #1

- **Jhonatan:** Me han encomendado la tarea de conseguir suministros para el esfuerzo bélico.
- **Player:** ¿Quiénes somos? ¿Con quién estás en guerra TÚ?
- **Jhonatan:** Todo será revelado. Primero necesito [número] [items]. ¿Puedo confiar en ti?
- [Menu]: Selecciona una opción
  - [Choice]: Afirmativo.
    - **Jhonatan:** Mi agradecimiento.
  - [Choice]: Negativo.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - {{transcript missing}}
      - [Choice]: No.
        - **Jhonatan:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Jhonatan ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Jhonatan:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Jhonatan ([número]/[número])
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2


##### Primera vez

- **Jhonatan:** ¡Buen trabajo, soldado!
- **Jhonatan:** Ahora que está hecho, necesitamos el siguiente bloque de suministros.

##### Después

- **Jhonatan:** Los siguientes suministros que necesito son una carga de [item].
- **Player:** Correcto. ¿Por qué [item]?
- **Jhonatan:** ¿Alguna vez has intentado pelear una guerra sin [item]? No lo creo.
- **Jhonatan:** El esfuerzo de guerra requiere [número] [item]. ¿Asumo que puedo confiar en usted para obtener el [item]?
- [Menu]: Selecciona una opción
  - [Choice]: Seguro que puedes.
    - **Jhonatan:** Mi agradecimiento.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Jhonatan:** No importa.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Jhonatan:** No importa.
      - [Choice]: No.
        - **Jhonatan:** No importa.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Jhonatan ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Jhonatan:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Jhonatan:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Jhonatan ([número]/[número])
    - **Jhonatan:** ¡Genial! ¡Ahora estamos listos para llevar la ofensiva a casa!
    - **Player:** ¿Puedo preguntar por qué hablas así?
    - **Jhonatan:** ¿Qué quieres decir, soldado?
    - **Player:** Estás hablando como un general imperial. Es un poco desagradable.
    - **Jhonatan:** ...
    - **Jhonatan:** Los guardias siempre están mirando. Tengo que guardar las apariencias.
    - **Player:** Cierto... bastante justo. ¿Qué más... nosotros... necesitamos para el esfuerzo bélico?
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Jhonatan:** ¡Ahora es el momento que estabas esperando, soldado! ¡La matanza!
- **Jhonatan:** ¡Finalmente venceremos a nuestro temido enemigo, el [monster]!
- **Player:** ¿Qué?
- **Jhonatan:** ¡Sí, mata a [número] [monster] en nombre del propio Faraón!
- [Menu]: Selecciona una opción
  - [Choice]: Está bien.
    - **Jhonatan:** Mi agradecimiento.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - {{transcript missing}}
      - [Choice]: No.
        - **Jhonatan:** No importa.

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el monstruo es una plaga de ranas:)
    - **Jhonatan:** ¿Has matado a [número] [monster]? Por lo general, están adelgazando alrededor de Sophanem. ¡Podríamos ganar esta guerra todavía! ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el monstruo es una plaga de ranas:)
      - **Jhonatan:** ¿Has matado a [número] [monster]? Por lo general, están adelgazando alrededor de Sophanem. ¡Podríamos ganar esta guerra todavía! (0 restante)
      - (continue)
    - **Player:** Sí, he matado al [monster].
    - (receives=Slayer experience)
    - **Jhonatan:** ¿Has bailado, como dicen, en la sangre de tus enemigos? ¿Has enviado las almas de [número] [monster] al Inframundo?
    - **Jhonatan:** No es que esos [monster] tengan alma, creo que realmente no pueden recibir ayuda.
    - **Jhonatan:** ¡Muchas gracias por ayudarme!
    - **Player:** Me temo que todavía necesitas mucha más ayuda.
    - **Jhonatan:** Lo siento, ¿qué?
    - **Player:** Nada. Fue un placer.
    - (Action: La misión está completa.)
    - (receives=a Menaphite gift offering and 2,000 reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.
