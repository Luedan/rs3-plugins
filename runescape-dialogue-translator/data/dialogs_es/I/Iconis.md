# Iconis

- **Original Wiki Page**: [Transcript:Iconis](https://runescape.wiki/w/Transcript%3AIconis)
- **Letter**: `I`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### On free-to-play worlds

- **Iconis:** ¡Buenos días! Me temo que no puedes utilizar los servicios del stand en un mundo que no es miembro. ¡La película cuesta mucho, sabes!

### On members' worlds

- **Iconis:** ¡Buenos días! ¿Quieres que te tomen una foto?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Sí, por favor!
    - **Player:** ¡Sí, por favor!
    - (Condition: If the player hasn't taken a picture in the last two hours:)
      - **Iconis:** ¡Simplemente ingresa a la tienda, ajusta tu ropa y presiona el botón "Tomar foto" cuando estés listo!
      - **Player:** ¡Gracias!
      - (Action: el player entra al fotomatón.)
    - (Condition: If the player has taken a picture in the last two hours:)
      - **Iconis:** Lo sentimos, te han tomado una foto recientemente. Podrás volver a tomarlo en [time remaining].
  - [Choice]: No, gracias.
    - **Player:** No, gracias.
    - **Iconis:** Como desees.
  - [Choice]: ¿Para qué son las fotos?
    - **Player:** ¿Para qué son las imágenes?
    - **Iconis:** El diablillo los envía a una misteriosa red que se puede encontrar más allá de este plano material. Desde allí, otros aventureros podrán verlos para ponerle cara al nombre.
    - **Iconis:** Por ejemplo, se utilizarán para mostrar los rostros de aventureros con grandes logros en el entrenamiento de habilidades.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Cómo funciona?
        - (below|work)
      - [Choice]: ¿Es seguro?
        - (below|safe)
  - [Choice]: ¿Cómo funciona?
    - {{anchor|work}} **Player:** ¿Cómo funciona?
    - **Iconis:** Hay un diablillo ahí dentro que usa un hechizo para tomarte una foto. Sin embargo, por el momento sólo puede hacerlo una vez cada 2 horas y le llevará algún tiempo procesar la imagen. Hay mucha demanda, ¿ves?
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Por qué un diablillo?
        - **Player:** ¿Por qué un diablillo?
        - **Iconis:** ¡Ah, buena pregunta! Mira, he experimentado con muchas formas de hacer representaciones visuales precisas de las cosas de una manera mágica. Más recientemente, he estado intentando modificar los orbes de visión para obtener una imagen fija.
        - **Iconis:** Sin embargo, debido a su forma, ¡siempre hacían que el sujeto pareciera gordo! Entonces se me ocurrió un cubo de visión, ¡pero eso hizo que las cosas parecieran aún peor!
        - **Player:** Entonces, ¿qué hiciste?
        - **Iconis:** Modifiqué y modifiqué la forma hasta que obtuve una imagen decente (me tomó semanas hacerla), pero luego este diablillo se teletransportó de la nada justo al lado. Mi dispositivo de visión cayó al suelo y se hizo añicos.
        - [Menu]: Selecciona una opción
          - [Choice]: ¡Ah, no!
            - **Player:** ¡Oh, no!
            - {{anchor|ohno}} **Iconis:** Efectivamente. Atrapé al culpable en una caja mágica y hablé con él. Parecía bastante confundido porque estaba usando orbes para tomar fotografías. Aparentemente, los diablillos tienen un hechizo bastante útil para eso, ¡así que lo contraté!
            - **Player:** ¿Los diablillos toman fotografías?
            - **Iconis:** Sí. No me reveló el funcionamiento exacto del hechizo, ni siquiera por qué lo hacen, pero el resultado es muy convincente.
            - [Menu]: Selecciona una opción
              - [Choice]: ¿Es seguro?
                - (below|safe)
              - [Choice]: ¿Para qué son las fotos?
                - (above|pictures)
              - [Choice]: Eso es todo, gracias.
                - (abajo)
          - [Choice]: Eso es lamentable.
            - **Player:** Eso es desafortunado.
            - (arriba2|ohno)
  - [Choice]: ¿Es seguro?
    - {{anchor|safe}} **Iconis:** ¡Oh, absolutamente! Yo mismo he probado el procedimiento miles de veces para asegurarme de que sea seguro y de que no haya efectos secundarios.
    - **Player:** ¿Pero están seguras mis pertenencias?
    - **Iconis:** ¡Totalmente! Tengo algunas runas, orbes y baratijas para garantizarlo.
  - [Choice]: Eso es todo, gracias.
    - **Player:** Eso es todo, gracias.
    - **Iconis:** ¡De nada!
