# Emmett

- **Original Wiki Page**: [Transcript:Emmett](https://runescape.wiki/w/Transcript%3AEmmett)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### South of Eagles' Peak, without the skill requirements to start The Firemaker's Curse

- Necesitas las siguientes habilidades para comenzar esta misión: 74 Firemaking, 76 Constitution, 64 Agility.
- **Player:** ¿Qué están haciendo todos aquí?
- **Emmett:** Alto secreto, amigo mío. Pero quizás cuando tengas más experiencia puedas ayudarnos.
- **Player:** Ya veo.

### Balthazar Beauregard's Big Top Bonanza


#### Diálogo por primera vez

- **Emmett:** Player!
- **Player:** ¿Cómo te va?
- **Emmett:** ¡Es maravilloso!
- **Emmett:** El maestro de ceremonias parecía querer alejarnos de los otros actos; algo sobre la masacre de fuego...
- **Emmett:** ¡Estoy feliz de volver a dirigir el poi de fuego! ¡Déjame mostrarte cómo hacerlo!
- **Player:** Está bien.
- (below|explain first)

#### Antes y después de la actuación


##### Si el player aún no se ha presentado esta semana

- **Emmett:** ¿Quieres comenzar tu actuación de flaming poi?
- [Menu]: Selecciona una opción
  - [Choice]: si
    - (Action: Player inicia la actuación.)
  - [Choice]: No
    - **Player:** No.
  - [Choice]: ¿Podrías explicármelo de nuevo? {{anchor|explain}}
    - **Player:** ¿Podrías explicármelo otra vez?
    - **Emmett:** ¡Por supuesto!
    - {{anchor|explain first}}**Emmett:** Debes pararte en la estrella cercana para comenzar. Cuando estés listo, ¡empieza a girar!
    - **Emmett:** Hay una variedad de trucos que puedes hacer con fire poi, algunos más difíciles que otros. Puedes probar cualquiera que quieras, pero tu skill level determinará cuáles es más probable que puedas completar.
    - **Emmett:** Tienes todo el tiempo que quieras, pero solo puedes realizar 6 trucos. Al final te contaré cómo te ha ido.
    - **Emmett:** Si por alguna razón quieres terminar antes, háblame. Sólo puedes hacer una actuación a la vez.
    - **Emmett:** ¿Quieres comenzar tu actuación de flaming poi?
    - [Menu]: Selecciona una opción
      - [Choice]: si
        - (Action: Player inicia la actuación.)
      - [Choice]: No
        - **Player:** No.
  - [Choice]: *(Si la reacción de la audiencia está desactivada)* ¿Puedes decirme cómo me va? {{anchor|tellme}}
    - **Emmett:** Sí.
  - [Choice]: *(Si la reacción de la audiencia está activada)* ¿Podrías dejar de decirme cómo me va?
    - **Emmett:** ¡Por supuesto! No dejarán de hablarte, pero dejarán de decirte si creen que estás siendo repetitivo o no.
    - **Emmett:** ¿Todavía quieres que los detenga?
    - [Menu]: Selecciona una opción
      - [Choice]: si
        - (end)
      - [Choice]: No
        - **Player:** No.

##### Si el player ya actuó esta semana

- **Emmett:** Ya hiciste tu actuación de fire poi esta semana. Habla con el maestro de ceremonias para ver si hay algo más que puedas hacer.

#### Durante la actuación


##### Al iniciar la actuación

- **Emmett:** Si quieres finalizar tu actuación, dímelo o aléjate del área de actuación.

##### Si se le habla durante la actuación

- **Emmett:** ¿Quieres terminar tu actuación antes de tiempo?
- [Menu]: Selecciona una opción
  - [Choice]: si
    - {{anchor|ended}} (Acción: el player finaliza su actuación).
    - (Condition: Si el player anotó puntos en su actuación:)
      - ¡Felicitaciones! Obtuviste una puntuación de [amount] en tu actuación de Firemaking (poi de fuego). Recibiste puntos de experiencia [amount].
    - (Condition: Si el player no obtuvo puntos en su actuación:)
      - **Ringmaster:** Lo siento, pero esa actuación no fue lo suficientemente buena para recibir una recompensa. Vuelve a intentarlo la semana que viene.
      - ¡Ay no! No obtuviste nada en tu actuación de Firemaking (fire poi). Recibiste 0 puntos de experiencia.
  - [Choice]: No
    - **Player:** No.
  - ¿Podrías explicármelo de nuevo?
    - (above|explain)
  - ¿Puedes decirme cómo estoy?
    - (above|tellme)

##### Si el player intenta salir del área de actuación

- ¿Quieres terminar tu actuación antes de tiempo?
- [Menu]: Selecciona una opción
  - [Choice]: si
    - (above|ended)
  - [Choice]: No
    - (end)

### Celebration of Fire

- **Emmet Logowski:** Hola.
- **Player:** ¿Qué haces aquí?
- **Emmet Logowski:** ¡Sera y yo nos enteramos de la celebración y queríamos unirnos!
- **Player:** ¿Qué estás haciendo exactamente?
- **Emmet Logowski:** ¡El baile del fuego, que por cierto es increíble!
- **Player:** Puedo ver eso...
- **Emmet Logowski:** ¡Bailar con fuego es genial cuando eres parte de un equipo de exhibición!
- **Player:** ...
- **Emmet Logowski:** Podría bailar con fuego todo el día...
- (Condition: Si el poi de fuego no ha sido reclamado:)
  - (receives=fire poi)
  - **Emmet Logowski:** Toma, ten este Poi. Quizás puedas aprender y algún día te convertirás en alguien especial como yo.
  - **Player:** ¡Gracias, lo intentaré!
- (Condition: Si se ha reclamado el poi de fuego:)
  - **Player:** ¿Tienes más Pois?
  - **Emmet Logowski:** Lo siento, no tengo nada conmigo, pero le di algunos suministros a Alice.
  - **Player:** Vale, gracias.

### Wintumber Warmer


#### Antes del evento


##### Habla con

- **Emmet Logowski:** Hola.
- **Player:** ¿Qué haces aquí?
- **Emmet Logowski:** ¡Se acerca el momento de la celebración!
- **Emmet Logowski:** ¡Vuelve pronto y podremos bailar con fuego!

##### Danza del fuego

- El evento Wintumber Warmer aún no ha comenzado.

#### Durante el evento


##### Habla con

- **Emmet Logowski:** Hola.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué estás haciendo aquí?
    - **Player:** ¿Qué haces aquí?
    - **Emmet Logowski:** ¡Sera y yo nos enteramos de la celebración y queríamos unirnos!
    - **Player:** ¿Qué estás haciendo exactamente?
    - **Emmet Logowski:** ¡El baile del fuego, que por cierto es increíble!
    - **Player:** Puedo ver eso...
    - **Emmet Logowski:** ¡Bailar con fuego es genial cuando eres parte de un equipo de exhibición!
    - **Player:** ...
    - **Emmet Logowski:** Podría bailar con fuego todo el día...
    - (initial)
  - [Choice]: Danza con fuego.
    - (Action: Player inicia la actividad.)

##### Danza del fuego

- (Action: Player inicia la actividad.)

#### Después del evento


##### Habla con

- **Emmet Logowski:** Hola.
- **Player:** ¿Qué haces aquí?
- **Emmet Logowski:** ¡Estuve aquí para la celebración de año nuevo!
- **Emmet Logowski:** Aunque eso ya se acabó... así que supongo que iré a bailar con fuego a otro lado.

##### Danza del fuego

- El evento Wintumber Warmer ha finalizado.
