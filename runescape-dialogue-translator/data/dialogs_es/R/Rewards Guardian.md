# Rewards Guardian

- **Original Wiki Page**: [Transcript:Rewards Guardian](https://runescape.wiki/w/Transcript%3ARewards%20Guardian)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Hola.
- **Rewards Guardian:** Saludos. ¿Qué sabiduría buscas?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Rewards Guardian:** ¿Yo? Estoy aquí para otorgarte recompensas por cualquiera de los puntos Pizazz que hayas obtenido en este campo de entrenamiento. Al igual que mis compañeros guardianes, soy parte de la arena y vivo para garantizar su funcionamiento seguro.
    - **Player:** Ya veo.
    - (initial)
  - [Choice]: ¿Puedo canjear mis puntos Pizazz, por favor?
    - **Player:** ¿Puedo canjear mis puntos Pizazz, por favor?
      - (Condition: If the player has a Progress hat with them:)
        - **Rewards Guardian:** Por qué, por supuesto.
        - (opens=Magic Training Arena Shop)
      - (Condition: If the player does not have a Progress hat with them:)
        - **Rewards Guardian:** Lo siento, debes llevar un sombrero de progreso Pizazz para que pueda comprobar qué puntos tienes. Si no tienes uno, habla con mi compañero guardián de abajo.
  - [Choice]: ¿Tiene algo más que pueda comprar?
    - **Player:** ¿Tienes algo más que pueda comprar?
    - **Rewards Guardian:** Bueno, tenemos un libro especial que puede interesarle y que proporciona una guía completa sobre este campo de capacitación. Cuesta 200 po; ¿te gustaría uno?
    - (Condition: If the player already has the book:)
      - **Player:** No gracias, ya tengo uno.
      - **Rewards Guardian:** Avísame si lo pierdes.
    - (Condition: If the player does not have the book:)
      - [Menu]: Selecciona una opción
        - [Choice]: Eso suena útil. Sí, por favor.
          - **Player:** Eso suena útil. Sí, por favor.
          - **Rewards Guardian:** Muy bien, serán 200 po, por favor.
          - (Condition: If the player does not have enough money:)
            - No puedes permitirte eso.
            - **Player:** Lo siento, no tengo suficiente dinero.
          - (Condition: If the player has enough money:)
            - (removes=200 coins) (receives=Arena book)
            - **Rewards Guardian:**Gracias.
        - [Choice]: No quiero un libro viejo y polvoriento.
          - **Player:** No quiero un libro viejo y polvoriento.
          - **Rewards Guardian:** No es viejo y ciertamente no tiene polvo, pero haz lo que quieras.
  - [Choice]: ¡Gracias, adiós!
    - **Player:** ¡Gracias, adiós!
    - **Rewards Guardian:** Usa lo que has aprendido, joven.
