# Kharl

- **Original Wiki Page**: [Transcript:Kharl](https://runescape.wiki/w/Transcript%3AKharl)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|City quest dialogue.}}

### Standard dialogue

- **Kharl:** ¿Alguna vez te ha gustado simplemente... bailar? Sin duda es un pasatiempo asequible.

### Overhead dialogue

*Ocasionalmente, Kharl habla solo en un diálogo aéreo.*
- {{RSChat|Dance, Kharl, dance.|colour=yellow|shadow=yes}}

### City quest dialogue

- **Kharl:** Por favor... dedica algo de tiempo. Necesito ayuda.
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Kharl:** Ah... ¡qué amable!
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
    - **Kharl:** No importa.

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

- {{transcript missing}}

#### Slayer master

- {{transcript missing}}

#### esfuerzo War


##### Tarea #1

- **Kharl:** Me han encomendado la tarea de conseguir suministros para el esfuerzo bélico.
- **Player:** ¿Quiénes somos? ¿Con quién estás en guerra TÚ?
- **Kharl:** Todo será revelado. Primero necesito [número] [items]. ¿Puedo confiar en ti?
- [Menu]: Selecciona una opción
  - [Choice]: Afirmativo.
    - **Kharl:** Ah... ¡qué amable!
  - [Choice]: Negativo.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Kharl:** Oh, bueno, tal vez aparezca alguien más.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Kharl:** Oh, bueno, tal vez aparezca alguien más.
      - [Choice]: No.
        - **Kharl:** Oh, bueno, tal vez aparezca alguien más.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Kharl:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Kharl:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Kharl ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Kharl:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Kharl:** ¿Tienes el [número] [item] a mano, soldado? ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Kharl ([número]/[número])
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2


##### Primera vez

- **Kharl:** ¡Buen trabajo, soldado!
- **Kharl:** Ahora que está hecho, necesitamos el siguiente bloque de suministros.

##### Después

- **Kharl:** Los siguientes suministros que necesito son una carga de [item].
- **Player:** Correcto. ¿Por qué [item]?
- **Kharl:** ¿Alguna vez has intentado pelear una guerra sin [item]? No lo creo.
- **Kharl:** El esfuerzo de guerra requiere [número] [item]. ¿Asumo que puedo confiar en usted para obtener el [item]?
- [Menu]: Selecciona una opción
  - [Choice]: Seguro que puedes.
    - **Kharl:** Ah... ¡qué amable!
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Kharl:** Oh, bueno, tal vez aparezca alguien más.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Kharl:** Oh, bueno, tal vez aparezca alguien más.
      - [Choice]: No.
        - **Kharl:** Oh, bueno, tal vez aparezca alguien más.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Kharl:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Kharl:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Kharl ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Kharl:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Kharl:** ¿Tienes los suministros, soldado? ¡Esta guerra no se financiará sola! ¡Necesitamos [número] [item]! ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Kharl ([número]/[número])
    - **Kharl:** ¡Genial! ¡Ahora estamos listos para llevar la ofensiva a casa!
    - **Player:** ¿Puedo preguntar por qué hablas así?
    - **Kharl:** ¿Qué quieres decir, soldado?
    - **Player:** Estás hablando como un general imperial. Es un poco desagradable.
    - **Kharl:** ...
    - **Kharl:** Los guardias siempre están mirando. Tengo que guardar las apariencias.
    - **Player:** Cierto... bastante justo. ¿Qué más... nosotros... necesitamos para el esfuerzo bélico?
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Kharl:** ¡Ahora es el momento que estabas esperando, soldado! ¡La matanza!
- **Kharl:** ¡Finalmente venceremos a nuestro temido enemigo, el [monster]!
- **Player:** ¿Qué?
- **Kharl:** ¡Sí, mata a [número] [monster] en nombre del propio Faraón!
- [Menu]: Selecciona una opción
  - [Choice]: Está bien.
    - **Kharl:** Ah... ¡qué amable!
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Kharl:** Oh, bueno, tal vez aparezca alguien más.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Kharl:** Oh, bueno, tal vez aparezca alguien más.
      - [Choice]: No.
        - **Kharl:** Oh, bueno, tal vez aparezca alguien más.

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el monstruo son los calfitos:)
      - **Kharl:** ¿Has matado a los calfitos de [número]? Se encuentran dentro de colmenas calfitas bajo las arenas del desierto. ¡Podríamos ganar esta guerra todavía! ([número] restante)
    - (Condition: Si el monstruo es una plaga de ranas:)
      - **Kharl:** ¿Has matado las ranas plaga [número]? Por lo general, están adelgazando alrededor de Sophanem. ¡Podríamos ganar esta guerra todavía! ([número] restante)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - (Condition: Si el monstruo son los calfitos:)
      - **Kharl:** ¿Has matado a los calfitos de [número]? Se encuentran dentro de colmenas calfitas bajo las arenas del desierto. ¡Podríamos ganar esta guerra todavía! ([número] restante)
      - (continue)
    - (Condition: Si el monstruo es una plaga de ranas:)
      - **Kharl:** ¿Has matado las ranas plaga [número]? Por lo general, están adelgazando alrededor de Sophanem. ¡Podríamos ganar esta guerra todavía! (0 restante)
      - (continue)
    - **Player:** Sí, he matado al [monster].
    - (receives=Slayer experience)
    - **Kharl:** ¿Has bailado, como dicen, en la sangre de tus enemigos? ¿Has enviado las almas de [número] [monster] al Inframundo?
    - **Kharl:** No es que esos [monster] tengan alma, creo que realmente no pueden recibir ayuda.
    - **Kharl:** ¡Muchas gracias por ayudarme!
    - **Player:** Me temo que todavía necesitas mucha más ayuda.
    - **Kharl:** Lo siento, ¿qué?
    - **Player:** Nada. Fue un placer.
    - (receives=a Menaphite gift offering and 2,000 reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.
