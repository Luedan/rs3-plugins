# Assistant Le Smith

- **Original Wiki Page**: [Transcript:Assistant Le Smith](https://runescape.wiki/w/Transcript%3AAssistant%20Le%20Smith)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to option

- **Assistant Le Smith:** ¿Quieres usar el globo? Para que lo sepas, algunas ubicaciones requieren logs especiales y altas habilidades de Firemaking.
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - (Acción: abre=Sistema de transporte de globos{{!)Choose Destination}}
  - [Choice]: No.
    - **Player:** No.
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Assistant Le Smith:** Soy Assistant Le Smith. Trabajaba como piloto de planeador, pero me echaron.
    - **Player:** ¿Por qué?
    - **Assistant Le Smith:** Dijeron que estaba demasiado lleno de palabrería.
    - **Assistant Le Smith:** ¿Quieres usar el globo?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí.
        - (Acción: abre=Sistema de transporte de globos{{!)Choose Destination}}
      - [Choice]: No.
        - **Player:** No.

### Store logs option

- [Menu]: ¿Darle a Assistant Le Smith todo tu logs?
  - [Choice]: Entrega tu logs
  - (Condition: If the player has logs to hand over:)
    - **Assistant Le Smith:** ¡Gracias! Ahora tienes cargos [número].
  - (Condition: If the player has no logs to hand over:)
    - **Assistant Le Smith:** No tienes ningún logs que pueda almacenar. Tienes cargos [número].
  - [Choice]: Cancelar
    - (end)
