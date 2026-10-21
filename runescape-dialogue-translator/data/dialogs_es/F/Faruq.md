# Faruq

- **Original Wiki Page**: [Transcript:Faruq](https://runescape.wiki/w/Transcript%3AFaruq)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Al Kharid

- **Faruq:** ¡Hola! ¿Has venido a probar mis maravillosos productos?
- [Menu]: Elige una opción:
  - [Choice]: Sí, me gustaría ver lo que tienes.
    - (opens=Faruq's Tools for Games)
  - [Choice]: Quizás. Tu puesto tiene algunas cosas de aspecto extraño; ¿para qué sirven?
    - **Player:** Quizás. Tu puesto tiene algunas cosas de aspecto extraño; ¿para qué sirven?
    - **Faruq:** Tengo los mejores artículos para aquellos que buscan sus propias cosas que hacer. ¿Quieres verlos?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, por favor.
        - (opens=Faruq's Tools for Games)
      - [Choice]: ¿Pero para qué sirven?
        - **Player:** ¿Pero para qué sirven?
        - **Faruq:** Aunque el mundo tiene muchas cosas que hacer, a algunas personas les gusta jugar sus propios juegos.
        - **Faruq:** Les vendo las herramientas para llevar la cuenta del tiempo, marcar lugares y rutas, decidir las cosas al azar, incluso para realizar grandes votaciones de su grupo.
        - [Menu]: Selecciona una opción
          - [Choice]: Déjame ver entonces.
            - (opens=Faruq's Tools for Games)
          - [Choice]: Estas herramientas, ¿son complicadas?
            - **Player:** Estas herramientas, ¿son complicadas?
            - **Faruq:** No, señor/señora, no son complicados.
            - **Faruq:** Tengo un libro que los explica, si es necesario.
            - (opens=Faruq's Tools for Games)
          - [Choice]: No creo que esto sea para mí.
            - **Player:** No creo que esto sea para mí.
            - **Faruq:** Eso es una pena. Estaré aquí si cambias de opinión.
  - [Choice]: cond=After Carnillean Rising|¿Puedo tener un cofre del tesoro?
    - (Condition: Si el player ya tiene un cofre del tesoro:)
      - **Player:** ¿Puedo tener un cofre del tesoro?
      - **Faruq:** No, solo puedes tener un cofre a la vez. ¿Puedo interesarte en mis otros productos?
      - (previous)
    - (Condition: De lo contrario:)
      - (receives=Treasure chest (Carnillean Rising))
      - [Faruq te regala un cofre del tesoro.]
      - **Faruq:** Ahora, ¿puedo interesarte por mis otros productos?
      - (previous)
  - [Choice]: No, gracias.
    - **Player:** No, gracias.
