# Sera

- **Original Wiki Page**: [Transcript:Sera](https://runescape.wiki/w/Transcript%3ASera)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### South of Eagles' Peak, without the skill requirements to start The Firemaker's Curse

- Necesitas las siguientes habilidades para comenzar esta misión: 74 Firemaking, 76 Constitution, 64 Agility.
- **Player:** ¿Qué están haciendo todos aquí?
- **Sera:** Alto secreto, amigo mío. Pero quizás cuando tengas más experiencia puedas ayudarnos.
- **Player:** Ya veo.

### Balthazar Beauregard's Big Top Bonanza


#### Diálogo por primera vez

- **Sera:** Me alegro de verte de nuevo, Player.
- **Player:** ¿Qué pasó con superar a Vulcan?
- **Sera:** Oh, decidí dejarle tener su gloria por ahora. Sé que fácilmente tengo la experiencia para superarlo después de nuestra excursión.
- **Sera:** Mientras tanto, yo me encargo de escupir fuego. Déjame darte un resumen de qué hacer.
- **Player:** Está bien.
- (below|explain first)

#### Antes y después de la actuación


##### Si el player aún no se ha presentado esta semana

- **Sera:** ¿Quieres comenzar tu actuación de escupir fuego?
- [Menu]: Selecciona una opción
  - [Choice]: si
    - (Action: Player inicia la actuación.)
  - [Choice]: No
    - **Player:** No.
  - [Choice]: ¿Podrías explicármelo de nuevo?
    - **Player:** ¿Podrías explicármelo otra vez? {{anchor|explain}}
    - **Sera:** Si es necesario.
    - {{anchor|explain first}}**Sera:** He inventado algunas soluciones que te permitirán respirar llamas de diferentes colores.
    - **Sera:** Puedes respirar lo que quieras, pero algunas de las soluciones son más difíciles que otras; He escrito pautas en las botellas.
    - **Sera:** Tienes todo el tiempo que quieras, pero solo puedes realizar 6 colores. Al final te contaré cómo te ha ido.
    - **Sera:** Si no puedes soportarlo y quieres terminar temprano, háblame. Sólo puedes hacer una actuación a la vez.
    - **Sera:** ¿Quieres comenzar tu actuación de escupir fuego?
    - [Menu]: Selecciona una opción
      - [Choice]: si
        - (Action: Player inicia la actuación.)
      - [Choice]: No
        - **Player:** No.
  - [Choice]: *(Si la reacción de la audiencia está desactivada)* ¿Puedes decirme cómo me va? {{anchor|tellme}}
    - **Sera:** Sí.
  - [Choice]: *(Si la reacción de la audiencia está activada)* ¿Podrías dejar de decirme cómo me va?
    - **Sera:** ¡Por supuesto! No dejarán de hablarte, pero dejarán de decirte si creen que estás siendo repetitivo o no.
    - **Sera:** ¿Todavía quieres que los detenga?
    - [Menu]: Selecciona una opción
      - [Choice]: si
        - (end)
      - [Choice]: No
        - **Player:** No.

##### Si el player ya actuó esta semana

- **Sera:** Ya hiciste tu actuación de escupir fuego esta semana. Habla con el maestro de ceremonias para ver si hay algo más que puedas hacer.

#### Durante la actuación


##### Al iniciar la actuación

- **Sera:** Si quieres finalizar tu actuación, dímelo o aléjate del área de actuación.

##### Si se le habla durante la actuación

- **Sera:** ¿Quieres terminar tu actuación antes de tiempo?
- [Menu]: Selecciona una opción
  - [Choice]: si
    - {{anchor|ended}} (Acción: el player finaliza su actuación).
    - (Condition: Si el player anotó puntos en su actuación:)
      - ¡Felicitaciones! Obtuviste una puntuación de [amount] en tu actuación de Firemaking (escupe fuego). Recibiste puntos de experiencia [amount].
    - (Condition: Si el player no obtuvo puntos en su actuación:)
      - **Ringmaster:** Lo siento, pero esa actuación no fue lo suficientemente buena para recibir una recompensa. Vuelve a intentarlo la semana que viene.
      - ¡Oh, no! No obtuviste nada en tu actuación de Firemaking (escupe fuego). Recibiste 0 puntos de experiencia.
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

- **Sera:** ¡Hola!
- **Player:** ¿Qué haces aquí?
- **Sera:** Emmet y yo nos enteramos de la celebración y ¡simplemente no pudimos resistirnos a un enorme fuego resplandeciente!
- **Player:** ¿Qué estás haciendo exactamente?
- **Sera:** Respiración de fuego, que me ayuda a desahogar mi ira.
- (Condition: Si la solución para respirar incendios no ha sido reclamada:)
  - **Player:** ¿Puedo intentarlo?
  - (receives=Fire breathing solution)
  - **Sera:** Claro, toma esta solución para respirar fuego. Quién sabe, es posible que incluso tengas un "talento extraordinario" para ello.
  - **Player:** Gracias; ¿Tienes algún consejo?
  - **Sera:** Se trata de una cosa y es asegurarse de respirar profundamente para tener suficiente aire para respirar con la presión correcta.
- (Condition: Si se ha reclamado la solución para respirar incendios:)
  - **Player:** ¿Tienes más solución para expulsar incendios?
  - **Sera:** Lo siento, no tengo ninguno encima, pero le di algunos suministros a Alice.
  - **Player:** Vale, gracias.

### Wintumber Warmer


#### Antes del evento


##### Habla con

- **Sera:** ¡Hola!
- **Player:** ¿Qué haces aquí?
- **Sera:** ¡Estamos aquí para una celebración y simplemente no pudimos resistirnos a un enorme fuego resplandeciente!
- **Sera:** Aún no hemos empezado, ¡así que vuelve pronto!

##### Respira fuego

- El evento Wintumber Warmer aún no ha comenzado.

#### Durante el evento


##### Habla con

- **Sera:** ¡Hola!
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué estás haciendo aquí?
    - **Player:** ¿Qué haces aquí?
    - **Sera:** Emmet y yo nos enteramos de la celebración y ¡simplemente no pudimos resistirnos a un enorme fuego resplandeciente!
    - **Player:** ¿Qué estás haciendo exactamente?
    - **Sera:** Respiración de fuego, que me ayuda a desahogar mi ira.
    - (initial)
  - [Choice]: Respira fuego.
    - (Action: Player inicia la actividad.)

##### Respira fuego

- (Action: Player inicia la actividad.)

#### Después del evento


##### Habla con

- **Sera:** ¡Hola!
- **Player:** ¿Qué haces aquí?
- **Sera:** Estamos haciendo las maletas después de la celebración de año nuevo{{Sic}}
- **Sera:** ¡Me encantaría volver el año que viene! ¡Esto ha sido muy divertido!

##### Respira fuego

- El evento Wintumber Warmer ha finalizado.
