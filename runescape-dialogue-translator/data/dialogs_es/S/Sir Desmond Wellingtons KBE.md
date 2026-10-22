# Sir Desmond Wellingtons KBE

- **Original Wiki Page**: [Transcript:Sir Desmond Wellingtons KBE](https://runescape.wiki/w/Transcript%3ASir%20Desmond%20Wellingtons%20KBE)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- Seleccione una opción
  - ¿Quién eres?
    - **Sir Desmond Wellingtons KBE:** ¡Sir Desmond Wellingtons, Caballero Comandante de la Orden de los Osos Exploradores e Intendente de la Guardia Real de Queen of Snow a su servicio!
    - Sir Desmond endereza el cuello, en lo que supones sería un saludo si sus cuatro patas no estuvieran siendo utilizadas para estar de pie.
    - **Player:** ¿Y qué trae a un caballero de tu talla a este lugar?
    - **Sir Desmond Wellingtons KBE:** Trabajo importante como siempre. Aquí para traer alegría y buena voluntad en nombre de la Reina. Estamos en tiempos difíciles en este momento, y Su Alteza no quiere darle la espalda a Gielinor. Podría acabar con todos, ¿eh?
    - **Player:** ¡Un sentimiento sorprendentemente cálido de una reina del hielo!
    - **Sir Desmond Wellingtons KBE:** Bueno, en ese sentido, he elaborado planes de batalla para darnos a todos la oportunidad de infundir alegría en los corazones de nuestros compañeros osos. ¡He designado esta Operación Papá Noel Secreto!
    - (initial)
  - ¿Puedes hablarme sobre el Santa Secreto?
    - **Sir Desmond Wellingtons KBE:** ¡Feliz, feliz! Hay dos fases en la Operación Secret Santa. Fase uno: Donar. Las personas amables pueden donar los artículos que tanto les costó ganar a mi cuidado. Los distribuiré en la fase dos. Eso sí, no queremos ningún tatuaje, por lo que hay un valor mínimo de donación. Todo lo que des debe valer al menos 10.000 coins en Grand Exchange. También tengo recompensas especiales para cualquiera que vaya más allá del cumplimiento del deber. Cada día puedo regalarles una lámpara prismática mediana por donaciones por un valor total de 100.000 coins. ¡Si haces esto 15 veces, puedo otorgarte el título de Papá Noel Secreto! También hay honores especiales para cualquiera que done 200.000.000 coins de una sola vez: ¡el título de Top Secret Santa! Fase dos: Regalo. Cualquiera puede pedirme un regalo y seleccionaré aleatoriamente un artículo de mis tiendas para entregárselo. Pero no te pongas codicioso, ¿eh? Sólo te dejaré recibir un regalo una vez cada 2 horas. Ese es el plan. Debería ser un buen momento.
    - (initial)
  - Me gustaría hacer una donación al Santa Secreto.
    - **Sir Desmond Wellingtons KBE:** ¡Qué muy divertido de tu parte, muy divertido de verdad!
    - ((If the player isn't in Ironman Mode:))
      - ((Gift Donation interface opens.))
    - ((If the player is in Ironman Mode:))
      - Como Ironman no puedes participar de la mayor alegría de todas: dar regalos. Todas las donaciones de Ironmen serán destruidas en una explosión controlada de acuerdo con las reglas de enfrentamiento estándar de Ironman. Cualquier residuo restante será destruido en una segunda explosión, más grande. Tu riqueza no se transferirá a otros jugadores, pero podrás recibir títulos cosméticos por tus donaciones y progreso en tareas relacionadas con la pista de yak.
      - ¿Aún te gustaría donar artículos?
        - Sí.
          - ((Gift Donation interface opens.))
        - Sí y no me vuelvas a preguntar.
          - ((Gift Donation interface opens.))
        - No.
          - (end)
  - Me gustaría reclamar un regalo del Papá Noel secreto.
    - **Sir Desmond Wellingtons KBE:** Di tu nombre y rango y comprobaré si tengo algo para ti.
    - ((If the player has not claimed a gift in the last 2 hours:))
      - ((Gift Claim interface opens.))
      - ((If the player walks away or otherwise closes the gift claim interface without taking or banking the gift(s):))
        - {{Colour|#036|WARNING:|#fff9}} Si cierras sesión, los artículos del cofre de recompensas se moverán a tu inventario o banco. Si ambos lugares están llenos, perderás los artículos.
    - *(Si el player ha reclamado un regalo en las últimas 2 horas:)*
      - ((With over an hour of cooldown left:))
        - color=#AE0000
      - ((With between a minute and an hour of cooldown left:))
        - color=#AE0000
      - ((With less than a minute of cooldown left:))
        - color=#AE0000}}
  - ¿Puedes contarme sobre el progreso de mi recompensa diaria?
    - ((Without having reached the daily 100,000 value:))
      - **Sir Desmond Wellingtons KBE:** Debes donar artículos por un valor total de al menos [número] coins para recibir una recompensa diaria. Debes donar lo suficiente para reclamar una recompensa diaria en [número] días más para recibir el título de Secret Santa.
      - (initial)
    - ((Having reached the daily 100,000 value:))
      - **Sir Desmond Wellingtons KBE:** Has donado suficiente riqueza para recibir tu recompensa diaria hoy. Si no lo has recibido de mí, puedes reclamarlo como reclamarías un regalo estándar de Secret Santa.
      - ((Without Secret Santa unlocked:))
        - **Sir Desmond Wellingtons KBE:** Debes donar lo suficiente para reclamar una recompensa diaria en [número] días más para recibir el título de Papá Noel Secreto.
        - (initial)
      - ((With Secret Santa unlocked:))
        - **Sir Desmond Wellingtons KBE:** Has donado artículos de valor suficiente en suficientes días para recibir el título de Papá Noel Secreto.
        - (initial)

### Donate gift

- (above|donate-gift)

### Claim gift

- (above|claim-gift)
