# Ranged assistant

- **Original Wiki Page**: [Transcript:Ranged assistant](https://runescape.wiki/w/Transcript%3ARanged%20assistant)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{toc}}

### First-time dialogue

- **Ranged assistant:** Saludos. Soy su asistente para la actuación a distancia. Por razones de seguridad debo explicarles ahora las reglas de la actuación.
  - (continue|first time)

### Before completing your Ranged performance in the circus

- **Ranged assistant:** ¿Entiendes los términos y condiciones y deseas continuar con la presentación de Ranged?
- **Seleccione una opción**
  - si
    - ¿Qué arma te gustaría usar?
      - Arco y flecha
        - (end)
      - arrojar cuchillos
        - (end)
      - arrojar hachas
        - (end)
  - No
    - **Player:** No.
  - ¿Podrías explicármelo de nuevo?
    - **Player:** ¿Puedes explicármelo otra vez?
    - {{anchor|first time}}**Ranged assistant:** Elige el objetivo al que deseas disparar, ya sea la diana o el popinjay, y luego el punto de disparo desde el que intentarás alcanzar el objetivo. Puedes disparar desde cualquier punto de tiro que desees, independientemente de tu nivel Ranged, pero es más probable que aciertes si tienes el nivel Ranged recomendado. Puedes realizar 10 disparos durante la duración de tu actuación. 5 tiros deben ser a la diana y los otros 5 deben ser al popinjay. Una vez realizados 10 tiros, te pediré que desistas, analizaré y te transmitiré tu puntuación. También puede realizar emoticones durante dicha actuación para "animar" dicha actuación. Participa a tu gusto; la actuación no está cronometrada. Si desea finalizar su actuación antes de tiempo, hable conmigo. Sólo podrás realizar una actuación a la vez.
      - (Inmediatamente después comienza la conversación nuevamente con solo las opciones iniciales de sí y no)
  - *Solo aparecerá una de las siguientes opciones, dependiendo de cuál se haya activado anteriormente:*
    - ¿Podrías decirme cómo estoy?
      - **Ranged assistant:** Sí.
    - ¿Podrías dejar de decirme cómo estoy?
      - **Player:** ¿Podrías dejar de decirme qué piensa el público de mi actuación? Es una distracción.
      - **Ranged assistant:** Por supuesto. Sin embargo, no puedo evitar que hablen. Simplemente dejaré de decirte si creen que tu actuación es repetitiva o no. ¿Todavía quieres que deje de decírtelo?
        - si
          - (end)
        - No
          - **Player:** No.

### During your Ranged performance in the circus

- **Ranged assistant:** ¿Deseas finalizar tu actuación antes de tiempo?
- **Seleccione una opción**
  - si
    - *Si el player anotó puntos en su actuación:*
      - ¡Felicitaciones! Obtuviste una puntuación de [amount] en tu actuación de Ranged. Recibiste puntos de experiencia [amount].
    - *Si el player no obtuvo puntos en su actuación:*
      - **Ringmaster:** Lo siento, pero esa actuación no fue lo suficientemente buena para recibir una recompensa. Vuelve a intentarlo la semana que viene.
      - ¡Ay no! No obtuviste nada en tu actuación de Ranged. Recibiste 0 puntos de experiencia.
  - No
    - **Player:** No.

### After your Ranged performance in the circus

- **Ranged assistant:** Ya hiciste tu actuación de Ranged esta semana. Deberías hablar con el maestro de ceremonias y ver si hay algo más que puedas hacer.
