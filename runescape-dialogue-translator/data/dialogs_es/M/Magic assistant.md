# Magic assistant

- **Original Wiki Page**: [Transcript:Magic assistant](https://runescape.wiki/w/Transcript%3AMagic%20assistant)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### First-time dialogue

- **Magic assistant:** ¡Hola! Soy tu asistente para la presentación de Magic. Como es la primera vez, les contaré lo que sucede.
- **Player:** Está bien.
  - (continue|first time)

### Before completing your Magic performance in the circus

- **Magic assistant:** ¿Quieres comenzar tu presentación de Magic?
- **Seleccione una opción**
  - si
    - (end)
  - No
    - **Player:** No.
  - ¿Podrías explicármelo de nuevo?
    - **Player:** ¿Puedes explicármelo otra vez?
    - {{anchor|first time}}**Magic assistant:** Por supuesto que puedo. Hay cuatro tipos de hechizos que puedes realizar. Levitación, teletransportación, alquimia y elemental. El anillo está lleno de animales y accesorios para que puedas realizar hechizos. Sin embargo, ciertos hechizos solo funcionarán con ciertos accesorios y animales. Pruébelos y vea qué sucede. Ah, pero será mejor que te diga que los accesorios y los animales tienen diferentes grados de dificultad, lo que sugiere que el skill level tiene más probabilidades de garantizarte el éxito, pero eres bienvenido a probar el que quieras. Lo último: sólo puedes realizar 10 hechizos. Al final te diré cómo te fue. Ah, y puedes hacer gestos entre movimientos para mantener las cosas frescas. Al público le encanta eso. Sin embargo, no es necesario acelerarlos, la actuación no está cronometrada. Si quieres terminar tu actuación antes, ven a hablar conmigo. Sólo puedes hacer una actuación a la vez.
      - (Inmediatamente después comienza la conversación)
  - *Solo aparecerá una de las siguientes opciones, dependiendo de cuál se haya activado anteriormente:*
    - ¿Podrías decirme cómo estoy?
      - **Magic assistant:** Sí.
    - ¿Podrías dejar de decirme cómo estoy?
      - **Player:** ¿Podrías dejar de decirme qué piensa el público de mi actuación? Es una distracción.
      - **Magic assistant:** Ciertamente puedo. Pero no puedo hacer que dejen de hablarte. Dejaré de decirte si creen que tu actuación es repetitiva o no. ¿Todavía quieres que deje de decírtelo?
        - si
          - (end)
        - No
          - **Player:** No.

### During your Magic performance in the circus

- **Magic assistant:** ¿Quieres terminar tu actuación antes?
- **Seleccione una opción**
  - si
    - *Si el player anotó puntos en su actuación:*
      - ¡Felicitaciones! Obtuviste una puntuación de [amount] en tu actuación de Magic. Recibiste puntos de experiencia [amount].
    - *Si el player no obtuvo puntos en su actuación:*
      - **Ringmaster:** Lo siento, pero esa actuación no fue lo suficientemente buena para recibir una recompensa. Vuelve a intentarlo la semana que viene.
      - ¡Ay no! No obtuviste nada en tu actuación de Magic. Recibiste 0 puntos de experiencia.
  - No
    - **Player:** No.
  - *Solo aparecerá una de las siguientes opciones, dependiendo de cuál se haya activado anteriormente:*
    - ¿Podrías decirme cómo estoy?
      - (arriba)
    - ¿Podrías dejar de decirme cómo estoy?
      - (arriba)

### After your Magic performance in the circus

- **Magic assistant:** Ya hiciste tu presentación de Magic esta semana. Deberías hablar con el maestro de ceremonias y ver si hay algo más que puedas hacer.
