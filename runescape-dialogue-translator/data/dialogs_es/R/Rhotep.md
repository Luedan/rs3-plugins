# Rhotep

- **Original Wiki Page**: [Transcript:Rhotep](https://runescape.wiki/w/Transcript%3ARhotep)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Missing city quest dialogue.}}

### Standard dialogue

- **Rhotep:** Juro que el maestro herrero se está volviendo loco. Cree que alguien sigue entrando y llevándose nuestros yunques, pero todavía están aquí.

### City quest dialogue

- **Rhotep:** Por favor, ¿dedicas un poco de tu tiempo a ayudar a un aprendiz?
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Rhotep:** Muchas gracias.
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
    - **Rhotep:** Oh, ¿qué haré?

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

- **Rhotep:** El magnífico Crondis se ha enfadado con [monster]. Requiere un sacrificio de sangre y un tributo.
- **Rhotep:** Primero, ve y mata a [número] [monster].
- **Player:** ¿Qué han hecho los [monster] para enojar al todopoderoso Crondis?
- **Rhotep:** No necesitas saberlo. ¿Irás a matarlos?
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Rhotep:** Muchas gracias.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Rhotep:** Oh, ¿qué haré?
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Rhotep:** Oh, ¿qué haré?
      - [Choice]: No.
        - **Rhotep:** Oh, ¿qué haré?

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Rhotep:** ¿Has vencido al [número] [monster] para Lady Crondis? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Rhotep:** ¿Has vencido al [número] [monster] para Lady Crondis? ([número] restantes)
    - **Player:** Sí, he masacrado al [monster].
    - (receives=Slayer experience)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea #2


##### Primera vez

- **Rhotep:** ¡Alabado sea Crondis!
- **Rhotep:** Ahora que los miserables han pagado por sus transgresiones, requerimos un holocausto.

##### Después

- **Rhotep:** Lo siguiente que necesito es [item].
- **Player:** Correcto. ¿Por qué [item]?
- **Rhotep:** El primer paso para apaciguar a Crondis es tradicionalmente una ofrenda quemada de [item].
- **Rhotep:** Así que ve y consigue [número] [item].
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Rhotep:** Muchas gracias.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Rhotep:** Oh, ¿qué haré?
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Rhotep:** Oh, ¿qué haré?
      - [Choice]: No.
        - **Rhotep:** Oh, ¿qué haré?

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Rhotep:** ¿Tienes el tributo a Crondis? Ella se impacienta. Necesito [número] [item]. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Rhotep:** ¿Tienes el tributo a Crondis? Ella se impacienta. Necesito [número] [item]. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Rhotep ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Rhotep:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Rhotep:** ¿Tienes el tributo a Crondis? Ella se impacienta. Necesito [número] [item]. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Rhotep ([número]/[número])
    - **Rhotep:** ¡Que el gran cocodrilo te sonría!
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Rhotep:** Finalmente, según la tradición, Crondis requiere que se vierta una ofrenda líquida en el Elid.
- **Player:** ¿Una oferta líquida?
- **Rhotep:** Sí, reúne [número] [item] para mí y haré que los trabajadores los liquiden.
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Rhotep:** Muchas gracias.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Rhotep:** Oh, ¿qué haré?
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Rhotep:** Oh, ¿qué haré?
      - [Choice]: No.
        - **Rhotep:** Oh, ¿qué haré?

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Rhotep:** ¿Has reunido el [número] [item]? ¡Necesitamos apaciguar a Crondis lo antes posible! ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Rhotep:** ¿Has reunido el [número] [item]? ¡Necesitamos apaciguar a Crondis lo antes posible! ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Rhotep ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Rhotep:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Rhotep:** ¿Has reunido el [número] [item]? ¡Necesitamos apaciguar a Crondis lo antes posible! ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Rhotep ([número]/[número])
    - **Rhotep:** ¿No eres trabajador? Buen trabajo.
    - **Rhotep:** ¡Muchas gracias por ayudarme!
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

- {{transcript missing}}

#### esfuerzo War

- {{transcript missing}}
