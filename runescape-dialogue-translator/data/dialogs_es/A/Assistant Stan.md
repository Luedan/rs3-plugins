# Assistant Stan

- **Original Wiki Page**: [Transcript:Assistant Stan](https://runescape.wiki/w/Transcript%3AAssistant%20Stan)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{dialogue|npc}}

### Talk-to option

- **Assistant Stan:** ¿Quieres usar el globo? Para que lo sepas, algunas ubicaciones requieren logs especiales y altas habilidades de Firemaking.
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - (Acción: abre=Sistema de transporte de globos{{!)Choose Destination}}
  - [Choice]: No.
    - **Player:** No.
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Assistant Stan:** Soy Stan. Auguste me contrató para cuidar este globo. Me aseguro de que la gente esté preparada para volar.
    - **Assistant Stan:** ¿Quieres usar el globo?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí.
        - (Acción: abre=Sistema de transporte de globos{{!)Choose Destination}}
      - [Choice]: No.
        - **Player:** No.

### Store logs option

- [Menu]: ¿Darle a Assistant Stan todo tu logs?
  - [Choice]: Entrega tu logs
  - (Condition: Si el player tiene logs para entregar:)
    - **Assistant Stan:** ¡Gracias! Ahora tienes cargos [número].
  - (Condition: Si el player no tiene logs para entregar:)
    - **Assistant Stan:** No tienes ningún logs que pueda almacenar. Tienes cargos [número].
  - [Choice]: Cancelar
    - (end)
