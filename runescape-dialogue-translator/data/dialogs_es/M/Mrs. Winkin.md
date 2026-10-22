# Mrs. Winkin

- **Original Wiki Page**: [Transcript:Mrs. Winkin](https://runescape.wiki/w/Transcript%3AMrs.%20Winkin)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Mrs. Winkin:** Oh, hola, querida. ¿Le puedo ayudar en algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Dónde estamos?
    - **Player:** ¿Dónde estamos?
    - **Mrs. Winkin:** Esta es Winkin's Farm, querida.
    - **Player:** Ah, ya veo. ¿Dónde está entonces el señor Winkin?
    - **Mrs. Winkin:** Oh, se dirigió al mercado hace un tiempo. Cuidaremos la granja mientras él no está.
    - **Mrs. Winkin:** Ahora, ¿había algo más que quisieras?
    - (initial|initial-options)
  - [Choice]: ¿Tienes alguna bandera?
    - **Player:** ¿Tienes alguna bandera?
    - **Mrs. Winkin:** Déjame comprobarlo por ti.
    - (Condition: If it is the first time:)
      - **Farmer Blinkin:** ¡Oh, debes ser nueva, querida! Siempre es bueno ver una cara nueva. Normalmente cobramos por las banderas, ya que muchas se pierden, pero puedes tener el primer juego gratis.
      - **Player:** ¡Vaya, gracias!
      - **Farmer Blinkin:** Ahora, recuerda: si plantas las banderas en cualquier lugar que no tenga semillas, perderás tu bandera, y no es barato volver a comprármelas. Aquí tienes, entonces.
      - (receives=10 flags)
      - **Player:** ¡Muchas gracias! Entonces me voy.
      - **Farmer Blinkin:** Adiós.
    - (Condition: If player has less than 10 flags in the backpack:)
      - **Mrs. Winkin:** ¡Ah! Lo primero es lo primero. Uno de los granjeros te dejó algunas banderas. Puedes recuperarlos. Aquí tienes.
    - (Condition: If player still has less than ten flags in the backpack, substitute [price] with (10 - (# of flags in the backpack) * 500):)
      - **Mrs. Winkin:** Muy bien. Puedes tener un total de 10 banderas. Obtener un conjunto completo de banderas le costará [price] coins. ¿Quieres comprar estas banderas?
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, por favor.
          - **Player:** Sí, por favor.
          - (removes=[price] coins) (receives=[number] flags)
          - **Mrs. Winkin:** Aquí estás, querida.
        - [Choice]: No, gracias.
          - **Player:** No, gracias.
          - **Mrs. Winkin:** Está bien, querida. Adiós.
    - (Condition: If player has 10 flags in the backpack:)
      - **Mrs. Winkin:** Parece que tienes todas las banderas que necesitas. No necesitas comprar más.
    - (Condition: If player ask him for flags for the first time:)
      - **Mrs. Winkin:** ¡Oh, debes ser nueva, querida! Siempre es bueno ver una cara nueva. Normalmente cobramos por las banderas, ya que muchas se pierden, pero puedes tener el primer juego gratis.
      - **Player:** ¡Vaya, gracias!
      - **Mrs. Winkin:** Ahora, recuerda: si plantas las banderas en cualquier lugar que no tenga semillas, perderás la bandera, y no es barato volver a comprarlas. Aquí tienes, entonces.
      - **Player:** ¡Muchas gracias! Entonces me voy.
      - (receives=10 flags)
      - **Mrs. Winkin:** Adiós.
  - [Choice]: ¿Tienes una pala de repuesto?
    - **Player:** ¿Tienes una pala de repuesto?
    - **Mrs. Winkin:** Por qué, por supuesto. Puedo venderte uno por 5 piezas de oro.
      - [Choice]: Bien, gracias.
        - **Player:** Está bien, gracias.
        - (removes=5 coins) (receives=spade)
        - **Mrs. Winkin:** Aquí tienes, entonces.
      - [Choice]: En realidad, he cambiado de opinión.
        - **Player:** En realidad, he cambiado de opinión.
        - **Mrs. Winkin:** Está bien, entonces.
  - [Choice]: ¿Tienes algo para intercambiar?
    - **Player:** ¿Tienes algo para intercambiar?
    - **Mrs. Winkin:** Por supuesto.
    - (opens=Mrs Winkin's World of Seeds)
  - [Choice]: Nada. Estoy bien gracias.
    - **Player:** Nada. Estoy bien gracias.
    - **Mrs. Winkin:** Está bien, querida.
