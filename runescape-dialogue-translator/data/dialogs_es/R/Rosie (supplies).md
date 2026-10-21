# Rosie (supplies)

- **Original Wiki Page**: [Transcript:Rosie (supplies)](https://runescape.wiki/w/Transcript%3ARosie%20%28supplies%29)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Rosie (suministros):** ¿Quieres comprar algunos suministros para tu barco? <br/>Necesitarás suministros para viajar en tu barco. Cuanto mayor sea la distancia, más suministros necesitarás.
  - (Condition: Si el player ha comprado la cantidad máxima de suministros:)
    - Ha comprado el máximo de consumibles [X]/[X].
    - ((Repetido en una ventana emergente:))
    - Ha comprado el máximo de consumibles [X]/[X].
  - (Condition: Si el player no ha comprado la cantidad máxima de suministros:)
    - ((Se abre la interfaz de compra de suministros.))
    - Suministros: [X]/[X].<br/> ¿Cuántos suministros desea comprar? <br/> (campanas [X] cada una)
      - (Condition: Si el player ingresa 0:)
        - Introduzca un número mayor que cero.
        - ((Repetido en una ventana emergente:))
        - Introduzca un número mayor que cero.
        - (continuea|buy-supplies)
      - (Condition: Si el player ingresa un número mayor que 0:)
        - Compró [X] [supply/supplies] para timbres [X].
        - Ahora tiene consumibles [X]/[X].
        - ((Repetido en una ventana emergente:))
        - Ahora tiene consumibles [X]/[X].
        - (continuea|buy-supplies)

### Buy 1

- Compró [X] [supply/supplies] para timbres [X].
- Ahora tiene consumibles [X]/[X].
- ((Repetido en una ventana emergente:))
- Ahora tiene consumibles [X]/[X].

### Buy X

- ((Se abre la interfaz de compra de suministros.))
  - Suministros: [X]/[X].<br/> ¿Cuántos suministros desea comprar? <br/> (campanas [X] cada una)
    - (Condition: Si el player ingresa 0:)
      - Introduzca un número mayor que cero.
      - ((Repetido en una ventana emergente:))
      - Introduzca un número mayor que cero.
    - (Condition: Si el player ingresa un número mayor que 0:)
      - Compró [X] [supply/supplies] para timbres [X].
      - Ahora tiene consumibles [X]/[X].
      - ((Repetido en una ventana emergente:))
      - Ahora tiene consumibles [X]/[X].

### Buy All

- (Condition: Si el player ha comprado la cantidad máxima de suministros:)
  - Ha comprado el máximo de consumibles [X]/[X].
  - ((Repetido en una ventana emergente:))
  - Ha comprado el máximo de consumibles [X]/[X].
- (Condition: Si el player no ha comprado la cantidad máxima de suministros:)
  - [Menu]: Confirmar compra: ¿Estás seguro de que deseas comprar [X] [supply/supplies] con timbres [X]?
    - [Choice]: Ok
      - Compró [X] [supply/supplies] para timbres [X].
      - Ahora tiene consumibles [X]/[X].
      - ((Repetido en una ventana emergente:))
      - Ahora tiene consumibles [X]/[X].
    - [Choice]: Cancelar
      - (end)
