# Henutemipet

- **Original Wiki Page**: [Transcript:Henutemipet](https://runescape.wiki/w/Transcript%3AHenutemipet)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Henutemipet:** A menudo soy la última persona en poner las manos sobre los difuntos antes de ser sepultados. Hay una hermosa finalidad en todo, si la buscas.

### City quest dialogue

- **Henutemipet:** Hay algo con lo que necesito ayuda, ¿tienes algo de tiempo?
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Henutemipet:** Los dioses te sonríen.
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
    - **Henutemipet:** Los dioses me enviarán a alguien muy pronto.

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

- **Henutemipet:** El magnífico Crondis se ha enfadado con [monster]. Requiere un sacrificio de sangre y un tributo.
- **Henutemipet:** Primero, ve y mata a [número] [monster].
- **Player:** ¿Qué han hecho los [monster] para enojar al todopoderoso Crondis?
- **Henutemipet:** No necesitas saberlo. ¿Irás a matarlos?
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Henutemipet:** Los dioses te sonríen.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Henutemipet:** Los dioses me enviarán a alguien muy pronto.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Henutemipet:** Los dioses me enviarán a alguien muy pronto.
      - [Choice]: No.
        - **Henutemipet:** Los dioses me enviarán a alguien muy pronto.

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Henutemipet:** ¿Has vencido al [número] [monster] para Lady Crondis? ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Henutemipet:** ¿Has vencido al [número] [monster] para Lady Crondis? ([número] restantes)
    - **Player:** Sí, he masacrado al [monster].
    - (receives=Slayer experience)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea #2


##### Primera vez

- **Henutemipet:** ¡Alabado sea Crondis!
- **Henutemipet:** Ahora que los miserables han pagado por sus transgresiones, requerimos un holocausto.

##### Después

- **Henutemipet:** Lo siguiente que necesito es [item].
- **Player:** Correcto. ¿Por qué [item]?
- **Henutemipet:** El primer paso para apaciguar a Crondis es tradicionalmente una ofrenda quemada de [item].
- **Henutemipet:** Así que ve y consigue [número] [item].
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Henutemipet:** Los dioses te sonríen.
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Henutemipet:** Los dioses me enviarán a alguien muy pronto.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Henutemipet:** Los dioses me enviarán a alguien muy pronto.
      - [Choice]: No.
        - **Henutemipet:** Los dioses me enviarán a alguien muy pronto.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Henutemipet:** ¿Tienes el tributo a Crondis? Ella se impacienta. Necesito [número] [item]. ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Henutemipet:** ¿Tienes el tributo a Crondis? Ella se impacienta. Necesito [número] [item]. ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Henutemipet ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Henutemipet:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Henutemipet:** ¿Tienes el tributo a Crondis? Ella se impacienta. Necesito [número] [item]. ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Henutemipet ([número]/[número])
    - **Henutemipet:** ¡Que el gran cocodrilo te sonría!
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Henutemipet:** Finalmente, según la tradición, Crondis requiere que se vierta una ofrenda líquida en el Elid.
- **Player:** ¿Una oferta líquida?
- **Henutemipet:** Sí, reúne [número] [item] para mí y haré que los trabajadores los liquiden.
- [Menu]: Selecciona una opción
  - [Choice]: Claro.
    - **Henutemipet:** Los dioses te sonríen.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Henutemipet:** Los dioses me enviarán a alguien muy pronto.
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Henutemipet:** Los dioses me enviarán a alguien muy pronto.
      - [Choice]: No.
        - **Henutemipet:** Los dioses me enviarán a alguien muy pronto.

##### Sin artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Henutemipet:** ¿Has reunido el [número] [item]? ¡Necesitamos apaciguar a Crondis lo antes posible! ([número] restantes)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Con algunos de los artículos

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Henutemipet:** ¿Has reunido el [número] [item]? ¡Necesitamos apaciguar a Crondis lo antes posible! ([número] restantes)
    - (removes=the requested items)
    - Número de [item] dado a Henutemipet ([número]/[número])
    - (Condition: Si el player dio solo uno de los elementos:)
      - **Player:** Sólo uno por ahora. Tómalo. Vuelvo enseguida.
      - (continue)
    - (Condition: Si el player tenía varios del artículo:)
      - **Player:** Tengo algunos. Tómelos. Vuelvo enseguida.
      - (continue)
    - **Henutemipet:** Genial. Gracias.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Con todo el artículo

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Henutemipet:** ¿Has reunido el [número] [item]? ¡Necesitamos apaciguar a Crondis lo antes posible! ([número] restantes)
    - **Player:** Sí, tengo el [item].
    - (removes=the requested items) (receives=experience)
    - Número de [item] dado a Henutemipet ([número]/[número])
    - **Henutemipet:** ¿No eres trabajador? Buen trabajo.
    - **Henutemipet:** ¡Muchas gracias por ayudarme!
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


##### Tarea #1

- **Henutemipet:** Me han encomendado la tarea de conseguir suministros para el esfuerzo bélico.
- **Player:** ¿Quiénes somos? ¿Con quién estás en guerra TÚ?
- **Henutemipet:** Todo será revelado. Primero necesito [número] [item]. ¿Puedo confiar en ti?
- [Menu]: Selecciona una opción
  - [Choice]: Afirmativo.
    - **Henutemipet:** Los dioses te sonríen.
  - [Choice]: Negativo.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - {{transcript missing}}
      - [Choice]: No.
        - **Henutemipet:** Los dioses me enviarán a alguien muy pronto.

##### Sin artículo

- {{transcript missing}}

##### Con algunos de los artículos

- {{transcript missing}}

##### Con todo el artículo

- {{transcript missing}}

##### Tarea #2


##### Primera vez

- {{transcript missing}}

##### Después

- {{transcript missing}}

##### Sin artículo

- {{transcript missing}}

##### Con algunos de los artículos

- {{transcript missing}}

##### Con todo el artículo

- {{transcript missing}}

##### Tarea #3

- {{transcript missing}}

##### Tarea incompleta

- {{transcript missing}}

##### Tarea completada

- {{transcript missing}}
