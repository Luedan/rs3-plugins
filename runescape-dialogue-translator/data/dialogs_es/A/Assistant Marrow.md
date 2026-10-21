# Assistant Marrow

- **Original Wiki Page**: [Transcript:Assistant Marrow](https://runescape.wiki/w/Transcript%3AAssistant%20Marrow)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to option

- **Assistant Marrow:** ¿Quieres usar el globo? Para que lo sepas, algunas ubicaciones requieren logs especiales y altas habilidades de Firemaking.
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - (Acción: abre=Sistema de transporte de globos{{!)Choose Destination}}
  - [Choice]: No.
    - **Player:** No.
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Assistant Marrow:** Soy Assistant Marrow. Trabajo aquí medio tiempo mientras estudio para ser médico.
    - **Assistant Marrow:** ¿Quieres usar el globo?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí.
        - (Acción: abre=Sistema de transporte de globos{{!)Choose Destination}}
      - [Choice]: No.
        - **Player:** No.

### Store logs option

- [Menu]: ¿Darle a Assistant Marrow todo tu logs?
  - [Choice]: Entrega tu logs
  - (Condition: Si el player tiene logs para entregar:)
    - **Assistant Marrow:** ¡Gracias! Ahora tienes cargos [número].
  - (Condition: Si el player no tiene logs para entregar:)
    - **Assistant Marrow:** No tienes ningún logs que pueda almacenar. Tienes cargos [número].
  - [Choice]: Cancelar
    - (end)
