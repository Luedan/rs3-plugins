# Wizard Taloram

- **Original Wiki Page**: [Transcript:Wizard Taloram](https://runescape.wiki/w/Transcript%3AWizard%20Taloram)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Wizards' Tower

- **Wizard Taloram:** Ahora no. <br>¡Estoy intentando concentrarme en un hechizo muy difícil!
- [Menu]: Elige una opción:
  - [Choice]: ¿Ese es tu demonio?
    - **Wizard Taloram:** ¿Lo convoqué, quieres decir? Ciertamente no, aunque soy el único mago en esta Torre con la experiencia para protegerla y estudiarla.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Cómo llegó aquí entonces?
        - **Wizard Taloram:** Ha estado aquí más tiempo del que nadie recuerda. Me atrevo a decir que algún mago tonto lo invocó mientras se entrometía con fuerzas que no entendían del todo.
        - **Wizard Taloram:** Cada vez que se destruye, reaparece en el mismo lugar, por lo que construimos una sala de contención a su alrededor y lo dejamos allí.
        - (initial|init)
      - [Choice]: Ah, lo siento.
        - (end)
  - [Choice]: cond=After Love Story|No lo hiciste bien contra Zenevivia.
    - **Wizard Taloram:** ¡Bah! Ganamos y nada más importa.
  - [Choice]: Ah, lo siento.
    - (end)
