# Malala

- **Original Wiki Page**: [Transcript:Malala](https://runescape.wiki/w/Transcript%3AMalala)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|Missing city quest dialogue.}}

### Standard dialogue

- **Malala:** Cuando el mundo entero está en silencio, incluso una voz se vuelve poderosa.

### City quest dialogue

- **Malala:** Saludos, extraño. Por mucho que prefiera no pedir ayuda, tengo un problema grave. ¿Podrías ayudarme?
- [Menu]: ¿Quieres ayudar?
  - [Choice]: Sí.
    - **Malala:** Gracias, eres amable.
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
    - **Malala:** Es una pena, aunque tal vez alguien más pueda ayudar. espero...

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


##### Tarea #1

- **Malala:** Estoy listo para un cambio de carrera.
- **Player:** Oh, ¿en serio? ¿Cómo puedo ayudar?
- **Malala:** Bueno, realmente quiero ser un Slayer master, aunque me vendría bien un poco de práctica.
- **Player:** Muy bien, haz tu mejor esfuerzo.
- **Malala:** ¡Saludos, aventurero! ¡Soy yo, el Slayer master!
- **Malala:** ¿Cómo estuvo eso?
- **Player:** Sí, eso estuvo genial, pero tienes que decirme qué quieres que mate.
- **Malala:** ¡Ah, claro!
- **Malala:** ¡Aventurero! Necesito que mates... uh...
- **Malala:** Necesito que mates...[número]...[monster]?
- [Menu]: Selecciona una opción
  - [Choice]: Puedo hacer eso.
    - **Malala:** Gracias, eres amable.
    - **Player:** ¿Dónde puedo encontrar [monster]?
    - (Condition: Si el monstruo asignado son lagartos del desierto:)
<!-- This needs double-checking -->
      - {{anchor|first}} **Malala:** Se pueden encontrar al este en el desierto.
    - (Condition: Si el monstruo asignado son bandidos:)
<!-- This needs double-checking -->
      - {{anchor|first}} **Malala:** Creo que hay un gran campamento de bandidos al norte de aquí, más allá de la cantera.
    - (Condition: Si el monstruo asignado son escorpiones:)
      - {{anchor|first}} **Malala:** Están muy al norte, en la mina cerca de Al Kharid. Creo.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Malala:** Es una pena, aunque tal vez alguien más pueda ayudar. espero...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Malala:** Es una pena, aunque tal vez alguien más pueda ayudar. espero...
      - [Choice]: No.
        - **Malala:** Es una pena, aunque tal vez alguien más pueda ayudar. espero...

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Malala:** ¿Mataste al [número] [monster]? ([número] restantes)
    - **Player:** Todavía no. ¿Dónde podría encontrar [monster] nuevamente?
<!-- Seems to continue the above but removes ". I think." -->
    - (continuea|first)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Malala:** ¿Mataste al [número] [monster]? ([número] restantes)
    - **Player:** ¡Sí, los [monster] han sido asesinados!
    - (receives=Slayer experience)
    - **Malala:** ¡Buen trabajo, aventurero!
    - **Malala:** Entonces, ¿qué hago ahora?
    - **Player:** Dime qué necesito acabar a continuación.
    - **Malala:** ¿Otra vez? ¡Bueno!
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #2

- **Malala:** ¡Aventurero! ¡Necesito que mates más cosas por mí!
- **Player:** ¿Qué debo matar por ti, Slayer master?
- **Malala:** He decidido que debes matar a [número] [monster].
- [Menu]: Selecciona una opción
  - [Choice]: Seguro que puedes.
    - **Malala:** Gracias, eres amable.
    - **Player:** ¿Dónde puedo encontrar [monster]?
    - (Condition: Si el monstruo asignado son bandidos:)
      - {{anchor|first}} **Malala:** Hay un gran campamento de bandidos al norte de aquí, más allá de la cantera. Al menos ahí me dijeron...
    - (Condition: Si el monstruo asignado es kalfitas:)
      - {{anchor|first}} **Malala:** Se encuentran dentro de colmenas calfitas bajo las arenas del desierto. Al menos ahí me dijeron...
    - (Condition: Si el monstruo asignado es scabarites:)
      - {{anchor|first}} **Malala:** Habitan principalmente en la Colmena Scabarite. Al menos ahí me dijeron...
  - [Choice]: No, lo siento.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Malala:** Es una pena, aunque tal vez alguien más pueda ayudar. espero...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Malala:** Es una pena, aunque tal vez alguien más pueda ayudar. espero...
      - [Choice]: No.
        - **Malala:** Es una pena, aunque tal vez alguien más pueda ayudar. espero...

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Malala:** ¿Ya te has ocupado del [número] [monster]? ([número] restantes)
    - **Player:** No. ¿Dónde puedo encontrar el [monster] nuevamente?
    - (Condition: Si el monstruo asignado son bandidos:)
      - {{anchor|first}} **Malala:** Hay un gran campamento de bandidos al norte de aquí, más allá de la cantera.
    - (Condition: Si el monstruo asignado es scabarites:)
      - {{anchor|first}} **Malala:** Habitan principalmente en la Colmena Scabarite.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Malala:** ¿Ya te has ocupado del [número] [monster]? ([número] restantes)
    - **Player:** Sí, los [monster] ya no existen.
    - (receives=Slayer experience)
    - **Malala:** ¡Me estoy volviendo muy bueno en esto!
    - **Malala:** ¡Aventurero! ¡Tengo una tarea más para ti!
    - (continue)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (arriba)

##### Tarea #3

- **Malala:** ¡Quiero que mates a [número] [monster]!
- **Player:** Vaya, directo al grano.
- [Menu]: Selecciona una opción
  - [Choice]: Lo haré.
    - **Malala:** Gracias, eres amable.
    - **Player:** ¿Dónde puedo encontrar [monster]?
    - (Condition: Si el monstruo asignado son kalfitas exiliados:)
      - {{anchor|first}} **Malala:** Se encuentran dentro de las Colmenas Kalphite exiliadas, justo al norte de la ciudad.
  - [Choice]: No.
    - [Menu]: ¿Te gustaría abandonar esta búsqueda de la ciudad?
      - [Choice]: Sí.
        - [Menu]: ¿Estás seguro de que deseas abandonar esta búsqueda de la ciudad?
          - [Choice]: Sí.
            - **Malala:** Es una pena, aunque tal vez alguien más pueda ayudar. espero...
            - (Action: La misión está completa.)
            - Ya está disponible una nueva misión de ciudad Menaphos.
          - [Choice]: No.
            - **Malala:** Es una pena, aunque tal vez alguien más pueda ayudar. espero...
      - [Choice]: No.
        - **Malala:** Es una pena, aunque tal vez alguien más pueda ayudar. espero...

##### Tarea incompleta

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Malala:** ¿Has terminado la tarea de matar a [número] [monster]? ([número] restantes)
    - **Player:** Todavía no. ¿Podrías indicarme la dirección de algún [monster]?
    - (continuea|first)
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

##### Tarea completada

- [Menu]: Selecciona una opción
  - [Choice]: Hable sobre su tarea actual.
    - **Malala:** ¿Has terminado la tarea de matar a [número] [monster]? ([número] restantes)
    - **Player:** Sí, lo he hecho.
    - (receives=Slayer experience)
    - **Malala:** ¡Encantador! Gracias por toda la práctica. No puedo esperar para decirle a más personas que maten cosas.
    - **Malala:** ¡Mucha suerte en el futuro, aventurero!
    - **Player:** ¡Gracias!
    - (receives=a Menaphite gift offering and reputation in their chosen faction)
    - Ya está disponible una nueva misión de ciudad Menaphos.
  - [Choice]: Abandona esta búsqueda de la ciudad.
    - (Action: La misión está completa.)
    - Ya está disponible una nueva misión de ciudad Menaphos.

#### esfuerzo War

- {{transcript missing}}
