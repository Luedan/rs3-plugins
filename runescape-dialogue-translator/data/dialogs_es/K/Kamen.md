# Kamen

- **Original Wiki Page**: [Transcript:Kamen](https://runescape.wiki/w/Transcript%3AKamen)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### After Underground Pass

- Parece un poco borracho.
- **Kamen:** {{RSChat|Hic!}}
- **Player:** Hola, ¿estás bien?
- **Kamen:** Ooooh, mi cabeza... estoy frita.
- **Player:** ¿Qué pasa?
- **Kamen:** Demasiada de esta cerveza casera, amigo mío. Lo hacemos a partir de raíces de plantas, pero te vuela la cabeza. No querrás ponerlo cerca de llamas desnudas. ¿Quieres un poco?
- [Menu]: Selecciona una opción
  - [Choice]: Bien entonces.
    - **Player:** Está bien, entonces.
    - **Kamen:** Aquí tienes... ¡Hic!
    - **Player:** {{RSChat|Aaarrgghh!}}
    - (Action: el player recibe 50 puntos de daño.)
    - El enano amablemente te da algo de comida para ayudarte a recuperarte de la espantosa bebida.
    - (receives=stew, bread and meat pie)
    - **Kamen:** ¡Ja, ja! Te lo advertí: es algo fuerte. Que tengas una buena comida; puede que te ponga un poco sobrio.
  - [Choice]: No gracias.
    - **Player:** No, gracias.
    - **Kamen:** Tu pérdida... ¡Hic! Bueno, ¿tal vez una buena comida? Podría desprenderme de algo de comida por unos coins.
    - [Menu]: Selecciona una opción
      - [Choice]: Bien entonces.
        - **Player:** Está bien, entonces.
        - **Kamen:** 75 coins por favor.
        - (Condition: Si el player tiene suficiente dinero:)
          - (removes=75 coins)
          - **Player:** Aquí tienes.
          - (receives=stew, bread and meat pie)
          - **Kamen:** Gracias... Come bien.
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Player:** Dios mío, no tengo suficiente dinero...
          - No puedes permitirte eso.
          - **Kamen:** Lo siento, no puedo regalárselo a cualquiera que pase.
      - [Choice]: No gracias.
        - **Player:** No, gracias.
        - **Kamen:** Bueno, vuelve cuando quieras.
