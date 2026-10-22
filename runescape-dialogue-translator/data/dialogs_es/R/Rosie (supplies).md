# Rosie (supplies)

- **Original Wiki Page**: [Transcript:Rosie (supplies)](https://runescape.wiki/w/Transcript%3ARosie%20%28supplies%29)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Rosie (suministros):** ¿Quieres comprar algunos suministros para tu barco? <br/>Necesitarás suministros para viajar en tu barco. Cuanto mayor sea la distancia, más suministros necesitarás.
  - (Condition: If the player has purchased the maximum amount of supplies:)
    - Ha comprado el máximo de consumibles [X]/[X].
    - ((Repeated in a pop-up:))
    - Ha comprado el máximo de consumibles [X]/[X].
  - (Condition: If the player has not purchased the maximum amount of supplies:)
    - ((Purchase supplies interface opens.))
    - Suministros: [X]/[X].<br/> ¿Cuántos suministros desea comprar? <br/> (campanas [X] cada una)
      - (Condition: If the player enters 0:)
        - Introduzca un número mayor que cero.
        - ((Repeated in a pop-up:))
        - Introduzca un número mayor que cero.
        - (continuea|buy-supplies)
      - (Condition: If the player enters a number greater than 0:)
        - Compró [X] [supply/supplies] para timbres [X].
        - Ahora tiene consumibles [X]/[X].
        - ((Repeated in a pop-up:))
        - Ahora tiene consumibles [X]/[X].
        - (continuea|buy-supplies)

### Buy 1

- Compró [X] [supply/supplies] para timbres [X].
- Ahora tiene consumibles [X]/[X].
- ((Repeated in a pop-up:))
- Ahora tiene consumibles [X]/[X].

### Buy X

- ((Purchase supplies interface opens.))
  - Suministros: [X]/[X].<br/> ¿Cuántos suministros desea comprar? <br/> (campanas [X] cada una)
    - (Condition: If the player enters 0:)
      - Introduzca un número mayor que cero.
      - ((Repeated in a pop-up:))
      - Introduzca un número mayor que cero.
    - (Condition: If the player enters a number greater than 0:)
      - Compró [X] [supply/supplies] para timbres [X].
      - Ahora tiene consumibles [X]/[X].
      - ((Repeated in a pop-up:))
      - Ahora tiene consumibles [X]/[X].

### Buy All

- (Condition: If the player has purchased the maximum amount of supplies:)
  - Ha comprado el máximo de consumibles [X]/[X].
  - ((Repeated in a pop-up:))
  - Ha comprado el máximo de consumibles [X]/[X].
- (Condition: If the player has not purchased the maximum amount of supplies:)
  - [Menu]: Confirmar compra: ¿Estás seguro de que deseas comprar [X] [supply/supplies] con timbres [X]?
    - [Choice]: Ok
      - Compró [X] [supply/supplies] para timbres [X].
      - Ahora tiene consumibles [X]/[X].
      - ((Repeated in a pop-up:))
      - Ahora tiene consumibles [X]/[X].
    - [Choice]: Cancelar
      - (end)
