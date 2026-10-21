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
    - (Condition: Si el player ya realizó el pago máximo:)
      - Ya le has pagado a Kelhar la cantidad máxima de gemas. Mata algunos dragones de piedras preciosas antes de intentar pagar nuevamente.
    - (Condition: Si el player no tiene pago aceptable y no ha realizado el pago máximo:)
      - Kelhar solo aceptará piedras de dragón sin cortar, ónix y gemas de hidrix incompletas como pago para ingresar a la cueva.
    - (Condition: Si el player tiene un pago aceptable y no ha realizado el pago máximo:)
      - [Menu]: ¿QUÉ GEMA TE GUSTARÍA UTILIZAR COMO PAGO?
        - (Condition: Si el player tiene al menos un ónix sin cortar:)
          - {{Transcript missing}}
        - (Condition: Si el player tiene al menos un hidrix incompleto:)
          - {{Transcript missing}}
        - (Condition: Si el player tiene al menos una piedra dragón sin cortar:)
          - Piedra de dragón sin cortar (2 muertes por gema)
            - ¿Cuántas gemas te gustaría usar?
            - (el player debe ingresar un número:)
            - (Condition: Si el player ingresa 0:)
              - (end)
            - (Condition: Si el player ingresa cualquier número distinto de 0:)
              - **Kelhar:** ¡Gracias! Ahora puedes matar un total de dragones de piedras preciosas [número].
        - [Choice]: No quiero pagarte ahora.
          - (end)

### Paying gems

- (above|gems)

### Checking kills

- (Condition: Si a el player no le quedan muertes:)
  - **Kelhar:** Debes pagarme en gemas sin cortar antes de que te permita ingresar a la mazmorra nuevamente.
- (Condition: Si a el player le quedan una o más muertes:)
  - **Kelhar:** Te permitiré matar otros dragones de piedras preciosas [1-60,000] antes de solicitar más pagos de gemas.
