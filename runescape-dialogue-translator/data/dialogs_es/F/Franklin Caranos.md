# Franklin Caranos

- **Original Wiki Page**: [Transcript:Franklin Caranos](https://runescape.wiki/w/Transcript%3AFranklin%20Caranos)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue after Swan Song

- **Franklin Caranos:** Hola de nuevo, Player.
- **Player:** Hola. ¿Cómo va el trabajo de reparación?
- **Franklin Caranos:** Estoy trabajando en ello. Siempre me vendrían bien más láminas de hierro, así que si tienes más, te daré 20 po por lámina.
- **Player:** Gracias, lo recordaré.

### Iron sheet dialogue

- (Condition: If the player has only one iron sheet:)
  - **Franklin Caranos:** Hola de nuevo, Player. ¿Querías venderme esa chapa de hierro? Te daría 20 po por ello.
  - (continue)
- (Condition: If the player has multiple iron sheets:)
  - **Franklin Caranos:** Hola de nuevo, Player. ¿Querías venderme esas láminas de hierro? Te daría [amount] gp.
  - (continue)
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: Sí, eso funcionará muy bien.
    - **Player:** Sí, eso funcionará muy bien.
    - (receives=20 coins per iron sheet) (removes=all iron sheets in inventory)
  - [Choice]: No, preferiría no hacerlo.
    - **Player:** No, preferiría no hacerlo.
    - **Franklin Caranos:** Está bien.
