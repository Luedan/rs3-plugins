# Teddy

- **Original Wiki Page**: [Transcript:Teddy](https://runescape.wiki/w/Transcript%3ATeddy)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{toc}}

### First-time dialogue

- **Teddy:** Hola. Mi nombre es Teodoro. Seré tu asistente hoy.
- **Player:** Eh, Teddy, sé quién eres.
- **Teddy:** No interrumpas, me harás olvidar mis líneas. ¡Y es Teodoro!
- **Teddy:** Explosión. No recuerdo lo que estaba diciendo. Ah, sí... estaba explicando el acto.
- (below|initial-explain)

### Before the performance

*Si el player aún no se ha presentado esta semana:*
- **Teddy:** ¿Quieres comenzar tu actuación de Thieving?
- **Seleccione una opción**
  - si
    - (Action: Player inicia la actuación.)
  - No
    - **Player:** No.
      - *(El diálogo termina.)*
  - ¿Podrías explicármelo de nuevo? {{anchor|explain}}
    - **Player:** ¿Podrías explicármelo otra vez?
    - **Teddy:** Si es necesario.
    - **Teddy:** Para comenzar tu actuación de Thieving, párate sobre la estrella cercana. Al comenzar, se le presentará una lista de trucos que puede realizar.
    - **Teddy:** Cada truco tiene un nivel de dificultad diferente. La calificación sugiere qué skill level tiene más probabilidades de realizar dicho truco. Sin embargo, puedes intentar trucos para los que no tienes nivel.
    - **Teddy:** Finalmente: sólo puedes realizar 5 trucos. Al final se le informará de sus resultados. Puedes realizar emoticones entre trucos para mantener las cosas animadas.
    - **Teddy:** Si deseas terminar tu actuación antes de tiempo, y entendería completamente esa sensación, simplemente háblame.
    - (Condition: First time:)
      - **Teddy:** ¿Te gustaría comenzar tu actuación de Thieving?
    - (Condition: Afterwards:)
      - **Teddy:** ¿Te gustaría comenzar tu actuación de Thieving?
    - **Seleccione una opción**
      - si
        - (Action: Player inicia la actuación.)
      - No
        - **Player:** No.
          - *(El diálogo termina.)*
  - *Uno de:*
    - ¿Puedes decirme cómo estoy? {{anchor|tellme}}
      - **Teddy:** Sí.
        - *(El diálogo termina.)*
    - ¿Podrías dejar de decirme cómo estoy?
      - **Teddy:** Por supuesto. Pero sólo evitará que te informen si eres repetitivo, no sus desagradables gritos generales. ¿Todavía quieres que los calle?
      - **Teddy:** ¿Todavía quieres que los detenga?
      - **Seleccione una opción**
        - si
          - *(El diálogo termina.)*
        - No
          - **Player:** No.
            - *(El diálogo termina.)*

### During the performance

*Al iniciar la actuación:*
- **Teddy:** Si quieres finalizar tu actuación, dímelo o aléjate del área de actuación.
*Si habla con usted durante la actuación:*
- **Teddy:** Tsk, ¿te rindes tan rápido?
- **Seleccione una opción**
  - si
    - (Action: Player finaliza la actuación.)
    - *Si el player anotó puntos en su actuación:*
      - ¡Felicitaciones! Obtuviste una puntuación de [amount] en tu actuación de Thieving. Recibiste puntos de experiencia [amount].
    - *Si el player no obtuvo puntos en su actuación:*
      - **Ringmaster:** Lo siento, pero esa actuación no fue lo suficientemente buena para recibir una recompensa. Vuelve a intentarlo la semana que viene.
      - ¡Ay no! No obtuviste nada en tu actuación de Thieving. Recibiste 0 puntos de experiencia.
  - No
    - **Player:** No.
      - *(El diálogo termina.)*
  - ¿Podrías explicármelo de nuevo?
    - (above|explain)
  - ¿Puedes decirme cómo estoy?
    - (above|tellme)
*Si el player intenta salir del área de actuación:*
- ¿Quieres terminar tu actuación antes de tiempo?
- **Seleccione una opción**
  - si
    - (Action: Player finaliza la actuación.)
    - *Si el player anotó puntos en su actuación:*
      - ¡Felicitaciones! Obtuviste una puntuación de [amount] en tu actuación de Thieving. Recibiste puntos de experiencia [amount].
    - *Si el player no obtuvo puntos en su actuación:*
      - **Ringmaster:** Lo siento, pero esa actuación no fue lo suficientemente buena para recibir una recompensa. Vuelve a intentarlo la semana que viene.
      - ¡Ay no! No obtuviste nada en tu actuación de Thieving. Recibiste 0 puntos de experiencia.
  - No
    - *(El diálogo termina.)*

### After the performance

- **Teddy:** Gracias por completar tu actuación de Thieving. Hable con Ringmaster si necesita más información. Odio este trabajo de espía.
