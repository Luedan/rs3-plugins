# Kelhar

- **Original Wiki Page**: [Transcript:Kelhar](https://runescape.wiki/w/Transcript%3AKelhar)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|missing dialogue for the other gems}}

### First-time dialogue when interacting with Kelhar or attempting to enter the gemstone cavern

- **Kelhar:** ¡Alto! ¡Hay monstruos peligrosos por delante!
- [Menu]: Selecciona una opción
  - [Choice]: Cuéntame más sobre ellos.
    - (continue|what)
  - [Choice]: ¡Déjame con ellos!
    - (continue|face)

### Main dialogue

- [Menu]: Elige una opción:
  - [Choice]: ¿Qué hay en esa cueva?
    - **Kelhar:** Dentro de esa cueva hay dragones como ninguno que hayas encontrado antes.
    - **Kelhar:** Equipados con gemas, son más fuertes que los dragones normales a los que te hayas enfrentado antes.
    - **Kelhar:** Guardo esta cueva para proteger a aquellos que, de otro modo, entrarían sin darse cuenta.
    - [Menu]: Selecciona una opción
      - [Choice]: Déjame enfrentarlos.
        - **Kelhar:** Sólo te dejaré pasar si un Slayer master te ha indicado que lo hagas... o si estás dispuesto a realizar un pago.
        - **Player:** ¿Cuánto quieres?
        - **Kelhar:** No en tu coins. En gemas.
        - **Player:** Hay joyas a nuestro alrededor. Extraeré un poco y ya vuelvo.
        - **Kelhar:** No. Necesito algunos un poco más preciosos. Tráeme piedra de dragón sin cortar, ónix o un hidrix incompleto y te permitiré entrar. Con cada gema te permitiré matar una cierta cantidad antes de que debas irte.
      - [Choice]: Gracias por hacérmelo saber.
        - (end)
  - [Choice]: ¿Puedo entrar a la cueva?
    - (above|face)
  - [Choice]: Me gustaría hacer un pago para entrar a la cueva.
    - (Condition: If the player has already made the maximum payment:)
      - Ya le has pagado a Kelhar la cantidad máxima de gemas. Mata algunos dragones de piedras preciosas antes de intentar pagar nuevamente.
    - (Condition: If the player does not have acceptable payment and has not made the maximum payment:)
      - Kelhar solo aceptará piedras de dragón sin cortar, ónix y gemas de hidrix incompletas como pago para ingresar a la cueva.
    - (Condition: If the player does have acceptable payment and has not made the maximum payment:)
      - [Menu]: ¿QUÉ GEMA TE GUSTARÍA UTILIZAR COMO PAGO?
        - (Condition: If the player has at least one uncut onyx:)
          - {{Transcript missing}}
        - (Condition: If the player has at least one incomplete hydrix:)
          - {{Transcript missing}}
        - (Condition: If the player has at least one uncut dragonstone:)
          - Piedra de dragón sin cortar (2 muertes por gema)
            - ¿Cuántas gemas te gustaría usar?
            - (el player debe ingresar un número:)
            - (Condition: If the player enters 0:)
              - (end)
            - (Condition: If the player enters any number other than 0:)
              - **Kelhar:** ¡Gracias! Ahora puedes matar un total de dragones de piedras preciosas [número].
        - [Choice]: No quiero pagarte ahora.
          - (end)

### Paying gems

- (above|gems)

### Checking kills

- (Condition: If the player has zero kills remaining:)
  - **Kelhar:** Debes pagarme en gemas sin cortar antes de que te permita ingresar a la mazmorra nuevamente.
- (Condition: If the player has one or more kills remaining:)
  - **Kelhar:** Te permitiré matar otros dragones de piedras preciosas [1-60,000] antes de solicitar más pagos de gemas.
