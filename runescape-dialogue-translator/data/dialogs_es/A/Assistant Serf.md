# Assistant Serf

- **Original Wiki Page**: [Transcript:Assistant Serf](https://runescape.wiki/w/Transcript%3AAssistant%20Serf)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{dialogue|npc}}

### Talk-to option

- **Assistant Serf:** ¿Quieres usar el globo? Para que lo sepas, algunas ubicaciones requieren logs especiales y altas habilidades de Firemaking.
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - (Acción: abre=Sistema de transporte de globos{{!)Choose Destination}}
  - [Choice]: No.
    - **Player:** No.
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Assistant Serf:** Soy un siervo. ¡Assistant Serf para ti! Auguste me liberó y me dio este trabajo.
    - **Assistant Serf:** ¿Quieres usar el globo?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí.
        - (Acción: abre=Sistema de transporte de globos{{!)Choose Destination}}
      - [Choice]: No.
        - **Player:** No.

### Store logs option

- [Menu]: ¿Darle a Assistant Serf todo tu logs?
  - [Choice]: Entrega tu logs
  - (Condition: If the player has logs to hand over:)
    - **Assistant Serf:** ¡Gracias! Ahora tienes cargos [número].
  - (Condition: If the player has no logs to hand over:)
    - **Assistant Serf:** No tienes ningún logs que pueda almacenar. Tienes cargos [número].
  - [Choice]: Cancelar
    - (end)
