# Gamfred

- **Original Wiki Page**: [Transcript:Gamfred](https://runescape.wiki/w/Transcript%3AGamfred)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Gamfred:** Hola. Soy Gamfred, el ingeniero de este gremio. ¿Has visto mi catapulta?
- [Menu]: Selecciona una opción
  - [Choice]: Eso no es una catapulta, es una ballesta grande.
    - **Player:** Eso no es una catapulta, es una ballesta grande.
    - **Gamfred:** ¿¡QUÉ!? ¡Te haré saber que es la mejor pieza de ingeniería enana en kilómetros a la redonda! ¡Cómo te ATREVES a insultar mi trabajo!
  - [Choice]: Sí, hermosa pieza de ingeniería.
    - **Player:** Sí, hermosa obra de ingeniería.
    - **Gamfred:** Encantado de conocer a alguien que aprecia el buen trabajo. ¿Ya lo has probado?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí.
        - **Player:** Sí.
        - **Gamfred:** ¿Qué te pareció?
        - [Menu]: Selecciona una opción
          - [Choice]: Estaba bien, supongo.
            - **Player:** Supongo que estuvo bien.
            - **Gamfred:** Bueno, supongo que no a todos les gustará.
          - [Choice]: ¡Fue divertido!
            - **Player:** ¡Fue divertido!
            - **Gamfred:** Me alegra oírlo. Inténtalo de nuevo alguna vez. Tenemos más pruebas que realizar.
          - [Choice]: No me gustó.
            - **Player:** No me gustó.
            - **Gamfred:** Bueno, supongo que no a todos les gustará. Pero dale otra oportunidad antes de irte.
          - [Choice]: ¿Puedo tener un escudo por favor?
            - **Player:** ¿Puedo darme un escudo, por favor?
            - (Condition: If you do not have the defensive shield:)
              - **Gamfred:** ¡Por supuesto!
              - (receives=defensive shield)
              - [El enano te entrega un gran escudo.]
            - (Condition: If you have the defensive shield:)
              - **Gamfred:** Muffin tonto, ¡ya tienes uno!
      - [Choice]: No, ¿cómo hago eso?
        - **Player:** No, ¿cómo hago eso?
        - **Gamfred:** Bueno, toma el gran escudo de defensa con ambas manos y observa la catapulta. Mi asistente te disparará diferentes cosas y tendrás que defenderte de ellas. Para ver qué se avecina en tu camino y qué modo defensivo elegir, mira el cartel en la pared.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Puedo tener un escudo por favor?
            - **Player:** ¿Puedo darme un escudo, por favor?
            - (Condition: If you do not have the defensive shield:)
              - **Gamfred:** ¡Por supuesto!
              - (receives=defensive shield)
              - [El enano te entrega un gran escudo.]
            - (Condition: If you have the defensive shield:)
              - **Gamfred:** Muffin tonto, ¡ya tienes uno!
          - [Choice]: Suena aburrido.
            - **Player:** Suena aburrido.
            - **Gamfred:** Tu pérdida...
  - [Choice]: ¿Dónde está?
    - **Player:** No, ¿dónde está?
    - **Gamfred:** ¿Eres un muchacho ciego? ¡Está allí, en la habitación de al lado, con mi asistente trabajando!
  - [Choice]: ¡Adiós!
    - **Player:** ¡Adiós!
    - **Gamfred:** ¡Vuelve pronto! Mi catapulta necesita más sujetos de prueba.
